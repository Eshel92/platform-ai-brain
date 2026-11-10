<!-- Converted from security/authentication/remote-clusters-privileges-api-key.asciidoc (AsciiDoc). Includes are inlined. -->

### Configure roles and users

To use a remote cluster for cross-cluster replication or cross-cluster search, you need to create user roles with
remote indices privileges or
remote cluster privileges on the local cluster.

You can manage users and roles from Stack Management in Kibana by selecting
*Security > Roles* from the side navigation. You can also use the
role management APIs to add, update, remove, and retrieve
roles dynamically.

The following examples use the security-api-put-role API. You must have at
least the `manage_security` cluster privilege to use this API.

**Note:** The cross-cluster API key used by the local cluster to connect the remote
cluster must have sufficient privileges to cover all remote indices privileges
required by individual users.

#### Configure privileges for cross-cluster replication

Assuming the remote cluster is connected under the name of `my_remote_cluster`,
the following request creates a role called `remote-replication` on the local
cluster that allows replicating the remote `leader-index` index:

```console
POST /_security/role/remote-replication
{
  "cluster": [
    "manage_ccr"
  ],
  "remote_indices": [
    {
      "clusters": [ "my_remote_cluster" ],
      "names": [
        "leader-index"
      ],
      "privileges": [
        "cross_cluster_replication"
      ]
    }
  ]
}
```

After creating the local `remote-replication` role, use the
security-api-put-user API to create a user on the local cluster cluster and
assign the `remote-replication` role. For example, the following request assigns
the `remote-replication` role to a user named `cross-cluster-user`:

```console
POST /_security/user/cross-cluster-user
{
  "password" : "l0ng-r4nd0m-p@ssw0rd",
  "roles" : [ "remote-replication" ]
}
```

Note that you only need to create this user on the local cluster.

#### Configure privileges for cross-cluster search

Assuming the remote cluster is connected under the name of `my_remote_cluster`,
the following request creates a `remote-search` role on the local cluster that
allows searching the remote `target-index` index:

```console
POST /_security/role/remote-search
{
  "remote_indices": [
    {
      "clusters": [ "my_remote_cluster" ],
      "names": [
        "target-index"
      ],
      "privileges": [
        "read",
        "read_cross_cluster",
        "view_index_metadata"
      ]
    }
  ]
}

```

After creating the `remote-search` role, use the security-api-put-user API
to create a user on the local cluster and assign the `remote-search` role. For
example, the following request assigns the `remote-search` role to a user named
`cross-search-user`:

```console
POST /_security/user/cross-search-user
{
  "password" : "l0ng-r4nd0m-p@ssw0rd",
  "roles" : [ "remote-search" ]
}
```

Note that you only need to create this user on the local cluster.
