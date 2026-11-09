<!-- Converted from reference/method/db.getCollectionInfos.txt (reStructuredText). Includes are inlined. -->

# db.getCollectionInfos()

## Definition

**`db.getCollectionInfos(filter, nameOnly, authorizedCollections)`**

Returns an array of documents with collection or view information, such as  name and options, for
the current database. The results depend on the user's
privilege. For details, see db.getCollectionInfo-access-control.

The `db.getCollectionInfos()` helper wraps the
`listCollections` command.

The `db.getCollectionInfos()` method has the following 
optional parameter:

| Parameter | Type | Description |
|---|---|---|
| `filter` | document | Optional. A query expression to filter the list of collections. You can specify a query expression on any of the fields returned by `db.getCollectionInfos`. |
| `nameOnly` | boolean | .. include:: /includes/listCollections-nameOnly-option.rst |
| `authorizedCollections` | boolean | Optional. A flag, when set to `true` and used with `nameOnly: true`, that allows a user without the required privilege (i.e. `listCollections` action on the database) to run the command when access control is enforced. When both `authorizedCollections` and `nameOnly` options are set to true, the command returns only those collections for which the user has privileges. For example, if a user has `find` action on specific collections, the command returns only those collections; or, if a user has `find` or any other action, on the database resource, the command lists all collections in the database. The default value is `false`. That is, the user must have `listCollections` action on the database to run the command. For a user who has `listCollections` action on the database, this option has no effect since the user has privileges to list the collections in the database. When used without `nameOnly: true`, this option has no effect. That is, the user must have the required privileges to run the command when access control is enforced. Otherwise, the user is unauthorized to run the command. |

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

Since `db.getCollectionInfos()` is a wrapper around the
`listCollections`, users must have the same privileges as
`listCollections` when access control is enforced.

The `listCollections` command requires the
`listCollections` action when access control is enforced.
Users must have privileges that grant the `listCollections` action
on the database to run `listCollections`.

For example, the following command grants the privilege to run
`db.getCollectionInfos()` against the `test` database:

```javascript
{ resource: { db: "test", collection: "" }, actions: [ "listCollections" ] }
```

The built-in role `read` provides the privilege to run
`listCollections` for a specific database.

Users without the required `read` privilege can run
`listCollections` when `authorizedCollections` and `nameOnly`
are both set to `true`. In this case, the command returns the names
and types for collection(s) where the user has privileges.

For example, consider a user with a role that grants the following
`find` privilege:

```javascript
{ resource: { db: "sales", collection: "currentQuarter" }, actions: [ "find" ] }
```

The user can run `listCollections` if  `authorizedCollections`
and `nameOnly` are both set to `true`.

```javascript
db.runCommand(
   {
       listCollections: 1.0,
       authorizedCollections: true,
       nameOnly: true
   }
)
```

The operation returns the name and type of the `currentQuarter`
collection.

However, the following operations return an error if the user does
not have the required access authorization:

```javascript
db.runCommand(
   {
       listCollections: 1.0,
       authorizedCollections: true
   }
)

db.runCommand(
   {
       listCollections: 1.0,
       nameOnly: true
   }
)
```

### `show collections`

The `mongosh` method `show collections` is similar to:

```javascript
db.runCommand(
   {
       listCollections: 1.0,
       authorizedCollections: true,
       nameOnly: true
   }
)
```

- For users with the required access, `show collections` lists the
  non-system collections for the database.

- For users without the required access, `show collections` lists
  only the collections for which the users has privileges.

## Behavior

### Client Disconnection

Starting in MongoDB 4.2, if the client that issued `db.getCollectionInfos()`
disconnects before the operation completes, MongoDB marks `db.getCollectionInfos()` 
for termination using `killOp`.

### Replica Set Member State Restriction

To run on a replica set member, `listCollections` operations require the member 
to be in `PRIMARY` or `SECONDARY` state. If the member
is in another state, such as `STARTUP2`, the
operation errors.

## Example

The following returns information for all collections in the
`example` database:

```javascript
use example
db.getCollectionInfos()
```

The method returns an array of documents that contain collection
information:

```javascript
[
   {
      "name" : "employees",
      "type" : "collection",
      "options" : {
         "flags" : 1,
         "validator" : {
            "$or" : [
               {
                  "phone" : {
                     "$exists" : true
                  }
               },
               {
                  "email" : {
                     "$exists" : true
                  }
               }
            ]
         }
      },
      "info" : {
         "readOnly" : false,
         "uuid" : UUID("222e18ca-4a10-4a42-a8fe-c39255cc4c55")
      },
      "idIndex" : {
         "v" : 2,
         "key" : {
            "_id" : 1
         },
         "name" : "_id_",
         "ns" : "example.employees"
      }
   },
   {
      "name" : "products",
      "type" : "collection",
      "options" : {
         "flags" : 1
      },
      "info" : {
         "readOnly" : false,
         "uuid" : UUID("1bc898b2-3b91-45e4-9d8b-0be462d5a157")
      },
      "idIndex" : {
         "v" : 2,
         "key" : {
            "_id" : 1
         },
         "name" : "_id_",
         "ns" : "example.products"
      }
   },
   {
      "name" : "mylogs",
      "type" : "collection",
      "options" : {
         "capped" : true,
         "size" : 256
      },
      "info" : {
         "readOnly" : true,
         "uuid" : UUID("8e62116d-b6a0-490a-808c-258ccb7ea947")
      },
      "idIndex" : {
         "v" : 2,
         "key" : {
            "_id" : 1
         },
         "name" : "_id_",
         "ns" : "example.mylogs"
      }
   }
]
```

To request collection information for a *specific* collection,
specify the collection name when calling the method, as in the following:

```javascript
use example
db.getCollectionInfos( { name: "employees" } )
```

The method returns an array with a single document that details the
collection information for the `employees` collection in the
`example` database.

```javascript
[
   {
      "name" : "employees",
      "type" : "collection",
      "options" : {
         "flags" : 1,
         "validator" : {
            "$or" : [
               {
                  "phone" : {
                     "$exists" : true
                  }
               },
               {
                  "email" : {
                     "$exists" : true
                  }
               }
            ]
         }
      },
      "info" : {
         "readOnly" : false,
         "uuid" : UUID("222e18ca-4a10-4a42-a8fe-c39255cc4c55")
      },
      "idIndex" : {
         "v" : 2,
         "key" : {
            "_id" : 1
         },
         "name" : "_id_",
         "ns" : "example.employees"
      }
   }
]
```

You can specify a filter on any of the fields returned by
`db.getCollectionInfos()`.

For example, the following command returns information for all
collections in the `example` database where `info.readOnly` is
`true`:

```javascript
use example
db.getCollectionInfos( { "info.readOnly" : true } )
```

The command returns the following:

```javascript
[
   {
      "name" : "mylogs",
      "type" : "collection",
      "options" : {
         "capped" : true,
         "size" : 256
      },
      "info" : {
         "readOnly" : true,
         "uuid" : UUID("8e62116d-b6a0-490a-808c-258ccb7ea947")
      },
      "idIndex" : {
         "v" : 2,
         "key" : {
            "_id" : 1
         },
         "name" : "_id_",
         "ns" : "example.mylogs"
      }
   }
]
```
