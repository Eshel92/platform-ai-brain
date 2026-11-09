<!-- Converted from tutorial/pagerduty-integration.txt (reStructuredText). Includes are inlined. -->

# Integrate with PagerDuty

You can configure Ops Manager to send alerts from your project to
your [PagerDuty](https://www.pagerduty.com/) dashboard. With PagerDuty integration, you can:

- Record incidents and notify on-call responders based on Ops Manager 
  alerts.

- Automatically resolve incidents in PagerDuty when an Ops Manager alert 
  is closed with bidirectional synchronization.

## How it Works

With a PagerDuty integration, you can send Ops Manager cluster event data 
to PagerDuty when Ops Manager alerts that you specify are triggered. 
PagerDuty can create a new incident for the corresponding 
service, filter additional alerts from the same source into that 
incident, and alert on-call PagerDuty users.

Once the Ops Manager alert has been resolved, PagerDuty resolves the 
incident.

## Prerequisites

To integrate Ops Manager with PagerDuty, you must have a PagerDuty 
account.

If you do not have an existing PagerDuty account, you can sign up at
`<https://www.pagerduty.com/sign-up/>`__.

**Note:**

All new PagerDuty keys use their [Events API v2](https://developer.pagerduty.com/docs/ZG9jOjExMDI5NTgw-events-api-v2-overview). 

If you have an Events API v1 key, you can continue to use 
that key with MongoDB Atlas.

## Support

If you need help with your Ops Manager PagerDuty integration, contact 
[MongoDB Support](https://support.mongodb.com).

## Procedure

First, navigate to the PagerDuty integration card:

**Step 1: Navigate to your Project Integrations.**

a. If it is not already displayed, select the organization that
   contains your desired project from the dropdown menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Next to the Projects menu, expand the
   Options menu, then click Integrations.

**Step 2: Start linking PagerDuty to your project.**

Click Configure for the PagerDuty integration card. 
You can configure PagerDuty with either your PagerDuty credentials 
or your PagerDuty API (Application Programming Interface) key.

You can configure an Ops Manager integration with [PagerDuty](https://www.pagerduty.com/) in two ways:

- By signing into PagerDuty from the Ops Manager 
  Project Integrations page, or

- By providing a valid Integration Key.

### Sign into PagerDuty

**Step 1: Click Sign in with PagerDuty.**

You are redirected to PagerDuty.

**Step 2: Log into PagerDuty using your PagerDuty credentials.**

**Step 3: Select PagerDuty services to integrate with MongoDB.**

From the dropdown menu, select the PagerDuty service that you 
want to integrate with MongoDB. 

**Note:**

You can select multiple services, but you will be prompted 
to pick a single default in the next step.

PagerDuty redirects you back to your Ops Manager project and displays a 
PagerDuty Configuration modal. 

**Step 3: Select a default service to integrate with MongoDB.**

From the PagerDuty Configuration modal, select one 
default service to integrate. Ops Manager automatically 
provides an integration key.

**Step 4: (Optional) Click Test Integration to confirm that your configuration is valid.**

When you click Test Integration, the PagerDuty 
configuration modal displays a banner with a success or 
failure message.

**Step 5: Click Activate to integrate PagerDuty with Ops Manager.**

When you click Activate, PagerDuty 
validates your configuration.

### Provide an Integration Key

**Step 1: Enter your Integration Key.**

**Step 2: (Optional) Click Test Integration to confirm that your key is valid.**

When you click Test Integration, the PagerDuty 
configuration modal displays a banner with a success or 
failure message.

**Step 3: Click Activate to integrate PagerDuty with Ops Manager.**

When you click Activate, PagerDuty 
validates your Integration Key.

**Important:**

The PagerDuty Events API does not fail when an invalid 
Integration Key is provided. If your key is invalid, the 
Test Integration button may falsely indicate a 
successful integration.

To confirm that your integration is successful, Ops Manager sends an 
initial alert. Check your PagerDuty dashboard for an initial 
incident created by that Ops Manager alert.

## Remove a PagerDuty Integration

To remove the PagerDuty integration from your Ops Manager project, 
click Remove on the PagerDuty card in your Ops Manager 
project's Project Integrations.
