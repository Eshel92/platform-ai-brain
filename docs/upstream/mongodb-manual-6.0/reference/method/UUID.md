<!-- Converted from reference/method/UUID.txt (reStructuredText). Includes are inlined. -->

# UUID()

## Definition

Generates a BSON UUID (Universally unique identifier) object.

`UUID()` has the following syntax:

**`UUID(<string>)`**

| Parameter | Type | Description |
|---|---|---|
| `hex` | string | Optional. Specify a 36 character string to convert to a UUID BSON object. If not provided, MongoDB generates a random UUID in [RFC 4122 v4](https://tools.ietf.org/html/rfc4122) format. |

:returns: A BSON UUID object.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Example

### Convert Character String to UUID

Create a 36 character string you wish to convert to a UUID:

```javascript
var myuuid = '3b241101-e2bb-4255-8caf-4136c566a962'
```

The following command outputs the `myuuid` variable as a BSON UUID object:

```javascript
UUID(myuuid)
```

This command generates the following output:

```javascript
UUID("3b241101-e2bb-4255-8caf-4136c566a962")
```

### Generate Random UUID

You can run the `UUID()` method without
specifying an argument to generate a random UUID:

```javascript
UUID()
```

This command outputs a random UUID in the following form:

```javascript
UUID("dee11d4e-63c6-4d90-983c-5c9f1e79e96c")
```
