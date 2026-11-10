<!-- Converted from snapshot-restore/take-snapshot.asciidoc (AsciiDoc). Includes are inlined. -->

## Create a snapshot

This guide shows you how to take snapshots of a running cluster. You can later
restore a snapshot to recover or transfer its
data.

In this guide, you’ll learn how to:

* Automate snapshot creation and retention with snapshot lifecycle management (SLM)
* Manually take a snapshot
* Monitor a snapshot's progress
* Delete or cancel a snapshot
* Back up cluster configuration files

The guide also provides tips for creating dedicated cluster state snapshots and
taking snapshots at different time intervals.

### Prerequisites

* To use Kibana's **Snapshot and Restore** feature, you must have the following
permissions:

** Cluster privileges: `monitor`, `manage_slm`,
`cluster:admin/snapshot`, and `cluster:admin/repository`

** Index privilege: `all` on the `monitor` index
* You can only take a snapshot from a running cluster with an elected
master node.

* A snapshot repository must be registered and
available to the cluster.

* The cluster's global metadata must be readable. To include an index in a
snapshot, the index and its metadata must also be readable. Ensure there aren't
any cluster blocks or <<index-modules-blocks,index
blocks>> that prevent read access.

### Considerations

* Each snapshot must have a unique name within its repository. Attempts to
create a snapshot with the same name as an existing snapshot will fail.

* Snapshots are automatically deduplicated. You can take frequent snapshots with
little impact to your storage overhead.

* Each snapshot is logically independent. You can delete a snapshot without
affecting other snapshots.

* Taking a snapshot can temporarily pause shard allocations.
See snapshots-shard-allocation.

* Taking a snapshot doesn't block indexing or other requests. However, the
snapshot won't include changes made after the snapshot process starts.

* You can take multiple snapshots at the same time. The
`snapshot.max_concurrent_operations` cluster
setting limits the maximum number of concurrent snapshot operations.

* If you include a data stream in a snapshot, the snapshot also includes the
stream’s backing indices and metadata.
You can also include only specific backing indices in a snapshot. However, the
snapshot won't include the data stream’s metadata or its other backing indices.

* A snapshot can include a data stream but exclude specific backing indices.
When you restore such a data stream, it will contain only backing indices in the
snapshot. If the stream’s original write index is not in the snapshot, the most
recent backing index from the snapshot becomes the stream’s write index.

### Automate snapshots with SLM

Snapshot lifecycle management (SLM) is the easiest way to regularly back up a cluster. An
SLM policy automatically takes snapshots on a preset schedule. The policy
can also delete snapshots based on retention rules you define.

**Tip:** Elasticsearch Service deployments automatically include the `cloud-snapshot-policy`
SLM policy. Elasticsearch Service uses this policy to take periodic snapshots of your
cluster. For more information, see the {cloud}/ec-snapshot-restore.html[Elasticsearch Service
snapshot documentation].

#### SLM security

The following cluster privileges control access to
the SLM actions when Elasticsearch security features are enabled:

`manage_slm`::
Allows a user to perform all SLM actions, including
creating and updating policies and starting and stopping SLM.

`read_slm`::
Allows a user to perform all read-only SLM actions, such as getting
policies and checking the SLM status.

`cluster:admin/snapshot/*`::
Allows a user to take and delete snapshots of any index, whether or not they
have access to that index.

You can create and manage roles to assign these privileges through Kibana
Management.

To grant the privileges necessary to create and manage SLM policies and
snapshots, you can set up a role with the `manage_slm` and
`cluster:admin/snapshot/*` cluster privileges and full access to the SLM
history indices.

For example, the following request creates an `slm-admin` role:

```console
POST _security/role/slm-admin
{
  "cluster": [ "manage_slm", "cluster:admin/snapshot/*" ],
  "indices": [
    {
      "names": [ ".slm-history-*" ],
      "privileges": [ "all" ]
    }
  ]
}
```

To grant read-only access to SLM policies and the snapshot history,
you can set up a role with the `read_slm` cluster privilege and read access
to the snapshot lifecycle management history indices.

For example, the following request creates a `slm-read-only` role:

```console
POST _security/role/slm-read-only
{
  "cluster": [ "read_slm" ],
  "indices": [
    {
      "names": [ ".slm-history-*" ],
      "privileges": [ "read" ]
    }
  ]
}
```

#### Create an SLM policy

To manage SLM in Kibana, go to the main menu and click **Stack
Management** > **Snapshot and Restore** > **Policies**. To create a policy,
click **Create policy**.

You can also manage SLM using the
SLM APIs. To create a policy, use
the create SLM policy API.

The following request creates a policy that backs up the cluster state, all data
streams, and all indices daily at 1:30 a.m. UTC.

```console
PUT _slm/policy/nightly-snapshots
{
  "schedule": "0 30 1 * * ?",       <1>
  "name": "<nightly-snap-{now/d}>", <2>
  "repository": "my_repository",    <3>
  "config": {
    "indices": "*",                 <4>
    "include_global_state": true    <5>
  },
  "retention": {                    <6>
    "expire_after": "30d",
    "min_count": 5,
    "max_count": 50
  }
}
```

