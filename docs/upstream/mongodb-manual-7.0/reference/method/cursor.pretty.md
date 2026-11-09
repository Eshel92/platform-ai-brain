<!-- Converted from reference/method/cursor.pretty.txt (reStructuredText). Includes are inlined. -->

# cursor.pretty() (mongosh method)

## Definition

**`cursor.pretty()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Configures the cursor to display results in a format that 
is easy to read.

The `pretty()` method has the following prototype form:

```javascript
db.collection.find(<query>).pretty()
```

## Behavior

The `pretty()` method:

- Does not change the output format in `mongosh`.
- Changes the output format in the legacy mongo shell.

## Examples

Consider the following document:

```javascript
db.books.insertOne({
    "_id" : ObjectId("54f612b6029b47909a90ce8d"),
    "title" : "A Tale of Two Cities",
    "text" : "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness...",
    "authorship" : "Charles Dickens"})
```

By default, `db.collection.find()` returns data in a dense format:

```javascript
db.books.find()
{ "_id" : ObjectId("54f612b6029b47909a90ce8d"), "title" : "A Tale of Two Cities", "text" : "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness...", "authorship" : "Charles Dickens" }
```

By using `cursor.pretty()` you can set the cursor to return data in a
format that is easier to read:

```javascript
db.books.find().pretty()
{
    "_id" : ObjectId("54f612b6029b47909a90ce8d"),
    "title" : "A Tale of Two Cities",
    "text" : "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness...",
    "authorship" : "Charles Dickens"
}
```
