<!-- Converted from reference/method/sh.commitReshardCollection.txt (reStructuredText). Includes are inlined. -->

# sh.commitReshardCollection()

## Definition

**`sh.commitReshardCollection(namespace)`**

**New in version:** 5.0

During a resharding operation, MongoDB does not block writes until
the estimated duration to complete the resharding operation is
below **two seconds**.

If the current estimate is above two seconds but the time frame is
acceptable to you, you can finish resharding faster. The
`sh.commitReshardCollection()` method blocks writes early and
forces the resharding operation to complete.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `commitReshardCollection` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `sh.commitReshardCollection()` method has the following
syntax:

```javascript
sh.commitReshardCollection( <namespace> )
```

### Parameter

The `sh.commitReshardCollection()` method takes the following
parameter:

| Parameter | Type | Description |
|---|---|---|
| namespace | String | .. _method-commitReshardCollection-namespace: The name of the collection to shard in the form `"<database>.<collection>"`. |

## Example

### Commit a Resharding Operation

The following command forces the resharding operation on the `sales.orders` to block writes and
complete:

```javascript
sh.commitReshardCollection("sales.orders")
```

**See also:**

sharding-resharding
