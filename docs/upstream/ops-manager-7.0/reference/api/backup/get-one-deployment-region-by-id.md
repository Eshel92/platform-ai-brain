<!-- Converted from reference/api/backup/get-one-deployment-region-by-id.txt (reStructuredText). Includes are inlined. -->

# Get One Deployment Region

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /admin/backup/backupDeployments/{DEPLOYMENT-ID}
```

## Request Parameters

### Request Path Parameters

| Parameter | Type | Necessity | Description |
|---|---|---|---|
| DEPLOYMENT-ID | string | Required | Unique identifier that references the deployment region in configurations. |

### Request Query Parameters

The following query parameters are optional:

| Name | Type | Necessity | Description | Default |
|---|---|---|---|---|
| pageNum | number | Optional | One-based integer that returns a subsection of results. | `1` |
| itemsPerPage | number | Optional | Number of items to return per page, up to a maximum of 500. | `100` |
| pretty | boolean | Optional | Flag that indicates whether the response body should be in a prettyprint format. | `false` |
| envelope | boolean | Optional | Flag that indicates whether or not to wrap the response in an envelope. Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or status code. To remediate this, set `envelope : true` in the query. For endpoints that return a list of results, the `results` object is an envelope. Ops Manager adds the `status` field to the response body. | `false` |
| backupJobsEnabledOnly | boolean | Optional | Flag indicating whether to exclude daemons not enabled for backing up databases from the response. Set this to `false` to include daemon configurations with the `backupJobsEnabled` flag set to `false`. | `true` |

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

| Name | Type | Description |
|---|---|---|
| `assignmentEnabled` | boolean | Flag indicating whether you can assign Deployment Regions to backup resources. |
| `bqProxyEndpoint` | string | Ops Manager instance that serves `Queryable Backup` requests. Value is in the following format: `domain:port`. For example, `localhost:8080`. |
| `deploymentDescription` | string | String that describes the purpose of the deployment region. |
| `id` | string | Unique identifier that references this deployment region in configurations. |
| `ingestionEndpoint` | string | Ops Manager instance to which the `Backup Agent` writes snapshot or oplog data. Value is a valid URL (Uniform Resource Locator) such as `http://www.mongodb.com`. Supports both HTTP (Hypertext Transfer Protocol) and HTTPS (Hypertext Transfer Protocol Secure). |
| `links` | object array | .. include:: /includes/api/links-explanation.rst |
| `restoreEndpoint` | string | Ops Manager instance that serves restore requests. |

## Example Request

```sh
curl --user "{publicKey}:{privateKey}" --digest \
     --header "Accept: application/json" \
     --include \
     --request GET "https://{opsManagerHost}:{port}/api/public/v1.0/admin/backup/backupDeployments/NY_NJ?pretty=true"
```

### Example Response

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
   "assignmentEnabled" : true,
   "bqProxyEndpoint" : "queryable-backup.mongodb.com:27217",
   "deploymentDescription" : "Eastern US",
   "id" : "NY_NJ",
   "ingestionEndpoint" : "https://api-backup.mongodb.com",
   "links" : [ ],
   "restoreEndpoint" : "https://api-backup.mongodb.com"
}
```
