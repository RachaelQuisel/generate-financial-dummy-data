## Trigger

- The user asks for test grants or starts Generate Financial Dummy Data.

## Inputs

- The destination identifies the application and table, or the file format and columns.
- The grant count, amounts, currency, dates, and states define the test.
- The selected organization, program, and funding year supply any required relationships.
- The user chooses existing supporting records or fictional records when the target needs them.

## What happens

1. The plugin acknowledges supplied details. It asks up to three questions about missing information. With no details, it asks for the destination, count, and amounts with currency.
2. It waits for answers. It remembers earlier answers and uses revised choices. It stops if the user pauses or cancels.
3. For application output, it checks access, fields, and relationships. For file output, it resolves the requested columns. If a required detail is missing or conflicts with the target, it asks before continuing.
4. It checks relevant triggers when the chosen values could start another action. Creating grants does not authorize notifications, submissions, payouts, or bills. It preserves shared automation rules.
5. It creates the requested grants and any requested supporting records. It uses a test label where supported. The label does not disable automations.
6. For saved records, it reads back the amounts and relationships. It checks the application view when visibility is part of the request. For a file, it checks rows, field types, amounts, and references.
7. After an uncertain write, it searches using saved identifiers and the test label before retrying. It stops if it cannot establish whether a record exists.
8. It returns the result with the checks performed and any unresolved result. A file is described as not imported.

## Outputs

- Saved grant links in the selected application, or an import file in the chosen location.
- A record count, financial values, and verification results.
- Two fictional worked examples explain grant relationships and separate amount fields. They are instructions, not live test evidence.
