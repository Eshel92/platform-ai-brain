<!-- Converted from api/index-patterns/update.asciidoc (AsciiDoc). Includes are inlined. -->

### Update index pattern API

deprecated::[8.0.0,Use the [data views API](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-data-views) instead.]

experimental[] Update part of an index pattern. Only the specified fields are updated in the
index pattern. Unspecified fields stay as they are persisted.

#### Request

`POST <kibana host>:<port>/api/index_patterns/index_pattern/<id>`

`POST <kibana host>:<port>/s/<space_id>/api/index_patterns/index_pattern/<id>`

#### Path parameters

`space_id`::
  (Optional, string) An identifier for the space. If `space_id` is not provided in the URL, the default space is used.

`id`::
  (Required, string) The ID of the index pattern you want to update.

#### Request body

`refresh_fields`:: (Optional, boolean) Reloads the index pattern fields after
the index pattern is updated. The default is `false`.

`index_pattern`::
  (Required, object) The index patterns fields you want to update.

You can partially update the following fields:

* `title`
* `name`
* `timeFieldName`
* `fields`
* `sourceFilters`
* `fieldFormatMap`
* `type`
* `typeMeta`

#### Response code

`200`::
    Indicates a successful call.

#### Examples

Update a title of the `<my-pattern>` index pattern:

```sh
$ curl -X POST api/index_patterns/index-pattern/my-pattern
{
  "index_pattern": {
    "title": "some-other-pattern-*"
  }
}
```

Customize the update behavior:

```sh
$ curl -X POST api/index_patterns/index-pattern/my-pattern
{
  "refresh_fields": true,
  "index_pattern": {
    "fields": {}
  }
}
```

All update fields are optional, but you can specify the following fields:

```sh
$ curl -X POST api/index_patterns/index-pattern/my-pattern
{
  "index_pattern": {
    "title": "...",
    "name": "...",
    "timeFieldName": "...",
    "sourceFilters": [],
    "fieldFormats": {},
    "type": "...",
    "typeMeta": {},
    "fields": {},
    "runtimeFieldMap": {}
  }
}
```

The API returns the updated index pattern object:

```sh
{
    "index_pattern": {

    }
}
```
