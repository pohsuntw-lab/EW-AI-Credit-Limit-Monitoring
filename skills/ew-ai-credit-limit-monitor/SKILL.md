---
name: ew-ai-credit-limit-monitor
description: Read a user's authenticated Codex and Work usage in Work mode, check current reset intelligence, forecast exhaustion, and provide a bilingual visual recommendation. Use when the user asks about Codex allowance, Work usage, weekly or five-hour limits, credits, reset timing, banked resets, or whether to wait, reset, or buy credits. This skill is read-only and never applies a reset or makes a purchase.
---

# EW AI Credit Limit Monitor / EW AI 額度監控

Produce a read-only, chart-first decision dashboard. English always precedes Traditional Chinese in titles, labels, explanations, and recommendations.

## Entry condition

The account Usage page requires an authenticated browser in Work mode.

- If browser control is unavailable or the user is not in Work mode, ask them to switch to Work mode and run the same request again. Stop there.
- If sign-in is required, use the browser's secure authentication handoff. Never request passwords, one-time codes, or account secrets in chat.

## Read account facts

Open the authenticated Codex Usage page:

`https://chatgpt.com/codex/cloud/settings/analytics#usage`

Read, when available:

- five-hour allowance remaining and reset time;
- weekly allowance remaining and reset time;
- credit balance;
- available banked resets, type, and expiry;
- recent reset history;
- usage totals or history needed to estimate burn rate.

The Usage page is the authority for account-specific facts. Do not infer a missing value. If the five-hour meter is not exposed, state that it is unavailable instead of inventing it.

## Check reset intelligence

Search current information every time; this information changes.

Read [references/official-sources.md](references/official-sources.md) before classifying a reset announcement.

1. Check OpenAI's official Help Center and ChatGPT Release Notes for the governing rules and confirmed promotions.
2. Check `https://codex-resets.com/` for the latest announcement and reset history.
3. Label codex-resets.com as third-party reset intelligence. Do not present it as an OpenAI policy source.
4. Distinguish normal scheduled reset, automatic/global reset, banked reset, purchased instant reset, and credits.
5. If a third-party announcement has no official or account-level confirmation, label it `THIRD-PARTY SIGNAL — UNVERIFIED / 第三方線索—尚未獲官方確認`. Never recommend a consequential action from that signal alone.

## Calculate the forecast

Use `scripts/calculate_usage.py` when the account provides enough timestamps. Do not calculate a burn-rate forecast from a single percentage without a defensible cycle start.

Report:

- percentage used and remaining;
- elapsed time and time until scheduled reset;
- average consumption per day;
- maximum future daily consumption that would reach the scheduled reset;
- projected exhaustion time;
- expected gap between exhaustion and normal reset;
- confidence and missing inputs.

## Decide, but never act

Read [references/decision-rules.md](references/decision-rules.md) before giving the recommendation.

Never click or submit:

- Use reset / 使用重置;
- Buy credits or instant reset / 購買點數或立即重置;
- Auto top-up / 自動儲值;
- payment, subscription, or billing controls.

The plugin advises only. A user must make any consequential choice themselves.

## Visual report requirement

Read [references/report-format.md](references/report-format.md) and follow it. A text-only answer is not acceptable when the necessary values exist.

The first and most visually prominent element must be the next scheduled reset. Display its exact date, time, and timezone using the largest Markdown heading. All other metrics, charts, sources, and recommendations follow underneath.

Use native `charts_widget_v2` chart cards as the primary report surface. Do not use Mermaid when the native chart widget is available. Do not repeat charted values in paragraphs or large tables.

The default successful report contains:

1. the next reset heading;
2. one weekly allowance pie chart;
3. one burn-rate comparison bar chart when the forecast is defensible;
4. one primary recommendation status with at most three compact facts;
5. one compact source line.

Keep the dashboard legible on mobile and visually scannable without reading prose. Use a compact Markdown fallback only when a native chart cannot be rendered or required data is missing. Never fabricate a series.

## Data handling

Use account data only to answer the current request. Do not upload, publish, message, or store account usage details outside the response. Do not expose account identifiers, billing details, credentials, cookies, tokens, or unrelated browser history.
