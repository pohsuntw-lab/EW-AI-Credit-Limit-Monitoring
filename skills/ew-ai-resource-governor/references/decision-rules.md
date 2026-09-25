# Resource Governance Decision Rules / AI 資源治理決策規則

Apply these rules before recommending a model. First decide how much enterprise AI resource a task deserves; then map that entitlement to a suitable current model and reasoning level.

## 1. Business policy / 企業政策

Identify first:

- protected, prohibited, or restricted work;
- approval requirements and budget ceilings;
- deadlines and service obligations;
- safety, security, privacy, legal, and data-integrity constraints.

Business policy overrides convenience and credit-saving preferences.

## 2. Task profile / 任務輪廓

Classify each factor as `LOW / 低`, `MEDIUM / 中`, or `HIGH / 高`:

- **Value / 價值:** business value if completed.
- **Risk / 風險:** consequence of an incorrect result or delay.
- **Urgency / 急迫性:** cost of waiting.
- **Difficulty / 難度:** uncertainty, cross-module reasoning, debugging depth, or architectural complexity.
- **Failure history / 失敗紀錄:** zero, one, or two-plus properly scoped failed attempts.

Do not equate long duration or a large repository with high reasoning difficulty.

## 3. Budget context / 預算情境

Use only an account-confirmed percentage or a percentage explicitly supplied by the user:

- **HEALTHY / 充足:** more than 50% remaining
- **WATCH / 注意:** 25–50% remaining
- **CONSTRAINED / 吃緊:** 10–24% remaining
- **CRITICAL / 臨界:** less than 10% remaining
- **NOT AVAILABLE / 無法取得:** no confirmed percentage available

These are product governance defaults, not platform limits.

Use a reset time only when the user supplies it or it is already present in the conversation. Treat it as a scheduling boundary:

- a nearby reset may support deferring low-value, non-urgent, high-consumption work;
- it never justifies delaying critical, high-risk, or deadline-bound work;
- never calculate or claim a reset time that was not provided.

Missing budget data lowers confidence in budget advice but does not block a task-policy recommendation.

## 4. Select one policy / 選擇一項策略

### PROCEED / 正常執行

Use when the task has clear value, manageable risk, and reasonable expected resource use. Also use for protected work that must continue.

### CONSERVE / 節省資源

Use when the task should continue but scope or allowance pressure calls for discipline.

Prefer:

- narrow scope and explicit acceptance criteria;
- relevant files or modules only;
- reuse of known evidence;
- no unnecessary rescans or parallel work;
- ordinary reasoning until evidence justifies escalation;
- immediate stop when acceptance criteria pass.

### DEFER / 延後

Use when work is low-value, low-urgency, resource-intensive, and safe to postpone.

Never defer incident response, safety work, data-integrity repair, security remediation, or work where waiting creates material risk merely to preserve credits.

### DEEP REASONING JUSTIFIED / 可使用深度推理

Use when:

- risk or value is high and the problem genuinely requires deeper reasoning;
- two properly scoped ordinary attempts failed;
- evidence indicates an architectural, concurrency, data-integrity, security, or similarly high-risk problem.

After diagnosis or architecture is settled, return mechanical implementation to ordinary resource use when appropriate.

## 5. Conflict rules / 衝突規則

Apply these priorities:

1. safety, legality, security, and data integrity;
2. critical business continuity;
3. value and cost of delay;
4. allowance conservation;
5. convenience.

High allowance does not justify waste. Low allowance does not justify unsafe or incorrect work.

## 6. Confidence / 信心程度

- **HIGH / 高:** task value, risk, urgency, difficulty, and failure history are known.
- **MEDIUM / 中:** one non-critical factor is missing.
- **LOW / 低:** value, risk, or urgency is unclear.

Allowance is optional and must not be the sole reason for LOW confidence.

## 7. Governing principle / 治理原則

**Lowest sufficient intelligence, highest necessary assurance. / 使用足以完成工作的最低合理智慧，保留必要的最高可靠性。**

Optimize scope before sacrificing correctness. Never trade safety, security, data integrity, required verification, or material decision quality for credit savings.
