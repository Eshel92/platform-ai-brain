<!-- Converted from reference/method/cursor.isExhausted.txt (reStructuredText). Includes are inlined. -->

# cursor.isExhausted() (mongosh method)

**`cursor.isExhausted()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

:returns: Boolean

`cursor.isExhausted()` returns `false` if documents remain
in the current document batch read by the cursor. Otherwise,
returns `true`.

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

### Tailable Cursors

You can use `isExhausted()` with a tailable cursor. A tailable cursor stays open even if
no documents remain in the current batch. Other cursors are
automatically closed when no documents remain.

### Change Streams

You cannot use `isExhausted()` with change streams. Instead, to examine if:

- documents remain in a change stream cursor, use
  `cursor.tryNext()`.
- a change stream cursor is closed, use `cursor.isClosed()`.

For change stream examples, see Watch Example
and Change Stream Images Example.

## Examples

This section contains examples that use a cursor to read documents from
a collection with temperature readings from a weather sensor. You'll see
examples of `isExhausted()`.

**Step 1: Create the collection**

Run:

```javascript
db.sensor.insertMany( [
   { _id: 0, temperature: 12 },
   { _id: 1, temperature: 23 }
] )
```

**Step 2: Create a cursor variable**

Create a cursor variable named `sensorCursor` that reads the
documents from the `sensor` collection:

```javascript
var sensorCursor = db.sensor.find()
```

**Step 3: Count the number of documents in the cursor**

Run:

```javascript
sensorCursor.count()
```

The output is `2` because there are two documents in the
collection.

**Step 4: Return the first document from the cursor**

Run:

```javascript
sensorCursor.next()
```

Output:

```javascript
{ _id: 0, temperature: 12 }
```

**Step 5: Examine the `isExhausted()` value**

Run:

```javascript
sensorCursor.isExhausted()
```

The output is `false` because there is a remaining document
in `sensorCursor`.

**Step 6: Return the next document from the cursor**

Run:

```javascript
sensorCursor.next()
```

Output:

```javascript
{ _id: 1, temperature: 23 }
```

**Step 7: Attempt to return the next document from the cursor**

Run:

```javascript
sensorCursor.next()
```

There are no more documents and the example returns `null`.

**Step 8: Examine the `isExhausted()` value**

Run:

```javascript
sensorCursor.isExhausted()
```

There are no more documents and `isExhausted()` returns
`true`.
