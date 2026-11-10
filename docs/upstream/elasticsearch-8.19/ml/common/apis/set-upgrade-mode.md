<!-- Converted from ml/common/apis/set-upgrade-mode.asciidoc (AsciiDoc). Includes are inlined. -->

# Set upgrade mode API

**New API reference**
For the most up-to-date API details, refer to [Machine learning APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml).

Sets a cluster wide upgrade_mode setting that prepares machine learning indices for an
upgrade. 

## Request

```console
POST /_ml/set_upgrade_mode?enabled=false&timeout=10m
```

`POST _ml/set_upgrade_mode`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

When upgrading your cluster, in some circumstances you must restart your nodes and
reindex your machine learning indices. In those circumstances, there must be no machine learning jobs running. 
You can close the machine learning jobs, do the upgrade, then open all the jobs again. 
Alternatively, you can use this API to temporarily halt tasks associated 
with the jobs and datafeeds and prevent new jobs from opening. You can also use this 
API during upgrades that do not require you to reindex your machine learning indices, 
though stopping jobs is not a requirement in that case.

For more information, see {stack-ref}/upgrading-elastic-stack.html[Upgrading the Elastic Stack].

When `enabled=true` this API temporarily halts all job and datafeed tasks and
prohibits new job and datafeed tasks from starting.

Subsequently, you can call the API with the enabled parameter set to false,
which causes machine learning jobs and datafeeds to return to their desired states.

You can see the current value for the `upgrade_mode` setting by using the
get machine learning info API.

**Important:** No new machine learning jobs can be opened while the `upgrade_mode` setting is
`true`.

## Query parameters

`enabled`::
  (Optional, Boolean) When `true`, this enables `upgrade_mode`. Defaults to
  `false`.

`timeout`::
  (Optional, time) The time to wait for the request to be completed. The default
  value is 30 seconds.

## Examples

The following example enables `upgrade_mode` for the cluster:

```console
POST _ml/set_upgrade_mode?enabled=true&timeout=10m
```

When the call is successful, an acknowledged response is returned. For example:

```console-result
{
  "acknowledged": true
}
```

The acknowledged response will only be returned once all machine learning jobs and datafeeds have
finished writing to the machine learning internal indices. This means it is safe to reindex those
internal indices without causing failures. You must wait for the acknowledged
response before reindexing to ensure that all writes are completed.

When the upgrade is complete, you must set `upgrade_mode` to `false` for
machine learning jobs to start running again. For example:

```console
POST _ml/set_upgrade_mode?enabled=false&timeout=10m
```
