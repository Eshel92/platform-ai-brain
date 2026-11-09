<!-- Converted from reference/api/user-create-first.txt (reStructuredText). Includes are inlined. -->

# Create the First User

Create the first Ops Manager user. You *can* call this endpoint without
having an API (Application Programming Interface) key.

**Important:** Exceptions

- This endpoint cannot be used if Ops Manager uses
  LDAP for authentication.
- This endpoint can create the first user only if Ops Manager runs in
  `Invitation Only Mode`.

Ops Manager grants the first Ops Manager programmatic API (Application Programming Interface) key created
through this endpoint the GLOBAL_OWNER role.
The returned JSON (Javascript Object Notation) document includes the first programmatic API (Application Programming Interface) key, which
you can use to make further API (Application Programming Interface) calls.

This endpoint doesn't create projects or organizations. With the new
programmatic API (Application Programming Interface) key that it created, you can call the
Create a Project
endpoint. That endpoint can create a project and organization in one
API (Application Programming Interface) call. You can't login to Ops Manager until after you have created a
project.

You *can* use this endpoint to create additional users with the
following caveats:

- Ops Manager doesn't grant the GLOBAL_OWNER role
  for those subsequent users unless you add the role to the API (Application Programming Interface)
  request.
- Ops Manager doesn't create a programmatic API (Application Programming Interface) key for subsequent users.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
POST /unauth/users
```

### Request Path Parameters

This endpoint doesn't use HTTP request path parameters.

### Request Query Parameters

| Name | Type | Description |
|---|---|---|
| whitelist | string | IP address that you want to add to the whitelist for the first Ops Manager user. You can add more than one `whitelist` parameter and value. |

### Request Body Parameters

* - Name
  - Type
  - Necessity
  - Description

* - `username`
  - string
  - Required
  - Username of the first Ops Manager user. Validated depending on the
    value of the `mms.email.validation` property:

    | Value | Description |
    |---|---|
    | `false` | (**Default**) Username is not required to be an email address. |
    | `loose` | Username must contain an `@` symbol followed by a period. |
    | `strict` | Username must adhere to a strict email address validation regular expression. |

    See `mms.email.validation` for details.

    The `username` is usually an email address. If you set this
    value to an email address, you do not need to set the
    `emailAddress` value explicitly.

* - `password`
  - string
  - Required
  - Password of the first Ops Manager user. This field is *not included*
    in the HTTP (Hypertext Transfer Protocol) response body. Ops Manager sends this in the HTTP (Hypertext Transfer Protocol)
    request only when creating the first Ops Manager user.

* - `emailAddress`
  - string
  - Optional
  - Email address of the first Ops Manager user.

* - `firstName`
  - string
  - Required
  - First name of the first Ops Manager user.

* - `lastName`
  - string
  - Required
  - Last name of the first Ops Manager user.

## Response

| Name | Type | Description |
|---|---|---|
| `programmaticApiKey` | object | Details of the first programmatic API (Application Programming Interface) key created in Ops Manager. |
| \| `programmaticApiKey` \| `.desc` | string | Description of the first programmatic API (Application Programming Interface) key. |
| \| `programmaticApiKey` \| `.id` | string | Unique identifier of the first programmatic API (Application Programming Interface) key. |
| \| `programmaticApiKey` \| `.links` | array of objects | .. include:: /includes/api/links-explanation.rst |
| \| `programmaticApiKey` \| `.privateKey` | string | Thirty-one alphanumeric characters and dashes that serve as the password of the first programmatic API (Application Programming Interface) key. |
| \| `programmaticApiKey` \| `.publicKey` | string | Six alphanumeric characters that serve as the username of the first programmatic API (Application Programming Interface) key. |
| \| `programmaticApiKey` \| `.roles` | array of objects | Roles assigned to the first programmatic API (Application Programming Interface) key. |
| \| `programmaticApiKey` \| `.roles.roleName` | string | Name of the assigned role. Ops Manager grants the first programmatic API (Application Programming Interface) key the `Global Owner` role (`GLOBAL_OWNER`). |
| `user` | object | Details of the first Ops Manager user. |
| \| `user` \| `.emailAddress` | string | Email address of the first Ops Manager user. |
| \| `user` \| `.firstName` | string | First name of the first Ops Manager user. |
| \| `user` \| `.id` | string | Unique identifier of the first Ops Manager user. |
| \| `user` \| `.lastName` | string | Last name of the first Ops Manager user. |
| \| `user` \| `.links` | array of objects | .. include:: /includes/api/links-explanation.rst |
| \| `user` \| `.mobileNumber` | string | Mobile number of the first Ops Manager user. |
| \| `user` \| `.roles` | array of objects | Roles assigned to the first Ops Manager user. |
| \| `user` \| `.roles.roleName` | string | Name of the assigned role. Ops Manager grants the first Ops Manager user the `Global Owner` role (`GLOBAL_OWNER`). |
| \| `user` \| `.teamIds` | array of strings | List of unique identifiers for the teams to which the first Ops Manager user belongs. |
| \| `user` \| `.username` | string | Username of the first Ops Manager user. |

## Example Request

```sh
curl --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request POST "https://<OpsManagerHost>:<Port>/api/public/v1.0/unauth/users?pretty=true&whitelist=1.2.3.4&whitelist=2.3.4.5" \
     --data '
       {
         "username": "jane.doe@example.com",
         "password": "Passw0rd.",
         "firstName": "Jane",
         "lastName": "Doe"
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
  "programmaticApiKey": {
    "desc": "Automatically generated Global API key",
    "id": "{API-KEY}",
    "links": [{
      "href": "http://<OpsManagerHost>:<Port>/api/public/v1.0/orgs/null/apiKeys/{API-KEY}",
      "rel": "self"
    }],
    "privateKey": "private key string",
    "publicKey": "public key string",
    "roles": [{
      "roleName": "GLOBAL_OWNER"
    }]
  },
  "user": {
    "emailAddress": "jane.doe@example.com",
    "firstName": "Jane",
    "id": "{USER-ID}",
    "lastName": "Doe",
    "links": [
      {
       "href" : "https://<OpsManagerHost>:<Port>/api/public/v1.0/users/{USER-ID}",
       "rel" : "self"
      }
    ],
    "roles": [
      {
        "roleName": "GLOBAL_OWNER"
      }
    ],
    "username": "jane.doe@example.com"
  }
}
```
