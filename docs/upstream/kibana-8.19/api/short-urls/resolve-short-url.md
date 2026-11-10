<!-- Converted from api/short-urls/resolve-short-url.asciidoc (AsciiDoc). Includes are inlined. -->

### Resolve short URL API

experimental[] Resolve a single Kibana short URL by its slug.

#### Request

`GET <kibana host>:<port>/api/short_url/_slug/<slug>`

#### Path parameters

`slug`::
  (Required, string) The slug of the short URL.

#### Response code

`200`::
    Indicates a successful call.

#### Example

Retrieve the short URL with the `hello-world` ID:

```sh
$ curl -X GET api/short_url/_slug/hello-world
```

The API returns the following:

```sh
{
  "id": "12345",
  "slug": "hello-world",
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
