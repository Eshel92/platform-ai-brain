<!-- Converted from api/index-patterns/default-set.asciidoc (AsciiDoc). Includes are inlined. -->

### Set default index pattern API

deprecated::[8.0.0,Use the [data views API](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-data-views) instead.]

experimental[] Set a default index pattern ID. Kibana UI will use default index pattern unless user picks a different one. 
The API doesn't validate if given `index_pattern_id` is a valid id. 

#### Request

`POST <kibana host>:<port>/api/index_patterns/default`

`POST <kibana host>:<port>/s/<space_id>/api/index_patterns/default`

#### Path parameters

`space_id`::
(Optional, string) An identifier for the space. If `space_id` is not provided in the URL, the default space is used.

#### Request body

`index_pattern_id`:: (Required, `string` or `null`) Sets a default index pattern id. Use `null` to unset a default index pattern.

`force`:: (Optional, boolean) Updates existing default index pattern id. The default is `false`.

#### Response code

`200`::
Indicates a successful call.

#### Example

Set the default index pattern id if none is set:

```sh
$ curl -X POST api/index_patterns/default
{
  "index_pattern_id": "..."
}
```

Upsert the default index pattern:

```sh
$ curl -X POST api/index_patterns/default
{
  "index_pattern_id": "...",
  "force": true
}
```

Unset the default index pattern:

```sh
$ curl -X POST api/index_patterns/default
{
  "index_pattern_id": null,
  "force": true
}
```

The API returns:

```sh
{
    "acknowledged": true
}
```
