<!-- Converted from reference/method/db.getLogComponents.txt (reStructuredText). Includes are inlined. -->

# db.getLogComponents() (mongosh method)

## Definition

**`db.getLogComponents()`**

Returns the current verbosity settings. The verbosity settings
determine the amount of /reference/log-messages that MongoDB
produces for each log message component.

If a component inherits the verbosity level of its parent,
`db.getLogComponents()` displays `-1` for the component's
verbosity.

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

## Output

The `db.getLogComponents()` returns a document with the
verbosity settings. For example:

```none
{
   "verbosity" : 0,
   "accessControl" : {
      "verbosity" : -1
   },
   "command" : {
      "verbosity" : -1
   },
   "control" : {
      "verbosity" : -1
   },
   "geo" : {
      "verbosity" : -1
   },
   "index" : {
      "verbosity" : -1
   },
   "network" : {
      "verbosity" : -1
   },
   "query" : {
      "verbosity" : 2
   },
   "replication" : {
      "verbosity" : -1,
      "election" : {
         "verbosity" : -1
      },
      "heartbeats" : {
         "verbosity" : -1
      },
      "initialSync" : {
         "verbosity" : -1
      },
      "rollback" : {
         "verbosity" : -1
      }
   },
   "sharding" : {
      "verbosity" : -1
   },
   "storage" : {
      "verbosity" : 2,
      "recovery" : {
         "verbosity" : -1
      },
      "journal" : {
         "verbosity" : -1
      }
   },
   "write" : {
      "verbosity" : -1
   }
}
```

To modify these settings, you can configure the
`systemLog.verbosity` and
`systemLog.component.<name>.verbosity` settings in the
configuration file or set the
`logComponentVerbosity` parameter using the
`setParameter` command or use the `db.setLogLevel()`
method. For examples, see log-messages-configure-verbosity.
