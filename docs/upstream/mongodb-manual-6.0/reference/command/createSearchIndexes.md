<!-- Converted from reference/command/createSearchIndexes.txt (reStructuredText). Includes are inlined. -->

# createSearchIndexes

## Definition

**`createSearchIndexes`**

**New in version:** 6.0.7

Creates one or more Atlas Search indexes on a specified collection.

The `mongosh` method `db.collection.createSearchIndex()`
provides a wrapper around the `createSearchIndexes` database command.

**Important:**

This command can only be run on a deployment hosted on
MongoDB Atlas, and requires an Atlas cluster tier of at
least M10.

## Syntax

Command syntax:

```javascript
db.runCommand(
   {
      createSearchIndexes: "<collection name>",
      indexes: [
         {
            name: "<index name>",
            definition: {
               /* search index definition fields */
            } 
        },
        ...
      ]
   }
)
```

## Command Fields

The `createSearchIndexes` command takes the following fields:

| Field | Type | Necessity | Description |
|---|---|---|---|
| `createSearchIndexes` | string | Required | Name of the collection on which to create the search index. |
| `indexes` | array | Required | Array of documents describing the indexes to create. |
| `indexes.name` | string | Optional | Name of the search index to create. You cannot create multiple indexes with the same name on a single collection. If you do not specify a `name`, the index is named `default`. |
| `indexes.definition` | document | Required | Document describing the index to create. For details on `definition` syntax, see search-index-definition-create. |

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

The `createSearchIndexes` command triggers an index build. There may be a delay
between when you receive a response from the command and when the index
is ready.

To see the status of your search indexes, use the
`$listSearchIndexes` aggregation stage.

## Access Control

If your deployment enforces access control, the user running
the `createSearchIndexes` command must have the `createSearchIndexes` privilege
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

## Output

The `createSearchIndexes` command output resembles the following:

```javascript
{
   ok: 1,
   indexesCreated: [
      {
         id: "<index Id>",
         name: "<index name>"   
      }
   ]
}
```

**Important:**

The response field `ok: 1` indicates that the command was
successful. However, there may be a delay between when you receive
the response and when the created indexes are ready for use.

To see the status of your search indexes, use the
`$listSearchIndexes` aggregation stage.

## Examples

### Create a Search Index on All Fields

The following example creates a search index named `searchIndex01` on
the `contacts` collection:

```javascript
db.runCommand( {
   createSearchIndexes: "contacts",
   indexes: [
      {
         name: "searchIndex01",
         definition: { mappings: { dynamic: true } }
      }
   ]
} )
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
db.runCommand( {
   createSearchIndexes: "cars",
   indexes: [
      {
         name: "frenchIndex01",
         definition: {
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
      }
   ]
} )
```

To learn more about language analyzers, see
ref-language-analyzers.

### Create Multiple Search Indexes

The following command creates two search indexes on the `products`
collection, `searchIndex02` and `searchIndex03`:

```javascript
db.runCommand( {
   createSearchIndexes: "products",
   indexes: [
      {
         name: "searchIndex02",
         definition: {
            mappings: {
               fields: {
                  title: {
                     type: "string",
                     analyzer: "lucene.simple"
                  }
               }
            }
         }
      },
      {
         name: "searchIndex03",
         definition:
            {
               mappings: { dynamic: true }
            }
      }
   ]
} )
```

`searchIndex02` uses a simple analyzer on
the `title` field. The simple analyzer divides text into searchable
terms based on non-letter characters, such as whitespace, punctuation,
or digits.

`searchIndex03` uses a dynamic field mapping, meaning the index
contains all fields in the collection that have supported data
types.
