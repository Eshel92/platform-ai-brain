<!-- Converted from reference/default-mongodb-port.txt (reStructuredText). Includes are inlined. -->

# Default MongoDB Port

The following table lists the default TCP ports used by MongoDB:

| Default Port | Description |
|---|---|
| `27017` | The default port for `mongod` and `mongos` instances. You can change this port with `port` or `--port`. |
| `27018` | The default port for `mongod` when running with `--shardsvr` command-line option or the `shardsvr` value for the `clusterRole` setting in a configuration file. |
| `27019` | The default port for `mongod` when running with `--configsvr` command-line option or the `configsvr` value for the `clusterRole` setting in a configuration file. |
| `27020` | The default port from which `mongocryptd` listens for messages. `mongocryptd` is installed with [MongoDB Enterprise Server](https://www.mongodb.com/download-center/enterprise) and supports automatic encryption operations. |
