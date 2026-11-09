<!-- Converted from reference/command/buildInfo.txt (reStructuredText). Includes are inlined. -->

# buildInfo

## Definition

**`buildInfo`**

The `buildInfo` command returns a build summary for the current
`mongod`. 

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
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
db.runCommand(
   { 
     buildInfo: 1 
   }
)
```

## Usage

In `mongosh`, call `buildInfo` in the
following form:

```javascript
db.runCommand( { buildInfo: 1 } )
```

The output document of `buildInfo` has the following
form:

```javascript
{
  "version" : "<string>",
  "gitVersion" : "<string>",
  "sysInfo" : "<string>",
  "loaderFlags" : "<string>",
  "compilerFlags" : "<string>",
  "allocator" : "<string>",
  "versionArray" : [ <num>, <num>, <...> ],
  "openssl" : <document>,
  "javascriptEngine" : "<string>",
  "bits" : <num>,
  "debug" : <boolean>,
  "maxBsonObjectSize" : <num>,
  "storageEngines" : [ "<string>", "<string>", "<...>" ],
  "ok" : <num>
}
```

## Output

**`buildInfo`**

The document returned by the `buildInfo` command.

### Supported

These fields are stable and should provide consistent behavior.

**`buildInfo.gitVersion`**

The commit identifier that identifies the state of the code used
to build the `mongod`.

**`buildInfo.versionArray`**

An array that conveys version information about the
`mongod` instance. See `version` for a
more readable version of this string.

**`buildInfo.version`**

A string that conveys version information about the
`mongod` instance. If you need to present version information to
a human, this field is preferable to `versionArray`.

This string will take the format `<major>.<minor>.<patch>` in the case of
a release, but development builds may contain additional information.

**`buildInfo.storageEngines`**

A list of storage engines available to the
`mongod` server.

**`buildInfo.javascriptEngine`**

A string that reports the JavaScript engine used in the
`mongod` instance. By default, this is `mozjs`.

**`buildInfo.bits`**

A number that reflects the target processor architecture of the
`mongod` binary.

**`buildInfo.debug`**

A boolean. `true` when built with debugging options.

**`buildInfo.maxBsonObjectSize`**

A number that reports the `Maximum BSON Document Size`.

**`buildInfo.openssl`**

An embedded document describing the version of the TLS/SSL library
that `mongod` was built with and is currently using.

**`buildInfo.modules`**

A list of add-on modules that `mongod` was built with. Possible
values currently include "enterprise" and "rocksdb".

### Unstable

These fields are for internal use only, and you should not expect their behavior
or existence to remain consistent on any level.

**`buildInfo.allocator`**

The memory allocator that `mongod` uses. By default
this is `tcmalloc`.

**`buildInfo.buildEnvironment`**

An embedded document containing various debugging information about the
`mongod` build environment.
