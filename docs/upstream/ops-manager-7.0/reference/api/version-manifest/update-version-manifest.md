<!-- Converted from reference/api/version-manifest/update-version-manifest.txt (reStructuredText). Includes are inlined. -->

# Update the Version Manifest

Use this resource to upload the latest version manifest from
MongoDB, Inc.

**Warning:**

Don't change any values in the JSON (Javascript Object Notation) file. The parameters and
values in this file -- as well as how they are structured -- can
change without notice.

## Required Roles

You can successfully call this endpoint with any of the following
assigned roles:

- `Global Owner`
- `Global Automation Admin`

**See also:**

om-update-version-manifest-api-tutorial.

   

## Resource

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
PUT /versionManifest
```

### Request Path Parameters

This endpoint doesn't use HTTP request path parameters.

### Request Query Parameters

The following query parameters are optional:

| Name | Type | Description | Default |
|---|---|---|---|
| `pretty` | boolean | Indicates whether the response body should be in a [prettyprint](https://en.wikipedia.org/wiki/Prettyprint?oldid=791126873) format. | `false` |

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

These values may change at any time without notice. They remain
compatible with Ops Manager.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request PUT "https://<OpsManagerHost>:<Port>/api/public/v1.0/versionManifest?pretty=true" \
     --data @4.2.json
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

The JSON (Javascript Object Notation) file includes all data that your Ops Manager instance needs.
This covers all available versions and variants of MongoDB to download
and deploy to Ops Manager\-managed MongoDB hosts.

The parameters and values in this file -- as well as how they are
structured -- can change without notice.
