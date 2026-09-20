# Architecture discovery task

The evaluating agent received a fresh copy of the current `SKILL.md` and an
otherwise empty workspace. It was explicitly asked to use that skill for
the following request, without parent conversation history or a reviewer guide:

> 我们准备做一个 TypeScript / Node.js 22 后台任务服务。已有 PostgreSQL，部署不想再加 Redis。需要延迟任务、失败重试、多 worker 和避免重复业务副作用。现在只做架构与选型建议，不安装依赖、不写业务代码、不创建远程资源。请给出有依据的组件边界、取舍和后续验证计划。

The agent could research public sources and write only `result.md` and
`sources.json` in its evaluation workspace. It was asked to record inspected
revisions, sources, actual checks, and uncertainties, and to distinguish
source inspection from runtime verification. No candidate names or desired
decision were supplied. The workspace boundary was an instruction, not an
OS-enforced security boundary.

This task uses live external sources and is not prepared by `evals/prepare.mjs`.
To repeat it, use a new empty workspace and a recorded Skill revision. Record
the candidate revisions actually inspected; upstream versions and results
may change. Do not treat agreement on a particular package as the success
criterion. Inspect whether the recommendation follows the constraints and
has attributable evidence without claiming unexecuted integration tests.
