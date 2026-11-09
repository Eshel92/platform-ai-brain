<!-- Converted from reference/api/third-party-integration-settings-discovery.txt (reStructuredText). Includes are inlined. -->

# Return the Latest Targets for Prometheus

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/prometheus/v1.0/`

## Syntax

```http
GET /groups/{GROUP-ID}/discovery
```

### Request Path Parameters

| Name | Type | Necessity | Description |
|---|---|---|---|
| {PROJECT-ID} | string | Required | Unique 24-hexadecimal digit string that identifies your project. |

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

## Response Elements

The response includes an array of your latest targets from
which to scrape and a document containing their labels.

| Name | Type | Description |
|---|---|---|
| targets | array | Each `host` and `port` from which to scrape metrics. |
| labels | document | Document that contains the label and value that differentiates your metrics. |
| labels.group_id | string | Unique hexadecimal digit string that identifies the project. |
| labels.group_name | string | Human-readable label that identifies the project. |
| labels.org_id | string | Unique hexadecimal digit string that identifies the organization. |

## Example Request

```sh
# Sets the `Authorization` header on every scrape request with the
# configured username and password.
# The URL that Prometheus fetches the targets from. 

curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --include \
     --request GET "https://cloud.mongodb.com/prometheus/v1.0/groups/{PROJECT-ID}/discovery" 
```

## Example Response

```json
[
  {
      "targets":[
        "mongodbd-prometheus:9216"
      ],
      "labels":{
        "group_id":"{PROJECT-ID}",
        "group_name":"CM-Testing",
        "org_id":"{ORG-ID}"
      }
  }
]
```
