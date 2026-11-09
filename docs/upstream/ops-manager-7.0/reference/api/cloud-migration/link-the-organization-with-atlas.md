<!-- Converted from reference/api/cloud-migration/link-the-organization-with-atlas.txt (reStructuredText). Includes are inlined. -->

# Connect One Organization with One Atlas Organization

Connect the source Ops Manager organization with a target MongoDB Atlas
organization.

## Required Roles

Your API Key must have the `Organization Owner` role to
successfully call this resource.

## Request

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
POST /orgs/{orgId}/liveExport/migrationLink
```

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| orgId | string | Required | Unique 24-hexadecimal digit string that identifies the source organization that contains your projects. |

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

| Name | Type | Necessity | Description |
|---|---|---|---|
| linkToken | string | Required | String that contains the information necessary to connect from MongoDB Cloud Manager or Ops Manager to MongoDB Atlas during a Live Migration from a MongoDB Cloud Manager or Ops Manager deployment to a cluster in MongoDB Atlas. When you migrate data from a MongoDB Cloud Manager or Ops Manager deployment, you need to do the following: 1. Generate a link-token in MongoDB Atlas 2. Enter it in your MongoDB Cloud Manager or Ops Manager organization’s settings. You use the same link-token to migrate each deployment in your MongoDB Cloud Manager or Ops Manager organization sequentially, one at a time. You can generate multiple link-tokens in MongoDB Atlas. Use one unique link-token for each MongoDB Cloud Manager or Ops Manager organization. |

## Response

| Name | Type | Description |
|---|---|---|
| status | string | State of the connection that exists between this organization and the target cluster in the MongoDB Atlas organization. Response returns `"SYNCED"` or `"NOT_SYNCED"`. |

## Example Request

```sh
curl --user '{USERNAME}:{APIKEY}' --digest \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/json' \
     --include \
     --request POST 'https://{OPSMANAGER-HOST}:{PORT}/api/atlas/v1.0/orgs/{orgId}/liveExport/migrationLink?pretty=true' \
     --data '{
         "linkToken": "string"
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
  "status": "SYNCED"
}
```
