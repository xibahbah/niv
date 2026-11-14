# Research scheduler prompt

Read AGENTS.md, MEMORY.md, OWNER.md, workflow/daily-policy.json, workflow/profile.json, and workflow/LATEST.md.
Read recent execution logs and relevant skill instructions, including Agent Reach when available.
Refresh existing leads before broad discovery.
Review the configured daily target using exact official job descriptions.
Apply the current owner's filters and deduplicate against existing tasks and submissions.
Save full JD evidence, requirement mapping, conditions, public contact sources, and access errors.
Prepare complete packets only from supported owner facts.
Compile and inspect the selected resumes before marking packets ready.
Publish a handoff and manifest under a unique scans/<date>/<run-id>/ directory.
Update workflow/LATEST.md only after those files exist.
Report distinct reviewed, excluded, conditional, hold, ready, and handed-off counts.
Preserve other workers' changes.
Do not apply or send messages from the research task.
Use the host-selected required model and runtime.
If those requirements cannot be confirmed, report the blocker rather than claim compliant execution.
