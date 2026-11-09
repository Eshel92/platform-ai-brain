<!-- Converted from tutorial/create-cluster-with-api.txt (reStructuredText). Includes are inlined. -->

# Deploy a Cluster through the API

This tutorial manipulates the Ops Manager Administration API's
automation configuration to deploy a sharded cluster that is
owned by another user. The tutorial first creates a new project, then a
new user as owner of the project, and then a sharded cluster owned by
the new user. You can create a script to automate these procedures for
use in routine operations.

To perform these steps, you must have sufficient access to Ops Manager. A
user with the `Global Owner` or
`Project Owner` role has sufficient access.

The procedures install a cluster with two shards. Each
shard comprises a three-member replica set. The tutorial
installs one `mongos` and three config servers.
Each component of the cluster resides on its own server, requiring a
total of 10 hosts.

The tutorial installs the
MongoDB Agent on each
host.

## Prerequisites

Ops Manager must have an existing user. If you are deploying the sharded
cluster on a fresh install of Ops Manager, you must register the first
user.

You must have the URL (Uniform Resource Locator) of the Ops Manager host, as set in the
mmsbaseurl setting of the MongoDB Agent configuration
file.

Provision ten hosts to serve the components of the
sharded cluster. For host requirements, see the
Production Notes in the
MongoDB manual.

Each host must provide its
MongoDB Agent with full
networking access to the hostnames and ports of the MongoDB Agents on
all the other hosts. Each agent runs the command `hostname -f`
to self-identify its hostname and port and report them to Ops Manager.

**Tip:**

To ensure agents can reach each other,
provision the hosts using Automation.
This installs the MongoDB Agents with correct network access. Use
this tutorial to reinstall the Automations on those machines.

## Examples

