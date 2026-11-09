<!-- Converted from reference/command/grantPrivilegesToRole.txt (reStructuredText). Includes are inlined. -->

# grantPrivilegesToRole (database command)

## Definition

**`grantPrivilegesToRole`**

Assigns additional privileges to a user-defined role defined on the database on which the
command is run. 

**Tip:**

In `mongosh`, this command can also be run through the `db.grantPrivilegesToRole` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

The `grantPrivilegesToRole` command uses the following syntax:

```javascript
db.runCommand(
   {
     grantPrivilegesToRole: "<role>",
     privileges: [
       {
         resource: { <resource> }, actions: [ "<action>", ... ]
       },
       ...
     ],
     writeConcern: { <write concern> },
     comment: <any>
   }
)
```

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
   

## Command Fields

The command has the following fields:

| Field | Type | Description |
|---|---|---|
| `grantPrivilegesToRole` | string | The name of the user-defined role to grant privileges to. |
| `privileges` | array | The privileges to add to the role. For the format of a privilege, see `privileges`. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

## Behavior

A role's privileges apply to the database where the role is created. A
role created on the `admin` database can include privileges that apply
to all databases or to the cluster.

## Required Access

You must have the `grantRole` action on the database a privilege targets in order to
grant the privilege. To grant a privilege on multiple databases or on the
`cluster` resource, you must have the `grantRole` action on
the `admin` database.

## Example

The following `grantPrivilegesToRole` command grants two
additional privileges to the `service` role that exists in the
`products` database:

```javascript
use products
db.runCommand(
   {
     grantPrivilegesToRole: "service",
     privileges: [
         {
           resource: { db: "products", collection: "" }, actions: [ "find" ]
         },
         {
           resource: { db: "products", collection: "system.js" }, actions: [ "find" ]
         }
     ],
     writeConcern: { w: "majority" , wtimeout: 5000 }
   }
)
```

The first privilege in the `privileges` array allows the user to
search on all non-system collections in the `products` database. The
privilege does not allow queries on system collections, such as the `system.js
<` collection. To grant access to these
system collections, explicitly provision access in the `privileges`
array. See /reference/resource-document.

The second privilege explicitly allows the `find` action on
`system.js <` collections on all
databases.
