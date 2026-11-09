<!-- Converted from reference/operator/aggregation/unset.txt (reStructuredText). Includes are inlined. -->

# $unset (aggregation)

## Definition

**Note:** Disambiguation

The following page refers to the aggregation stage
`$unset`. For the update operator `$unset`, see
`$unset`.

**`$unset`**

Removes/excludes fields from documents.

## Syntax

The `$unset` stage has the following syntax:

- To remove a single field, the `$unset` takes a string that
  specifies the field to remove:

  ```javascript
  { $unset: "<field>" }
  ```

- To remove multiple fields, the `$unset` takes an array of
  fields to remove.

  ```javascript
  { $unset: [ "<field1>", "<field2>", ... ] }
  ```

## Considerations

### `$unset` and `$project`

The `$unset` is an alias for the `$project`
stage that removes/excludes fields:

```javascript
{ $project: { "<field1>": 0, "<field2>": 0, ... } }
```

### Embedded Fields

To remove/exclude a field or fields within an embedded document, you
can use the dot notation, as in:

```javascript
{ $unset: "<field.nestedfield>" }
```

or

```javascript
{ $unset: [ "<field1.nestedfield>", ...] }
```

## Examples

Create a sample `books` collection with the following documents:

```javascript
db.books.insertMany([
   { "_id" : 1, title: "Antelope Antics", isbn: "0001122223334", author: { last:"An", first: "Auntie" }, copies: [ { warehouse: "A", qty: 5 }, { warehouse: "B", qty: 15 } ] },
   { "_id" : 2, title: "Bees Babble", isbn: "999999999333", author: { last:"Bumble", first: "Bee" }, copies: [ { warehouse: "A", qty: 2 }, { warehouse: "B", qty: 5 } ] }
])
```

### Remove a Single Field

The following example removes the top-level field `copies`:

```javascript
db.books.aggregate([ { $unset: "copies" } ])
```

Alternatively, you can also use the following syntax:

```javascript
db.books.aggregate([ { $unset: [ "copies" ] } ])
```

Either operation returns the following documents:

```javascript
{ "_id" : 1, "title" : "Antelope Antics", "isbn" : "0001122223334", "author" : { "last" : "An", "first" : "Auntie" } }
{ "_id" : 2, "title" : "Bees Babble", "isbn" : "999999999333", "author" : { "last" : "Bumble", "first" : "Bee" } }
```

### Remove Top-Level Fields

The following example removes the top-level fields `isbn` and
`copies`:

```javascript
db.books.aggregate([
   { $unset: [ "isbn", "copies" ] }
])
```

The `$unset` operation outputs the following documents:

```javascript
{ "_id" : 1, "title" : "Antelope Antics", "author" : { "last" : "An", "first" : "Auntie" } }
{ "_id" : 2, "title" : "Bees Babble", "author" : { "last" : "Bumble", "first" : "Bee" } }
```

### Remove Embedded Fields

The following example removes the top-level field `isbn`, the
embedded field `first` (from the `name` document) and the embedded field
`warehouse` (from the elements in the `copies` array):

```javascript
db.books.aggregate([
   { $unset: [ "isbn", "author.first", "copies.warehouse" ] }
])
```

The `$unset` operation outputs the following documents:
 

```javascript
{ "_id" : 1, "title" : "Antelope Antics", "author" : { "last" : "An" }, "copies" : [ { "qty" : 5 }, { "qty" : 15 } ] }
{ "_id" : 2, "title" : "Bees Babble", "author" : { "last" : "Bumble" }, "copies" : [ { "qty" : 2 }, { "qty" : 5 } ] }
```
