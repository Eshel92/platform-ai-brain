<!-- Converted from search/explain.asciidoc (AsciiDoc). Includes are inlined. -->

### Explain API

**New API reference**
For the most up-to-date API details, refer to [Search APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search).

Returns information about why a specific document matches (or doesn't match) a 
query.

```console
GET /my-index-000001/_explain/0
{
  "query" : {
    "match" : { "message" : "elasticsearch" }
  }
}
```

#### Request

`GET /<index>/_explain/<id>`

`POST /<index>/_explain/<id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for the target index.

#### Description

The explain API computes a score explanation for a query and a specific
document. This can give useful feedback whether a document matches or
didn't match a specific query.

#### Path parameters

`<id>`::
  (Required, integer) Defines the document ID.
  
`<index>`::
(Required, string)
Index names used to limit the request.

Only a single index name can be provided to this parameter.

#### Query parameters

`analyzer`::
(Optional, string) Analyzer to use for the query string.
This parameter can only be used when the `q` query string parameter is
specified.
`analyze_wildcard`::
(Optional, Boolean) If `true`, wildcard and prefix queries are analyzed.
Defaults to `false`.
This parameter can only be used when the `q` query string parameter is
specified.
`default_operator`::
(Optional, string) The default operator for query string query: AND or OR.
Defaults to `OR`.
This parameter can only be used when the `q` query string parameter is
specified.
`df`::
(Optional, string) Field to use as default where no field prefix is given in the
query string.
This parameter can only be used when the `q` query string parameter is
specified.
`lenient`::
(Optional, Boolean) If `true`, format-based query failures (such as providing
text to a numeric field) in the query string will be ignored. Defaults to
`false`.
This parameter can only be used when the `q` query string parameter is
specified.
`preference`::
(Optional, string) Specifies the node or shard the operation should be
performed on. Random by default.
`q`::
(Optional, string) Query in the Lucene query string syntax.
`stored_fields`::
  (Optional, string) A comma-separated list of stored fields to return in the 
  response.

`routing`::
(Optional, string)
Custom value used to route operations to a specific shard.
`_source`::
(Optional, string) True or false to return the `_source` field or not, or a
list of fields to return.
`_source_excludes`::
(Optional, string)
A comma-separated list of source fields to exclude from
the response.
You can also use this parameter to exclude fields from the subset specified in
`_source_includes` query parameter.
If the `_source` parameter is `false`, this parameter is ignored.
`_source_includes`::
(Optional, string)
A comma-separated list of source fields to
include in the response.
If this parameter is specified, only these source fields are returned. You can
exclude fields from this subset using the `_source_excludes` query parameter.
If the `_source` parameter is `false`, this parameter is ignored.

#### Request body

`query`::
(Optional, query object) Defines the search query using
Query DSL.

#### Examples

```console
GET /my-index-000001/_explain/0
{
  "query" : {
    "match" : { "message" : "elasticsearch" }
  }
}
```

The API returns the following response:

```console-result
{
   "_index":"my-index-000001",
   "_id":"0",
   "matched":true,
   "explanation":{
      "value":1.6943598,
      "description":"weight(message:elasticsearch in 0) [PerFieldSimilarity], result of:",
      "details":[
         {
            "value":1.6943598,
            "description":"score(freq=1.0), computed as boost * idf * tf from:",
            "details":[
               {
                  "value":2.2,
                  "description":"boost",
                  "details":[]
               },
               {
                  "value":1.3862944,
                  "description":"idf, computed as log(1 + (N - n + 0.5) / (n + 0.5)) from:",
                  "details":[
                     {
                        "value":1,
                        "description":"n, number of documents containing term",
                        "details":[]
                     },
                     {
                        "value":5,
                        "description":"N, total number of documents with field",
                        "details":[]
                     }
                  ]
               },
               {
                  "value":0.5555556,
                  "description":"tf, computed as freq / (freq + k1 * (1 - b + b * dl / avgdl)) from:",
                  "details":[
                     {
                        "value":1.0,
                        "description":"freq, occurrences of term within document",
                        "details":[]
                     },
                     {
                        "value":1.2,
                        "description":"k1, term saturation parameter",
                        "details":[]
                     },
                     {
                        "value":0.75,
                        "description":"b, length normalization parameter",
                        "details":[]
                     },
                     {
                        "value":3.0,
                        "description":"dl, length of field",
                        "details":[]
                     },
                     {
                        "value":5.4,
                        "description":"avgdl, average length of field",
                        "details":[]
                     }
                  ]
               }
            ]
         }
      ]
   }
}
```

There is also a simpler way of specifying the query via the `q` parameter. The 
specified `q` parameter value is then parsed as if the `query_string` query was 
used. Example usage of the `q` parameter in the
explain API:

```console
GET /my-index-000001/_explain/0?q=message:search
```

The API returns the same result as the previous request.
