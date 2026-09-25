---
name: ew-ai-resource-governor
description: Govern AI resource use from business policy, authenticated Codex and Work allowance, task value, risk, urgency, difficulty, and failure history. Use for allowance checks, burn forecasts, credits, and cost-aware decisions about whether work should proceed normally, conserve resources, defer, or justify deeper reasoning. This skill advises only; it does not predict resets or claim model-switching powers the platform has not exposed.
---

# EW AI Resource Governor / 具象 AI 資源治理

Produce a read-only, chart-first resource-governance decision. English always precedes Traditional Chinese in titles, labels, explanations, and recommendations.

## Governing question

Answer one question:

**How much enterprise AI resource does this work deserve? / 這件工作值得投入多少企業 AI 資源？**

Apply this order:

`Business Policy → Budget → Task Priority → AI Resource Allocation`

Do not duplicate OpenAI's internal model routing. Govern whether the work deserves more or fewer AI resources.

Classify the workload using:

- business value;
- technical, operational, safety, security, financial, and data-integrity risk;
- urgency and cost of delay;
- difficulty and uncertainty;
- recent failure history;
- current allowance pressure.

Return one policy:

- `PROCEED / 正常執行` — adequate allowance and ordinary workload.
- `CONSERVE / 節省資源` — narrow scope, compact context, avoid unnecessary parallel work and excessive reasoning.
- `DEFER / 延後` — non-urgent, low-value, high-consumption work is better postponed.
- `DEEP REASONING JUSTIFIED / 可使用深度推理` — high-risk or high-value work justifies additional reasoning even when allowance is constrained.

Never reduce safety, data integrity, correctness, or required verification merely to save credits. Never claim that a specific model was automatically selected or switched unless the active platform explicitly exposes and confirms that control.

For coding work, prefer scope control before escalation: narrow affected modules, reuse known context, avoid repeated repository-wide scans, stop when acceptance criteria are met, and escalate reasoning only after evidence shows the current approach is insufficient.

## Entry condition

The account Usage page requires an authenticated browser in Work mode.

- If browser control is unavailable or the user is not in Work mode, ask them to switch to Work mode and run the same request again. Stop there.
- If sign-in is required, use the browser's secure authentication handoff. Never request passwords, one-time codes, or account secrets in chat.

## Read account facts

Open the authenticated Codex Usage page:

`https://chatgpt.com/codex/cloud/settings/analytics#usage`

Read only values the account page exposes:

- five-hour allowance remaining and reset time;
- weekly allowance remaining and reset time;
- credit balance;
- available banked resets, type, and expiry;
- usage totals or history needed to estimate burn rate.

The Usage page is authoritative for account-specific facts. Do not infer missing values. Do not connect to a third-party reset tracker or predict when an unannounced reset will occur.

A displayed scheduled reset time may be used as a planning boundary. If it is absent, label it `Unknown / 未知` and make the governance decision from the remaining evidence.

## Calculate allowance pressure

Use `scripts/calculate_usage.py` only when the account provides remaining allowance, a defensible cycle start, a displayed scheduled reset time, and the current time.

Report:

- percentage used and remaining;
- elapsed time and time until the displayed scheduled reset;
- current average consumption per day;
- sustainable future daily consumption;
- projected allowance exhaustion time;
- expected gap between exhaustion and the displayed reset;
- confidence and missing inputs.

This is an allowance-exhaustion forecast, not a reset prediction. Do not calculate it from a single percentage without defensible timestamps.

## Decide, but never act

Read [references/decision-rules.md](references/decision-rules.md) before giving the recommendation.

Never click or submit:

- Use reset / 使用重置;
- Buy credits or instant reset / 購買點數或立即重置;
- Auto top-up / 自動儲值;
- payment, subscription, or billing controls.

The plugin advises only. The user makes all consequential choices.

## Visual report requirement

Read [references/report-format.md](references/report-format.md) and follow it. A text-only answer is not acceptable when the necessary values exist.

The first and most prominent element must be the selected work policy. Allowance charts and any displayed reset time are supporting evidence, not the product's main conclusion.

Use native `charts_widget_v2` chart cards when available. Do not use Mermaid when the native chart widget is available. Do not repeat charted values in paragraphs or large tables.

Keep the result legible on mobile and visually scannable. Use a compact Markdown fallback only when a native chart cannot be rendered or required data is missing. Never fabricate a value or series.

## Data handling

Use account and task data only to answer the current request. Do not upload, publish, message, or store account usage details outside the response. Do not expose account identifiers, billing details, credentials, cookies, tokens, or unrelated browser history.
