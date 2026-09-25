# Chart-First Report Format / 圖表優先報告格式

Put English before Traditional Chinese throughout. Keep the complete result compact and mobile-friendly.

## 1. Mandatory opening / 必要開頭

Begin with exactly one selected policy:

~~~markdown
## WORK POLICY / 工作策略

# 🟣 CONSERVE / 節省資源
~~~

Do not place a generic report title above the policy.

## 2. Resource examination / 資源檢查

Show five-hour and weekly allowance, credits, banked resets, and account-displayed reset times when available. Use one compact allowance chart when numeric values exist.

## 3. Work diagnosis / 工作診斷

Show the factors in one compact table:

~~~markdown
| FACTOR / 因素 | LEVEL / 等級 | WHY / 理由 |
|---|---:|---|
| VALUE / 價值 | HIGH / 高 | ... |
| RISK / 風險 | MEDIUM / 中 | ... |
| URGENCY / 急迫性 | LOW / 低 | ... |
| DIFFICULTY / 難度 | MEDIUM / 中 | ... |
| FAILURES / 失敗 | 0 | ... |
| ALLOWANCE / 額度 | 18% remaining / 剩餘 18% | Account-confirmed or user-supplied / 帳戶確認或使用者提供 |
| RESET / 重置 | 14h displayed / 顯示 14 小時 | Planning boundary only / 僅作排程邊界 |
~~~

Use only known facts. Replace unavailable values with `NOT AVAILABLE / 無法取得`. Never invent an allowance percentage or reset time.

When a native chart widget is available, add one compact horizontal bar chart for Value, Risk, Urgency, and Difficulty using LOW=1, MEDIUM=2, HIGH=3. Label the numeric mapping clearly. Do not chart Failure count or missing allowance. If a native chart is unavailable, the table is the visual fallback.

## 4. Resource prescription / 資源處方

Give one direct line:

Narrow scope → relevant modules only → ordinary reasoning → escalate after evidence / 縮小範圍 → 僅處理相關模組 → 一般推理 → 有證據才升級

Adapt it to the selected policy.

## 5. Model recommendation / 模型建議

Show one recommendation card:

~~~markdown
| RECOMMENDATION / 建議 | SELECTION / 選擇 |
|---|---|
| MODEL / 模型 | GPT-6 Sol |
| REASONING / 推理強度 | MEDIUM / 中 |
| FALLBACK / 備選 | GPT-5.6 Terra |
| TRADEOFF / 取捨 | Balanced quality and allowance / 平衡品質與額度 |
| STATUS / 狀態 | USER DECISION REQUIRED / 需使用者決定 |
~~~

The names above are an example format. Replace them with models currently available to the user. This is a recommendation, not an executed change.

## 6. User decision / 使用者決定

Give one action sentence followed by no more than three reasons:

- why the selected policy fits;
- what would justify escalation or de-escalation;
- what evidence is missing, if material.

End with:

User decision required; no model or account setting was changed / 需使用者決定；未變更模型或帳戶設定

## 7. Prohibited sections / 禁止內容

Do not add:

- predicted or independently retrieved reset times;
- burn-rate forecasts;
- claims that a model or reasoning setting was changed;
- instructions that secretly or automatically change the user's model;
- long methodology, essays, or duplicated summaries.
