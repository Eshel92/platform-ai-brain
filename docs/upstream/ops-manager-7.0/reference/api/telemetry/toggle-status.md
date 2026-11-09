<!-- Converted from reference/api/telemetry/toggle-status.txt (reStructuredText). Includes are inlined. -->

# Toggle Telemetry Status

Enable or disable telemetry collection for your Ops Manager installation.

## Required Roles

This endpoint requires an API key that has the `Global Owner` role.

## Endpoint

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/private/v1.0/telemetry`

```http
PATCH /collection/status
```

## Request

### Path Parameters

This endpoint doesn't use HTTP request path parameters.

### Query Parameters

This endpoint doesn't use HTTP request query parameters.

### Body Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| enabled | boolean | required | Set to `true` to enable telemetry, or `false` to disable telemetry. |

## Response

### Response Document

This endpoint returns an empty JSON (Javascript Object Notation) object.

## Example Request

```sh
curl --user "{publicApiKey}:{privateApiKey}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request PATCH "https://<OpsManagerHost>:<Port>/api/private/v1.0/telemetry/collection/status"
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
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=ISO-8859-1
Date: {dateInUnixFormat}
X-MongoDB-Service-Version: gitHash={gitHash};
versionString={ApplicationVersion}
Content-Length: {requestLengthInBytes}
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
{}
```
