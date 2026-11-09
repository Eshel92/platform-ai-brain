<!-- Converted from reference/api/automation-status-full.txt (reStructuredText). Includes are inlined. -->

# Get Automation Status of Last 50 Plans

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

## Overview

Retrieves the 50 most recent plans for MongoDB processes. Plans are a 
set of actions required to get a MongoDB deployment to the 
`goalVersion`.

The endpoint returns the `goalVersion` field to 
report the version of the automation configuration the response object 
describes and the `lastGoalVersionAchieved` field to report the 
versions of the configuration running on each server.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/GROUP-ID/automationStatus/full
```

## Request Parameters

### Request Path Parameters

| Parameter | Type | Description |
|---|---|---|
| GROUP-ID | string | *(Required.)* The unique identifier for the group. |

### Request Query Parameters

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

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

| Name | Type | Description |
|---|---|---|
| goalVersion | number | The version of the automation configuration. If there is a conflict in submissions of automation configurations, this field lists the winning configuration. |
| processes | array | The project's deployed MongoDB instances. |
| process.errorCode | integer | The error code. Returns `0` if the process has no errors. |
| process.errorCodeDescription | string | Detailed error description. Returns an empty string if the process has no errors. |
| process.errorCodeHumanReadable | string | Short error description. Returns an empty string if the process has no errors. |
| process.errorString | string | Output of the log line that contains the error. Examine this field for additional error context. Returns an empty string if the process has no errors. |
| processes.hostname | string | The fully qualified domain name (retrieved by issuing `hostname -f`) of the server on which the MongoDB process and Automation are hosted. |
| processes.name | string | The process name as specified in the automation configuration. |
| processes.lastGoalVersionAchieved | number | The last version of the automation configuration with which this process had deployed as configured. If the `processes.lastGoalVersionAchieved` number is not equal to the `goalVersion` number, the process has not yet deployed according to the current configuration. |
| processes.plan | array | Describes how a process that is not yet up-to-date with the configuration will achieve the goal state. |

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
  --header 'Accept: application/json' \
  --include \
  --request GET "https://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/automationStatus/full"
```

### Example Response

#### Response Header

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

#### Response Body

```json
{
	"goalVersion": 11,
	"processes": [{
		"errorCode": 0,
		"errorCodeDescription": "",
		"errorCodeHumanReadable": "",
		"errorString": "",
		"hostname": "example.net",
		"lastGoalVersionAchieved": 11,
		"name": "myReplicaSet_3",
		"plan": ["Download",
			"WaitRsInit",
			"WaitFeatureCompatibilityVersionCorrect"
		]
	}, {
		"errorCode": 100,
		"errorCodeDescription": "There is an issue with file permissions for this process",
		"errorCodeHumanReadable": "File Permissions Error",
		"errorString": "<myReplicaSet_1> [13:11:33.348] Failed to compute states : <myReplicaSet_1> [13:11:33.348] Error calling ComputeState : <myReplicaSet_1> [13:11:33.348] Error getting fickle state for current state : <myReplicaSet_1> [13:11:33.348] Error checking if process is running from dbpath = /data/0 : <myReplicaSet_1> [13:11:33.348] Error getting file contents of /data/0/mongod.lock as string : <myReplicaSet_1> [13:11:33.348] Error reading file from /data/0/mongod.lock : open /data/0/mongod.lock: permission denied",
		"hostname": "example.net",
		"lastGoalVersionAchieved": 1,
		"name": "myReplicaSet_1",
		"plan": ["Download"]
	}, {
		"errorCode": 0,
		"errorCodeDescription": "",
		"errorCodeHumanReadable": "",
		"errorString": "",
		"hostname": "example.net",
		"lastGoalVersionAchieved": 11,
		"name": "myReplicaSet_2",
		"plan": ["Download",
			"Start",
			"WaitRsInit",
			"WaitFeatureCompatibilityVersionCorrect",
			"AdjustRoles"
		]
	}]
}
```
