<!-- Converted from reference/command/updateSearchIndex.txt (reStructuredText). Includes are inlined. -->

# updateSearchIndex

## Definition

**`updateSearchIndex`**

**New in version:** 6.0.7

Updates an existing Atlas Search index.

The `mongosh` method `db.collection.updateSearchIndex()`
provides a wrapper around the `updateSearchIndex` database command.

**Important:**

This command can only be run on a deployment hosted on
MongoDB Atlas, and requires an Atlas cluster tier of at
least M10.

## Syntax

Command syntax:

```javascript
db.runCommand(
   {
      updateSearchIndex: "<collection name>",
      id: "<index Id>",
      name: "<index name>",
      definition: {
         /* search index definition fields */
      }
   }
)
```

## Command Fields

The `updateSearchIndex` command takes the following fields:

| Field | Type | Necessity | Description |
|---|---|---|---|
| `updateSearchIndex` | string | Required | Name of the collection that contains the index to update. |
| `id` | string | Conditional | `id` of the index to update. You must specify **either** the `id` or `name` field. |
| `name` | string | Conditional | Name of the index to update. You must specify **either** the `id` or `name` field. |
| `definition` | document | Required | Document describing the updated search index definition. The specified definition replaces the prior definition in the search index. For details on `definition` syntax, see search-index-definition-update. |

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

The `updateSearchIndex` command triggers an index build with the new index
definition. There may be a delay between when you receive a response
from the command and when the updated index is ready.

The old index definition can still support queries while the new index
is being built. Once the new index finishes building, the old index is
no longer usable. To see the status of your search indexes, use the
`$listSearchIndexes` aggregation stage.

## Access Control

If your deployment enforces access control, the user running
the `updateSearchIndex` command must have the `updateSearchIndex` privilege
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

## Output

A successful `updateSearchIndex` command returns the following:

```javascript
{
   ok: 1
}
```

**Important:**

The response field `ok: 1` indicates that the command was successful.
However, there may be a delay between when you receive the response and
when the updated index is ready and replaces the original index.

To see the status of your search indexes, use the
`$listSearchIndexes` aggregation stage.

## Example

The following example updates a search index named `searchIndex01` on
the `contacts` collection:

```javascript
db.runCommand( {
   updateSearchIndex: "contacts",
   name: "searchIndex01",
   definition:
      {
         mappings: { dynamic: true },
         storedSource: {
            exclude: [ "directors", "imdb.rating" ]
         }
      }
} )
```
