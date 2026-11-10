<!-- Converted from rest-api/info.asciidoc (AsciiDoc). Includes are inlined. -->

## Info API

**New API reference**
For the most up-to-date API details, refer to [Info APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-info).

Provides general information about the installed X-Pack features.

### Request

`GET /_xpack`

### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

### Description

The information provided by this API includes:

* Build Information - including the build number and timestamp.
* License Information - basic information about the currently installed license.
* Features Information - The features that are currently enabled and available
  under the current license.

### Path parameters

`categories`::
  (Optional, list) A comma-separated list of the information categories to
  include in the response. For example, `build,license,features`.

`human`::
  (Optional, Boolean) Defines whether additional human-readable information is
  included in the response. In particular, it adds descriptions and a tag line.
  The default value is `true`.

### Examples

The following example queries the info API:

```console
GET /_xpack
```

Example response:

```console-result
{
   "build" : {
      "hash" : "2798b1a3ce779b3611bb53a0082d4d741e4d3168",
      "date" : "2015-04-07T13:34:42Z"
   },
   "license" : {
      "uid" : "893361dc-9749-4997-93cb-xxx",
      "type" : "trial",
      "mode" : "trial",
      "status" : "active",
      "expiry_date_in_millis" : 1542665112332
   },
   "features" : {
      "ccr" : {
        "available" : true,
        "enabled" : true
      },
     "aggregate_metric" : {
          "available" : true,
          "enabled" : true
      },
      "analytics" : {
          "available" : true,
          "enabled" : true
      },
      "archive" : {
          "available" : true,
          "enabled" : true
      },
      "enrich" : {
          "available" : true,
          "enabled" : true
      },
      "frozen_indices" : {
         "available" : true,
         "enabled" : true
      },
      "graph" : {
         "available" : true,
         "enabled" : true
      },
      "ilm" : {
         "available" : true,
         "enabled" : true
      },
      "logstash" : {
         "available" : true,
         "enabled" : true
      },
      "ml" : {
         "available" : true,
         "enabled" : true
      },
      "esql" : {
         "available" : true,
         "enabled" : true
      },
      "monitoring" : {
         "available" : true,
         "enabled" : true
      },
      "rollup": {
         "available": true,
         "enabled": true
      },
      "searchable_snapshots" : {
         "available" : true,
         "enabled" : true
      },
      "security" : {
         "available" : true,
         "enabled" : true
      },
      "slm" : {
         "available" : true,
         "enabled" : true
      },
      "spatial" : {
         "available" : true,
         "enabled" : true
      },
      "eql" : {
         "available" : true,
         "enabled" : true
      },
      "sql" : {
         "available" : true,
         "enabled" : true
      },
      "transform" : {
         "available" : true,
         "enabled" : true
      },
      "voting_only" : {
         "available" : true,
         "enabled" : true
      },
      "watcher" : {
         "available" : true,
         "enabled" : true
      },
      "data_streams" : {
         "available" : true,
         "enabled" : true
      },
      "data_tiers" : {
         "available" : true,
         "enabled" : true
      },
      "enterprise_search": {
         "available": true,
         "enabled": true
      },
      "universal_profiling": {
         "available": true,
         "enabled": true
      },
      "logsdb": {
        "available": true,
        "enabled": false
      }
   },
   "tagline" : "You know, for X"
}
```

The following example only returns the build and features information:

```console
GET /_xpack?categories=build,features
```

The following example removes the descriptions from the response:

```console
GET /_xpack?human=false
```
