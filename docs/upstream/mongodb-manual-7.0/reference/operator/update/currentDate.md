<!-- Converted from reference/operator/update/currentDate.txt (reStructuredText). Includes are inlined. -->

# $currentDate (update operator)

## Definition

**`$currentDate`**

The `$currentDate` operator sets the value of a field to
the current date, either as a Date
or a timestamp. The default
type is Date.

## Compatibility

You can use `$currentDate` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$currentDate` operator has the form:

```javascript
{ $currentDate: { <field1>: <typeSpecification1>, ... } }
```

`<typeSpecification>` can be either:

- a boolean `true` to set the field value to the current date as a
  Date, or

- a document `{ $type: "timestamp" }` or `{ $type: "date" }`
  which explicitly specifies the type. The operator is
  *case-sensitive* and accepts only the lowercase `"timestamp"` or
  the lowercase `"date"`.

To specify a `<field>` in an embedded document or in an array, use
dot notation.

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

`$currentDate` sets the specified field to the date when
`$currentDate` was run.

If the field does not exist, `$currentDate` adds the field to a
document.

Starting in MongoDB 5.0, `mongod` no longer raises an
error when you use an update operator like `$currentDate`
with an empty operand expression ( `{ }` ). An empty update results
in no changes and no oplog entry is created (meaning that the
operation is a no-op).

## Example

Create a sample collection `customers` with the following document:

```javascript
db.customers.insertOne( 
   { _id: 1, status: "a", lastModified: ISODate("2013-10-02T01:11:18.965Z") }
)
```

The following operation updates the `lastModified` field to the
current date, the `"cancellation.date"` field to the current timestamp
as well as updating the `status` field to `"D"` and the
`"cancellation.reason"` to `"user request"`.

```javascript
db.customers.updateOne(
   { _id: 1 },
   {
     $currentDate: {
        lastModified: true,
        "cancellation.date": { $type: "timestamp" }
     },
     $set: {
        "cancellation.reason": "user request",
        status: "D"
     }
   }
)
```

`$currentDate` sets the specified field to the date when
`$currentDate` was run.

To verify the update:

```javascript
db.customers.find()
```

The updated document resembles:

```javascript
{
   "_id" : 1,
   "status" : "D",
   "lastModified" : ISODate("2020-01-22T21:21:41.052Z"),
   "cancellation" : {
      "date" : Timestamp(1579728101, 1),
      "reason" : "user request"
   }
}
```

The `lastModified` field is set to the date when
`$currentDate` was run in the update example shown earlier.

### Aggregation Alternative to `$currentDate`

Update methods can accept an aggregation pipeline. Specifically, the previous 
example can be rewritten as the following using the aggregation stage 
`$set` and the aggregation variables `NOW` 
(for the current datetime) and `CLUSTER_TIME`
(for the current timestamp):

**Tip:**

- To access aggregation variables, prefix the variable with double
  dollar signs `$$` and enclose in quotes.

- `CLUSTER_TIME` is available only on replica sets and
  sharded clusters.

- The `NOW` and `CLUSTER_TIME` values remain the
  same throughout the pipeline.

```javascript
db.customers.updateOne(
  { _id: 1 },
  [
   { $set: { lastModified: "$$NOW", cancellation: {date: "$$CLUSTER_TIME", reason: "user request"}, status: "D" } }
  ]
)
```

After the operation, you can query the collection to verify the update:

```javascript
db.customers.find().pretty()
```

The query should return the following document:

```javascript
{
   "_id" : 1,
   "status" : "D",
   "lastModified" : ISODate("2020-01-22T21:02:18.994Z"),
   "cancellation" : {
      "date" : Timestamp(1579726934, 2),
      "reason" : "user request"
   }
}
```

**See also:**

- `db.collection.updateOne()`
- `db.collection.updateMany()`
- `db.collection.findAndModify()`
- `db.collection.findOneAndUpdate()`
