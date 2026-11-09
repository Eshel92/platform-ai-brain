<!-- Converted from tutorial/slack-integration.txt (reStructuredText). Includes are inlined. -->

# Integrate with Slack

You can integrate Ops Manager with  [Slack](https://slack.com/) to receive
Ops Manager alerts in your Slack channel.

## Prerequisites

To integrate Ops Manager with Slack, you must:

- Have a [Slack workspace](https://slack.com/help/articles/206845317-Create-a-Slack-workspace/).

- Have [sufficient permissions to install a Slack app in your workspace](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace/).

## Procedure

To integrate Ops Manager with Slack and receive alerts in your Slack channel:

**Step 1: Retrieve your Ops Manager redirect URL.**

a. Navigate to your Ops Manager Application.
#. In the Ops Manager Application, click the Admin link in the upper
   right corner of the page.
#. Click the General tab and then click
   Ops Manager Config.
#. Copy the URL in the URL To Access Ops Manager.

   **Important:**

   The URL is required in a later step.

**Step 2: Create a Slack app.**

a. Navigate to [Your Apps](https://api.slack.com/apps/).
#. Click Create New App. The Create an app
   modal displays.
#. Click From scratch.
   The Name app & choose workspace modal displays.
#. In the App Name field, enter a name for your Slack app.
#. From the Pick a workspace to develop your app in: dropdown,
   select an available Slack workspace.
#. Click Create App. The app configuration page displays.

**Step 3: Configure app permissions.**

a. Click Permissions under the Add features and
   functionality section. The OAuth & Permissions page displays.
#. Under the Redirect URLs section,
   click Add New Redirect URL. A text field displays.
#. Enter the text description, such as: `URL To Access Ops Manager`
   and click Add.
#. Click Save URLs.
#. Navigate to the Scopes section
   and locate User Token Scopes.
#. Click Add an OAuth Scope. A dropdown list of available
   OAuth scopes displays.
#. From the dropdown, select the chat:write scope.

**Step 4: Manage app distribution.**

a. Return to the app configuration page. 
#. Navigate to the Basic Information section
   and click Manage Distribution.
#. Click Distribute app and review the available
   distribution options.
   You can share your app with your workspace, other workspaces on
   your grid, or other workspaces outside your grid.

**Step 5: Retrieve your Client ID and Client Secret.**

a. Return to the app configuration page.
#. Navigate to the App Credentials section and copy the value
   of the Client ID field.
#. Copy the value of the Client Secret field.

   **Important:**

   The Client ID and Client Secret are required in
   the next step.

**Step 6: Set your Ops Manager slack.oauth2.clientId and slack.oauth2.clientSecret.**

a. Navigate to your Ops Manager Application.
#. In the Ops Manager Application, click the Admin link in the
   upper right corner of the page.
#. Click the General tab
   and then click Ops Manager Config.
#. From the list of tabs at the top of the page, select Custom.
#. In the displayed Key text box,
   enter `slack.oauth2.clientId`.
#. In the displayed Value text box, enter your
   Client ID value.
#. Click Add Option.
#. In the displayed Key text box,
   enter `slack.oauth2.clientSecret`.
#. In the displayed Value text box, enter your
   Client Secret value.
#. Click Save.

**Step 6: Perform the integration.**

Complete the steps to modify Slack integration settings.
