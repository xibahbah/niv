# Operating procedure

## Read order

Read AGENTS.md, MEMORY.md, OWNER.md, and workflow/daily-policy.json.
Then read workflow/profile.json, workflow/LATEST.md, and recent execution logs.
Load relevant skill instructions before using them.
Treat upstream examples as examples, not the new owner's facts or permission.

## Research and screening

Refresh unresolved backlog entries before collecting more leads.
Search official employer boards and public ATS feeds first.
Use public search and LinkedIn results to discover exact employer postings.
Use Agent Reach when it fills an actual access or body-text gap.

Save the official URL, employer, ATS ID, retrieval time, and readable full JD.
Record live status and the access method.
Keep a search snippet or JavaScript shell labeled as incomplete evidence.
Do not mark a 403 response as a closed job.

Evaluate each mandatory requirement against OWNER.md.
Record degree, experience, location, pay, authorization, availability, and evidence of fit.
Distinguish mandatory requirements from preferences.
Evaluate explicit degree or experience alternatives before exclusion.
Do not count internships as required full-time experience without support.

Use conditional status for unresolved salary, sponsorship, or start-date compatibility.
Use excluded for a demonstrated hard conflict.
Use hold for incomplete source access or missing owner answers.
Use ready only when eligibility, answers, and materials are complete.

## Deduplication

Use employer plus ATS identifier where available.
Save alias URLs for the same posting.
Preserve separate openings at the same employer.
Do not deduplicate by a generic path segment such as jobs.
Check current application logs, packets, owner skips, and company limits.
If identity is uncertain, flag possible_duplicate and investigate.

## Materials and handoff

Map at least two requirements to supported owner evidence.
Tailor wording without inventing metrics, production experience, or employment status.
Compile the resume and inspect the actual PDF.
Check contact details, dates, page count, overflow, and uploaded filename.
Save jd.md, review.md, answers.md, task.json, and the selected resume.

Use workflow/templates/HANDOFF.md and manifest.example.json.
Each count has a distinct meaning. Do not add overlapping counts.
Commit immutable evidence before changing workflow/LATEST.md.
Publish the handoff commit and packet paths for the browser worker.

## Browser execution

Check standing scope or per-task approval from the new owner.
Claim one role before navigation and recheck current submission totals.
Inspect all actual form fields, including prefilled sections and dropdown values.
Save expanded free text, employment dates, checkbox states, and resume filename.
Compare actual values against intended values with source references.
Capture every page before submission.

Write a per-role audit and both daily reports, including failed attempts.
Only confirmation evidence supports submitted status.
If a result is ambiguous, use verify_submission and reconcile before retrying.
A Git push failure never justifies another external submission.

## Concurrency

Use unique scan run directories and per-worker event IDs.
Use task claims with worker ID, claim time, and lease expiry.
For multiple execution workers, use one transactional claim store or one queue consumer.
A plain file lease without atomic coordination is not a distributed lock.
Re-read shared state before committing. Preserve other workers' events.
Never force-push or discard another worker's log.
Count the daily cap across all workers in the configured timezone.

## Public contacts

Record the exact public source URL and verification date for each hiring contact.
Do not guess email addresses or claim an existing relationship.
Check previous messages and drafts before authorized outreach.
Research permission alone does not authorize sending.
