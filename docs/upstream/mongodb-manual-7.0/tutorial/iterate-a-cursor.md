<!-- Converted from tutorial/iterate-a-cursor.txt (reStructuredText). Includes are inlined. -->

# Iterate a Cursor in `mongosh`

This tutorial demonstrates how to access documents in a cursor. 

## About This Task

To access documents in a cursor, you can manually iterate the cursor or use
the `toArray()` method.

This tutorial overviews how to: 

- Save a cursor as a variable using the `let` keyword.

- Use the `next()`, `hasNext()`, and `forEach()` methods to
  access documents in a cursor.

- Return and access the cursor documents as an array with the
  `toArray()` method.

### Batch Sizes

A cursor returns documents in batches. By default, mongosh 
displays 20 documents per cursor iteration. You can use
config.set("displayBatchSize") to change it, if this is too
much or too little for your needs.

## Before You Begin

- Install mongosh.

- Connect to a deployment.

### Insert Documents Into a New Collection

Use `mongosh` to insert documents into a new collection using the default
`test` database:

```javascript
db.users.insertMany( [ 
   { _id: 0, type: "admin", email: "admin@example.com", name: "Admin User" }, 
   { _id: 1, type: "user", email: "user1@example.com", name: "Test User 1" }, 
   { _id: 2, type: "user", email: "user2@example.com", name: "Test User 2" }
] )
```

## Examples

### Save a Cursor with `let`

In `mongosh`, the cursor does not automatically iterate when you
assign it to a variable using the `let` keyword.

```javascript
let myCursor = db.users.find( { type: "user" } )
```

You can call the cursor variable in the shell to print matching
documents.

```javascript
myCursor
```

Output:

```shell
[
   {
      _id: 1,
      type: 'user',
      email: 'user1@example.com',
      name: 'Test User 1'
   },
   {
      _id: 2,
      type: 'user',
      email: 'user2@example.com',
      name: 'Test User 2'
   }
]
```

If the returned cursor is not assigned to a variable using the
`let` keyword, then the cursor is automatically iterated up to
the batch size, printing the first batch of results.

```javascript
db.users.find( { type: "user" } )
```

Output:

```shell
[
   {
      _id: 1,
      type: 'user',
      email: 'user1@example.com',
      name: 'Test User 1'
   },
   {
      _id: 2,
      type: 'user',
      email: 'user2@example.com',
      name: 'Test User 2'
   }
]
```

### Access Documents in a Cursor with `next()`

You can also use the cursor method `next()` to access
the documents. `next()` returns the document the cursor
currently points and then moves the cursor forward to the next document.

```javascript
let myCursor = db.users.find( { type: "user" } )

myCursor.next()
```

Output:

```shell
{
   _id: 1,
   type: 'user',
   email: 'user1@example.com',
   name: 'Test User 1'
}
```

### Access Documents in a Cursor with `hasNext()`

The cursor method `hasNext()` returns `true` or
`false` to indicate if there are more documents to be returned from the cursor.

```javascript
let myCursor = db.users.find( { type: "user" } )

myCursor.hasNext()
```

Output:

```shell
true
```

You can use the `hasNext()` and `next()` methods to print all remaining documents from the cursor using
the `printjson()` helper.

```javascript
let myCursor = db.users.find( { type: "user" } )

while ( myCursor.hasNext() ) { 
   printjson( myCursor.next() )
}
```

Output:

```shell
{
   _id: 1,
   type: 'user',
   email: 'user1@example.com',
   name: 'Test User 1'
}
{
   _id: 2,
   type: 'user',
   email: 'user2@example.com',
   name: 'Test User 2'
}
```

### Access Documents in a Cursor with `forEach()`

Similarly, you can use the cursor method `forEach()`
to apply a helper, such as `printjson()`, to each document in the cursor.

```javascript
let myCursor = db.users.find( { type: "user" } )

myCursor.forEach( myDocument => printjson(myDocument) )
```

Output:

```shell
{
   _id: 1,
   type: 'user',
   email: 'user1@example.com',
   name: 'Test User 1'
}
{
   _id: 2,
   type: 'user',
   email: 'user2@example.com',
   name: 'Test User 2'
}
```

Starting in `mongosh` 2.1.0, you can also use `for-of` loops to
iterate the cursor. The following example returns the same results as the
previous example.

```javascript
let myCursor = db.users.find( { type: "user" } )

for ( let myDocument of myCursor ) {
   printjson( myDocument )
}
```

Output:

```shell
{
   _id: 1,
   type: 'user',
   email: 'user1@example.com',
   name: 'Test User 1'
}
{
   _id: 2,
   type: 'user',
   email: 'user2@example.com',
   name: 'Test User 2'
}
```

See JavaScript cursor methods and your
`driver` documentation for more information on cursor methods.

### Access Documents in a Cursor with `toArray()`

In `mongosh`, use the `toArray()` method to
iterate the cursor and return the documents in an array.

```javascript
let myCursor = db.users.find( { type: "user" } )

let documentArray = myCursor.toArray()

documentArray
```

Output:

```shell
[
   {
      _id: 1,
      type: 'user',
      email: 'user1@example.com',
      name: 'Test User 1'
   },
   {
      _id: 2,
      type: 'user',
      email: 'user2@example.com',
      name: 'Test User 2'
   }
]
```

You can access the resulting document array as a traditional array.

```javascript
let myCursor = db.users.find( { type: "user" } )

let documentArray = myCursor.toArray()

documentArray[1]
```

Output:

```shell
{
   _id: 2,
   type: 'user',
   email: 'user2@example.com',
   name: 'Test User 2'
}
```

The `toArray()` method loads all documents returned by the
cursor into RAM and exhausts the cursor.

Some `Drivers` provide access to the documents by using an index on
the cursor (i.e. `cursor[index]`). This is a shortcut for first calling the
`toArray()` method and then using an index on the resulting
array.

```javascript
let myCursor = db.users.find( { type: "user" } )

myCursor.toArray() [1]
```

Output:

```shell
{
   _id: 2,
   type: 'user',
   email: 'user2@example.com',
   name: 'Test User 2'
}
```
