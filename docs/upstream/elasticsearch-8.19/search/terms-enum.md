<!-- Converted from search/terms-enum.asciidoc (AsciiDoc). Includes are inlined. -->

### Terms enum API

**New API reference**
For the most up-to-date API details, refer to [Search APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search).

The terms enum API can be used to discover terms in the index that match
a partial string. Supported field types are `keyword`,
`constant_keyword`, `flattened`,
`version` and `ip`. This is used for auto-complete:

```console
POST stackoverflow/_terms_enum
{
    "field" : "tags",
    "string" : "kiba"
}
```

The API returns the following response:

```console-result
{
  "_shards": {
    "total": 1,
    "successful": 1,
    "failed": 0
  },
  "terms": [
    "kibana"
  ],
  "complete" : true
}
```

If the `complete` flag is `false`, the returned `terms` set may be incomplete
and should be treated as approximate. This can occur due to a few reasons, such
as a request timeout or a node error.

**Note:** The terms enum API may return terms from deleted documents. Deleted
documents are initially only marked as deleted. It is not until their segments
are merged that documents are actually deleted. Until
that happens, the terms enum API will return terms from these documents.

#### Request

`GET /<target>/_terms_enum`

#### Description

The terms_enum API  can be used to discover terms in the index that begin with the provided
string. It is designed for low-latency look-ups used in auto-complete scenarios.

#### Path parameters

`<target>`::
(Required, string) Comma-separated list of data streams, indices, and aliases
to search. Supports wildcards (`*`). To search all data streams or indices, omit
this parameter or use `*` or `_all`.

#### Request body

`field`::
(Mandatory, string)
Which field to match

`string`::
(Optional, string)
The string to match at the start of indexed terms. If not provided, all terms in the field
are considered.

**Note:** The prefix string cannot be larger than the larges possible keyword value, which is
Lucene's term byte-length limit of `32766`

`size`::
(Optional, integer)
How many matching terms to return. Defaults to 10

`timeout`::
(Optional, time value)
The maximum length of time to spend collecting results. Defaults to "1s" (one second).
If the timeout is exceeded the `complete` flag set to false in the response and the results may
be partial or empty.

`case_insensitive`::
(Optional, boolean)
When true the provided search string is matched against index terms without case sensitivity.
Defaults to false.

`index_filter`::
(Optional,  query object Allows to filter an index shard if the provided
query rewrites to `match_none`.

`search_after`::
(Optional, string)
The string after which terms in the index should be returned. Allows for a form of
pagination if the last result from one request is passed as the `search_after`
parameter for a subsequent request.
