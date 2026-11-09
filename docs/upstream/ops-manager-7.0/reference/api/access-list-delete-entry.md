<!-- Converted from reference/api/access-list-delete-entry.txt (reStructuredText). Includes are inlined. -->

# Delete One Entry from One Access List

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Resource

```http
DELETE /users/{USER-ID}/accessList/{ACCESS-LIST-ENTRY}
```

**Note:**

You cannot remove your current IP address from the access list.

### Request Path Parameters

| Parameter | Type | Description |
|---|---|---|
| USER-ID | string | *(Required.)* Unique identifier of the current user. To retrieve the ID of the current user, see Get All Users in One Project. |
| `ACCESS-LIST-ENTRY` | string | The IP or CIDR (Classless Inter-Domain Routing) address. If the entry includes a subnet mask, such as `192.0.2.0/24`, use the URL-encoded value `%2F` for the forward slash `/`. |

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
curl --user '{PUBLIC-KEY}:{PRIVATE-KEY}' --digest \
 --include \
 --request DELETE "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/users/{USER-ID}/accessList/192.0.2.0%2F24"
```

## Example Response

This endpoint doesn't return a response body.
