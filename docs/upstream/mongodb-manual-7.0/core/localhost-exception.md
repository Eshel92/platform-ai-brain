<!-- Converted from core/localhost-exception.txt (reStructuredText). Includes are inlined. -->

# Localhost Exception in Self-Managed Deployments

**Important:**

On a `mongod` instance, the localhost exception only
applies when there are **no users or roles** created in the MongoDB
instance.

The localhost exception allows you to create the first user or role in the
system after enabling access control. You can also use it to initiate a replica set.

## Initiating a Replica Set

You can use the localhost exception to initiate a replica set, following
the steps in server-replica-set-deploy. You must wait until the replica
set elects a primary before you can add the first user.

## Creating the First User or Role

**Warning:**

Connections using the localhost exception have access to create
*only* the **first user OR role**. Only create a role first if you are
authorizing users with LDAP. See LDAP Authorization for more information.

After you enable access control, connect to the localhost interface and
create the first user in the `admin` database. 
The first user must have privileges to create other users. The
`userAdmin` or `userAdminAnyDatabase` role both confer the
privilege to create other users.

### Localhost Exception for Sharded Clusters

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

## All Localhost Exception Permissions

While the localhost exception applies, you can:

- Run the `createUser` command or `db.createUser()` method.
  This ends the localhost exception.
- Run the `createRole` command or `db.createRole()` method.
  This ends the localhost exception.
- Use the `grantRole` action to grant a role to a user on an 
  external authentication system, such as LDAP.
- Run `replSetInitiate` to initiate a new replica set
- Run `replSetGetStatus` to get the status of the current member's 
  replica set
- Run `replSetReconfig` on the primary member to modify replica set 
  configuration.
- On a `mongos` instance, if the cluster is hosted on
  `localhost`, you can run `addShard` to add a shard to the
  cluster.
