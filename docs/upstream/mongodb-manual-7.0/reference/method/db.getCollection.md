<!-- Converted from reference/method/db.getCollection.txt (reStructuredText). Includes are inlined. -->

# db.getCollection() (mongosh method)

## Definition

**`db.getCollection(name)`**

Returns a collection or a view object
that is functionally equivalent to using the `db.<collectionName>`
syntax. The method is useful for a collection or a view whose name
might interact with `mongosh` itself, such as names
that begin with `_` or that match a database shell method.

The `db.getCollection()` method has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `name` | string | The name of the collection. |

          
          

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

## Behavior

The `db.getCollection()` object can access any
collection methods.

The collection specified may or may not exist on the server.  If the collection
does not exist, MongoDB creates it implicitly as part of 
write operations like 
`db.collection.insertOne()`.

## Example

The following example uses `db.getCollection()` to access the
`auth` collection and insert a document into it.

```javascript
var authColl = db.getCollection("auth")

authColl.insertOne(
   {
       usrName : "John Doe",
       usrDept : "Sales",
       usrTitle : "Executive Account Manager",
       authLevel : 4,
       authDept : [ "Sales", "Customers"]
   }
)
```

This returns:

```javascript
{
   "acknowledged" : true,
   "insertedId" : ObjectId("569525e144fe66d60b772763")
}
```

The previous example requires the use of 
`db.getCollection("auth")` because
of a name conflict with the database method `db.auth()`.  Calling
`db.auth` directly to perform an insert operation would reference the
`db.auth()` method and would error.

The following example attempts the same operation, but without using the
`db.getCollection()` method:

```javascript
db.auth.insertOne(
   {
       usrName : "John Doe",
       usrDept : "Sales",
       usrTitle : "Executive Account Manager",
       authLevel : 4,
       authDept : [ "Sales", "Customers"]
   }
)
```

The operation errors as `db.auth()` method has no `insertOne`
method.

**See also:**

collection-method
