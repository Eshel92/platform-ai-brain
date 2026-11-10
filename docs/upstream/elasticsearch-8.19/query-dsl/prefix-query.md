<!-- Converted from query-dsl/prefix-query.asciidoc (AsciiDoc). Includes are inlined. -->

### Prefix query

Returns documents that contain a specific prefix in a provided field.

#### Example request

The following search returns documents where the `user.id` field contains a term
that begins with `ki`.

```console
GET /_search
{
  "query": {
    "prefix": {
      "user.id": {
        "value": "ki"
      }
    }
  }
}
```

#### Top-level parameters for `prefix`

`<field>`::
(Required, object) Field you wish to search.

#### Parameters for `<field>`

`value`::
(Required, string) Beginning characters of terms you wish to find in the
provided `<field>`.

`rewrite`::
(Optional, string) Method used to rewrite the query. For valid values and more
information, see the `rewrite` parameter.

`case_insensitive` added:[7.10.0] ::
(Optional, Boolean) Allows ASCII case insensitive matching of the
value with the indexed field values when set to true. Default is false which means
the case sensitivity of matching depends on the underlying field's mapping.

#### Notes

##### Short request example

You can simplify the `prefix` query syntax by combining the `<field>` and
`value` parameters. For example:

```console
GET /_search
{
  "query": {
    "prefix" : { "user" : "ki" }
  }
}
```

##### Speed up prefix queries

You can speed up prefix queries using the `index_prefixes`
mapping parameter. If enabled, Elasticsearch indexes prefixes in a separate field,
according to the configuration settings. This lets Elasticsearch run prefix queries
more efficiently at the cost of a larger index.

##### Allow expensive queries

Prefix queries will not be executed if `search.allow_expensive_queries`
is set to false. However, if `index_prefixes` are enabled, an optimised query is built which
is not considered slow, and will be executed in spite of this setting.
