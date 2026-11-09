<!-- Converted from core/localhost-exception.txt (reStructuredText). Includes are inlined. -->

# Localhost Exception in Self-Managed Deployments

**Important:**

On a `mongod` instance, the localhost exception only
applies when there are **no users or roles** created in the MongoDB
instance.

The localhost exception allows you to enable access control and then
create the first user or role in the system. After you enable access
control, connect to the localhost interface and create the first user in
the `admin` database.

If you create a user first, the user must have privileges to create
other users. The `userAdmin` or
`userAdminAnyDatabase` role both confer the privilege to
create other users.

**Warning:**

Connections using the localhost exception have access to create
*only* the **first user or role**.

Once you create any user or role, the localhost exception is
disabled. If you need to create a user and a role, you must create
the user first using one of the builtin `userAdmin` or
`userAdminAnyDatabase` roles. If you create a role first,
you won't be able to create a user.

The ability to create a role first with the `db.createRole()`
method is specifically for users authorizing with LDAP. See LDAP
Authorization for more information.

## Localhost Exception for Sharded Clusters

**Important:**

- On a `mongos`, the localhost exception only applies
  when there are no sharded cluster users
  or roles created.
- In a sharded cluster, the localhost exception applies to each shard
  individually as well as to the cluster as a whole.

Once you create a sharded cluster and add a user administrator through the `mongos` instance, you
**must** still prevent unauthorized access to the individual shards. To
prevent unauthorized access to individual shards, follow one of the
following steps for each shard in your cluster:

- Create a user administrator on the shard's
  primary.
- Disable the localhost exception at startup. To disable the localhost
  exception, set the `enableLocalhostAuthBypass` parameter to
  `0`.
