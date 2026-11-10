<!-- Converted from transform/apis/stop-transform.asciidoc (AsciiDoc). Includes are inlined. -->

# Stop transforms API

**New API reference**
For the most up-to-date API details, refer to [Transform APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-transform).

Stops one or more transforms.

## Request

`POST _transform/<transform_id>/_stop` +

`POST _transform/<transform_id1>,<transform_id2>/_stop` +

`POST _transform/_all/_stop`

## Prerequisites

Requires the `manage_transform` cluster privilege. This privilege is included 
in the `transform_admin` built-in role.

## Path parameters

`<transform_id>`::
(Required, string)
Identifier for the transform. To stop multiple transforms, use a
comma-separated list or a wildcard expression. To stop all transforms, use
`_all` or `*` as the identifier.

## Query parameters

`allow_no_match`::
 (Optional, Boolean)
Specifies what to do when the request:
* Contains wildcard expressions and there are no transforms that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns a successful acknowledgement message
when there are no matches. When there are only partial matches, the API stops
the appropriate transforms. For example, if the request contains
`test-id1*,test-id2*` as the identifiers and there are no transforms
that match `test-id2*`, the API nonetheless stops the transforms
that match `test-id1*`.

If this parameter is `false`, the request returns a `404` status code when there
are no matches or only partial matches.
`force`::
  (Optional, Boolean) Set to `true` to stop a failed transform or to 
  forcefully stop a transform that did not respond to the initial stop 
  request.

`timeout`::
  (Optional, time value) If `wait_for_completion=true`, the API blocks for (at
  maximum) the specified duration while waiting for the transform to stop. If
  more than `timeout` time has passed, the API throws a timeout exception. Even
  if a timeout exception is thrown, the stop request is still processing and
  eventually moves the transform to `STOPPED`. The timeout simply means the API
  call itself timed out while waiting for the status change. Defaults to `30s`.

`wait_for_checkpoint`::
  (Optional, Boolean) If set to `true`, the transform will not completely stop
  until the current checkpoint is completed. If set to `false`, the transform
  stops as soon as possible. Defaults to `false`.

`wait_for_completion`::
  (Optional, Boolean) If set to `true`, causes the API to block until the indexer 
  state completely stops. If set to `false`, the API returns immediately and the
  indexer will be stopped asynchronously in the background. Defaults to `false`.

## Response codes

`404` (Missing resources)::
  If `allow_no_match` is `false`, this code indicates that there are no
  resources that match the request or only partial matches for the request. 

## Examples

```console
POST _transform/ecommerce_transform/_stop
```

When the transform stops, you receive the following results:

```console-result
{
  "acknowledged" : true
}
```