<1> When to take snapshots, written in Cron syntax.
<2> Snapshot name. Supports date math. To prevent
    naming conflicts, the policy also appends a UUID to each snapshot name.
<3> Registered snapshot repository used to
    store the policy's snapshots.
<4> Data streams and indices to include in the policy's snapshots.
<5> If `true`, the policy's snapshots include the cluster state. This also
    includes all feature states by default. To only include specific feature
    states, see back-up-specific-feature-state.
<6> Optional retention rules. This configuration keeps snapshots for 30 days,
    retaining at least 5 and no more than 50 snapshots regardless of age. See
    slm-retention-task and snapshot-retention-limits.

#### Manually run an SLM policy

You can manually run an SLM policy to immediately create a snapshot. This
is useful for testing a new policy or taking a snapshot before an upgrade.
Manually running a policy doesn't affect its snapshot schedule.

To run a policy in Kibana, go to the **Policies** page and click the run icon
under the **Actions** column. You can also use the
execute SLM policy API.

```console
POST _slm/policy/nightly-snapshots/_execute
```

The snapshot process runs in the background. To monitor its progress, see
monitor-snapshot.

#### SLM retention

SLM snapshot retention is a cluster-level task that runs separately from
a policy's snapshot schedule. To control when the SLM retention task
runs, configure the `slm.retention_schedule` cluster
setting.

```console
PUT _cluster/settings
{
  "persistent" : {
    "slm.retention_schedule" : "0 30 1 * * ?"
  }
}
```

To immediately run the retention task, use the
execute SLM retention policy API.

```console
POST _slm/_execute_retention
```

An SLM policy's retention rules only apply to snapshots created using the
policy. Other snapshots don't count toward the policy's retention limits.

#### Snapshot retention limits

We recommend you include retention rules in your SLM policy to delete
snapshots you no longer need.

A snapshot repository can safely scale to thousands of snapshots. However, to
manage its metadata, a large repository requires more memory on the master node.
Retention rules ensure a repository's metadata doesn't grow to a size that could
destabilize the master node.

### Manually create a snapshot

To take a snapshot without an SLM policy, use the
create snapshot API. The snapshot name supports
date math.

```console
# PUT _snapshot/my_repository/<my_snapshot_{now/d}>
PUT _snapshot/my_repository/%3Cmy_snapshot_%7Bnow%2Fd%7D%3E
```

Depending on its size, a snapshot can take a while to complete. By default,
the create snapshot API only initiates the snapshot process, which runs in the
background. To block the client until the snapshot finishes, set the
`wait_for_completion` query parameter to `true`.

```console
PUT _snapshot/my_repository/my_snapshot?wait_for_completion=true
```

You can also clone an existing snapshot using <<clone-snapshot-api,clone
snapshot API>>.

### Monitor a snapshot

To monitor any currently running snapshots, use the <<get-snapshot-api,get
snapshot API>> with the `_current` request path parameter.

```console
GET _snapshot/my_repository/_current
```

To get a complete breakdown of each shard participating in any currently running
snapshots, use the get snapshot status API.

```console
GET _snapshot/_status
```

#### Check SLM history

To get more information about a cluster's SLM execution history,
including stats for each SLM policy, use the <<slm-api-get-stats,get
SLM stats API>>. The API also returns information about the cluster's
snapshot retention task history.

```console
GET _slm/stats
```

To get information about a specific SLM policy's execution history, use
the get SLM policy API. The response includes:

* The next scheduled policy execution.
* The last time the policy successfully started the snapshot process, if
  applicable. A successful start doesn't guarantee the snapshot completed.
* The last time policy execution failed, if applicable, and the associated
  error.

```console
GET _slm/policy/nightly-snapshots
```

### Delete or cancel a snapshot

To delete a snapshot in Kibana, go to the **Snapshots** page and click the trash
icon under the **Actions** column. You can also use the
delete snapshot API.

```console
DELETE _snapshot/my_repository/my_snapshot_2099.05.06
```

If you delete a snapshot that's in progress, Elasticsearch cancels it. The snapshot
process halts and deletes any files created for the snapshot. Deleting a
snapshot doesn't delete files used by other snapshots.

### Back up configuration files

If you run Elasticsearch on your own hardware, we recommend that, in addition to backups,
you take regular backups of the files in each node's
`$ES_PATH_CONF` directory using the file backup software
of your choice. Snapshots don't back up these files. Also note that these files will
differ on each node, so each node's files should be backed up individually.

**Important:** The `elasticsearch.keystore`, TLS keys, and SAML,
OIDC, and Kerberos
realms private key files contain sensitive information. Consider encrypting
your backups of these files.

### Back up a specific feature state

By default, a snapshot that includes the cluster state also includes all
feature states. Similarly, a snapshot that excludes the
cluster state excludes all feature states by default.

You can also configure a snapshot to only include specific feature states,
regardless of the cluster state.

To get a list of available features, use the <<get-features-api,get features
API>>.

```console
GET _features
```

The API returns:

