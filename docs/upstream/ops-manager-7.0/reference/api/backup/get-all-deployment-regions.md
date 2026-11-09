<!-- Converted from reference/api/backup/get-all-deployment-regions.txt (reStructuredText). Includes are inlined. -->

# Get All Deployment Regions

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /admin/backup/backupDeployments
```

## Request Parameters

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

### Request Body

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --include \
     --request GET "https://{opsManagerHost}:{port}/api/public/v1.0/admin/backup/backupDeployments"
```

### Response Body

```json
{
  "links" : [ ],
  "results" : [ {
    "assignmentEnabled" : true,
    "bqProxyEndpoint" : "queryable-backup.mongodb.com:27217",
    "deploymentDescription" : "Eastern US",
    "id" : "NY_NJ",
    "ingestionEndpoint" : "https://api-backup.mongodb.com",
    "links" : [ ],
    "restoreEndpoint" : "https://api-backup.mongodb.com"
  } ],
  "totalCount" : 1
}
```
