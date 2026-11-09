<!-- Converted from reference/api/automation-config/update-agent-versions.txt (reStructuredText). Includes are inlined. -->

# Update Agent Versions

This endpoint updates the MongoDB Agent and tools to the latest
versions available at the time of the request:

- MongoDB Agent
- `BI Connector`
- [MongoDB Database Tools](https://www.mongodb.com/docs/database-tools/)

After this request completes, Ops Manager modifies the agent configuration
and saves the updated version.

## Required Roles

This resource requires the `Project Automation Admin` role.

## Resource

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
POST /groups/{PROJECT-ID}/automationConfig/updateAgentVersions
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

| Name | Type | Necessity | Description |
|---|---|---|---|
| automationAgentVersion | string | Optional | Version to which you want to update the MongoDB Agent. |
| biConnectorVersion | string | Optional | Version to which you want to update the `BI Connector`. |
| mongoDbToolsVersion | string | Optional | Version to which you want to update the [MongoDB Database Tools](https://www.mongodb.com/docs/database-tools/) |

## Response

| Parameter | Type | Description |
|---|---|---|
| automationAgentVersion | string | Version of the MongoDB Agent in the specified project. |
| backupAgentVersion | string | Version of the Backup Agent in the specified project. Ops Manager has removed the Backup Agent, so this parameter should return **null**. |
| biConnectorVersion | string | Version of the `MongoDB Connector for BI` in the specified project. |
| mongoDbToolsVersion | string | Version of the MongoDB Database Tools in the specified project. |
| monitoringAgentVersion | string | Version of the Monitoring Agent in the specified project. Ops Manager has removed the Monitoring Agent, so this parameter should return **null**. |

## Example Request

```sh
curl --user "{publicApiKey}:{privateApiKey}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/automationConfig/updateAgentVersions?pretty=true" \
     --data '{
       "automationAgentVersion": "10.14.31.6566"
     }'
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

```json
{
  "automationAgentVersion": "10.14.31.6566",
  "backupAgentVersion" : null,
  "biConnectorVersion" : "2.14.0",
  "mongoDbToolsVersion" : null,
  "monitoringAgentVersion" : null
}
```
