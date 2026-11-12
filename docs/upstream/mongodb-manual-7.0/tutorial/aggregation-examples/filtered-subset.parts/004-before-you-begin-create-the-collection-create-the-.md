<!-- Part 4 of 11 of tutorial/aggregation-examples/filtered-subset.md (split because the page is big). -->

### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```cpp
auto persons = db["persons"];

std::vector<bsoncxx::document::value> docs = {
    bsoncxx::from_json(R"({
        "person_id": "6392529400",
        "firstname": "Elise",
        "lastname": "Smith",
        "dateofbirth": {"$date": 620947927},
        "vocation": "ENGINEER",
        "address": {
            "number": 5625,
            "street": "Tipa Circle",
            "city": "Wojzinmoj"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "1723338115",
        "firstname": "Olive",
        "lastname": "Ranieri",
        "dateofbirth": {"$date": 485529270000},
        "gender": "FEMALE",
        "vocation": "ENGINEER",
        "address": {
            "number": 9303,
            "street": "Mele Circle",
            "city": "Tobihbo"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "8732762874",
        "firstname": "Toni",
        "lastname": "Jones",
        "dateofbirth": {"$date": 690978836000},
        "vocation": "POLITICIAN",
        "address": {
            "number": 1,
            "street": "High Street",
            "city": "Upper Abbeywoodington"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "7363629563",
        "firstname": "Bert",
        "lastname": "Gooding",
        "dateofbirth": {"$date": -88368048000},
        "vocation": "FLORIST",
        "address": {
            "number": 13,
            "street": "Upper Bold Road",
            "city": "Redringtonville"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "1029648329",
        "firstname": "Sophie",
        "lastname": "Celements",
        "dateofbirth": {"$date": -31561935000},
        "vocation": "ENGINEER",
        "address": {
            "number": 5,
            "street": "Innings Close",
            "city": "Basilbridge"
        }
    })"),
    bsoncxx::from_json(R"({
        "person_id": "7363626383",
        "firstname": "Carl",
        "lastname": "Simmons",
        "dateofbirth": {"$date": 915148835000},
        "vocation": "ENGINEER",
        "address": {
            "number": 187,
            "street": "Hillside Road",
            "city": "Kenningford"
        }
    })")
};

auto result = persons.insert_many(docs); // Might throw an exception
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```cpp
pipeline.match(bsoncxx::from_json(R"({
    "vocation": "ENGINEER"
})"));
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```cpp
pipeline.sort(bsoncxx::from_json(R"({
    "dateofbirth": -1
})"));
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```cpp
pipeline.limit(3);
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```cpp
pipeline.append_stage(bsoncxx::from_json(R"({
    "$unset": ["_id", "address"]
})"));
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```cpp
auto cursor = persons.aggregate(pipeline);
```

Finally, run the following commands in your shell to start your
application:

```bash
c++ --std=c++17 agg-tutorial.cpp $(pkg-config --cflags --libs libmongocxx) -o ./app.out
./app.out
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{ "person_id" : "7363626383", "firstname" : "Carl", "lastname" : "Simmons", "dateofbirth" : { "$date" : "1999-01-01T00:00:35Z" }, "vocation" : "ENGINEER" }
{ "person_id" : "1723338115", "firstname" : "Olive", "lastname" : "Ranieri", "dateofbirth" : { "$date" : "1985-05-21T13:14:30Z" }, "gender" : "FEMALE", "vocation" : "ENGINEER" }
{ "person_id" : "6392529400", "firstname" : "Elise", "lastname" : "Smith", "dateofbirth" : { "$date" : "1970-01-08T04:29:07.927Z" }, "vocation" : "ENGINEER" }
```


### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new Node.js app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the driver and connect to MongoDB,
see the `Node.js Driver Quick Start guide`.

To learn more about performing aggregations in the Node.js Driver, see the
`Aggregation guide`.

After you install the driver, create a file called
`agg_tutorial.js`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```javascript
const { MongoClient } = require("mongodb");

// Replace the placeholder with your connection string.
const uri = "<connection string>";
const client = new MongoClient(uri);

async function run() {
  try {
    const aggDB = client.db("agg_tutorials_db");

    // Get a reference to relevant collections.
    // ... const someColl =
    // ... const anotherColl =

    // Delete any existing documents in collections.
    // ... await someColl.deleteMany({});

    // Insert sample data into the collection or collections.
    // ... const someData = [ ... ];
    // ... await someColl.insertMany(someData);

    // Create an empty pipeline array.
    const pipeline = [];

    // Add code to create pipeline stages.
    // ... pipeline.push({ ... })

    // Run the aggregation.
    // ... const aggregationResult = ...

    // Print the aggregation results.
    for await (const document of aggregationResult) {
      console.log(document);
    }
  } finally {
    await client.close();
  }
}

run().catch(console.dir);
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
`Create a Connection String`
step of the Node.js Quick Start guide.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```javascript
const uri = "mongodb+srv://mongodb-example:27017";
```


### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```javascript
const persons = aggDB.collection("persons");
await persons.deleteMany({});

await persons.insertMany([
  {
    person_id: "6392529400",
    firstname: "Elise",
    lastname: "Smith",
    dateofbirth: new Date("1972-01-13T09:32:07Z"),
    vocation: "ENGINEER",
    address: {
      number: 5625,
      street: "Tipa Circle",
      city: "Wojzinmoj",
    },
  },
  {
    person_id: "1723338115",
    firstname: "Olive",
    lastname: "Ranieri",
    dateofbirth: new Date("1985-05-12T23:14:30Z"),
    gender: "FEMALE",
    vocation: "ENGINEER",
    address: {
      number: 9303,
      street: "Mele Circle",
      city: "Tobihbo",
    },
  },
  {
    person_id: "8732762874",
    firstname: "Toni",
    lastname: "Jones",
    dateofbirth: new Date("1991-11-23T16:53:56Z"),
    vocation: "POLITICIAN",
    address: {
      number: 1,
      street: "High Street",
      city: "Upper Abbeywoodington",
    },
  },
  {
    person_id: "7363629563",
    firstname: "Bert",
    lastname: "Gooding",
    dateofbirth: new Date("1941-04-07T22:11:52Z"),
    vocation: "FLORIST",
    address: {
      number: 13,
      street: "Upper Bold Road",
      city: "Redringtonville",
    },
  },
  {
    person_id: "1029648329",
    firstname: "Sophie",
    lastname: "Celements",
    dateofbirth: new Date("1959-07-06T17:35:45Z"),
    vocation: "ENGINEER",
    address: {
      number: 5,
      street: "Innings Close",
      city: "Basilbridge",
    },
  },
  {
    person_id: "7363626383",
    firstname: "Carl",
    lastname: "Simmons",
    dateofbirth: new Date("1998-12-26T13:13:55Z"),
    vocation: "ENGINEER",
    address: {
      number: 187,
      street: "Hillside Road",
      city: "Kenningford",
    },
  },
]);
```

**Step 1: Add a match stage for people who are engineers.**

First, add a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```javascript
pipeline.push({
  $match: {
    vocation: "ENGINEER",
  },
});
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, add a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```javascript
pipeline.push({
  $sort: {
    dateofbirth: -1,
  },
});
```

**Step 3: Add a limit stage to see only three results.**

Next, add a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```javascript
pipeline.push({
  $limit: 3,
});
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, add an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```javascript
pipeline.push({
  $unset: ["_id", "address"],
});
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```javascript
const aggregationResult = await persons.aggregate(pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
node agg_tutorial.js
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```javascript
{
  person_id: '7363626383',
  firstname: 'Carl',
  lastname: 'Simmons',
  dateofbirth: 1998-12-26T13:13:55.000Z,
  vocation: 'ENGINEER'
}
{
  person_id: '1723338115',
  firstname: 'Olive',
  lastname: 'Ranieri',
  dateofbirth: 1985-05-12T23:14:30.000Z,
  gender: 'FEMALE',
  vocation: 'ENGINEER'
}
{
  person_id: '6392529400',
  firstname: 'Elise',
  lastname: 'Smith',
  dateofbirth: 1972-01-13T09:32:07.000Z,
  vocation: 'ENGINEER'
}
```


### Create the Template App

Before you begin following this aggregation tutorial, you must set up a
new PHP app. You can use this app to connect to a MongoDB
deployment, insert sample data into MongoDB, and run the aggregation
pipeline.

**Tip:**

To learn how to install the PHP library and connect to MongoDB,
see the [Get Started with the PHP Library](https://www.mongodb.com/docs/php-library/current/get-started/)
tutorial.

To learn more about performing aggregations in the PHP library, see the
[Aggregation guide](https://www.mongodb.com/docs/php-library/current/aggregation/).

After you install the library, create a file called
`agg_tutorial.php`. Paste the following code in this file to create an
app template for the aggregation tutorials.

**Important:**

In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.

If you attempt to run the code without making any changes, you will
encounter a connection error.

```php
<?php

require 'vendor/autoload.php';

// Modify imports for each tutorial as needed.
use MongoDB\Client;
use MongoDB\BSON\UTCDateTime;
use MongoDB\Builder\Pipeline;
use MongoDB\Builder\Stage;
use MongoDB\Builder\Type\Sort;
use MongoDB\Builder\Query;
use MongoDB\Builder\Expression;
use MongoDB\Builder\Accumulator;

use function MongoDB\object;

// Replace the placeholder with your connection string.
$uri = '<connection string>';
$client = new Client($uri);

// Get a reference to relevant collections.
// ... $someColl = $client->agg_tutorials_db->someColl;
// ... $anotherColl = $client->agg_tutorials_db->anotherColl;

// Delete any existing documents in collections if needed.
// ... $someColl->deleteMany([]);

// Insert sample data into the collection or collections.
// ... $someColl->insertMany(...);

// Add code to create pipeline stages within the Pipeline instance.
// ... $pipeline = new Pipeline(...);

// Run the aggregation.
// ... $cursor = $someColl->aggregate($pipeline);

// Print the aggregation results.
foreach ($cursor as $doc) {
    echo json_encode($doc, JSON_PRETTY_PRINT), PHP_EOL;
}
```

For every tutorial, you must replace the connection string placeholder with
your deployment's connection string.

**Tip:**

To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/php-library/current/get-started/#create-a-connection-string)
step of the Get Started with the PHP Library tutorial.

For example, if your connection string is
`"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles
the following:

```php
$uri = 'mongodb+srv://mongodb-example:27017';
```


### Create the Collection

This example uses a `persons` collection, which contains documents
describing each person's name, date of birth, vocation, and other
details. The aggregation selects documents based on whether
their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the
following code to your application:

```php
$persons = $client->agg_tutorials_db->persons;
$persons->deleteMany([]);

$persons->insertMany(
    [
        [
            'person_id' => '6392529400',
            'firstname' => 'Elise',
            'lastname' => 'Smith',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1972-01-13T09:32:07')),
            'vocation' => 'ENGINEER',
            'address' => ['number' => 5625, 'Street' => 'Tipa Circle', 'city' => 'Wojzinmoj'],
        ],
        [
            'person_id' => '1723338115',
            'firstname' => 'Olive',
            'lastname' => 'Ranieri',
            'gender' => 'FEMALE',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1985-05-12T23:14:30')),
            'vocation' => 'ENGINEER',
            'address' => ['number' => 9303, 'street' => 'Mele Circle', 'city' => 'Tobihbo'],
        ],
        [
            'person_id' => '8732762874',
            'firstname' => 'Toni',
            'lastname' => 'Jones',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1991-11-23T16:53:56')),
            'vocation' => 'POLITICIAN',
            'address' => ['number' => 1, 'street' => 'High Street', 'city' => 'Upper Abbeywoodington'],
        ],
        [
            'person_id' => '7363629563',
            'firstname' => 'Bert',
            'lastname' => 'Gooding',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1941-04-07T22:11:52')),
            'vocation' => 'FLORIST',
            'address' => ['number' => 13, 'street' => 'Upper Bold Road', 'city' => 'Redringtonville'],
        ],
        [
            'person_id' => '1029648329',
            'firstname' => 'Sophie',
            'lastname' => 'Celements',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1959-07-06T17:35:45')),
            'vocation' => 'ENGINEER',
            'address' => ['number' => 5, 'street' => 'Innings Close', 'city' => 'Basilbridge'],
        ],
        [
            'person_id' => '7363626383',
            'firstname' => 'Carl',
            'lastname' => 'Simmons',
            'dateofbirth' => new UTCDateTime(new DateTimeImmutable('1998-12-26T13:13:55')),
            'vocation' => 'ENGINEER',
            'address' => ['number' => 187, 'street' => 'Hillside Road', 'city' => 'Kenningford'],
        ]
    ]
);
```

**Step 1: Add a match stage for people who are engineers.**

In your `Pipeline` instance, create a `$match` stage that finds documents in which
the value of the `vocation` field is `"ENGINEER"`:

```php
Stage::match(vocation: 'ENGINEER'),
```

**Step 2: Add a sort stage to sort from youngest to oldest.**

Next, create a `$sort` stage that sorts the
documents in descending order by the `dateofbirth` field to
list the youngest people first:

```php
Stage::sort(dateofbirth: Sort::Desc),
```

**Step 3: Add a limit stage to see only three results.**

Next, create a `$limit`
stage to the pipeline to output only the first three documents in
the results.

```php
Stage::limit(3),
```

**Step 4: Add an unset stage to remove unneeded fields.**

Finally, create an `$unset` stage. The
`$unset` stage removes unnecessary fields from the result documents:

```php
Stage::unset('_id', 'address')
```

**Tip:**

Use the `$unset` operator instead of `$project` to avoid
modifying the aggregation pipeline if documents with
different fields are added to the collection.

**Step 5: Run the aggregation pipeline.**

Add the following code to the end of your application to perform
the aggregation on the `persons` collection:

```php
$cursor = $persons->aggregate($pipeline);
```

Finally, run the following command in your shell to start your
application:

```bash
php agg_tutorial.php
```

**Step 6: Interpret the aggregation results.**

The aggregated result contains three documents. The documents
represent the three youngest people with the vocation of `"ENGINEER"`,
ordered from youngest to oldest. The results omit the `_id` and `address`
fields.

```none
{
    "person_id": "7363626383",
    "firstname": "Carl",
    "lastname": "Simmons",
    "dateofbirth": {
        "$date": {
            "$numberLong": "914678035000"
        }
    },
    "vocation": "ENGINEER"
}
{
    "person_id": "1723338115",
    "firstname": "Olive",
    "lastname": "Ranieri",
    "gender": "FEMALE",
    "dateofbirth": {
        "$date": {
            "$numberLong": "484787670000"
        }
    },
    "vocation": "ENGINEER"
}
{
    "person_id": "6392529400",
    "firstname": "Elise",
    "lastname": "Smith",
    "dateofbirth": {
        "$date": {
            "$numberLong": "64143127000"
        }
    },
    "vocation": "ENGINEER"
}
```
