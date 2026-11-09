<!-- Converted from reference/api/groups/remove-one-user-from-one-group.txt (reStructuredText). Includes are inlined. -->

# Remove One User from One Project

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
DELETE /groups/{PROJECT-ID}/users/{USER-ID}
```

## Request Parameters

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| PROJECT-ID | string | *(Required.)* The unique identifier for the project. |
| USER-ID | string | *(Required.)* The unique identifier for the user in **{PROJECT-ID}**. |

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

This endpoint does not have response elements.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
 --include \
 --request DELETE "https://{opsManagerHost}:{port}/api/public/v1.0/groups/{PROJECT-ID}/users/{USER-ID}"
```

## Example Response

This endpoint doesn't return a response body.
