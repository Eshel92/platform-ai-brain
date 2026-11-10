<!-- Converted from query-dsl/wildcard-query.asciidoc (AsciiDoc). Includes are inlined. -->

### Wildcard query

Returns documents that contain terms matching a wildcard pattern.

A wildcard operator is a placeholder that matches one or more characters. For
example, the `*` wildcard operator matches zero or more characters. You can
combine wildcard operators with other characters to create a wildcard pattern.

#### Example request

The following search returns documents where the `user.id` field contains a term
that begins with `ki` and ends with `y`. These matching terms can include `kiy`,
`kity`, or `kimchy`.

```console
GET /_search
{
  "query": {
    "wildcard": {
      "user.id": {
        "value": "ki*y",
        "boost": 1.0,
        "rewrite": "constant_score_blended"
      }
    }
  }
}
```

#### Top-level parameters for `wildcard`

`<field>`::
(Required, object) Field you wish to search.

#### Parameters for `<field>`

`boost`::
(Optional, float) Floating point number used to decrease or increase the
relevance scores of a query. Defaults to `1.0`.
You can use the `boost` parameter to adjust relevance scores for searches
containing two or more queries.
Boost values are relative to the default value of `1.0`. A boost value between
`0` and `1.0` decreases the relevance score. A value greater than `1.0`
increases the relevance score.

`case_insensitive` added:[7.10.0]::
(Optional, Boolean) Allows case insensitive matching of the
pattern with the indexed field values when set to true. Default is false which means
the case sensitivity of matching depends on the underlying field's mapping.

`rewrite`::
(Optional, string) Method used to rewrite the query. For valid values and more information, see the
`rewrite` parameter.

`value`::
(Required, string) Wildcard pattern for terms you wish to find in the provided
`<field>`.
This parameter supports two wildcard operators:

* `?`, which matches any single character
* `*`, which can match zero or more characters, including an empty one

**Warning:** Avoid beginning patterns with `*` or `?`. This can increase
the iterations needed to find matching terms and slow search performance.

`wildcard`::
(Required, string) An alias for the `value` parameter. If you specify both
`value` and `wildcard`, the query uses the last one in the request body.

#### Notes

Wildcard queries using `*` can be resource-intensive, particularly with leading wildcards. To improve performance, minimize their use and consider alternatives like the n-gram tokenizer. While this allows for more efficient searching, it may increase index size. For better performance and accuracy, combine wildcard queries with other query types like `match` or `bool` to first narrow down results.

##### Allow expensive queries

Wildcard queries will not be executed if `search.allow_expensive_queries`
is set to false.
