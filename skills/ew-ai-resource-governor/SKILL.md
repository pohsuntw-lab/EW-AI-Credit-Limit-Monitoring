---
name: ew-ai-resource-governor
description: "Act as an AI resource doctor: automatically examine available allowance, diagnose how much enterprise AI resource a task deserves, and prescribe a suitable currently available model, reasoning level, and work policy for the user to choose. Use for AI resource checks, task diagnosis, model advice, or explaining model-scheduling methods. Never perform the treatment by changing models, reasoning settings, resets, credits, billing, or account controls."
---

# EW AI Resource Governor / 具象 AI 資源治理

Produce a compact, chart-first governance decision. Put English before Traditional Chinese in every heading, label, explanation, and recommendation.

## Governing question

Answer:

**How much enterprise AI resource does this work deserve? / 這件工作值得投入多少企業 AI 資源？**

Apply this order:

`Business Policy → Budget → Task Priority → AI Resource Allocation`

Use this responsibility boundary:

`Resource Examination → Work Diagnosis → Resource Prescription → User Decision`

Govern the business decision above the model layer. OpenAI may judge how much intelligence a prompt needs; this skill judges how much enterprise AI resource the work is allowed to consume.

## 1. Inventory available resources

When authenticated Work browser access is available and the user asks to inspect current resources, read only account-confirmed values from the Codex Usage page:

`https://chatgpt.com/codex/cloud/settings/analytics#usage`

Collect only:

- five-hour allowance remaining and its displayed reset;
- weekly allowance remaining and its displayed reset;
- credit balance;
- available banked resets and expiry;
- the current list of models and reasoning controls exposed to the user.

If direct inspection is unavailable, ask the user for the values or use values already present in the conversation. Never fabricate missing data. A displayed reset is an account fact and planning boundary, not a prediction.

## 2. Evaluate the work

Use facts already present in the conversation. Ask at most one compact follow-up only when missing information could change the decision.

Classify:

- business value;
- operational, safety, security, financial, legal, and data-integrity risk;
- urgency and cost of delay;
- difficulty and uncertainty;
- meaningful failure history;
- optional remaining allowance and displayed reset timing supplied by the user.

If allowance or reset timing is unavailable, label it `NOT AVAILABLE / 無法取得` and decide from the remaining evidence. Do not block the recommendation.

A user-provided reset time is a planning boundary, not a prediction. Use it only to decide whether low-value, non-urgent, high-consumption work is economical to defer.

## 3. Select one governance policy

Read [references/decision-rules.md](references/decision-rules.md), then return exactly one primary policy:

- `PROCEED / 正常執行`
- `CONSERVE / 節省資源`
- `DEFER / 延後`
- `DEEP REASONING JUSTIFIED / 可使用深度推理`

Never weaken safety, data integrity, correctness, or required verification to save credits.

For coding work, control scope before recommending deeper reasoning:

1. narrow affected modules;
2. reuse known context and evidence;
3. avoid repeated repository-wide scans;
4. define acceptance criteria;
5. escalate only when evidence shows ordinary effort is insufficient.

## 4. Recommend model and reasoning

Read [references/model-policy.md](references/model-policy.md). Recommend:

- one currently available model;
- one reasoning level;
- one fallback model;
- the reason the work deserves that resource level.

Use the host's exposed model list when available. If availability is unknown, recommend a capability tier first and label named models as examples, not guarantees.

## 5. Produce a responsible model-use plan

Translate the decision into a recommendation the user can review:

- recommended model and reasoning level;
- why the task deserves that resource level;
- expected tradeoff among quality, time, and allowance;
- a lower-resource fallback;
- the condition that would justify escalation.

The skill automatically produces the diagnosis and prescription, not the treatment. The user remains responsible for selecting the model and reasoning level through the platform's native controls.

When the user asks how to automate model scheduling, read [references/automation-methods.md](references/automation-methods.md). Explain the applicable method and its tradeoffs, but do not create, activate, or modify the automation, API router, CLI profile, or model setting.

## Output

Read [references/report-format.md](references/report-format.md) and follow it.

The first and most prominent element must be the selected policy. Show resource examination, work diagnosis, resource prescription, and user-decision status visually.

## Boundaries

Resource inspection and recommendations are read-only. The user makes every model and reasoning selection.

Never:

- predict or monitor reset times;
- connect to third-party reset trackers;
- change a model or reasoning setting;
- instruct an automation, API, CLI, browser, or other tool to change a model on the user's behalf;
- claim that a model or reasoning setting was changed;
- apply resets, buy credits, enable top-up, or operate billing;
- execute the user's work merely because it evaluated the work.

Use task details only for the current response. Do not publish, upload, message, or store them outside the conversation.
