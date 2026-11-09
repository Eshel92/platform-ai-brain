<!-- Converted from reference/command/setAllowMigrations.txt (reStructuredText). Includes are inlined. -->

# setAllowMigrations

## Definition

**`setAllowMigrations`**

Prevents the start of new automatic migrations on a collection, prevents 
in-flight range migrations 
(started manually or by the balancer) from committing, 
and excludes the collection from new balancer rounds.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in serverless instances.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   {
    setAllowMigrations: "<db>.<collection>", 
    allowMigrations: <true|false>
   } 
)
```

## Command Fields

The command takes the following parameters:

* - Field
  - Type
  - Description

* - setAllowMigrations
  - `string`
  - .. _setAllowMigrations-cmd-coll:

    The collection to modify.

* - allowMigrations
  - `boolean`
  - .. _setAllowMigrations-cmd-flag:

    If `false`:

    - MongoDB prevents new automatic migrations on the collection
    - in-flight range migrations will not be committed
    - the collection will be excluded from new balancer rounds

    If `true`: 

    - MongoDB allows new automatic migrations on the collection
    - in-flight range migrations will be committed
    - the collection will be included in new balancer rounds
 

## Behavior

`setAllowMigrations` requires the same privileges as 
`moveChunk`.

## Example

This operation prevents migrations on the `store.inventory`
collection:

```javascript
db.adminCommand( {
   setAllowMigrations: "store.inventory",
   allowMigrations: false
} )
```
