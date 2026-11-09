<!-- Converted from reference/api/teams/teams-get-one-by-id.txt (reStructuredText). Includes are inlined. -->

# Get One Team by ID

**Note:**

This endpoint is incompatible with projects using
LDAP Authentication.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Syntax

```none
GET /orgs/{ORG-ID}/teams/{TEAM-ID}
```

### Request Path Parameters

| Path Element | Required/Optional | Description |
|---|---|---|
| `ORG-ID` | Required. | The unique identifier for the organization associated with the team. |
| `TEAM-ID` | Required | The unique identifier of the team whose information you want to retrieve. |

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
| `id` | string | The unique identifier for the team. |
| `name` | string | The name of the organization associated with the team. |
| `links` | array | .. include:: /includes/api/links-explanation.rst |

## Example Request

```sh
curl --user "{username:apiKey}"" --digest -i \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/orgs/{ORG-ID}/teams/{TEAM-ID}?pretty=true"
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
 "id": "{TEAM-ID}",
 "links": [
     {
         "href": "https://{OPSMANAGER-HOST}:{PORT}/api/pubic/v1.0/orgs/{ORG-ID}/teams/{TEAM-ID}",
         "rel": "self"
     }
 ],
 "name": "myNewTeam"
}
```
