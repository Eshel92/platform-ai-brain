<!-- Converted from reference/command/setFeatureCompatibilityVersion.txt (reStructuredText). Includes are inlined. -->

# setFeatureCompatibilityVersion (database command)

## Definition

**`setFeatureCompatibilityVersion`**

Enables or disables the features that persist data incompatible with
earlier versions of MongoDB. You can only issue the
`setFeatureCompatibilityVersion` against the `admin`
database.

To learn what the feature compatibility version is and how it supports
downgrades, see versions-and-upgrade-paths.

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

**Changed in version:** 7.0

The command has the following syntax:

```javascript
db.adminCommand( 
   {
     setFeatureCompatibilityVersion: <version>,
     confirm: true,
     writeConcern: { wtimeout: <timeout> }
   } 
)
```

## Command Fields

The `setFeatureCompatibilityVersion` command takes the following
fields:

### setFeatureCompatibilityVersion

*Required*

The possible values for `version` are:

| Version | Description |
|---|---|
| `"7.0"` | *Available on MongoDB 7.0 Deployments* Enables the 7.0 features that persist data incompatible with MongoDB 6.0. |
| `"6.0"` | *Available on MongoDB 6.0 and 7.0 Deployments* Enables the 6.0 features that persist data incompatible with MongoDB 5.0. |
| `"5.0"` | *Available on MongoDB 5.0 and 6.0 Deployments* Enables the 5.0 features that persist data incompatible with MongoDB 4.4. |

### confirm

*Required*

**New in version:** 7.0

Set to `true` to confirm the feature compatibility change and allow
the operation to proceed.

If you omit the `confirm` parameter or set `confirm` to a value
other than `true`, the command fails and returns a warning about
modifying the feature compatibility version. The warning states that
after you upgrade or downgrade your cluster's FCV (feature compatibility version), you cannot
downgrade the binary version without support assistance.

### writeConcern

*Optional*

The `writeConcern` specifies the write concern
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

### Downgrade with Backward-Incompatible Data

If you try to downgrade the FCV (feature compatibility version) of a cluster that contains
incompatible data in the downloaded version, you receive a
`CannotDowngrade` error. When this error occurs, the cluster remains
in the transitionary `downgrading` state.

To move the cluster out of the `downgrading` state, either:

- Modify your cluster data to remove backwards-incompatible features,
  then re-run the `setFeatureCompatibilityVersion` command with the
  downgraded version to set the FCV (feature compatibility version) to the downgraded version.

- Run the `setFeatureCompatibilityVersion` command with the original
  upgraded version to set the FCV (feature compatibility version) back to the original version.

  **Important:**

  Setting the FCV (feature compatibility version) to the original version stops the downgrade
  procedure and changes the FCV (feature compatibility version) back to the upgraded version.
  This procedure does not reset the cluster back to the state before
  the FCV (feature compatibility version) downgrade began.

  If a failed FCV (feature compatibility version) downgrade's internal metadata is not
  cleaned up, any subsequent FCV upgrade attempt fails with an
  error message. You must complete the FCV (feature compatibility version) downgrade before
  trying to upgrade the FCV (feature compatibility version).

### Downgrade Policy Changes in MongoDB 7.0

Starting in MongoDB 7.0, you cannot downgrade your deployment's FCV (feature compatibility version)
to or from a rapid release version of MongoDB.

If you upgrade or downgrade your deployment's FCV (feature compatibility version), you cannot
downgrade your deployment's binary version without assistance from
support.

To learn more, see 7.0-downgrade.

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
| For new 7.0 deployments | `"7.0"` |
| For 7.0 deployments upgraded from 6.0 | `"6.0"` until you `setFeatureCompatibilityVersion` to `"7.0"`. |
| For new 6.0 deployments | `"6.0"` |
| For 6.0 deployments upgraded from 5.0 | `"5.0"` until you `setFeatureCompatibilityVersion` to `"6.0"`. |

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
db.adminCommand(
   {
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

### Set Feature Compatibility Version on MongoDB 7.0 Deployments

#### Enable 7.0 Backwards Incompatible Features

To enable the 7.0 features that persist data incompatible with
MongoDB 6.0, set the feature compatibility
to `"7.0"` on the MongoDB 7.0 deployment:

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
db.adminCommand(
   {
      setFeatureCompatibilityVersion: "7.0",
      confirm: true
   }
)
```

#### Disable 7.0 Backwards Incompatible Features

To disable the 7.0 features that persist data incompatible with
MongoDB 6.0, set the feature compatibility
to `"6.0"` on the MongoDB 7.0 deployment:

**Note:**

Run the `setFeatureCompatibilityVersion` command against
the `admin` database.

- For a standalone, run the command on the standalone
  `mongod` instance.

- For a replica set, run the command on the primary. A majority of the
  data-bearing members must be available.

- For a sharded cluster, run the command on a `mongos`
  instance.

- `"6.0"` featureCompatibilityVersion is supported on MongoDB
  6.0 and MongoDB 7.0 deployments only.

```javascript
db.adminCommand(
   {
      setFeatureCompatibilityVersion: "6.0",
      confirm: true
   }
)
```

If run as part of the downgrade process from MongoDB 7.0 to MongoDB 
6.0, you must also remove all persisted features that are
incompatible with 6.0. See the
appropriate downgrade procedures.

### Set Feature Compatibility Version on MongoDB 6.0 Deployments

#### Enable 6.0 Backwards Incompatible Features

To enable the 6.0 features that persist data incompatible with
MongoDB 5.0 , set the feature compatibility to `"6.0"` on the MongoDB 6.0 
deployment:

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
MongoDB 5.0, set the feature compatibility to `"5.0"` on the MongoDB 6.0 
deployment:

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
incompatible with 5.0. See the appropriate downgrade procedures.

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

## Troubleshooting

If you experience startup issues after setting your feature compatibility 
version, contact [MongoDB Support](https://support.mongodb.com/welcome) for assistance.
