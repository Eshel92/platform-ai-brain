<!-- Converted from query-dsl/ids-query.asciidoc (AsciiDoc). Includes are inlined. -->

### IDs

Returns documents based on their IDs. This query uses document IDs stored in
the `_id` field.

#### Example request

```console
GET /_search
{
  "query": {
    "ids" : {
      "values" : ["1", "4", "100"]
    }
  }
}    
```

#### Top-level parameters for `ids`

`values`::
(Required, array of strings) An array of document IDs.
