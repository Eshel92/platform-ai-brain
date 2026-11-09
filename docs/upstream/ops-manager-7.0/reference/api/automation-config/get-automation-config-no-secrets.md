<!-- Converted from reference/api/automation-config/get-automation-config-no-secrets.txt (reStructuredText). Includes are inlined. -->

# Get the Automation Configuration (Redacted Secrets)

A project's automation configuration determines the goal state of its MongoDB
processes and agents. The MongoDB Agent builds the deployment according
to the goals specified. 

**Important:**

A project's automation configuration might contain sensitive
information, such as passwords or key values. This resource gets the
automation configuration with sensitive information redacted. To get
the nonredacted automation configuration, use the
/groups/{PROJECT-ID}/automationConfig
endpoint.

## Compatibility

This endpoint is available in Ops Manager 7.0.18 and later.

## Required Roles

This resource requires the `Project Automation Admin` role.

## Resource

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /groups/{PROJECT-ID}/automationConfig/noSecrets 
```

## Request

### Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| PROJECT-ID | string | Required | Unique identifier of the `group` that owns the automation configuration. |

### Query Parameters

The following query parameters are optional:

* - Name
  - Type
  - Necessity
  - Description
  - Default

* - pretty
  - boolean
  - Optional
  - Flag indicating whether the response body should be in a
    prettyprint format.
  - `false`

* - envelope
  - boolean
  - Optional
  - Flag that indicates whether or not to wrap the response in an
    envelope.

    Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or
    status code. To remediate this, set **envelope=true** in the
    query.

    For endpoints that return one result, the response body
    includes:

    | Name | Description |
    |---|---|
    | status | HTTP (Hypertext Transfer Protocol) response code |
    | envelope | Expected response body |

  - `false`

### Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

To review these parameters, see
/reference/api/automation-config/automation-config-parameters.

## Example Request

```sh
curl --user "{publicApiKey}:{privateApiKey}" --digest \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/automationConfig?pretty=true" \
     --output currentAutomationConfig.json
