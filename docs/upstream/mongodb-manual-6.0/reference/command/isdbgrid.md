<!-- Converted from reference/command/isdbgrid.txt (reStructuredText). Includes are inlined. -->

# isdbgrid

## Definition

**`isdbgrid`**

This command verifies that a process is a `mongos`.

If you issue the `isdbgrid` command when connected to a
`mongos`, the response document includes the `isdbgrid`
field set to `1`. 

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
     isdbgrid: 1
   }
)
```

## Output

The returned document is similar to the following:

```javascript
{ "isdbgrid" : 1, "hostname" : "app.example.net", "ok" : 1 }
```

If you issue the `isdbgrid` command when connected to a
`mongod`, MongoDB returns an error document. The
`isdbgrid` command is not available to `mongod`.
The error document, however, also includes a line that reads
`"isdbgrid" : 1`, just as in the document returned for a
`mongos`. The error document is similar to the following:

```javascript
{
   "errmsg" : "no such cmd: isdbgrid",
   "bad cmd" : {
         "isdbgrid" : 1
   },
   "ok" : 0
}
```

 
You can instead use the `hello` command to determine
connection to a `mongos`. When connected to a
`mongos`, the `hello` command returns a document that
contains the string `isdbgrid` in the `msg` field.
