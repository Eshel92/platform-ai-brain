<!-- Converted from reference/method/db.hostInfo.txt (reStructuredText). Includes are inlined. -->

# db.hostInfo() (mongosh method)

**`db.hostInfo()`**

Returns a document with information about the underlying system
that the `mongod` or `mongos` runs on. Some of the
returned fields are only included on some platforms.

`db.hostInfo()` provides a `mongosh` helper
method around the `hostInfo` command. The output of
`db.hostInfo()` on a Linux system will resemble the
following:

```javascript
{
   "system" : {
          "currentTime" : ISODate("<timestamp>"),
          "hostname" : "<hostname>",
          "cpuAddrSize" : <number>,
          "memSizeMB" : <number>, 
          "memLimitMB" : <number>,  
          "numCores" : <number>,
          "cpuArch" : "<identifier>",
          "numaEnabled" : <boolean>
   },
   "os" : {
          "type" : "<string>",
          "name" : "<string>",
          "version" : "<string>"
   },
   "extra" : {
          "versionString" : "<string>",
          "libcVersion" : "<string>",
          "kernelVersion" : "<string>",
          "cpuFrequencyMHz" : "<string>",
          "cpuFeatures" : "<string>",
          "pageSize" : <number>,
          "numPages" : <number>,
          "maxOpenFiles" : <number>
   },
   "ok" : <return>
}
```

See `hostInfo` for full documentation of the output of
`db.hostInfo()`.

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
