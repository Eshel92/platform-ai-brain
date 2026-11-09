<!-- Converted from reference/api/teams/teams-add-user.txt (reStructuredText). Includes are inlined. -->

# Add Users to Team

**Note:**

This endpoint is incompatible with projects using
LDAP Authentication.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Syntax

```none
POST /orgs/{ORG-ID}/teams/{TEAM-ID}/users
```

### Request Path Parameters

| Path Element | Required/Optional | Description |
|---|---|---|
| `ORG-ID` | Required. | The unique identifier for the organization you want to associate the team with. |
| `TEAM-ID` | Required | The name of the team you want to add users to. |

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

Specify an array of documents, where each document represents one
user you want to add to the team. Each document in the array
must contain the following fields:

| Name | Type | Description |
|---|---|---|
| `id` | string | The unique ID of the user you want to add to the team |

## Response

### Response Document

The response JSON (Javascript Object Notation) document includes an array of result
objects, an array of link objects and a count of the total
number of result objects retrieved.

| Name | Type | Description |
|---|---|---|
| `results` | array | Array includes one object for each item detailed in the results-embedded-document-get-all section. |
| `links` | array | Array includes one or more links to sub-resources and/or related resources. The relations between URL (Uniform Resource Locator)\s are explained in the Web Linking Specification. |
| `totalCount` | number | Integer count of the total number of items in the result set. It may be greater than the number of objects in the results array if the entire result set is paginated. |

### `results` Embedded Document

Each element in the `result` array is one user added to the team.

| Name | Type | Description |
|---|---|---|
| `country` | string | The [ISO 3166 Alpha-2](https://www.iso.org/iso-3166-country-codes.html) country code associated with the user. |
| `emailAddress` | string | The email address associated with the user. |
| `firstName` | string | The first name of the user. |
| `id` | string | The unique identifier for the team. |
| `lastName` | string | The last name of the user. |
| `links` | array | .. include:: /includes/api/links-explanation.rst |
| `mobileNumber` | string | The phone number associated with the user. |
| `roles` | array | Each object in the `roles` array represents the MongoDB Atlas organization role the user has for the associated `org_id` |
| `roles.orgId` | string | ID of the organization where the user has the assigned `roles.roleName` organization role. |
| `roles.roleName` | string | The organization role assigned to the user for the specified `roles.orgId`. |
| `teamsId` | array | Each string in the array is a team associated with the user. |
| `username` | string | Username associated with the user. |

## Example Request

```sh
 curl -u "username:apiKey" --digest \
 --header "Accept: application/json" \
 --header "Content-Type: application/json" \
 --request POST "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/orgs/{ORG-ID}/teams/{TEAM-ID}/users?pretty=true" \
 --data '[{ "id" : "{USER-ID}" }]'
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
 "links": [
     {
         "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/orgs/{ORG-ID}/teams/{TEAM-ID}/users?pretty=true",
         "rel": "self"
     }
 ],
 "results": [
     {
         "country": "US",
         "emailAddress": "JohnDoe@example.com",
         "firstName": "John",
         "id": "{USER-ID}",
         "lastName": "Doe",
         "links": [
             {
                 "href": "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/users/{USER-ID}",
                 "rel": "self"
             }
         ],
         "mobileNumber": "5555550100",
         "roles": [
             {
                 "orgId": "{ORG-ID}",
                 "roleName": "ORG_MEMBER"
             },
             ...
         ],
         "teamIds": [ "{TEAM-ID}" ],
         "username": "JohnDoe@example.com"
     }
 ],
 "totalCount": 1
}
```
