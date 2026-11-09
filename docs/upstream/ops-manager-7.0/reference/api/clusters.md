<!-- Converted from reference/api/clusters.txt (reStructuredText). Includes are inlined. -->

# Clusters

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

MongoDB supports two types of clusters: replica sets and sharded clusters.
A sharded cluster can contain replica sets within it: each shard can be a
replica set and the config server can also be a replica set. These
relationships are reflected in the way Ops Manager models clusters, and it
might lead to unexpected results from the `clusters` resource. 

**Example:**

Consider a deployment with one sharded cluster containing four
shards, and each shard is a three-node replica set. 

In this scenario, the `clusters` resource will return five
entities: 

- One that represents the sharded cluster, and 
- Four that represent the replica sets (shards). 

However, if each shard in this fictitious deployment were a
standalone mongod instead of a replica set, then the
`clusters` resource returns only one entity representing the
sharded cluster.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following endpoints are available for `clusters`.

| Method | Endpoint | Description |
|---|---|---|
| GET | /clusters | Get details for all clusters in all projects available to the programmatic key making the request. |
| GET | /groups/{PROJECT-ID}/clusters | Retrieve details for all clusters in one project. |
| GET | /groups/{PROJECT-ID}/clusters/{CLUSTER-ID} | Retrieve details for one cluster in one project. |
| PATCH | /groups/{PROJECT-ID}/clusters/{CLUSTER-ID} | Update one cluster in one project. |
