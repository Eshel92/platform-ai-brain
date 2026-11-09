<!-- Converted from reference/api/api-keys/org/delete-one-org-api-key-access-list.txt (reStructuredText). Includes are inlined. -->

# Delete One Access List Entry for an API Key

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

Delete a specified address on the access list from the specified
API Key.

## Resource

```http
DELETE /orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList/{ACCESS-LIST-ENTRY}
```

### Request Path Parameters

| Name | Type | Description |
|---|---|---|
| `ORG-ID` | string | Unique identifier for the organization to which the target API (Application Programming Interface) key belongs. Request the /orgs endpoint to retrieve all organizations to which the authenticated user has access. |
| `API-KEY-ID` | string | Unique identifier for the API (Application Programming Interface) key for which you want to retrieve access list entries. Request the /orgs/{ORG-ID}/apiKeys endpoint to retrieve all API (Application Programming Interface) keys for the specified organization to which the authenticated user has access. |
| `ACCESS-LIST-ENTRY` | string | The IP or CIDR (Classless Inter-Domain Routing) address. If the entry includes a subnet mask, such as `192.0.2.0/24`, use the URL-encoded value `%2F` for the forward slash `/`. |

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

This endpoint returns an empty JSON document.

## Example Request

```sh
curl --user "{USERNAME}:{APIKEY}" --digest \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --request DELETE "https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/orgs/{ORG-ID}/apiKeys/{API-KEY-ID}/accessList/192.0.2.0%2F24"
```

## Example Response

```json
HTTP/1.1 204 No Content
```
