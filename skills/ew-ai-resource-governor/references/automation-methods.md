# Model Scheduling Methods / 模型調度方法

Explain methods only. Never create, activate, or modify a user's automation, model, reasoning setting, API request, or CLI configuration.

## Method A — ChatGPT or Work / ChatGPT 或工作模式

Dynamic model switching is not a Skill action. Use the governance report to recommend the model and reasoning level, then tell the user where to select them in the composer.

Best for: individual interactive work.

Tradeoff: simple and responsible, but requires a user decision for every change.

## Method B — Codex Automations / Codex 自動化

Teach the user to separate recurring work by task class, then assign a model and reasoning level to each automation during setup.

Example policy:

| Task class / 任務類型 | Model tier / 模型層級 | Reasoning / 推理 |
|---|---|---|
| Routine reporting / 例行報告 | ECONOMY | LOW–MEDIUM |
| Standard coding / 一般程式工作 | BALANCED | MEDIUM |
| Architecture review / 架構審查 | HIGH ASSURANCE | HIGH |
| Critical diagnosis / 關鍵診斷 | FRONTIER | HIGH–MAX |

Best for: recurring, well-defined tasks.

Tradeoff: each automation has a deliberate preset; it is not a hidden model change inside an interactive conversation.

## Method C — Codex CLI profiles / Codex CLI 設定檔

Teach the user to create named profiles for economy, balanced, and high-assurance work, with explicit model and reasoning defaults. The user chooses which profile or command to run.

Best for: developers and repeatable engineering workflows.

Tradeoff: deterministic and auditable, but the user must maintain profiles as model availability changes.

## Method D — Application API router / 應用程式 API 路由

For an application the user owns, explain this architecture:

`Task facts → EW policy classification → user-approved routing rules → Responses API model and reasoning parameters → usage log`

The policy classifier should return:

- task class;
- value, risk, urgency, difficulty, and failure history;
- allowance state;
- recommended capability tier;
- reasoning level;
- fallback tier;
- escalation condition;
- human approval requirement.

Best for: enterprise applications that need repeatable governance across many requests.

Tradeoff: true programmatic routing requires application development, API credentials, logging, evaluation, and cost controls. It is outside the execution scope of this Skill.

## Responsible boundary / 責任邊界

Always distinguish:

- `RECOMMENDED / 建議`
- `USER APPROVED / 使用者核准`
- `CONFIGURED BY USER / 使用者已設定`

Never report the last two states without explicit evidence.
