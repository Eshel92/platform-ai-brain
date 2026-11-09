<!-- Converted from tutorial/rotate-automation-password-with-api.txt (reStructuredText). Includes are inlined. -->

# Rotate Automation Password with the API

You can programmatically rotate the automation user's password by 
updating a project's automation configuration.

This page describes the following process to rotate the automation 
user's password using the Ops Manager API:

1. Set **auth.newAutoPwd** and leave **auth.autoPwd** with its 
   current password.

#. Wait for the goal state.

#. **auth.newAutoPwd** copies over the **auth.autoPwd**
   password automatically.

You can set this option only when you include SCRAM-SHA-1 
or SCRAM-SHA-256 as one of the authentication 
mechanisms for the Automation in **auth.autoAuthMechanisms**.

## Prerequisites

- You must have access to the API (Application Programming Interface). To learn more, see
  /tutorial/configure-public-api-access.
- Your API key must have the `Project Automation Admin` or
  `Project Owner` role.
- Authentication must be enabled.

## Variables for Automation Config API Resources

The API resources use one or more of these variables. Replace these
variables with your desired values before calling these API resources.

| Name | Type | Description |
|---|---|---|
| `PUBLIC-KEY` | string | Your public API Key for your API (Application Programming Interface) credentials. |
| `PRIVATE-KEY` | string | Your private API Key for your API (Application Programming Interface) credentials. |
| `<OpsManagerHost>:<Port>` | string | URL (Uniform Resource Locator) of your Ops Manager instance. |
| `GROUP-ID` | string | Unique identifier of your project from your project settings. |
| `CLUSTER-ID` | string | Unique identifier of your cluster. |

## Procedure

**Step 1: Retrieve and validate the automation configuration from Ops Manager.**

a. Use the automationConfig
   resource to retrieve the configuration. Issue the following
   command, replacing the placeholders with the Variables for Automation Config API Resources.

   ```sh
   curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
        --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/automationConfig?pretty=true" \
        --output currentAutomationConfig.json
   ```

b. Validate the downloaded Automation Configuration file.

   Compare the `version` field of the
   `currentAutomationConfig.json` with that of the Automation
   Configuration backup file, `mms-cluster-config-backup.json`. The
   `version` value is the last element in both JSON (Javascript Object Notation) documents.
   You can find this file on any host running the MongoDB Agent at:

   - Linux and macOS: `/var/lib/mongodb-mms-automation/mms-cluster-config-backup.json`
   - Windows: `%SystemDrive%\MMSAutomation\versions\mms-cluster-config-backup.json`

   If the `version` values match, you are working with the current
   version of the Automation Configuration file.

**Step 2: Create a new automation configuration file from the current one.**

Replace the variables in the following command and run it:

```sh
sed -e "/autoPwd/a\\    \"newAutoPwd\" : \"<NEW_OPS_MANAGER_AUTOMATION_PASSWORD>\"," -e 's/  "version" : <CURRENT_AUTOMATION_CONFIGURATION_VERSION>/  "version" : <NEW_AUTOMATION_CONFIGURATION_VERSION>/' currentAutomationConfig.json > modifiedAutomationConfig.json
```

| Name | Description |
|---|---|
| `<NEW_OPS_MANAGER_AUTOMATION_PASSWORD>` | Specify the new Automation password. |
| `<CURRENT_AUTOMATION_CONFIGURATION_VERSION>` | Specify the current Automation version. To check your current Automation version, see get-auto-config. |
| `<NEW_AUTOMATION_CONFIGURATION_VERSION>` | Specify the current Automation version incremented by 1. For example, if you have a current Automation version of `4`, the new Automation version should be `5`. |

**Step 3: Send the updated automation configuration.**

Use the automationConfig
resource to send the updated automation configuration.

Issue the following command, pointing to the 
`modifiedAutomationConfig.json` file created in the previous step, 
which contains the updated configuration document. Replace the 
placeholders with the Variables for Automation Config API Resources.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Content-Type: application/json"
     --request PUT "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/automationConfig?pretty=true" \
     --data '@modifiedAutomationConfig.json'
```

Upon successful update of the configuration, the API returns the HTTP
`200 OK` status code to indicate the request has succeeded.

**Step 4: Confirm successful update of the automation configuration.**

Retrieve the automation configuration from Ops Manager and confirm it
contains the changes. To retrieve the configuration, issue the
following command, replacing the placeholders with the Variables for Automation Config API Resources.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/automationConfig?pretty=true"
```

**Note:**

The Automation version automatically increments two times. For 
example,  if you pushed the new Automation version as 5, the new 
Automation version after all changes is 7. The Automation 
updates the Automation user password on all managed MongoDB 
Server deployments.

**Step 5: Check the deployment status to ensure goal state is reached.**

Use the automationStatus
resource to retrieve the deployment status. Issue the following
command, replacing the placeholders with the Variables for Automation Config API Resources.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/automationStatus?pretty=true"
```

Confirm that the values of all the `lastGoalVersionAchieved` fields
in the `processes` array match the `goalVersion` field. To learn
about deployment status, see /reference/api/automation-status.
