<!-- Converted from reference/api/user-update.txt (reStructuredText). Includes are inlined. -->

# Update Roles for One User

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Add, update, or remove a user's roles within an organization or 
project. By default, any new non-global organization and project 
roles in the payload send users an invitation to the organization or 
project first. You can add users directly to an organization or project 
only if you set the `mms.user.bypassInviteForExistingUsers` 
setting to `true`.

## Resource

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
PATCH /users/{USER-ID}
```

## Required Roles

You must have the appropriate Owner roles to use this API (Application Programming Interface) endpoint.

| Level | Needed Role |
|---|---|
| Organization | `Organization Owner` |
| Project | `Project Owner` |

**Important:**

You can always update your own user account.

If you own an organization or project, you can update the
user roles for any user with membership in that
organization or project. You cannot modify any other user profile
information.

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| `USER-ID` | string | Required | Unique identifier of the user that you want to retrieve. To retrieve the `USER-ID` for a user, see api-get-all-users-in-group. |

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

* - Name
  - Type
  - Necessity
  - Description

* - `roles`
  - array of objects
  - Required
  - Role assigned to the Ops Manager user.

* - | `roles`
    | `.orgId`
  - string
  - Optional
  - Unique identifier of the organization in which the Ops Manager user
    has the specified role.

* - | `roles`
    | `.groupId`
  - string
  - Optional
  - Unique identifier of the project in which the Ops Manager user has the
    specified role.

    Roles that start with `GLOBAL_` don't require a `groupId`.
    These roles aren't tied to a project.

* - | `roles`
    | `.roleName`
  - string
  - Optional
  - Name of the role. Accepted values are:

    | Value | Description |
    |---|---|
    | `ORG_MEMBER` | `Organization Member` |
    | `ORG_READ_ONLY` | `Organization Read Only` |
    | `ORG_GROUP_CREATOR` | `Organization Project Creator` |
    | `ORG_OWNER` | `Organization Owner` |
    | `GROUP_AUTOMATION_ADMIN` | `Project Automation Admin` |
    | `GROUP_BACKUP_ADMIN` | `Project Backup Admin` |
    | `GROUP_MONITORING_ADMIN` | `Project Monitoring Admin` |
    | `GROUP_OWNER` | `Project Owner` |
    | `GROUP_READ_ONLY` | `Project Read Only` |
    | `GROUP_USER_ADMIN` | `Project User Admin` |
    | `GROUP_DATA_ACCESS_ADMIN` | `Project Data Access Admin` |
    | `GROUP_DATA_ACCESS_READ_ONLY` | `Project Data Access Read Only` |
    | `GROUP_DATA_ACCESS_READ_WRITE` | `Project Data Access Read/Write` |
    | `GLOBAL_AUTOMATION_ADMIN` | `Global Automation Admin` |
    | `GLOBAL_BACKUP_ADMIN` | `Global Backup Admin` |
    | `GLOBAL_MONITORING_ADMIN` | `Global Monitoring Admin` |
    | `GLOBAL_OWNER` | `Global Owner` |
    | `GLOBAL_READ_ONLY` | `Global Read Only` |
    | `GLOBAL_USER_ADMIN` | `Global User Admin` |

## Response

The JSON (Javascript Object Notation) document contains each of the following elements:

* - `Name`
  - Type
  - Description

* - `emailAddress`
  - string
  - Email address of the Ops Manager user.

* - `firstName`
  - string
  - First name of the Ops Manager user.

* - `id`
  - string
  - Unique identifier of the Ops Manager user.

* - `lastName`
  - string
  - Last name of the Ops Manager user.

* - `links`
  - object array
  - Links to related sub-resources. All `links` arrays in
    responses include at least one link called self. The
    relationship between URLs are explained in the
    Web Linking Specification.

* - `mobileNumber`
  - string
  - Mobile number of the Ops Manager user.

* - `roles`
  - empty array
  - Role assigned to the Ops Manager user.

* - | `roles`
    | `.groupId`
  - string
  - Unique identifier for the project in which the user has the
    specified role.

    Roles that start with `GLOBAL_` don't require a
    `groupId`. These roles aren't tied to a project.

* - | `roles`
    | `.orgId`
  - string
  - Unique identifier for the organization in which the user has
    the specified role.

* - | `roles`
    | `.roleName`
  - string
  - Name of the role. Accepted values are:

    | Value | Description |
    |---|---|
    | `ORG_MEMBER` | `Organization Member` |
    | `ORG_READ_ONLY` | `Organization Read Only` |
    | `ORG_GROUP_CREATOR` | `Organization Project Creator` |
    | `ORG_OWNER` | `Organization Owner` |
    | `GROUP_AUTOMATION_ADMIN` | `Project Automation Admin` |
    | `GROUP_BACKUP_ADMIN` | `Project Backup Admin` |
    | `GROUP_MONITORING_ADMIN` | `Project Monitoring Admin` |
    | `GROUP_OWNER` | `Project Owner` |
    | `GROUP_READ_ONLY` | `Project Read Only` |
    | `GROUP_USER_ADMIN` | `Project User Admin` |
    | `GROUP_DATA_ACCESS_ADMIN` | `Project Data Access Admin` |
    | `GROUP_DATA_ACCESS_READ_ONLY` | `Project Data Access Read Only` |
    | `GROUP_DATA_ACCESS_READ_WRITE` | `Project Data Access Read/Write` |
    | `GLOBAL_AUTOMATION_ADMIN` | `Global Automation Admin` |
    | `GLOBAL_BACKUP_ADMIN` | `Global Backup Admin` |
    | `GLOBAL_MONITORING_ADMIN` | `Global Monitoring Admin` |
    | `GLOBAL_OWNER` | `Global Owner` |
    | `GLOBAL_READ_ONLY` | `Global Read Only` |
    | `GLOBAL_USER_ADMIN` | `Global User Admin` |

* - `username`
  - string
  - Username of the Ops Manager user.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request PATCH "https://<OpsManagerHost>:<Port>/api/public/v1.0/users/{USER-ID}" \
     --data '
       {
         "roles": [{
           "groupId": "{GROUP-ID}",
           "roleName": "{ROLE}"
         }]
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
  "id": "{USER-ID}",
  "username": "jane",
  "emailAddress": "jane@qa.example.com",
  "firstName": "Jane",
  "lastName": "D'oh",
  "links": [{
    "href": "https://<OpsManagerHost>:<Port>/api/public/v1.0/users/{USER-ID}",
    "rel": "self"
  },
  {
    "href": "https://<OpsManagerHost>:<Port>/api/public/v1.0/users/{USER-ID}/accessList",
    "rel": "http://mms.mongodb.com/accessList"
  }],
  "roles": [{
    "orgId": "{ORG-ID}",
    "roleName": "ORG_MEMBER"
  },{
    "groupId": "{PROJECT-ID}",
    "roleName": "GROUP_READ_ONLY"
  }],
  "teamIds": []
}
```
