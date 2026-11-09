<!-- Converted from reference/api/agents/get-agent-versions-per-project.txt (reStructuredText). Includes are inlined. -->

# Retrieve All Agent Versions for One Project

## Required Roles

You can successfully call this endpoint with any of the following
assigned roles:

- `Project Read Only`

## Request

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

```http
GET /groups/{PROJECT-ID}/agents/versions
```

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| `PROJECT-ID` | string | Required | Unique identifier of the project. |

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

* - Name
  - Type
  - Description

* - `count`
  - integer
  - Number of Agents that your Ops Manager Application has found.

* - `entries`
  - array of objects
  - Details on each Agent on every host that this Ops Manager Application
    manages.

* - | `entries`
    | `.address`
  - string
  - IPv6 address for the host that runs this Agent.

* - | `entries`
    | `.hostname`
  - string
  - FQDN (fully qualified domain name) of the host that runs this Agent.

* - | `entries`
    | `.hostnameShort`
  - string
  - Hostname that runs this Agent.

* - | `entries`
    | `.version`
  - string
  - Version of this Agent that this host runs.

* - | `entries`
    | `.pingCount`
  - integer
  - Count of pings received from this Agent.

* - | `entries`
    | `.confCount`
  - integer
  - Count of configuration calls received from this Agent.

* - | `entries`
    | `.tagName`
  - string
  - Label for this Agent if backup is enabled.

* - | `entries`
    | `.lastPing`
  - number
  - Timestamp in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time?oldid=828172017) when Ops Manager received the last ping from this
    Agent.

    Applies to Monitoring Agents and MongoDB Agents with Monitoring
    enabled.

* - | `entries`
    | `.lastConf`
  - number
  - Timestamp in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time?oldid=828172017) when Ops Manager received the last configuration
    call from this Agent.

* - | `entries`
    | `.msSinceLastConf`
  - number
  - Number of milliseconds that have passed since the last
    configuration call.

* - | `entries`
    | `.isPrimary`
  - boolean
  - Flag that indicates if the host on which this Agent runs is the
    primary.

* - | `entries`
    | `.isManaged`
  - boolean
  - Flag that indicates if Ops Manager manages this Agent.

    Applies to Monitoring and Backup Agents only.

* - | `entries`
    | `.numProcess`
  - integer
  - Number of MongoDB process that run on this host.

* - | `entries`
    | `.isVersionOld`
  - boolean
  - Flag that indicates the installed Agent is outdated. The current
    released version of this Agent exceeds the version of the
    installed Agent.

* - | `entries`
    | `.isVersionDeprecated`
  - boolean
  - Flag that indicates this Agent is deprecated. The minimum
    supported version of this Agent exceeds the version of the
    installed Agent.

* - | `entries`
    | `.pingState`
  - string
  - Current state of this Agent. `pingName` returns one of the
    following values:

    - `ok`
    - `warning`
    - `error`

* - | `entries`
    | `.isModule`
  - boolean
  - Flag that indicates this entry is a module of the MongoDB Agent.

* - `isAnyAgentNotManaged`
  - boolean
  - Flag indicating if any Agent runs on a host in an unmanaged
    state.

* - `isAnyAgentVersionDeprecated`
  - boolean
  - Flag indicating if any Agent in any deployment runs a deprecated
    version of that Agent.

* - `isAnyAgentVersionOld`
  - boolean
  - Flag indicating if any Agent in any deployment runs a not
    current version of that Agent.

* - `latestVersion`
  - string
  - Latest version of this type of Agent.

* - `links`
  - array of objects
  - .. include:: /includes/api/links-explanation.rst

* - `minimumAgentVersionDetected`
  - string
  - Minimum supported version of this Agent installed on this host.

* - `minimumVersion`
  - string
  - Minimum supported version of this Agent that works with your
    Ops Manager installation.

## Example Request

```sh
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
     --request GET "http://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/agents/versions?pretty=true"
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
  "count": 0,
  "entries": [],
  "isAnyAgentNotManaged": false,
  "isAnyAgentVersionDeprecated": false,
  "isAnyAgentVersionOld": false,
  "latestVersion": "10.14.0.6304",
  "links": [{
      "href": "http://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/agents/current",
      "rel": "self"
    },
    {
      "href": "http://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}",
      "rel": "http://mms.mongodb.com/group"
    }
  ],
  "minimumAgentVersionDetected": "10.14.0.6304",
  "minimumVersion": "5.0.0.309"
}
```
