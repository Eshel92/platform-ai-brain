<!-- Converted from reference/command/configureCollectionBalancing.txt (reStructuredText). Includes are inlined. -->

# configureCollectionBalancing (database command)

## Definition

**`configureCollectionBalancing`**

**New in version:** 5.3

Configures balancer settings for a sharded collection, such as
setting the chunk size for and defragmenting the collection.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   {
     configureCollectionBalancing: "<db>.<collection>",
     chunkSize: <num>,
     defragmentCollection: <bool>
     enableAutoMerger: <bool> 
   } 
)
```

### Command Fields

`configureCollectionBalancing` has the following fields:

| Field | Type | Necessity | Description |
|---|---|---|---|
| `configureCollectionBalancing` | string | Required | The name of the database and sharded collection to configure. |
| `chunkSize` | integer | Optional | Sets the chunk size in MiB for the collection. The recommended size is 256, 512, or larger. For details on default behavior, see chunksize-not-specified. |
| `defragmentCollection` | boolean | Optional | Causes the balancer to defragment the collection. Defaults to `false`. |
| `enableAutoMerger` | boolean | Optional | Whether or not the AutoMerger takes this collection into account. Defaults to `true`. |

 

For more information, see Data Partitioning with Chunks.

To configure the chunk defragmentation throttling time parameter, see
`chunkDefragmentationThrottlingMS`.

To learn about defragmenting sharded collections, see
defragment-sharded-collections.

## Behavior

### Default Behavior When chunkSize Is Not Specified

If you do not specify `chunkSize` for a collection and no custom size 
has been set previously, the global default `chunkSize` is 
used for balancing.

### Specifying chunkSize: 0

If you use `configureCollectionBalancing` with
`chunkSize: 0`, the per-collection `chunkSize` is reset and the 
global default `chunkSize` is used for balancing.

For more information on configuring default `chunkSize`,
see tutorial-modifying-range-size.

### Default Behavior When enableAutoMerger Is Not Specified

If you do not specify `enableAutoMerger` for a collection and no 
custom automerging behavior has been previously set, it 
defaults to `true` and will be taken into account by the 
AutoMerger.

## Examples

### Configure Chunk Size

To change the chunk size for a sharded collection, use
the `chunkSize` option:

```javascript
db.adminCommand( {
   configureCollectionBalancing: "test.students",
   chunkSize: 256
} )
```

Use this command to change the chunk size for the given collection.

**Warning:**

By default, MongoDB cannot move a chunk if the number of documents in
the chunk is greater than 2 times the result of dividing the
configured chunk size by the average document size.

To find the average document size, see the `avgObjSize` field in the
output of the `db.collection.stats()` method.

For more information, see Range Size.

### Defragment Collections

**Warning:**

We do not recommend using `defragmentCollection` to defragment sharded
collections for MongoDB 6.0.0 to 6.0.3 and MongoDB 6.1.0 to 6.1.1, as the
defragmentation process on these releases can make databases and collections
unavailable for extended periods of time.

To tell the balancer to defragment a sharded collection, use the
`defragmentCollection` option:

```javascript
db.adminCommand( {
   configureCollectionBalancing: "test.students",
   defragmentCollection: true
} )
```

Use this command to have the balancer defragment a sharded collection.
To monitor the chunk defragmentation process, use the
`balancerCollectionStatus` command.

To learn more about defragmenting sharded collections, see
defragment-sharded-collections.

### Reconfigure and Defragment Collections

To defragment a sharded collection while updating the chunk size, use
the `defragmentCollection` option and the `chunkSize` option
together:

```javascript
db.adminCommand( {
   configureCollectionBalancing: "test.students",
   chunkSize: 512,
   defragmentCollection: true
} )
```

### Disable the AutoMerger on a Collection

To explicitly disable the AutoMerger on a collection,
set the `enableAutoMerger` option to `false`:

```javascript
db.adminCommand( {
   configureCollectionBalancing: "test.students",
   enableAutoMerger: false
} )
```
