<!-- Converted from search/validate.asciidoc (AsciiDoc). Includes are inlined. -->

### Validate API

**New API reference**
For the most up-to-date API details, refer to [Validate a query](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-validate-query).

Validates a potentially expensive query without executing it.

```console
GET my-index-000001/_validate/query?q=user.id:kimchy
```

#### Request

`GET /<target>/_validate/<query>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for the target data stream, index,
or alias.

#### Description

The validate API allows you to validate a potentially expensive query
without executing it. The query can be sent either as a path parameter or in the
request body.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases to
search. Supports wildcards (`*`). To search all data streams or indices, omit
this parameter or use `*` or `_all`.

`query`::
(Optional, query object) Defines the search query using
Query DSL.

#### Query parameters

`all_shards`::
  (Optional, Boolean) If `true`, the validation is executed on all shards
  instead of one random shard per index. Defaults to `false`.

`allow_no_indices`::
(Optional, Boolean)
If `false`, the request returns an error if any wildcard expression,
index alias, or `_all` value targets only missing or closed indices.
This behavior applies even if the request targets other open indices. For
example, a request targeting `foo*,bar*` returns an error if an index starts
with `foo` but no index starts with `bar`.
Defaults to `false`.

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
`expand_wildcards`::
(Optional, string)
Type of index that wildcard patterns can match. If the request can target data
streams, this argument determines whether wildcard expressions match hidden data
streams. Supports comma-separated values, such as `open,hidden`. Valid values
are:

`all`::
Match any data stream or index, including hidden ones.

`open`::
Match open, non-hidden indices. Also matches any non-hidden data stream.

`closed`::
Match closed, non-hidden indices. Also matches any non-hidden data stream. Data
streams cannot be closed.

`hidden`::
Match hidden data streams and hidden indices. Must be combined with `open`,
`closed`, or both.

`none`::
Wildcard patterns are not accepted.
`explain`::
  (Optional, Boolean) If `true`, the response returns detailed information if an
  error has occurred. Defaults to `false`.

`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`lenient`::
(Optional, Boolean) If `true`, format-based query failures (such as providing
text to a numeric field) in the query string will be ignored. Defaults to
`false`.
This parameter can only be used when the `q` query string parameter is
specified.
`rewrite`::
  (Optional, Boolean) If `true`, returns a more detailed explanation showing the
  actual Lucene query that will be executed. Defaults to `false`.

`q`::
(Optional, string) Query in the Lucene query string syntax.

#### Examples

```console
PUT my-index-000001/_bulk?refresh
{"index":{"_id":1}}
{"user" : { "id": "kimchy" }, "@timestamp" : "2099-11-15T14:12:12", "message" : "trying out Elasticsearch"}
{"index":{"_id":2}}
{"user" : { "id": "kimchi" }, "@timestamp" : "2099-11-15T14:12:13", "message" : "My user ID is similar to kimchy!"}
```

When sent a valid query:

```console
GET my-index-000001/_validate/query?q=user.id:kimchy
```

The response contains `valid:true`:

```console-result
{"valid":true,"_shards":{"total":1,"successful":1,"failed":0}}
```

The query may also be sent in the request body:

```console
GET my-index-000001/_validate/query
{
  "query" : {
    "bool" : {
      "must" : {
        "query_string" : {
          "query" : "*:*"
        }
      },
      "filter" : {
        "term" : { "user.id" : "kimchy" }
      }
    }
  }
}
```

**Note:** The query being sent in the body must be nested in a `query` key, same as
the search api works

If the query is invalid, `valid` will be `false`. Here the query is invalid
because Elasticsearch knows the `post_date` field should be a date due to dynamic
mapping, and 'foo' does not correctly parse into a date:

```console
GET my-index-000001/_validate/query
{
  "query": {
    "query_string": {
      "query": "@timestamp:foo",
      "lenient": false
    }
  }
}
```

```console-result
{"valid":false,"_shards":{"total":1,"successful":1,"failed":0}}
```

##### The explain parameter

An `explain` parameter can be specified to get more detailed information about
why a query failed:

```console
GET my-index-000001/_validate/query?explain=true
{
  "query": {
    "query_string": {
      "query": "@timestamp:foo",
      "lenient": false
    }
  }
}
```

The API returns the following response:

```console-result
{
  "valid" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "failed" : 0
  },
  "explanations" : [ {
    "index" : "my-index-000001",
    "valid" : false,
    "error" : "my-index-000001/IAEc2nIXSSunQA_suI0MLw] QueryShardException[failed to create query:...failed to parse date field [foo]"
  } ]
}
```

##### The rewrite parameter

When the query is valid, the explanation defaults to the string representation
of that query. With `rewrite` set to `true`, the explanation is more detailed
showing the actual Lucene query that will be executed.

```console
GET my-index-000001/_validate/query?rewrite=true
{
  "query": {
    "more_like_this": {
      "like": {
        "_id": "2"
      },
      "boost_terms": 1
    }
  }
}
```

The API returns the following response:

```console-result
{
   "valid": true,
   "_shards": {
      "total": 1,
      "successful": 1,
      "failed": 0
   },
   "explanations": [
      {
         "index": "my-index-000001",
         "valid": true,
         "explanation": "((user:terminator^3.71334 plot:future^2.763601 plot:human^2.8415773 plot:sarah^3.4193945 plot:kyle^3.8244398 plot:cyborg^3.9177752 plot:connor^4.040236 plot:reese^4.7133346 ... )~6) -ConstantScore(_id:2)) #(ConstantScore(_type:_doc))^0.0"
      }
   ]
}
```

##### Rewrite and all_shards parameters

By default, the request is executed on a single shard only, which is randomly
selected. The detailed explanation of the query may depend on which shard is
being hit, and therefore may vary from one request to another. So, in case of
query rewrite the `all_shards` parameter should be used to get response from
all available shards.

```console
GET my-index-000001/_validate/query?rewrite=true&all_shards=true
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

The API returns the following response:

```console-result
{
  "valid": true,
  "_shards": {
    "total": 1,
    "successful": 1,
    "failed": 0
  },
  "explanations": [
    {
      "index": "my-index-000001",
      "shard": 0,
      "valid": true,
      "explanation": "(user.id:kimchi)^0.8333333 user.id:kimchy"
    }
  ]
}
```
