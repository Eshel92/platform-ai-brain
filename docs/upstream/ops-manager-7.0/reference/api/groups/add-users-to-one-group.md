<!-- Converted from reference/api/groups/add-users-to-one-group.txt (reStructuredText). Includes are inlined. -->

# Add Existing Users to One Project

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

This resource adds users who exist in Ops Manager to another project. It does 
not create new users and add them to a project. By default, users first 
receive an invitation to the project. You can add users directly to a 
project only if you set the
`mms.user.bypassInviteForExistingUsers` setting to `true`.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
POST /groups/{PROJECT-ID}/users
```

## Request Parameters

### Request Path Parameters

| Parameter | Type | Description |
|---|---|---|
| PROJECT-ID | string | *(Required.)* The unique identifier for the project. |

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
| id | string | The unique identifier for an existing user. |
| roles | object array | The roles to which this user is assigned. |
| roles.groupId | string | The unique identifier for the project role. |
| roles.roleName | string | The display name for the user role. |

## Response

| Name | Type | Description |
|---|---|---|
| emailAddress | string | The email address for the Ops Manager user. |
| firstName | string | The first name displayed for the returned Ops Manager user. |
| id | string | The unique identifier for the user. |
| links | object array | .. include:: /includes/api/links-explanation.rst |
| lastName | string | The last name displayed for the returned Ops Manager user. |
| roles | object array | The roles to which this user is assigned. |
| roles.groupId | string | The unique identifier for the project role. |
| roles.roleName | string | The display name for the user role. |
| username | string | The Ops Manager username. |

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --header "Content-Type: application/json" \
 --include \
 --request POST "https://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/users?pretty=true" \
 --data '
 [
   {
     "id": "{USER-ID}",
     "roles": [{
       "roleName": "GROUP_OWNER"
     }]
   }
 ]'
```

**Note:**

You must send an array of entities, even if adding a single user. For
each user that you wish to add, specify the user ID and the roles the
user should possess. For role values, see the description of the
`roles.roleName` field in the
users resource.

If you specify a user that is already a member of the project, their
existing roles are overwritten with the specified permissions.

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
    "href" : "http://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/users?pretty=true&pageNum=1&itemsPerPage=100",
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
    } ],
    "username" : "jim.bloggs"
  } ],
  "totalCount" : 2
}
```
