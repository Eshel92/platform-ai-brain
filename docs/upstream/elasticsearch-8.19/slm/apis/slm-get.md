<!-- Converted from slm/apis/slm-get.asciidoc (AsciiDoc). Includes are inlined. -->

### Get snapshot lifecycle policy API

**New API reference**
For the most up-to-date API details, refer to [Snapshot lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-slm).

Retrieves one or more snapshot lifecycle policy definitions and
information about the latest snapshot attempts.

#### Request

`GET _slm/policy/<policy-id>`

`GET _slm/policy`

#### Prerequisites

If the Elasticsearch security features are enabled, you must have the `manage_slm`
cluster privilege to use this API. For more information, see
security-privileges.

#### Description

Returns the specified policy definition and 
information about the latest successful and failed attempts to create snapshots. 
If no policy is specified, returns all defined policies.

#### Path parameters

`<policy-id>`::
(Optional, string)
Comma-separated list of snapshot lifecycle policy IDs.

#### Examples

##### Get a specific policy

Get the `daily-snapshots` policy:

```console
GET _slm/policy/daily-snapshots?human
```

This request returns the following response:

```console-result
{
  "daily-snapshots": {
    "version": 1,                                 <1>
    "modified_date": "2099-05-06T01:30:00.000Z",  <2>
    "modified_date_millis": 4081757400000,
    "policy" : {
      "schedule": "0 30 1 * * ?",
      "name": "<daily-snap-{now/d}>",
      "repository": "my_repository",
      "config": {
        "indices": ["data-*", "important"],
        "ignore_unavailable": false,
        "include_global_state": false
      },
      "retention": {
        "expire_after": "30d",
        "min_count": 5,
        "max_count": 50
      }
    },
    "stats": {
      "policy": "daily-snapshots",
      "snapshots_taken": 0,
      "snapshots_failed": 0,
      "snapshots_deleted": 0,
      "snapshot_deletion_failures": 0
    },
    "next_execution": "2099-05-07T01:30:00.000Z", <3>
    "next_execution_millis": 4081843800000
  }
}
```
<1> The version of the snapshot policy, only the latest version is stored and incremented when the policy is updated
<2> The last time this policy was modified.
<3> The next time this policy will be executed.

##### Get all policies

```console
GET _slm/policy
```
