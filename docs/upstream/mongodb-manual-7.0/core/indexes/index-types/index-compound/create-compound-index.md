<!-- Converted from core/indexes/index-types/index-compound/create-compound-index.txt (reStructuredText). Includes are inlined. -->

# Create a Compound Index

**Compound indexes** are indexes that contain references to multiple
fields. Compound indexes improve performance for queries on exactly the
fields in the index or fields in the index prefix. 

To create a compound index, use the
`db.collection.createIndex()` method:

```javascript
db.<collection>.createIndex( {
   <field1>: <sortOrder>, 
   <field2>: <sortOrder>,
   ...
   <fieldN>: <sortOrder>
} )
```

## Restriction

You can specify up to 32 fields in a single compound index.

## Before You Begin

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

## Procedure

The following operation creates a compound index containing the
`title` and `metacritic` fields:

```javascript
```

Output:

```javascript
```

In this example:

- The index on `title` is ascending (`1`).
- The index on `metacritic` is descending (`-1`).

## Results

The created index supports queries that select on:

- Both `title` and `metacritic` fields.

- Only the `title` field, because `title` is a prefix of the compound index.

For example, the index supports these queries:

```javascript
```

Output:

```javascript
```

```javascript
```

Output:

```javascript
```

The index **does not** support queries on only the `metacritic` field,
because `metacritic` is not part of the index prefix. For example,
the index does not support this query:

```javascript
```

Output:

```javascript
```

## Learn More

- To learn how to create efficient compound indexes, see
  esr-indexing-guideline.

- To learn how sort order (ascending or descending) impacts performance
  of compound indexes, see sorting-with-indexes.

- To learn about other index types, see index-types.

- To learn what properties you can specify for indexes, see
  index-properties.
