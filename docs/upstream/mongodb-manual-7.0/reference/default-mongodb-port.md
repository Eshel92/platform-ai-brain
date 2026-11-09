<!-- Converted from reference/default-mongodb-port.txt (reStructuredText). Includes are inlined. -->

# Default MongoDB Port

The following table lists the default TCP ports used by MongoDB:

| Default Port | Description |
|---|---|
| `27017` | Default port for `mongod` and `mongos`. Change this port with `port` or `--port`. |
| `27018` | Default port for `mongod` when using the `--shardsvr` command-line option or `clusterRole` set to `shardsvr` in a configuration file. |
| `27019` | Default port for `mongod` when using the `--configsvr` command-line option or `clusterRole` set to `configsvr` in a configuration file. |
| `27020` | Default port on which `mongocryptd` listens for messages. [MongoDB Enterprise Server](https://www.mongodb.com/download-center/enterprise) includes `mongocryptd`, which supports automatic encryption operations. |
