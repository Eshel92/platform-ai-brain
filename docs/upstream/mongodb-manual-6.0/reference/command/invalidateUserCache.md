<!-- Converted from reference/command/invalidateUserCache.txt (reStructuredText). Includes are inlined. -->

# invalidateUserCache

## Definition

**`invalidateUserCache`**

Flushes user information from in-memory cache, including removal of each user's
credentials and roles. This allows you to purge the cache
at any given moment, regardless of the
interval set in the `userCacheInvalidationIntervalSecs` parameter.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     invalidateUserCache: 1 
   } 
)
```

## Required Access

You must have privileges that include the
`invalidateUserCache` action on the cluster resource in order
to use this command.
