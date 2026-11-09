<!-- Converted from reference/method/sh.stopAutoMerger.txt (reStructuredText). Includes are inlined. -->

# sh.stopAutoMerger() (mongosh method)

## Definition

**`sh.stopAutoMerger()`**

**New in version:** 7.0

Disables the AutoMerger.

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
sh.stopAutoMerger()
```

## Behavior

When the method runs, it stops the AutoMerger. Any in 
progress operations issued by the AutoMerger are completed.

## Example

The following example disables the AutoMerger. Run the example 
from `mongos`:

```javascript
sh.stopAutoMerger()
```

## Learn More

- automerger-concept
- `sh.startAutoMerger()` method
- `sh.enableAutoMerger()` method
- `sh.disableAutoMerger()` method

- `configureCollectionBalancing` command
- `mergeAllChunksOnShard` command
- `autoMergerIntervalSecs` parameter
- `autoMergerThrottlingMS` parameter
