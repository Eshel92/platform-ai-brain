<!-- Converted from reference/method/ObjectId.toString.txt (reStructuredText). Includes are inlined. -->

# ObjectId.toString() (mongosh method)

**`ObjectId.toString()`**

Returns the string representation of the `ObjectId()`.

## Compatibility

You can use `ObjectId.toString()` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Example

The following example:

- Generates a new `ObjectId()` and stores it in the 
  variable `myObjectId`.

- Creates a string representation of `myObjectId` using
  the `toString()` method.
  
- Stores the string representation in the variable `myObjectIdString`.

Run the following commands in `mongosh`:

```javascript
myObjectId = ObjectId("507c7f79bcf86cd7994f6c0e")
myObjectIdString = myObjectId.toString()
```

The operation returns the following string:

```javascript
507c7f79bcf86cd7994f6c0e
```

To confirm the type of `myObjectIdString`, use the `typeof` JavaScript operator:

```javascript
typeof myObjectIdString
```

The operation returns the following:

```javascript
string
```
