---
name: generate-financial-dummy-data
description: Create test grants through a conversation. Ask for missing details about the destination, grant count, amounts, and test scenario. Create records in the chosen application or prepare an import file. This version covers grants and required supporting records.
---

# Generate Financial Dummy Data

Create the test grants the user requests. Keep this workflow limited to grants and required supporting records. Do not create payouts or bills.

## Start the conversation

Read [references/conversation.md](references/conversation.md) for the opening questions and follow-up examples.

- In the first reply, acknowledge any details the user supplied. Ask up to three questions about missing information. Respond with questions rather than a plan alone.
- If the user supplied no details, ask where the grants should go, how many are needed, and which amounts and currency to use.
- Wait for the answers before any work that depends on them. Time passing does not answer a question.
- After each reply, acknowledge the new information. Ask up to three questions about the remaining details. Do not repeat answered questions or show the whole checklist at once.
- If the destination is known, inspect its fields without changing records. Use that information to choose useful follow-up questions.
- If the user changes an answer, use the new answer. If the user pauses or cancels the request, stop creating records.
- If all required details are already supplied, state the requested setup and proceed. Do not add a routine approval question.

Use common words in every reply. Use complete sentences. Keep each question short. Explain a required technical term when it first appears. Preserve product names, field names, and commands.

## Resolve the remaining details

- For application output, identify the exact application, workspace, database, and table. Use the available tools to confirm access. Use the supported connection process if access is missing. Do not ask for credentials in chat.
- For file output, ask for the format and columns. The user can supply a template or a field list. A schema is the list of fields and their allowed values.
- Resolve the grant count, amounts, currency, dates, and grant states. Use exact amounts or the user's rules for generating them.
- Identify the organization, applicant, program, or funding cycle when the target requires it. Ask whether to reuse existing records or create fictional supporting records.
- If requested, recommended, and awarded amounts are separate fields, resolve which values belong in each field.
- Ask about vendor links only when the target or test requires them. Do not choose an organization, year, or status from a previous project.
- If the user asks for another financial record type, explain the grant scope. Do not treat an invoice or expense as a grant.

## Create the test data

1. Inspect the target's current fields and relationships. Confirm which values are required. Let the application generate calculated fields and record numbers.
2. State the destination, grant count, amounts, relationships, and test states. Ask about conflicting or missing requirements before generation.
3. Inspect relevant automation triggers when the selected values could send a notification, submit an application, or start a financial action. Creating test grants does not authorize those actions. Do not change shared automation rules as part of this workflow.
4. Use a test label where the target supports it. Explain that the label does not disable automations. Reuse the relationships the user selected. Create supporting records only when the requested setup includes them.
5. Apply the requested values. Keep related amounts, dates, and states consistent. Do not copy real transaction identifiers or staff approval history.
6. For application output, save the grants. Read back their values and links. If the user expects them in an interface, check that view too. Account for filters and multiple result pages.
7. For file output, create the file. Check the row count, field types, amounts, and relationship references. State that the file has not been imported.
8. If an application view omits a saved grant, inspect the fields and filters it reads. Correct missing values on the new records when the evidence supports that change. Do not redesign the application or its fields.
9. Keep returned record identifiers and a unique label for the group of grants. After an uncertain write, search for that group before retrying. Continue records that were partly created by using their saved identifiers. Retry only records confirmed absent. Stop the attempt if existence cannot be established.

## Respond with the result

Return the record links or file. State the count, financial values, and checks performed. Distinguish a created file from saved records and verified interface visibility. State any unresolved check. Explain what is needed to complete it.
