<!-- Converted from slm/apis/slm-delete.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete snapshot lifecycle policy API

**New API reference**
For the most up-to-date API details, refer to [Snapshot lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-slm).

Deletes an existing snapshot lifecycle policy.

#### Request

`DELETE /_slm/policy/<snapshot-lifecycle-policy-id>`

#### Prerequisites

If the Elasticsearch security features are enabled, you must have the `manage_slm`
cluster privilege to use this API. For more information, see
security-privileges.

#### Description

Deletes the specified lifecycle policy definition. 
This prevents any future snapshots from being taken
but does not cancel in-progress snapshots
or remove previously-taken snapshots.

#### Path parameters

`<policy-id>`::
(Required, string)
ID of the snapshot lifecycle policy to delete.

#### Examples

```console
DELETE /_slm/policy/daily-snapshots
```
