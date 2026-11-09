<!-- Converted from reference/method/db.getSiblingDB.txt (reStructuredText). Includes are inlined. -->

# db.getSiblingDB()

## Definition

**`db.getSiblingDB(<database>)`**

| Parameter | Type | Description |
|---|---|---|
| `database` | string | The name of a MongoDB database. |

:returns: A database object.

Used to return another database without modifying the
`db` variable in the shell environment.

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

## Example

You can use `db.getSiblingDB()` as an alternative to the ``use
<database>`` helper. This is particularly useful when writing scripts
using `mongosh` where the `use` helper is not
available. 

Consider a MongoDB instance with two databases, `users` and
`records`. The `active` collection is a part of the `users`
database. The `requests` collection is a part of the `records`
database.

### Specify a Database

This operation sets the `db` object to point to the database named
`users`, and then returns a `document count` for the `active` collection.

```javascript
db = db.getSiblingDB('users')
db.active.countDocuments()
```

### Use Multiple Databases

You can create multiple `db` objects, that refer to different
databases, as in the following sequence of operations:

```javascript
users = db.getSiblingDB('users')
records = db.getSiblingDB('records')

users.active.countDocuments()
users.active.findOne()

records.requests.countDocuments()
records.requests.findOne()
```

This operation creates two `db` objects. Each `db` object refers to
a different database, `users` or `records`.

For each database, the query returns:

- a `document count`, and 
- an `example document`

from a collection in that database.
