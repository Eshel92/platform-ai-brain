<!-- Converted from reference/operator/aggregation/ifNull.txt (reStructuredText). Includes are inlined. -->

# $ifNull (aggregation)

## Definition

**`$ifNull`**

**Changed in version:** 5.0

The `$ifNull` expression evaluates input expressions for
null values and returns:
   
- The first non-null input expression
  value found.
   
- A replacement expression value if all
  input expressions evaluate to null.
     
`$ifNull` treats undefined values and missing fields as
null.
   

## Compatibility

You can use `$ifNull` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

```none
{
   $ifNull: [
      <input-expression-1>,
      ...
      <input-expression-n>,
      <replacement-expression-if-null>
   ]
}
```

## Examples

This `inventory` collection is used in the examples:

```javascript
db.inventory.insertMany( [
   { "_id" : 1, "item" : "buggy", description: "toy car", "quantity" : 300 },
   { "_id" : 2, "item" : "bicycle", description: null, "quantity" : 200 },
   { "_id" : 3, "item" : "flag" }
] )
```

### Single Input Expression

The following example uses `$ifNull` to return:

- `description` if it is non-null.

- `"Unspecified"` string if `description` is null or missing.

```javascript
db.inventory.aggregate(
   [
      {
         $project: {
            item: 1,
            description: { $ifNull: [ "$description", "Unspecified" ] }
         }
      }
   ]
)
```

Output:

```javascript
{ "_id" : 1, "item" : "buggy", "description" : "toy car" }
{ "_id" : 2, "item" : "bicycle", "description" : "Unspecified" }
{ "_id" : 3, "item" : "flag", "description" : "Unspecified" }
```

### Multiple Input Expressions

**New in version:** 5.0

The following example uses `$ifNull` to return:

- `description` if it is non-null.

- `quantity` if `description` is null or missing and `quantity`
  is non-null.

- `"Unspecified"` string if `description` and `quantity` are both
  null or missing.

```javascript
db.inventory.aggregate(
   [
      {
         $project: {
            item: 1,
            value: { $ifNull: [ "$description", "$quantity", "Unspecified" ] }
         }
      }
   ]
)
```

Output:

```javascript
{ "_id" : 1, "item" : "buggy", "value" : "toy car" }
{ "_id" : 2, "item" : "bicycle", "value" : 200 }
{ "_id" : 3, "item" : "flag", "value" : "Unspecified" }
```
