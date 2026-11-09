<!-- Converted from reference/api/third-party-integration-settings-delete.txt (reStructuredText). Includes are inlined. -->

# Delete a Configuration for a Third-Party Service Integration

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Syntax

```http
DELETE /groups/{GROUP-ID}/integrations/{INTEGRATION-TYPE}
```

### Request Path Parameters

* - Parameter
  - Necessity
  - Description

* - `{PROJECT-ID}`
  - Required
  - Project identifier.

* - `{INTEGRATION-TYPE}`
  - Required
  - Third-party service identifier. Accepted
    values are:

    - `DATADOG`
    - `HIP_CHAT`
    - `PAGER_DUTY`
    - `SLACK`
    - `NEW_RELIC`
    - `OPS_GENIE`
    - `VICTOR_OPS`
    - `WEBHOOK`

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

## Response Elements

This endpoint does not have response elements.

## Example Request

```sh
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request DELETE "https://cloud.mongodb.com/api/public/v1.0/groups/{PROJECT-ID}/integrations/PAGER_DUTY"
```

## Example Response

This endpoint doesn't return a response body.
