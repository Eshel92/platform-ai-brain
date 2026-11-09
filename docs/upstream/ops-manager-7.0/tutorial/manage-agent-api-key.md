<!-- Converted from tutorial/manage-agent-api-key.txt (reStructuredText). Includes are inlined. -->

# Manage Agent API Keys

## Overview

**Note:** New Agent API Keys Model

With the new Agent API Key model, multiple Agent API Keys can be
associated with a project. This gives users the ability to perform
Agent key rotation.

In addition, the new Agent API Key model improves on security as the
keys are displayed only once upon creation and Ops Manager  no longer
stores or displays these keys.

An Agent API key is a unique identifier that the Automation,
Monitoring, and Backup Agents for a project use to authenticate
themselves to Ops Manager. A project can have multiple Agent API keys. Any of
the project's agents can use any of the Agent API keys associated with
the project.

## View Agent API Keys

For keys created using the new Agent API Key Model:
   You can manage your Agent API keys from the Agent API
   Keys tab. From the Deployment view, click on the
   Agents tab, and then the Agent API Keys tab.

   The tab displays a list of existing Agent API keys. The keys
   themselves are redacted. However, the list displays the description
   and creation details.

## Create Agent API Key

**Note:** Only the project's owner can create an Agent API key. You can

generate an Agent API Key while installing an agent if you 
are the project owner and the project has either no Agent API keys
or just the Original Group API key.

**Step 1: Go to the Agent API Keys Tab.**

From the Deployment view, click on the Agents tab, and then Agent API Keys.

**Step 2: Click Generate.**

**Step 3: Enter a description.**

Enter a description for the key. The description acts as an identifier for the key as
the key is shown only once upon generation.

The description has a limit of 1000 characters.

**Step 4: Copy and record the key.**

Copy and record the key when it is generated.

**Important:**

When you generate an Agent API Key, Ops Manager displays it **one time
only**. You must copy this key. Treat it like a password; store
it in a secure place. Ops Manager never displays the full key again.

After you have  recorded the key, click Close.

## Delete Agent API Key

**Note:** Only the project's owner can delete an Agent API key.

**Step 1: Go to the Agent API Keys Tab.**

From the Deployment view, click on the Agents tab, and then  Agent API Keys.

**Step 2: Delete the Agent API key.**

For the key you wish to delete, click the gear button under the
Actions column and select Delete.

**Step 3: Confirm.**
