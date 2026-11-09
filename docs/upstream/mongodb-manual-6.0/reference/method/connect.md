<!-- Converted from reference/method/connect.txt (reStructuredText). Includes are inlined. -->

# connect()

## Description

**`connect(url, user, password)`**

Creates a connection to a MongoDB instance and returns the reference
to the database. However, in most cases, use the `Mongo()`
object and its `getDB()` method instead.

* - Parameter

  - Type

  - Description

* - `url`

  - string

  - Specifies the connection string.
    You can specify either:

    - `<hostname>:<port>/<database>`
    - `<hostname>/<database>`
    - `<database>`

* - `user`

  - string

  - Optional. Specifies an existing username with access privileges for this database.
    If `user` is specified, you must include the `password` parameter as well.

* - `password`

  - string

  - Optional unless the `user` parameter is specified. Specifies the
    password for the `user`.
          

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Example

The following example instantiates a new connection to the MongoDB
instance running on the localhost interface and returns a reference
to `myDatabase`:

```javascript
db = connect("localhost:27017/myDatabase")
```

**See also:**

- `Mongo()`
- `Mongo.getDB()`
- `db.auth()`