As you work with the API (Application Programming Interface), you can view examples on the
[GitHub example page](https://github.com/10gen-labs/mms-api-examples/tree/master/automation/).

## Variables for Cluster Creation API Resources

The API resources use one or more of these variables. Replace these variables with your desired values before calling these API resources.

| Name | Type | Description |
|---|---|---|
| `PUBLIC-KEY` | string | Your public API Key for your API (Application Programming Interface) credentials. |
| `PRIVATE-KEY` | string | Your private API Key for your API (Application Programming Interface) credentials. |
| `<OpsManagerHost>:<Port>` | string | URL (Uniform Resource Locator) of your Ops Manager instance. |
| `GROUP-ID` | string | Unique identifier of your project from your project settings. |

## Prerequisites

- /tutorial/configure-public-api-access to enable you to use the
  API.

- Complete the MongoDB Agent Prerequisites.

## Procedures

### Create the Group and the User through the API

**Step 1: Use the API to create a project.**

Use the Ops Manager Administration API to send a projects document to create the new project.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
--header "Content-Type: application/json" \
--request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups?pretty=true" \
--data '
  {
    "name": "{GROUP-NAME}",
    "orgId": "{ORG-ID}"
  }'
```

The API (Application Programming Interface) returns a document that includes the project's
`agentApiKey` and `id`.

**Step 2: Record the values of `agentApiKey` and `id` in the returned document.**

Record these values for use in this procedure and in other procedures
in this tutorial.

**Step 3: Use the API to create a user in the new project.**

Use the `/users` endpoint to add a user to the new project.

The body of the request should contain a
users JSON (Javascript Object Notation) document with the user's
information.

Set the user's `roles.roleName` to `GROUP_OWNER` and the user's
`roles.groupId` set to the new group's' `id`.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Content-Type: application/json" \
     --request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/users?pretty=true" \
     --data '
       {
          "username": "<new_user@example.com>",
          "emailAddress": "<new_user@example.com>",
          "firstName": "<First>",
          "lastName": "<Last>",
          "password": "<password>",
          "roles": [{
            "groupId": "{PROJECT-ID}",
            "roleName": "GROUP_OWNER"
          }]
       }'
```

**Step 4: (Optional) If you used a global owner user to create the project, you can remove that user from the project.**

The user you use to create the project is automatically added to the
project. If you used a user with the `Global Owner` role,
you can remove the user from the project without losing the ability
to make changes to the project in the future. As long as you have the
project's `agentApiKey` and `id`, you have full access to the
project when logged in as the global owner.

`GET` the global owner's ID. Issue the following command to
request the project's users:

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/users?pretty=true"
```

The API (Application Programming Interface) returns a JSON (Javascript Object Notation) document that lists all the project's
users. Locate the user with `roles.roleName` set to
`GLOBAL_OWNER`. Copy the user's `id` value, and issue the
following to remove the user from the project, replacing
`{USER-ID}` with the user's `id` value:

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/users/{USER-ID}?pretty=true"
```

If Ops Manager removes the user successfully, the API (Application Programming Interface) returns the
HTTP (Hypertext Transfer Protocol) `200 OK` status code.

### Install the MongoDB Agent on each Provisioned Host

**Step 1: Complete the MongoDB Agent installation procedure on each host.**

To learn how to install the MongoDB Agent, follow the
procedure for the appropriate platform.

**Step 2: Confirm the initial state of the automation configuration.**

When the MongoDB Agent first runs, it downloads the
`mms-cluster-config-backup.json` file, which describes the desired
state of the automation configuration.

On one of the hosts, navigate to `/var/lib/mongodb-mms-automation/`
and open `mms-cluster-config-backup.json`. Confirm that the file's
`version` field is set to `1`. Ops Manager automatically increments
this field as changes occur.

### Deploy the New Cluster

To add or update a deployment, retrieve the
configuration, make
changes as needed, and send the updated configuration though the API (Application Programming Interface)
to Ops Manager.

The following procedure deploys an updated automation configuration
through the API (Application Programming Interface):

**Step 1: Retrieve the automation configuration from Ops Manager.**

a. Use the automationConfig
   resource to retrieve the configuration. Issue the following
   command, replacing the placeholders with the Variables for Cluster Creation API Resources.

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

**Step 2: Create the top level of the new automation configuration.**

Create a document with the following fields. As you build the
configuration document, refer the
description of an automation configuration for detailed explanations
of the settings. For examples, see the [MongoDB Labs page](https://github.com/10gen-labs/mms-api-examples/tree/master/automation/).

```javascript
{
    "options": {
        "downloadBase": "/var/lib/mongodb-mms-automation",
    },
    "mongoDbVersions": [],
    "monitoringVersions": [],
    "backupVersions": [],
    "processes": [],
    "replicaSets": [],
    "sharding": []
}
```

**Step 4: Add the Monitoring to the automation configuration.**

In the `monitoringVersions.hostname` field, enter the hostname of
the server where Ops Manager should install the Monitoring. Use the fully
qualified domain name that running `hostname -f` on the server
returns, as in the following:

```javascript
"monitoringVersions": [
  {
    "hostname": "<server_x.example.com>",
    "logPath": "/var/log/mongodb-mms-automation/monitoring-agent.log",
    "logRotate": {
      "sizeThresholdMB": 1000,
      "timeThresholdHrs": 24
    }
  }
]
```

This configuration example also includes the `logPath` field, which
specifies the log location, and `logRotate`, which specifies the
log thresholds.

**Step 5: Add the servers to the automation configuration.**

This sharded cluster has 10 MongoDB instances, as described in the
create-cluster-with-api-overview, each running on its own
server. Thus, the automation configuration's `processes` array will
have 10 documents, one for each MongoDB instance.

The following example adds the first document to the `processes`
array. Replace `<process_name_1>` with any name you choose, and
replace `<server1.example.com>` with the FQDN (fully qualified domain name) of the host.

Add 9 documents: one for each MongoDB instance in your sharded
cluster.

Specify the `args2_6` syntax for the `processes.<args>` field.
The `processes.args2_6` object accepts most MongoDB settings and 
parameters for MongoDB versions 2.6 and later. To learn more, see 
om-unsupported-mdb-settings.

```javascript
"processes": [
  {
    "version": "4.0.6",
    "name": "<process_name_1>",
    "hostname": "<server1.example.com>",
    "logRotate": {
      "sizeThresholdMB": 1000,
      "timeThresholdHrs": 24
    },
    "authSchemaVersion": 5,
    "featureCompatibilityVersion": "4.0",
    "processType": "mongod",
    "args2_6": {
      "net": {
        "port": 27017
      },
      "storage": {
        "dbPath": "/data/"
      },
      "systemLog": {
        "path": "/data/mongodb.log",
        "destination": "file"
      },
      "replication": {
        "replSetName": "rs1"
      }
    }
  },
]
```

**Step 6: Add the sharded cluster topology to the automation configuration.**

Add two replica set documents to the `replicaSets` array. Add
three members to each document.

**Example:**

This section adds one replica set member to the first replica set
document:

**Important:**

You must include `"protocolVersion": 1` in the root document
for each replica set.

```javascript
"replicaSets": [
  {
    "_id": "rs1",
    "members": [
      {
        "_id": 0,
        "host": "<process_name_1>",
        "priority": 1,
        "votes": 1,
        "secondaryDelaySecs": 0,
        "hidden": false,
        "arbiterOnly": false
      }
    ],
    "protocolVersion": 1
  }
]
```

In the `sharding` array, add the replica sets to the shards, and
add the config server replica set name, as in the following:

```javascript
"sharding": [
  {
    "shards": [
      {
        "tags": [],
        "_id": "shard1",
        "rs": "rs1"
      },
      {
        "tags": [],
        "_id": "shard2",
        "rs": "rs2"
      }
    ],
    "name": "sharded_cluster_via_api",
    "configServerReplica": "rs-config"
  }
]
```

**Step 7: Send the updated automation configuration.**

Use the automationConfig
resource to send the updated automation configuration.

Issue the following command with path to the updated configuration 
document and replace the placeholders with the Variables for Cluster Creation API Resources.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Content-Type: application/json"
     --request PUT "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/automationConfig?pretty=true" \
     --data @currentAutomationConfig.json
```

Upon successful update of the configuration, the API returns the HTTP
`200 OK` status code to indicate the request has succeeded.

**Step 8: Confirm successful update of the automation configuration.**

Retrieve the automation configuration from Ops Manager and confirm it
contains the changes. To retrieve the configuration, issue the
following command, replacing the placeholders with the
Variables for Cluster Creation API Resources.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/automationConfig?pretty=true"
```

**Step 9: Verify that the configuration update is deployed.**

Use the automationStatus
resource to verify the configuration update is fully deployed. Issue
the following command:

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/automationStatus?pretty=true"
```

The `curl` command returns a JSON (Javascript Object Notation) object containing the
`processes` array and the `goalVersion` key and value. The
`processes` array contains a document for each server that hosts a
MongoDB instance. The new configuration is successfully deployed when
all `lastGoalVersionAchieved` fields in the `processes` array
equal the value specified for `goalVersion`.

**Example:**

In this response, `processes[2].lastGoalVersionAchieved` is
behind `goalVersion`. This indicates that the MongoDB instance
at `server3.example.com` is running one version behind the
`goalVersion`. Wait several seconds and issue the `curl`
command again.

```javascript
{
  "goalVersion": 2,
  "processes": [{
    "hostname": "server1.example.com",
    "lastGoalVersionAchieved": 2,
    "name": "ReplSet_0",
    "plan": []
  }, {
    "hostname": "server2.example.com",
    "lastGoalVersionAchieved": 2,
    "name": "ReplSet_1",
    "plan": []
  }, {
     "hostname": "server3.example.com",
     "lastGoalVersionAchieved": 1,
     "name": "ReplSet_2",
     "plan":[]
  }]
}
```

To view the new configuration in the Ops Manager console, click
Deployment.

## Next Steps

To make an additional version of MongoDB available in the cluster,
see update-mongodb-version-of-deployment-via-api.
