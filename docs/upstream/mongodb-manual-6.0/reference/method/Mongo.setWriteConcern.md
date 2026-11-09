<!-- Converted from reference/method/Mongo.setWriteConcern.txt (reStructuredText). Includes are inlined. -->

# Mongo.setWriteConcern()

## Definition

**`Mongo.setWriteConcern()`**

Sets the write concern for the `Mongo()` connection object.

See the write-concern for an introduction to write concerns
in MongoDB.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command takes the following form:

```javascript
db.getMongo().setWriteConcern( { w: <value>, j: <boolean>, wtimeout: <number> } )
```

The fields are: 

* - Field
  - Description

* - `w`
  - The number of `mongod` or `mongod`
    instances that must acknowledge a write. Possible values are:

    - "majority". A majority of the target instances must
      acknowledge the write.
    - <number>. The specified number of target instances must
      acknowledge the write.
    - <custom write concern name>. A user defined write concern, the
      tagged instances must acknowledge the write.

    See write concern specification for details.

* -  `j`
  - A boolean value. `j: true` requests acknowledgment that the
    write operation has been written to the on-disk journal.

* - `wtimeout`
  - The number of milliseconds to wait for acknowledgment of the
    write concern. `wtimeout` is only applicable when `w` has a
    value greater than `1`.

## Example

In the following example:

- Two `mongod` or `mongod` instances must
  acknowledge writes.
- There is a `1` second timeout to wait for write acknowledgments.

```javascript
db.getMongo().setWriteConcern( { w: 2, wtimeout: 1000 } )
```

**See also:**

- `getWriteConcern()`
