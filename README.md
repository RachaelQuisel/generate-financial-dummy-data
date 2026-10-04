# Generate Financial Dummy Data

*Dummy grants, built for the test you actually want to run.*

I built this plugin to turn a grant scenario into usable test records through a conversation. It asks for the missing details before creating anything: destination, quantity, financial values, relationships, dates, and grant states.

- Start with a connected system or request an import file.
- Supply exact amounts or rules for generating them.
- Reuse existing relationships or request fictional supporting records.
- Receive record links or a file with a clear verification result.

Invoke `generate-financial-dummy-data` and describe your scenario. For example: “Help me create three dummy grants for a fictional organization, with awards of 250, 500, and 750 USD.” The setup will ask where they should go and which other details the target needs.

This version creates grants and required supporting records. It does not create payouts or bills. Connected-system use requires available tools and access to the selected destination; the plugin does not bundle credentials or connectors.

The hand-drawn icon follows the Soft Index style. `scripts/render_icon.py` uses the original geometry and rendering helpers from Ghibli Icon Maker. Render it with Python and Pillow installed.
