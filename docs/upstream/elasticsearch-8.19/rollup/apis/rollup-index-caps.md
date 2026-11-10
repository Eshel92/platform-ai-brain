<!-- Converted from rollup/apis/rollup-index-caps.asciidoc (AsciiDoc). Includes are inlined. -->

### Get rollup index capabilities API

deprecated::[8.11.0,"Rollups will be removed in a future version. Use downsampling instead."]

**New API reference**
For the most up-to-date API details, refer to [Rollup APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-rollup).

Returns the rollup capabilities of all jobs inside of a rollup index (e.g. the
index where rollup data is stored).

#### Request

`GET <target>/_rollup/data`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have any of the `read`,
`view_index_metadata`, or `manage` index privilege
on the index that stores the rollup results. For more information, see
security-privileges.

#### Description

A single rollup index may store the data for multiple {rollup-jobs}, and may
have a variety of capabilities depending on those jobs.

This API will allow you to determine:

1. What jobs are stored in an index (or indices specified via a pattern)?
2. What target indices were rolled up, what fields were used in those rollups
and what aggregations can be performed on each job?

#### Path parameters

`<target>`::
(Required, string) Data stream or index to check for rollup capabilities.
Wildcard (`*`) expressions are supported.

#### Examples

Imagine we have an index named `sensor-1` full of raw data. We know that the
data will grow over time, so there will be a `sensor-2`, `sensor-3`, etc.
Let's create a {rollup-job} that stores its data in `sensor_rollup`:

```console
PUT _rollup/job/sensor
{
  "index_pattern": "sensor-*",
  "rollup_index": "sensor_rollup",
  "cron": "*/30 * * * * ?",
  "page_size": 1000,
  "groups": {
    "date_histogram": {
      "field": "timestamp",
      "fixed_interval": "1h",
      "delay": "7d"
    },
    "terms": {
      "fields": [ "node" ]
    }
  },
  "metrics": [
    {
      "field": "temperature",
      "metrics": [ "min", "max", "sum" ]
    },
    {
      "field": "voltage",
      "metrics": [ "avg" ]
    }
  ]
}
```

If at a later date, we'd like to determine what jobs and capabilities were
stored in the `sensor_rollup` index, we can use the get rollup index API:

```console
GET /sensor_rollup/_rollup/data
```

Note how we are requesting the concrete rollup index name (`sensor_rollup`) as
the first part of the URL. This will yield the following response:

```console-result
{
  "sensor_rollup" : {
    "rollup_jobs" : [
      {
        "job_id" : "sensor",
        "rollup_index" : "sensor_rollup",
        "index_pattern" : "sensor-*",
        "fields" : {
          "node" : [
            {
              "agg" : "terms"
            }
          ],
          "temperature" : [
            {
              "agg" : "min"
            },
            {
              "agg" : "max"
            },
            {
              "agg" : "sum"
            }
          ],
          "timestamp" : [
            {
              "agg" : "date_histogram",
              "time_zone" : "UTC",
              "fixed_interval" : "1h",
              "delay": "7d"
            }
          ],
          "voltage" : [
            {
              "agg" : "avg"
            }
          ]
        }
      }
    ]
  }
}
```

The response that is returned contains information that is similar to the
original rollup configuration, but formatted differently. First, there are some
house-keeping details: the {rollup-job} ID, the index that holds the rolled data,
the index pattern that the job was targeting.

Next it shows a list of fields that contain data eligible for rollup searches.
Here we see four fields: `node`, `temperature`, `timestamp` and `voltage`. Each
of these fields list the aggregations that are possible. For example, you can
use a min, max, or sum aggregation on the `temperature` field, but only a
`date_histogram` on `timestamp`.

Note that the `rollup_jobs` element is an array; there can be multiple,
independent jobs configured for a single index or index pattern. Each of these
jobs may have different configurations, so the API returns a list of all the
various configurations available.

Like other APIs that interact with indices, you can specify index patterns
instead of explicit indices:

```console
GET /*_rollup/_rollup/data
```
