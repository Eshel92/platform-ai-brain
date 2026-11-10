<!-- Converted from mapping/fields/source-field.asciidoc (AsciiDoc). Includes are inlined. -->

### `_source` field

The `_source` field contains the original JSON document body that was passed
at index time. The `_source` field itself is not indexed (and thus is not
searchable), but it is stored so that it can be returned when executing
_fetch_ requests, like get or search.

If disk usage is important to you, then consider the following options:

- Using synthetic `_source`, which reconstructs source content at the time of retrieval instead of storing it on disk. This shrinks disk usage, at the cost of slower access to `_source` in Get and Search queries.
- Disabling the `_source` field completely. This shrinks disk
usage but disables features that rely on `_source`.

(See `mapping/fields/synthetic-source.md`)

#### Disabling the `_source` field

Though very handy to have around, the source field does incur storage overhead
within the index. For this reason, it can be disabled as follows:

```console
PUT my-index-000001
{
  "mappings": {
    "_source": {
      "enabled": false
    }
  }
}
```

**Think before disabling the `_source` field**
==================================================

Users often disable the `_source` field without thinking about the
consequences, and then live to regret it. If the `_source` field isn't
available then a number of features are not supported:

* The `update`, `update_by_query`,
and `reindex` APIs.

* In the Kibana [Discover](https://www.elastic.co/guide/en/kibana/8.19/discover.html) application, field data will not be displayed.

* On the fly highlighting.

* The ability to reindex from one Elasticsearch index to another, either
  to change mappings or analysis, or to upgrade an index to a new major
  version.

* The ability to debug queries or aggregations by viewing the original
  document used at index time.

* Potentially in the future, the ability to repair index corruption
  automatically.
==================================================

**Note:** You can't disable the `_source` field for indexes with `index_mode` 
set to `logsdb` or `time_series`.

**Tip:** If disk space is a concern, rather increase the
compression level instead of disabling the `_source`.

#### Including / Excluding fields from `_source`

An expert-only feature is the ability to prune the contents of the `_source`
field after the document has been indexed, but before the `_source` field is
stored.

**Warning:** Removing fields from the `_source` has similar downsides to disabling
`_source`, especially the fact that you cannot reindex documents from one
Elasticsearch index to another. Consider using
source filtering instead.

The `includes`/`excludes` parameters (which also accept wildcards) can be used
as follows:

```console
PUT logs
{
  "mappings": {
    "_source": {
      "includes": [
        "*.count",
        "meta.*"
      ],
      "excludes": [
        "meta.description",
        "meta.other.*"
      ]
    }
  }
}

PUT logs/_doc/1
{
  "requests": {
    "count": 10,
    "foo": "bar" <1>
  },
  "meta": {
    "name": "Some metric",
    "description": "Some metric description", <1>
    "other": {
      "foo": "one", <1>
      "baz": "two" <1>
    }
  }
}

GET logs/_search
{
  "query": {
    "match": {
      "meta.other.foo": "one" <2>
    }
  }
}
```

<1> These fields will be removed from the stored `_source` field.
<2> We can still search on this field, even though it is not in the stored `_source`.
