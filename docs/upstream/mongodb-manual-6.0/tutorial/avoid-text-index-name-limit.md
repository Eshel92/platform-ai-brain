<!-- Converted from tutorial/avoid-text-index-name-limit.txt (reStructuredText). Includes are inlined. -->

# Specify Name for `text` Index

**Note:** Changed in MongoDB 4.2

MongoDB removes the index name length limit of 127 byte maximum. 

The default name for the index consists of each indexed field name
concatenated with `_text`. For example, the following command creates
a `text` index on the fields `content`, `users.comments`, and
`users.profiles`:

```javascript
db.collection.createIndex(
   {
     content: "text",
     "users.comments": "text",
     "users.profiles": "text"
   }
)
```

The default name for the index is:

```javascript
"content_text_users.comments_text_users.profiles_text"
```

## Specify a Name for `text` Index

You can pass the `name` option to the
`db.collection.createIndex()` method:

```javascript
db.collection.createIndex(
   {
     content: "text",
     "users.comments": "text",
     "users.profiles": "text"
   },
   {
     name: "MyTextIndex"
   }
)
```

## Use the Index Name to Drop a `text` Index

Whether the text index has the default name
or you specified a name for the text index,
to drop the text index, pass the index name
to the `db.collection.dropIndex()` method.

For example, consider the index created by the following operation:

```javascript
db.collection.createIndex(
   {
     content: "text",
     "users.comments": "text",
     "users.profiles": "text"
   },
   {
     name: "MyTextIndex"
   }
)   
```

Then, to remove this text index, pass the name `"MyTextIndex"` to the
`db.collection.dropIndex()` method, as in the following:

```javascript
db.collection.dropIndex("MyTextIndex")
```

To get the names of the indexes, use the
`db.collection.getIndexes()` method.
