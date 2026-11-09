<!-- Converted from reference/command/listCollections.txt (reStructuredText). Includes are inlined. -->

# listCollections

## Definition

**`listCollections`**

Retrieves information, including the names and creation options, for
the collections and views in a database. 

The `listCollections` command returns a document that contains
information you can use to create a cursor on the collection. 

`mongosh` provides the `db.getCollectionInfos()`
and the `db.getCollectionNames()` helper methods.

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
db.runCommand(
   { 
     listCollections: 1, 
     filter: <document>, 
     nameOnly: <boolean>, 
     authorizedCollections: <boolean>, 
     comment: <any> 
   }
)
```

## Command Fields

The command can take the following optional fields:

| Field | Type | Description |
|---|---|---|
| `filter` | document | Optional. A query expression to filter the list of collections. You can specify a query expression on any of the fields returned by `listCollections`. |
| `nameOnly` | boolean | .. include:: /includes/listCollections-nameOnly-option.rst |
| `authorizedCollections` | boolean | Optional. A flag, when set to `true` and used with `nameOnly: true`, that allows a user without the required privilege (i.e. `listCollections` action on the database) to run the command when access control is enforced. When both `authorizedCollections` and `nameOnly` options are set to true, the command returns only those collections for which the user has privileges. For example, if a user has `find` action on specific collections, the command returns only those collections; or, if a user has `find` or any other action, on the database resource, the command lists all collections in the database. The default value is `false`. That is, the user must have `listCollections` action on the database to run the command. For a user who has `listCollections` action on the database, this option has no effect since the user has privileges to list the collections in the database. When used without `nameOnly: true`, this option has no effect. That is, the user must have the required privileges to run the command when access control is enforced. Otherwise, the user is unauthorized to run the command. |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst Any comment set on a `listCollections` command is inherited by any subsequent `getMore` commands run on the `listCollections` cursor. |

## Behavior

### Filter

Use a filter to limit the results of `listCollections`. You
can specify a `filter` on any of the fields returned in the `listCollections` result
set.

### Locks

`listCollections` lock behavior:

- Earlier than MongoDB 5.0, `listCollections` takes an intent
  shared lock lock on each collection in the database
  when `listCollections` holds an intent shared lock on the database.

- Starting in MongoDB 5.0, `listCollections` doesn't take an intent
  shared lock on a collection or database. `listCollections` isn't
  blocked by operations holding an exclusive write lock on a collection.

To learn about locks, see faq-concurrency-locking.

### Client Disconnection

Starting in MongoDB 4.2, if the client that issued `listCollections`
disconnects before the operation completes, MongoDB marks `listCollections` 
for termination using `killOp`.

### Replica Set Member State Restriction

To run on a replica set member, `listCollections` operations require the member 
to be in `PRIMARY` or `SECONDARY` state. If the member
is in another state, such as `STARTUP2`, the
operation errors.

## Required Access

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

## Output

**`listCollections.cursor`**

A document that contains information with which to create a cursor
to documents that contain collection names and options. The cursor
information includes the cursor id, the full namespace for the
command, as well as the first batch of results. Each document in the
batch output contains the following fields:

| Field | Type | Description |
|---|---|---|
| name | String | Name of the collection. |
| type | String | Type of data store. Returns `collection` for collections, `view` for views, and `timeseries` for time series collection. |
| options | Document | Collection options. These options correspond directly to the options available in `db.createCollection()`. For the descriptions on the options, see `db.createCollection()`. |
| info | Document | Lists the following fields related to the collection: readOnly `boolean`. If `true` the data store is read only. uuid UUID (Universally unique identifier). Once established, the collection UUID does not change. The collection UUID remains the same across replica set members and shards in a sharded cluster. |
| idIndex | Document | Provides information on the `_id` index for the collection. |

**`listCollections.ok`**

The return value for the command. A value of `1` indicates
success.

## Example

### List All Collections

The `music` database contains three collections, `motorhead`, 
`taylorSwift`, and `ramones`.

To list the collections in the database, you can use the built-in
`mongosh` command, show collections.

```javascript
show collections
```

The output is:

```javascript
motorhead
ramones
taylorSwift
```

To get a similar list with the `listCollections` collections command,
use the `nameOnly` option.

```javascript
db.runCommand(
   {
      listCollections: 1.0,
      nameOnly: true
   }
)
```

The output is:

```javascript
{
  cursor: {
    id: Long("0"),
    ns: 'music.$cmd.listCollections',
    firstBatch: [
      { name: 'motorhead', type: 'collection' },
      { name: 'taylorSwift', type: 'collection' },
      { name: 'ramones', type: 'collection' }
    ]
  },
  ok: 1
}
```

To get more detailed information, remove the `nameOnly` option.

```javascript
db.runCommand(
   {
      listCollections: 1.0
   }
)
```

The output is:

```javascript
{
  cursor: {
    id: Long("0"),
    ns: 'music.$cmd.listCollections',
    firstBatch: [
      {
        name: 'motorhead',
        type: 'collection',
        options: {},
        info: {
          readOnly: false,
          uuid: new UUID("09ef1858-2831-47d2-a3a7-9a29a9cfeb94")
        },
        idIndex: { v: 2, key: { _id: 1 }, name: '_id_' }
      },
      {
        name: 'taylorSwift',
        type: 'collection',
        options: {},
        info: {
          readOnly: false,
          uuid: new UUID("6c46c8b9-4999-4213-bcef-9a36b0cff228")
        },
        idIndex: { v: 2, key: { _id: 1 }, name: '_id_' }
      },
      {
        name: 'ramones',
        type: 'collection',
        options: {},
        info: {
          readOnly: false,
          uuid: new UUID("7e1925ba-f2f9-4e42-90e4-8cafd434a6c4")
        },
        idIndex: { v: 2, key: { _id: 1 }, name: '_id_' }
      }
    ]
  },
  ok: 1
}
```

## Learn More

For collection options:

- `db.createCollection()`
- `create`

For collection information:

- `db.getCollectionInfos()`
- mongosh built-in commands
