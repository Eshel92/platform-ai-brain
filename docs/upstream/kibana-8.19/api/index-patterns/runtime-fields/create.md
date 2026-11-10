<!-- Converted from api/index-patterns/runtime-fields/create.asciidoc (AsciiDoc). Includes are inlined. -->

### Create runtime field API

deprecated::[8.0.0,Use the [data views API](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-data-views) instead.]

experimental[] Create a runtime field

#### Request

`POST <kibana host>:<port>/api/index_patterns/index_pattern/<index_pattern_id>/runtime_field`

`POST <kibana host>:<port>/s/<space_id>/api/index_patterns/index_pattern/<index_pattern_id>/runtime_field`

#### Path parameters

`space_id`::
(Optional, string) An identifier for the space. If `space_id` is not provided in the URL, the default space is used.

`index_pattern_id`::
(Required, string) The ID of the index pattern.

#### Request body

`name`:: (Required, string) The name for a runtime field.

`runtimeField`:: (Required, object) The runtime field definition object.

#### Examples

Create a runtime field on an index pattern:

```sh
$ curl -X POST api/index_patterns/index_pattern/<index_pattern_id>/runtime_field
{
  "name": "runtimeFoo",
  "runtimeField": {
     "type": "long",
     "script": {
        "source": "emit(doc["foo"].value)"
      }
  }
}
```

The API returns created runtime field object and update index pattern object:

```sh
{
    "index_pattern": {...},
    "field": {...}
}
```
