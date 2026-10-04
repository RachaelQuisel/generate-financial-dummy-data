---
name: generate-financial-dummy-data
description: Interactively create synthetic financial grant records for a user-selected system or generate an import file. Gather missing destination, schema, quantity, values, and scenario details before running; scope is grants and required supporting records.
---

# Generate Financial Dummy Data

Guide the user from a test scenario to usable dummy grants. This version covers grants and required supporting records. It does not create payouts or bills. No platform, organization, vendor, fiscal year, or status is a global default.

## Start with an interactive intake

Every new run begins with a short conversational setup. Acknowledge the details already provided, then ask for the missing inputs. Do not silently select an application, invent an organization, choose approval states, or start writes from an incomplete request.

Ask one to three focused questions at a time, using suggested choices where helpful. Wait for the answers before work that depends on them; elapsed time is not an answer. Read-only schema inspection may continue when the destination is known. Skip questions the user already answered.

Collect the following information as needed:

| Input | Prompt to adapt |
| --- | --- |
| Output and destination | "Should I create records in a connected system or prepare a file? Which application, workspace, database, or table should I use?" |
| Quantity and purpose | "How many grants do you need, and what scenario should they represent?" |
| Financial values | "What amounts and currency should I use? Give exact amounts or a range and distribution." |
| Relationships | "Which organizations, applicants, programs, or funding cycles should these grants belong to? Should I reuse existing records or generate fictional supporting records?" |
| States and dates | "Which grant states and date range should the test cover?" |
| Structure | "Can I inspect the destination's schema, or should I use a field list, template, or example you provide?" |

Ask follow-ups only when the schema or scenario requires them. If requested, recommended, and awarded amounts are distinct, resolve which amounts belong in which fields. Ask about vendor mappings only when relevant to the scenario. For file output, resolve format and columns; for connected-system output, verify the exact destination and available access. Use supported connection flows rather than asking for credentials in chat.

If a user requests a different financial record type, explain this version's grant scope and resolve whether they want a grant scenario. Do not reinterpret an invoice or expense as a grant.

## Establish a concrete batch

Inspect the current schema, required fields, select choices, generated identifiers, and relationships using available connectors, APIs, CLIs, or supported browser tools. Do not assume that a Program must be created per grant or that one amount should fill every financial field.

Summarize the destination, record count, value rules, relationships, and desired states in plain language before generation. Proceed once the user's supplied instructions cover the work; do not add a universal confirmation step. When key inputs conflict or remain missing, ask rather than guessing.

Use fictional names and an identifiable test label where suitable. A label marks dummy data; it does not disable automations. Inspect relevant triggers when the selected values could send notifications, submit applications, or initiate financial actions. Grant creation does not authorize those additional actions or changes to shared automation rules.

## Generate and verify

- Reuse the requested existing relationships. Create fictional supporting records only when required and included in the requested setup.
- Apply the supplied exact values or generation rules. Keep related amounts, dates, and statuses consistent with the scenario. Do not manufacture real approval history or copy transaction identifiers.
- In a connected system, write the approved scope of grants and let the system generate computed fields and identifiers. Read back each grant's saved values and resolved links.
- For file output, write the chosen format and verify row counts, types, financial values, and relationship references. Make clear that a generated file has not been imported into an application.

When application visibility is part of the request, also verify the records in that interface. Search by returned identifiers or test labels, account for filters and pagination, and inspect actual lookup dependencies when records are missing. Repair evidence-backed omissions on the new dummy records within scope. Do not expand into schema redesign or application repair.

Keep returned IDs and a distinctive batch label. After an unknown create outcome, inspect for that batch before retrying. Finish confirmed partial writes using their IDs and retry only records confirmed absent. Stop an uncertain creation attempt rather than creating duplicates.

## Return the result

Provide record links or the generated file, count, financial values, and the checks performed. Distinguish file-generated, records-saved, and application-visible outcomes. Report any verification gap and the information or access needed to resolve it.
