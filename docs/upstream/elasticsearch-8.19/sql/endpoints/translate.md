<!-- Converted from sql/endpoints/translate.asciidoc (AsciiDoc). Includes are inlined. -->

## SQL Translate API

The SQL Translate API accepts SQL in a JSON document and translates it
into native Elasticsearch queries. For example:

```console
POST /_sql/translate
{
  "query": "SELECT * FROM library ORDER BY page_count DESC",
  "fetch_size": 10
}
```

Which returns:

```console-result
{
  "size": 10,
  "_source": false,
  "fields": [
    {
      "field": "author"
    },
    {
      "field": "name"
    },
    {
      "field": "page_count"
    },
    {
      "field": "release_date",
      "format": "strict_date_optional_time_nanos"
    }
  ],
  "sort": [
    {
      "page_count": {
        "order": "desc",
        "missing": "_first",
        "unmapped_type": "short"
      }
    }
  ],
  "track_total_hits": -1
}
```

Which is the request that SQL will run to provide the results.
In this case, SQL will use the scroll
API. If the result contained an aggregation then SQL would use
the normal search API.

The request body accepts the same parameters as
the SQL search API, excluding `cursor`.
