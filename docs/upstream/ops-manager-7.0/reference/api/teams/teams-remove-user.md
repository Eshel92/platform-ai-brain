<!-- Converted from reference/api/teams/teams-remove-user.txt (reStructuredText). Includes are inlined. -->

# Remove a User from a Team

**Note:**

This endpoint is incompatible with projects using
LDAP Authentication.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Syntax

```none
DELETE /orgs/{ORG-ID}/teams/{TEAM-ID}/users/{USER-ID}
```

### Request Path Parameters

| Path Element | Required/Optional | Description |
|---|---|---|
| `ORG-ID` | Required. | The unique identifier for the organization that contains the team from which you want to remove a MongoDB user. |
| `TEAM-ID` | Required | The unique identifier of the team from which you want to remove a MongoDB user. |
| `USER-ID` | Required | The unique identifier of the MongoDB user that you want to remove from the specified team. |

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
curl -X DELETE -i --digest --user "{username:apiKey}" \
 "https://{OPS-MANAGER-HOST}:{PORT}/api/public/v1.0/orgs/6005bd5780eef53d35e9f743/teams/6bdd139c87d9d630926164bf/users/69g63c0980eef52994dbfdge"
```

## Example Response

This endpoint doesn't return a response body.
