<!-- Converted from api/short-urls/delete-short-url.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete short URL API

experimental[] Delete a Kibana short URL.

#### Request

`DELETE <kibana host>:<port>/api/short_url/<id>`

#### Path parameters

`id`::
  (Required, string) The short URL ID that you want to remove.

#### Response code

`200`::
    Indicates a successful call.

#### Example

Delete a short URL `12345` ID:

```sh
$ curl -X DELETE api/short_url/12345
```
