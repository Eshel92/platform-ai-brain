<!-- Converted from tutorial/mms-integrate-with-microsoft-teams.txt (reStructuredText). Includes are inlined. -->

# Integrate with Microsoft Teams

You can integrate Ops Manager with 
[Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software/) 
to receive alerts in your Microsoft Teams channel.

## Prerequisites

To integrate Ops Manager with Microsoft Teams and receive alerts in your Microsoft Teams channel,
you must have a 
[Microsoft Teams account](https://go.microsoft.com/fwlink/p/?linkid=2123761&lm=deeplink&lmsrc=NeutralHomePageWeb&cmpid=FreemiumSignUpHero).

## Procedure

To integrate Ops Manager with Microsoft Teams and receive alerts in your Microsoft Teams channel:

**org:**

**Important:** Required Privileges

To manage all organization alerts, you must have the 
`Organization Owner` role for the organization.

The `Organization Billing Admin` role grants a 
limited authorization to manage billing alerts.

**Step 1: Create the Microsoft Teams incoming webhook.**

a. Navigate to the Microsoft Teams channel where you want to add the webhook.

#. Select ellipsis-h from the top navigation bar. A dropdown menu of available options displays.

#. Select Connectors from the dropdown menu. A modal with available connectors displays.

#. Search for Incoming Webhook and select Add. A modal with information about the Incoming Webhook connector displays.

#. Click Add. The modal closes.

#. Select ellipsis-h from the top navigation bar. A dropdown menu of available options displays.

#. Select Connectors from the dropdown menu. The modal with available connectors displays.

#. Search for Incoming Webhook and select Configure. A configuration modal displays.

#. In the modal, enter a name for your webhook. Optionally, you can upload a unique image to help you identify your webhook.

#. Click Create. 

#. Copy the incoming webhook URL. 

   **Important:**

   Ops Manager requires this URL to configure the integration.

#. Click Done.

**Step 2: Navigate to the Alerts page for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Alerts in the sidebar.

**Step 3: Choose whether to create a new alert setting or clone an existing one.**

To create a new alert:

a. Click Add Alert.

To clone an existing alert setting:

a. Click the Alert Settings tab.
#. Locate the alert setting you want to clone.
#. Click ellipsis-h then Clone in that alert
   setting's row.

**Step 4: Choose the Target.**

Click one of the options under Select a Target.

**Step 5: Choose the Condition.**

**Step 6: Configure the Microsoft Teams integration.**

a. Under the Add Notification Method heading, click the
   button for Microsoft Teams.

#. Enter the incoming webhook URL in the provided text box.

#. To test the integration, click Post Test Alert.

#. Under Recurrence, set the recurrence conditions
   in the provided text boxes.

#. Click Add.

**project:**

**Important:** Required Privileges

To manage project alerts, you must have the 
`Project Owner` role for the project.

**Step 1: Create the Microsoft Teams incoming webhook.**

a. Navigate to the Microsoft Teams channel where you want to add the webhook.

#. Select ellipsis-h from the top navigation bar. A dropdown menu of available options displays.

#. Select Connectors from the dropdown menu. A modal with available connectors displays.

#. Search for Incoming Webhook and select Add. A modal with information about the Incoming Webhook connector displays.

#. Click Add. The modal closes.

#. Select ellipsis-h from the top navigation bar. A dropdown menu of available options displays.

#. Select Connectors from the dropdown menu. The modal with available connectors displays.

#. Search for Incoming Webhook and select Configure. A configuration modal displays.

#. In the modal, enter a name for your webhook. Optionally, you can upload a unique image to help you identify your webhook.

#. Click Create. 

#. Copy the incoming webhook URL. 

   **Important:**

   Ops Manager requires this URL to configure the integration.

#. Click Done.

**Step 2: Navigate to the Integrations page for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Next to the Projects menu, expand the
   Options menu, then click Integrations.

**Step 3: Configure the Microsoft Teams integration.**

a. Search for Microsoft Teams and click Configure. A configuration modal displays.

#. Enter the incoming webhook URL in the provided text box.

#. To test the integration, click Test Integration.

#. Click Activate. 

**Step 4: Navigate to the Alerts page for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Click the `bell` Project Alerts icon in the
   navigation bar, or click Alerts in the sidebar.

**Step 5: Choose whether to create a new alert setting or clone an existing one.**

To create a new alert without cloning an existing setting:

a. Click Add.
#. Select New Alert.

To clone an existing alert setting:

a. Click the Alert Settings tab.
#. Locate the alert setting you want to clone.
#. Click ellipsis-h then Clone in that alert
   setting's row.

**Step 6: Select the condition that triggers the alert.**

In the Alert if section, select the target component and
the condition. 

**Step 7: Apply the alert only to specific targets. (Optional)**

If the options in the For section are available, you can
optionally filter the alert to apply only to a subset of the targets.

The matches field can use regular expressions.

**Step 8: Select the alert recipients and delivery methods.**

In the Send to section:

a. (Optional) To help reduce the false positives that Ops Manager 
   sends, in the send if condition lasts 
   at least field, specify the minutes to elapse before the 
   condition sends the alert. The next alert check that runs after
   the specified time elapses sends the alert.

#. (Optional) In the resend after field, specify the 
   minutes to elapse before the condition resends the alert.

#. Click Add and select Microsoft Teams.

**Step 9: Click Save.**
