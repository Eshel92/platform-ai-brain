<!-- Converted from reference/api/diagnostics/get-project-diagnostic-archive.txt (reStructuredText). Includes are inlined. -->

# Get One Project Diagnostic Archive

MongoDB engineers may request that Ops Manager administrators provide
diagnostic archives for one project for debugging and troubleshooting.
Project diagnostic archives also contain global system information
about Ops Manager.

## Required Roles

The API Key requires the `Global Monitoring Admin` or
`Global Owner` role to download a diagnostic archive.

## Resource

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /groups/{PROJECT-ID}/diagnostics
```

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| `PROJECT-ID` | string | Required | Unique identifier of the project that owns the diagnostics archive. |

### Request Query Parameters

Provide any of the following query parameters that you need:

| Name | Type | Necessity | Description | Default |
|---|---|---|---|---|
| pageNum | number | Optional | One-based integer that returns a subsection of results. | `1` |
| itemsPerPage | number | Optional | Number of items to return per page, up to a maximum of 500. | `100` |
| pretty | boolean | Optional | Flag that indicates whether the response body should be in a prettyprint format. | `false` |
| envelope | boolean | Optional | Flag that indicates whether or not to wrap the response in an envelope. Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or status code. To remediate this, set `envelope : true` in the query. For endpoints that return a list of results, the `results` object is an envelope. Ops Manager adds the `status` field to the response body. | `false` |
| backupJobsEnabledOnly | boolean | Optional | Flag indicating whether to exclude daemons not enabled for backing up databases from the response. Set this to `false` to include daemon configurations with the `backupJobsEnabled` flag set to `false`. | `true` |

|  |  |  |  |  |
|---|---|---|---|---|
| ageLimit | integer | Optional | Length of time in days to retrieve entries for the diagnostic archive. | 7 |
| limit | integer | Optional | Maximum number of entries for the diagnostic archive. | 1000 |
| minutes | integer | Optional | Time range of the diagnostic archive, beginning at the specified number of minutes in the past and ending at the present time. For example, to retrieve a diagnostic archive with data for the last 10 minutes, specify `minutes=10` in your request . | 1440 |
| sizeLimit | integer | Optional | Maximum file size of each file in the diagnostic archive expressed in the number of characters. This includes values up to the nearest whole value to this limit. | 50000000 |

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

This endpoint returns a compressed (`.tar.gz`) archive file to your 
current working directory with the name you specified using the 
`--output` or the `-o` option.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/gzip" \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/diagnostics?pretty=true" \
     --output project_diagnostics.tar.gz
```

The response saves `project_diagnostics.tar.gz` to your current
working directory on your local host.

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

This endpoint returns a compressed (`.tar.gz`) archive file to your 
current working directory with the name you specified using the 
`--output` or the `-o` option.
