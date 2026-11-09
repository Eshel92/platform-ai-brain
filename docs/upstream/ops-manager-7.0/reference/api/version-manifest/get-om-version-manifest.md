<!-- Converted from reference/api/version-manifest/get-om-version-manifest.txt (reStructuredText). Includes are inlined. -->

# Retrieve the Ops Manager Version Manifest

Use this resource to retrieve the version manifest that Ops Manager is
configured to use.

Your Ops Manager instance might not return MongoDB's most recent version
manifest. Instances with limited internet access might have this issue.

**See also:**

Version Manifest

**Warning:**

Don't change any values in the JSON (Javascript Object Notation) file. The parameters and
values in this file -- as well as how they are structured -- can
change without notice.

## Required Roles

You can successfully call this endpoint without having an API key or 
assigned roles in any organization or project.

## Resource

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /unauth/versionManifest
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
curl --include --header "Accept: application/json" \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/unauth/versionManifest?pretty=true"
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

Ops Manager returns the version manifest that it is configured to use.

The parameters and values in this file -- as well as how they are
structured -- can change without notice.
