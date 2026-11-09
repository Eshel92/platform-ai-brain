<!-- Converted from reference/command/grantRolesToRole.txt (reStructuredText). Includes are inlined. -->

# grantRolesToRole

## Definition

**`grantRolesToRole`**

Grants roles to a user-defined role.

**Tip:**

In `mongosh`, this command can also be run through the `db.grantRolesToRole` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

The `grantRolesToRole` command affects roles on the
database where the command runs. 

The command has the following syntax:

```javascript
db.runCommand(
   {  
     grantRolesToRole: "<role>",
     roles: [
                { role: "<role>", db: "<database>" },
                ...
            ],
     writeConcern: { <write concern> },
     comment: <any>
   }
)
```

  
The command has the following fields:

| Field | Type | Description |
|---|---|---|
| `grantRolesToRole` | string | The name of a role to add subsidiary roles. |
| `roles` | array | An array of roles from which to inherit. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

In the `roles` field, you can specify both
built-in roles and user-defined
roles.

To specify a role that exists in the same database where
`grantRolesToRole` runs, you can either specify the role with the name of
the role:

```javascript
"readWrite"
```

Or you can specify the role with a document, as in:

```javascript
{ role: "<role>", db: "<database>" }
```

To specify a role that exists in a different database, specify the role
with a document.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB
             

## Behavior

A role can inherit privileges from other roles in its database. A role
created on the `admin` database can inherit privileges from roles in
any database.

## Required Access

You must have the `grantRole` action on a database to grant a role on that database.

## Example

The following `grantRolesToRole` command updates the
`productsReaderWriter` role in the `products` database to inherit the privileges of the `productsReader`
role in the `products` database:

```javascript
use products
db.runCommand(
   { grantRolesToRole: "productsReaderWriter",
     roles: [
              "productsReader"
     ],
     writeConcern: { w: "majority" , wtimeout: 5000 }
   }
)
```
