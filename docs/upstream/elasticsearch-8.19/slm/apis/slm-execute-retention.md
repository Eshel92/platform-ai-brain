<!-- Converted from slm/apis/slm-execute-retention.asciidoc (AsciiDoc). Includes are inlined. -->

### Execute snapshot retention policy API

**New API reference**
For the most up-to-date API details, refer to [Snapshot lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-slm).

Deletes any snapshots that are expired according to the policy's retention rules.

#### Request

`POST /_slm/_execute_retention`

#### Prerequisites

If the Elasticsearch security features are enabled, you must have the `manage_slm`
cluster privilege to use this API. For more information, see
security-privileges.

#### Description

Manually applies the retention policy to force immediate removal of expired snapshots. 
The retention policy is normally applied according to its schedule.

#### Examples

To force removal of expired snapshots:

```console
POST /_slm/_execute_retention
```

Retention runs asynchronously in the background.
