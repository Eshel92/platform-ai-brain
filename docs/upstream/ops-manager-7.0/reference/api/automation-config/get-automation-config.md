<!-- Converted from reference/api/automation-config/get-automation-config.txt (reStructuredText). Includes are inlined. -->

# Get the Automation Configuration

A project's automation configuration determines the goal state of its MongoDB
processes and agents. The MongoDB Agent builds the deployment according
to the goals specified. 

**Important:**

A project's automation configuration might contain sensitive
information, including passwords or key values. To get the automation
configuration with sensitive information redacted, use the
/groups/{PROJECT-ID}/automationConfig/noSecrets endpoint. 

## Required Roles

This resource requires the `Project Automation Admin` role.

## Resource

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /groups/{PROJECT-ID}/automationConfig
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

To review an example of this configuration, see
/reference/api/automation-config/automation-config-example.
