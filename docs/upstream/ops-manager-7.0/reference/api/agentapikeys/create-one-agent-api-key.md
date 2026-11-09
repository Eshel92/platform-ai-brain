<!-- Converted from reference/api/agentapikeys/create-one-agent-api-key.txt (reStructuredText). Includes are inlined. -->

# Create One Agent API Key

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
POST /groups/{PROJECT-ID}/agentapikeys
```

This endpoint is restricted to users with the
`Project Owner` role.

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| PROJECT-ID | string | Unique identifier of the `project` that owns the Agent API Key. |

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

| Name | Type | Description |
|---|---|---|
| desc | string | Label for this Agent API Key. |

## Response

* - Name
  - Type
  - Description

* - id
  - string
  - Unique identifier of this Agent API Key.

* - key
  - string
  - Agent API Key.

    After creating this Agent API Key, subsequent requests 
    return the last four characters of Agent API Keys.

* - desc
  - string
  - Label for this Agent API Key. Limited to 1,000 characters.

* - createdTime
  - string
  - Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the Agent API Key was created.

* - createdUserId
  - string
  - Unique identifier of user who created this Agent API Key.

* - createdIpAddr
  - string
  - IP (Internet Protocol) address that created this Agent API Key.

* - createdBy
  - string
  - Source of this Agent API Key. Accepted values are:

    - `USER`
    - `OLD_KEY`
    - `PROVISIONING`
    - `ATLAS`
    - `PUBLIC_API`

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --header "Content-Type: application/json" \
 --include \
 --request POST "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/groups/{PROJECT-ID}/agentapikeys?pretty=true" \
 --data '
   {
     "desc": "Agent API Key for this project"
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
  "_id" : "{AGENT-API-KEY-ID}",
  "createdBy" : "PUBLIC_API",
  "createdIpAddr" : "{IP-ADDRESS}",
  "createdTime" : 1520458807291,
  "createdUserId" : "{USER-ID}",
  "desc" : "Agent API Key for this project",
  "key" : "{AGENT-API-KEY}"
}
```
