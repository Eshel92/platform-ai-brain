<!-- Converted from transform/apis/reset-transform.asciidoc (AsciiDoc). Includes are inlined. -->

# Reset transform API

**New API reference**
For the most up-to-date API details, refer to [Transform APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-transform).

Resets a transform.

## Request

`POST _transform/<transform_id>/_reset`

## Prerequisites

* Requires the `manage_transform` cluster privilege. This privilege is included
in the `transform_admin` built-in role.

[reset-transform-desc]]

## Description

Before you can reset the transform, you must stop it; alternatively, use the
`force` query parameter.

If you reset a transform, all checkpoints, states, and the destination index 
(if it was created by the transform) are deleted. The transform is updated 
to the latest format as if the update-transform API was used. The 
transform is ready to start again as if it had just been created.

## Path parameters

`<transform_id>`::
(Required, string)
Identifier for the transform.

## Query parameters

`force`::
(Optional, Boolean)
If this value is `true`, the transform is reset regardless of its current
state. If it's false, the transform must be `stopped` before it can be reset.
The default value is `false`

`timeout`::
(Optional, time)
Period to wait for a response. If no response is received before the timeout
expires, the request fails and returns an error. Defaults to `30s`.

## Examples

```console
POST _transform/ecommerce_transform/_reset
```

When the transform is reset, you receive the following results:

```console-result
{
  "acknowledged" : true
}
```
