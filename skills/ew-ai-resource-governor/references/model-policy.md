# Model Recommendation Policy / 模型建議政策

Recommend only a model currently exposed to the user. The user makes the final selection.

## Capability tiers / 能力層級

### ECONOMY / 經濟

Use for routine, low-risk, well-defined work.

- Preferred: current Luna-class model.
- Reasoning: LOW or MEDIUM.
- Examples: formatting, extraction, simple edits, mechanical coding changes.

### BALANCED / 平衡

Use for ordinary professional work with moderate uncertainty.

- Preferred: current Terra-class model; use Sol-class for coding-heavy work.
- Reasoning: MEDIUM.
- Examples: standard reports, scoped analysis, normal coding, test repair.

### HIGH ASSURANCE / 高可靠

Use for high-value, high-risk, or genuinely complex work.

- Preferred: current Sol-class model.
- Reasoning: HIGH or XHIGH when exposed.
- Examples: architecture, difficult debugging, contracts, material data decisions.

### FRONTIER / 前沿

Use only when the consequences or complexity justify the highest resource level.

- Preferred: current Astra-class model.
- Reasoning: HIGH, MAX, or the highest appropriate exposed level.
- Examples: critical incident analysis, cross-system architecture, unresolved high-risk work after two properly scoped attempts.

Use Ultra only for a large task that benefits from multi-agent delegation. Do not recommend it merely because a task is important.

## Recommendation rules / 建議規則

1. Start from business value and risk, not model prestige.
2. Use the lowest sufficient model and reasoning level.
3. Escalate after evidence, not anxiety.
4. Prefer narrowing scope before increasing reasoning.
5. Include one lower-resource fallback.
6. State quality, time, and allowance tradeoffs.
7. End with `USER DECISION REQUIRED / 需使用者決定`.

Model names and availability change. When the host exposes a current model list, use it. Otherwise recommend the capability tier and label model names as examples.
