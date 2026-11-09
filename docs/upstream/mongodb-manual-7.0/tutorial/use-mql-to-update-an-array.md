<!-- Converted from tutorial/use-mql-to-update-an-array.txt (reStructuredText). Includes are inlined. -->

# Update Array Elements with MQL Positional Operators

You can use positional operators with MongoDB Query Language (MQL) to
update documents that contain arrays without replacing
the array or appending to it.

This tutorial presents several use cases for positional operators within
MongoDB.

## Before You Begin

- Install mongosh.

- Connect to a deployment.

- Use `mongosh` to insert documents into a new collection in the
  default `test` database:

  ```javascript
  db.employees.insertMany( 
     [
        {
           _id: 'SF',
           engineering: [
              { name: 'Alice', email: 'missingEmail', salary: 100000 },
              { name: 'Bob', email: 'missingEmail', salary: 75000 }
           ],
           sales: [
              { name: 'Charlie', email: 'charlie@mail.com', salary: 90000, bonus: 1000 }
           ]
        },
        {
           _id: 'NYC',
           engineering: [
              { name: 'Dave', email: 'dave@mail.com', salary: 55000 },
           ],
           sales: [
              { name: 'Ed', email: 'ed@mail.com', salary: 99000, bonus: 2000 },
              { name: 'Fran', email: 'fran@mail.com', salary: 50000, bonus: 10000 }
           ]
        }
     ] 
  );
  ```

## Steps

The following examples show you how to:

- positional-update-first-array-match

- positional-update-specific-array-match

- positional-update-all-array-elements

- positional-update-array-filter-match

### Use the $ Operator to Update the First Match in an Array

To update only the first match within an array, use the `$`
operator. The `$` operator acts as a placeholder to update the first
element matched.

The following example uses the `updateOne()` method with
the `$` and `$set` operators to update the first email that has the value
`missingEmail` in the `engineering` array to `alice@mail.com`.

```javascript
db.employees.updateOne(
   { "engineering.email": "missingEmail" },
   { "$set": { "engineering.$.email": "alice@mail.com" } }
);
```

Use the `find()` method to confirm the update to
Alice's email.

```javascript
   db.employees.find()
```

Output:

```shell
[
   {
      _id: 'SF',
      engineering: [
         { name: 'Alice', email: 'alice@mail.com', salary: 100000 },
         { name: 'Bob', email: 'missingEmail', salary: 75000 }
      ],
      sales: [
         { name: 'Charlie', email: 'charlie@mail.com', salary: 90000, bonus: 1000 }
      ]
   },
   {
      _id: 'NYC',
      engineering: [ 
         { name: 'Dave', email: 'dave@mail.com', salary: 55000 }
      ],
      sales: [
         { name: 'Ed', email: 'ed@mail.com', salary: 99000, bonus: 2000 },
         { name: 'Fran', email: 'fran@mail.com', salary: 50000, bonus: 10000 }
      ]
   }
]
```

As shown in the example above, after you filter for documents that have an array
element with the `engineering.email` field set to `missingEmail`, the
`$` operator only updates the first occurrence that matches the filter.

### Use the $ Operator with $elemMatch to Update a Specific Element

To update a particular element, you can use the `$elemMatch` operator.

The following example uses the `$elemMatch` operator and the `$`
operator to update Bob's `email` to `"bob@mail.com"`.

```javascript
db.employees.updateOne(  
   { engineering: { $elemMatch: { name: "Bob", email: "missingEmail" } } },  
   { $set: { "engineering.$.email": "bob@mail.com" } }  
); 
```

Use the `find()` method to confirm the update to
Bob's email.

```javascript
db.employees.find(  
   { "engineering": { $elemMatch: { name: "Bob" } } },  
   { "engineering.$": 1, _id: 0 }  
);  
```

Output:

```shell
[
   {
      engineering: [ { name: 'Bob', email: 'bob@mail.com', salary: 75000 } ]
   }
]
```

