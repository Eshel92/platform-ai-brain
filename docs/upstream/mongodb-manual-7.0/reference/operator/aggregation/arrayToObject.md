<!-- Converted from reference/operator/aggregation/arrayToObject.txt (reStructuredText). Includes are inlined. -->

# $arrayToObject (expression operator)

## Definition

**`$arrayToObject`**

Converts an array into a single document. 

`$arrayToObject` has the following syntax:

```javascript
{ $arrayToObject: <expression> }
```

The `<expression>` can be any valid expression that resolves to:

- An array of two-element arrays where the first element is the
  field name, and the second element is the field value:

  ```javascript
  $arrayToObject: [ 
      [ [ "item", "abc123" ], [ "qty", 25 ] ] 
  ]
  ```

\- OR -

- An array of documents that contains two fields, `k` and `v`
  where:

  - The `k` field contains the field name.

  - The `v` field contains the value of the field.

  ```javascript
  $arrayToObject: [ 
     [ 
        { "k": "item", "v": "abc123" }, 
        { "k": "qty", "v": 25 } 
     ] 
  ]
  ```

## Behavior

If you pass in an empty array to `$arrayToObject`, MongoDB creates an
empty object.

If the name of a field repeats in the array,

- Starting in 4.0.5, `$arrayToObject` uses the last value
  for that field. For 4.0.0-4.0.4, the value used depends on the driver.

- Starting in 3.6.10, `$arrayToObject` uses the last value
  for that field. For 3.6.0-3.6.9, the value used depends on the driver.

- Starting in 3.4.19, `$arrayToObject` uses the last value
  for that field. For 3.4.0-3.4.19, the value uses depends on the
  driver.

* - Example
  - Results

* - .. code-block:: json
       :copyable: false

       { $arrayToObject: [
          [ { "k": "item", "v": "abc123" },
            { "k": "qty", "v": "$qty" } ]
       ] }

  - Given a document with the field `qty` and value `25`,     
    `$arrayToObject` returns:

    ```json
    { "item" : "abc123", "qty" : 25 }
    ```

* - .. code-block:: json
       :copyable: false

       { $arrayToObject: { $literal:  [ 
          [ "item", "abc123" ], [ "qty", 25 ] 
       ] } }

  - .. code-block:: json
       :copyable: false

       { "item" : "abc123", "qty" : 25 }

* - .. code-block:: json
       :copyable: false

       { $arrayToObject: { $literal: [ 
          { "k": "item", "v": "123abc" }, 
          { "k": "item", "v": "abc123" } 
       ] } }

  - .. code-block:: json
       :copyable: false

       { "item" : "abc123" }

    Starting in versions 4.0.5+ (3.6.10+ and 3.4.19+), if the name
    of a field repeats in the array, `$arrayToObject`
    uses the last value for that field.

## Examples

### `$arrayToObject`  Example

Consider a `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "ABC1",  dimensions: [ { "k": "l", "v": 25} , { "k": "w", "v": 10 }, { "k": "uom", "v": "cm" } ] },
   { _id: 2, item: "ABC2",  dimensions: [ [ "l", 50 ], [ "w",  25 ], [ "uom", "cm" ] ] },
   { _id: 3, item: "ABC3",  dimensions: [ [ "l", 25 ], [ "l",  "cm" ], [ "l", 50 ] ] }
] )
```

The following aggregation pipeline operation use the
`$arrayToObject` to return the `dimensions` field as a
document:

```javascript
db.inventory.aggregate(
   [
      {
         $project: {
            item: 1,
            dimensions: { $arrayToObject: "$dimensions" }
         }
      }
   ]
)
```

The operation returns the following:

```javascript
{ _id: 1, item: "ABC1", dimensions: { "l" : 25, "w" : 10, "uom" : "cm" } }
{ _id: 2, item: "ABC2", dimensions: { "l" : 50, "w" : 25, "uom" : "cm" } }
{ _id: 3, item: "ABC3", dimensions: { "l" : 50 } }
```

Starting in versions 4.0.5+ (3.6.10+ and 3.4.19+), if the name of a
field repeats in the array, `$arrayToObject` uses the last
value for that field. 

### `$objectToArray` + `$arrayToObject` Example

Consider a `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "ABC1", instock: { warehouse1: 2500, warehouse2: 500 } },
   { _id: 2, item: "ABC2", instock: { warehouse2: 500, warehouse3: 200},
   }
] )
```

The following aggregation pipeline operation calculates the total in
stock for each item and adds to the `instock` document:

```javascript
db.inventory.aggregate( [
   { $addFields: { instock: { $objectToArray: "$instock" } } },
   { $addFields: { instock: { $concatArrays: [ "$instock", [ { "k": "total", "v": { $sum: "$instock.v" } } ] ] } } } ,
   { $addFields: { instock: { $arrayToObject: "$instock" } } }
] )
```

The operation returns the following:

```javascript
{ _id: 1, item: "ABC1", instock: { warehouse1: 2500, warehouse2: 500, total: 3000 } }
{ _id: 2, item: "ABC2", instock: { warehouse2: 500, warehouse3: 200, total: 700 } }
```

**See also:**

`$objectToArray`
