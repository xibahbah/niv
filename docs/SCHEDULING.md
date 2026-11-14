# Scheduling without the owner's computer

A scheduler, an agent runtime, and repository access are separate requirements.
This template provisions none of them automatically.

## Required acceptance checks

1. Select a managed cloud runtime or a hosted runner.
2. Check it works while the owner's computer stays disconnected.
3. Select the requested model in the runner's actual configuration.
4. Check the recorded model on a trial run.
5. Check private repository reads and writes.
6. Check network access and required research tools.
7. Produce a real handoff and inspect it.
8. Record the scheduler ID, timezone, next run, runtime, and model.

Writing Sol in a prompt does not select Sol.
Do not silently substitute Astra when the owner requires Sol.
If the host exposes no model or runtime controls, report setup as blocked.

## Suggested cadence

Research: 19:00 in the owner's timezone.
Browser execution: the following morning, after checking for a completed handoff.
Use a timezone-aware scheduler when daylight saving changes matter.
These times are suggestions, not active tasks.

## Separate Grok runner

Use workflow/grokbot-start.md as the execution instruction.
Configure the schedule inside the actual Grok runner.
If it only controls a local computer, it cannot fulfill a computer-off requirement.
Use a supported hosted browser environment only after checking account access.
Do not copy browser cookies or secrets into Git.

## Stale handoff and shortages

If no new complete handoff exists, inspect remaining valid ready packets.
Recheck job availability and authorization before execution.
Report a shortage instead of inventing thirty submissions.
Do not move research-only conditional entries into the execution queue.

## Audit the schedule

Save the schedule, model selector, runtime identity, and last checked output.
Separate enabled, started, completed, and delivered states.
Check the integration before claiming that the research scheduler also starts Grok.
