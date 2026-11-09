<!-- Converted from tutorial/update-mongodb-version-of-deployment-via-api.txt (reStructuredText). Includes are inlined. -->

# Update the MongoDB Version of a Deployment

This tutorial describes how to use the API to migrate a
MongoDB deployment to a new version of MongoDB. These steps assume you
have an existing deployment that uses a `4.0.6` version of MongoDB,
as would be the case if you used the tutorial to
/tutorial/create-cluster-with-api.

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

## Considerations

The API (Application Programming Interface) supports most MongoDB settings and parameters for MongoDB 
versions 2.6 and later. To learn more, see 
om-unsupported-mdb-settings.

**Warning:** Upgrades from MongoDB 5.0 to 6.0

When you upgrade a sharded cluster from MongoDB 5.0 to 6.0, you
must use the procedure on the
Upgrade a Sharded Cluster to 6.0 page of the MongoDB
Manual to refresh the cached routing table for each `mongos`.

## Variables for API Resources to Update MongoDB Version

The API resources use one or more of these variables. Replace these
variables with your desired values before calling these API resources.

| Name | Type | Description |
|---|---|---|
| `PUBLIC-KEY` | string | Your public API Key for your API (Application Programming Interface) credentials. |
| `PRIVATE-KEY` | string | Your private API Key for your API (Application Programming Interface) credentials. |
| `<OpsManagerHost>:<Port>` | string | URL (Uniform Resource Locator) of your Ops Manager instance. |
| `GROUP-ID` | string | Unique identifier of your project from your project settings. |
| `CLUSTER-ID` | string | Unique identifier of your cluster. |

## Prerequisite

You must have credentials to access Ops Manager as a user with the
`Global Owner` role.

## Procedure

**Step 1: Retrieve the automation configuration from Ops Manager.**

a. Use the automationConfig
   resource to retrieve the configuration. Issue the following
   command, replacing the placeholders with the Variables for API Resources to Update MongoDB Version.

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

**Step 2: Open the configuration document for editing.**

As you edit the configuration document in the next steps, refer to
the description of an automation configuration for detailed descriptions
of settings.

**Step 3: Update the MongoDB version in the `processes` array.**

Update **every** `processes.version` field to specify `4.2.1`:

```javascript
"version": "4.2.1"
```

**Step 4: Send the updated automation configuration.**

Use the automationConfig
resource to send the updated automation configuration.

Issue the following command with path to the updated configuration 
document and replace the placeholders with the Variables for API Resources to Update MongoDB Version.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Content-Type: application/json"
     --request PUT "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/automationConfig?pretty=true" \
     --data @currentAutomationConfig.json
```

Upon successful update of the configuration, the API returns the HTTP
`200 OK` status code to indicate the request has succeeded.

**Step 5: Confirm successful update of the automation configuration.**

Retrieve the automation configuration from Ops Manager and confirm it
contains the changes. To retrieve the configuration, issue the
following command, replacing the placeholders with the
Variables for API Resources to Update MongoDB Version.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/automationConfig?pretty=true"
```

**Step 6: Check the deployment status to ensure goal state is reached.**

Use the automationStatus
resource to retrieve the deployment status. Issue the following
command, replacing the placeholders with the Variables for API Resources to Update MongoDB Version.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/automationStatus?pretty=true"
```

Confirm that the values of all the `lastGoalVersionAchieved` fields
in the `processes` array match the `goalVersion` field. To learn
about deployment status, see /reference/api/automation-status.
