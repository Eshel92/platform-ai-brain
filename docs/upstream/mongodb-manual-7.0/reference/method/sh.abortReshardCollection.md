<!-- Converted from reference/method/sh.abortReshardCollection.txt (reStructuredText). Includes are inlined. -->

# sh.abortReshardCollection() (mongosh method)

## Definition

**`sh.abortReshardCollection(namespace)`**

**New in version:** 5.0

During a resharding operation, you can
abort the operation with the `sh.abortReshardCollection()`
method.

You can abort a resharding operation at
any point until the commit phase. If the
resharding operation has reached the
commit phase before you run
the `sh.abortReshardCollection()` method, the method returns
an error.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `abortReshardCollection` command.

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

The `sh.abortReshardCollection()` method has the following syntax:

```javascript
sh.abortReshardCollection( <namespace> )
```

### Parameter

The `sh.abortReshardCollection()` method takes the following
parameter:

| Parameter | Type | Description |
|---|---|---|
| namespace | String | .. _method-abortReshardCollection-namespace: The name of the collection to shard in the form `"<database>.<collection>"`. |

## Example

### Abort a Resharding Operation

The following example aborts a running resharding operation on the `sales.orders` collection:

```javascript
sh.abortReshardCollection("sales.orders")
```

**See also:**

sharding-resharding
