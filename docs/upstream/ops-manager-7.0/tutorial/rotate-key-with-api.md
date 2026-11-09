<!-- Converted from tutorial/rotate-key-with-api.txt (reStructuredText). Includes are inlined. -->

# Rotate a Key File with the API

You can programmatically rotate a key file by updating a project's
automation configuration.

To rotate a key file using the Ops Manager API:

1. Retrieve the current configuration.
2. Add the new key file that you want to use with the **auth.newKey**
   setting.
3. Replace the entire configuration using `PUT`.
   You must use `PUT`. **Do not** use `PATCH`.

When all MongoDB Agents use the new key, Ops Manager 
replaces the value of **auth.key** with the new key that you 
provided in **auth.newKey** and removes **auth.newKey** from the
automation configuration.

## Prerequisites

- You must have access to the API (Application Programming Interface). To learn more, see
  /tutorial/configure-public-api-access.
- Your API key must have the `Project Automation Admin` or
  `Project Owner` role.
- Authentication must be enabled.
- At least one cluster in the project must be configured with the
  clusterAuthMode
  option set to `keyFile` or `sendKeyFile`.
- All clusters in the project must be running MongoDB version 4.2 or
  higher.

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

**Step 2: Add your new key file to the automation configuration file you downloaded.**

a. Open `currentAutomationConfig.json` in your preferred text editor.

#. Add the **auth.newKey** field. Set this field's value to the 
   new key file that you want Ops Manager to use.

   **Note:**

   The sample configuration below is truncated for readability.

   ```json
   {
     "auth": {
       "disabled": "false",
       "key": "<your-old-key>",
       "newKey": "<your-new-key>"
     }
   }
   ```

If you're updating the MongoDB Agent, see
update-monitoring-backup-versions before continuing
with this procedure.

**Step 3: Send the updated automation configuration.**

Use the automationConfig
resource to send the updated automation configuration.

Issue the following command with path to the updated configuration 
document and replace the placeholders with the Variables for Automation Config API Resources.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Content-Type: application/json"
     --request PUT "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/automationConfig?pretty=true" \
     --data @currentAutomationConfig.json
```

Upon successful update of the configuration, the API returns the HTTP
`200 OK` status code to indicate the request has succeeded.

**Step 4: Confirm successful update of the automation configuration.**

Retrieve the automation configuration from Ops Manager and confirm it
contains the changes. To retrieve the configuration, issue the
following command, replacing the placeholders with the
Variables for Automation Config API Resources.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/automationConfig?pretty=true"
```

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
