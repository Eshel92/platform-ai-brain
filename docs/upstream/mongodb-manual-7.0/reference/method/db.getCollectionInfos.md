<!-- Converted from reference/method/db.getCollectionInfos.txt (reStructuredText). Includes are inlined. -->

# db.getCollectionInfos() (mongosh method)

## Definition

**`db.getCollectionInfos(filter, options)`**

Returns an array of documents that contain collection or view information, such as name and options, for the
current database. The results depend on the user's privilege. For
details, see db.getCollectionInfo-access-control.

The `db.getCollectionInfos()` helper wraps the
`listCollections` command.

## Syntax

The `db.getCollectionInfos()` method has the following 
parameters:

| Parameter | Type | Description |
|---|---|---|
| `filter` | document | Optional. A query predicate to filter the list of collections. You can specify a query predicate on any of the fields returned by `db.getCollectionInfos()`. |
| `options` | document | Optional. A document that specifies additional options for the command. For a list of available options, see dbCollectionInfos-options. |

### Options

You can specify the following options in the `options` document of a
`db.getCollectionInfos()` command:

* - Option
  - Type
  - Description

* - `nameOnly`
  - boolean
  - .. include:: /includes/listCollections-nameOnly-option.rst

    For an example, see dbCollectionInfos-example-nameOnly.

* - `authorizedCollections`
  - boolean
  - Optional. When set to `true` and used with ``nameOnly:
    true``, allows a user without the required privilege (such as the
    `listCollections` action on the database) to run
    `db.getCollectionInfos()` when access control is enforced.

    When both `authorizedCollections` and `nameOnly` options are
    set to true, the command returns only those collections for
    which the user has privileges. For example:

    - If a user has the `find` action on specific
      collections, the command returns only those collections.

    - If a user has any permission action on the database resource,
      the command lists all collections in the database.

    The default value is `false`, meaning the user must have
    `listCollections` action on the database to run the
    command.

    For a user who has `listCollections` action on the
    database, this option has no effect since the user has privileges to
    list the collections in the database.

    When used without `nameOnly: true`, this option has no effect.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
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

The `listCollections` command and its wrapper
`db.getCollectionInfos()` require the
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

If the client that issued `db.getCollectionInfos()` disconnects before the operation 
completes, MongoDB marks `db.getCollectionInfos()` for termination using 
`killOp`.

### Replica Set Member State Restriction

To run on a replica set member, `listCollections` operations require the member 
to be in `PRIMARY` or `SECONDARY` state. If the member
is in another state, such as `STARTUP2`, the
operation errors.

## Examples

### Return Information for All Collections in a Database

The following returns information for all collections in the
`example` database:

```javascript
use example
db.getCollectionInfos()
```

Output:

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

### Return Only Collection Names

To return only the names of collections in the current database,
specify the `nameOnly: true` option. For example:

```javascript
use example
db.getCollectionInfos( {}, { nameOnly: true } )
```

Output:

```javascript
[
  { name: 'products', type: 'collection' },
  { name: 'weather', type: 'timeseries' },
  { name: 'system.buckets.weather', type: 'collection' },
  { name: 'system.views', type: 'collection' },
  { name: 'sales', type: 'collection' }
]
```

### Return Information for a Specific Collection

To request collection information for a specific collection, specify the
collection name in the filter document. The following example returns an
array with a single document that details the collection information for
the `employees` collection in the `example` database.

```javascript
use example
db.getCollectionInfos( { name: "employees" } )
```

Output:

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

### Return Information for Read-Only Collections

You can specify a filter on any of the fields returned by
`db.getCollectionInfos()`.

For example, the following command returns information for all
collections in the `example` database where `info.readOnly` is
`true`:

```javascript
use example
db.getCollectionInfos( { "info.readOnly" : true } )
```

Output:

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
