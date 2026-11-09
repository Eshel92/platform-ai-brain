<!-- Converted from reference/method/Mongo.setReadPref.txt (reStructuredText). Includes are inlined. -->

# Mongo.setReadPref() (mongosh method)

## Definition

**`Mongo.setReadPref(mode, tagSet, hedgeOptions)`**

Call the `setReadPref()` method on a `Mongo` connection object to control how the client will
route all queries to members of the replica set. [#specificqueries]_

**Note:**

You must call `Mongo.setReadPref()` on the connection object
before retrieving documents using that connection to use that read
preference.

   

### Parameters

| Parameter | Type | Description |
|---|---|---|
| mode | string | .. _mongo-setReadPref-mode: One of the following read preference modes: `primary`, `primaryPreferred`, `secondary`, `secondaryPreferred`, or `nearest` |
| tagSet | array of documents | .. _mongo-readpref-tagset: Optional. A tag set used to target reads to members with the specified tag(s). `tagSet` is not available if using read preference mode `primary`. For details, see replica-set-read-preference-tag-sets. |
| hedgeOptions | document | .. _mongo-readpref-hedge: Optional. A document that specifies whether to enable the use of hedged reads: `{ enabled: <boolean> }` The `enabled` field defaults to true; i.e. specifying an empty document `{ }` is equivalent to specifying `{ enabled: true }`. Hedged reads are available for sharded clusters. To use hedged reads, the `mongos` must have `enabled support` for hedged reads (the default) and the non-`primary` read preferences must enable the use of hedged reads. Read preference `nearest` enables the use of hedged reads on sharded clusters by default; i.e. by default, has `{ enabled: true }`. |

`Mongo.setReadPref()` does not support the
replica-set-read-preference-max-staleness option for read
preference.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

`Mongo.setReadPref()` has the following behavior.

### Interaction with db.runCommand()

Starting in mongosh 2.0, `db.runCommand()` ignores any global
read preferences added through the connection string or by using the 
`Mongo.setReadPref()` method. To specify the desired read preference, 
use the `options` argument when calling `db.runCommand()`.
      

## Examples

### Specify Read Preference Mode

The following operation sets the read preference mode to target the read to a secondary member.
This implicitly allows reads from secondaries.

```javascript
db.getMongo().setReadPref('secondary')
```

However, if called while connected to the primary using `mongosh`, the 
above command does not route queries to a secondary. 

### Specify Read Preference Tag Set

To target secondaries with specific tags, include both the mode and the tagSet
array:

```javascript
db.getMongo().setReadPref(
   "secondary",
   [
      { "datacenter": "B" },    // First, try matching by the datacenter tag
      { "region": "West"},      // If not found, then try matching by the region tag
      { }                       // If not found, then use the empty document to match all eligible members
   ]
)
```

During the secondary selection process, MongoDB tries to find secondary
members with the `datacenter: "B"` tag first.

- If found, MongoDB limits the eligible secondaries to those with the
  `datacenter: "B"` tag and ignores the remaining tags. 
  
- If none are found, then, MongoDB tries to find secondary members with
  the `"region": "West"` tag. 

  - If found, MongoDB limits the eligible secondaries to those with the
    `"region": "West"` tag.

  - If none are found, MongoDB uses any eligible secondaries.

See read-pref-order-matching for details.

**See also:**

/tutorial/configure-replica-set-tag-sets

### Specify Hedged Read

For sharded clusters, you can enable hedged reads 
for non-primary read preferences. To use hedged 
reads, the `mongos` must have `enabled support` for hedged reads (the default) and the
non-`primary` read preferences must
enable the use of hedged reads.

To target secondaries on sharded clusters using hedged reads,
include both the mode and the
hedgeOptions, as in the following
examples:

- Without a tag set

  ```javascript
  db.getMongo().setReadPref(
     "secondary",            // mode
     null,                   // tag set
     { enabled: true }       // hedge options
  )
  ```

- With a tag set

  ```javascript
  db.getMongo().setReadPref(
     "secondary",                      // mode
     [ { "datacenter": "B" },  { } ],  // tag set
     { enabled: true }                 // hedge options
  )
  ```
