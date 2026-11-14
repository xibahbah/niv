# Grok execution log — <local date>

Worker: <worker>
Timezone: <timezone>
Handoff: <path and commit>
Start: <timestamp>
End: <timestamp>

## Counts

| Metric | Count |
| --- | ---: |
| Claimed tasks | 0 |
| Filled forms | 0 |
| Confirmed submissions | 0 |
| Needs input | 0 |
| CAPTCHA blocks | 0 |
| Other blocks | 0 |
| Ambiguous submissions | 0 |
| Duplicates skipped | 0 |

## Events

| Time | Task / attempt | Action | Observed result | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| <timestamp> | <ID> | <action> | <result> | <state> | <path> |

## CAPTCHA and failure details

### <attempt ID>

- Platform and URL: <value>
- Provider or error class: <value or unknown>
- Visible error: <exact text>
- Attempts: <count and timestamps>
- Observed behavior: <what happened>
- Suspected cause: <hypothesis or unknown>
- Evidence for cause: <evidence or none>
- Resume retained after failure: <yes/no/unknown>
- Submission may have occurred: <yes/no/unknown>
- Recovery attempted: <action>
- Next action: <specific action>
- Screenshot or receipt: <path>

## Lessons and unresolved facts

Use the durable learning format in MEMORY.md.
Record source, scope, certainty, and any superseded rule.
Do not change personal answers from an inference.

## Reconciliation

- Form report: <filled-forms.md>
- Application log updates: <row IDs>
- Task updates: <paths>
- Commit: <SHA>
- Remaining work: <list>