### Use the $[] Operator to Update All Array Elements Within a Document

To update every element of an array with a single operation, use the
`$[]` operator.

Consider a case where you want to give an additional bonus of $2,000 to your
sales employees in NYC. You can use the `updateMany()` method
with the `$[]` operator and the `$inc` operator to increase all
`bonus` fields within the `sales` array in the `NYC` document by `2000`.

```javascript
db.employees.updateMany(
   { "_id": "NYC" },
   { "$inc": { "sales.$[].bonus": 2000 } }
);
```

Use the `find()` method to confirm the update to
the `bonus` fields for the employees on NYC's sales team.

```javascript
db.employees.find(  
   { _id: "NYC" },
   { sales: 1, _id: 0 }  
);  
```

Output:

```shell
[
   {
      sales: [
         { name: 'Ed', email: 'ed@mail.com', salary: 99000, bonus: 4000 },
         { name: 'Fran', email: 'fran@mail.com', salary: 50000, bonus: 12000 }
      ]
   }
]
```

### Use the $[<identifier>] Operator to Update Elements that Match a Filter Condition

To update several array elements in a single operation without
excessive client-side code paired with a replace operation, use the
`$[<identifier>]` operator. The `$[<identifier>]` operator acts
as a placeholder to update all elements that match an arrayFilters condition.

Consider a case where you want to update specific employees' salaries if 
they meet a number of conditions. You can use the
`updateMany()` method with the `$[<identifier>]`
operator to accomplish this task.

```javascript
db.employees.updateMany(
   {},
   {
      "$set": {
            "engineering.$[elemX].salary": 95000,
             "sales.$[elemY].salary": 75000
      }
   },
   {
      "arrayFilters": [
            { "elemX.name": "Bob", "elemX.salary": 75000 },
            { "elemY.name": "Ed", "elemY.salary": 50000, }
      ]
   }
);
```

In the above example, the first parameter is an empty match, to evaluate all
documents in the collection.

`elemX` and `elemY` represent two different arrayFilters:

- To match `elemX`, an array object must have a `name` field of `Bob` and
  a `salary` of `75000`.

- To match `elemY`, an array object must have a `name` field of `Ed` and a
  `salary` of `50000`.

If an array item in the document matches the `elemX` filter, then `updateMany()` 
sets the `salary` field for the object to `95000`. If an array item matches the 
`elemY` filter, then `updateMany()` sets the `salary` field for the object to 
`75000`. If a filter doesn't match, the corresponding `$set` operation 
doesn't trigger.

Use the `find()` method to confirm the update to
Bob's salary because he meets both `elemX`'s conditions.

```javascript
db.employees.find(  
   { "engineering.name": "Bob" },  
   { engineering: { $elemMatch: { name: "Bob" } }, _id: 0 }  
);
```

Output:

```shell
[  
   {  
      engineering: [  
         { name: "Bob", email: "bob@mail.com", salary: 95000 }  
      ]  
   }  
]  
```

Use the `find()` method to confirm the update to
Ed's salary did not succeed because he does not meet either `elemX` or
`elemY`'s conditions.

```javascript
db.employees.find(  
   { "sales.name": "Ed" },  
   { sales: { $elemMatch: { name: "Ed" } }, _id: 0 }  
);  
```

Output:

```shell
[  
   {  
      sales: [  
         { name: "Ed", email: "ed@mail.com", salary: 99000, bonus: 4000 }  
      ]  
   }  
]
```

## Conclusion

This tutorial teaches you some of the positional operators within the MongoDB
Query Language (MQL). These operators are useful when working with arrays
because they prevent you from having to do full replaces on the array or
extended client-side manipulation. To learn more about MQL, see [get started with Atlas](https://www.mongodb.com/docs/get-started/).

To learn more about update operators in MongoDB, see update-operators-ref.
