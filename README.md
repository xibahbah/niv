# Job Search Workflow

A reusable workflow for evidence-based job research and audited applications.
Use any capable research agent and a separate browser agent.
This repository contains no candidate profile or application history.

## Start here

1. Read ONBOARDING.md with your agent.
2. Run `python3 scripts/bootstrap.py`.
3. Fill the generated OWNER.md and workflow/profile.json with your own checked facts.
4. Read workflow/daily-run.md and docs/OPERATIONS.md.
5. Check capabilities with `python3 scripts/preflight.py`.
6. Run a small research-only trial before scheduling.
7. Configure your own authorization in workflow/daily-policy.json.

The default permits no submissions or messages.
An application cap is a limit, not permission.

## Included

- Eight skill folders, with upstream licenses and provenance.
- Public ATS discovery: Greenhouse, Ashby, Lever, RemoteOK, and Remotive.
- Agent Reach instructions and integration notes.
- Evidence, handoff, application, contact, and audit templates.
- Onboarding, durable memory, error recovery, and concurrency rules.
- Bootstrap, preflight, public export, and manifest validation programs.
- Separate research and Grok prompts.

## Daily flow

Research refreshes the backlog and verifies exact official job descriptions.
It records exclusions, unresolved conditions, and complete application packets.
The browser worker reads the handoff, checks authorization, and audits each form.
It saves separate filled-form and execution reports.

A Markdown prompt does not start a scheduler.
See docs/SCHEDULING.md for runtime and model acceptance checks.
This template does not provision cloud execution, model selection, or a Grok service.

## Private working data

Keep your actual working copy in private storage.
The default Git rules ignore OWNER.md, profiles, scans, applications, outreach, and logs.
For shared agent access, create a separate private repository.
Only there, deliberately track the required private files after checking visibility.
Never change this public template into your application database.

## Commands

```sh
python3 scripts/bootstrap.py
python3 scripts/preflight.py
python3 .claude/skills/job-search/find_jobs.py --config workflow/profile.json --output workflow/runs/candidates.json
python3 scripts/validate_handoff.py path/to/manifest.json
python3 scripts/export_public.py /tmp/job-workflow-public
```

ATS output contains leads, not checked eligibility.
Resume rendering requires your chosen compiler and a blank template.
Candidate-specific resume designs are deliberately excluded.

See THIRD_PARTY.md for attribution and docs/LESSONS.md for reusable lessons.
See docs/PROGRAMS.md for the program inventory and validation scope.
