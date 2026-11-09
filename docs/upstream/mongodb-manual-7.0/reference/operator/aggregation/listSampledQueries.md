<!-- Converted from reference/operator/aggregation/listSampledQueries.txt (reStructuredText). Includes are inlined. -->

# $listSampledQueries (aggregation stage)

## Definition

**`$listSampledQueries`**

Returns sampled queries for all collections or a specific 
collection. Sampled queries are used by the
`analyzeShardKey` command to calculate metrics about the read and 
write distribution of a shard key.

## Syntax

`$listSampledQueries` has this syntax:

```javascript
{  
   $listSampledQueries: { namespace: <namespace> } 
}
```

## Behavior

- To list sampled queries for a single collection, specify
  the collection in the `namespace` argument.

- To list sampled queries for all collections, omit the `namespace`
  argument.

## Access Control

`$listSampledQueries` requires the `clusterMonitor` role 
on the cluster. 

## Limitations

- You cannot use `$listSampledQueries` on Atlas
  multi-tenant
  configurations.
- You cannot use `$listSampledQueries` on standalone deployments.
- You cannot use `$listSampledQueries` directly against a
  `--shardsvr` replica set.
  When running on a sharded cluster, `$listSampledQueries`
  must run against a `mongos`.

## Examples

**shell:**

### List Sampled Queries for All Collections

The following aggregation operation lists all sampled queries for all
collections in the replica set:

```javascript
db.aggregate( [  { $listSampledQueries: {  } } ] )
```

### List Sampled Queries for A Specific Collection

The following aggregation operation lists all sampled queries for a 
`post` collection in the `social` database:

```javascript
db.aggregate( [  { $listSampledQueries: { namespace: "social.post" } } ] )
```

**nodejs:**

To use the MongoDB Node.js driver to add a `$listSampledQueries` stage to
an aggregation pipeline, use the `$listSampledQueries` operator in a
pipeline object.

### List Sampled Queries for All Collections

The following aggregation operation lists all sampled queries for all
collections in the replica set:

```javascript
const pipeline = [{ $listSampledQueries: {} }];

const cursor = db.aggregate(pipeline);
return cursor;
```

### List Sampled Queries for A Specific Collection

The following aggregation operation lists all sampled queries for the
`movies` collection in the `sample_mflix` database:

```javascript
const pipeline = [{ $listSampledQueries: { namespace: "sample_mflix.movies" } }];

const cursor = db.aggregate(pipeline);
return cursor;
```

## Output

The output fields differ for read and write queries.

### Read Queries

```none
{
   _id: <uuid>,  
   ns: "<database>.<collection>",
   collectionUuid: <collUUID>,
   cmdName: <find|aggregate|count|distinct>,
   cmd: {
     filter: <object>,
     collation: <object>,
     let: <object>
   },
   expireAt: <date>
}
```

* - Field Name
  - Type
  - Description

* - `_id`
  - UUID
  - Sample ID for the query.

* - `ns`
  - string
  - Namespace of the sampled collection.

* - `collectionUuid`
  - UUID
  - ID of the sampled collection.

* - `cmdName`
  - string
  - Name of the sampled command. Can be one of:

    - `"find"`
    - `"aggregate"`
    - `"count"`
    - `"distinct"`

* - `cmd.filter`
  - object
  - Filter the command ran with, if applicable.

* - `cmd.collation`
  - object
  - Collation the command ran with, if applicable.

* - `cmd.let`
  - object
  - Custom variables the command ran with, if applicable.

* - `expireAt`
  - date
  - Date that the sample expires.

### Write Queries

```none
{
   _id: <uuid>,
   ns: "<database>.<collection>",
   collectionUuid: <collUUID>,
   cmdName: <update|delete|findAndModify>,
   cmd: <object>,
   expireAt: <date>
}
```

* - Field Name
  - Type
  - Description

* - `_id`
  - UUID
  - Sample ID for the query.

* - `ns`
  - string
  - Namespace of the sampled collection.

* - `collectionUuid`
  - UUID
  - ID of the sampled collection.

* - `cmdName`
  - string
  - Name of the sampled command. Can be one of:

    - `"update"`
    - `"delete"`
    - `"findAndModify"`

* - `cmd`
  - object
  - Command object

* - `expireAt`
  - date
  - Date that the sample expires.
