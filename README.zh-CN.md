![在已有成果上继续构建：复用代码、测试和工程决策。](assets/readme-banner.svg)

<h1 align="center">reuse-before-build</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-0969da?style=flat-square&amp;labelColor=24343b" alt="License: MIT"></a>
  <a href="https://agentskills.io/specification"><img src="https://img.shields.io/badge/Agent%20Skills-SKILL.md-2f6b4f?style=flat-square&amp;logo=markdown&amp;logoColor=white&amp;labelColor=24343b" alt="Agent Skills format: SKILL.md"></a>
  <a href="https://github.com/Ai-Eastern/reuse-before-build/commits/main/"><img src="https://img.shields.io/github/last-commit/Ai-Eastern/reuse-before-build/main?style=flat-square&amp;labelColor=24343b&amp;color=2f6b4f" alt="Last commit on public main"></a>
</p>

<p align="center"><strong>发现已有实现，复用代码与测试，带着证据接续任务。</strong></p>
<p align="center">一个 Skill 文件夹 · 无需服务 · 无运行时依赖</p>

[English](README.md) · [安装](#安装) · [试用](#试用) · [实际结果](#实际结果) · [工具兼容](docs/compatibility.md) · [MIT 许可](LICENSE)

这是一个 Agent Skill，让编码 Agent **动手之前先找已有成果**：先查项目本身、标准库和已安装的依赖；仍有实质缺口时，再查 GitHub 和官方来源。然后依据实际读过的代码决定 **Take（直接复用）、Borrow（借鉴适配）还是 Build（自行补齐）**，而不是依据搜索摘要或记忆。

它针对三种事后要付代价的习惯：已有辅助函数却再写一个；新增的测试没有验证任何新东西；推荐一个没人读过代码和许可证的库。

## 用起来有什么不同

**已被覆盖的行为。** 同一任务、同一练习项目，分别在不加载和加载 Skill 时观察（GPT-5.6 Luna，2026-09-21；[报告](evals/results/2026-09-21/luna-search-timing/REPORT.md)）：

```text
要求      确保 retry 首次成功时立即返回、不再调用 operation，保持生产代码不变。
不加载    修改测试文件来"强化"首次成功的用例：产生了改动，但没有新增覆盖。
加载后    指出现有断言 seen == [1] 已经证明只调用一次，不改任何文件，并运行现有测试。
```

**为新设计选组件**（流程示意）：

```text
要求      为新服务设计持久化 webhook 投递。
发现      在 GitHub 和官方仓库查找已有实现。
检查      在固定版本上阅读核心代码、失败语义、测试和许可证。
决策      直接复用已核实的核心，借鉴适用的模式，只补缺失部分。
交付      说明这些选择如何影响架构，未核实的候选明确标出。
```

参见[架构示例](examples/architecture-reuse-example.md)。只要求设计时，交付物就是设计，不代表授权安装依赖或编写代码。

## 何时使用

- **适合：** 选择架构、库或组件；实现可能已经存在的功能或辅助函数；新增或检查测试；从交接记录或检查点接续工程任务。
- **不需要：** 改错别字、重命名等小的本地改动。Skill 只会对它们做简短的本地检查。
- **如何调用：** 在请求里提到 `reuse-before-build`。能自动选择 Skill 的宿主也可能在任务匹配时自动加载；第一次使用时建议明确点名，确认它已加载。

## 安装

要安装的是 [`skills/reuse-before-build`](skills/reuse-before-build/SKILL.md) 文件夹：`SKILL.md`、按需读取的 `references/` 和 `LICENSE`。请复制整个文件夹。

**Claude Code，对所有项目生效：**

```bash
git clone --depth 1 https://github.com/Ai-Eastern/reuse-before-build.git /tmp/reuse-before-build
```

```bash
cp -R /tmp/reuse-before-build/skills/reuse-before-build ~/.claude/skills/
```

只想对单个项目生效时，改为复制到该项目的 `.claude/skills/`。

**用 skills CLI 安装到 Codex、Claude Code 或其他 Agent**（在你的项目目录下执行）：

```bash
npx skills@1.7.0 add Ai-Eastern/reuse-before-build --skill reuse-before-build --agent codex --copy -y
```

把 `codex` 换成 `claude-code` 或其他 Agent 名称即可。这个 CLI 需要 Node.js ≥22.20.0，Skill 本身不需要。手动复制、PowerShell 命令和其他工具的目录，见[兼容指南](docs/compatibility.md#manual-installation)。

## 试用

```text
使用 reuse-before-build，给已有 HTTP 客户端增加重试支持。
先检查已有代码、测试和相关决策。
修改前说明：哪些成果可以复用、哪些结论需要验证，以及最小下一步。
```

如果当前任务是架构设计：

```text
使用 reuse-before-build，为新项目设计持久化 webhook 投递。
现有成果不足时，查找 GitHub 和官方仓库中的实现。
说明哪些可以直接复用、借鉴适配或自行补齐，以及它们如何影响架构。
本次只做设计，不安装依赖或编写实现代码。
```

好的回答会引用它实际读过的文件或来源，并解释为什么这样选。想先练手，可以用仓库里的 [retry-service 练习项目](evals/fixtures/retry-service/README.md)。加载不了时，参照[排查说明](docs/compatibility.md#troubleshooting)。

## 工作方式

**先找已有成果 → 核对是否真正适用 → 选择最小范围 → 验证。**

| 决策 | 何时 | 接下来做什么 |
| --- | --- | --- |
| **Take · 直接复用** | 已有成果已经满足需求 | 直接使用，并运行相关检查 |
| **Borrow · 借鉴适配** | 已有代码、测试或模式稍加调整即可适用 | 说明复用了什么，做最小改动 |
| **Build · 自行补齐** | 检索后没有合理可用的方案 | 只补缺失部分，并记录否决的选项 |
| **Blocked · 受阻** | 决策依赖的事实无法获得 | 说明缺什么，继续做不受影响的工作 |
| **Needs human approval · 需要批准** | 下一步超出你已授权的范围 | 准备好方案，先征求同意 |

- **投入随事件而定。** 先做本地检查。只有出现真实的能力或兼容性缺口才做外部检索；新会话、新文件或测试失败，本身都不是重新检索的理由。
- **凭证据，不凭印象。** 采用外部库之前，Agent 会固定一个版本，读它的清单、许可证、实现，以及一个测试或调用位置。没能完整读到的候选，一律标为"未核实"。
- **先用现有测试。** 先读现有的测试运行器和断言，只为真实缺口扩展测试，已覆盖的行为不重复加测试。新测试的输入要能区分正确结果和看似合理的错误结果。
- **带着证据接续。** 交接记录或旧的测试日志只是需要和当前工作区核对的说法，不能授予新的权限。参见[检查点说明](skills/reuse-before-build/references/checkpoints.md)。

规则写在 [`SKILL.md`](skills/reuse-before-build/SKILL.md) 中。只在特定情况下才需要的细节，比如检查外部候选、编写检查点，放在 [`references/`](skills/reuse-before-build/references/external-candidates.md) 里。

## 实际结果

| 检查内容 | 观察到的结果 | 详情 |
| --- | --- | --- |
| 重构版与 V13 对比：Claude Opus 5.5，2026-10-11 | 8 个场景共 17 次运行，两个版本通过了全部检查，包括 V12 在 Codex 上失败过的“只有响应头”场景。证据完整时，重构版仍会作出采用决定，而不是一律阻止。耗时和 token 没有可测的差异。 | [报告](evals/results/2026-10-11/claude-restructure/REPORT.md) |
| 与精简类 Skill（`ponytail`）组合使用：GPT-6 Luna / high，2026-09-26，V13 | 8 个显式组合案例全部满足限定标准：复用了已有测试和代码，补充了真实缺口，没有新增重复实现或第二套测试运行器。部分验证命令有重复。 | [报告](evals/results/2026-09-26/skill-combination/REPORT.md) |
| 在 Codex 应用中自然加载：GPT-6 Luna / high，2026-09-26，V10–V12 | 大多数目标案例中 Skill 能原生加载。**已知弱点：** 只有响应头可用时，V12 仍有 2/3 的运行采用了候选（不加载 Skill 的对照组也是 2/3）。 | [报告](evals/results/2026-09-26/native-host/REPORT.md) |
| 核心场景：GPT-6 Luna / high，2026-09-26，V10 | 16 个新上下文场景满足限定标准，包括复用测试、补测能抓住故意植入的缺陷、识别过期结果、核对交接权限。 | [报告](evals/results/2026-09-26/luna6-independent/REPORT.md) |
| 候选检查：GPT-5.6 Luna / medium，2026-09-26 | 11 次运行。固定版本的源码和许可证读取有所改善；真实设计中的测试佐证仍不完整。 | [报告](evals/results/2026-09-26/evidence-gate/REPORT.md) |
| 检索时机与测试复用：GPT-5.6 Luna / medium，2026-09-21 | 17 次运行，含不加载 Skill 的对照组。加载 Skill 后，充分的现有测试被直接复用而不改文件，新断言能抓住故意写错的实现；两次架构试跑仍跳过了源码和许可证检查。 | [报告](evals/results/2026-09-21/luna-search-timing/REPORT.md) |

每一行都是单一宿主和模型上的小样本，不是成功率。方法、文件哈希和保留的失败记录见[验证说明](docs/validation.md)。

## 与其他 Skill 配合使用

与 `ponytail` 等精简类 Skill 同用时，共享一次复用决策和一套验证计划；已有测试足够就直接使用；精简实现时不丢掉必要的证据。详见[协作规则](docs/compatibility.md#combining-workflow-skills)。

已整理 **Codex、Claude Code、GitHub Copilot CLI、Cursor、Gemini CLI、OpenCode 和 Windsurf** 的安装路径。[兼容指南](docs/compatibility.md)逐项区分了"文档支持"和"实际观察到的行为"。

## 示例与贡献

- **从具体任务开始：** [为架构发现已有实现](examples/architecture-reuse-example.md)、[复用代码](examples/take-example.md)、[适配代码](examples/borrow-example.md)、[补齐实现](examples/build-example.md)、[复用测试](examples/test-reuse-example.md)、[接续工作](examples/resume-example.md)。
- **了解决策边界：** [证据不足](examples/blocked-example.md)、[授权边界](examples/needs-approval-example.md)。这些是说明性示例，实际运行记录见上方。
- **帮助改进：** [提交可复现案例](https://github.com/Ai-Eastern/reuse-before-build/issues/new/choose)、验证一种工具，或[运行评估](evals/README.md)。请附上修订、宿主与模型、任务、预期结果和脱敏证据。

<details>
<summary>范围与限制</summary>

这是指令工作流，效果取决于宿主和模型。它不增加工具、不提供运行时强制拦截，也不保证降低成本。外部检索需要 Agent 已有的网络能力；证据检查不能替代安全或法律审查。

接续只覆盖当前任务的工程状态，不索引无关对话、不提供全局记忆、不授予额外权限。示例和评估资产均为可选；Skill 本身就是 [`skills/reuse-before-build`](skills/reuse-before-build/SKILL.md) 文件夹。

</details>

[MIT](LICENSE) · 再分发时请保留版权和许可声明。
