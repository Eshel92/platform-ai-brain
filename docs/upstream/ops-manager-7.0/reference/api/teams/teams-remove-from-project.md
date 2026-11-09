<!-- Converted from reference/api/teams/teams-remove-from-project.txt (reStructuredText). Includes are inlined. -->

# Remove One Team From One Project

**Note:**

This endpoint is incompatible with projects using
LDAP Authentication.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Syntax

```none
DELETE /groups/{PROJECT-ID}/teams/{TEAM-ID}
```

### Request Path Parameters

| Path Element | Required/Optional | Description |
|---|---|---|
| `PROJECT-ID` | Required | The unique identifier of the group from which you want to remove a team. |
| `TEAM-ID` | Required | The unique identifier of the team that you want to remove from the specified project. |

### Request Query Parameters

The following query parameters are optional:

* - Name
  - Type
  - Description
  - Default

* - pageNum
  - integer
  - Page number (1-index based).
  - `1`

* - itemsPerPage
  - integer
  - Number of items to return per page, up to a maximum of 500.
  - `100`

* - pretty
  - boolean
  - Indicates whether the response body should be in a
    prettyprint format.
  - `false`

* - envelope
  - boolean
  - Indicates whether or not to wrap the response in an envelope.

    Some API (Application Programming Interface) clients cannot access the HTTP (Hypertext Transfer Protocol) response headers or
    status code. To remediate this, set `"envelope" : true` in the
    query.

    For endpoints that return one result, response body
    includes:

    | status | HTTP (Hypertext Transfer Protocol) response code |
    |---|---|
    | envelope | Expected response body |

    For endpoints that return a list of results, the `results`
    object is an envelope. Ops Manager adds the `status` field to the
    response body.
  - None

### Request Body Parameters

This endpoint doesn't use HTTP request body parameters.

## Response

This endpoint does not return a response body.

## Example Request

```sh
curl -X DELETE --digest --user "{PUBLIC-KEY}:{PRIVATE-KEY}" \
 "https://cloud.mongodb.com/api/public/v1.0/groups/{PROJECT-ID}/teams/5a4c0c7887d9d672cf86df58"
```

## Example Response

```none
{}
```
