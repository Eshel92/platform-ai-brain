<!-- Converted from reference/method/db.collection.dropSearchIndex.txt (reStructuredText). Includes are inlined. -->

# db.collection.dropSearchIndex()

## Definition

**`db.collection.dropSearchIndex()`**

**New in version:** 6.0.7

Deletes an existing Atlas Search index or Atlas Vector Search index.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `dropSearchIndex` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in serverless instances. For more information, 
see Unsupported Commands.

## Syntax

Command syntax:

```javascript
db.<collection>.dropSearchIndex(<name>)
```

## Command Fields

`dropSearchIndex()` takes the following field:

| Field | Type | Necessity | Description |
|---|---|---|---|
| `name` | string | Required | Name of the search index to drop. |

## Behavior

After you run `dropSearchIndex()`, there may be a delay between when you
receive a response from the command and when the index is deleted.

To see the status of your search indexes, use the
`$listSearchIndexes` aggregation stage. Once your index is
deleted, that index no longer appears in the `$listSearchIndexes`
output.

## Access Control

If your deployment enforces access control, the user running the
`dropSearchIndex()` method must have the
`dropSearchIndex` privilege action on the database:

```javascript
{ resource: { database : true }, actions: [ "dropSearchIndex" ] }
```

The built-in `dbAdmin` and `readWrite` roles provide
the `dropSearchIndex` privilege. The following example grants the
`readWrite` role on the `qa` database:

```javascript
db.grantRolesToUser(
   "<user>",
   [ { role: "readWrite", db: "qa" } ]
)
```

## Example

The following example deletes a search index named `searchIndex01` on
the `movies` collection:

```javascript
db.movies.dropSearchIndex("searchIndex01")
```
