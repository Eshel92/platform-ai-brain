<!-- Converted from reference/api/agents-get-all.txt (reStructuredText). Includes are inlined. -->

# Get Links to Agent Resources for a Project

Get links to Monitoring, Backup, and Automation Agent resources for a project.

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/agents
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| PROJECT-ID | string | Unique identifier of the `project` that owns the Agent API Key. |

### Request Query Parameters

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

| Relation | Description |
|---|---|
| self | Me |
| `http://mms.mongodb.com/group` | The project the agents belong to |
| `http://mms.mongodb.com/monitoringAgents` | Links to all Monitoring Agents. |
| `http://mms.mongodb.com/backupAgents` | Links to all Backup Agents. |
| `http://mms.mongodb.com/automationAgents` | Links to all Automation Agents. |

## Example

### Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
 --header 'Accept: application/json' \
 --include \
 --request GET "https://<ops-manager-host>/api/public/v1.0/groups/{PROJECT-ID}/agents"
```

### Response

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
  "links":[
    {
      "href":"https://cloud.mongodb.com/api/public/v1.0/groups/{PROJECT-ID}/agents",
      "rel":"self"
    },
    {
      "href":"https://cloud.mongodb.com/api/public/v1.0/groups/{PROJECT-ID}",
      "rel":"http://mms.mongodb.com/group"
    },
    {
      "href":"https://cloud.mongodb.com/api/public/v1.0/groups/{PROJECT-ID}/agents/MONITORING",
      "rel":"http://mms.mongodb.com/monitoringAgents"
    },
    {
      "href":"https://cloud.mongodb.com/api/public/v1.0/groups/{PROJECT-ID}/agents/BACKUP",
      "rel":"http://mms.mongodb.com/backupAgents"
    },
    {
      "href":"https://cloud.mongodb.com/api/public/v1.0/groups/{PROJECT-ID}/agents/AUTOMATION",
      "rel":"http://mms.mongodb.com/automationAgents"
    }
  ]
}
```
