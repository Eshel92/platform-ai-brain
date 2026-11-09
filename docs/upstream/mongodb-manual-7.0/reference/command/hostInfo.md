<!-- Converted from reference/command/hostInfo.txt (reStructuredText). Includes are inlined. -->

# hostInfo (database command)

## Definition

**`hostInfo`**

:returns: A document with information about the underlying system
          that the `mongod` or `mongos` runs on.
          Some of the returned fields are only included on some
          platforms.

You must run the `hostInfo` command, which takes no
arguments, against the `admin` database. 

## Compatibility

This command is available in deployments hosted in the following environments: 

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
db.adminCommand( 
   { 
     hostInfo: 1 
   } 
)
```

## Output

In `mongosh` you can use `db.hostInfo()`
as a helper to access `hostInfo`. The output of
`hostInfo` on a Linux system will resemble the
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
          "numCoresAvailableToProcess" : <number>,
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

 

### Output Fields

**`hostInfo`**

The document returned by the `hostInfo`.

**`hostInfo.system`**

An embedded document providing information about the underlying
environment of the system running the `mongod` or `mongos`

**`hostInfo.system.currentTime`**

A timestamp of the current system time.

**`hostInfo.system.hostname`**

The system name, which should correspond to the output of
`hostname -f` on Linux systems.

**`hostInfo.system.cpuAddrSize`**

A number reflecting the architecture of the system. Either
`32` or `64`.

**`hostInfo.system.memSizeMB`**

The total amount of system memory (RAM) in megabytes.

**`hostInfo.system.memLimitMB`**

The memory usage limit in megabytes.

For example, running in a container may impose memory limits that
are lower than the total system memory. This memory limit, rather
than the total system memory, is used as the maximum RAM available
to calculate WiredTiger internal cache.

**`hostInfo.system.numCores`**

The total number of available logical processor cores.

**`hostInfo.system.numCoresAvailableToProcess`**

The number of CPU cores available to the process. Returns `-1`
when the underlying system call to retrieve the number of cores fails.

**`hostInfo.system.cpuArch`**

A string that represents the system architecture. Either `x86`
or `x86_64`.

**`hostInfo.system.numaEnabled`**

A boolean value. `false` if NUMA is interleaved (i.e. disabled),
otherwise `true`.

**`hostInfo.os`**

An embedded document that contains information about the operating
system running the `mongod` and `mongos`.

**`hostInfo.os.type`**

A string representing the type of operating system, such as
`Linux` or `Windows`.

**`hostInfo.os.name`**

If available, returns a display name for the operating
system.

**`hostInfo.os.version`**

If available, returns the name of the distribution or operating
system.

**`hostInfo.extra`**

An embedded document with extra information about the operating system
and the underlying hardware. The content of the
`extra` embedded document depends on the operating
system.

**`hostInfo.extra.cpuString`**

A string containing a human-readable description of the system's
processor.

`cpuString` only appears on macOS systems.

**`hostInfo.extra.versionString`**

A complete string of the operating system version and
identification. On Linux and macOS systems, this contains output
similar to `uname -a`.

**`hostInfo.extra.libcVersion`**

The release of the system `libc`.

`libcVersion` only appears on Linux
systems.

**`hostInfo.extra.kernelVersion`**

The release of the Linux kernel in current use.

`kernelVersion` only appears on Linux
systems.

**`hostInfo.extra.alwaysFullSync`**

`alwaysFullSync` only appears on macOS
systems.

**`hostInfo.extra.nfsAsync`**

`nfsAsync` only appears on macOS
systems.

**`hostInfo.extra.cpuFrequencyMHz`**

Reports the clock speed of the system's processor in megahertz.

**`hostInfo.extra.cpuFeatures`**

Reports the processor feature flags. On Linux systems this the
same information that `/proc/cpuinfo` includes in the
`flags` fields.

**`hostInfo.extra.pageSize`**

Reports the default system page size in bytes.

**`hostInfo.extra.physicalCores`**

Reports the number of physical, non-HyperThreading, cores available on the
system.

`physicalCores` only appears on macOS systems.

**`hostInfo.extra.numPages`**

`numPages` only appears on Linux systems.

**`hostInfo.extra.maxOpenFiles`**

Reports the current system limits on open file handles. See
/reference/ulimit for more information.

`maxOpenFiles` only appears on Linux
systems.

**`hostInfo.extra.scheduler`**

Reports the active I/O scheduler.
`scheduler` only appears on OS
X systems.
