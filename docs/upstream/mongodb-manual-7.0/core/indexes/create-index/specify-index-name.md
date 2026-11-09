<!-- Converted from core/indexes/create-index/specify-index-name.txt (reStructuredText). Includes are inlined. -->

# Specify an Index Name

When you create an index, you can give the index a custom name. Giving
your index a name helps distinguish different indexes on your
collection. For example, you can more easily identify the indexes used
by a query in the query plan's explain results
if your indexes have distinct names.

To specify the index name, include the `name` option when you create
the index:

```javascript
db.<collection>.createIndex( 
   { <field>: <value> }, 
   { name: "<indexName>" } 
)
```

## About this Task

Before you specify an index name, consider the following:

- Index names must be unique. Creating an index with 
  the name of an existing index returns an error.

- You can't rename an existing index. Instead, you must drop and recreate the index with a new name.

### Default Index Names

If you don't specify a name during index creation, 
the system generates the name by concatenating each index key 
field and value with underscores. For example:

| Index | Default Name |
|---|---|
| `{ score : 1 }` | `score_1` |
| `{ content : "text", "description.tags": "text" }` | `content_text_description.tags_text` |
| `{ category : 1, locale : "2dsphere"}` | `category_1_locale_2dsphere` |
| `{ "fieldA" : 1, "fieldB" : "hashed", "fieldC" : -1 }` | `fieldA_1_fieldB_hashed_fieldC_-1` |

## Procedure

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

Create a text index on the `name` and `text` fields. Set the index
`name` to `CommentsTextIndex`:

```javascript
```

Output:

```javascript
```

 

## Results

After you create the index, you can use the
`db.collection.getIndexes()` method to get the index name:

```javascript
```

Output:

```javascript
```

## Learn More

- To learn how to create an index, see manual-create-an-index.
- For more information about index properties, see index-properties.
