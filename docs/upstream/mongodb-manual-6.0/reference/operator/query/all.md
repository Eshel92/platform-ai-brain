<!-- Converted from reference/operator/query/all.txt (reStructuredText). Includes are inlined. -->

# $all

**`$all`**

The `$all` operator selects the documents where the value of
a field matches all specified values. The matched documents can either 
contain a field with a value that is an array containing all the specified
elements, or a field with a single value matching the specified element.

## Compatibility

You can use `$all` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

To specify an `$all` expression, use the following prototype:

```javascript
{ <field>: { $all: [ <value1> , <value2> ... ] } }
```

## Behavior

### Equivalent to `$and` Operation

The `$all` is equivalent to an `$and` operation of the
specified values; i.e. the following statement:

```javascript
{ tags: { $all: [ "ssl" , "security" ] } }
```

is equivalent to:

```javascript
{ $and: [ { tags: "ssl" }, { tags: "security" } ] }
```

### Nested Array

When passed an array of a nested array (e.g. `[ [ "A" ] ]` ),
`$all` matches documents where the field contains the
nested array as an element (e.g. `field: [ [ "A" ], ... ]`), *or* the
field equals the nested array (e.g. `field: [ "A" ]`).

For example, consider the following query:

```javascript
db.articles.find( { tags: { $all: [ [ "ssl", "security" ] ] } } )
```

The query is equivalent to:

```javascript
db.articles.find( { $and: [ { tags: [ "ssl", "security" ] } ] } )
```

which is equivalent to:

```javascript
db.articles.find( { tags: [ "ssl", "security" ] } )
```

As such, the `$all` expression matches documents where the
`tags` field is an array that contains the nested array ``[ "ssl",
"security" ]`` or is an array that equals the nested array:

```javascript
tags: [ [ "ssl", "security" ], ... ]
tags: [ "ssl", "security" ]
```

### Empty Array

When passed an empty array, `$all` matches no documents. 

## Examples

The exampless in this section use the `inventory` collection that contains
the following documents:

```javascript
db.inventory.insertMany ( [
   {
      _id: ObjectId("5234cc89687ea597eabee675"),
      code: "xyz",
      tags: [ "school", "book", "bag", "headphone", "appliance" ],
      qty: [
            { size: "S", num: 10, color: "blue" },
            { size: "M", num: 45, color: "blue" },
            { size: "L", num: 100, color: "green" }
         ]
   }

   {
      _id: ObjectId("5234cc8a687ea597eabee676"),
      code: "abc",
      tags: [ "appliance", "school", "book" ],
      qty: [
            { size: "6", num: 100, color: "green" },
            { size: "6", num: 50, color: "blue" },
            { size: "8", num: 100, color: "brown" }
         ]
   }

   {
      _id: ObjectId("5234ccb7687ea597eabee677"),
      code: "efg",
      tags: [ "school", "book" ],
      qty: [
            { size: "S", num: 10, color: "blue" },
            { size: "M", num: 100, color: "blue" },
            { size: "L", num: 100, color: "green" }
         ]
   }

   {
      _id: ObjectId("52350353b2eff1353b349de9"),
      code: "ijk",
      tags: [ "electronics", "school" ],
      qty: [
            { size: "M", num: 100, color: "green" }
         ]
   }
] )
```

### Use `$all` to Match Values

The following operation uses the `$all` operator to query the
`inventory` collection for documents where the value of the `tags`
field is an array whose elements include `appliance`, `school`, and
`book`:

```javascript
db.inventory.find( { tags: { $all: [ "appliance", "school", "book" ] } } )
```

The above query returns the following documents:

```javascript
{
   _id: ObjectId("5234cc89687ea597eabee675"),
   code: "xyz",
   tags: [ "school", "book", "bag", "headphone", "appliance" ],
   qty: [
          { size: "S", num: 10, color: "blue" },
          { size: "M", num: 45, color: "blue" },
          { size: "L", num: 100, color: "green" }
        ]
}

{
   _id: ObjectId("5234cc8a687ea597eabee676"),
   code: "abc",
   tags: [ "appliance", "school", "book" ],
   qty: [
          { size: "6", num: 100, color: "green" },
          { size: "6", num: 50, color: "blue" },
          { size: "8", num: 100, color: "brown" }
        ]
}
```

### Use `$all` with `$elemMatch`

If the field contains an array of documents, you can use the
`$all` with the `$elemMatch` operator.

The following operation queries the `inventory` collection for
documents where the value of the `qty` field is an array whose
elements match the `$elemMatch` criteria:

```javascript
db.inventory.find( {
                     qty: { $all: [
                                    { "$elemMatch" : { size: "M", num: { $gt: 50} } },
                                    { "$elemMatch" : { num : 100, color: "green" } }
                                  ] }
                   } )
```

The query returns the following documents:

```javascript
{
   _id: ObjectId("5234ccb7687ea597eabee677"),
   code: "efg",
   tags: [ "school", "book"],
   qty: [
      { size: "S", num: 10, color: "blue" },
      { "size: "M", num: 100, color: "blue" },
      { size: "L", num: 100, color: "green" }
   ]
}

{
   _id: ObjectId("52350353b2eff1353b349de9"),
   code: "ijk",
   tags: [ "electronics", "school" ],
   qty: [
      { size: "M", num: 100, color: "green" }
   ]
}
```

The `$all` operator exists to support queries on arrays. But
you may use the `$all` operator to select against a non-array
`field`, as in the following example:

```javascript
db.inventory.find( { "qty.num": { $all: [ 50 ] } } )
```

**However**, use the following form to express the same query:

```javascript
db.inventory.find( { "qty.num" : 50 } )
```

Both queries will select all documents in the `inventory`
collection where the value of the `num` field equals `50`.

**Note:**

In most cases, MongoDB does not treat arrays as sets. This operator
provides a notable exception to this approach.

## Additional Examples

For additional examples on querying arrays, see:

- read-operations-arrays
- array-match-embedded-documents

For additional examples on querying, see 
read-operations-query-document.

**See also:**

`db.collection.find()`
