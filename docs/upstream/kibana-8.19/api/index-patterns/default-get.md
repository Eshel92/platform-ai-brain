<!-- Converted from api/index-patterns/default-get.asciidoc (AsciiDoc). Includes are inlined. -->

### Get default index pattern API

deprecated::[8.0.0,Use the [data views API](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-data-views) instead.]

experimental[] Retrieve a default index pattern ID. Kibana UI uses default index pattern unless user picks a different one.

#### Request

`GET <kibana host>:<port>/api/index_patterns/default`

`GET <kibana host>:<port>/s/<space_id>/api/index_patterns/default`

#### Path parameters

`space_id`::
(Optional, string) An identifier for the space. If `space_id` is not provided in the URL, the default space is used.

#### Response code

`200`::
Indicates a successful call.

#### Example

Retrieve the default index pattern id:

```sh
$ curl -X GET api/index_patterns/default
```

The API returns an ID of a default index pattern:

```sh
{
    "index_pattern_id": "..."
}
```

In case there is no default index pattern, the API returns:

```sh
{
    "index_pattern_id": null
}
```
