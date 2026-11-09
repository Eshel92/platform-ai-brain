<!-- Converted from reference/cluster-parameters.txt (reStructuredText). Includes are inlined. -->

# Cluster Parameters for a Self-Managed Deployment

## Synopsis

You can specify configuration options which affect all nodes in a 
replica set or sharded cluster. To set these options, use the 
`setClusterParameter` command:

```javascript
db.adminCommand( { setClusterParameter:{ <parameter>: <value> } } )
```

To view the current values of cluster parameters, use the 
`getClusterParameter` command: 

```javascript
db.adminCommand( { getClusterParameter: <parameter> } )
```

The `setClusterParameter` command is only available in self-managed
installations. The `setClusterParameter` command is not available in
MongoDB Atlas.

## Parameters

**`changeStreamOptions`**

**New in version:** 6.0

Available for both `mongod` and `mongos`.

This is an object containing change stream 
configuration options. 

You can only set `changeStreamOptions` on mongos or a 
replica set primary. The value is set cluster-wide.

**`changeStreamOptions.preAndPostImages.expireAfterSeconds`**

**New in version:** 6.0

*Default*: off

Controls the retention policy of change stream pre- and post-images.
Pre- and post-images are the versions of a document before and after 
document modification respectively. `expireAfterSeconds` 
controls how long pre- and post-images are retained. 

When `expireAfterSeconds` is `off`, MongoDB uses the default retention 
policy: pre- and post-images are retained until the corresponding change 
stream events are removed from the oplog.  

To specify the minimum pre- and post-image retention time:

- Set `expireAfterSeconds` using an integer. 

- If a change stream event is removed from the oplog, then the 
  corresponding pre- and post-images are also deleted regardless of the 
  `expireAfterSeconds` pre- and post-image retention time.

The following example sets the retention time for pre- and post-images in 
change streams to `100 seconds`:

```javascript
db.runCommand( {
   setClusterParameter: {
   changeStreamOptions: { preAndPostImages: { expireAfterSeconds: 100 } }
   }
} )
```
