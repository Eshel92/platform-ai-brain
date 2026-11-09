<!-- Converted from reference/required-access-mongodb-agent.txt (reStructuredText). Includes are inlined. -->

# Required Access for MongoDB Agent

If your MongoDB deployment enforces access control, the Ops Manager
MongoDB Agent must authenticate to MongoDB as a
user with the proper access.

**Note:**

The instructions on this page are for deployments that do not use Automation. If you use Automation, Ops Manager manages authentication for you and the following instructions do not apply.

To authenticate, create a user with the appropriate roles in MongoDB.
The following tutorials include instructions and examples for creating
the MongoDB Agent user in your MongoDB deployment:

- /tutorial/configure-mongodb-agent-for-scram.

- /tutorial/configure-mongodb-agent-for-ldap.

- /tutorial/configure-mongodb-agent-for-kerberos.

- /tutorial/configure-mongodb-agent-for-x509.

MongoDB user roles are separate from Ops Manager
user roles. These roles and their
privileges are described in the MongoDB manual beginning with the
Authorization page.

## Considerations

To authenticate to sharded clusters, create shard-local users on *each*
shard *and* create cluster-wide users:

- Create shard-local users by connecting directly to the replica set
  for each shard.

- Create cluster-wide users while connected to the `mongos`: these
  credentials persist to the config servers.

**Important:**

Every `mongod` and `mongos` process in your Ops Manager deployment
must use the same username and roles for the MongoDB Agent user.

## Automation

Connect to the `mongod` or `mongos` instance as a user with access to
create database users.
See db.createUser() method
page in the MongoDB Manual.

To automate MongoDB instances, the MongoDB Agent must authenticate
on the `admin` database as a MongoDB user with the following roles:

- `clusterAdmin`
- `readWriteAnyDatabase`
- `userAdminAnyDatabase`
- `dbAdminAnyDatabase`
- `backup`
- `restore`

For sharded clusters, the MongoDB Agent also requires:

- `directShardOperations`

You must specify the `directShardOperations` role for sharded cluster
automation. This role allows the automation agent to perform maintenance
operations that require direct access to shards, such as adding shards to
existing clusters. For non-sharded deployments (standalone or replica sets),
you can omit this role.

## Backup

To backup MongoDB instances, the MongoDB Agent must authenticate on the
listed database as a MongoDB user with the required roles.

* - MongoDB Database Version
  - MongoDB FCV (Feature Compatibility Version)
  - Required Role
  - Database
* - 4.2.x or later
  - 4.2 or later
  - `clusterAdmin`
  - `admin`
* - 3.0.0 through 4.2.x
  - 4.0 or earlier
  - `backup`
  - `admin`
* - 2.6.x
  - 
  - 
    - `clusterAdmin`
    - `readAnyDatabase`
    - `userAdminAnyDatabase`
    - `readWrite`
  - `admin`
* - 2.6.x
  - 
  - `readWrite`
  - `local`

## Monitoring

To monitor MongoDB instances, the MongoDB Agent must authenticate on the
`admin` database as a MongoDB user with the
`clusterMonitor` role.

Monitoring includes gathering `dbStats` and
database profiling information.

## Authentication Mechanisms

To authenticate, create the user in MongoDB with the appropriate
access. The authentication method that the MongoDB deployment uses
determines which options to set when creating the user as well as
determining any additional MongoDB Agent configuration:

- For SCRAM authentication, see
  /tutorial/configure-mongodb-agent-for-scram.

- For LDAP authentication, see
  /tutorial/configure-mongodb-agent-for-ldap.

- For Kerberos authentication, see
  /tutorial/configure-mongodb-agent-for-kerberos.

- For X.509 authentication, see
  /tutorial/configure-mongodb-agent-for-x509.
