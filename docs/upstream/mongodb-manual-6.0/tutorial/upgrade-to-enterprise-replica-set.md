<!-- Converted from tutorial/upgrade-to-enterprise-replica-set.txt (reStructuredText). Includes are inlined. -->

# Upgrade to MongoDB Enterprise (Replica Set)

MongoDB Enterprise provides various features not available in the
MongoDB Community edition, such as:

- /core/inmemory

- /core/auditing

- /core/kerberos

- /core/security-ldap and /core/security-ldap-external

- /core/security-encryption-at-rest

The following steps outline the procedure to upgrade a replica set from
the MongoDB Community Edition to the MongoDB Enterprise Edition. For
example, the steps can be used to upgrade MongoDB 6.0 Community to
MongoDB 6.0 Enterprise.

## About This Task

### Upgrade Major Releases

**Warning:**

Do not use these instructions to upgrade to another release version.
To upgrade release versions, refer to the appropriate release
upgrade instructions, such as Upgrade to MongoDB 6.0.

### Ops Manager

With `Ops Manager`, you can automatically upgrade
from MongoDB Community Server to MongoDB Enterprise Server.

For more information, see
`Change MongoDB Version`.

### Rolling Upgrades

When updating the replica set manually, you can perform a
rolling upgrade to update each MongoDB Community Server to
Enterprise edition with minimal downtime.

In a rolling upgrade, each secondary is taken down and upgraded.
The Enterprise server then rejoins the replica set as a
secondary. When all secondaries are upgraded, you can
step down the primary, forcing the replica set to elect
one of the Enterprise servers as the new primary. 

## Steps

To minimize downtime, manually upgrade each from MongoDB
Community Server to Enterprise Edition: 

**Step 1: Upgrade the secondaries**

Upgrade each secondary member of the replica set
individually. Finish the upgrade process on one server and
wait until it rejoins the replica set as an Enterprise
server before starting the next.

For the procedure, see Upgrade to MongoDB Enterprise 
Server.

**Step 2: Step down the primary**

When all secondaries in the replica set are up and running
MongoDB Enterprise Server, step down the primary
member. This forces an election, causing an Enterprise
Server to become the new primary member.

To step down the primary member, use the 
`rs.status` method to get the `id`
of the current primary member:

```javascript
rs.status().members.find(m => m.state === 1)._id
```

Output:

```javascript
0
```

Then, force the primary to step down with the
`rs.stepDown` method:

```javascript
rs.stepDown( 120 )
```

This command steps down the primary and makes the server
ineligible as primary for 120 seconds. If no primary is
found after 120 seconds, the server can then be reelected.
For more information, see the `rs.stepDown`
method.

To confirm that the primary member has stepped down and
the replica set has chose a new primary, rerun the
`rs.status` method:

```javascript
rs.status().members.find(m => m.state === 1)._id
```

Output:

```javascript
1
```

**Step 3: Upgrade the primary**

Upgrade the former primary member. When the former
primary starts, it rejoins the replica set as a secondary.

For the procedure, see Upgrade to MongoDB Enterprise 
Server.

**Important:**

Before using any Enterprise features, ensure that all members have
been upgraded to Enterprise edition.
