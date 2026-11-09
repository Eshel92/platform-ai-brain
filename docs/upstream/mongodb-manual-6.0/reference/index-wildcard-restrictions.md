<!-- Converted from reference/index-wildcard-restrictions.txt (reStructuredText). Includes are inlined. -->

# Wildcard Index Restrictions

## Incompatible Index Types or Properties

Wildcard indexes do not support the following index types or
properties:

- Compound
- TTL
- Text
- 2d (Geospatial)
- 2dsphere (Geospatial)
- Hashed
- Unique

**Note:**

Wildcard Indexes are distinct from and incompatible with
text-index-wildcard. Wildcard indexes cannot support
queries using the `$text` operator. 

## Unsupported Query and Aggregation Patterns

Field does **not** exist
  Wildcard indexes are sparse and do
  not index empty fields. Wildcard indexes therefore cannot support 
  querying for documents where a field does **not** exist.

  For example, consider a collection `inventory` with a wildcard
  index on `product_attributes`. The wildcard index
  **cannot** support the following queries:

  ```javascript
  db.inventory.find( {"product_attributes" : { $exists : false } } )

  db.inventory.aggregate([
    { $match : { "product_attributes" : { $exists : false } } }
  ])
  ```

Field is equal to a document or an array
  Wildcard indexes generate entries for the **contents** of a
  document or array, and not the document/array itself. Wildcard 
  indexes therefore cannot support exact document/array equality 
  matches. Wildcard indexes *can* support querying where 
  the field equals an empty document `{}`.

  For example, consider a collection `inventory` with a wildcard
  index on `product_attributes`. The wildcard index
  **cannot** support the following queries:

  ```javascript
  db.inventory.find({ "product_attributes" : { "price" : 29.99 } } )
  db.inventory.find({ "product_attributes.tags" : [ "waterproof", "fireproof" ] } )

  db.inventory.aggregate([{ 
    $match : { "product_attributes" : { "price" : 29.99 } }
  }])

  db.inventory.aggregate([{ 
    $match : { "product_attributes.tags" : ["waterproof", "fireproof" ] } }
  }])
  ```

Field is not equal to a document or array
  Wildcard indexes generate entries for the **contents** of a
  document or array, and not the document/array itself. Wildcard 
  indexes therefore cannot support exact document/array inequality
  matches.

  For example, consider a collection `inventory` with a wildcard
  index on `product_attributes`. The wildcard index
  **cannot** support the following queries:

  ```javascript
  db.inventory.find( { $ne : [ "product_attributes", { "price" : 29.99 } ] } )
  db.inventory.find( { $ne : [ "product_attributes.tags",  [ "waterproof", "fireproof" ] ] } )

  db.inventory.aggregate([{ 
    $match : { $ne : [ "product_attributes", { "price" : 29.99 } ] }
  }])

  db.inventory.aggregate([{ 
    $match : { $ne : [ "product_attributes.tags", [ "waterproof", "fireproof" ] ] }
  }])
  ```

Array Field is equal or not equal to null
  If a given field is an array in any document in the collection,
  wildcard indexes cannot support queries for documents where that
  field is equal or not equal to null.

  For example, consider a collection `inventory` with a wildcard
  index on `product_attributes`. The wildcard index
  **cannot** support the following queries if 
  `product_attributes.tags` is an array in any document in the
  collection:

  ```javascript
  db.inventory.find( { "product_attributes.tags": { $ne: null } } )

  db.inventory.find( { "product_attributes.tags": null } )

  db.inventory.aggregate([{ 
    $match : { "product_attributes.tags": { $ne: null } }
  }])

  db.inventory.aggregate([{ 
    $match : { "product_attributes.tags": null }
  }])
  ```

Field is equal to null
  Wildcard indexes cannot support queries for documents where a field
  is equal to null. The query `{ $eq: null }` matches all
  documents where the field is null or missing. Wildcard are
  sparse, meaning they do not index the
  documents where the indexed field is missing, and therefore cannot
  support a match on null.

  For example, consider a collection `inventory` with a wildcard index
  on `product_attributes`. The wildcard index cannot support the
  following queries:

  ```javascript
  db.inventory.find( { "product_attributes.price": { $eq: null } } )

  db.inventory.aggregate([{
     $match : { "product_attributes.price": { $eq: null } }
  }])
  ```

## Sharding

You cannot shard a collection using a wildcard index. Create a
non-wildcard index on the field or fields you want to shard on.
For more information on shard key selection, see
sharding-shard-key.
