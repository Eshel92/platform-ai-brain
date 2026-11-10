<!-- Converted from api/index-patterns/runtime-fields/get.asciidoc (AsciiDoc). Includes are inlined. -->

### Get runtime field API

deprecated::[8.0.0,Use the [data views API](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-data-views) instead.]

experimental[] Get a runtime field

#### Request

`GET <kibana host>:<port>/api/index_patterns/index_pattern/<index_pattern_id>/runtime_field/<name>`

`GET <kibana host>:<port>/s/<space_id>/api/index_patterns/index_pattern/<index_pattern_id>/runtime_field/<name>`

#### Path parameters

`space_id`::
(Optional, string) An identifier for the space. If `space_id` is not provided in the URL, the default space is used.

`index_pattern_id`::
(Required, string) The ID of the index pattern.

`name`::
(Required, string) The name of the runtime field you want to retrieve.

#### Example

Retrieve a runtime field named `foo` of index pattern with the `my-pattern` ID:

```sh
$ curl -X GET api/index_patterns/index_pattern/my-pattern/runtime_field/foo
```

The API returns a runtime `field` object, and a `runtimeField` definition object:

```sh
{
    "field": {
        ...
    },
    "runtimeField": {
        ...
    }
}
```
