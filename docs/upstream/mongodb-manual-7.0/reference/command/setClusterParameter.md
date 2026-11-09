<!-- Converted from reference/command/setClusterParameter.txt (reStructuredText). Includes are inlined. -->

# setClusterParameter (database command)

## Definition

   

**`setClusterParameter`**

`setClusterParameter` is an administrative command for
modifying values of **cluster parameters**. Cluster parameters 
are configurable parameters which affect all nodes in a replica set or 
sharded cluster. 

You must issue the `setClusterParameter` command against the `admin` 
database.

The `setClusterParameter` command is only available in self-managed
installations. The `setClusterParameter` command is not available in
MongoDB Atlas.

## Compatibility

This command is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

**Important:**

This command is not supported in MongoDB Atlas clusters.
For information on Atlas support for all commands, 
see Unsupported Commands.

## Syntax

```javascript
db.adminCommand( 
   { 
     setClusterParameter: { <parameter>: <value> } 
   } 
)
```

For the available cluster parameters, including examples, see
cluster-parameters. 

## Behavior

- You can only run `setClusterParameter` on the `admin` database. If you run 
  the command on any other database, MongoDB returns an error.

- You can only run `setClusterParameter` on a replica set primary or on a 
  sharded cluster. 

- You **cannot** run `setClusterParameter` on a standalone deployment. 

- `setClusterParameter` accepts only one parameter at a time.

### Accesss Control

When authentication is enabled, `setClusterParameter` 
only works when authenticated as a user with a role that has access 
to the `setClusterParameter` action.

### Persistence

The parameter modifications made using `setClusterParameter` 
are persisted on replica sets and sharded clusters. This ensures that 
parameter modifications made using `setClusterParameter` survive 
restarts.

### Stable API

When using Stable API V1 with apiStrict set to `true`, you cannot use
`setClusterParameter` to modify cluster parameters.
