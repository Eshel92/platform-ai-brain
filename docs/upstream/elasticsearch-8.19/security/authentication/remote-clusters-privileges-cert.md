<!-- Converted from security/authentication/remote-clusters-privileges-cert.asciidoc (AsciiDoc). Includes are inlined. -->

### Configure roles and users for remote clusters

After connecting remote clusters, you create a
user role on both the local and remote clusters and assign necessary privileges.
These roles are required to use cross-cluster replication and cross-cluster search.

**Important:** You must use the same role names on both the local
and remote clusters. For example, the following configuration for cross-cluster replication uses the
`remote-replication` role name on both the local and remote clusters. However,
you can specify different role definitions on each cluster.

You can manage users and roles from Stack Management in Kibana by selecting
*Security > Roles* from the side navigation. You can also use the
role management APIs to add, update, remove, and
retrieve roles dynamically. When you use the APIs to manage roles in the
`native` realm, the roles are stored in an internal Elasticsearch index.

The following requests use the
create or update roles API. You must have at least the
`manage_security` cluster privilege to use this API.

#### Configure privileges for cross-cluster replication

The cross-cluster replication user requires different cluster and index privileges on the remote
cluster and local cluster. Use the following requests to create separate roles
on the local and remote clusters, and then create a user with the required
roles.

##### Remote cluster

On the remote cluster that contains the leader index, the cross-cluster replication role requires
the `read_ccr` cluster privilege, and `monitor` and `read` privileges on the
leader index.

**Note:** If requests are authenticated with an API key, the API key
requires the above privileges on the **local** cluster, instead of the remote.

**Note:** If requests are issued on behalf of other users,
then the authenticating user must have the `run_as` privilege on the remote
cluster.

The following request creates a `remote-replication` role on the remote cluster:

```console
POST /_security/role/remote-replication
{
  "cluster": [
    "read_ccr"
  ],
  "indices": [
    {
      "names": [
        "leader-index-name"
      ],
      "privileges": [
        "monitor",
        "read"
      ]
    }
  ]
}
```

##### Local cluster

On the local cluster that contains the follower index, the `remote-replication`
role requires the `manage_ccr` cluster privilege, and `monitor`, `read`, `write`,
and `manage_follow_index` privileges on the follower index.

The following request creates a `remote-replication` role on the local cluster:

```console
POST /_security/role/remote-replication
{
  "cluster": [
    "manage_ccr"
  ],
  "indices": [
    {
      "names": [
        "follower-index-name"
      ],
      "privileges": [
        "monitor",
        "read",
        "write",
        "manage_follow_index"
      ]
    }
  ]
}
```

After creating the `remote-replication` role on each cluster, use the
create or update users API to create a user on
the local cluster cluster and assign the `remote-replication` role. For
example, the following request assigns the `remote-replication` role to a user
named `cross-cluster-user`:

```console
POST /_security/user/cross-cluster-user
{
  "password" : "l0ng-r4nd0m-p@ssw0rd",
  "roles" : [ "remote-replication" ]
}
```

**Note:** You only need to create this user on the *local* cluster.

You can then configure cross-cluster replication to replicate your
data across datacenters.

#### Configure privileges for cross-cluster search

The cross-cluster search user requires different cluster and index privileges on the remote
cluster and local cluster. The following requests create separate roles on the
local and remote clusters, and then create a user with the required roles.

##### Remote cluster

On the remote cluster, the cross-cluster search role requires the `read` and
`read_cross_cluster` privileges for the target indices.

**Note:** If requests are authenticated with an API key, the API key
requires the above privileges on the **local** cluster, instead of the remote.

**Note:** If requests are issued on behalf of other users,
then the authenticating user must have the `run_as` privilege on the remote
cluster.

The following request creates a `remote-search` role on the remote cluster:

```console
POST /_security/role/remote-search
{
  "indices": [
    {
      "names": [
        "target-indices"
      ],
      "privileges": [
        "read",
        "read_cross_cluster"
      ]
    }
  ]
}
```

##### Local cluster

On the local cluster, which is the cluster used to initiate cross cluster
search, a user only needs the `remote-search` role. The role privileges can be
empty.

The following request creates a `remote-search` role on the local cluster:

```console
POST /_security/role/remote-search
{}
```

After creating the `remote-search` role on each cluster, use the
create or update users API to create a user on the
local cluster and assign the `remote-search` role. For example, the following
request assigns the `remote-search` role to a user named `cross-search-user`:

```console
POST /_security/user/cross-search-user
{
  "password" : "l0ng-r4nd0m-p@ssw0rd",
  "roles" : [ "remote-search" ]
}
```

**Note:** You only need to create this user on the *local* cluster.

Users with the `remote-search` role can then
search across clusters.

#### Configure privileges for cross-cluster search and Kibana

When using Kibana to search across multiple clusters, a two-step authorization
process determines whether or not the user can access data streams and indices
on a remote cluster:

* First, the local cluster determines if the user is authorized to access remote
clusters. The local cluster is the cluster that Kibana is connected to.
* If the user is authorized, the remote cluster then determines if the user has
access to the specified data streams and indices.

To grant Kibana users access to remote clusters, assign them a local role
with read privileges to indices on the remote clusters. You specify data streams
and indices in a remote cluster as `<remote_cluster_name>:<target>`.

To grant users read access on the remote data streams and indices, you must
create a matching role on the remote clusters that grants the
`read_cross_cluster` privilege with access to the appropriate data streams and
indices.

For example, you might be actively indexing Logstash data on a local cluster and
and periodically offload older time-based indices to an archive on your remote
cluster. You want to search across both clusters, so you must enable Kibana
users on both clusters.

##### Local cluster

On the local cluster, create a `logstash-reader` role that grants
`read` and `view_index_metadata` privileges on the local `logstash-*` indices.

**Note:** If you configure the local cluster as another remote in Elasticsearch, the
`logstash-reader` role on your local cluster also needs to grant the
`read_cross_cluster` privilege.

```console
POST /_security/role/logstash-reader
{
  "indices": [
    {
      "names": [
        "logstash-*"
        ],
        "privileges": [
          "read",
          "view_index_metadata"
          ]
    }
  ]
}
```

Assign your Kibana users a role that grants
[access to Kibana](https://www.elastic.co/guide/en/kibana/8.19/xpack-security-authorization.html), as well as your
`logstash_reader` role. For example, the following request creates the
`cross-cluster-kibana` user and assigns the `kibana-access` and
`logstash-reader` roles.

```console
PUT /_security/user/cross-cluster-kibana
{
  "password" : "l0ng-r4nd0m-p@ssw0rd",
  "roles" : [
    "logstash-reader",
    "kibana-access"
    ]
}
```

##### Remote cluster

On the remote cluster, create a `logstash-reader` role that grants the
`read_cross_cluster` privilege and `read` and `view_index_metadata` privileges
for the `logstash-*` indices.

```console
POST /_security/role/logstash-reader
{
  "indices": [
    {
      "names": [
        "logstash-*"
        ],
        "privileges": [
          "read_cross_cluster",
          "read",
          "view_index_metadata"
          ]
    }
  ]
}
```
