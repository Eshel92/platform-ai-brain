<!-- Converted from reference/method/ObjectId.getTimestamp.txt (reStructuredText). Includes are inlined. -->

# ObjectId.getTimestamp() (mongosh method)

## Definition

**`ObjectId.getTimestamp()`**

Returns the timestamp portion of the `ObjectId()` as a Date.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Example

The following example calls the `getTimestamp()` method on an `ObjectId()`:

```javascript
ObjectId("507c7f79bcf86cd7994f6c0e").getTimestamp()
```

This will return the following output:

```javascript
ISODate("2012-10-15T21:26:17Z")
```

**See also:**

ObjectId BSON Type
