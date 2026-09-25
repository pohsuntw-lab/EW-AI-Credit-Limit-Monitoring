# Chart-First Report Format / 圖表優先報告格式

English must appear before Traditional Chinese throughout the report.

The successful report is a compact governance decision, not a reset bulletin and not an essay.

## Mandatory opening

Begin with the selected policy:

```markdown
## WORK POLICY / 工作策略

# 🟣 CONSERVE / 節省資源
```

Do not place a reset heading or generic report title above the policy.

## Decision line

Immediately below the policy, show one compact line:

```markdown
**VALUE / 價值:** HIGH · **RISK / 風險:** MEDIUM · **URGENCY / 緊急度:** LOW · **BUDGET / 預算:** CONSTRAINED
```

When the task is coding work, add at most one execution instruction:

`Narrow scope → relevant modules only → normal reasoning → escalate after evidence / 縮小範圍 → 僅讀相關模組 → 一般推理 → 有證據才升級`

## Allowance context

Show only account-confirmed values:

```markdown
**WEEKLY / 每週:** 18% remaining / 剩餘 18% · **5-HOUR / 五小時:** Not exposed / 未顯示 · **DISPLAYED RESET / 帳號顯示重置:** 14h
```

Use `Unknown / 未知` or `Not exposed / 未顯示` when appropriate. Never predict an undisclosed reset or cite a third-party reset tracker.

## Allowance chart

When values exist, render one native `charts_widget_v2` pie chart for weekly remaining versus used allowance. Do not repeat those percentages in a table.

```text
genui{"charts_widget_v2":{"content":{"chartType":"pie","meta":{"title":"Weekly allowance / 每週額度","description":"18% remaining; 82% used. / 剩餘18%，已使用82%。","footer":"Account confirmed / 帳號確認"},"nameKey":"status","valueKey":"percentage","series":[{"dataKey":"percentage","label":"Allowance / 額度","valueFormat":"raw","valueSuffix":"%"}],"data":[{"status":"Remaining / 剩餘","percentage":18},{"status":"Used / 已使用","percentage":82}]}}}
```

Replace examples with account facts. The two values must total 100.

## Burn chart

Render a current-versus-sustainable daily burn bar chart only when the cycle start and displayed reset time are defensible. Its footer may state projected allowance exhaustion and the gap before the displayed reset. This is an allowance forecast, not a reset prediction.

Do not render the chart when required timestamps are missing. Show one short missing-data notice instead.

## Recommendation

Give one sentence stating the best action, followed by no more than three compact reasons. End with:

`No action was executed / 未執行任何操作`

## Density limits

- Use no more than two chart cards.
- Do not use Mermaid when `charts_widget_v2` is available.
- Do not repeat a number already visible in a chart unless it is a decision threshold.
- Do not add an executive summary, methodology section, reset-news section, source-comparison section, or model-routing essay.
- Keep the complete result understandable on one mobile screen plus chart scrolling.
