# Daily shared workflow

Read MEMORY.md first. Read workflow/daily-policy.json next.
The daily policy overrides older numeric targets and proposed schedules.
Read the latest owner rules and exact personal-answer sources.
Use existing skills when relevant. Read their instructions before using them.

## GPT research

1. Use the configured local date and a unique run ID.
2. Read current application logs, task packets, recent agent logs, and unresolved lessons.
3. Start with the existing researched backlog. Refresh exact official JDs.
4. Research 30 roles. Expand discovery only when needed.
5. Distinguish researched, excluded, conditional, packet-ready, and handed-off counts.
6. Never lower eligibility standards to meet a target.
7. Compare canonical ATS IDs and URL aliases against existing tasks and submissions.
8. Map at least two JD requirements to documented experience.
9. Record pay, location, degree, experience, authorization wording, start date, and live status.
10. Keep unknowns conditional. Exclude hard conflicts under current owner rules.
11. Prepare tailored materials only from supported evidence.
12. Compile and inspect each resume PDF before marking its packet ready.
13. If compilation or browser access fails, record the limitation and continue independent work.
14. Save scans/<date>/<run-id>/HANDOFF.md and the role evidence.
15. List at most 30 complete eligible packets for Grok. Carry unresolved roles separately.
16. Publish the handoff before updating workflow/LATEST.md.
17. Report shortfalls and blockers honestly. Do not claim discovery counts as eligible jobs.

## Authorization

This template authorizes no submissions. Read the current owner's explicit authorization before execution.
It does not authorize guessed required answers or reopening explicitly skipped roles.
Record the actual standing-authorization source in new task packets.
Do not claim the owner individually reviewed a packet when that did not happen.
Preserve old approval fields and explicit holds.
Do not submit while required answers or eligibility conflicts remain unresolved.
No email or LinkedIn messages are authorized by this workflow.

## Grok execution

1. Read workflow/LATEST.md and the referenced handoff.
2. Re-read current logs before claiming a task.
3. Count today's confirmed submissions across all workers before starting another.
4. Stop at the daily cap. Do not treat a retry as a new job.
5. Claim one task using a worker ID and timestamp.
6. Confirm the job is live and the packet is complete and in scope.
7. Read the exact form wording. Inspect every prefilled value.
8. Record all actual answers before submission.
9. Compare rendered values and uploaded filenames against the intended packet.
10. Capture the full form, including expanded text and each page.
11. Save applications/<folder>/filled-form.md and the daily filled-forms report.
12. Submit only when required fields match supported answers.
13. Capture the confirmation and actual outcome.
14. Update the task and application log without overwriting another worker's changes.
15. Append the event to the daily execution log.
16. Record errors, CAPTCHA observations, and lessons even when submission fails.
17. If submission is ambiguous, set verify_submission. Do not submit again until reconciled.

The filled-form report supports the owner's review.
Use the owner's selected approval mode. Standing scope and per-task approval are distinct.
Never label a form correct merely because it was prefilled.
Mark unread or partially captured fields unknown.

## CAPTCHA and errors

Record the provider, page, time, visible error, attempt count, and attachment state.
Distinguish observed failure from suspected cause.
After two unchanged failures, stop automatic retries and mark blocked_captcha.
A further attempt needs changed conditions or explicit direction.
Do not bypass access controls.
Do not store credentials, session cookies, or challenge tokens.
A page error after Submit can be ambiguous. Reconcile before any retry.

## Shared repository

Use unique scan directories and per-worker logs.
Do not rename or delete historical files during active work.
Read the current blob before updating shared files.
Merge concurrent additions by task, event, or lesson ID.
Never force-push. Never retry an external submission because a Git write failed.
Only the browser worker updates its claimed task and submission row.
Other workers write proposed log changes in their own run directory.

## Report files

Grok writes two separate Markdown reports per local date.
Use workflow/templates/filled-forms.md and workflow/templates/run-log.md.
Keep per-role filled-form.md for detailed evidence.
The daily report must show actual answers, not only links or generic success labels.
Include incomplete attempts so the owner can audit mistakes.

