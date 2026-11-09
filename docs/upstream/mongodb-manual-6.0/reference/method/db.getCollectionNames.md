<!-- Converted from reference/method/db.getCollectionNames.txt (reStructuredText). Includes are inlined. -->

# db.getCollectionNames()

## Definition

**`db.getCollectionNames()`**

Returns an array containing the names of all collections and
views in the current database, or if running
with access control, the names of the collections according to user's
privilege. For details, see db.collectionnames-access.

## Compatibility

This method is available in deployments hosted in the following environments: 

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

## Required Access

The `db.getCollectionNames()` is equivalent to:

```javascript
db.runCommand(
   {
       listCollections: 1.0,
       authorizedCollections: true,
       nameOnly: true
   }
)
```

- For users with the required access (privileges that grant
  `listCollections` action on the database), the method
  lists the names of all collections for the database.

- For users without the required access, the method lists only the
  collections for which the users has privileges. For example, if a
  user has `find` on a specific collection in a
  database, the method would return just that collection.

## Behavior

### Client Disconnection

Starting in MongoDB 4.2, if the client that issued `db.getCollectionNames()`
disconnects before the operation completes, MongoDB marks `db.getCollectionNames()` 
for termination using `killOp`.

### Replica Set Member State Restriction

To run on a replica set member, `listCollections` operations require the member 
to be in `PRIMARY` or `SECONDARY` state. If the member
is in another state, such as `STARTUP2`, the
operation errors.

## Example

The following returns the names of all collections in the `records`
database:

```javascript
use records
db.getCollectionNames()
```

The method returns the names of the collections in an array:

```javascript
[ "employees", "products", "mylogs", "system.indexes" ]
```
