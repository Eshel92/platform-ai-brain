<!-- Converted from slm/apis/slm-put.asciidoc (AsciiDoc). Includes are inlined. -->

### Create or update snapshot lifecycle policy API

**New API reference**
For the most up-to-date API details, refer to [Snapshot lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-slm).

Creates or updates a snapshot lifecycle policy.

#### Request

`PUT /_slm/policy/<snapshot-lifecycle-policy-id>`

#### Prerequisites

If the Elasticsearch security features are enabled, you must have the
`manage_slm` cluster privilege and the `manage` index privilege
for any included indices to use this API.
For more information, see security-privileges.

#### Description

Use the create or update snapshot lifecycle policy API
to create or update a snapshot lifecycle policy.

If the policy already exists,
this request increments the policy's version.
Only the latest version of a policy is stored.

#### Path parameters

`<snapshot-lifecycle-policy-id>`::
(Required, string)
ID for the snapshot lifecycle policy
you want to create or update.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

`timeout`::
(Optional, time units) Period to wait for a response from all relevant nodes in the cluster after updating the cluster metadata.
If no response is received before the timeout expires, the cluster metadata update still applies but the response will indicate that it was not completely acknowledged.
Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Request body

`config`::
(Required, object)
Configuration for each snapshot created by the policy.
**Properties of `config`**
`expand_wildcards`::
(Optional, string) Determines how wildcard patterns in the `indices` parameter
match data streams and indices. Supports comma-separated values, such as
`open,hidden`. Defaults to `all`. Valid values are:

`all`:::
Match any data stream or index, including closed and hidden ones.

`open`:::
Match open indices and data streams.

`closed`:::
Match closed indices and data streams.

`hidden`:::
Match hidden data streams and indices. Must be combined with `open`, `closed`,
or both.

`none`:::
Don't expand wildcard patterns.

`ignore_unavailable`::
(Optional, Boolean)
If `false`, the snapshot fails if any data stream or index in `indices` is
missing. If `true`, the snapshot ignores missing data
streams and indices. Defaults to `false`.

`include_global_state`::
(Optional, Boolean)
If `true`, include the cluster state in the snapshot. Defaults to `true`.
The cluster state includes:

* Persistent cluster settings
* Index templates
* Legacy index templates
* Ingest pipelines
* ILM policies
* Stored scripts
* For snapshots taken after 7.12.0, feature states

`indices`::
(Optional, string or array of strings)
Comma-separated list of data streams and indices to include in the snapshot.
Supports multi-target syntax. Defaults to an empty array
(`[]`), which includes all regular data streams and regular indices. To exclude
all data streams and indices, use `-*`.
You can't use this parameter to include or exclude <<system-indices,system
indices or system data streams>> from a snapshot. Use
`feature_states` instead.

`feature_states`::
(Optional, array of strings)
Feature states to include in the snapshot. To get a list of
possible values and their descriptions, use the <<get-features-api,get features
API>>.
If `include_global_state` is `true`, the snapshot includes all feature states by
default. If `include_global_state` is `false`, the snapshot includes no feature
states by default.
Note that specifying an empty array will result in the default behavior. To
exclude all feature states, regardless of the `include_global_state` value,
specify an array with only the value `none` (`["none"]`).

`metadata`::
(Optional, object)
Attaches arbitrary metadata to the snapshot, such as a record of who took the snapshot, why it was taken, or any other useful data. Metadata must be less than 1024 bytes.

`partial`::
(Optional, Boolean)
If `false`, the entire snapshot will fail if one or more indices included in the snapshot do not have all primary shards available. Defaults to `false`.
If `true`, allows taking a partial snapshot of indices with unavailable shards.
:!page-id:

`name`::
(Required, string)
Name automatically assigned to each snapshot created by the policy.
Date math is supported.
To prevent conflicting snapshot names, a UUID is automatically appended to each
snapshot name.

`repository`::
(Required, string)
Repository used to store snapshots created by this policy. This repository must
exist prior to the policy's creation. You can create a repository using the
snapshot repository API.

`retention`::
(Optional, object)
Retention rules used to retain and delete snapshots created by the policy.
**Properties of `retention`**
`expire_after`::
(Optional, time units)
Time period after which a snapshot is considered expired and eligible for
deletion. SLM deletes expired snapshots based on the
`slm.retention_schedule`.

`max_count`::
(Optional, integer)
Maximum number of snapshots to retain, even if the snapshots have not yet
expired. If the number of snapshots in the repository exceeds this limit, the
policy retains the most recent snapshots and deletes older snapshots. This limit
only includes snapshots with a `state` of
`SUCCESS`.

`min_count`::
(Optional, integer)
Minimum number of snapshots to retain, even if the snapshots have expired.

`schedule`::
(Required, Cron syntax or time units)
Periodic or absolute schedule at which the policy creates snapshots. SLM
applies `schedule` changes immediately.
Schedule may be either a Cron schedule or a time unit describing the interval between snapshots.
When using a time unit interval, the first snapshot is scheduled one interval after the policy modification time, and then again every interval after.

#### Examples

##### Create a policy

Create a `daily-snapshots` lifecycle policy:

```console
PUT /_slm/policy/daily-snapshots
{
  "schedule": "0 30 1 * * ?", <1>
  "name": "<daily-snap-{now/d}>", <2>
  "repository": "my_repository", <3>
  "config": { <4>
    "indices": ["data-*", "important"], <5>
    "ignore_unavailable": false,
    "include_global_state": false
  },
  "retention": { <6>
    "expire_after": "30d", <7>
    "min_count": 5, <8>
    "max_count": 50 <9>
  }
}
```

<1> When the snapshot should be taken, in this case, 1:30am daily
<2> The name each snapshot should be given
<3> Which repository to take the snapshot in
<4> Any extra snapshot configuration
<5> Data streams and indices the snapshot should contain
<6> Optional retention configuration
<7> Keep snapshots for 30 days
<8> Always keep at least 5 successful snapshots, even if they're more than 30 days old
<9> Keep no more than 50 successful snapshots, even if they're less than 30 days old

##### Use Interval Scheduling

Create an `hourly-snapshots` lifecycle policy using interval scheduling:

```console
PUT /_slm/policy/hourly-snapshots
{
  "schedule": "1h",
  "name": "<hourly-snap-{now/d}>",
  "repository": "my_repository",
  "config": {
    "indices": ["data-*", "important"]
  }
}
```
Creates a snapshot once every hour. The first snapshot will be created one hour after the policy is modified,
with subsequent snapshots being created every hour afterward.
