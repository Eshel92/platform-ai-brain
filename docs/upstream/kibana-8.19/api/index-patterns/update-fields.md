<!-- Converted from api/index-patterns/update-fields.asciidoc (AsciiDoc). Includes are inlined. -->

### Update index pattern fields API

deprecated::[8.0.0,Use the [data views API](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-data-views) instead.]

experimental[] Update fields presentation metadata, such as `count`,
`customLabel`, and `format`. You can update multiple fields in one request. Updates
are merged with persisted metadata. To remove existing metadata, specify `null` as the value.

#### Request

`POST <kibana host>:<port>/api/index_patterns/index_pattern/<id>/fields`

`POST <kibana host>:<port>/s/<space_id>/api/index_patterns/index_pattern/<id>/fields`

#### Path parameters

`space_id`::
(Optional, string) An identifier for the space. If `space_id` is not provided in the URL, the default space is used.

`id`::
(Required, string) The ID of the index pattern fields you want to update.

#### Request body

`fields`::
(Required, object) the field object

#### Response code

`200`::
Indicates a successful call.

#### Examples

Set popularity `count` for field `foo`:

```sh
$ curl -X POST api/index_patterns/index-pattern/my-pattern/fields
{
    "fields": {
        "foo": {
            "count": 123
        }
    }
}
```

Update multiple metadata fields in one request:

```sh
$ curl -X POST api/index_patterns/index-pattern/my-pattern/fields
{
    "fields": {
        "foo": {
            "count": 123,
            "customLabel": "Foo"
        },
        "bar": {
            "customLabel": "Bar"
        }
    }
}
```

Use `null` value to delete metadata:
```sh
$ curl -X POST api/index_patterns/index-pattern/my-pattern/fields
{
    "fields": {
        "foo": {
            "customLabel": null
        }
    }
}
```

The endpoint returns the updated index pattern object:
```sh
{
    "index_pattern": {

    }
}
```
