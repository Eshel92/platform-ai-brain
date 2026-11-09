<!-- Converted from data-modeling/design-antipatterns/unnecessary-indexes.txt (reStructuredText). Includes are inlined. -->

# Remove Unnecessary Indexes

Creating indexes for every query can lead to unnecessary indexes, which 
can degrade database performance. Unnecessary indexes might be rarely 
used, redundant due to coverage by another compound index, or not used 
at all. To optimize database performance, it's important to minimize the 
number of indexes you use. Identify and remove unnecessary indexes to 
maintain efficient query execution and resource use.

## About this Task

Consider the following `courses` collection, where each document stores 
information about a different school course.

```javascript
// Biology course document
db.courses.insertOne(
   {
      _id: 1,
      course_name: "Biology 101",
      professor: "Tate",
      semester: "Fall",
      days: "Monday, Friday",
      time: "12:00",
      building: "Olson"
   } 
 )
```

The `courses` collection has an index for every field:

- `_id` is indexed by default
- `{ course_name: 1 }`
- `{ professor: 1 }`
- `{ semester: 1 }`
- `{ building: 1 }`
- `{ days: 1 }`
- `{ time: 1 }`
- `{ day: 1, time: 1 }`

Creating indexes for every field in a collection can lead to bloated 
collections and negatively impact write performance.

## Steps

**Step 1: Evaluate index usage.**

To determine which indexes are rarely used, use the
`$indexStats` aggregation stage:

```javascript
db.courses.aggregate( [ { $indexStats: { } } ] )
```

**Warning:**

`$indexStats` reports index usage metrics in the
accesses field only for the node
where the query runs. For more comprehensive index usage statistics,
run `$indexStats` on each node in the cluster.

The output includes the accesses field, which reports the number of
times users have used each index to run an operation on the node
`M-C02FJ3BDML85:27017`: 

```javascript
[
   {
      name: "building_1",
      key: { "building": 1 },
      host: "M-C02FJ3BDML85:27017",
      accesses: { "ops": "Long('0')", "since": "ISODate('2024-06-24T17:35:00.000Z')" },
      spec: { "v": 2, "key": { "building": 1 }, "name": "building_1" }
   },
   {
      name: "day_1",
      key: { "day": 1 },
      host: "M-C02FJ3BDML85:27017",
      accesses: { "ops": "Long('1')", "since": "ISODate('2024-06-24T17:35:30.000Z')" },
      spec: { "v": 2, "key": { "day": 1 }, "name": "day_1" }
   },
   {
      name: "time_1",
      key: { "time": 1 },
      host: "M-C02FJ3BDML85:27017",
      accesses: { "ops": "Long('1')", "since": "ISODate('2024-06-24T17:36:00.000Z')" },
      spec: { "v": 2, "key": { "time": 1 }, "name": "time_1" }
   },
   {
      name: "day_1_time_1",
      key: { "day": 1, "time": 1 },
      host: "M-C02FJ3BDML85:27017",
      accesses: { "ops": "Long('110')", "since": "ISODate('2024-06-24T17:31:21.800Z')" },
      spec: { "v": 2, "key": { "day": 1, "time": 1 }, "name": "day_1_time_1" }
   },
   {
      name: "_id_",
      key: { "_id": 1 },
      host: "M-C02FJ3BDML85:27017",
      accesses: { "ops": "Long('150')", "since": "ISODate('2024-06-24T15:31:49.463Z')" },
      spec: { "v": 2, "key": { "_id": 1 }, "name": "_id_" }
   },
   {
      name: "course_name_1",
      key: { "course_name": 1 },
      host: "M-C02FJ3BDML85:27017",
      accesses: { "ops": "Long('120')", "since": "ISODate('2024-06-24T17:29:26.344Z')" },
      spec: { "v": 2, "key": { "course_name": 1 }, "name": "course_name_1" }
   },
   ...
]
```

- The `building_1` index can be dropped because it is not used 
  for any queries, as indicated by its `accesses` count of zero.

- The `{ days: 1 }` and `{ time: 1 }` indexes can be dropped because 
  the compound index `{ day: 1, time: 1 }` 
  covers time-related queries.

You can also use MongoDB Atlas Performance Advisor 
(available for M10 clusters or higher) and `MongoDB Compass` to 
determine, hide, and drop unnecessary indexes.

**Step 2: Hide unnecessary indexes.**

After you identify unnecessary indexes, you can use the 
`db.collection.hideIndex()` method to hide the indexes and 
evaluate their impact on the database before you remove them.

```javascript
db.courses.hideIndex( "days_1" )
db.courses.hideIndex( "time_1" )
db.courses.hideIndex( "building_1" )
```

**Step 3: Drop unnecessary indexes.**

If you determine the indexes are unnecessary and have a negative impact 
on performance, drop the indexes using the `db.collection.dropIndexes()` 
method.

```javascript
db.courses.dropIndexes( [ "days_1", "time_1", "building_1" ] ) 
```

In this example, only the following indexes remain because they are the 
most frequently used and help optimize queries:

- `_id` is indexed by default
- `{ course_name: 1 }`
- `{ professor: 1 }`
- `{ semester: 1 }`
- `{ day: 1, time: 1 }`

## Learn More

- schema-design-patterns
- MongoDB Atlas Performance Advisor
- `Manage Indexes`
