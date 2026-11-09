<!-- Converted from reference/method/sh.disableAutoMerger.txt (reStructuredText). Includes are inlined. -->

# sh.disableAutoMerger() (mongosh method)

## Definition

**`sh.disableAutoMerger(namespace)`**

**New in version:** 7.0

Disables automatic chunk merges for a namespace.

`sh.disableAutoMerger()` is a `mongosh` helper method. It
is effectively the same as running the 
`configureCollectionBalancing` command with the 
`enableAutoMerger` field set to `false`.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `configureCollectionBalancing` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

```javascript
sh.disableAutoMerger( <namespace> )
```

## Method Field

The method takes the following field:

| Field | Type | Necessity | Description |
|---|---|---|---|
| `namespace` | String | Required | Namespace in the format `"<database>.<collection>"`. Method enables automatic chunk merges for the supplied namespace. |

## Behavior

When the method runs, it stops the AutoMerger. Any in 
progress operations issued by the AutoMerger are completed.

## Example

The following example disables automatic chunk merges for
`"testDatabase.myCollection"`. Run the example from
`mongos`:

```javascript
sh.disableAutoMerger( "testDatabase.myCollection" )
```

## Learn More

- automerger-concept
- `sh.startAutoMerger()` method
- `sh.stopAutoMerger()` method
- `sh.enableAutoMerger()` method

- `configureCollectionBalancing` command
- `mergeAllChunksOnShard` command
- `autoMergerIntervalSecs` parameter
- `autoMergerThrottlingMS` parameter
