建议首轮验证采用 **pg-boss 12.33.2 + 已有 PostgreSQL + 独立 Node.js worker 进程**。队列库负责持久化、延迟领取、重试和任务状态；业务负责输入契约、逻辑操作的幂等性及外部副作用确认。本次是源码支持的架构建议，**没有安装依赖、连接数据库或运行集成测试**。

**Reuse Decision：Take。** 范围是复用队列执行基础设施，采用前执行下述验证；不表示集成已经通过。应用目录初始仅有指定的 SKILL.md，没有可复用应用、测试或已安装依赖。检索顺序为本地目录 → Node/PostgreSQL 原生能力 → 本地依赖缺位 → 外部候选。初筛 3 个候选，仅深入 pg-boss 和 Graphile Worker；未读取父仓库及其评审材料。

| 候选 | 实际查到的适配证据 | 取舍 |
| --- | --- | --- |
| **pg-boss 12.33.2，首选** | npm gitHead 对应 `8daa8ea242b6df327fa9514766bd5574df1c3e72`；包要求 Node ≥22.12.0，README 要求 PostgreSQL ≥13；核心 LICENSE 为 MIT。源码实现到期筛选、SKIP LOCKED 领取、有限重试与带随机扰动的指数退避；事务 worker 可把 handler 数据库写入和任务完成一起提交。 | 对当前普通 Node 服务提供直接的队列与事务边界；复用核心库即可。保留版本锁定，目标 PostgreSQL 版本与 Node 22 小版本尚待确认。 |
| **Graphile Worker 0.18.0，备选** | gitHead 对应 `4cda192c5df254392a1dff350e5d73f7d2c18a85`；包及当前官方文档要求 Node ≥22.18.0，文档要求 PostgreSQL ≥12；核心 LICENSE.md 为 MIT。源码使用 run_at、SKIP LOCKED、locked_by/locked_at，失败更新下一次 run_at。 | 已有 SQL 触发器/数据库内投递体系时更值得优先考虑；本项目没有这项既有优势。job_key 是调度更新/合并机制，不能充当永久业务幂等记录。 |
| **BullMQ 6.3.8，保留候选** | npm 元数据与官方文档已出现 PostgreSQL backend，入口为 createPostgresBackend；文档要求 PostgreSQL ≥13，显式迁移，连接池之外还有 LISTEN 连接。 | **不能以“必须 Redis”排除。** 此轮只做元数据及官方文档筛选，未深查该后端源码、测试及核心许可证；不作为已验证可采纳组件。已有 BullMQ API 资产时再深入，当前没有迁移收益。 |

