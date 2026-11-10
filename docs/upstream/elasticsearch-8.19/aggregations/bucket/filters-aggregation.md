<!-- Converted from aggregations/bucket/filters-aggregation.asciidoc (AsciiDoc). Includes are inlined. -->

### Filters aggregation

A multi-bucket aggregation where each bucket contains the documents
that match a query.

Example:

```console
PUT /logs/_bulk?refresh
{ "index" : { "_id" : 1 } }
{ "body" : "warning: page could not be rendered" }
{ "index" : { "_id" : 2 } }
{ "body" : "authentication error" }
{ "index" : { "_id" : 3 } }
{ "body" : "warning: connection timed out" }

GET logs/_search
{
  "size": 0,
  "aggs" : {
    "messages" : {
      "filters" : {
        "filters" : {
          "errors" :   { "match" : { "body" : "error"   }},
          "warnings" : { "match" : { "body" : "warning" }}
        }
      }
    }
  }
}
```

In the above example, we analyze log messages. The aggregation will build two
collection (buckets) of log messages - one for all those containing an error,
and another for all those containing a warning.

Response:

```console-result
{
  "took": 9,
  "timed_out": false,
  "_shards": ...,
  "hits": ...,
  "aggregations": {
    "messages": {
      "buckets": {
        "errors": {
          "doc_count": 1
        },
        "warnings": {
          "doc_count": 2
        }
      }
    }
  }
}
```

#### Anonymous filters

The filters field can also be provided as an array of filters, as in the
following request:

```console
GET logs/_search
{
  "size": 0,
  "aggs" : {
    "messages" : {
      "filters" : {
        "filters" : [
          { "match" : { "body" : "error"   }},
          { "match" : { "body" : "warning" }}
        ]
      }
    }
  }
}
```

The filtered buckets are returned in the same order as provided in the
request. The response for this example would be:

```console-result
{
  "took": 4,
  "timed_out": false,
  "_shards": ...,
  "hits": ...,
  "aggregations": {
    "messages": {
      "buckets": [
        {
          "doc_count": 1
        },
        {
          "doc_count": 2
        }
      ]
    }
  }
}
```

#### `Other` Bucket

The `other_bucket` parameter can be set to add a bucket to the response which will contain all documents that do 
not match any of the given filters. The value of this parameter can be as follows:

`false`::         Does not compute the `other` bucket
`true`::          Returns the `other` bucket either in a bucket (named `_other_` by default) if named filters are being used, 
                  or as the last bucket if anonymous filters are being used

The `other_bucket_key` parameter can be used to set the key for the `other` bucket to a value other than the default `_other_`. Setting 
this parameter will implicitly set the `other_bucket` parameter to `true`.

The following snippet shows a response where the `other` bucket is requested to be named `other_messages`.

```console
PUT logs/_doc/4?refresh
{
  "body": "info: user Bob logged out"
}

GET logs/_search
{
  "size": 0,
  "aggs" : {
    "messages" : {
      "filters" : {
        "other_bucket_key": "other_messages",
        "filters" : {
          "errors" :   { "match" : { "body" : "error"   }},
          "warnings" : { "match" : { "body" : "warning" }}
        }
      }
    }
  }
}
```

The response would be something like the following:

```console-result
{
  "took": 3,
  "timed_out": false,
  "_shards": ...,
  "hits": ...,
  "aggregations": {
    "messages": {
      "buckets": {
        "errors": {
          "doc_count": 1
        },
        "warnings": {
          "doc_count": 2
        },
        "other_messages": {
          "doc_count": 1
        }
      }
    }
  }
}
```

#### Non-keyed Response

By default, the named filters aggregation returns the buckets as an object. But in some sorting cases, such as
bucket sort, the JSON doesn't guarantee the order of elements
in the object. You can use the `keyed` parameter to specify the buckets as an array of objects. The value of this
parameter can be as follows:

`true`::        (Default) Returns the buckets as an object
`false`::       Returns the buckets as an array of objects

**Note:** This parameter is ignored by Anonymous filters.

Example:

```console
POST /sales/_search?size=0&filter_path=aggregations
{
  "aggs": {
    "the_filter": {
      "filters": {
        "keyed": false,
        "filters": {
          "t-shirt": { "term": { "type": "t-shirt" } },
          "hat": { "term": { "type": "hat" } }
        }
      },
      "aggs": {
        "avg_price": { "avg": { "field": "price" } },
        "sort_by_avg_price": {
          "bucket_sort": { "sort": { "avg_price": "asc" } }
        }
      }
    }
  }
}
```

Response:

```console-result
{
  "aggregations": {
    "the_filter": {
      "buckets": [
        {
          "key": "t-shirt",
          "doc_count": 3,
          "avg_price": { "value": 128.33333333333334 }
        },
        {
          "key": "hat",
          "doc_count": 3,
          "avg_price": { "value": 150.0 }
        }
      ]
    }
  }
}
```
