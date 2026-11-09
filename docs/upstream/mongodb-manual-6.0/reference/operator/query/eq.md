<!-- Converted from reference/operator/query/eq.txt (reStructuredText). Includes are inlined. -->

# $eq

**`$eq`**

Specifies equality condition. The `$eq` operator matches
documents where the value of a field equals the specified value.

## Compatibility

You can use `$eq` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$eq` operator has the following form:

```javascript
{ <field>: { $eq: <value> } }
```

Specifying the `$eq` operator is equivalent to using the form
`{ field: <value> }` except when the `<value>` is a regular 
expression. See below for examples. 

## Behavior

### Comparison Order

For comparison of different BSON type values, see the specified
BSON comparison order.

### Match a Document Value

If the specified `<value>` is a document, the order of the fields in
the document matters.

### Match an Array Value

If the specified `<value>` is an array, MongoDB matches documents
where the `<field>` matches the array exactly or the `<field>`
contains an element that matches the array exactly. The order of the
elements matters. For an example, see eq-match-array-value.

### Match a Regular Expression

The expression `{ field: <value> }` implicitly specifies a match on 
`<value>`. MongoDB translates the implicit match to a more explicit
form. 

When the `<value>` is fixed, like a particular string, the expression
is equivalent to using the `$eq` operator `{ field: { $eq: <value> } }`.

If `<value>` is a regular expression, the statement is expanded
using the `$regex` operator `{ field: { $regex: <value> } }`.

For examples illustrating this behaviour, see eq-regex-matching.

### Security Implications

Always use the explicit form `{ field: { $eq: <value> } }` with 
user-supplied input to avoid problems with maliciously formed queries.

## Examples

The following examples query against the `inventory` collection with
the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: { name: "ab", code: "123" }, qty: 15, tags: [ "A", "B", "C" ] },
   { _id: 2, item: { name: "cd", code: "123" }, qty: 20, tags: [ "B" ] },
   { _id: 3, item: { name: "ij", code: "456" }, qty: 25, tags: [ "A", "B" ] },
   { _id: 4, item: { name: "xy", code: "456" }, qty: 30, tags: [ "B", "A" ] },
   { _id: 5, item: { name: "mn", code: "000" }, qty: 20, tags: [ [ "A", "B" ], "C" ] }
] )
```

### Equals a Specified Value

The following example queries the `inventory` collection to select
all documents where the value of the `qty` field equals `20`:

```javascript
db.inventory.find( { qty: { $eq: 20 } } )
```

The query is equivalent to:

```javascript
db.inventory.find( { qty: 20 } )
```

Both queries match the following documents:

```javascript
[
   { _id: 2, item: { name: "cd", code: "123" }, qty: 20, tags: [ "B" ] },
   { _id: 5, item: { name: "mn", code: "000" }, qty: 20, tags: [ [ "A", "B" ], "C" ] }
]
```

### Field in Embedded Document Equals a Value

The following example queries the `inventory` collection to select
all documents where the value of the `name` field in the `item`
document equals `"ab"`. To specify a condition on a field in an
embedded document, use the dot notation.

```javascript
db.inventory.find( { "item.name": { $eq: "ab" } } )
```

The query is equivalent to:

```javascript
db.inventory.find( { "item.name": "ab" } )
```

Both queries match the following document:

```javascript
[ { _id: 1, item: { name: "ab", code: "123" }, qty: 15, tags: [ "A", "B", "C" ] } ]
```

**See also:**

Query Embedded Documents

### Array Element Equals a Value

The following example queries the `inventory` collection to select
all documents where the `tags` array contains an element with the
value `"B"` [#match-string-value]_:

```javascript
db.inventory.find( { tags: { $eq: "B" } } )
```

The query is equivalent to:

```javascript
db.inventory.find( { tags: "B" } )
```

Both queries match the following documents:

```javascript
[
   { _id: 1, item: { name: "ab", code: "123" }, qty: 15, tags: [ "A", "B", "C" ] },
   { _id: 2, item: { name: "cd", code: "123" }, qty: 20, tags: [ "B" ] },
   { _id: 3, item: { name: "ij", code: "456" }, qty: 25, tags: [ "A", "B" ] },
   { _id: 4, item: { name: "xy", code: "456" }, qty: 30, tags: [ "B", "A" ] }
]
```

**See also:**

- `$elemMatch`
- Query Arrays

### Equals an Array Value

The following example queries the `inventory` collection to select
all documents where the `tags` array equals exactly the specified
array or the `tags` array contains an element that equals the array
`[ "A", "B" ]`.

```javascript
db.inventory.find( { tags: { $eq: [ "A", "B" ] } } )
```

The query is equivalent to:

```javascript
db.inventory.find( { tags: [ "A", "B" ] } )
```

Both queries match the following documents:

```javascript
[
   { _id: 3, item: { name: "ij", code: "456" }, qty: 25, tags: [ "A", "B" ] },
   { _id: 5, item: { name: "mn", code: "000" }, qty: 20, tags: [ [ "A", "B" ], "C" ] }
]
```

### Regex Match Behaviour

The following examples demonstrate the differences in behavior between
implicit and explict regular expression matching. Consider a collection 
with these documents: 

```javascript
db.companies.insertMany( [
   { _id: 001, company: "MongoDB" },
   { _id: 002, company: "MongoDB2" }
] )
```

$eq match on a string
  A string expands to return the same values whether an implicit match
  or an explicit use of `$eq`. Both of these queries:

  ```javascript
  db.collection.find( { company: "MongoDB" }, {_id: 0 })
  db.collection.find( { company: { $eq: "MongoDB" } }, {_id: 0 } )
  ```

  return the following result: 

  ```javascript
  [ { company: "MongoDB" } ]
  ```

$eq match on a regular expression
   An explicit query using `$eq` and a regular expression will only 
   match an object which is also a regular expresssion. The example 
   query won't return anything since values in the `company` field 
   are strings.
   

   ```javascript
   db.companies.find( { company: { $eq: /MongoDB/ } }, {_id: 0 } )
   ```

      
Regular expression matches
   A query with an implicit match against a regular expression is
   equivalent to a making a query with the `$regex` operator. Both of
   these queries:

   ```javascript
   db.companies.find( { company: /MongoDB/ }, {_id: 0 })
   db.companies.find( { company: { $regex: /MongoDB/ } }, {_id: 0 } )
   ```

   return the same results:

   ```javascript
   [
      { company: "MongoDB" },
      { company: "MongoDB2" }  
   ]
   ```
