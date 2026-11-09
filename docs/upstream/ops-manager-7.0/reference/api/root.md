<!-- Converted from reference/api/root.txt (reStructuredText). Includes are inlined. -->

# Root

The **root** resource is the starting point for the Ops Manager API. From
here, you can traverse the `links` to reach all other API resources.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /
```

### Request Path Parameters

This endpoint doesn't use HTTP request path parameters.

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

The response includes:

| Name | Type | Description |
|---|---|---|
| appName | string | MongoDB Ops Manager |
| build | string | The SHA that corresponds to the GitHub commit for the Ops Manager. |
| links | object array | .. include:: /includes/api/links-explanation.rst |
| throttling | boolean | The field is obsolete and has the value `false`. |

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \ 
 --header 'Accept: application/json' \ 
 --include \ 
 --request GET "<ops-manager-host>:<port>/api/public/v1.0"
```

## Example Response

```json
{
   "appName" : "MongoDB Ops Manager",
   "build" : "ec8b09b880be314981caa9d8fbefc3280056522e",
   "links" : [

   ],
   "throttling" : false
}
```
