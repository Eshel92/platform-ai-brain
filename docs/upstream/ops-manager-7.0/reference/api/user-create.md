<!-- Converted from reference/api/user-create.txt (reStructuredText). Includes are inlined. -->

# Create One User

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Create a new user. By default, any non-global organization and project 
roles in the payload send users an invitation to the organization or  
project first.

## Resource

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
POST /users
```

### Request Path Parameters

This endpoint doesn't use HTTP request path parameters.

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

All fields are required.

* - Name
  - Type
  - Description

* - username
  - string
  - Username of the Ops Manager user. Validated depending on the 
    value of the `mms.email.validation` property:

    | Value | Description |
    |---|---|
    | `false` | (**Default**) Username is not required to be an email address. |
    | `loose` | Username must contain an `@` symbol followed by a period. |
    | `strict` | Username must adhere to a strict email address validation regular expression. |

    See `mms.email.validation` for details.

* - password
  - string
  - Password of the Ops Manager user. 

    This field is *not* included in the
    entity returned from the server. It can be sent only in the entity body when you create a new user.

* - emailAddress
  - string
  - Email address of the Ops Manager user.

* - mobileNumber
  - string
  - Mobile telephone number of the Ops Manager user.

* - firstName
  - string
  - First name of the Ops Manager user.

* - lastName
  - string
  - Last name of the Ops Manager user.

* - roles
  - object array
  - Role assignments of the Ops Manager user.

* - roles.orgId
  - string
  - Unique identifier of the organization in which the Ops Manager user
    has the specified role.

* - roles.groupId
  - string
  - Unique identifier of the group in which the Ops Manager user has the
    specified role.

    For the "global" roles (those whose name starts
    with `GLOBAL_`) there is no `groupId` since these
    roles are not tied to a group.

* - roles.roleName
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
     --request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/users" \
     --data '
       {
         "username": "jane.doe@mongodb.com",
         "emailAddress": "jane.doe@mongodb.com",
         "firstName": "Jane",
         "lastName": "Doe",
         "password": "M0ng0D8!:)",
         "roles": [{
           "groupId": "533daa30879bb2da07807696",
           "roleName": "GROUP_USER_ADMIN"
         },{
           "orgId" : "55555bbe3bd5253aea2d9b16",
           "roleName" : "ORG_MEMBER"
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
HTTP/1.1 201 Created
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
  "id" : "533dc19ce4b00835ff81e2eb",
  "username" : "jane.doe@mongodb.com",
  "emailAddress" : "jane.doe@mongodb.com",
  "firstName" : "Jane",
  "lastName" : "Doe",
  "roles" : [],
  "links" : []
}
```
