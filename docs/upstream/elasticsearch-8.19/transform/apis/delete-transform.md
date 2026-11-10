<!-- Converted from transform/apis/delete-transform.asciidoc (AsciiDoc). Includes are inlined. -->

# Delete transform API

**New API reference**
For the most up-to-date API details, refer to [Transform APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-transform).

Deletes an existing transform.

## Request

`DELETE _transform/<transform_id>`

## Prerequisites

* Requires the `manage_transform` cluster privilege. This privilege is included 
in the `transform_admin` built-in role.
* Before you can delete the transform, you must stop it.

## Path parameters

`<transform_id>`::
(Required, string)
Identifier for the transform.

## Query parameters

`force`::
(Optional, Boolean) When `true`, the transform is deleted regardless of its
current state. The default value is `false`, meaning that the transform must be
`stopped` before it can be deleted.

`delete_dest_index`::
(Optional, Boolean) When `true`, the destination index is deleted together with
the transform. The default value is `false`, meaning that the destination
index will not be deleted.

`timeout`::
(Optional, time)
Period to wait for a response. If no response is received before the timeout
expires, the request fails and returns an error. Defaults to `30s`.

## Examples

```console
DELETE _transform/ecommerce_transform
```

When the transform is deleted, you receive the following results:

```console-result
{
  "acknowledged" : true
}
```