```

## Example Response

### Response Header

```http
HTTP/1.1 401 Unauthorized
Content-Type: application/json;charset=ISO-8859-1
Date: {dateInUnixFormat}
WWW-Authenticate: Digest realm="MMS Public API", domain="", nonce="{nonce}", algorithm=MD5, op="auth", stale=false
Content-Length: {requestLengthInBytes}
Connection: keep-alive
```

```http
HTTP/1.1 200 OK
Vary: Accept-Encoding
Content-Type: application/json
Strict-Transport-Security: max-age=300
Date: {dateInUnixFormat}
Connection: keep-alive
Content-Length: {requestLengthInBytes}
X-MongoDB-Service-Version: gitHash={gitHash}; versionString={ApplicationVersion}
```

### Response Body

The following example response body shows an example automation
configuration with the sensitive information redacted. The
`/groups/{PROJECT-ID}/automationConfig/noSecrets` endpoint returns
redacted text with the sensitive field value replaced by the string
`<redacted>`: 

```json
{
  "backupVersions": [
    {
      "hostname": "test-2.aabc.3172.mongodbdns.com"
    }
  ],
  "mongoDbVersions": [
    {
      "name": "4.4.0"
    }
  ],
  "monitoringVersions": [
    {
      "hostname": "test-2.aabc.3172.mongodbdns.com"
    }
  ],
  "options": {
    "downloadBase": "/var/lib/mongodb-mms-automation",
    "downloadBaseWindows": "%SystemDrive%\\MMSAutomation\\versions"
  },
  "processes": [
    {
      "args2_6": {
        "net": {
          "port": 27017
        },
        "operationProfiling": {},
        "replication": {
          "replSetName": "replSet1"
        },
        "storage": {
          "dbPath": "/data/replSet1_10"
        },
        "systemLog": {
          "destination": "file",
          "path": "/data/replSet1_10/mongodb.log"
        }
      },
      "hostname": "test-2.aabc.3172.mongodbdns.com",
      "logRotate": {
        "sizeThresholdMB": 1000,
        "timeThresholdHrs": 24
      },
      "auditLogRotate": {
        "sizeThresholdMB": 1000,
        "timeThresholdHrs": 24
      },
      "name": "replSet1_10",
      "directAttachVerificationKey": "<redacted>",
      "processType": "mongod",
      "version": "4.4.0",
      "authSchemaVersion": 5,
      "featureCompatibilityVersion": "4.2"
    },
    {
      "args2_6": {
        "net": {
          "port": 27017
        },
        "operationProfiling": {},
        "replication": {
          "replSetName": "replSet1"
        },
        "storage": {
          "dbPath": "/data/replSet1_11"
        },
        "systemLog": {
          "destination": "file",
          "path": "/data/replSet1_11/mongodb.log"
        }
      },
      "hostname": "test-1.aabc.3172.mongodbdns.com",
      "logRotate": {
        "sizeThresholdMB": 1000,
        "timeThresholdHrs": 24
      },
      "auditLogRotate": {
        "sizeThresholdMB": 1000,
        "timeThresholdHrs": 24
      },
      "name": "replSet1_11",
      "directAttachVerificationKey": "<redacted>",
      "processType": "mongod",
      "version": "4.4.0",
      "authSchemaVersion": 5,
      "featureCompatibilityVersion": "4.2"
    },
    {
      "args2_6": {
        "net": {
          "port": 27017
        },
        "operationProfiling": {},
        "replication": {
          "replSetName": "replSet1"
        },
        "storage": {
          "dbPath": "/data/replSet1_12"
        },
        "systemLog": {
          "destination": "file",
          "path": "/data/replSet1_12/mongodb.log"
        }
      },
      "hostname": "test-0.aabc.3172.mongodbdns.com",
      "logRotate": {
        "sizeThresholdMB": 1000,
        "timeThresholdHrs": 24
      },
      "auditLogRotate": {
        "sizeThresholdMB": 1000,
        "timeThresholdHrs": 24
      },
      "name": "replSet1_12",
      "directAttachVerificationKey": "<redacted>",
      "processType": "mongod",
      "version": "4.4.0",
      "authSchemaVersion": 5,
      "featureCompatibilityVersion": "4.2"
    },
    {
      "args2_6": {
        "net": {
          "port": 27018
        },
        "operationProfiling": {},
        "replication": {
          "replSetName": "replSet1"
        },
        "storage": {
          "dbPath": "/data/replSet1_13"
        },
        "systemLog": {
          "destination": "file",
          "path": "/data/replSet1_13/mongodb.log"
        }
      },
      "hostname": "test-2.aabc.3172.mongodbdns.com",
      "logRotate": {
        "sizeThresholdMB": 1000,
        "timeThresholdHrs": 24
      },
      "auditLogRotate": {
        "sizeThresholdMB": 1000,
        "timeThresholdHrs": 24
      },
      "name": "replSet1_13",
      "directAttachVerificationKey": "<redacted>",
      "processType": "mongod",
      "version": "4.4.0",
      "authSchemaVersion": 5,
      "featureCompatibilityVersion": "4.2"
    }
  ],
  "replicaSets": [
    {
      "_id": "replSet1",
      "protocolVersion": "1",
      "members": [
        {
          "_id": 0,
          "arbiterOnly": false,
          "hidden": true,
          "host": "replSet1_10",
          "priority": 0.0,
          "secondaryDelaySecs": 200,
          "votes": 0
        },
        {
          "_id": 1,
          "arbiterOnly": false,
          "hidden": false,
          "host": "replSet1_11",
          "priority": 1.0,
          "secondaryDelaySecs": 0,
          "votes": 1
        },
        {
          "_id": 2,
          "arbiterOnly": false,
          "hidden": false,
          "host": "replSet1_12",
          "priority": 1.0,
          "secondaryDelaySecs": 0,
          "votes": 1
        },
        {
          "_id": 3,
          "arbiterOnly": true,
          "hidden": false,
          "host": "replSet1_13",
          "priority": 0.0,
          "secondaryDelaySecs": 0,
          "votes": 1
        }
      ]
    }
  ],
  "roles": [],
  "sharding": [],
  "indexConfigs": [
    {
      "key": [
        [
          "field",
          "1"
        ]
      ],
      "rsName": "replSet1",
      "dbName": "db",
      "collectionName": "collection"
    }
  ]
}
```
