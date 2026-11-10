<!-- Converted from query-dsl/parent-id-query.asciidoc (AsciiDoc). Includes are inlined. -->

### Parent ID query

Returns child documents joined to a specific parent document.
You can use a join field mapping to create parent-child
relationships between documents in the same index.

#### Example request

##### Index setup

To use the `parent_id` query, your index must include a join
field mapping. To see how you can set up an index for the `parent_id` query, try
the following example.

. Create an index with a join field mapping.
```console
PUT /my-index-000001
{
  "mappings": {
    "properties": {
      "my-join-field": {
        "type": "join",
        "relations": {
          "my-parent": "my-child"
        }
      }
    }
  }
}

```

. Index a parent document with an ID of `1`.
```console
PUT /my-index-000001/_doc/1?refresh
{
  "text": "This is a parent document.",
  "my-join-field": "my-parent"
}
```

. Index a child document of the parent document.
```console
PUT /my-index-000001/_doc/2?routing=1&refresh
{
  "text": "This is a child document.",
  "my-join-field": {
    "name": "my-child",
    "parent": "1"
  }
}
```

##### Example query

The following search returns child documents for a parent document with an ID of
`1`.

```console
GET /my-index-000001/_search
{
  "query": {
      "parent_id": {
          "type": "my-child",
          "id": "1"
      }
  }
}
```

#### Top-level parameters for `parent_id`

`type`::
(Required, string) Name of the child relationship mapped for the
join field.

`id`::
(Required, string) ID of the parent document. The query will return child
documents of this parent document.

`ignore_unmapped`::
(Optional, Boolean) Indicates whether to ignore an unmapped `type` and not
return any documents instead of an error. Defaults to `false`.

If `false`, Elasticsearch returns an error if the `type` is unmapped.

You can use this parameter to query multiple indices that may not contain the
`type`.
