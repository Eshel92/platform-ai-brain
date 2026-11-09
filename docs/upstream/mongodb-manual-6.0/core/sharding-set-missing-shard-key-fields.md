<!-- Converted from core/sharding-set-missing-shard-key-fields.txt (reStructuredText). Includes are inlined. -->

# Set Missing Shard Key Fields

If you have missing shard key fields, you can set the shard key field to
`null`. If you want to set the missing shard key field to a
non-`null` value, see update-shard-key.

To perform the update, you can use the following operations on a
`mongos`:

* - Command
  - Method
  - Description

* - | update with
    | `multi: true`

  - | db.collection.updateMany()

  - - Can be used to set the missing key value to `null` only.

    - Can be performed inside or outside a transaction.

    - Can be performed as a retryable write or not.

    - For additional requirements, refer to the specific
      command/method.

* - | update  with
    | `multi: false`

  - | db.collection.replaceOne()
    | db.collection.updateOne()

  - - Can be used to set the missing key value to `null` or any
      other value.

    - The update to set missing shard key fields **must** meet one of
      the following requirements:

      - the filter of the query contains an equality condition on the full
        shard key in the query
      - the filter of the query contains an exact match on _id
      - the update targets a single shard

    - To set to a non-`null` value, refer to
      update-shard-key.

    - For additional requirements, refer to the specific
      command/method.

* - findAndModify
  - | db.collection.findOneAndReplace()
    | db.collection.findOneAndUpdate()
    | db.collection.findAndModify()

  - - Can be used to set the missing key value to `null` or any
      other value.

    - When setting missing shard key fields with a method that
      explicitly updates only one document, the update **must** meet
      one of the following requirements:

      - the filter of the query contains an equality condition on
        the full shard key in the query
      - the filter of the query contains an exact match on _id
      - the update targets a single shard

    - Missing key values are returned when matching on `null`. To
      avoid updating a key value that is `null`, include additional
      query conditions as appropriate.

    - To set to a non-`null` value, refer to
      update-shard-key.

    - For additional requirements, refer to the specific
      command/method.

* -
  - | `db.collection.bulkWrite()`
    | `Bulk.find.replaceOne()`
    | `Bulk.find.updateOne()`
    | `Bulk.find.update()`

  - - To set to a `null` value,  you can specify multiple shard
      key modifications in the bulk operation.

    - When setting missing shard key fields with a method that
      explicitly updates only one document, the update **must** meet
      one of the following requirements:

      - the filter of the query contains an equality condition on
        the full shard key in the query
      - the filter of the query contains an exact match on _id
      - the update targets a single shard

    - To set to a non-`null` value, refer to
      update-shard-key.

    - For additional requirements, refer to the underlying
      command/method.

## Example

Consider a `sales` collection which is sharded on the `location`
field. Some documents in the collection have no `location` field. A
missing field is considered the same as a null value for the field. To
explicitly set these fields to `null`, run the following command:

```javascript
db.sales.updateOne(
  { _id: 12345, location: null },
  { $set: { location: null } }
)
```

When setting missing shard key fields with
`db.collection.updateOne()` or another method that explicitly
updates only one document, the update **must** meet one of the following
requirements:

- the filter of the query contains an equality condition on the full
  shard key in the query
- the filter of the query contains an exact match on _id
- the update targets a single Shard
