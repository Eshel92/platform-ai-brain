<!-- Converted from core/materialized-views.txt (reStructuredText). Includes are inlined. -->

# On-Demand Materialized Views

**Note:** Disambiguation

This page discusses on-demand materialized views. For discussion of
standard views, see views-landing-page.

To understand the differences between the view types, see
materialized-view-compare.

An on-demand materialized view is a pre-computed aggregation pipeline
result that is stored on and read from disk. On-demand materialized
views are typically the results of a `$merge` or
`$out` stage.

## Comparison with Standard Views

MongoDB provides two different view types: **standard views** and
**on-demand materialized views**. Both view types return the results
from an aggregation pipeline.

- Standard views are computed when you read the view, and are not stored
  to disk.

- On-demand materialized views are stored on and read from disk. They
  use a `$merge` or `$out` stage to update the saved
  data.

### Indexes

Standard views use the indexes of the underlying collection. As a
result, you cannot create, drop or re-build indexes on a standard view
directly, nor get a list of indexes on the view.

You can create indexes directly on on-demand materialized views because
they are stored on disk.

### Performance

On-demand materialized views provide better read performance than
standard views because they are read from disk instead of computed as
part of the query. This performance benefit increases based on the
complexity of the pipeline and size of the data being aggregated.

On MongoDB Atlas, Atlas Stream Processing can also maintain a streaming materialized
view that updates continuously as source data changes. To learn more,
see Streaming Materialized Views.

## Create a Materialized View in the MongoDB Atlas UI

The example in this section uses the sample training dataset. To learn how to load the sample dataset 
into your MongoDB Atlas deployment, see Load Sample Data.

To create a materialized view in the MongoDB Atlas UI, follow these
steps:

**Step 1: In the MongoDB Atlas UI, go to the Clusters page for your project.**

a. If it's not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it's not already displayed, select your project
   from the Projects menu in the navigation bar.

#. In the sidebar, click Clusters under 
   the Database heading.

   The [Clusters](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23%2Fclusters) page displays.

**Step 2: Navigate to the collection**

a. For the cluster that contains the sample data,
   click Browse Collections.
#. In the left navigation pane, select the
   sample_training database.
#. Select the grades collection.

**Step 3: Click the Aggregation tab**

**Step 4: Click Add Stage**

**Step 5: Select an aggregation stage from the Select drop-down menu**

The aggregation stage transforms the data that you want to save as
a view. To learn more about available aggregation stages, see 
aggregation-pipeline-operator-reference.

For this example, add a new field with the `$set` stage:

a. Select `$set` from the Select drop-down
   menu.
#. Add the following syntax to the aggregation pipeline 
   editor to create an average score across all `score`
   values in the `scores` array within the `grades`
   collection:

   ```javascript
   {
     averageScore: { $avg: "$scores.score" }
   }
   ```

   MongoDB Atlas adds the `averageScore` value to each document.

**Step 6: Click Add Stage**

**Step 7: Add the `$out` stage**

a. Select the `$out` stage from the Select
   drop-down menu.
#. Add the following syntax to the aggregation pipeline
   to write the results of the pipeline to the `myView`
   collection in the `sample_training` database:

   ```javascript
   'myView'
   ```

#. Click Save Documents.

The `$out` stage writes the results of the
aggregation pipeline to the specified collection, which creates
the view. To learn more, see `$out`.

Refresh the list of collections to see the `myView` collection.

To learn how to query the `myView` collection in the MongoDB Atlas
UI, see View, Filter, and Sort Documents in the
MongoDB Atlas documentation.

## Example

The example uses the `movies` collection from the
sample_mflix dataset.
To learn how to load sample data, see
Load Sample Data.

### 1. Define the On-Demand Materialized View

The following `updateMovieStats` function defines a
`movieYearStats` materialized view that contains the
count and average IMDb rating of movies by year. The function
accepts a `startYear` parameter to update statistics for
movies released from that year forward.

```javascript
updateMovieStats = function(startYear) {
   db.movies.aggregate( [
      { $match: { year: { $gte: startYear } } },
      { $group: {
           _id: "$year",
           movieCount: { $sum: 1 },
           avgRating: { $avg: "$imdb.rating" }
      } },
      { $merge: { into: "movieYearStats", whenMatched: "replace" } }
   ] );
};
```

- The `$match` stage filters movies to process only
  those with a `year` value greater than or equal to
  `startYear`.

- The `$group` stage groups movies by `year`. The
  documents output by this stage have the form:

  ```javascript
  { "_id" : <year>, "movieCount" : <num>, "avgRating" : <num> }
  ```

- The `$merge` stage writes the output to the
  `movieYearStats` collection.

  The stage matches on the `_id` field and
  checks if each aggregation result
  matches an existing document:

  - When there is a match (that is, a
    document with the same year already exists in the
    collection), the stage replaces the existing document with the document from the
    aggregation results.

  - When there isn't a match, the
    stage inserts the document from the aggregation results into
    the collection (the default behavior when not matched).

### 2. Perform Initial Run

For the initial run, pass in a starting year to populate
`movieYearStats` with data from that year forward:

```javascript
updateMovieStats(2015);
```

After the initial run,
`db.movieYearStats.find().sort( { _id: 1 } )` returns
documents like the following:

```javascript
{ "_id" : 2015, "movieCount" : <num>, "avgRating" : <num> }
{ "_id" : 2016, "movieCount" : <num>, "avgRating" : <num> }
{ "_id" : 2017, "movieCount" : <num>, "avgRating" : <num> }
```

### 3. Refresh Materialized View

Assume a new movie is added to the `movies` collection
for 2016:

```javascript
db.movies.insertOne( {
   title: "Grove Test Movie",
   year: 2016,
   imdb: { rating: 7.5, votes: 500 }
} )
```

To refresh `movieYearStats` for 2016 onward, run the
function with a `startYear` of `2016`:

```javascript
updateMovieStats(2016);
```

The updated `movieYearStats` reflects the new movie in the
`movies` collection.
`db.movieYearStats.find().sort( { _id: 1 } )` returns:

```javascript
{ "_id" : 2015, "movieCount" : <num>, "avgRating" : <num> }
{ "_id" : 2016, "movieCount" : <num>, "avgRating" : <num> }
{ "_id" : 2017, "movieCount" : <num>, "avgRating" : <num> }
```

## Additional Information

The `$merge` stage:

- Can output to a collection in the same or different database.

- Creates a new collection if the output collection does not already
  exist.

- Can incorporate results (insert new documents, merge documents,
  replace documents, keep existing documents, fail the operation,
  process documents with a custom update pipeline) into an existing
  collection.

- Can output to a sharded collection. Input collection can
  also be sharded.

See `$merge` for:

- More information on `$merge` and available options

- Example: merge-mat-view-init-creation

- Example: merge-mat-view-refresh

- Example: merge-mat-view-insert-only
