<!-- Converted from api/index-patterns/runtime-fields/update.asciidoc (AsciiDoc). Includes are inlined. -->

### Update runtime field API

deprecated::[8.0.0,Use the [data views API](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-data-views) instead.]

experimental[] Update an existing runtime field

#### Request

`POST <kibana host>:<port>/api/index_patterns/index_pattern/<index_pattern_id>/runtime_field/<name>`

`POST <kibana host>:<port>/s/<space_id>/api/index_patterns/index_pattern/<index_pattern_id>/runtime_field/<name>`

#### Path parameters

`space_id`::
(Optional, string) An identifier for the space. If `space_id` is not provided in the URL, the default space is used.

`index_pattern_id`::
(Required, string) The ID of the index pattern.

`name`::
(Required, string) The name of the runtime field you want to update.

#### Request body

`runtimeField`:: (Required, object) The runtime field definition object.

You can update following fields:

* `type`
* `script`

#### Examples

Update an existing runtime field on an index pattern:

```sh
$ curl -X POST api/index_patterns/index_pattern/<index_pattern_id>/runtime_field/<runtime_field_name>
{
  "runtimeField": {
     "script": {
        "source": "emit(doc["bar"].value)"
      }
  }
}
```

The API returns updated runtime field object and updated index pattern object:

```sh
{
    "index_pattern": {...},
    "field": {...}
}
```
