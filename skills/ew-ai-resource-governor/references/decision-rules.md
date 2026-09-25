# Resource Governance Decision Rules / AI 資源治理決策規則

Apply these rules in order. The goal is not to choose the smartest model; it is to decide how much enterprise AI resource a task deserves.

## 1. Apply business policy / 套用企業政策

Identify any explicit policy first:

- protected work that must receive sufficient resources;
- prohibited or restricted work;
- approval requirements;
- budget ceilings;
- deadlines and service obligations;
- safety, security, privacy, legal, or data-integrity constraints.

Business policy overrides convenience and credit-saving preferences.

## 2. Classify the workload / 工作分級

Score qualitatively from LOW / MEDIUM / HIGH:

- **Value / 價值** — business or user value if completed now.
- **Risk / 風險** — consequence of an incorrect result.
- **Urgency / 緊急度** — cost of delay.
- **Difficulty / 難度** — uncertainty, cross-module reasoning, debugging depth, or architectural complexity.
- **Failure history / 失敗紀錄** — whether properly scoped ordinary attempts already failed.

Do not equate long duration or a large repository with high reasoning difficulty.

## 3. Read the budget state / 讀取預算狀態

Use authenticated account facts when available.

Classify weekly remaining allowance:

- **HEALTHY / 充足:** > 50%
- **WATCH / 注意:** 25–50%
- **CONSTRAINED / 吃緊:** 10–25%
- **CRITICAL / 臨界:** < 10%

These are governance defaults, not OpenAI limits. If defensible usage data projects allowance exhaustion before the displayed scheduled reset, treat the state one level more conservatively.

Also consider five-hour limits, credits, eligible banked resets, and time until a scheduled reset only when those values are visible on the account page. Never predict an undisclosed reset or query a third-party reset tracker.

## 4. Select one governance policy / 選擇一項治理策略

### PROCEED / 正常執行

Use when allowance is healthy, or the task is high-value and expected resource use is reasonable.

### CONSERVE / 節省資源

Use when allowance is WATCH or CONSTRAINED and the task should continue.

Prefer:

- narrow scope and explicit acceptance criteria;
- reuse known context;
- relevant files or modules only;
- no unnecessary repository-wide rescans;
- no unnecessary parallel agents;
- normal reasoning unless evidence justifies escalation;
- stop immediately when acceptance criteria pass.

### DEFER / 延後

Use when allowance is CONSTRAINED or CRITICAL and the task is low urgency and low consequence if postponed.

Never defer critical incident response, safety work, data-integrity repair, security remediation, or another task where waiting creates material risk merely to preserve credits.

### DEEP REASONING JUSTIFIED / 可使用深度推理

Use when risk or value is HIGH and the problem genuinely requires deeper reasoning, or when two properly scoped ordinary attempts failed without resolving the root cause.

Allowance pressure alone must not force a lower-quality approach where correctness is material.

## 5. Escalation rule / 升級規則

Before recommending deeper reasoning, check whether the problem can be reduced by better scope, better evidence, tests, logs, or a smaller reproduction.

Escalate when:

- two properly scoped attempts failed; or
- evidence shows an architectural, concurrency, data-integrity, security, or similarly high-risk problem; or
- incorrect output would create material consequences.

After diagnosis or architecture is settled, recommend returning to ordinary resource use for mechanical implementation when appropriate.

Do not claim the plugin switched a model unless the active platform explicitly exposes and confirms that action.

## 6. Allowance-aware scheduling / 感知額度的排程

When non-urgent, high-consumption work can wait with little cost and a displayed reset is near, DEFER may be economical.

When important work may be blocked:

1. reduce avoidable burn first;
2. protect allowance for high-value or high-risk work;
3. consider an eligible banked reset only from account-confirmed facts;
4. consider paid credits only after free options and timing have been evaluated.

Never execute a reset or purchase.

## 7. Burn-rate rules / 消耗速度規則

If projected exhaustion is at or after the displayed scheduled reset, do not create artificial scarcity.

If projected exhaustion is before the displayed scheduled reset:

- show sustainable burn rate;
- show required reduction;
- protect allowance for high-value or high-risk work;
- postpone low-value batch work before compromising important work.

Do not calculate a precise forecast without defensible timestamps.

## 8. Confidence / 信心程度

- **High:** authenticated allowance, timestamps, and task context are available.
- **Medium:** account state is known but one planning input is inferred or missing.
- **Low:** key account or task facts are missing. Give conservative guidance and do not fabricate precision.

## 9. Governing principle / 治理原則

**Lowest sufficient intelligence, highest necessary assurance. / 使用足以完成工作的最低合理智慧，保留必要的最高可靠性。**

Optimize scope before sacrificing correctness. Never trade safety, security, data integrity, required verification, or material decision quality for credit savings.
