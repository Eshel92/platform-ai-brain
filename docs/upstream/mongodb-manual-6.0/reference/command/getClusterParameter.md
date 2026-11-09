<!-- Converted from reference/command/getClusterParameter.txt (reStructuredText). Includes are inlined. -->

# getClusterParameter

## Definition

**`getClusterParameter`**

`getClusterParameter` is an administrative command for
retrieving the values of **cluster parameters**. Cluster parameters
are configurable parameters that affect all nodes in a sharded cluster.

To run `getClusterParameter`, use the `db.adminCommand( { command } )`
method.

The `getClusterParameter` command is only available in self-managed
installations. The `getClusterParameter` command is not available in
MongoDB Atlas.

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
db.adminCommand(
   {
     getClusterParameter: <parameter> | [<parameter>, <parameter>] | "'*'"
   }
)
```

 

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - `<parameter>`
  - String or array of strings 
  - You can specify one of the following: 

    - The name of the parameter you want to retrieve.

    - An array with the names of multiple parameters.

    - `'*'`, to return values for all parameters available to
      `getClusterParameter`.

## Behavior

- You can only run `getClusterParameter` on the `admin` database. If
  you run the command on any other database, MongoDB returns an error.

- You can run `getClusterParameter` on any node in a replica set or
  sharded cluster.

- When you run `getClusterParameter` on `mongod`,
  `getClusterParameter` returns cached parameter values.

- When you run `getClusterParameter` on `mongos`,
  `getClusterParameter` returns the durable value of the
  cluster parameter from the config server.

### Access Control

When authentication is enabled, `getClusterParameter` 
only works when authenticated as a user with a role that has access to the 
`getClusterParameter` action.

## Examples

**Note:**

The output of the following examples may vary depending on the specific
configuration of the running MongoDB deployment.

### Retrieve Single Cluster Parameter

The following operation runs `getClusterParameter` on the `admin`
database using a value of `hostName` to retrieve the value for
a hypothetical cluster parameter named `hostName`:

```javascript
use admin
db.adminCommand( { getClusterParameter : "hostName" } )
```

### Retrieve Multiple Cluster Parameters

The following operation runs `getClusterParameter` on the `admin` 
database using the values `hostName` and `testParameter` to retrieve the 
values for hypothetical cluster parameters named `hostName` and 
`testParameter`:

```javascript
use admin
db.adminCommand( { getClusterParameter: [ "hostName", "testParameter" ] } )
```

### Retrieve All Cluster Parameters

The following operation runs `getClusterParameter` with a value of
`'*'` to retrieve the values from all cluster parameters:

```javascript
use admin
db.adminCommand( { getClusterParameter : '*' } )
```

**See also:**

`setClusterParameter` for more about these parameters.
