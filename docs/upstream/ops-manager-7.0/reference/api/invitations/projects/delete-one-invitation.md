<!-- Converted from reference/api/invitations/projects/delete-one-invitation.txt (reStructuredText). Includes are inlined. -->

# Delete One Project Invitation

Deletes one pending invitation to the Ops Manager project that you
specify. You can't delete an invitation that a user has accepted.

## Required Roles

You can successfully call this endpoint with the
`Project User Admin` role.

## Resource

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
DELETE /groups/{GROUP-ID}/invites/{INVITATION-ID}
```

### Request Path Parameters

| Path Element | Type | Necessity | Description |
|---|---|---|---|
| GROUP-ID | string | Required | Unique 24-hexadecimal digit string that identifies the project. |
| INVITATION-ID | string | Required | Unique 24-hexadecimal digit string that identifies the invitation. |

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

This endpoint does not have response elements.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest --include \
     --header "Accept: application/json" \
     --request DELETE "https://opsmanager.example.com/api/public/v1.0/groups/{GROUP-ID}/invitations/{INVITATION-ID}"
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
HTTP/1.1 204 No Content
Vary: Accept-Encoding
Content-Type: application/json
Strict-Transport-Security: max-age=300
Date: {dateInUnixFormat}
Connection: keep-alive
Content-Length: {requestLengthInBytes}
X-MongoDB-Service-Version: gitHash={gitHash}; versionString={ApplicationVersion}
```

### Response Body

This endpoint returns an empty JSON (Javascript Object Notation) object.
