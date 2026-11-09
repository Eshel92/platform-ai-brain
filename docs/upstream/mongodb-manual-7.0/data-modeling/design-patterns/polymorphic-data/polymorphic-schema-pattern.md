<!-- Converted from data-modeling/design-patterns/polymorphic-data/polymorphic-schema-pattern.txt (reStructuredText). Includes are inlined. -->

# Store Polymorphic Data

Store polymorphic data when you need to access documents that have
different fields or data types together in the same query.

MongoDB uses a flexible data model, which means documents in a single
collection do not need to have the same structure. Polymorphic data is
data in a single collection that varies in document fields or data
types.

## About this Task

In this example, your application stores professional athletes who play
different sports. Your queries access all athletes, but the attributes
stored for each athlete vary depending on their sport.

The polymorphic pattern stores different document shapes in the same
collection, which improves performance for queries that need to access
all athletes regardless of sport.

## Steps

**Step 1: Insert the sample data.**

```javascript
db.athletes.insertMany( [
   {
      sport: "bowling",
      name: "Earl Anthony",
      career_earnings: 1440000,
      perfect_games: 25,
      pba_championships: 43,
      events: [
         {
            name: "japan_pba",
            score: 300,
            year: 1972
         }
      ]
   },
   {
      sport: "tennis",
      name: "Steffi Graf",
      career_earnings: 21000000,
      grand_slam_wins: 22,
      surfaces: [ "grass", "clay", "hard court" ]
   },
   {
      sport: "cricket",
      name: "Sachin Tendulkar",
      career_earnings: 8000000,
      runs: 15921,
      centuries: 51,
      teammates: [ "Arshad Ayub", "Kapil Dev" ]
   }
] )
```

**Step 2: Query all documents.**

Even though the documents in the `athletes` collection have
different fields, you can return all documents with a single
query:

```javascript
db.athletes.find()
```

Output:

```javascript
[
   {
      _id: ObjectId('6706dcd66fd2c3b24f2e7e92'),
      sport: 'bowling',
      name: 'Earl Anthony',
      career_earnings: 1440000,
      perfect_games: 25,
      pba_championships: 43,
      events: [ { name: 'japan_pba', score: 300, year: 1972 } ]
   },
   {
      _id: ObjectId('6706dcd66fd2c3b24f2e7e93'),
      sport: 'tennis',
      name: 'Steffi Graf',
      career_earnings: 21000000,
      grand_slam_wins: 22,
      surfaces: [ 'grass', 'clay', 'hard court' ]
   },
   {
      _id: ObjectId('6706dcd66fd2c3b24f2e7e94'),
      sport: 'cricket',
      name: 'Sachin Tendulkar',
      career_earnings: 8000000,
      runs: 15921,
      centuries: 51,
      teammates: [ 'Arshad Ayub', 'Kapil Dev' ]
   }
]
```

**Step 3: Query unique fields.**

The polymorphic pattern does not require additional logic to query
on fields that are specific to a particular sport. For example,
the following query returns athletes that have more than 20 grand
slam wins, which only applies to athletes who play tennis:

```javascript
db.athletes.find(
   { grand_slam_wins: { $gt: 20 } }
)
```

Output:

```javascript
[
   {
      _id: ObjectId('6706cd8a6fd2c3b24f2e7e8d'),
      sport: 'tennis',
      name: 'Steffi Graf',
      career_earnings: 21000000,
      grand_slam_wins: 22,
      surfaces: [ 'grass', 'clay', 'hard court' ]
   }
]
```

## Learn More

- inheritance-schema-pattern

- schema-validation-overview

- create-indexes-to-support-queries
