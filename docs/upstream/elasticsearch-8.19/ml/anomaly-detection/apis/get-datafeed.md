<!-- Converted from ml/anomaly-detection/apis/get-datafeed.asciidoc (AsciiDoc). Includes are inlined. -->

# Get datafeeds API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Retrieves configuration information for datafeeds.

## Request

`GET _ml/datafeeds/<feed_id>` +

`GET _ml/datafeeds/<feed_id>,<feed_id>` +

`GET _ml/datafeeds/` +

`GET _ml/datafeeds/_all`

## Prerequisites

Requires the `monitor_ml` cluster privilege. This privilege is included in the 
`machine_learning_user` built-in role.

## Description

**Important:** This API returns a maximum of 10,000 datafeeds.

## Path parameters

`<feed_id>`::
(Optional, string)
Identifier for the datafeed. It can be a datafeed identifier or a wildcard
expression.
You can get information for multiple datafeeds in a single API request by using a
comma-separated list of datafeeds or a wildcard expression. You can get
information for all datafeeds by using `_all`, by specifying `*` as the
datafeed identifier, or by omitting the identifier.

## Query parameters

`allow_no_match`::
(Optional, Boolean)
Specifies what to do when the request:
* Contains wildcard expressions and there are no datafeeds that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty `datafeeds` array when
there are no matches and the subset of results when there are partial matches.
If this parameter is `false`, the request returns a `404` status code when there
are no matches or only partial matches.
`exclude_generated`::
(Optional, Boolean)
Indicates if certain fields should be removed from the configuration on
retrieval. This allows the configuration to be in an acceptable format to be retrieved
and then added to another cluster. Default is false.

## Response body

The API returns an array of datafeed resources. For the full list of properties,
see create datafeeds API.

## Response codes

`404` (Missing resources)::
  If `allow_no_match` is `false`, this code indicates that there are no
  resources that match the request or only partial matches for the request.

## Examples

```console
GET _ml/datafeeds/datafeed-high_sum_total_sales
```

The API returns the following results:

```console-result
{
  "count" : 1,
  "datafeeds" : [
    {
      "datafeed_id" : "datafeed-high_sum_total_sales",
      "job_id" : "high_sum_total_sales",
      "authorization" : {
        "roles" : [
          "superuser"
        ]
      },
      "query_delay" : "93169ms",
      "chunking_config" : {
        "mode" : "auto"
      },
      "indices_options" : {
        "expand_wildcards" : [
          "open"
        ],
        "ignore_unavailable" : false,
        "allow_no_indices" : true,
        "ignore_throttled" : true
      },
      "query" : {
        "bool" : {
          "filter" : [
            {
              "term" : {
                "event.dataset" : "sample_ecommerce"
              }
            }
          ]
        }
      },
      "indices" : [
        "kibana_sample_data_ecommerce"
      ],
      "scroll_size" : 1000,
      "delayed_data_check_config" : {
        "enabled" : true
      }
    }
  ]
}
```
