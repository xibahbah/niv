---
name: job-crawler
description: Find the best matching roles at a specific company for this repository's Claude and Grokbot job workflow.
---

Read workflow/README.md and workflow/profile.json before work. If the profile is missing, copy workflow/profile.example.json and ask the owner to fill their facts and preferences. Explicit current user instructions take precedence.

Find the best matching roles at a specific company. Use public ATS endpoints from claude-jobs first and public web research second. Rank against the active profile. If accessing a page requires interactive browser use, write a precise Grokbot lookup request with its URL and requested fields. Read the upstream workflow for ATS discovery methods.

Use the active owner's source material. Follow the configured role, location and seniority preferences. Unknown work-authorization answers stay unresolved until supplied by the owner. Resume bullets and numbers must be supported by source material. Record sources and gaps.

UPSTREAM.md preserves the original third-party workflow. Its author's profile, seniority, remote-only rules, Google Drive setup, company-wide exclusions and direct browser submission instructions are reference examples. This repository uses the configured profile, local resume sources and the Claude/Grokbot division of work above. Tool names in the upstream text require actual available equivalents.

