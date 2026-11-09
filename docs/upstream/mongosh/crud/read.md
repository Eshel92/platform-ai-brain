<!-- Converted from crud/read.txt (reStructuredText). Includes are inlined. -->

# Query Documents

   

Use the `db.collection.find()` method in the MongoDB Shell
to query documents in a collection.

The examples on this page reference the MongoDB sample dataset. To learn more about setting up deployments and populate a
cluster with the sample data, see Get Started with MongoDB.

## Read All Documents in a Collection

To read all documents in the collection, pass an empty document as the
query filter parameter to the find method. The query filter parameter
determines the select criteria.

**Example:**

To return all documents from the `sample_mflix.movies` collection:

```javascript
use sample_mflix

db.movies.find()
```

This operation is equivalent to the following SQL statement:

```sql
SELECT * FROM movies
```

## Specify Equality Condition

To select documents which match an equality condition, specify
the condition as a `<field>:<value>` pair in the
query filter document.

**Example:**

To return all movies where the `title` equals `Titanic` from the
`sample_mflix.movies` collection:

```javascript
use sample_mflix

db.movies.find( { "title": "Titanic" } )
```

This operation corresponds to the following SQL statement:

```sql
SELECT * FROM movies WHERE title = "Titanic"
```

## Specify Conditions Using Query Operators

Use query operators in a
query filter document
to perform more complex comparisons and evaluations. Query operators
in a query filter document have the following form:

```javascript
{ <field1>: { <operator1>: <value1> }, ... }
```

**Example:**

To return all movies from the `sample_mflix.movies` collection
which are either rated `PG` or `PG-13`:

```javascript
use sample_mflix

db.movies.find( { rated: { $in: [ "PG", "PG-13" ] } } )
```

This operation corresponds to the following SQL statement:

```sql
SELECT * FROM movies WHERE rated in ("PG", "PG-13")
```

**Note:**

Although you can express this query using the `$or` operator,
use the `$in` operator rather than the `$or`
operator when performing equality checks on the same field.

## Specify Logical Operators (AND / OR)

A compound query can specify conditions for more than one field in the
collection's documents. Implicitly, a logical `AND` conjunction
connects the clauses of a compound query so that the query selects the
documents in the collection that match all the conditions.

**Example:**

To return movies which were released in Mexico **and** have an IMDB
rating of at least 7:

```javascript
use sample_mflix

db.movies.find( { countries: "Mexico", "imdb.rating": { $gte: 7 } } )
```

Use the `$or` operator to specify a compound query that joins
each clause with a logical `OR` conjunction so that the query selects
the documents in the collection that match at least one condition.

**Example:**

To return movies from the `sample_mflix.movies` collection which
were released in 2010 **and** *either* won at least 5 awards or
have a `genre` of `Drama`:

```javascript
use sample_mflix

db.movies.find( {
     year: 2010,
     $or: [ { "awards.wins": { $gte: 5 } }, { genres: "Drama" } ]
} )
```

## Read Behavior

To learn more about the specific behavior of reading documents,
see Behavior.

## Additional Query Tutorials

For additional query examples, see:

- Query Embedded Documents

- Query an Array

- Query an Array of Embedded Documents

- Project Fields to Return from Query

- Query for Null or Missing Fields
