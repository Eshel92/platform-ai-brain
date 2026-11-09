<!-- Converted from reference/api/agents-get-by-type.txt (reStructuredText). Includes are inlined. -->

# Get Agents by Type for One Project

Get all agents of a specified type (i.e. Monitoring, Backup, or
Automation) for a project.

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
GET /groups/{PROJECT-ID}/agents/{TYPE}
```

### Request Path Parameters

* - Name
  - Type
  - Description

* - PROJECT-ID
  - string
  - Unique identifier of the `project` that owns the
    Agent API Key.

* - TYPE
  - string
  - The agent type to retrieve. **TYPE** can be one of the
    following values:

    - `MONITORING`
    - `BACKUP`
    - `AUTOMATION`

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

* - Name
  - Type
  - Description

* - `typeName`
  - string
  - The type of agent: `MONITORING`, `BACKUP`, or `AUTOMATION`.

* - `hostname`
  - string
  - Primary hostname. A host typically may have aliases, so the primary
    is the best available name as decided by Ops Manager.

* - `confCount`
  - number
  - Number of configuration calls.

* - `lastConf`
  - timestamp
  - Date and time of last configuration call.

* - `stateName`
  - string
  - The current state of the agent. `stateName` can return the following
    values:

    - `ACTIVE`: the agent is active and operating
    - `STANDBY`: the agent is on standby
    - `NO_PROCESSES`: the agent is not managing,
      monitoring, or backing up any processes.

* - `pingCount`
  - number
  - **Only applicable to Monitoring Agents**. The number of pings that
    the Monitoring Agent has sent to the `hostname` URL.

* - `isManaged`
  - Boolean

  - **Only applicable to Monitoring and Backup Agents**. Specifies
    whether or not Ops Manager manages the agent.

* - `lastPing`
  - timestamp
  - **Only applicable to Monitoring Agents**. Time of most recent
    ping.

* - `tag`
  - string
  - **Only applicable to Backup Agents**. The agent's tag, if there is one.

## Example Request

Get All Monitoring Agents for One Project.

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --header "Accept: application/json" \
 --include \
 --request GET "https://<ops-manager-host>/api/public/v1.0/groups/{PROJECT-ID}/agents/MONITORING"
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
  "links" : [],
  "results": [
    {
      "confCount": 59,
      "hostname": "example",
      "isManaged": true,
      "lastConf": "2015-06-18T14:21:42Z",
      "lastPing": "2015-06-18T14:21:42Z",
      "pingCount": 6,
      "stateName": "ACTIVE",
      "typeName": "MONITORING"
    }
  ],
  "totalCount": 1
}
```
