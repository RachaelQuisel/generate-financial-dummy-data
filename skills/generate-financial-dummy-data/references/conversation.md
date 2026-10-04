# Conversation examples

These examples show how to ask for missing details. They do not choose defaults for a new request.

## When the user gives no details

User: "Generate financial dummy data."

Assistant:

"Where should I put the test grants: in an application or in a file?

How many grants do you need?

What amounts and currency should I use?"

Wait for the answers. Do not create records or a file yet.

## When the user chooses a file

User: "A CSV file with three grants. Use awards of 250, 500, and 750 USD."

Assistant:

"I'll use three grants with awards of 250, 500, and 750 USD. CSV means comma-separated values.

Which columns should the file include? You can provide a template or a field list.

Should the grants use an existing organization or a fictional organization?

Which dates and grant states should I use?"

Wait for the missing details. Do not assume a column list, organization, date range, or approval state.

## When the user chooses an application

User: "Put two grants in our grant tracker. Use awards of 400 and 600 USD."

Assistant:

"I'll use two grants with awards of 400 and 600 USD.

Which application and table contain your grant tracker?

Which organization should the grants belong to?

Which year and grant states should I use?"

After the target is known, inspect its fields. Ask a focused follow-up if the supplied values do not match the required fields.

## When an answer changes

User: "Make the second grant 800 USD instead."

Assistant: "I'll use 800 USD for the second grant."

Keep the other answers. If records were already saved, explain that fact before changing them. Resolve whether the user intends to update that record or create another one when the intent is unclear.

## When a result cannot be verified

Assistant: "The two grants were saved. I could not open the application view. Here are the record links. I need access to that view to check visibility."

State the verified result and the unresolved check. Do not claim that saved records are visible in an application without checking the view.
