<!-- Converted from ml/common/apis/get-ml-info.asciidoc (AsciiDoc). Includes are inlined. -->

# Get machine learning info API

**New API reference**
For the most up-to-date API details, refer to [Machine learning APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml).

Returns defaults and limits used by machine learning.

## Request

`GET _ml/info`

## Prerequisites

Requires the `monitor_ml` cluster privilege. This privilege is included in the
`machine_learning_user` built-in role.

## Description

This endpoint is designed to be used by a user interface that needs to fully
understand machine learning configurations where some options are not specified,
meaning that the defaults should be used. This endpoint may be used to find out
what those defaults are. It also provides information about the maximum size
of machine learning jobs that could run in the current cluster configuration.

## Examples

The endpoint takes no arguments:

```console
GET _ml/info
```

This is a possible response:

```console-result
{
  "defaults" : {
    "anomaly_detectors" : {
      "categorization_analyzer" : {
        "char_filter" : [
          "first_line_with_letters"
        ],
        "tokenizer" : "ml_standard",
        "filter" : [
          {
            "type" : "stop",
            "stopwords" : [
              "Monday",
              "Tuesday",
              "Wednesday",
              "Thursday",
              "Friday",
              "Saturday",
              "Sunday",
              "Mon",
              "Tue",
              "Wed",
              "Thu",
              "Fri",
              "Sat",
              "Sun",
              "January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December",
              "Jan",
              "Feb",
              "Mar",
              "Apr",
              "May",
              "Jun",
              "Jul",
              "Aug",
              "Sep",
              "Oct",
              "Nov",
              "Dec",
              "GMT",
              "UTC"
            ]
          },
          {
            "type": "limit",
            "max_token_count": "100"
          }
        ]
      },
      "model_memory_limit" : "1gb",
      "categorization_examples_limit" : 4,
      "model_snapshot_retention_days" : 10,
      "daily_model_snapshot_retention_after_days" : 1
    },
    "datafeeds" : {
      "scroll_size" : 1000
    }
  },
  "upgrade_mode": false,
  "native_code" : {
    "version": "7.0.0",
    "build_hash": "99a07c016d5a73"
  },
  "limits" : {
    "effective_max_model_memory_limit": "28961mb",
    "total_ml_memory": "86883mb",
    "total_ml_processors": 16,
    "max_single_ml_node_processors": 16
  }
}
```
