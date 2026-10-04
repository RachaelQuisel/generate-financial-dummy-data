# Examples adapted from project documentation

These examples show how grant relationships and financial fields affect the conversation. They use fictional names and financial values. The field names illustrate one data model. Check the chosen application's fields before using them. Do not use these examples as defaults for another request.

## Example 1: A recurring program across two years

The documented model keeps one Program across funding cycles. Each funding year has a separate Grant. Each Program belongs to one Organization.

User:

"Create two test grants for Example Organization. Reuse its existing Example Program. Use an award of 350 USD for 2025–2026 and 550 USD for 2026–2027. I want to find them in the grant tracker."

Assistant:

"I'll reuse Example Program for both grants. I'll use awards of 350 and 550 USD for the two years you specified.

Which application and table contain the grant tracker?

Which grant and report states should I use?"

Wait for the answers. Then inspect the target's fields and verify the existing Program and Organization. If the target requires a different relationship, explain the conflict before creating records.

Expected checks:

- Both Grants link to the selected Program.
- The Program resolves to the selected Organization.
- Each Grant has the correct year and award amount.
- No duplicate Program is created for this request.
- The tracker can find both Grants through its organization and year filters.
- Each saved Grant is identified by its own record identifier. A displayed grant number is not assumed to be unique.

## Example 2: Different requested, recommended, and awarded amounts

The documented review workflow keeps Amount Requested, Amount Recommended, and Amount Awarded as separate fields. One amount must not replace the other two.

User:

"Create one test grant for Example Organization in 2026–2027. Set Amount Requested to 1,200 USD, Amount Recommended to 900 USD, and Amount Awarded to 700 USD."

Assistant:

"I'll keep the three amounts separate: requested 1,200 USD, recommended 900 USD, and awarded 700 USD.

Which application and table should I use?

Which Program should the Grant belong to?

Which grant and report states should I use?"

Wait for the answers. Verify that the target supports the three distinct amount fields. Ask about any incompatible field or status before writing. Inspect relevant triggers before selecting test states that could start another action.

Expected checks:

- Amount Requested remains 1,200 USD.
- Amount Recommended remains 900 USD.
- Amount Awarded remains 700 USD.
- The Grant resolves to the chosen Organization, Program, and year.
- Any requested application view shows the correct amount in each field.
- No payout, bill, or real approval history is created.

These are worked instructions. They are not evidence of a live test run.
