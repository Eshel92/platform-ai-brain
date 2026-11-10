<!-- Converted from api/index-patterns/delete.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete index pattern API

deprecated::[8.0.0,Use data-views-api-delete instead.]

experimental[] Delete Kibana index patterns.

**Warning:** Once you delete an index pattern, _it cannot be recovered_.

#### Request

`DELETE <kibana host>:<port>/api/index_patterns/index_pattern/<id>`

`DELETE <kibana host>:<port>/s/<space_id>/api/index_patterns/index_pattern/<id>`

#### Path parameters

`space_id`::
  (Optional, string) An identifier for the space. If `space_id` is not provided in the URL, the default space is used.

`id`::
  (Required, string) The ID of the index pattern you want to delete.

#### Response code

`200`::
  Indicates that index pattern is deleted. Returns an empty response body. 

#### Example

Delete an index pattern object with the `my-pattern` ID:

```sh
$ curl -X DELETE api/index_patterns/index_pattern/my-pattern
```
