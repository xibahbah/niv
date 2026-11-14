# Publish or transfer this template

Only the sanitized release files belong in a public repository.
Never push the private working repository or its Git history.
Do not change a private candidate repository to public.

## Export

Run scripts/export_public.py with a new destination.
It checks the release allowlist and reviewed file hashes.
Files outside the allowlist are never copied.
If a file changed, review its content before updating the manifest.
The hash check cannot detect personal data already approved into a new manifest.

## Publish from the clean export

After checking GitHub authentication:

```sh
git init -b main
git add .
git commit -m "Publish reusable job-search workflow"
gh repo create OWNER/REPOSITORY --public --source=. --remote=origin --push
```

Run these commands only inside the clean export.
Replace OWNER/REPOSITORY with the intended public destination.
Check the resulting repository's visibility and file list.

## Start a private instance

Create a new private repository from a clean export without copying public Git history.
Run bootstrap.py and answer ONBOARDING.md privately.
Check the private remote before tracking generated owner files.
Retain ignores for credentials and temporary outputs.
Connect each agent to this private instance.
The public template remains a generic reference.

## Release maintenance

Review changed source files for personal data, credentials, and private paths.
Update release-manifest.json only after that review.
Preserve all third-party license files.
Rerun the export and privacy checks before publishing.