```console-result
{
  "features": [
    {
      "name": "tasks",
      "description": "Manages task results"
    },
    {
      "name": "kibana",
      "description": "Manages Kibana configuration and reports"
    },
    {
      "name": "security",
      "description": "Manages configuration for Security features, such as users and roles"
    },
    ...
  ]
}
```

To include a specific feature state in a snapshot, specify the feature `name` in
the `feature_states` array.

For example, the following SLM policy only includes feature states for
the Kibana and Elasticsearch security features in its snapshots.

```console
PUT _slm/policy/nightly-snapshots
{
  "schedule": "0 30 2 * * ?",
  "name": "<nightly-snap-{now/d}>",
  "repository": "my_repository",
  "config": {
    "indices": "*",
    "include_global_state": true,
    "feature_states": [
      "kibana",
      "security"
    ]
  },
  "retention": {
    "expire_after": "30d",
    "min_count": 5,
    "max_count": 50
  }
}
```

Any index or data stream that's part of the feature state will display in a
snapshot's contents. For example, if you back up the `security` feature state,
the `security-*` system indices display in the <<get-snapshot-api,get snapshot
API>>'s response under both `indices` and `feature_states`.

### Dedicated cluster state snapshots

Some feature states contain sensitive data. For example, the `security` feature
state includes system indices that may contain user names and encrypted password
hashes. Because passwords are stored using cryptographic hashes,
the disclosure of a snapshot would not automatically enable a third party to
authenticate as one of your users or use API keys. However, it would disclose
confidential information, and if a third party can modify snapshots, they could
install a back door.

To better protect this data, consider creating a dedicated repository and
SLM policy for snapshots of the cluster state. This lets you strictly
limit and audit access to the repository.

For example, the following SLM policy only backs up the cluster state.
The policy stores these snapshots in a dedicated repository.

```console
PUT _slm/policy/nightly-cluster-state-snapshots
{
  "schedule": "0 30 2 * * ?",
  "name": "<nightly-cluster-state-snap-{now/d}>",
  "repository": "my_secure_repository",
  "config": {
    "include_global_state": true,                 <1>
    "indices": "-*"                               <2>
  },
  "retention": {
    "expire_after": "30d",
    "min_count": 5,
    "max_count": 50
  }
}
```

<1> Includes the cluster state. This also includes all feature states by
    default.
<2> Excludes regular data streams and indices.

If you take dedicated snapshots of the cluster state, you'll need to exclude the
cluster state from your other snapshots. For example:

```console
PUT _slm/policy/nightly-snapshots
{
  "schedule": "0 30 2 * * ?",
  "name": "<nightly-snap-{now/d}>",
  "repository": "my_repository",
  "config": {
    "include_global_state": false,    <1>
    "indices": "*"                    <2>
  },
  "retention": {
    "expire_after": "30d",
    "min_count": 5,
    "max_count": 50
  }
}
```

<1> Excludes the cluster state. This also excludes all feature states by
    default.
<2> Includes all regular data streams and indices.

### Create snapshots at different time intervals

If you only use a single SLM policy, it can be difficult to take frequent
snapshots and retain snapshots with longer time intervals.

For example, a policy that takes snapshots every 30 minutes with a maximum of
100 snapshots will only keep snapshots for approximately two days. While this
setup is great for backing up recent changes, it doesn't let you restore data
from a previous week or month.

To fix this, you can create multiple SLM policies with the same snapshot
repository that run on different schedules. Since a policy's retention rules
only apply to its snapshots, a policy won't delete a snapshot created by another
policy.

For example, the following SLM policy takes hourly snapshots with a
maximum of 24 snapshots. The policy keeps its snapshots for one day.

```console
PUT _slm/policy/hourly-snapshots
{
  "name": "<hourly-snapshot-{now/d}>",
  "schedule": "0 0 * * * ?",
  "repository": "my_repository",
  "config": {
    "indices": "*",
    "include_global_state": true
  },
  "retention": {
    "expire_after": "1d",
    "min_count": 1,
    "max_count": 24
  }
}
```

The following policy takes nightly snapshots in the same snapshot repository.
The policy keeps its snapshots for one month.

```console
PUT _slm/policy/daily-snapshots
{
  "name": "<daily-snapshot-{now/d}>",
  "schedule": "0 45 23 * * ?",          <1>
  "repository": "my_repository",
  "config": {
    "indices": "*",
    "include_global_state": true
  },
  "retention": {
    "expire_after": "30d",
    "min_count": 1,
    "max_count": 31
  }
}
```

<1> Runs at 11:45 p.m. UTC every day.

The following policy creates monthly snapshots in the same repository. The
policy keeps its snapshots for one year.

```console
PUT _slm/policy/monthly-snapshots
{
  "name": "<monthly-snapshot-{now/d}>",
  "schedule": "0 56 23 1 * ?",            <1>
  "repository": "my_repository",
  "config": {
    "indices": "*",
    "include_global_state": true
  },
  "retention": {
    "expire_after": "366d",
    "min_count": 1,
    "max_count": 12
  }
}
```

<1> Runs on the first of the month at 11:56 p.m. UTC.
