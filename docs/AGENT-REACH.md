# Agent Reach integration

Agent Reach is an optional read-only source adapter.
The included skill files describe its commands and limits.
Its executable and dependencies must exist on the actual runner.

Upstream: https://github.com/Panniantong/Agent-Reach
Reviewed version: 1.6.0.
Read the bundled skill and upstream installation guide before setup.

## Inspect first

```sh
agent-reach --help
agent-reach doctor
agent-reach channels
```

Doctor checks installation state. It does not prove live access.
Use a supported live check for the channel you need.
Run these checks on the scheduled host, not only a laptop.

## Installation

The upstream guide warns against the unrelated PyPI package with the same name.
Use the upstream GitHub release installer after reviewing its current instructions:

```sh
uv tool install https://github.com/Panniantong/Agent-Reach/releases/latest/download/agent-reach.zip
agent-reach setup
```

Record the installed version. Updates require the owner's chosen update policy.
This template installs no programs automatically.

## LinkedIn

Read the declared jobs and read parameters from agent-reach channels.
Use public search and readable public job details first.
The LinkedIn channel supports job search and JD reading.
It does not establish recruiter-profile scraping or message capability.
Follow the result's error code and documented recovery.
Stop on login, platform verification, busy, or rate-limit blocks.
Do not rotate accounts or backends to evade a block.

## ATS sources

The included ATS script handles configured Greenhouse, Ashby, and Lever feeds directly.
Agent Reach is not required for these public adapters.
Use exact official job text to check leads from any source.
Preserve access failures in the handoff.
