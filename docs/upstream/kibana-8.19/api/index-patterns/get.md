<!-- Converted from api/index-patterns/get.asciidoc (AsciiDoc). Includes are inlined. -->

### Get index pattern API

deprecated::[8.0.0,Use the [data views API](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-data-views) instead.]

experimental[] Retrieve a single Kibana index pattern by ID.

#### Request

`GET <kibana host>:<port>/api/index_patterns/index_pattern/<id>`

`GET <kibana host>:<port>/s/<space_id>/api/index_patterns/index_pattern/<id>`

#### Path parameters

`space_id`::
(Optional, string) An identifier for the space. If `space_id` is not provided in the URL, the default space is used.

`id`::
(Required, string) The ID of the index pattern you want to retrieve.

#### Response code

`200`::
Indicates a successful call.

`404`::
The specified index pattern and ID doesn't exist.

#### Example

Retrieve the index pattern object with the `my-pattern` ID:

```sh
$ curl -X GET api/index_patterns/index_pattern/my-pattern
```

The API returns an index pattern object:

```sh
{
    "index_pattern": {
        "id": "my-pattern",
        "version": "...",
        "title": "...",
        "type": "...",
        "timeFieldName": "...",
        "sourceFilters": [],
        "fields": {},
        "typeMeta": {},
        "fieldFormats": {},
        "fieldAttrs": {},
        "runtimeFieldMap" {},
        "allowNoIndex: "..."
    }
}
```
