# Programs and scope

| Program | Purpose | Limits |
| --- | --- | --- |
| scripts/bootstrap.py | Create missing private working files | Never overwrites owner answers |
| scripts/preflight.py | Inventory available commands and files | Does not prove authentication or live access |
| .claude/skills/job-search/find_jobs.py | Collect public ATS leads | Every lead still needs official JD review |
| scripts/filter_listings.py | Filter downloaded listing arrays and known URLs | No inferred eligibility from index metadata |
| scripts/validate_handoff.py | Check counts and evidence paths | Cannot check facts or permission |
| scripts/export_public.py | Export a reviewed file allowlist | Cannot approve changes for you |
| .claude/skills/asd-ste100/scripts/ste-lint.py | Check writing structure | Does not check factual claims |

## Listing index import

Download the public index through your available GitHub or web tools.
Keep the source URL and retrieval date with the downloaded file.
Then run:

```sh
python3 scripts/filter_listings.py path/to/listings.json --config workflow/profile.json --log applications/log.csv --max-days 30 --output workflow/runs/index-leads.json
```

The script adapts the earlier listing filter without fixed candidate dates or personal eligibility rules.
It retains unknown dates and leaves eligibility to exact JD review.
It preserves query parameters that can identify separate postings.
Alias URLs still need ATS identity reconciliation.

## Resume tools

The original private workspace contains candidate-specific LaTeX sources and generators.
Those programs embed personal content and are not part of this public release.
Supply a blank resume template and set profile.build_command for your renderer.
Compile and inspect the resulting PDF before marking a packet ready.
A reusable resume design and renderer can be added separately.
Do not copy private generators into the public repository.

## Validation performed

Python syntax checks passed.
A fixture checked that the Lever adapter retains requirement lists and additional text.
A fixture checked that bootstrap preserves an existing owner record and defaults to no submission authorization.
A fixture checked that invalid handoffs fail validation.
Private-file sentinel tests passed for the public exporter.
A modified release file caused export to stop before creating an output directory.
New core prose passed the writing linter with zero findings.
Live scheduled execution and external submissions were not tested.
