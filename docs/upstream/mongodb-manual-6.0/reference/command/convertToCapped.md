<!-- Converted from reference/command/convertToCapped.txt (reStructuredText). Includes are inlined. -->

# convertToCapped

## Definition

**`convertToCapped`**

**Warning:** Do Not Run This Command On Sharded Collections

MongoDB does **not** support the `convertToCapped`
command on sharded collections.

The `convertToCapped` command converts an existing,
non-capped collection to a capped collection within the same
database.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in serverless instances.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB
   

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     convertToCapped: <collection>,
     size: <capped size>,
     writeConcern: <document>,
     comment: <any>  
   }
)
```

### Command Fields

The command takes the following fields:

| Field | Description |
|---|---|
| convertToCapped | The name of the existing collection to convert. |
| size | The maximum size, in bytes, for the capped collection. |
| writeConcern | Optional. A document expressing the write concern of the `drop` command. Omit to use the default write concern. |
| `comment` | .. include:: /includes/extracts/comment-content.rst |

`convertToCapped` takes an existing collection
(`<collection>`) and transforms it into a capped collection with
a maximum size in bytes, specified by the `size` argument
(`<capped size>`).

During the conversion process, the `convertToCapped`
command exhibits the following behavior:

- MongoDB traverses the documents in the original collection in
  natural order and loads the documents into a new
  capped collection.

- If the `capped size` specified for the capped collection is
  smaller than the size of the original uncapped collection, then
  MongoDB will overwrite documents in the capped collection based
  on insertion order, or *first in, first out* order.

- Internally, to convert the collection, MongoDB uses the following
  procedure

  - `cloneCollectionAsCapped` command creates the capped
    collection and imports the data.

  - MongoDB drops the original collection.

  - `renameCollection` renames the new capped collection
    to the name of the original collection.

- .. include:: /includes/fact-database-lock.rst

**Warning:**

The `convertToCapped` will not recreate indexes from
the original collection on the new collection, other than the
index on the `_id` field. If you need indexes on this
collection you will need to create these indexes after the
conversion is complete.

## Example

### Convert a Collection

The following example uses `db.collection.insertOne()` to create
an `events` collection, and `db.collection.stats()` to obtain
information about the collection:

```javascript
db.events.insertOne( { click: 'button-1', time: new Date() } )
db.events.stats()
```

MongoDB will return the following:

```javascript
{
        "ns" : "test.events",
        ...
        "capped" : false,
        ...
}
```

To convert the `events` collection into a capped collection and view the
updated collection information, run the following commands:

```javascript
db.runCommand( { convertToCapped: 'events', size: 8192 } )
db.events.stats()
```

MongoDB will return the following:

```javascript
{
     "ns" : "test.events",
     ...
     "capped" : true,
     "max" : NumberLong("9223372036854775807"),
     "maxSize" : 8192,
     ...
}
```

The `convertToCapped` will not recreate indexes from
the original collection on the new collection, other than the
index on the `_id` field. If you need indexes on this
collection you will need to create these indexes after the
conversion is complete.

**See also:**

`create`
