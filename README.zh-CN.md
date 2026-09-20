![在已有成果上继续构建：复用代码、测试和工程决策。](assets/readme-banner.svg)

<h1 align="center">reuse-before-build</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-0969da?style=flat-square&amp;labelColor=24343b" alt="License: MIT"></a>
  <a href="https://agentskills.io/specification"><img src="https://img.shields.io/badge/Agent%20Skills-SKILL.md-2f6b4f?style=flat-square&amp;logo=markdown&amp;logoColor=white&amp;labelColor=24343b" alt="Agent Skills format: SKILL.md"></a>
  <a href="https://github.com/Ai-Eastern/reuse-before-build/stargazers"><img src="https://img.shields.io/github/stars/Ai-Eastern/reuse-before-build?style=flat-square&amp;logo=github&amp;logoColor=white&amp;labelColor=24343b&amp;color=9a6700" alt="GitHub stars"></a>
  <a href="https://github.com/Ai-Eastern/reuse-before-build/commits/main/"><img src="https://img.shields.io/github/last-commit/Ai-Eastern/reuse-before-build/main?style=flat-square&amp;labelColor=24343b&amp;color=2f6b4f" alt="Last commit on public main"></a>
</p>

<p align="center"><strong>复用已有代码，扩展现有测试，带着证据接续任务。</strong></p>
<p align="center">一个自足的 <code>SKILL.md</code> · 无需服务 · 无运行时依赖</p>

