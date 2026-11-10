<!-- Converted from api/index-patterns/create.asciidoc (AsciiDoc). Includes are inlined. -->

### Create index pattern API

deprecated::[8.0.0,Use the [data views API](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-data-views) instead.]

experimental[] Create Kibana index patterns.

#### Request

`POST <kibana host>:<port>/api/index_patterns/index_pattern`

`POST <kibana host>:<port>/s/<space_id>/api/index_patterns/index_pattern`

#### Path parameters

`space_id`::
  (Optional, string) An identifier for the space. If `space_id` is not provided in the URL, the default space is used.

#### Request body

`override`:: (Optional, boolean) Overrides an existing index pattern if an
index pattern with the provided title already exists. The default is `false`.

`refresh_fields`:: (Optional, boolean) Reloads index pattern fields after
the index pattern is stored. The default is `false`.

`index_pattern`:: (Required, object) The index pattern object. All fields are optional.

#### Response code

`200`::
    Indicates a successful call.

#### Examples

Create an index pattern with a custom title:

```sh
$ curl -X POST api/index_patterns/index_pattern
{
  "index_pattern": {
     "title": "hello"
  }
}
```

Customize the creation behavior:

```sh
$ curl -X POST api/index_patterns/index_pattern
{
  "override": false,
  "refresh_fields": true,
  "index_pattern": {
     "title": "hello"
  }
}
```

At creation, all index pattern fields are optional:

```sh
$ curl -X POST api/index_patterns/index_pattern
{
  "index_pattern": {
      "id": "...",
      "version": "...",
      "title": "...",
      "type": "...",
      "timeFieldName": "...",
      "sourceFilters": [],
      "fields": {},
      "typeMeta": {},
      "fieldFormats": {},
      "fieldAttrs": {},
      "runtimeFieldMap": {}
      "allowNoIndex": "..."
    }
}
```

The API returns the index pattern object:

```sh
{
    "index_pattern": {...}
}
```
