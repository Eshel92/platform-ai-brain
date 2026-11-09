<!-- Converted from tutorial/update-automation-configuration.txt (reStructuredText). Includes are inlined. -->

# Update a Project's Automation Configuration

A project's automation configuration determines the goal state of its MongoDB
processes and agents. The MongoDB Agent builds the deployment according
to the goals specified. 

To update the configuration:

1. Retrieve the current configuration. 

   You can use the /groups/{PROJECT-ID}/automationConfig endpoint to get the full configuration, or use the
   /groups/{PROJECT-ID}/automationConfig/noSecrets endpoint to get the configuration with
   sensitive information redacted, such as passwords or key values.
#. Make changes to a copy of the current configuration, changing only
   those items you want modified.
#. Replace the entire configuration using `PUT`, with the updated
   configuration in the request body. You must use `PUT`. **Do not**
   use `PATCH`.

   When you submit updates, Ops Manager makes internal modifications to the
   data and then saves your new configuration version.

**Note:**

Some parameters cannot be updated through the `automationConfig`
endpoint. To learn more, see:

- update-monitoring-backup-versions
- update-backup-logs
- update-monitoring-logs

To make updates to the MongoDB Agent *other than* `hostname`, you
must do so through a different endpoint.

**Important:**

An automation configuration might contain sensitive information,
including passwords or key values. To update a project's automation
configuration without updating any fields that contain sensitive
information, use the
/groups/{PROJECT-ID}/automationConfig/noSecrets endpoint.

   

## Prerequisites

You must have access to the API (Application Programming Interface). To learn more, see
/tutorial/configure-public-api-access.

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

**Step 2: Edit the downloaded automation configuration file.**

Open `currentAutomationConfig.json` in your preferred text editor.

To learn more about the automation configuration options, see
/reference/cluster-configuration.

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