[English](README.md) · [快速开始](#快速开始) · [工作方式](#工作方式) · [实际结果](#实际结果) · [工具兼容](docs/compatibility.md) · [MIT 许可](LICENSE)

让编码 Agent 在实现前，先找到已有成果、检查适用性，再选择 **Take（直接复用）**、**Borrow（借鉴适配）** 或 **Build（新建）**。任务接续时，依据保存的工程记录核对哪些结论仍然成立，再继续工作。

## 三种任务，都不必从头开始

| 当你需要…… | 先检查已有成果 |
| --- | --- |
| **开发功能** | 检查本地模块和扩展点，再决定是否新增实现或依赖。 |
| **补齐测试** | 复用已有 runner、fixture 和断言，优先扩展最相关的测试。 |
| **接续任务** | 读取已保存的目标、决策和证据，与当前工作区核对，包括未提交的修改。 |

**测试资产可以复用，旧的通过结果需要核对。** 历史结果描述的是当时的状态；相关代码、测试、配置或环境变化后，需要重跑受影响的检查。

## 快速开始

> **开发预览：** 此修订尚未推送至公开 `main`。试用本轮改造，请从干净的修订后工作副本或提供的源码包安装。

在**另一个需要使用 Skill 的项目**中打开终端，替换来源路径后执行：

```bash
npx skills@1.7.0 add "<absolute-path-to-clean-checkout>" --skill reuse-before-build --agent codex --copy -y
```

可选安装器要求 **Node.js ≥22.20.0**，Skill 本身不需要。也可以手动将 `SKILL.md` 和 `LICENSE` 放到 Codex 项目的 `.agents/skills/reuse-before-build/`；详见[复制命令与其他工具目录](docs/compatibility.md#manual-installation)。

<details>
<summary>安装当前已公开的 GitHub 版本</summary>

以下命令取得的是较早的公开版本，不含本预览的改造：

```bash
npx skills@1.7.0 add Ai-Eastern/reuse-before-build --skill reuse-before-build --agent codex --copy -y
```

</details>

在 Agent 中打开目标项目，明确选择或提及 `reuse-before-build`，然后给它一个真实任务：

```text
使用 reuse-before-build，给已有 HTTP 客户端增加重试支持。
先检查已有代码、测试和相关决策。
修改前说明：哪些成果可以复用、哪些结论需要验证，以及最小下一步。
```

结果应引用实际文件或来源，并解释选择。无法加载时参照[加载排查](docs/compatibility.md#troubleshooting)，也可以先用仓库中的[练习项目](evals/fixtures/retry-service/README.md)尝试。

## 工作方式

**先找已有成果 → 核对适用性与证据 → 选择最小改动 → 验证。**

按本地代码与测试、标准库或平台能力、已安装依赖的顺序检查，必要时再查外部候选。证据充分即可停止；小改动只做简短的本地检查。

| 决策 | 接下来做什么 |
| --- | --- |
| **Take · 直接复用** | 使用已满足需求的成果，并做相关验证。 |
| **Borrow · 借鉴适配** | 扩展已有实现、测试或模式，明确改动边界。 |
| **Build · 新建** | 检查合理复用选项后，只补齐缺失的行为。 |

所选路径缺少必要证据、且没有已验证替代方案时，报告 **Blocked**。具体下一步超出现有授权时，报告 **Needs human approval**。一个候选不适用，不会阻止另一条已有证据支持的路径。

### 让工程决策跨会话继续有效

交接前，保留目标、工作区状态、可复用成果、决策、验证和下一步。优先使用项目已有记录，也可采用[检查点模板](templates/reuse-checkpoint.md)，并把记录路径提供给接续会话。

恢复时，将记录与当前请求、工作区重新核对：保留仍适用的结论，只复查受变化影响的部分。交接摘要不会新增授权。接续依赖可读取的记录，不保证自动记忆或自动捕获宿主的上下文压缩事件。

## 实际结果

两个新上下文 Agent 在小型重试服务模拟项目中，显式加载 Skill 后完成了以下任务：

| 场景 | 实际观察 | 证据 |
| --- | --- | --- |
| **扩展已有测试** | 原测试文件新增 2 个用例，生产代码未变，**4/4 通过**。 | [差异](evals/results/2026-09-20/test-borrow.patch) · [复核日志](evals/results/2026-09-20/test-borrow.tap) |
| **源码变更后接续** | HEAD 未变，但识别出旧的通过结果已失效；报告 **1 通过、1 失败**，未修改工作区。 | [记录](evals/results/2026-09-20/dirty-resume.json) · [复核日志](evals/results/2026-09-20/dirty-resume.tap) |

第二个场景刻意引入了回归，识别失败就是预期行为。这是两次有界观察，没有对照实验，不代表普遍成功率或 token 节省比例。详见[评估方法、证据与覆盖边界](docs/validation.md)。

## 与你的 Agent 配合使用

已整理 **Codex、Claude Code、GitHub Copilot CLI、Cursor、Gemini CLI、OpenCode 和 Windsurf** 的安装路径。各工具的证据程度不同：文档支持格式、安装检查通过和实际行为验证，是不同的结论。

[兼容指南](docs/compatibility.md)逐项记录了目录与验证状态。Skill 使用 Agent 原本具备的文件、检索和测试工具。

## 示例与贡献

- **从具体任务开始：** [复用代码](examples/take-example.md)、[适配代码](examples/borrow-example.md)、[补齐实现](examples/build-example.md)、[复用测试](examples/test-reuse-example.md)、[接续工作](examples/resume-example.md)。
- **了解决策边界：** [证据不足](examples/blocked-example.md)、[授权边界](examples/needs-approval-example.md)。这些是说明性示例，实际运行记录见上方。
- **帮助改进：** [提交可复现案例](https://github.com/Ai-Eastern/reuse-before-build/issues/new/choose)、验证一种工具，或[运行评估](evals/README.md)。附上修订、宿主与模型、任务、预期结果和脱敏证据。

<details>
<summary>范围与限制</summary>

这是指令工作流，效果取决于宿主和模型。它不增加工具、不提供运行时强制拦截，也不保证降低成本。外部检索需要 Agent 已有的网络能力；证据检查不能替代安全或法律审查。

接续只覆盖当前任务的工程状态，不索引无关对话、不提供全局记忆、不授予额外权限。示例、模板和评估资产均为可选；核心指令在 [SKILL.md](SKILL.md) 中。

</details>

[MIT](LICENSE) · 再分发时请保留版权和许可声明。
