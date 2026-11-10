<!-- Converted from query-dsl/_query-template.asciidoc (AsciiDoc). Includes are inlined. -->

### Sample query

Does a cool thing. For example, it matches `x` to `y`.

#### Example request

```console
GET _search
{
  "query": {
    "sample": {
      "foo": "baz",
      "bar": true
    }
  }
}
```

#### Parameters

`foo`::
(Required, string)
A cool thing.

`bar`::
(Optional, string)
If `true`, does a cool thing.
Defaults to `false`.

#### Notes

##### Avoid using the `sample` query for `text` fields

By default, Elasticsearch changes the values of `text` fields during analysis. For
example, ...

##### Using the `sample` query on time series data

You can use the `sample` query to perform searches on time series data.
For example:

```console
GET my_time_series_index/_search
{
  "query": {
    "sample": {
      "foo": "baz",
      "bar": false
    }
  }
}
```
