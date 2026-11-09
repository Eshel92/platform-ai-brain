<!-- Converted from reference/api/groups/get-all-users-in-one-group.txt (reStructuredText). Includes are inlined. -->

# Get All Users in One Project

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/users
```

## Request Parameters

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| PROJECT-ID | string | Required | Unique identifier for the project. |

### Request Query Parameters

* - Name
  - Type
  - Necessity
  - Description

* - flattenTeams
  - boolean
  - Optional
  - Flag that indicates whether the returned list should include
    users who belong to a team assigned a role in this project. You
    may not have assigned the individual users a role in this
    project.

    - If this flag is set to `false`, the endpoint returns only
      users that were assigned a role in the project.

    - If this flag is set to `true`, the endpoint returns both
      users that were assigned roles in the project *and* users who
      are members of teams that were assigned roles in the project.

* - includeOrgUsers
  - boolean
  - Optional
  - Flag that indicates whether the returned list should include
    users with implicit access to the project through the
    `Organization Owner` or 
    `Organization Read Only` role. You might not have
    assigned the individual users a role in this project.

    - If this flag is set to `false`, the endpoint returns only
      users who are assigned a role in the project.

    - If this flag is set to `true`, the endpoint returns both
      users who are assigned roles in the project *and* users who
      have implicit access to the project through their organization role.

    The default value is `false`.

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

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

Each **result** is one user.

| Name | Type | Description |
|---|---|---|
| emailAddress | string | Email address assigned to the returned MongoDB Atlas user. |
| firstName | string | First name assigned to the returned MongoDB Atlas user. |
| id | string | Unique identifier assigned to the returned MongoDB Atlas user. |
| lastName | string | Last name assigned to the returned MongoDB Atlas user. |
| links | object array | .. include:: /includes/api/links-explanation.rst |
| roles | object array | Roles assigned to the returned MongoDB Atlas user. |
| roles.groupId | string | Unique identifier for the project to which the returned MongoDB Atlas user was assigned the role provided in `role.roleName`. |
| roles.orgId | string | Unique identifier for the organization to which the returned MongoDB Atlas user was assigned the role provided in `role.roleName`. |
| roles.roleName | string | Display name for the role assigned to the returned MongoDB Atlas user for either the group provided in `role.groupId` or the organization provided in `role.orgId`. |
| username | string | MongoDB Atlas username given to the returned MongoDB Atlas user. |

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --include \
 --request GET "https://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/users?pretty=true&includeOrgUsers=true"
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
  "links" : [ {
    "href" : "http://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/ users?pretty=true&pageNum=1&itemsPerPage=100",
    "rel" : "self"
  } ],
  "results" : [ {
    "emailAddress" : "joe.bloggs@example.com",
    "firstName" : "Joe",
    "id" : "{USER-ID}",
    "lastName" : "Bloggs",
    "links" : [ {
      "href" : "http://{opsManagerHost}:{port}/api/public/v1.0/users/{USER-ID}",
      "rel" : "self"
    }, {
      "href" : "http://{opsManagerHost}:{port}/api/public/v1.0/users/{USER-ID}/accessList",
      "rel" : "http://mms.mongodb.com/accessList"
    } ],
    "roles" : [ {
      "groupId" : "{PROJECT-ID}",
      "roleName" : "GROUP_OWNER"
    }, {
      "groupId" : "{OTHER-PROJECT-ID}",
      "roleName" : "GROUP_OWNER"
    }
    ...
    ],
    "username" : "joe.bloggs"
  }, {
    "emailAddress" : "jim.bloggs@example.com",
    "firstName" : "Jim",
    "id" : "{OTHER-USER-ID}",
    "lastName" : "Bloggs",
    "links" : [ {
      "href" : "http://{opsManagerHost}:{port}/api/public/v1.0/users/{OTHER-USER-ID}",
      "rel" : "self"
    }, {
      "href" : "http://{opsManagerHost}:{port}/api/public/v1.0/users/{OTHER-USER-ID}/accessList",
      "rel" : "http://mms.mongodb.com/accessList"
    } ],
    "roles" : [ {
      "roleName" : "GLOBAL_READ_ONLY"
    }, {
      "groupId" : "{PROJECT-ID}",
      "roleName" : "GROUP_OWNER"
    }, {
      "orgId" : "{ORGANIZATION-ID}",
      "roleName" : "ORG_READ_ONLY"
    } ],
    "username" : "jim.bloggs"
  } ],
  "totalCount" : 2
}
```
