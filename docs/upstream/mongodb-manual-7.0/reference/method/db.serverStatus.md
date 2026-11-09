<!-- Converted from reference/method/db.serverStatus.txt (reStructuredText). Includes are inlined. -->

# db.serverStatus() (mongosh method)

**`db.serverStatus()`**

Returns a document that provides an overview of the
database process's state.

This command provides a wrapper around the database command
`serverStatus`.

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

## Behavior

By default, `db.serverStatus()` excludes in its output:

- some content in the server-status-repl document.

- server-status-mirroredReads document.

To include fields that are excluded by default, specify the top-level
field and set it to `1` in the command. To exclude fields that are included 
by default, specify the field and set to 0. You can specify either top-level 
or embedded fields. 

For example, the following operation suppresses the `repl`,
`metrics` and `locks` information in the output.

```javascript
db.serverStatus( { repl: 0,  metrics: 0, locks: 0 } )
```

The following example includes all server-status-repl
information in the output:

```javascript
db.serverStatus( { repl: 1 } )
```

### Exclude All Optional Fields

Starting in MongoDB 7.0.38, you can exclude all optional fields 
from the `db.serverStatus()` output by specifying `none: 1`. 
After you exclude all optional fields, you can then specify
the fields you want to include.

This example uses `none` to initially exclude all optional 
fields from the output, then includes the  `locks` document.

```javascript
db.serverStatus({ none: 1, locks: 1 })
```

### Initialization

The statistics reported by `db.serverStatus()` are reset when
the `mongod` server is restarted. The `db.serverStatus()`
command does not report some statistics until they have been
initialized by server events.

For example, after restarting the `mongod` server, 
`db.serverStatus()` won't return any values for `findAndModify`.

```javascript
db.serverStatus().metrics.commands.findAndModify
// No results returned
```

After you run an update query, subsequent calls to 
`db.serverStatus()` display the expected metrics. 

```javascript
{
   "arrayFilters" : Long(0),
   "failed" : Long(0),
   "pipeline" : Long(0),
   "total" : Long(1)
}
```

**Note:**

The `db.serverStatus()` method returns an error if a specific
object is queried before the counters have begun to increment. 

If there haven't been any document updates yet:

```javascript
db.serverStatus().metrics.commands.update.pipeline
```

Returns: 

```javascript
TypeError: db.serverStatus(...).metrics.commands.update is undefined :
@(shell):1:1
```

### Include `mirroredReads`

By default, the `mirroredReads` information is not included in 
the output. To return `mirroredReads` information, you must 
explicitly specify the inclusion:

```javascript
db.serverStatus( { mirroredReads: 1 } )
```

### Include `latchAnalysis`

By default, the `latchAnalysis` information (available
starting in version 4.4) is not included in the output. To return
`latchAnalysis` information, you must explicitly specify
the inclusion:

```javascript
db.serverStatus( { latchAnalysis: 1 } )
```

## Output

See serverStatus Output for complete
documentation of the output of this function.
