<!-- Converted from reference/command/getCmdLineOpts.txt (reStructuredText). Includes are inlined. -->

# getCmdLineOpts (database command)

## Definition

**`getCmdLineOpts`**

The `getCmdLineOpts` command returns a document
containing command line options used to start the given
`mongod` or `mongos`. Run
`getCmdLineOpts` in the `admin` database.

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
     getCmdLineOpts: 1  
   } 
)
```

## Output

This command returns a document with two fields, `argv` and
`parsed`. The `argv` field contains an array with each item from
the command string used to invoke `mongod` or
`mongos`. The document in the `parsed` field includes all
runtime options, including those parsed from the command line and
those specified in the configuration file, if specified.

Consider the following example output of
`getCmdLineOpts`:

```javascript
{
   "argv" : [
      "/usr/bin/mongod",
      "--config",
      "/etc/mongod.conf"
   ],
   "parsed" : {
      "config" : "/etc/mongod.conf",
      "net" : {
         "bindIp" : "127.0.0.1",
         "port" : 27017
      },
      "processManagement" : {
         "fork" : true
      },
      "storage" : {
         "dbPath" : "/data/db"
      },
      "systemLog" : {
         "destination" : "file",
         "logAppend" : true,
         "path" : "/var/log/mongodb/mongod.log"
      }
   },
   "ok" : 1
}
```
