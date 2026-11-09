<!-- Converted from reference/method/ObjectId.txt (reStructuredText). Includes are inlined. -->

# ObjectId()

## Description

**`ObjectId(<value>)`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Returns a new objectid. The 12-byte objectid consists
of:

- A 4-byte timestamp, representing the ObjectId's creation, measured in seconds since the
  Unix epoch.

- A 5-byte random value generated once per client-side process. This random value is unique to the
  machine and process. If the process restarts or the primary node of the process changes,
  this value is re-generated.

- A 3-byte incrementing counter per client-side process, initialized to a random value.
  The counter resets when a process restarts.

For timestamp and counter values, the most significant bytes appear
first in the byte sequence (big-endian). This is unlike other BSON
values, where the least significant bytes appear first (little-endian).

If an integer value is used to create an ObjectId, the integer replaces
the timestamp.

## Compatibility

You can use `ObjectId()` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

`ObjectId()` can accept one of the following inputs:

| Input Type | Description |
|---|---|
| `hexadecimal` | Optional. A 24 character hexadecimal string value for the new ObjectId. |
| `integer` | Optional. The integer value, in seconds, is added to the Unix epoch to create the new timestamp. |

## Methods

`ObjectId()` has the following methods:

| Methods | Description |
|---|---|
| `ObjectId.getTimestamp()` | Returns the timestamp portion of the object as a Date. |
| `ObjectId.toString()` | Returns the ObjectId as a hexadecimal string. |

## Behavior

Starting in MongoDB 5.0, `mongosh` replaces the legacy `mongo`
shell. The `ObjectId()` methods work differently in `mongosh` than
in the legacy `mongo` shell. For more information on the legacy
methods, see Legacy mongo Shell.

## Examples

### Generate a New ObjectId

To generate a new ObjectId, use `ObjectId()` with no argument:

```javascript
newObjectId = ObjectId()
```

In this example, the value of `newObjectId` is:

```javascript
ObjectId("507f1f77bcf86cd799439011")
```

### Return a Hexadecimal String

To return the ObjectId as a hexadecimal string, use the `toString()`
method.

```javascript
ObjectId("507f191e810c19729de860ea").toString()
```

The method returns:

```none
507f191e810c19729de860ea
```

### Specify a Date

You can use a custom document-bson-type-date to specify an ObjectId. 

**Step 1: Set a variable for your specified date**

Internally, Date objects are stored as signed 
64-bit integer that represents the number of milliseconds since the 
Unix epoch. To learn more, see `Date()`.

```javascript
myDate = new Date( "2024-01-01" )
```

**Step 2: Convert your Date object to seconds**

```javascript
timestamp = Math.floor( myDate / 1000 )
```

**Step 3: Set your new ObjectId with `timestamp` as the argument**

You can verify the Date by using `ObjectId.getTimestamp()`.

```javascript
newObjectId = ObjectId(timestamp) 
```

Output:

```javascript
ObjectId("6592008029c8c3e4dc76256c")
```

### Specify an Integer String

If you want to adjust the ObjectId timestamp, use an integer to generate
a new ObjectId.

```javascript
newObjectId = ObjectId(32)
```

The ObjectId value resembles:

```javascript
ObjectId("00000020f51bb4362eee2a4d")
```

The example ObjectId consists of:

- A four byte time stamp, `00000020`
- A five byte random element, `f51bb4362e`
- A three byte counter, `ee2a4d`

The first four bytes of the ObjectId are the number of seconds since the
Unix epoch. In this example, the ObjectId timestamp is
`00000020` which is `32` in hexadecimal.

### Specify a Hexadecimal String

If you want to use a hexadecimal string to specify an ObjectId, pass a
unique, 24 character hexadecimal value when you call
`ObjectId()`:

```javascript
newObjectId = ObjectId("507f191e810c19729de860ea")
```

**See also:**

ObjectId BSON Type
