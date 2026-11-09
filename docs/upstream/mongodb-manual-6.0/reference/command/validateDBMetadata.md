<!-- Converted from reference/command/validateDBMetadata.txt (reStructuredText). Includes are inlined. -->

# validateDBMetadata

## Definition

**New in version:** 5.0

**`validateDBMetadata`**

The `validateDBMetadata` command checks that the stored 
metadata of a database or a collection is valid within a particular 
API version.

`validateDBMetadata` reports errors, but does not have the
capability to fix errors.

## Compatibility

This command is available in deployments hosted in the following environments: 

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

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     validateDBMetadata: 1,
     apiParameters: {
       version: <string>,
       strict: <boolean>,
       deprecationErrors: <boolean>
      },
     db: <string>,
     collection: <string>,
   } 
)
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - apiParameters 
  - document
  - .. _api-params-document:

    *All Fields are Required*.

    - `version` (*string*)

      The API Version to validate against. For now, `"1"` is the 
      only version.

    - `strict` (*boolean*)

      If `true`, APIStrictError 
      responses will be included in the output.

    - `deprecationErrors` (*boolean*)

      If `true`, APIDeprecationError 
      responses will be included in the output.

* - `db`
  - string
  - *Optional*. The name of the database to validate. If no database
    is specified, all databases will be validated.

* - `collection`
  - string
  - *Optional*. The name of the collection or view to validate. If no 
    collection or view is specified, all collections in the database  
    specified by `db` will be validated. If no database is 
    specified, all collections in all databases will be validated.

## Behavior

- Validate all collections in all databases, reporting 
  APIStrictError 
  and APIVersionError error responses.

  ```javascript
  db.runCommand( { 
    validateDBMetadata: 1, 
    apiParameters: { 
      version: "1", 
      strict: true, 
      deprecationErrors: true 
    }, 
  })
  ```

- Validate all collections in `inventory`: 

  ```javascript
  db.runCommand( { 
    validateDBMetadata: 1, 
    apiParameters: { 
      version: "1", 
      strict: true, 
      deprecationErrors: true 
    }, 
    db: "inventory",
  })
  ```

- Validate the `sales` collection in the `inventory` database:

  ```javascript
  db.runCommand( { 
    validateDBMetadata: 1, 
    apiParameters: { 
      version: "1", 
      strict: true, 
      deprecationErrors: true 
    }, 
    db: "inventory",
    collection: "sales",
  })
  ```

- Validate any and all `sales` collections across all databases:

  ```javascript
  db.runCommand( { 
    validateDBMetadata: 1, 
    apiParameters: { 
      version: "1", 
      strict: true, 
      deprecationErrors: true 
    }, 
    collection: "sales",
  })
  ```

**Note:**

Your user must have the `validate` privilege action on 
all collections you want to validate.

## Output

```javascript
{
   apiVersionErrors: [
     {
       ns: <string>,
       code: <int>,
       codeName: <string>,
       errmsg: <string>
     }
   ],
   ok: <int>,
   hasMoreErrors: <boolean>,
}
```

**`validateDBMetadata.apiVersionErrors`**

Array of documents describing API Version errors.

**`validateDBMetadata.apiVersionErrors[n].ns`**

Namespace of the collection or view with error.

**`validateDBMetadata.apiVersionErrors[n].code`**

Numeric error code.

**`validateDBMetadata.apiVersionErrors[n].codeName`**

Name of the error code.

**`validateDBMetadata.apiVersionErrors[n].errmsg`**

String describing the error.

**`validateDBMetadata.ok`**

If the command fails, `ok` is set to `1`. Otherwise, `ok` is 
set to `0`. `validateDBMetadata.ok` may have a value of 
`0` and still report validation errors.
   

**`validateDBMetadata.hasMoreErrors`**

If `true`, there are additional errors.

## Example

Use the sample Query API code to create a `sales`
collection in `mongosh`: 

```javascript
db.sales.insertMany([
    { "_id" : 1, "item" : "shoes", "price" : 10, "quantity" : 2, "date" : ISODate("2021-01-01T08:00:00Z") },
    { "_id" : 2, "item" : "hat", "price" : 20, "quantity" : 1, "date" : ISODate("2021-02-03T09:00:00Z") },
    { "_id" : 3, "item" : "gloves", "price" : 5, "quantity" : 5, "date" : ISODate("2021-02-03T09:05:00Z") },
    { "_id" : 4, "item" : "pants", "price" : 10, "quantity" : 10, "date" : ISODate("2021-02-15T08:00:00Z") },
    { "_id" : 5, "item" : "socks", "price" : 5, "quantity" : 10, "date" : ISODate("2021-02-15T09:05:00Z") },
    { "_id" : 6, "item" : "shirt", "price" : 5, "quantity" : 5, "date" : ISODate("2021-02-15T12:05:10Z") },
    { "_id" : 7, "item" : "belt", "price" : 5, "quantity" : 10, "date" : ISODate("2021-02-15T14:12:12Z") },
    { "_id" : 8, "item" : "blouse", "price" : 10, "quantity" : 5, "date" : ISODate("2021-03-16T20:20:13Z") }
])
```

  
Add a text index on the `item` field.   

```javascript
db.sales.createIndex( { item: "text" } )
```

Validate the `sales` collection for strict compliance with API 
version 1 and include `deprecationErrors` in the output.

```javascript
db.runCommand( { 
  validateDBMetadata: 1, 
  apiParameters: { 
    version: "1", 
    strict: true, 
    deprecationErrors: true 
  }, 
  collection: "sales",
})
```

`validateDBMetadata` reports an `APIStrictError` on the 
`item_text` index. 

```javascript
{
   apiVersionErrors: [
     {
       ns: 'test.sales',
       code: 323,
       codeName: 'APIStrictError',
       errmsg: 'The index with name item_text is not allowed in API version 1.'
     }
   ],
   ok: 1,
   hasMoreErrors: false,
}
```
