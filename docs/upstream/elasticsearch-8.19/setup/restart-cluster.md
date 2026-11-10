<!-- Converted from setup/restart-cluster.asciidoc (AsciiDoc). Includes are inlined. -->

## Full-cluster restart and rolling restart

There may be <<security-basic-setup,situations where you want
to perform a full-cluster restart>> or a rolling restart. In the case of
full-cluster restart, you shut down and restart all the
nodes in the cluster while in the case of
rolling restart, you shut down only one node at a
time, so the service remains uninterrupted.

**Warning:**
Nodes exceeding the low watermark threshold will be slow to restart. Reduce the disk
usage below the low watermark before restarting nodes.

### Full-cluster restart

. *Disable shard allocation.*

When you shut down a data node, the allocation process waits for
`index.unassigned.node_left.delayed_timeout` (by default, one minute) before
starting to replicate the shards on that node to other nodes in the cluster,
which can involve a lot of I/O. Since the node is shortly going to be
restarted, this I/O is unnecessary. You can avoid racing the clock by
disabling allocation of replicas before
shutting down data nodes:

```console
PUT _cluster/settings
{
  "persistent": {
    "cluster.routing.allocation.enable": "primaries"
  }
}
```

You can also consider gateway settings when restarting 
large clusters to reduce initial strain while nodes are processing 
through discovery. 

. *Stop indexing and perform a flush.*
Performing a flush speeds up shard recovery.

```console
POST /_flush
```

. *Temporarily stop the tasks associated with active machine learning jobs and datafeeds.* (Optional)
Machine learning features require specific {subscriptions}[subscriptions].

You have two options to handle machine learning jobs and datafeeds when you shut down a
cluster:

* Temporarily halt the tasks associated with your machine learning jobs and datafeeds and
prevent new jobs from opening by using the
set upgrade mode API:
```console
POST _ml/set_upgrade_mode?enabled=true
```
When you disable upgrade mode, the jobs resume using the last model state that
was automatically saved. This option avoids the overhead of managing active jobs
during the shutdown and is faster than explicitly stopping datafeeds and closing
jobs.

* {ml-docs}/stopping-ml.html[Stop all datafeeds and close all jobs]. This option
saves the model state at the time of closure. When you reopen the jobs after the
cluster restart, they use the exact same model. However, saving the latest model
state takes longer than using upgrade mode, especially if you have a lot of jobs
or jobs with large model states.

. *Shut down all nodes.*
* If you are running Elasticsearch with `systemd`:
```sh
sudo systemctl stop elasticsearch.service
```

* If you are running Elasticsearch with SysV `init`:
```sh
sudo -i service elasticsearch stop
```

* If you are running Elasticsearch as a daemon:
```sh
kill $(cat pid)
```

. *Perform any needed changes.*

. *Restart nodes.*
If you have dedicated master nodes, start them first and wait for them to
form a cluster and elect a master before proceeding with your data nodes.
You can check progress by looking at the logs.

As soon as enough master-eligible nodes have discovered each other, they form a
cluster and elect a master. At that point, you can use
the cat health and cat nodes APIs to monitor nodes
joining the cluster:

```console
GET _cat/health

GET _cat/nodes
```

The `status` column returned by `_cat/health` shows the health of each node
in the cluster: `red`, `yellow`, or `green`.

. *Wait for all nodes to join the cluster and report a status of yellow.*
When a node joins the cluster, it begins to recover any primary shards that
are stored locally. The `_cat/health` API initially reports
a `status` of `red`, indicating that not all primary shards have been allocated.

Once a node recovers its local shards, the cluster `status` switches to
`yellow`, indicating that all primary shards have been recovered, but not all
replica shards are allocated. This is to be expected because you have not yet
re-enabled allocation. Delaying the allocation of replicas until all nodes
are `yellow` allows the master to allocate replicas to nodes that
already have local shard copies.

. *Re-enable allocation.*
When all nodes have joined the cluster and recovered their primary shards,
re-enable allocation by restoring `cluster.routing.allocation.enable` to its
default:

```console
PUT _cluster/settings
{
  "persistent": {
    "cluster.routing.allocation.enable": null
  }
}
```

