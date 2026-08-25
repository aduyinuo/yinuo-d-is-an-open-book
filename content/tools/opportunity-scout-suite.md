# Opportunity Scout Suite

## Components
1. Postdoc and Faculty Scout
2. Funding Scout
3. Conference Scout
4. Micro Opportunities Scout

## Shared architecture
- source ingestion
- entity normalization and deduplication
- profile-fit scoring
- deadline and prep timeline planner
- follow-up tracking

## Output channels
- ranked queues
- weekly digest
- calendar reminders
- GitBook opportunity pages

## Quality constraints
- ranking, not over-filtering
- explainable fit scores
- explicit deadline confidence and source trace

## Status

Built and running. `.github/workflows/opportunities.yml` refreshes the four queues every morning from eleven sources, and commits whatever changed.

<table><thead><tr><th width="230">Component</th><th width="150">Page</th><th>Sources</th></tr></thead><tbody>
<tr><td>Conference Scout</td><td><a href="../overview-4/conference-deadlines.md">Conference deadlines</a></td><td>CCF deadlines, sec-deadlines, ai-deadlines, WikiCFP across security, AI and HCI</td></tr>
<tr><td>Funding Scout</td><td><a href="../overview-4/funding-opportunities.md">Funding opportunities</a></td><td>NSF upcoming-funding feed, Grants.gov search API</td></tr>
<tr><td>Postdoc and Faculty Scout</td><td><a href="../overview-4/postdoc-faculty-opportunities.md">Postdoc/faculty opportunities</a></td><td>AcademicJobsOnline, CS and postdoc listings</td></tr>
<tr><td>Micro Opportunities Scout</td><td><a href="../overview-4/micro-opportunities.md">Micro opportunities</a></td><td>Grants.gov, filtered to travel awards, seed and planning grants, workshops, early career</td></tr>
</tbody></table>

Fit scores carry the terms that produced them. Deadlines carry their confidence: stated by the source, read out of prose, or absent. Nothing is dropped for scoring low.

_Last updated: 2026-08_
