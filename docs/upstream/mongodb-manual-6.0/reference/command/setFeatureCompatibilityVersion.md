<!-- Converted from reference/command/setFeatureCompatibilityVersion.txt (reStructuredText). Includes are inlined. -->

# setFeatureCompatibilityVersion

## Definition

**`setFeatureCompatibilityVersion`**

Enables or disables the features that persist data incompatible with
earlier versions of MongoDB. You can only issue the
`setFeatureCompatibilityVersion` against the `admin`
database.

**Warning:**

Enabling backwards-incompatible features can complicate the
downgrade process since you must remove any persisted
backwards-incompatible features before you downgrade.

It is recommended that after upgrading, you allow your deployment to
run without enabling backwards-incompatible features for a burn-in period 
to ensure the likelihood of downgrade is minimal. When you are confident 
that the likelihood of downgrade is minimal, enable these features.

## Compatibility

This command is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   {
     setFeatureCompatibilityVersion: <version>,
     writeConcern: { wtimeout: <timeout> }
   } 
)
```

## Command Fields

The possible values for `version` are:

| Version | Description |
|---|---|
| `"6.0"` | *Available on MongoDB 6.0 Deployments* Enables the 6.0 features that persist data incompatible with MongoDB 5.0. |
| `"5.0"` | *Available on MongoDB 5.0 and 6.0 Deployments* Enables the 5.0 features that persist data incompatible with MongoDB 4.4. |

The optional `writeConcern` specifies the write concern
wc-wtimeout value in milliseconds:

- The time period that the primary waits for
  acknowledgment from the majority of the replica set members. If the
  acknowledgment is not received in the time period, the operation
  fails.

- Default is `60000` milliseconds. Use a longer time period if the
  secondary members of the replica set have a delay that exceeds
  the wc-wtimeout default.

**Note:**

- For a standalone, run the command on the standalone
  `mongod` instance.

- For a replica set, run the command on the primary. A majority of the
  data-bearing members must be available.

- For a sharded cluster, run the command on a `mongos`
  instance.

## Behavior

### Conflicts with Background Operations

Certain background operations may prevent
execution of `setFeatureCompatibilityVersion`. Use 
`currentOp` to identify any ongoing operations.

### Sync Failures

If you trigger a `setFeatureCompatibilityVersion` change during an 
initial sync, the sync may fail with an `OplogOperationUnsupported` error
message when replaying entries on the `oplog` application phase. The sync 
following this attempt succeeds because the operation phase no longer replays
the operation.

### Default Values

| Deployments | `featureCompatibilityVersion` |
|---|---|
| For new 6.0 deployments | `"6.0"` |
| For 6.0 deployments upgraded from 5.0 | `"5.0"` until you `setFeatureCompatibilityVersion` to `"6.0"`. |
| For new 5.0 deployments | `"5.0"` |
| For 5.0 deployments upgraded from 4.4 | `"4.4"` until you `setFeatureCompatibilityVersion` to `"5.0"`. |

### Idempotency

This command must perform writes to an internal system collection. If
for any reason the command does not complete successfully, you can
safely retry the command as the operation is idempotent.

### Cluster-to-Cluster Sync and User Write Blocking

Starting in MongoDB 6.0, if you need to downgrade the feature
compatibility version, ensure you disable cluster-to-cluster replication
and user write blocking.

#. If you enabled cluster-to-cluster replication, disable it.

#. If you enabled user write blocking, disable it:

   ```javascript
   db.runCommand( { setUserWriteBlockMode: 1, global: false } )
   ```

#. Wait for the previous command to complete.

#. Downgrade the feature compatibility version using
   `setFeatureCompatibilityVersion`.

For more information on MongoDB Cluster-to-Cluster Sync, see the 
[documentation](https://www.mongodb.com/docs/cluster-to-cluster-sync/current).

### Feature Compatibility in Arbiters

Arbiters do not replicate the `admin.system.version` collection.
Because of this, arbiters always have a feature compatibility version equal
to the downgrade version of the binary, regardless of the FCV value of the
replica set.

For example, an arbiter in a MongoDB 5.0 cluster, has an FCV
value of 4.4.

## Examples

### Get FeatureCompatibilityVersion

To view the `featureCompatibilityVersion` for a `mongod`
instance, run the `getParameter` command on a 
`mongod` instance:

```javascript
db.adminCommand( {
                    getParameter: 1,
                    featureCompatibilityVersion: 1
                 }
               )
