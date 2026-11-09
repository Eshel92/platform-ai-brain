<!-- Converted from reference/api/teams/teams-rename-one.txt (reStructuredText). Includes are inlined. -->

# Rename a Team

**Note:**

This endpoint is incompatible with projects using
LDAP Authentication.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Syntax

```none
PATCH /orgs/{ORG-ID}/teams/{TEAM-ID}
```

### Request Path Parameters

| Path Element | Required/Optional | Description |
|---|---|---|
| `ORG-ID` | Required | The unique identifier for the organization associated with the team that you want to rename. |
| `TEAM-ID` | Required | The unique identifier of the team that you want to rename. |

### Request Query Parameters

The following query parameters are optional:

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

| Path Element | Required/Optional | Description |
|---|---|---|
| `name` | `Required` | The new name of the team. |

## Response

| Name | Type | Description |
|---|---|---|
| `id` | string | The unique identifier for the team. |
| `links` | object array | .. include:: /includes/links-explanation.rst |
| `name` | string | The new name of the team. |

## Example

### Request

```shell
curl -X PATCH --digest --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --header "Content-Type: application/json" \
 "https://cloud.mongodb.com/api/public/v10/orgs/6006bd5780eef53d35e9f74e/teams/6b77131987d9d66ddeb3f907?pretty=true" \
 --data '{"name":"Finance"}'
```

### Response

```json
{
  "id" : "6b77131987d9d66ddeb3f907",
  "links" : [ {
    "href" : "https://cloud.mongodb.com/api/public/v1.0/orgs/6006bd5780eef53d35e9f74e/teams/6b77131987d9d66ddeb3f907",
    "rel" : "self"
  } ],
  "name" : "Finance"
}
```
