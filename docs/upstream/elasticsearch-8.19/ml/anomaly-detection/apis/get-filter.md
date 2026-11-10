<!-- Converted from ml/anomaly-detection/apis/get-filter.asciidoc (AsciiDoc). Includes are inlined. -->

# Get filters API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Retrieves filters.

## Request

`GET _ml/filters/<filter_id>` +

`GET _ml/filters/`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

You can get a single filter or all filters. For more information, see 
{ml-docs}/ml-ad-run-jobs.html#ml-ad-rules[Custom rules].

## Path parameters

`<filter_id>`::
(Optional, string)
A string that uniquely identifies a filter.

## Query parameters

`from`::
    (Optional, integer) Skips the specified number of filters. Defaults to `0`.

`size`::
    (Optional, integer) Specifies the maximum number of filters to obtain.
    Defaults to `100`.

## Response body

The API returns an array of filter resources, which have the following
properties:
  
`description`::
(string) A description of the filter.

`filter_id`::
(string)
A string that uniquely identifies a filter.
`items`::
(array of strings) An array of strings which is the filter item list.

## Examples

```console
GET _ml/filters/safe_domains
```

The API returns the following results:

```console-result
{
  "count": 1,
  "filters": [
    {
      "filter_id": "safe_domains",
      "description": "A list of safe domains",
      "items": [
        "*.google.com",
        "wikipedia.org"
      ]
    }
  ]
}
```
