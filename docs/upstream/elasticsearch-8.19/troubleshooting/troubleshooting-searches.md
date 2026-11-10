<!-- Converted from troubleshooting/troubleshooting-searches.asciidoc (AsciiDoc). Includes are inlined. -->

## Troubleshooting searches

When you query your data, Elasticsearch may return an error, no search results,
or results in an unexpected order. This guide describes how to troubleshoot
searches.

### Ensure the data stream, index, or alias exists

Elasticsearch returns an `index_not_found_exception` when the data stream, index
or alias you try to query does not exist. This can happen when you misspell the
name or when the data has been indexed to a different data stream or index.

Use the exists API to check whether a data stream, index, or
alias exists:

```console
HEAD my-data-stream
```

Use the data stream stats API to list all data
streams:

```console
GET /_data_stream/_stats?human=true
```

Use the get index API to list all indices and their
aliases:

```console
GET _all?filter_path=*.aliases
```

Instead of an error, it is possible to retrieve partial search results if some
of the indices you're querying are unavailable. Set `ignore_unavailable` to
`true`:

```console
GET /my-alias/_search?ignore_unavailable=true
```

### Ensure the data stream or index contains data

When a search request returns no hits, the data stream or index may contain no
data. This can happen when there is a data ingestion issue. For example, the
data may have been indexed to a data stream or index with another name.

Use the count API to retrieve the number of documents in a data
stream or index. Check that `count` in the response is not 0.

```console
GET /my-index-000001/_count
```

**Note:** When getting no search results in Kibana, check that you have selected the
correct data view and a valid time range. Also, ensure the data view has been
configured with the correct time field.

### Check that the field exists and its capabilities

Querying a field that does not exist will not return any results. Use the
field capabilities API to check whether a field exists:

```console
GET /my-index-000001/_field_caps?fields=my-field
```

If the field does not exist, check the data ingestion process. The field may
have a different name.

If the field exists, the request will return the field's type and whether it is
searchable and aggregatable.

```console-response
{
  "indices": [
    "my-index-000001"
  ],
  "fields": {
    "my-field": {
      "keyword": {
        "type": "keyword",         <1>
        "metadata_field": false,
        "searchable": true,        <2>
        "aggregatable": true       <3>
      }
    }
  }
}
```

<1> The field is of type `keyword` in this index.
<2> The field is searchable in this index.
<3> The field is aggregatable in this index.

### Check the field's mappings

A field's capabilities are determined by its mapping. To retrieve
the mapping, use the get mapping API:

```console
GET /my-index-000001/_mappings
```

If you query a `text` field, pay attention to the analyzer that may have been
configured. You can use the analyze API to check how a
field's analyzer processes values and query terms:

```console
GET /my-index-000001/_analyze
{
  "field" : "my-field",
  "text" : "this is a test"
}
```

To change the mapping of an existing field, refer to
Changing the mapping of a field.

### Check the field's values

Use the `exists` query to check whether there are
documents that return a value for a field. Check that `count` in the response is
not 0.

```console
GET /my-index-000001/_count
{
  "query": {
    "exists": {
      "field": "my-field"
    }
  }
}
```

If the field is aggregatable, you can use aggregations
to check the field's values. For `keyword` fields, you can use a
terms aggregation to retrieve
the field's most common values:

```console
GET /my-index-000001/_search?filter_path=aggregations
{
  "size": 0,
  "aggs": {
    "top_values": {
      "terms": {
        "field": "my-field",
        "size": 10
      }
    }
  }
}
```

For numeric fields, you can use the
stats aggregation to get an
idea of the field's value distribution:

```console
GET my-index-000001/_search?filter_path=aggregations
{
  "aggs": {
    "my-num-field-stats": {
      "stats": {
        "field": "my-num-field"
      }
    }
  }
}
```

If the field does not return any values, check the data ingestion process. The
field may have a different name.

### Check the latest value

For time-series data, confirm there is non-filtered data within the attempted
time range. For example, if you are trying to query the latest data for the
`@timestamp` field, run the following to see if the max `@timestamp` falls
within the attempted range:

```console
GET my-index-000001/_search?sort=@timestamp:desc&size=1
```

### Validate, explain, and profile queries

When a query returns unexpected results, Elasticsearch offers several tools to
investigate why.

The validate API enables you to validate a query. Use the
`rewrite` parameter to return the Lucene query an Elasticsearch query is
rewritten into:

```console
GET /my-index-000001/_validate/query?rewrite=true
{
  "query": {
    "match": {
      "user.id": {
        "query": "kimchy",
        "fuzziness": "auto"
      }
    }
  }
}
```

Use the explain API to find out why a specific document
matches or doesn’t match a query:

```console
GET /my-index-000001/_explain/0
{
  "query" : {
    "match" : { "message" : "elasticsearch" }
  }
}
```

The profile API provides detailed timing information about a
search request. For a visual representation of the results, use the
[Search Profiler](https://www.elastic.co/guide/en/kibana/8.19/xpack-profiler.html) in Kibana.

**Note:** To troubleshoot queries in Kibana, select **Inspect** in the toolbar. Next,
select **Request**. You can now copy the query Kibana sent to Elasticsearch for
further analysis in Console.

### Check index settings

Index settings can influence search results. For
example, the `index.query.default_field` setting, which determines the field
that is queried when a query specifies no explicit field. Use the
get index settings API to retrieve the settings for an
index:

```console
GET /my-index-000001/_settings
```

You can update dynamic index settings with the <<indices-update-settings,update
index settings API>>. <<change-dynamic-index-setting-for-a-data-stream,Changing
dynamic index settings for a data stream>> requires changing the index template
used by the data stream.

For static settings, you need to create a new index with the correct settings.
Next, you can reindex the data into that index. For data streams, refer to
<<change-static-index-setting-for-a-data-stream,Change a static index setting
for a data stream>>.

### Find slow queries

Slow logs can help pinpoint slow performing search 
requests. Enabling audit logging on top can help determine 
query source. Add the following settings to the `elasticsearch.yml` configuration file
to trace queries. The resulting logging is verbose, so disable these settings when not 
troubleshooting.

```yaml
xpack.security.audit.enabled: true
xpack.security.audit.logfile.events.include: _all
xpack.security.audit.logfile.events.emit_request_body: true
```

Refer to
https://www.elastic.co/blog/advanced-tuning-finding-and-fixing-slow-elasticsearch-queries[Advanced
tuning: finding and fixing slow Elasticsearch queries] for more information.
