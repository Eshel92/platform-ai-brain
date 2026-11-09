<!-- Converted from core/indexes/index-types/index-text/create-text-index.txt (reStructuredText). Includes are inlined. -->

# Create a Text Index on Self-Managed Deployments

**Note:**

This page describes text query capabilities for self-managed
(non-Atlas) deployments. For data hosted on MongoDB Atlas, MongoDB
offers an improved full-text query solution, Atlas Search and a vector search solution, Atlas Vector Search. 

Text indexes support text search queries on fields containing string
content. Text indexes improve performance when searching for specific
words or multi-word strings within string content. 

To create a text index, use the `db.collection.createIndex()`
method. To index a field that contains a string or an array of string
elements, specify the string `"text"` as the index key:

```javascript
db.<collection>.createIndex(
   {
      <field1>: "text",
      <field2>: "text",
      ...
   }
)
```

## About this Task

- .. include:: /includes/fact-text-index-limit-one.rst

- You can index multiple fields in a single text index. A text index can
  contain up to 32 fields. To see an example, see
  compound-text-index-example.

## Before You Begin

Create a `blog` collection with the following documents:

```javascript
db.blog.insertMany( [
   {
     _id: 1,
     content: "This morning I had a cup of coffee.",
     about: "beverage",
     keywords: [ "coffee" ]
   },
   {
     _id: 2,
     content: "Who likes chocolate ice cream for dessert?",
     about: "food",
     keywords: [ "poll" ]
   },
   {
     _id: 3,
     content: "My favorite flavors are strawberry and coffee",
     about: "ice cream",
     keywords: [ "food", "dessert" ]
   }
] )
```

## Procedures

The following examples show you how to:

- single-text-index-example

- compound-text-index-example

### Create a Single-Field Text Index

Create a text index on the `content` field:

```javascript
db.blog.createIndex( { "content": "text" } )
```

The index supports text search queries on the `content` field. For
example, the following query returns documents where the `content`
field contains the string `coffee`:

```javascript
db.blog.find(
   {
      $text: { $search: "coffee" }
   }
)
```

Output:

```javascript
[
   {
     _id: 1,
     content: 'This morning I had a cup of coffee.',
     about: 'beverage',
     keywords: [ 'coffee' ]
   },
   {
     _id: 3,
     content: 'My favorite flavors are strawberry and coffee',
     about: 'ice cream',
     keywords: [ 'food', 'dessert' ]
   }
]
```

#### Matches on Non-Indexed Fields

The `{ "content": "text" }` index only includes the `content` field,
and does not return matches on non-indexed fields. For example, the
following query searches the `blog` collection for the string
`food`:

```javascript
db.blog.find(
   {
      $text: { $search: "food" }
   }
)
```

The preceding query returns no documents. Although the string `food`
appears in documents `_id: 2` and `_id: 3`, it appears in the
`about` and `keywords` fields respectively. The `about` and
`keywords` fields are not included in the text index, and therefore do
not affect text search query results.

### Create a Compound Text Index

**Note:**

Before you can create the index in this example, you must drop
any existing text indexes on the `blog`
collection.

Create a compound text index on the `about` and `keywords` fields in
the `blog` collection:

```javascript
db.blog.createIndex(
   {
      "about": "text",
      "keywords": "text"
   }
)
```

The index supports text search queries on the `about` and `keywords`
fields. For example, the following query returns documents where the
string `food` appears in either the `about` or `keywords` field:

```javascript
db.blog.find(
   {
      $text: { $search: "food" }
   }
)
```

Output:

```javascript
[
  {
    _id: 3,
    content: 'My favorite flavors are strawberry and coffee',
    about: 'ice cream',
    keywords: [ 'food', 'dessert' ]
  },
  {
    _id: 2,
    content: 'Who likes chocolate ice cream for dessert?',
    about: 'food',
    keywords: [ 'poll' ]
  }
]
```
