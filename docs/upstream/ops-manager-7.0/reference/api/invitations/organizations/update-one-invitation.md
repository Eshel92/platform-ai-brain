<!-- Converted from reference/api/invitations/organizations/update-one-invitation.txt (reStructuredText). Includes are inlined. -->

# Update One Organization Invitation

Updates one pending invitation to the Ops Manager organization that you
specify.

## Required Roles

You can successfully call this endpoint with the
`Organization User Admin` role.

## Resource

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
PATCH /orgs/{ORG-ID}/invites
```

### Request Path Parameters

| Path Element | Type | Necessity | Description |
|---|---|---|---|
| ORG-ID | string | Required | Unique 24-hexadecimal digit string that identifies the organization. |

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

* - Body Parameter
  - Type
  - Necessity
  - Description

* - roles
  - array of strings
  - Required
  - Ops Manager roles to assign to the invited
    user.

    If the user accepts the invitation, Ops Manager assigns these roles
    to them.

    **Important:**

    Ops Manager replaces the **roles** in the invitation with
    those that you provide in this request.

    Ensure that you include all roles that you want to assign the
    user in this request.

* - username
  - string
  - Required
  - Username of the user whose invitation you want to update. In
    Ops Manager, an invited user's username is the email address to
    which Ops Manager sent the invitation.

## Response

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
     --header "Content-Type: application/json" \
     --request PATCH "https://opsmanager.example.com/api/public/v1.0/orgs/{ORG-ID}/invites?pretty=true" \
     --data '
       {
         "roles": [
           "ORG_OWNER"
         ],
         "username": "wyatt.smith@example.com"
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
   "createdAt": "2021-02-18T21:05:40Z",
   "expiresAt": "2021-03-20T21:05:40Z",
   "id": "{INVITATION-ID}",
   "inviterUsername": "admin@example.com",
   "orgId": "{ORG-ID}",
   "orgName": "{ORG-NAME}",
   "roles": [
     "ORG_OWNER"
   ],
   "teamIds": [],
   "username": "wyatt.smith@example.com"
}
```
