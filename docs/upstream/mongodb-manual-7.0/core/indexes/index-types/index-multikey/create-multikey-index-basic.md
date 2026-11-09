<!-- Converted from core/indexes/index-types/index-multikey/create-multikey-index-basic.txt (reStructuredText). Includes are inlined. -->

# Create an Index on an Array Field

You can create an index on a field containing an array value to improve
performance for queries on that field. When you create an index on a
field containing an array value, MongoDB stores that index as a multikey
index.

To create an index, use the `db.collection.createIndex()`
method. Your operation should resemble this prototype:

```javascript
db.<collection>.createIndex( { <field>: <sortOrder> } )
```

## About this Task

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

You regularly run a query that returns movies released before 1910 that
have the `Short` genre. You can create an index on the `genres`
field to improve performance for this query.

## Procedure

The following operation creates an ascending multikey index on the
`genres` field of the `movies` collection:

```javascript
```

Output:

```javascript
```

Because `genres` contains an array value, MongoDB stores this index
as a multikey index.

## Results

The index contains a key for each individual value that appears in the
`genres` field. For example, for the movie `The Godfather`, which
stores the genres `Crime` and `Drama`, the index contains one key
for each genre. The index is ascending, meaning the keys are stored in
ascending order.

The index supports queries that select on the `genres` field. For
example, the following query returns movies where at least one element
in the `genres` array is `Short` and the movie was released before
1910:

```javascript
```

Output:

```javascript
```

**Note:**

Documents in the `movies` collection contain additional fields not 
shown here.

## Learn More

- To learn how to create a multikey index on embedded document fields,
  see index-create-multikey-embedded.

- To learn about multikey index bounds, see
  indexes-multikey-bounds.
