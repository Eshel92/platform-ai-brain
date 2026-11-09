<!-- Converted from reference/method/db.collection.createSearchIndex.txt (reStructuredText). Includes are inlined. -->

# db.collection.createSearchIndex() (mongosh method)

## Definition

**`db.collection.createSearchIndex()`**

**New in version:** 7.0 (*Also available starting in 6.0.7*)

Creates an Atlas Search index or Atlas Vector Search index on a specified collection.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `createSearchIndexes` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

## Syntax

Command syntax:

```javascript
db.<collection>.createSearchIndex(
   <name>,
   {
      <definition>
   }
)
```

## Command Fields

`createSearchIndex()` takes these fields:

| Field | Type | Necessity | Description |
|---|---|---|---|
| `name` | string | Optional | Name of the search index to create. You cannot create multiple indexes with the same name on a single collection. If you do not specify a `name`, the index is named `default`. |
| `definition` | document | Required | Document describing the index to create. For details on `definition` syntax, see search-index-definition-create-mongosh. |

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

## Behavior

`createSearchIndex()` triggers an index build. There may be a delay
between when you receive a response from the command and when the index
is ready.

To see the status of your search indexes, use the
`$listSearchIndexes` aggregation stage.

## Access Control

If your deployment enforces access control, the user running
`createSearchIndex()` must have the `createSearchIndexes` privilege
action on the database or collection:

```javascript
{
   resource: {
      db : <database>,
      collection: <collection>
   },
   actions: [ "createSearchIndexes" ]
}
```

The built-in `readWrite` role provides the
`createSearchIndexes` privilege. The following example grants
`accountUser01` the `readWrite` role on the `products` database:

```javascript
db.grantRolesToUser(
   "accountUser01",
   [ { role: "readWrite", db: "products" } ]
)
```

## Examples

### Create a Search Index on All Fields

The following example creates a search index named `searchIndex01` on
the `movies` collection:

```javascript
db.movies.createSearchIndex(
   "searchIndex01",
   { mappings: { dynamic: true } }
)
```

The index definition specifies `mappings: { dynamic: true }`, which
means that the index contains all fields in the collection that have
supported data types.

### Create a Search Index with a Language Analyzer

A language analyzer introduces stop-words, which are words that are not
significant enough to be indexed.

The following example creates a search index named `frenchIndex01` on
the `cars` collection, and specifies the `lucene.french` analyzer on
the `fr` field:

```javascript
db.cars.createSearchIndex(
   "frenchIndex01",
   {
      mappings: {
         fields: {
            subject: {
               fields: {
                  fr: {
                     analyzer: "lucene.french",
                     type: "string"
                  }
               },
               type: "document"
            }
         }
      }
   }
)
```

To learn more about language analyzers, see
ref-language-analyzers.

### Create a Search Index with the Default Name

The following `createSearchIndex()` method only specifies the index
definition and omits the index name. The command creates a search index
with the name `default` on the `food` collection:

```javascript
db.food.createSearchIndex(
   {
      mappings: {
         fields: {
            title: {
               type: "string"
            }
         }
      }
   }
)
```
