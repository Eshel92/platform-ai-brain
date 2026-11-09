<!-- Converted from reference/command/dropSearchIndex.txt (reStructuredText). Includes are inlined. -->

# dropSearchIndex (database command)

## Definition

**`dropSearchIndex`**

**New in version:** 7.0 (*Also available starting in 6.0.7*)

Deletes an existing Atlas Search index.

The `mongosh` method `db.collection.dropSearchIndex()`
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
      dropSearchIndex: "<collection name>",
      id: "<index Id>",
      name: "<index name>"
   }
)
```

## Command Fields

The `dropSearchIndex` command takes the following fields:

| Field | Type | Necessity | Description |
|---|---|---|---|
| `dropSearchIndex` | string | Required | Name of the collection that contains the index to delete. |
| `id` | string | Conditional | `id` of the index to delete. You must specify **either** the `id` or `name` field. |
| `name` | string | Conditional | Name of the index to delete. You must specify **either** the `id` or `name` field. |

## Behavior

After you run the `dropSearchIndex` command, there may be a delay between when you
receive a response from the command and when the index is deleted.

To see the status of your search indexes, use the
`$listSearchIndexes` aggregation stage. Once your index is
deleted, that index no longer appears in the `$listSearchIndexes`
output.

## Access Control

If your deployment enforces access control, the user running
the `dropSearchIndex` command must have the `dropSearchIndex` privilege
action on the database or collection:

```javascript
{
   resource: {
      db : <database>,
      collection: <collection>
   },
   actions: [ "dropSearchIndex" ]
}
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

## Output

A successful `dropSearchIndex` command returns the following:

```javascript
{
   ok: 1
}
```

## Example

The following example deletes a search index named `searchIndex01` on
the `contacts` collection:

```javascript
db.runCommand( {
   dropSearchIndex: "contacts",
   name: "searchIndex01"
} )
```
