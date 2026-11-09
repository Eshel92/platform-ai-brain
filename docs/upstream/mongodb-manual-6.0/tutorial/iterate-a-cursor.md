<!-- Converted from tutorial/iterate-a-cursor.txt (reStructuredText). Includes are inlined. -->

# Iterate a Cursor in `mongosh`

The `db.collection.find()` method returns a cursor. To access
the documents, you need to iterate the cursor. However, in
`mongosh`, if the returned cursor is not assigned to a
variable using the `var` keyword, then the cursor is automatically
iterated up to 20 times [#set-shell-batch-size]_ to print up to the
first 20 documents in the results.

The following examples describe ways to manually iterate the cursor to
access the documents or to use the iterator index.

## Manually Iterate the Cursor

In `mongosh`, when you assign the cursor returned from
the `find()` method to a variable using
the `var` keyword, the cursor does not automatically iterate.

You can call the cursor variable in the shell to iterate up to 20 times
[#set-shell-batch-size]_ and print the matching documents, as in the
following example:

```javascript
var myCursor = db.users.find( { type: 2 } );

myCursor
```

You can also use the cursor method `next()` to
access the documents, as in the following example:

```javascript
var myCursor = db.users.find( { type: 2 } );

while (myCursor.hasNext()) {
   print(tojson(myCursor.next()));
}
```

As an alternative print operation, consider the `printjson()` helper
method to replace `print(tojson())`:

```javascript
var myCursor = db.users.find( { type: 2 } );

while (myCursor.hasNext()) {
   printjson(myCursor.next());
}
```

You can use the cursor method `forEach()` to
iterate the cursor and access the documents, as in the following
example:

```javascript
var myCursor =  db.users.find( { type: 2 } );

myCursor.forEach(printjson);
```

See JavaScript cursor methods and your
`driver` documentation for more
information on cursor methods.

## Iterator Index

In `mongosh`, you can use the
`toArray()` method to iterate the cursor and return
the documents in an array, as in the following:

```javascript
var myCursor = db.inventory.find( { type: 2 } );
var documentArray = myCursor.toArray();
var myDocument = documentArray[3];
```

The `toArray()` method loads into RAM all
documents returned by the cursor; the `toArray()`
method exhausts the cursor.

Additionally, some `Drivers` provide
access to the documents by using an index on the cursor (i.e.
`cursor[index]`). This is a shortcut for first calling the
`toArray()` method and then using an index
on the resulting array.

Consider the following example:

```javascript
var myCursor = db.users.find( { type: 2 } );
var myDocument = myCursor[1];
```

The `myCursor[1]` is equivalent to the following example:

```javascript
myCursor.toArray() [1];
```
