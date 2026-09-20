# reuse-before-build

**让编码 Agent 先复用已有实现、测试资产和工程决策，再开始新工作。**

这是一个 Agent Skill：先检查已有成果和证据，再选择 **Take（直接复用）**、**Borrow（借鉴适配）** 或 **Build（新建）**。缺少关键事实或权限时，明确指出缺口。任务交接或上下文压缩后，它会把历史决策、验证记录与当前代码重新对应起来。

**一个自足的 `SKILL.md`，无需服务，无运行时依赖。**

[English](README.md) · [快速开始](#快速开始) · [示例](#示例) · [工具兼容](docs/compatibility.md) · [验证记录](docs/validation.md)

> **开发预览：** 当前工作副本包含尚未发布的改动。从 GitHub 安装获得的是较早的公开 `main`，并非本轮改造。预览新内容请使用下方的本地安装方式。

## 适合什么任务

| 你的任务 | Skill 检查的已有成果 |
| --- | --- |
| 增加功能 | 已有模块、扩展点、官方方案、合适的依赖库 |
| 增加或修复测试 | 已有 fixture、测试辅助函数、断言、回归用例和执行命令 |
| 接续未完成工作 | 相关决策、来源和历史验证记录，以及记录之后发生的变化 |

历史测试通过，只能证明当时的状态。Skill 会判断记录是否仍适用，并在需要时重跑相关检查。接续恢复限于当前项目的工程任务。

一次小型模拟项目上的实际评估得到以下结果：

```text
任务：补齐重试失败边界的测试。
决策：Borrow，扩展已有测试。
改动：增加 2 个用例，生产代码未变。
验证：4 个测试通过。
```

可检查[实际差异与复核记录](docs/validation.md#inspect-the-behavior-evidence)。这是一次有界评估，不代表普遍成功率。

## 快速开始

### 预览当前工作副本

取得包含本轮修改的完整工作副本。在**另一个需要使用该 Skill 的项目**中打开终端，把下面的来源路径替换为工作副本的绝对路径，然后执行：

```bash
npx skills@1.7.0 add "<absolute-path-to-revised-checkout>" --skill reuse-before-build --agent codex --copy -y
```

该命令安装到当前项目。不要在 Skill 源仓库中执行 `add .`：目标目录位于源目录内部时，安装器可能跳过复制。详见[本地安装说明](docs/compatibility.md#optional-installer)。

可选安装器要求 **Node.js >=22.20.0**，本轮已在隔离的 Windows 环境使用 Node.js 24.18.0 检查安装。使用 Skill 本身不需要 Node.js。详见[安装验证及边界](docs/validation.md)。

若要安装**当前公开版本**，在目标项目中执行：

```bash
npx skills@1.7.0 add Ai-Eastern/reuse-before-build --skill reuse-before-build --agent codex --copy -y
```

Claude Code、Copilot、Cursor、Gemini CLI、OpenCode 和 Windsurf 的目录及验证状态见[兼容说明](docs/compatibility.md)。首次尝试建议采用项目级安装。

### 不使用 Node.js

Agent 只需要 `SKILL.md`；再分发时请同时保留 `LICENSE`。以下命令在目标项目中创建 Codex 项目级安装，请把来源路径替换为修订后工作副本的位置。

**PowerShell**

```powershell
$skillSource = 'C:\path\to\reuse-before-build'
$skillDir = Join-Path (Get-Location) '.agents/skills/reuse-before-build'
New-Item -ItemType Directory -Force -Path $skillDir | Out-Null
Copy-Item -LiteralPath (Join-Path $skillSource 'SKILL.md'), (Join-Path $skillSource 'LICENSE') -Destination $skillDir
```

**POSIX shell**

```sh
skill_source=/path/to/reuse-before-build
mkdir -p .agents/skills/reuse-before-build
cp "$skill_source/SKILL.md" "$skill_source/LICENSE" .agents/skills/reuse-before-build/
```

示例、模板和评估资产都是可选内容，Skill 运行无需读取它们。详见[手动安装和更新](docs/compatibility.md#manual-installation)。

### 第一次使用

在 Agent 中打开目标项目，明确选择或提及 `reuse-before-build`，然后发送：

```text
使用 reuse-before-build 处理这个任务：给已有 HTTP 客户端增加重试支持。
先检查实现、相关测试，以及有关的决策或验证记录。
指出哪些成果可以复用，哪些结论需要重新验证。
修改文件前，先给出复用决策和最小下一步。
```

请把任务替换成你项目中的真实需求。有效结果应引用实际文件或来源、解释选择，并给出针对性的验证步骤。仅输出 `Take` 或 `Build` 不代表 Skill 已正确执行。无法加载时，参照[发现与加载排查](docs/compatibility.md#troubleshooting)。

需要一个小项目来尝试时，可以使用仓库中的 [retry-service fixture](evals/fixtures/retry-service/README.md)，按[评估说明](evals/README.md)准备独立的测试复用或任务接续场景。这些可选检查使用 Node.js 和 Git，使用 Skill 本身无需运行它们。

## 输出是什么

| 决策 | 含义 |
| --- | --- |
| **Take** | 直接使用已有实现或测试资产 |
| **Borrow** | 借鉴有用模式，说明适配边界 |
| **Build** | 检查合理的复用选项后，新建最小可行实现 |
| **Blocked** | 当前决策需要的关键事实缺失或互相矛盾 |
| **Needs human approval** | 已知风险需要 Agent 尚不具备的授权 |

检索从项目内部开始，按任务需要扩展；小改动保持轻量。已有工程记录帮助接续，但记录中的结论必须与当前代码和环境核对。Skill 使用宿主本来具备的文件、检索和测试工具。

## 示例

以下均为**说明性场景**，不表示其中描述的系统或测试已经实际运行：

- [复用已有 HTTP 客户端](examples/take-example.md)
- [扩展本地队列及其测试](examples/borrow-example.md)
- [补齐缺失的领域判断](examples/build-example.md)
- [处理缺失证据](examples/blocked-example.md)
- [识别需要授权的风险](examples/needs-approval-example.md)

下面两份说明对应可运行的小项目与已记录的评估：

- [复用测试资产](examples/test-reuse-example.md)
- [从工程记录接续任务](examples/resume-example.md)

可运行检查、实际结果及其限制见[验证说明](docs/validation.md)。工具官方文档、安装成功和 Agent 行为验证分别记录，不混为一种兼容承诺。

## 范围与限制

这是指令工作流，执行效果取决于宿主和模型。它不增加工具、不提供运行时强制拦截，也不保证节省成本。外部检索使用 Agent 原本具备的网络或搜索能力；证据检查不能替代安全或法律审查。

Skill 复用、恢复当前任务需要的工程信息，不索引无关对话，不管理全局记忆库。它保留用户任务和已有授权边界；安装 Skill 不会获得额外权限。

## 贡献与许可

欢迎提交可复现的决策失败案例、安装修正和工具验证记录。请附上 Skill 修订、宿主与模型版本、操作系统、任务、预期行为和脱敏结果。核心 Skill 应保持自足、与宿主无关，兼容性主张需要证据。

采用 [MIT](LICENSE) 许可。再分发时请保留版权和许可声明。
