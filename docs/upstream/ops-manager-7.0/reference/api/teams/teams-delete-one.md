<!-- Converted from reference/api/teams/teams-delete-one.txt (reStructuredText). Includes are inlined. -->

# Delete One Team

**Note:**

This endpoint is incompatible with projects using
LDAP Authentication.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Syntax

```none
DELETE /orgs/{ORG-ID}/teams/{TEAM-ID}
```

### Request Path Parameters

| Path Element | Required/Optional | Description |
|---|---|---|
| `ORG-ID` | Required. | The unique identifier for the organization associated with the team. |
| `TEAM-ID` | Required | The unique identifier of the team you want to delete. |

       

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

This endpoint doesn't use HTTP request body parameters.

## Response

This endpoint doesn't return a response body.

## Example Request

```sh
 :copyable:

curl --user "{username:apiKey}"" --digest -i \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --request DELETE \
  "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/orgs/{ORG-ID}/teams/{TEAM-ID}?pretty=true"
```

## Example Response

This endpoint doesn't return a response body.
