<!-- Converted from tutorial/modify-chunk-size-in-sharded-cluster.txt (reStructuredText). Includes are inlined. -->

# Modify Range Size in a Sharded Cluster

The default range size for a sharded cluster is 128 megabytes. This
default range size works well for most deployments; however, if you
notice that automatic migrations use more I/O than your hardware can
handle, you may want to reduce the range size. A small range size leads 
to more rapid and frequent migrations. The allowed size is between 1 and 
1024 megabytes, inclusive.

To modify the range size, use the following procedure:

#. Connect to any `mongos` in the cluster using
   `mongosh`.

#. Issue the following command to switch to the config-database:

   ```javascript
   use config
   ```

#. Issue the following command to store the global range size
   configuration value:

   ```javascript
   db.settings.updateOne(
      { _id: "chunksize" },
      { $set: { _id: "chunksize", value: <sizeInMB> } },  
      { upsert: true }
   )
   ```

Modifying the chunk size has several limitations:

- .. include:: /includes/autosplit-no-operation.rst

  Starting in MongoDB 6.0, the following auto-splitting commands do not
  perform an operation:

  - `sh.enableAutoSplit()`
  - `sh.disableAutoSplit()`

- In MongoDB versions earlier than 6.0, automatic splitting only occurs
  for insert or update operations.

- If you lower the chunk size, it may take time for all chunks to split to
  the new size.

- Splits cannot be undone.

- If you increase the chunk size, existing chunks grow only through
  insertion or updates until they reach the new size.

- The allowed range of the chunk size is between 1 and 1024 megabytes,
  inclusive.
