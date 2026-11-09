<!-- Converted from reference/method/db.collection.updateSearchIndex.txt (reStructuredText). Includes are inlined. -->

# db.collection.updateSearchIndex() (mongosh method)

## Definition

**`db.collection.updateSearchIndex()`**

**New in version:** 7.0 (*Also available starting in 6.0.7*)

Updates an existing Atlas Search index or Atlas Vector Search index.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `updateSearchIndex` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

## Syntax

Command syntax:

```javascript
db.<collection>.updateSearchIndex(
   <name>,
   {
      <definition>
   }
)
```

## Command Fields

`updateSearchIndex()` takes these fields:

* - Field
  - Type
  - Necessity
  - Description

* - `name`
  - string
  - Required
  - Name of the search index to update.

* - `definition`
  - document
  - Required
  - Document describing the index to create. The `definition` syntax
    depends on whether you create a standard search index or a Vector
    Search index. For the `definition` syntax, see:

    - search-index-definition-update
    - vector-search-index-definition-update

### Search Index Definition Syntax

The search index definition takes the following fields:

```javascript
{
   analyzer: "<analyzer-for-index>", 
   searchAnalyzer: "<analyzer-for-query>", 
   mappings: { 
      dynamic: <boolean>,
      fields: { <field-definition> } 
   },
   analyzers: [ <custom-analyzer> ],
   storedSource: <boolean> | {
      <stored-source-definition>
   },
   synonyms: [ {
      name: "<synonym-mapping-name>",
      source: {
         collection: "<source-collection-name>"
      },
      analyzer: "<synonym-mapping-analyzer>"
   } ]
}
```

* - Field
  - Type
  - Necessity
  - Description

* - `analyzer`
  - string 
  - Optional 
  - Specifies the analyzer to apply to 
    string fields when indexing.

    If you omit this field, the index uses the standard analyzer.

* - `searchAnalyzer`
  - string 
  - Optional
  - Specifies the analyzer to apply to query
    text before the text is searched.

    If you omit this field, the index uses the same analyzer specified
    in the `analyzer` field.

    If you omit both the `searchAnalyzer` and the `analyzer`
    fields, the index uses the standard analyzer.

* - `mappings`
  - object
  - Required
  - Specifies how to index fields on different paths for this index. 

* - `mappings.dynamic`
  - boolean
  - Optional
  - Enables or disables dynamic field mapping for this index.

    If set to `true`, the index contains all fields containing
    supported data types.

    If set to `false`, you must specify individual fields to index 
    using `mappings.fields`.

    If omitted, defaults to `false`.

* - `mappings.fields`
  - document
  - Conditional
  - Required only if dynamic mapping is disabled. 

    Specifies the fields to index. To learn more, see
    fts-field-mappings. 

* - `analyzers`
  - array
  - Optional 
  - Specifies the custom-analyzers to use in this index.

* - `storedSource` 
  - boolean or Stored Source Definition 
  - Optional 
  - Specifies document fields to store for queries performed using
    the returnedStoredSource
    option.

    You can store fields of all bson-data-chart on Atlas Search.
    The `storedSource` value can be one of these:

    - `true`, to store all fields  
    - `false`, to not store any fields 
    - An object that specifies the
      fields to `include` or `exclude` from storage

    If omitted, defaults to `false`.

    To learn more, see fts-stored-source-definition.

* - `synonyms` 
  - array of Synonym Mapping Definitions
  - Optional 
  - Specifies synonym mappings to use in your index. Configuring
    synonyms allows you to you index and search for words that have
    the same or a similar meaning.

    To learn more, see synonyms-ref.

### Vector Search Index Definition Syntax

The vector search index definition takes the following fields:

```javascript
{
  "fields": [ 
    {
      "type": "vector" | "filter",
      "path": "<field-to-index>",
      "numDimensions": <number-of-dimensions>,
      "similarity": "euclidean" | "cosine" | "dotProduct"
    }
  ]
}
```

For explanations of vector search index definition fields, see
avs-types-vector-search.

## Behavior

`updateSearchIndex()` triggers an index build with the new index
definition. There may be a delay between when you receive a response
from the command and when the updated index is ready.

The old index definition can still support queries while the new index
is being built. Once the new index finishes building, the old index is
no longer usable. To see the status of your search indexes, use the
`$listSearchIndexes` aggregation stage.

## Access Control

If your deployment enforces access control, the user running
`updateSearchIndex()` must have the `updateSearchIndex` privilege
action on the database or collection:

```javascript
{
   resource: {
      db : <database>,
      collection: <collection>
   },
   actions: [ "updateSearchIndex" ]
}
```

The built-in `readWrite` and `restore` roles provide
the `updateSearchIndex` privilege. The following example grants the
`readWrite` role on the `qa` database:

```javascript
db.grantRolesToUser(
   "<user>",
   [ { role: "readWrite", db: "qa" } ]
)
```

## Example

The following example creates a new Atlas Search index and then updates that
index.

#. Create a search index named `searchIndex01` on the `movies`
   collection:

   ```javascript
   db.movies.createSearchIndex(
      "searchIndex01",
      {
         mappings: { dynamic: true },
         storedSource: {
            exclude: [ "imdb.rating" ]
         }
      }
   )
   ```

#. Update the `searchIndex01` index:

   ```javascript
   db.movies.updateSearchIndex(
      "searchIndex01",
      {
         mappings: { dynamic: true },
         storedSource: {
            exclude: [ "movies" ]
         }
      }
   )
   ```
