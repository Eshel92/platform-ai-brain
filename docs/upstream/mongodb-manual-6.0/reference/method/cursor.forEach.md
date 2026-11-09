<!-- Converted from reference/method/cursor.forEach.txt (reStructuredText). Includes are inlined. -->

# cursor.forEach()

## Definition

**`cursor.forEach(function)`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Iterates the cursor to apply a JavaScript `function` to each
document from the cursor.

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

## Syntax

The method has the following syntax:

```javascript
db.collection.find().forEach( <function> )
```

## Method Fields

The method accepts the following field:

| Field | Type | Description |
|---|---|---|
| `function` | JavaScript code | Function to apply to each document returned from the cursor. The function signature includes one field that stores the current document that is read from the cursor. |

## Examples

Create the `users` collection:

```none
db.users.insertMany( [
   { name: "John" },
   { name: "Jane" }
] )
```

The following example uses `forEach()` with the
`find()` method to print the user names that are
read from the `users` collection. `myDoc` stores the current
document.

```none
db.users.find().forEach( function( myDoc ) {
   print( "User name: " + myDoc.name )
} )
```

Example output:

```none
User name: John
User name: Jane
```

Starting in `mongosh` 2.1.0, you can also use `for-of`
loops. The following example returns the same results as the previous
example:

```none
for ( const myDoc of db.users.find() ) {
   print( "User name: " + myDoc.name )
}
```

## Learn More

For a method that has similar functionality, see `cursor.map()`.
