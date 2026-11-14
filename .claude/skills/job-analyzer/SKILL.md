---
name: job-analyzer
description: Analyze a supplied JD against the active resume and evidence paths for this repository's Claude and Grokbot job workflow.
---

Read workflow/README.md and workflow/profile.json before work. If the profile is missing, copy workflow/profile.example.json and ask the owner to fill their facts and preferences. Explicit current user instructions take precedence.

Analyze a supplied JD against the active resume and evidence paths. Identify required skills, optional skills, demonstrated evidence, gaps, eligibility questions and deadline. Tailor the existing resume source, compile with the configured build command when available, inspect the rendered PDF and extracted text, and write review.md showing factual changes. Keep each company version separate. Prepare answers and a draft execution task. Use upstream analysis sections for depth, with local files as the resume source.

Use the active owner's source material. Follow the configured role, location and seniority preferences. Unknown work-authorization answers stay unresolved until supplied by the owner. Resume bullets and numbers must be supported by source material. Record sources and gaps.

UPSTREAM.md preserves the original third-party workflow. Its author's profile, seniority, remote-only rules, Google Drive setup, company-wide exclusions and direct browser submission instructions are reference examples. This repository uses the configured profile, local resume sources and the Claude/Grokbot division of work above. Tool names in the upstream text require actual available equivalents.