版本与来源：[pg-boss 包契约](https://github.com/timgit/pg-boss/blob/8daa8ea242b6df327fa9514766bd5574df1c3e72/package.json)、[要求](https://github.com/timgit/pg-boss/blob/8daa8ea242b6df327fa9514766bd5574df1c3e72/README.md)、[核心许可](https://github.com/timgit/pg-boss/blob/8daa8ea242b6df327fa9514766bd5574df1c3e72/LICENSE)；[Graphile 包元数据](https://registry.npmjs.org/graphile-worker/0.18.0)、[要求](https://worker.graphile.org/docs/requirements)、[核心许可](https://github.com/graphile/worker/blob/4cda192c5df254392a1dff350e5d73f7d2c18a85/LICENSE.md)；[BullMQ PostgreSQL 官方说明](https://docs.bullmq.io/guide/postgresql)。两个深入候选的对应提交日期分别为 2026-09-18、2026-09-08，说明此快照有近期维护活动，不构成响应时效或稳定性保证。未完成传递依赖许可审计。

Node timers 只提供进程内回调，且不保证精确触发时间；PostgreSQL 原生 SKIP LOCKED 适合多消费者领取，但不足以单独提供完整重试、恢复和运维协议。因此没有证据支持自建完整队列的必要性。[Node 22.18 timers](https://nodejs.org/download/release/v22.18.0/docs/api/timers.html)、[PostgreSQL 18 SELECT](https://www.postgresql.org/docs/18/sql-select.html)

**建议的组件边界如下。**

| 边界 | 责任及最小实现 |
| --- | --- |
| 生产者 / 业务事务 | 生成稳定的 operationId、任务类型、payloadVersion、业务对象 ID 和执行时间。业务变更与 pg-boss.send 使用**同一数据库、同一个事务连接**；另开连接投递不满足原子性。复用库的 db 适配入口，不手写库内部表。该队列记录可承担本地事务 outbox 的职责，初期无须再加一张中转表和转发服务。 |
| pg-boss 队列核心 | 独立 schema 管理队列状态；使用 startAfter，明确 retryLimit、retryDelay、retryBackoff、retryDelayMax 和过期/保留策略；多进程 work 消费。按任务类别分有限数量的队列，先以单任务批次便于隔离失败。队列去重策略只优化调度，不承担永久业务去重。 |
| 数据库任务 handler | 对短时、纯数据库任务，复用 transactional: true，所有业务 SQL 使用回调给出的 tx，连同 completion 一起提交。对业务 operationId 仍施加唯一约束/幂等记录，避免“同一业务操作被重复投递成不同任务”导致重复效果。 |
| 外部副作用 handler | 通过业务适配器调用下游；稳定幂等键与请求内容指纹写入本地效果记录，重试使用原键。调用返回后保存外部回执；超时未知进入查询/对账路径。HTTP 等外部调用不放在长数据库事务里。 |
| 部署与运维 | API 与 worker 可复用同一构建产物，分别启动和扩容；发布步骤管理队列 schema 迁移，运行账号权限按实际 SQL 需求最小化。复用队列失败记录/死信能力，补充指标与受控重放流程。不要先增加通用调度服务、工作流引擎或多后端抽象。 |

这些边界来自实际接口和执行路径：适配器测试用公开 send(..., { db }) 验证事务回滚后任务不存在；manager 的事务路径先领取任务，再开始 handler 事务，调用 completion 后 commit，异常先 rollback 再 fail；plans 以数据库时间筛选到期任务，并以 SKIP LOCKED 领取。[投递事务断言](https://github.com/timgit/pg-boss/blob/8daa8ea242b6df327fa9514766bd5574df1c3e72/test/adapterTest.ts#L427)、[事务执行路径](https://github.com/timgit/pg-boss/blob/8daa8ea242b6df327fa9514766bd5574df1c3e72/src/manager.ts#L537)、[领取及重试 SQL](https://github.com/timgit/pg-boss/blob/8daa8ea242b6df327fa9514766bd5574df1c3e72/src/plans.ts#L1788)

**“避免重复业务副作用”需要按效果位置定义保证。**

- 仅在同一 PostgreSQL 中的效果：幂等键唯一约束、业务写入、处理结果处于同一事务；若采用事务 worker，再与 completion 一并提交。冲突时确认既有操作的请求指纹一致；已成功可返回先前结果，不重复写业务状态。幂等记录保留期覆盖自动重试、人工重放及业务去重窗口。
- 涉及外部系统：库可能在“外部已成功、任务完成尚未提交”后重试。需要下游支持幂等键，或能按业务键可靠查询、确认效果；确认其键作用域、有效期和重复请求内容规则。唯一的本地记录本身无法关闭跨系统提交窗口。
- 下游不支持幂等或可靠结果查询时，不能同时承诺失败后自动重试不丢任务且外部绝不重复。该类任务保留 unknown 状态并人工确认/补偿，产品需接受对应限制；不能把队列 README 的 exactly-once 字样当作跨系统保证。
- 超时、心跳过期或强制关闭后旧 handler 可能仍在执行；业务幂等性必须承受重叠尝试，不能只依赖“当前只有一个 worker”。延迟时间是最早可领取时间，实际完成时间仍受轮询、积压和执行耗时影响。

pg-boss 的现有 retryTest 明确断言：任务未完成且过期后，可再次领取**同一个 ID**。这直接要求 handler 能安全重试。Graphile 官方亦说明任务成功后删除记录，job_key 不形成永久日志，正在运行的同 key 任务可能导致新任务另行排队。[重投递测试](https://github.com/timgit/pg-boss/blob/8daa8ea242b6df327fa9514766bd5574df1c3e72/test/retryTest.ts#L9)、[Graphile job_key 边界](https://worker.graphile.org/docs/job-key)

**运维取舍与尚缺参数。** 复用现有 PostgreSQL 降低服务种类，但任务写入、WAL、vacuum、连接与业务查询争用同一资源，数据库故障同时影响入队和消费。先限制每进程并发与连接池，并给控制/完成/心跳查询保留余量；重试采用退避、上限和死信处置，避免故障放大。任务保留策略须覆盖最长延迟加重试周期。指标至少包括可执行队列最老等待时间、执行耗时、失败/重试/死信数、活跃任务、数据库连接等待与表膨胀。业务量、任务时长、可接受延迟、最长延迟窗口、数据库实际版本和下游能力均未知，所以本次不承诺吞吐数字、恢复秒数或精确并发配置。

**后续验证计划（全部未执行）。**

| 验证范围 | 复用的现有证据 / 后续断言 |
| --- | --- |
| 版本与启动 | 锁定包版本、实际 Node 22 小版本、目标 PostgreSQL 主版本及模块方式；在隔离测试库验证迁移、权限、启动/停止、连接池配置和后续升级。不要把最低数据库版本当作仍受运维支持的建议版本。 |
| 原子入队 | 借用 adapterTest 的成功/回滚断言，换成实际数据库驱动；覆盖业务事务提交、回滚和连接中断。验收：业务与任务同时存在或同时不存在，重试入口不产生重复逻辑操作。 |
| 延迟与重试 | 复用 delayTest、retryTest 的 TestClock 与断言；覆盖未来执行时间、进程重启后持久性、UTC/时区、有限重试、退避范围、终态/死信。验收：不提前执行，达到上限后停止自动业务尝试。 |
| 多 worker 与崩溃 | 在真实目标 PostgreSQL 启动至少 2 个独立 worker 进程，统计领取和业务效果；在领取后、事务中、事务提交前后杀进程，并测试超时旧 handler 仍存活。验收：任务不静默丢失，重试有界，同一 operationId 的业务效果只有一份。已检查的 multiMasterTest 只覆盖并发启动/迁移，**不把它当作跨进程业务去重测试**。 |
| 事务 worker | 复用 transactionalWorkTest 中提交写入、抛错回滚、回滚后重试计数、进入死信的断言；补真实驱动、超时及数据库重连验证。纯数据库效果与 completion 要原子，连接不可泄漏。 |
| 外部副作用 | 先用可控制响应的下游测试替身，模拟“已受理后断连接”、重复投递、并发、回执写入失败、幂等键过期；再在下游真实测试环境验证协议。验收按对方回执/操作记录计数，不能只看本地 handler 调用次数。 |
| 容量及运维 | 用真实 payload、任务时长、延迟任务存量与突发量测队列 p95/p99 延迟和业务查询影响；演练失联、停机排空、失败重放、清理和升级。通过双方确定的 SLO 后再定并发、保留时间与容量。 |

现有测试只是**阅读源码和断言**：没有运行、没有复用历史通过结果。参考入口为 pg-boss 的 package.json 中 npm test（含 pretest）和 npm run cover；后续执行须使用隔离库，先核查 test/hooks.ts 与 test/testHelper.ts 的数据库创建/清理范围，不能直接套到现有生产库。已深入阅读的断言见 [delayTest](https://github.com/timgit/pg-boss/blob/8daa8ea242b6df327fa9514766bd5574df1c3e72/test/delayTest.ts)、[retryTest](https://github.com/timgit/pg-boss/blob/8daa8ea242b6df327fa9514766bd5574df1c3e72/test/retryTest.ts)、[transactionalWorkTest](https://github.com/timgit/pg-boss/blob/8daa8ea242b6df327fa9514766bd5574df1c3e72/test/transactionalWorkTest.ts)。Graphile 对比阅读了 [领取 SQL](https://github.com/graphile/worker/blob/4cda192c5df254392a1dff350e5d73f7d2c18a85/src/sql/getJobs.ts)、[失败 SQL](https://github.com/graphile/worker/blob/4cda192c5df254392a1dff350e5d73f7d2c18a85/src/sql/failJobs.ts) 与 [jobKey/runAt 断言](https://github.com/graphile/worker/blob/4cda192c5df254392a1dff350e5d73f7d2c18a85/__tests__/workerUtils.addJob.test.ts)。

来源访问没有阻断本次结论。Node 的 latest-v22.x 文档入口经浏览工具访问失败，已改用官方 v22.18.0 固定文档成功读取。npm/GitHub 原始来源可读；包下载产物与 gitHead 的一致性、签名和运行时兼容性未验证。完整来源、实际检查与未知项记录在同目录 [architecture-sources.json](architecture-sources.json)。本次仅新增 result.md 与 sources.json。
