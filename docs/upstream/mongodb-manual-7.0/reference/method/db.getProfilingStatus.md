<!-- Converted from reference/method/db.getProfilingStatus.txt (reStructuredText). Includes are inlined. -->

# db.getProfilingStatus() (mongosh method)

**`db.getProfilingStatus()`**

:returns: The current `profile` level,
          `slowOpThresholdMs` setting,
          and `slowOpSampleRate`
          setting.

          You can set a `filter` to control which operations are logged by 
          the profiler. When set, any configured filters are also returned by
          `db.getProfilingStatus()`, along with a `note`
          explaining filter behavior.

          You can set the profiling filter with either:

          - the `db.setProfilingLevel()` shell method, or

          - the `operationProfiling.filter` configuration file option.

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
