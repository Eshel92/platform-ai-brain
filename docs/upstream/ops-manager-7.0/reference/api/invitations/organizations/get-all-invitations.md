<!-- Converted from reference/api/invitations/organizations/get-all-invitations.txt (reStructuredText). Includes are inlined. -->

# Get All Organization Invitations

Retrieves all pending invitations to the specified Ops Manager
organization.

## Required Roles

You can successfully call this endpoint with the
`Organization User Admin` role.

## Resource

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /orgs/{ORG-ID}/invites
```

### Request Path Parameters

| Path Element | Type | Necessity | Description |
|---|---|---|---|
| ORG-ID | string | Required | Unique 24-hexadecimal digit string that identifies the organization. |

### Request Query Parameters

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

|  |  |  |  |  |
|---|---|---|---|---|
| username | string | Optional | Email address of the invited user. This is the address to which Ops Manager sent the invite. If omitted, Ops Manager returns all pending invitations. |  |

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

The response JSON (Javascript Object Notation) document includes an array of objects.
Each object represents one invitation to the Ops Manager project.

| Name | Type | Description |
|---|---|---|
| createdAt | string | Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when Ops Manager sent the invitation. |
| expiresAt | string | Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the invitation expires. Users have 30 days to accept an invitation to an Ops Manager project. |
| id | string | Unique 24-hexadecimal digit string that identifies the invitation. |
| inviterUsername | string | Ops Manager user who invited **username** to the organization. |
| orgId | string | Unique 24-hexadecimal digit string that identifies the organization. |
| orgName | string | Name of the organization. |
| roles | array of strings | Ops Manager roles to assign to the invited user. If the user accepts the invitation, Ops Manager assigns these roles to them. |
| teamIds | array of strings | Unique 24-hexadecimal digit strings that identify the teams that the user was invited to join. |
| username | string | Email address to which Ops Manager sent the invitation. If the user accepts the invitation, they use this email address as their Ops Manager username. |

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest --include \
     --header "Accept: application/json" \
     --request GET "https://opsmanager.example.com/api/public/v1.0/orgs/{ORG-ID}/invites?pretty=true"
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
[
  {
    "createdAt": "2021-02-18T18:51:46Z",
    "expiresAt": "2021-03-20T18:51:46Z",
    "id": "{INVITATION-ID-1}",
    "inviterUsername": "admin@example.com",
    "orgId": "{ORG-ID}",
    "orgName": "{ORG-NAME}",
    "roles": [
      "GROUP_OWNER"
    ],
    "teamIds": [],
    "username": "jane.smith@example.com"
  },
  {
    "createdAt": "2021-02-18T21:28:38Z",
    "expiresAt": "2021-03-20T21:28:38Z",
    "id": "{INVITATION-ID-2}",
    "inviterUsername": "admin@example.com",
    "orgId": "{ORG-ID}",
    "orgName": "{ORG-NAME}",
    "roles": [
      "ORG_MEMBER"
    ],
    "teamIds": [],
    "username": "john.smith@example.com"
  },
  {
    "createdAt": "2021-02-18T21:05:40Z",
    "expiresAt": "2021-03-20T21:05:40Z",
    "id": "{INVITATION-ID-3}",
    "inviterUsername": "admin@example.com",
    "orgId": "{ORG-ID}",
    "orgName": "{ORG-NAME}",
    "roles": [
      "ORG_MEMBER"
    ],
    "teamIds": [],
    "username": "wyatt.smith@example.com"
  }
]
```
