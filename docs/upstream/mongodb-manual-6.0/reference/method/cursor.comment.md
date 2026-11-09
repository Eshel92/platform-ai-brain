<!-- Converted from reference/method/cursor.comment.txt (reStructuredText). Includes are inlined. -->

# cursor.comment()

## Definition

**`cursor.comment()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Adds a `comment` field to the query.

`cursor.comment()` has the following syntax:

```javascript
cursor.comment( <string> )
```

`comment()` has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `comment` | string | The comment to apply to the query. |

          
          

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

`comment()` associates a comment string with the
find operation. This can make it easier to track a particular query in the
following diagnostic outputs:

- The `system.profile <`
- The `QUERY` log component
- `db.currentOp()`

See configure log verbosity for the
`mongod` log, the
Database Profiler tutorial, or
the `db.currentOp()` command.

## Example

The following operation attaches a comment to a query on the `restaurants`
collection:

```javascript
db.restaurants.find(
   { "borough" : "Manhattan" }
).comment( "Find all Manhattan restaurants" )
```

## Output Examples

### `system.profile <`

The following is an excerpt from the
`system.profile <`:

```javascript
{
   "op" : "query",
   "ns" : "guidebook.restaurant",
   "query" : {
      "find" : "restaurant",
      "filter" : {
         "borough" : "Manhattan"
      },
      "comment" : "Find all Manhattan restaurants"
   },
   ...
}
```

### `mongod` log

The following is an excerpt from the `mongod` log. It has been
formatted for readability.

**Important:**

The verbosity level for `QUERY` must be greater than `0`.
See log-messages-configure-verbosity

```javascript
2015-11-23T13:09:16.202-05:00 I COMMAND  [conn1]
   command guidebook.restaurant command: find {
      find: "restaurant",
      filter: { "borough" : "Manhattan" },
      comment: "Find all Manhattan restaurants"
   }
   ...
```

### `db.currentOp()`

Suppose the following operation is currently running on a `mongod`
instance:

```javascript
db.restaurants.find(
   { "borough" : "Manhattan" }
).comment("Find all Manhattan restaurants")
```

Running the `db.currentOp()` command returns the following:

```javascript
{
   "inprog" : [
      {
         "host" : "198.51.100.1:27017",
         "desc" : "conn3",
         "connectionId" : 3,
         ...

         "op" : "query",
         "ns" : "test.$cmd",
         "command" : {
            "find" : "restaurants",
            "filter" : {
               "borough" : "Manhattan"
            },
            "comment" : "Find all Manhattan restaurants",
            "$db" : "test"
         },
         "numYields" : 0,
         ...
      }
   ],
   "ok" : 1
}
```
