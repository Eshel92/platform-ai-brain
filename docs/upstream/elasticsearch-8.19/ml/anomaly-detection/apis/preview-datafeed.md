<!-- Converted from ml/anomaly-detection/apis/preview-datafeed.asciidoc (AsciiDoc). Includes are inlined. -->

# Preview datafeeds API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Previews a datafeed.

## Request

`GET _ml/datafeeds/<datafeed_id>/_preview` +

`POST _ml/datafeeds/<datafeed_id>/_preview` +

`GET _ml/datafeeds/_preview` +

`POST _ml/datafeeds/_preview`

## Prerequisites

Requires the following privileges:

* cluster: `manage_ml` (the `machine_learning_admin` built-in role grants this
   privilege)
* source index configured in the datafeed: `read`.

## Description

The preview datafeeds API returns the first "page" of search results from a
datafeed. You can preview an existing datafeed or provide configuration details
for the datafeed and anomaly detection job in the API. The preview shows the structure of
the data that will be passed to the anomaly detection engine.

**Important:** When Elasticsearch security features are enabled, the datafeed query is
previewed using the credentials of the user calling the preview datafeed API.
When the datafeed is started it runs the query using the roles of the last user
to create or update it. If the two sets of roles differ then the preview may
not accurately reflect what the datafeed will return when started. To avoid
such problems, the same user that creates or updates the datafeed should preview
it to ensure it is returning the expected data. Alternatively, use
secondary authorization headers to
supply the credentials.

## Path parameters

`<datafeed_id>`::
(Optional, string)
A numerical character string that uniquely identifies the
datafeed. This identifier can contain lowercase alphanumeric characters (a-z
and 0-9), hyphens, and underscores. It must start and end with alphanumeric
characters.
**Note:** If you provide the `<datafeed_id>` as a path parameter, you cannot
provide datafeed or anomaly detection job configuration details in the request body.

## Query parameters

`end`::
(Optional, string) The time that the datafeed preview should end. The preview may not go to the end of the provided value
as only the first page of results are returned. The time can be specified by using one of the following formats:
* ISO 8601 format with milliseconds, for example `2017-01-22T06:00:00.000Z`
* ISO 8601 format without milliseconds, for example `2017-01-22T06:00:00+00:00`
* Milliseconds since the epoch, for example `1485061200000`

Date-time arguments using either of the ISO 8601 formats must have a time zone
designator, where `Z` is accepted as an abbreviation for UTC time.

**Note:** When a URL is expected (for example, in browsers), the `+` used in time
zone designators must be encoded as `%2B`.

This value is exclusive.

`start`::
(Optional, string) The time that the datafeed preview should begin, which can be
specified by using the same formats as the `end` parameter. This value is
inclusive.

**Note:** If you don't provide either the `start` or `end` parameter, the datafeed preview will search over the entire
time of data but exclude data within `cold` or `frozen` data tiers.

## Request body

`datafeed_config`::
(Optional, object) The datafeed definition to preview. For valid definitions, see
the create datafeeds API.

`job_config`::
(Optional, object) The configuration details for the anomaly detection job that is
associated with the datafeed. If the `datafeed_config` object does not include a
`job_id` that references an existing anomaly detection job, you must supply this
`job_config` object. If you include both a `job_id` and a `job_config`, the
latter information is used. You cannot specify a `job_config` object unless you also supply a `datafeed_config` object. For valid definitions, see the
create anomaly detection jobs API.

## Examples

This is an example of providing the ID of an existing datafeed:

```console
GET _ml/datafeeds/datafeed-high_sum_total_sales/_preview
```

The data that is returned for this example is as follows:

```console-result
[
  {
    "order_date" : 1574294659000,
    "category.keyword" : "Men's Clothing",
    "customer_full_name.keyword" : "Sultan Al Benson",
    "taxful_total_price" : 35.96875
  },
  {
    "order_date" : 1574294918000,
    "category.keyword" : [
      "Women's Accessories",
      "Women's Clothing"
    ],
    "customer_full_name.keyword" : "Pia Webb",
    "taxful_total_price" : 83.0
  },
  {
    "order_date" : 1574295782000,
    "category.keyword" : [
      "Women's Accessories",
      "Women's Shoes"
    ],
    "customer_full_name.keyword" : "Brigitte Graham",
    "taxful_total_price" : 72.0
  }
]
```

The following example provides datafeed and anomaly detection job configuration
details in the API:

```console
POST _ml/datafeeds/_preview
{
  "datafeed_config": {
    "indices" : [
      "kibana_sample_data_ecommerce"
    ],
    "query" : {
      "bool" : {
        "filter" : [
          {
            "term" : {
              "_index" : "kibana_sample_data_ecommerce"
            }
          }
        ]
      }
    },
    "scroll_size" : 1000
  },
  "job_config": {
    "description" : "Find customers spending an unusually high amount in an hour",
    "analysis_config" : {
      "bucket_span" : "1h",
      "detectors" : [
        {
          "detector_description" : "High total sales",
          "function" : "high_sum",
          "field_name" : "taxful_total_price",
          "over_field_name" : "customer_full_name.keyword"
        }
      ],
      "influencers" : [
        "customer_full_name.keyword",
        "category.keyword"
      ]
    },
    "analysis_limits" : {
      "model_memory_limit" : "10mb"
    },
    "data_description" : {
      "time_field" : "order_date",
      "time_format" : "epoch_ms"
    }
  }
}
```

The data that is returned for this example is as follows:

```console-result
[
  {
    "order_date" : 1574294659000,
    "category.keyword" : "Men's Clothing",
    "customer_full_name.keyword" : "Sultan Al Benson",
    "taxful_total_price" : 35.96875
  },
  {
    "order_date" : 1574294918000,
    "category.keyword" : [
      "Women's Accessories",
      "Women's Clothing"
    ],
    "customer_full_name.keyword" : "Pia Webb",
    "taxful_total_price" : 83.0
  },
  {
    "order_date" : 1574295782000,
    "category.keyword" : [
      "Women's Accessories",
      "Women's Shoes"
    ],
    "customer_full_name.keyword" : "Brigitte Graham",
    "taxful_total_price" : 72.0
  }
]
```
