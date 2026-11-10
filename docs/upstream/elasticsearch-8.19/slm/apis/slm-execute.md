<!-- Converted from slm/apis/slm-execute.asciidoc (AsciiDoc). Includes are inlined. -->

### Execute snapshot lifecycle policy API

**New API reference**
For the most up-to-date API details, refer to [Snapshot lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-slm).

Immediately creates a snapshot according to the lifecycle policy, 
without waiting for the scheduled time.

#### Request

`PUT /_slm/policy/<snapshot-lifecycle-policy-id>/_execute`

#### Prerequisites

If the Elasticsearch security features are enabled, you must have the `manage_slm`
cluster privilege to use this API. For more information, see
security-privileges.

#### Description

Manually applies the snapshot policy to immediately create a snapshot. 
The snapshot policy is normally applied according to its schedule,
but you might want to manually execute a policy before performing an upgrade
or other maintenance. 

#### Path parameters

`<policy-id>`::
(Required, string)
ID of the snapshot lifecycle policy to execute.

#### Examples

To take an immediate snapshot according to the `daily-snapshots` policy:

```console
POST /_slm/policy/daily-snapshots/_execute
```

If successful, this request returns the generated snapshot name:

```console-result
{
  "snapshot_name": "daily-snap-2019.04.24-gwrqoo2xtea3q57vvg0uea"
}
```

The snapshot is taken in the background. You can use the 
snapshot APIs to 
monitor the status of the snapshot.

To see the status of a policy's most recent snapshot, you can use the 
get snapshot lifecycle policy API.
