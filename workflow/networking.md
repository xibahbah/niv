# Networking and Gmail — Claude owner

## Start
Read profile.json, the current application log and the relevant job folder. Use the Gmail connector in the user's Claude environment. Confirm its actual search, read, draft, attachment and send capabilities before relying on them. A connected account alone does not establish all of these capabilities. Missing Gmail access must not block job scanning. Keep drafts in GitHub when Gmail draft creation is unavailable.

## Contact research
For up to profile.networking.daily_draft_target priority roles, search existing Gmail threads using the company name/domain, job ID and known contact names. Read relevant threads to verify the person's full name, exact address, company relationship and last interaction. Search Sent and drafts before creating outreach. Check profile.networking.relationship_mode. For cold_outreach, assume no established contacts: research relevant recruiters, team members and alumni publicly, then use Gmail to check prior outreach and create drafts. Shared alumni status alone is not an existing relationship. If the owner later supplies a real contact, use that verified history. Confirm current affiliation from a reliable source when uncertain. Record where each address came from. Never guess an email address from a naming convention or describe a stranger as a connection.
Use public sources for additional research. If only LinkedIn provides the needed interaction, prepare a queued browser request for Grokbot after its existing application work. Gmail email drafting and approved sending stay with Claude.

## Message choice
For someone who knows the owner, ask directly and politely whether they would feel comfortable referring the owner to the specific role. Include the posting, a brief fit explanation and the correct resume.
For a new contact, choose one specific ask based on the context: a team question, brief conversation, or referral if they are comfortable. Do not require a preliminary meeting.
For a recruiter, use the exact job ID and current application state. A prepared resume is not a submitted application. For an already submitted role, say when it was submitted and ask about the team or next step.
Use one or two verified evidence points and concise, natural language. Check dated claims such as incoming employment against current evidence. Mention attachments only when the actual draft includes them. Existing outreach/referral-templates.md is a wording reference when present, not a source of verified current facts.

## Draft and approve
Create one record per contact/company using outreach/records/<company>-<contact-key>.json and the contact.example.json shape. Keep one active contact record across multiple related jobs and channels. Store the proposed subject/body, sources, job IDs and the selected resume path. Create or update a Gmail draft if the connector supports it and record its real draft ID.
The current workflow uses review-before-send. The owner may approve one draft or a clearly identified batch. Approval covers the recipient, channel, final text and attachments. Revise approval if these change materially. Once approved, Claude can send using its available Gmail connector. Read the latest thread and approval immediately before sending.
After a successful send, record the returned message/thread ID and timestamp. If sending times out or the outcome is ambiguous, set verify_sent and search Sent before retrying. A draft ID does not prove sending. Never retry a send solely because a GitHub write failed.

## Replies and follow-up
Check tracked threads for replies, classify referral offered / resume requested / conversation requested / declined / no response, and draft the appropriate next step. Record the actual referral separately from merely asking for one. Bring time-sensitive questions and interview invitations to the owner's review summary.
After the configured follow-up interval, create one follow-up draft in the existing thread if there has been no reply. Recheck Gmail first. Stop follow-ups after a decline, opt-out, reply, or the configured maximum. A suggested call time is a draft until the owner confirms availability.

## Shared-repository coordination
Claude writes new scan results under scans/<date>/<run-id>/, new candidate packages in new application folders, and networking records under outreach/records/. Grokbot continues its already assigned application packets and result files. Read applications/log.csv for deduplication, and leave its ongoing updates to the active application worker. Put proposed new log rows in the scan run directory for later reconciliation.
Use distinct filenames per run. Pull the latest branch before committing. If a push conflicts, rebase and preserve both workers' records. Re-read a contact record and Gmail thread before any external action. Use one Gmail-sending worker per account.
Store only job-relevant contact facts, draft text and Gmail message references in the private repo. Gmail credentials and unrelated mailbox contents remain outside it.

## Daily outputs
Morning review summary: new shortlisted jobs, resume changes, new Gmail drafts, replies needing action, follow-ups due, and blocked questions. Include GitHub record paths and available Gmail draft links/IDs.
The configured target and follow-up timing are adjustable starting defaults. This document does not schedule or run Claude.

