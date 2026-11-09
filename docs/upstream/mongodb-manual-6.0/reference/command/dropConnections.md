<!-- Converted from reference/command/dropConnections.txt (reStructuredText). Includes are inlined. -->

# dropConnections

## Definition

**`dropConnections`**

The `dropConnections` command drops the 
`mongod` / `mongos` instance's outgoing
connections to the specified hosts. The `dropConnections`
must be run  against the `admin` database. 

## Compatibility

This command is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has following syntax:

```javascript
db.adminCommand(
   { 
     dropConnections: 1, 
     hostAndPort : [ "host1:port1", "host2:port2", ... ],
     comment: <any>
   }
)
```

## Command Fields

The command requires the following field:

| Field | Type | Description |
|---|---|---|
| `hostAndPort` | array | Each array element represents the hostname and port of a remote machine. |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

## Access Control

If the deployment enforces 
authentication/authorization,
the `dropConnections` command requires the 
`dropConnections` action on the 
cluster resource. 

Create a user-defined role in the `admin`
database  where the `privilege` array includes the following document:

```javascript
{ "resource" : { "cluster" : true } }, "actions" : [ "dropConnections" ] }
```

- Use `db.createUser()` to create a user on the `admin`
  database with the custom role.

  *or* 

- Use `db.grantRolesToUser()` to grant the role to an  existing 
  user on the `admin` database.

For example, the following operation creates a
user-defined role on the `admin` database with the privileges
to support `dropConnections`:

```javascript
db.getSiblingDB("admin").createRole(
  {
    "role" : "dropConnectionsRole",
    "privileges" : [
      { 
        "resource" : { "cluster" : true }, 
        "actions" : [ "dropConnections" ] 
      }
    ],
    "roles" : []
  }
)
```

Assign the custom role to a user on the `admin` database:

```javascript
db.getSiblingDB("admin").createUser(
  {
    "user" : "dropConnectionsUser",
    "pwd" : "replaceThisWithASecurePassword",
    "roles" : [ "dropConnectionsRole" ]
  }
)
```

The created user can execute `dropConnections`. 

For more examples of user creation, see /tutorial/create-users.
For a tutorial on adding privileges to an existing database user, see 
modify-existing-user-access.

## Behavior

`dropConnections` silently ignores `hostAndPort` elements
that do not include both the hostname and port of the remote machine.

## Example

Consider a replica set with a recently removed member at
`oldhost.example.com:27017`. Running the following 
`dropConnections` command against each active
replica set member ensures there are no remaining outgoing connections 
to `oldhost.example.com:27017`:

```javascript
db.adminCommand( 
  {
    "dropConnections" : 1,
    "hostAndPort" : [
      "oldhost.example.com:27017"
    ] 
  } 
)
```

The command returns output similar to the following:

```javascript
{
 "ok" : 1,
 "$clusterTime" : {
   "clusterTime" : Timestamp(1551375968, 1),
   "signature" : {
     "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
     "keyId" : NumberLong(0)
   }
 },
 "operationTime" : Timestamp(1551375968, 1)
}
```

You can confirm the status of the connection pool for the
`mongod` or `mongos` using the
`connPoolStats` command.
