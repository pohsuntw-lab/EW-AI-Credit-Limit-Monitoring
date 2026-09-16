# Chart-First Report Format / 圖表優先報告格式

English must appear before Traditional Chinese throughout the report.

The successful report is a dashboard, not an essay. Show charts first and keep explanatory prose to the minimum required for a safe decision.

## Mandatory opening

Do not place a report title above the reset time. Begin exactly with this hierarchy:

```markdown
## NEXT RESET / 下次重置

# TUE, SEP 22, 2026 · 09:42 GMT+8
```

Use the user's actual localized time, spell out the timezone, and never omit the date.

## Compact status line

Immediately below the reset time, show one compact line only:

```markdown
**5-HOUR / 五小時:** Not exposed / 未顯示 · **CREDITS / 點數:** 0 · **BANKED / 儲存重置:** 2
```

Use `Not exposed / 未顯示` for an unavailable account value.

## Allowance chart

Render one native `charts_widget_v2` pie chart. The chart is the primary display of weekly remaining versus used allowance. Do not repeat those percentages in a table.

```text
genui{"charts_widget_v2":{"content":{"chartType":"pie","meta":{"title":"Weekly allowance / 每週額度","description":"76% remaining; 24% used. / 剩餘76%，已使用24%。","footer":"Account confirmed / 帳號頁面確認"},"nameKey":"status","valueKey":"percentage","series":[{"dataKey":"percentage","label":"Allowance / 額度","valueFormat":"raw","valueSuffix":"%"}],"data":[{"status":"Remaining / 剩餘","percentage":76},{"status":"Used / 已使用","percentage":24}]}}}
```

Replace the example values with account facts. The two values must total 100.

## Burn forecast chart

When the forecast is defensible, render one native `charts_widget_v2` bar chart comparing current daily burn with sustainable daily burn. Pin the axis to a sensible zero baseline. Put the required reduction, projected exhaustion time, and gap before reset in the chart description or footer instead of separate paragraphs.

```text
genui{"charts_widget_v2":{"content":{"chartType":"bar","meta":{"title":"Daily burn-rate comparison / 每日消耗速度比較","description":"Current consumption is above the sustainable rate. / 目前消耗速度高於可維持速度。","footer":"Reduce by 33.5%. Projected exhaustion: Sep 20, 11:39; 46 hours before reset. / 需降低33.5%；預估9月20日11:39用完，比重置早46小時。"},"xKey":"rate","series":[{"dataKey":"percentage","label":"Daily consumption / 每日消耗","axisLabel":"Percent per day / 每日百分比","valueFormat":"raw","valueSuffix":"%"}],"yAxisMin":0,"data":[{"rate":"Current / 目前","percentage":19.68},{"rate":"Sustainable / 可維持","percentage":13.09}]}}}
```

Replace the example values and timestamps with calculated results. Do not render this chart when the cycle start is not defensible. In that case, show one short missing-data notice.

## No duplicate timeline

Do not add a reset timeline table when the reset heading and burn-chart footer already contain the relevant times. Mention an expiring banked reset only when it materially changes the recommendation.

## Recommendation panel

Use exactly one primary status:

- `🟢 CONTINUE / 繼續使用`
- `🟡 SLOW DOWN / 降低消耗`
- `🟠 WAIT FOR RESET / 等待重置`
- `🔴 CONSIDER BANKED RESET / 考慮使用儲存重置`

Show the status immediately after the charts. State the best action in one sentence, followed by no more than three compact facts. Clearly say `No action was executed / 未執行任何操作`.

## Compact source line

Close with one compact line containing three visibly distinct authority labels:

- `ACCOUNT CONFIRMED / 帳號確認`: authenticated Usage page.
- `OFFICIALLY CONFIRMED / 官方確認`: exact OpenAI Help Center or Release Notes link.
- `THIRD-PARTY SIGNAL — UNVERIFIED / 第三方線索—尚未獲官方確認`: codex-resets.com link.

Do not add source summaries unless sources conflict or a warning materially affects the decision. Never merge official and third-party authority levels.

## Density limits

- Use no more than two chart cards in the default report.
- Do not use Mermaid when `charts_widget_v2` is available.
- Do not repeat a number already visible in a chart unless it is the primary recommendation threshold.
- Do not add an executive summary, methodology section, narrative forecast, or long explanation.
- Keep the complete report understandable on one mobile screen plus chart scrolling.
