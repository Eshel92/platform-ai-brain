<!-- Converted from reference/api/usage/update-default-server-type-for-one-organization.txt (reStructuredText). Includes are inlined. -->

# Update Default Server Type For One Organization

Update the default server type for one organization.

## Required Roles

Your API Key must have the `Global Owner` role to
successfully call this resource.

## Request

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
PUT /usage/organizations/{orgId}/defaultServerType
```

### Request Path Parameters

Ops Manager requires all request path parameters:

| Request Parameters | Type | Description |
|---|---|---|
| orgId | string | Unique identifier of the organization. |

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

* - serverType
  - object
  - Required
  - Server Type of the physical host.

* - | serverType
    | .name
  - object
  - Required
  - Server Type value for the physical host.

    You can set this to one of the following values:

    - `DEV_SERVER`
    - `TEST_SERVER`
    - `PRODUCTION_SERVER`
    - `RAM_POOL`

    To learn more, see admin-console-general-mongodb-usage.

* - | serverType
    | .label
  - object
  - Optional
  - Server Type label for the physical host.

    You can set this to one of the following values:

    - **Dev Server**
    - **Test Server**
    - **Production Server**
    - **Ram Pool**

    To learn more, see admin-console-general-mongodb-usage.

## Response

* - Response Element
  - Type
  - Description

* - serverType
  - object
  - Server Type of the physical host.

* - | serverType
    | .name
  - object
  - Server Type value for the physical host.

    Ops Manager returns one of following values:

    - `DEV_SERVER`
    - `TEST_SERVER`
    - `PRODUCTION_SERVER`
    - `RAM_POOL`

    To learn more, see admin-console-general-mongodb-usage.

* - | serverType
    | .label
  - object
  - Server Type label for the physical host.

    Ops Manager returns one of following values:

    - **Dev Server**
    - **Test Server**
    - **Production Server**
    - **Ram Pool**

    To learn more, see admin-console-general-mongodb-usage.

## Example Request

```sh
curl --user "{publicApiKey}:{privateApiKey}" --digest \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/json' \
     --include \
     --request PUT 'https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/usage/organizations/{orgId}/defaultServerType?pretty=true' \
     --data '{
       "serverType":{
          "name":"RAM_POOL",
          "label":"RAM Pool"
       }
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

This endpoint doesn't return a response body.