Once allocation is re-enabled, the cluster starts allocating replica shards to
the data nodes. At this point it is safe to resume indexing and searching,
but your cluster will recover more quickly if you can wait until all primary
and replica shards have been successfully allocated and the status of all nodes
is `green`.

You can monitor progress with the `_cat/health` and
`_cat/recovery` APIs:

```console
GET _cat/health

GET _cat/recovery
```
. *Restart machine learning jobs.* (Optional)
If you temporarily halted the tasks associated with your machine learning jobs, use the
set upgrade mode API to return them to active states:

```console
POST _ml/set_upgrade_mode?enabled=false
```

If you closed all machine learning jobs before stopping the nodes, open the jobs and start
the datafeeds from Kibana or with the open jobs and
start datafeed APIs.

### Rolling restart

. *Disable shard allocation.*

When you shut down a data node, the allocation process waits for
`index.unassigned.node_left.delayed_timeout` (by default, one minute) before
starting to replicate the shards on that node to other nodes in the cluster,
which can involve a lot of I/O. Since the node is shortly going to be
restarted, this I/O is unnecessary. You can avoid racing the clock by
disabling allocation of replicas before
shutting down data nodes:

```console
PUT _cluster/settings
{
  "persistent": {
    "cluster.routing.allocation.enable": "primaries"
  }
}
```

You can also consider gateway settings when restarting 
large clusters to reduce initial strain while nodes are processing 
through discovery. 
. *Stop non-essential indexing and perform a flush.* (Optional)
While you can continue indexing during the rolling restart, shard recovery
can be faster if you temporarily stop non-essential indexing and perform a
flush.

```console
POST /_flush
```

. *Temporarily stop the tasks associated with active machine learning jobs and datafeeds.* (Optional)
Machine learning features require specific {subscriptions}[subscriptions].

You have two options to handle machine learning jobs and datafeeds when you shut down a
cluster:

* Temporarily halt the tasks associated with your machine learning jobs and datafeeds and
prevent new jobs from opening by using the
set upgrade mode API:
```console
POST _ml/set_upgrade_mode?enabled=true
```
When you disable upgrade mode, the jobs resume using the last model state that
was automatically saved. This option avoids the overhead of managing active jobs
during the shutdown and is faster than explicitly stopping datafeeds and closing
jobs.

* {ml-docs}/stopping-ml.html[Stop all datafeeds and close all jobs]. This option
saves the model state at the time of closure. When you reopen the jobs after the
cluster restart, they use the exact same model. However, saving the latest model
state takes longer than using upgrade mode, especially if you have a lot of jobs
or jobs with large model states.
* If you perform a rolling restart, you can also leave your machine learning
jobs running. When you shut down a machine learning node, its jobs automatically
move to another node and restore the model states. This option enables your jobs
to continue running during the shutdown but it puts increased load on the
cluster.

. *Shut down a single node in case of rolling restart.*
* If you are running Elasticsearch with `systemd`:
```sh
sudo systemctl stop elasticsearch.service
```

* If you are running Elasticsearch with SysV `init`:
```sh
sudo -i service elasticsearch stop
```

* If you are running Elasticsearch as a daemon:
```sh
kill $(cat pid)
```

. *Perform any needed changes.*

. *Restart the node you changed.*
Start the node and confirm that it joins the cluster by checking the log file or
by submitting a `_cat/nodes` request:

```console
GET _cat/nodes
```

. *Reenable shard allocation.*
For data nodes, once the node has joined the cluster, remove the
`cluster.routing.allocation.enable` setting to enable shard allocation and start
using the node:

```console
PUT _cluster/settings
{
  "persistent": {
    "cluster.routing.allocation.enable": null
  }
}
```

. *Repeat in case of rolling restart.*
When the node has recovered and the cluster is stable, repeat these steps
for each node that needs to be changed.

. *Restart machine learning jobs.* (Optional)
If you temporarily halted the tasks associated with your machine learning jobs, use the
set upgrade mode API to return them to active states:

```console
POST _ml/set_upgrade_mode?enabled=false
```

If you closed all machine learning jobs before stopping the nodes, open the jobs and start
the datafeeds from Kibana or with the open jobs and
start datafeed APIs.
