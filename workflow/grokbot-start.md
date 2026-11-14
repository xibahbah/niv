# Grok daily execution prompt

Read AGENTS.md, MEMORY.md, OWNER.md, workflow/daily-policy.json, and workflow/daily-run.md from the private working repository.
Read workflow/LATEST.md and its actual handoff.
Read current application logs, task states, and recent Grok and research logs.
Read relevant skill instructions.

Execute only complete eligible packets within the current owner's documented authorization.
Use the configured daily cap across all workers.
Do not treat this template as approval.
Respect explicit holds, skips, company limits, and missing required answers.
Reuse confirmed equivalent answers without asking again.
Do not guess a new answer when question wording changes its meaning.

Claim a task before work. Recheck live status and duplicate submissions.
Inspect every rendered field and actual uploaded resume.
Before submitting, save the full form and screenshots.
Write applications/<role>/filled-form.md.
Write logs/grok/<local-date>/filled-forms.md for the daily audit.
Write logs/grok/<local-date>/run-log.md for execution events and errors.
Use the supplied report templates. Include incomplete attempts.

Record CAPTCHA provider, visible error, timestamps, attempt count, attachment state, evidence, and next action.
Separate observed failures from suspected causes.
After two unchanged failures, stop automatic retries.
For ambiguous submission, use verify_submission and reconcile before retrying.
Require actual confirmation evidence before recording submitted.

Preserve other workers' files and events. Never force-push.
Save durable personal corrections in OWNER.md with sources and dates.
Report actual submissions, blockers, and shortages.
Do not send messages unless separately authorized.

For daily execution, configure this prompt in your real scheduler.
Report its task ID, timezone, next run, runtime, and tested result.
If your runner cannot schedule or requires a local computer, state that limitation.
A saved prompt alone is not an active schedule.
