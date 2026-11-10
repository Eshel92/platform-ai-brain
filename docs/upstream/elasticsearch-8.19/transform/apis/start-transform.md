<!-- Converted from transform/apis/start-transform.asciidoc (AsciiDoc). Includes are inlined. -->

# Start transform API

**New API reference**
For the most up-to-date API details, refer to [Transform APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-transform).

Starts a transform.

## Request

`POST _transform/<transform_id>/_start`

## Prerequisites

Requires the following privileges:

* cluster: `manage_transform` (the `transform_admin` built-in role grants this
  privilege)

## Description

When you start a transform, it creates the destination index if it does not
already exist. The `number_of_shards` is set to `1` and the
`auto_expand_replicas` is set to `0-1`.

If it is a pivot transform, it deduces the mapping definitions for the
destination index from the source indices and the transform aggregations. If
fields in the destination index are derived from scripts (as in the case of
`scripted_metric` or `bucket_script` aggregations), the transform uses
dynamic mappings unless an index template exists.

If it is a latest transform, it does not deduce mapping definitions; it uses
dynamic mappings.

**Tip:** To use explicit mappings, create the destination index before you start the
transform. Alternatively, you can create an index template, though it does not
affect the deduced mappings in a pivot transform.

When the transform starts, a series of validations occur to ensure
its success. If you deferred validation when you created the
transform, they occur when you start the transform--with the
exception of privilege checks. When Elasticsearch security features are enabled, the
transform remembers which roles the user that created it had at the
time of creation and uses those same roles. If those roles do not have the
required privileges on the source and destination indices, the
transform fails when it attempts unauthorized operations.

## Path parameters

`<transform_id>`::
(Required, string)
Identifier for the transform.

## Query parameters

`from`::
(Optional, string) Restricts the set of transformed entities to those changed
 after this time. Relative times like now-30d are supported.
Only applicable for continuous transforms.

`timeout`::
(Optional, time)
Period to wait for a response. If no response is received before the timeout
expires, the request fails and returns an error. Defaults to `30s`.

## Examples

```console
POST _transform/ecommerce_transform/_start
```

When the transform starts, you receive the following results:

```console-result
{
  "acknowledged" : true
}
```
