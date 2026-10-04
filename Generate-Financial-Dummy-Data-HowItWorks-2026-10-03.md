## Trigger

- You start Generate Financial Dummy Data and request test grants.

## Inputs

- Your request identifies the test scenario.
- The destination identifies the application or file output.
- The grant count defines the number of records.
- Amounts and currency define the financial values. You can provide exact values or generation rules.
- Organizations, applicants, programs, and funding cycles define required links.
- Dates and grant states define the test conditions.
- The application's current fields define required values and allowed choices. File output uses your template or field list.
- Application output uses the tools and access available in your session.
- Worked examples illustrate grant relationships and separate financial fields. Their fictional values are not defaults.

## What happens

1. The plugin reads the details you supplied. If a documented example fits the scenario, it uses that example to choose follow-up questions and checks. It still verifies the chosen application's fields.
2. If details are missing, it asks up to three questions. With an empty request, it asks for the destination, grant count, and financial values.
3. It waits for your answers. It then asks about any remaining requirements. It does not repeat answered questions.
4. If you choose an application, it reads that application's fields and relationships. If access is missing, it explains which connection is needed. Work that needs that access stops.
5. If you choose a file, it resolves the format and columns from your template or field list.
6. It resolves required organizations, dates, and grant states. If amount fields have different meanings, it asks which values belong in each field.
7. It states the requested setup. Missing or conflicting details must be resolved before creation.
8. If the selected values could trigger notifications, submissions, or financial actions, it checks the relevant automation. Grant creation does not authorize those actions.
9. It uses a test label where the target supports one. A label does not disable automations.
10. It creates the requested grants and required supporting records. If you pause or cancel, creation stops.
11. For application output, it reads back the saved values and links. It also checks the application view when visibility is part of the request. For file output, it checks the row count, amounts, and relationship references. It checks that each value has the required type, such as text, a number, or a date.
12. If a saved grant is missing from the application view, it checks the fields and filters that view reads. It corrects missing values on the new records when the evidence supports the change. It does not redesign the application.
13. If a write has an uncertain result, it searches for the records before retrying. It retries only records confirmed absent. The attempt stops if existence cannot be established.
14. It reports the checks performed. If a check cannot be completed, it states the verified result and the remaining gap.

## Outputs

- Application output creates grant records in the selected destination. Required supporting records are created only when included in your setup.
- File output creates the requested import file. It does not import that file into an application.
- The chat response provides record links or a file link. It includes the count, financial values, verification results, and unresolved checks.
