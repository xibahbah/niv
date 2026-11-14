---
name: job-form-filler
description: Prepare a browser execution packet for Grokbot using the workflow/task for this repository's Claude and Grokbot job workflow.
disable-model-invocation: true
---

Read workflow/README.md and workflow/profile.json before work. If the profile is missing, copy workflow/profile.example.json and ask the owner to fill their facts and preferences. Explicit current user instructions take precedence.

Prepare a browser execution packet for Grokbot using the workflow/task.example.json format. Include exact apply URL, selected resume PDF, approved answers, unresolved questions and explicit approval. Grokbot performs browser navigation, fill, upload and authorized submission. Claude resolves content questions. Use the upstream form-field checklist as a reference. Record confirmation evidence for submitted applications and verify_submission for ambiguous outcomes.

Use the active owner's source material. Follow the configured role, location and seniority preferences. Unknown work-authorization answers stay unresolved until supplied by the owner. Resume bullets and numbers must be supported by source material. Record sources and gaps.

UPSTREAM.md preserves the original third-party workflow. Its author's profile, seniority, remote-only rules, Google Drive setup, company-wide exclusions and direct browser submission instructions are reference examples. This repository uses the configured profile, local resume sources and the Claude/Grokbot division of work above. Tool names in the upstream text require actual available equivalents.

