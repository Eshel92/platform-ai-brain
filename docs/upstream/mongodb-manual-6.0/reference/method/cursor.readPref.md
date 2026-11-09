<!-- Converted from reference/method/cursor.readPref.txt (reStructuredText). Includes are inlined. -->

# cursor.readPref()

## Definition

**`cursor.readPref(mode, tagSet, hedgeOptions)`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Append `readPref()` to a cursor to
control how the client routes the query to members
of the replica set.

**Note:**

You must apply `readPref()` to the cursor before retrieving
any documents from the database.

### Parameters

| Parameter | Type | Description |
|---|---|---|
| mode | string | .. _cursor-readpref-mode: One of the following read preference modes: `primary`, `primaryPreferred`, `secondary`, `secondaryPreferred`, or `nearest` |
| tagSet | array of documents | .. _cursor-readpref-tagset: Optional. A tag set used to target reads to members with the specified tag(s). `tagSet` is not available if using `primary`. For details, see replica-set-read-preference-tag-sets. |
| hedgeOptions | document | .. _cursor-readpref-hedge: Optional. A document that specifies whether to enable the use of hedged reads. `{ enabled: <boolean> }` The `enabled` field defaults to true; i.e. specifying an empty document `{ }` is equivalent to specifying `{ enabled: true }`. Hedged reads are available for sharded clusters. To use hedged reads, the `mongos` must have `enabled support` for hedged reads (the default) and the non-`primary` read preferences must enable the use of hedged reads. Read preference `nearest` enables the use of hedged reads on sharded clusters by default; i.e. by default, has `{ enabled: true }`. |

`readPref()` does not support the
replica-set-read-preference-max-staleness option for read
preference.

## Compatibility

This method is available in deployments hosted in the following environments: 

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

## Examples

### Specify Read Preference Mode

The following operation uses the read preference mode to target the read to a secondary member.

```javascript
db.collection.find({ }).readPref( "secondary")
```

### Specify Read Preference Tag Set

To target secondaries with specific tags, include both the mode and the tagSet
array:

```javascript
db.collection.find({ }).readPref( 
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
  db.collection.find({ }).readPref( 
     "secondary",            // mode
     null,                   // tag set
     { enabled: true }       // hedge options
  )
  ```

- With a tag set

  ```javascript
  db.collection.find({ }).readPref( 
     "secondary",                      // mode
     [ { "datacenter": "B" },  { } ],  // tag set
     { enabled: true }                 // hedge options
  )
  ```
