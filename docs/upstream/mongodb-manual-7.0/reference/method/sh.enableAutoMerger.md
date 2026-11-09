<!-- Converted from reference/method/sh.enableAutoMerger.txt (reStructuredText). Includes are inlined. -->

# sh.enableAutoMerger() (mongosh method)

## Definition

**`sh.enableAutoMerger(namespace)`**

**New in version:** 7.0

Enables automatic chunk merges for a namespace.

`sh.enableAutoMerger()` is a `mongosh` helper method. It
is effectively the same as running the 
`configureCollectionBalancing` command with the 
`enableAutoMerger` field set to `true`.

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
sh.enableAutoMerger( <namespace> )
```

## Method Field

The method takes the following field:

| Field | Type | Necessity | Description |
|---|---|---|---|
| `namespace` | String | Required | Namespace in the format `"<database>.<collection>"`. Method enables automatic chunk merges for the supplied namespace. |

## Behavior

To set the time intervals for automatic chunk merges, use these
parameters:

- `autoMergerIntervalSecs`
- `autoMergerThrottlingMS`

**Note:**

You can set these parameters on config servers only.

## Example

The following example enables automatic chunk merges for
`"testDatabase.myCollection"`. Run the example from
`mongos`:

```javascript
sh.enableAutoMerger( "testDatabase.myCollection" )
```

## Learn More

- automerger-concept
- `sh.disableAutoMerger()` method
- `sh.startAutoMerger()` method
- `sh.stopAutoMerger()` method

- `configureCollectionBalancing` command
- `mergeAllChunksOnShard` command
- `autoMergerIntervalSecs` parameter
- `autoMergerThrottlingMS` parameter
