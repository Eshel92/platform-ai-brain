<!-- Converted from reference/method/sh.startAutoMerger.txt (reStructuredText). Includes are inlined. -->

# sh.startAutoMerger() (mongosh method)

## Definition

**`sh.startAutoMerger()`**

**New in version:** 7.0

Enables the AutoMerger.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

```javascript
sh.startAutoMerger()
```

## Behavior

To set the time intervals for automatic chunk merges, use these
parameters:

- `autoMergerIntervalSecs`
- `autoMergerThrottlingMS`

**Note:**

You can set these parameters on config servers only.

## Example

The following example enables the AutoMerger. Run the example 
from `mongos`:

```javascript
sh.startAutoMerger()
```

## Learn More

- automerger-concept
- `sh.stopAutoMerger()` method
- `sh.enableAutoMerger()` method
- `sh.disableAutoMerger()` method

- `configureCollectionBalancing` command
- `mergeAllChunksOnShard` command
- `autoMergerIntervalSecs` parameter
- `autoMergerThrottlingMS` parameter