```

The output resembles:

```javascript
{
  featureCompatibilityVersion: { version: '5.0' },
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1660318752, i: 5 }),
    signature: {
      hash: Binary(Buffer.from("ce0cff3621e9b089fa6d8e9a1e1efc1a1ff15dab", "hex"), 0),
      keyId: Long("7129893797260951557")
    }
  },
  operationTime: Timestamp({ t: 1660318752, i: 5 })
}
```

**Note:**

The operation is undefined on the `mongos` instances.

On a sharded cluster that has access control enabled, you must
connect to the shard as a shard local user
to run the command.

### Set Feature Compatibility Version on MongoDB 6.0 Deployments

#### Enable 6.0 Backwards Incompatible Features

To enable the 6.0 features that persist data incompatible with
MongoDB 5.0, set the feature compatibility
to `"6.0"` on the MongoDB 6.0 deployment:

**Note:**

Run the `setFeatureCompatibilityVersion` command against
the `admin` database.

- For a standalone, run the command on the standalone
  `mongod` instance.

- For a replica set, run the command on the primary. A majority of the
  data-bearing members must be available.

- For a sharded cluster, run the command on a `mongos`
  instance.

```javascript
db.adminCommand( { setFeatureCompatibilityVersion: "6.0" } )
```

#### Disable 6.0 Backwards Incompatible Features

To disable the 6.0 features that persist data incompatible with
MongoDB 5.0, set the feature compatibility
to `"5.0"` on the MongoDB 6.0 deployment:

**Note:**

Run the `setFeatureCompatibilityVersion` command against
the `admin` database.

- For a standalone, run the command on the standalone
  `mongod` instance.

- For a replica set, run the command on the primary. A majority of the
  data-bearing members must be available.

- For a sharded cluster, run the command on a `mongos`
  instance.

- `"5.0"` featureCompatibilityVersion is supported on MongoDB
  5.0 and MongoDB 6.0 deployments only.

```javascript
db.adminCommand( { setFeatureCompatibilityVersion: "5.0" } )
```

If run as part of the downgrade process from MongoDB 6.0 to MongoDB 
5.0, you must also remove all persisted features that are
incompatible with 5.0. See the
appropriate downgrade procedures.

### Set Feature Compatibility Version on MongoDB 5.0 Deployments

#### Enable 5.0 Backwards Incompatible Features

To enable the 5.0 features that persist data incompatible with
MongoDB 4.4, set the feature compatibility
to `"5.0"` on the MongoDB 5.0 deployment:

**Note:**

Run the `setFeatureCompatibilityVersion` command against
the `admin` database.

- For a standalone, run the command on the standalone
  `mongod` instance.

- For a replica set, run the command on the primary. A majority of the
  data-bearing members must be available.

- For a sharded cluster, run the command on a `mongos`
  instance.

```javascript
db.adminCommand( { setFeatureCompatibilityVersion: "5.0" } )
```

#### Disable 5.0 Backwards Incompatible Features

To disable the 5.0 features that persist data incompatible with
MongoDB 4.4, set the feature compatibility
to `"4.4"` on the MongoDB 5.0 deployment:

**Note:**

Run the `setFeatureCompatibilityVersion` command against
the `admin` database.

- For a standalone, run the command on the standalone
  `mongod` instance.

- For a replica set, run the command on the primary. A majority of the
  data-bearing members must be available.

- For a sharded cluster, run the command on a `mongos`
  instance.

- `"4.4"` featureCompatibilityVersion is supported on MongoDB
  4.4 and MongoDB 5.0 deployments only.

```javascript
db.adminCommand( { setFeatureCompatibilityVersion: "4.4" } )
```

If run as part of the downgrade process from MongoDB 5.0 to MongoDB
4.4, you must also remove all persisted features that are
incompatible with 4.4. See the
appropriate downgrade procedures.

### Set Feature Compatibility Version on MongoDB 4.2 Deployments

#### Enable 4.2 Backwards Incompatible Features

To enable the 4.2 features that persist data incompatible with
MongoDB 4.0, set the feature compatibility
to `"4.2"` on the MongoDB 4.2 deployment:

**Note:**

Run the `setFeatureCompatibilityVersion` command against
the `admin` database.

- For a standalone, run the command on the standalone
  `mongod` instance.

- For a replica set, run the command on the primary. A majority of the
  data-bearing members must be available.

- For a sharded cluster, run the command on a `mongos`
  instance.

```javascript
db.adminCommand( { setFeatureCompatibilityVersion: "4.2" } )
```

### Set Write Concern Timeout

The following example sets the optional write concern wc-wtimeout
field to 5000 (5 seconds).

**Note:**

Run the `setFeatureCompatibilityVersion` command against
the `admin` database.

- For a standalone, run the command on the standalone
  `mongod` instance.

- For a replica set, run the command on the primary. A majority of the
  data-bearing members must be available.

- For a sharded cluster, run the command on a `mongos`
  instance.

```javascript
db.adminCommand( {
   setFeatureCompatibilityVersion: "5.0",
   writeConcern: { wtimeout: 5000 }
} )
```
