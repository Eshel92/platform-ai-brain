<!-- Converted from reference/api/maintenance-windows-get-all.txt (reStructuredText). Includes are inlined. -->

# Get All Maintenance Windows

Retrieve all maintenance windows with end dates in the future.

## Required Roles

You can successfully call this endpoint with any assigned role.

## Request

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /groups/{PROJECT-ID}/maintenanceWindows/
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| `PROJECT-ID` | string | Unique identifier of the project. |

### Request Query Parameters

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

This endpoint doesn't use HTTP request body parameters.

## Response

### Response Document

The response JSON (Javascript Object Notation) document includes an array of result
objects, an array of link objects and a count of the total
number of result objects retrieved.

| Name | Type | Description |
|---|---|---|
| `results` | array | Array includes one object for each item detailed in the results-embedded-document-get-all section. |
| `links` | array | Array includes one or more links to sub-resources and/or related resources. The relations between URL (Uniform Resource Locator)\s are explained in the Web Linking Specification. |
| `totalCount` | number | Integer count of the total number of items in the result set. It may be greater than the number of objects in the results array if the entire result set is paginated. |

### `results` Embedded Document

Each **result** is one maintenance window.

| Name | Type | Description |
|---|---|---|
| `id` | string | Unique identifier of the maintenance window. |
| `groupId` | string | Unique identifier of the project to which this maintenance window applies. |
| `created` | string | Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the maintenance window was created. |
| `updated` | string | Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the maintenance window was last updated. |
| `startDate` | string | Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the maintenance window starts. |
| `endDate` | string | Timestamp in ISO 8601 date and time format in UTC (Coordinated Universal Time) when the maintenance window ends. |
| `alertTypeNames` | array of strings | Alert types to silence during maintenance window. For example: `HOST`, `REPLICA_SET`, `CLUSTER`, `AGENT`, `BACKUP` |
| `description` | string | Description of the maintenance window. This field is returned only if you provided a description of the maintenance window. |

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --include \
     --request GET "https://<OpsManagerHost>:<Port>/api/public/v1.0/groups/{PROJECT-ID}/maintenanceWindows"
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

```json
{
  "results" : [ {
    "alertTypeNames" : [ "BACKUP" ],
    "created" : "2015-10-22T15:04:31Z",
    "description" : "new description",
    "endDate" : "2015-10-23T23:30:00Z",
    "groupId" : "{PROJECT-ID}",
    "id" : "5628faffd4c606594adaa3b2",
    "startDate" : "2015-10-23T22:00:00Z",
    "updated" : "2015-10-22T15:04:31Z",
    "links" : []
  }, {
    "alertTypeNames" : [ "AGENT", "BACKUP" ],
    "created" : "2015-10-22T15:40:09Z",
    "endDate" : "2015-10-23T23:30:00Z",
    "groupId" : "{PROJECT-ID}",
    "id" : "56290359d4c606594adaafe8",
    "startDate" : "2015-10-23T22:00:00Z",
    "updated" : "2015-10-22T15:40:09Z",
    "links" : []
  } ],
  "links" : [],
  "totalCount" : 2
}
```
