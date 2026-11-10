<!-- Converted from api/short-urls/get-short-url.asciidoc (AsciiDoc). Includes are inlined. -->

### Get short URL API

experimental[] Retrieve a single Kibana short URL.

#### Request

`GET <kibana host>:<port>/api/short_url/<id>`

#### Path parameters

`id`::
  (Required, string) The ID of the short URL.

#### Response code

`200`::
    Indicates a successful call.

#### Example

Retrieve the short URL with the `12345` ID:

```sh
$ curl -X GET api/short_url/12345
```

The API returns the following:

```sh
{
  "id": "12345",
  "slug": "adjective-adjective-noun",
  "locator": {
    "id": "LOCATOR_ID",
    "version": "x.x.x",
    "state": {}
  },
  "accessCount": 0,
  "accessDate": 1632680100000,
  "createDate": 1632680100000
}
```
