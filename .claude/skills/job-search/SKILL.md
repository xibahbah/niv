---
name: job-search
description: Gather fresh jobs across configured public ATS feeds for this repository's Claude and Grokbot job workflow.
---

Read workflow/README.md and workflow/profile.json before work. If the profile is missing, copy workflow/profile.example.json and ask the owner to fill their facts and preferences. Explicit current user instructions take precedence.

Gather fresh jobs across configured public ATS feeds. Run python3 .claude/skills/job-search/find_jobs.py --config workflow/profile.json --output workflow/runs/candidates.json. Review full JDs for promising matches, deduplicate against applications/log.csv by posting URL or ATS ID, and rank using the active profile. Preserve separate openings at the same company. Report failed sources alongside results. Prepare at most the configured daily target.

Use the active owner's source material. Follow the configured role, location and seniority preferences. Unknown work-authorization answers stay unresolved until supplied by the owner. Resume bullets and numbers must be supported by source material. Record sources and gaps.

UPSTREAM.md preserves the original third-party workflow. Its author's profile, seniority, remote-only rules, Google Drive setup, company-wide exclusions and direct browser submission instructions are reference examples. This repository uses the configured profile, local resume sources and the Claude/Grokbot division of work above. Tool names in the upstream text require actual available equivalents.

