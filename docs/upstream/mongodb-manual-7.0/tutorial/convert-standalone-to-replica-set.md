<!-- Converted from tutorial/convert-standalone-to-replica-set.txt (reStructuredText). Includes are inlined. -->

# Convert a Standalone Self-Managed mongod to a Replica Set

Use a standalone `mongod` instance for testing and
development. A standalone instance isn't a good choice for a production
deployment because it can be a single point of failure. A replica
set provides redundancy and availability. Always use a
replica set in production.

If you have a standalone server with data that you want to use in
production, convert the standalone server to a replica set first.

**Important:**

If you convert a development server to a replica set for production
use, consult the security checklist first.
Do this before you expose your cluster to the Internet.

You can migrate from a standalone server
to a [MongoDB Atlas](https://www.mongodb.com/docs/atlas) cluster.
MongoDB Atlas is the fully managed service for MongoDB deployments in
the cloud. To learn more, see [Migrate or Import Data](https://www.mongodb.com/docs/atlas/import/) in the MongoDB Atlas
documentation.

## About This Task

### Server Architecture

The tutorial uses the following servers:

| Hostname | Port | Description |
|---|---|---|
| `mongodb0.example.net` | `27017` | A running standalone MongoDB Server with data. |
| `mongodb1.example.net` | `27017` | A new MongoDB Server to join the replica set. |
| `mongodb2.example.net` | `27017` | A new MongoDB Server to join the replica set. |

## Before You Begin

### Cluster Type

Before you convert your standalone instance, consider whether a
replica set or a sharded cluster is more appropriate for your workload.

A sharded cluster provides redundancy and availability by
distributing data across shards, which are
usually hosted on multiple servers to allow horizontal scaling.

### Authorization

To use authorization with a replica set, you must also configure
replica set members to use X.509 certificates or keyfiles to
perform internal authentication.

For more information, see:

- x509-internal-authentication
- deploy-repl-set-with-keyfile

## Procedure

**Step 1: Shut down the standalone instance.**

Use `mongosh` to connect to
your existing `mongod` instance:

```shell
mongosh "mongodb://mongodb0.example.net:27017"
```

Switch to the `admin` database and run `shutdown`.

```javascript
use admin
db.adminCommand(
   {
      shutdown: 1,
      comment: "Convert to replica set"
   }
)
```

When you run the `shutdown` command, the server responds with a message
similar to the following example:

`MongoNetworkError: connection <connection number> to <host>:<port> closed`

**Step 2: Configure Replica Set Members**

Update the configuration file on each server to set
the `replSetName` setting.

```yaml
replication:
  replSetName: "rs0"
```

**Step 3: Configure Member Authentication**

Configure member authentication for each server in the replica set.

**convert-config-rs-x509:**

Configure the replica set to use X.509 certificates for internal member
authentication.

| Setting | Option | Description |
|---|---|---|
| `net.tls.mode` | `--tlsMode` | Sets the TLS mode to use in authentication.  To configure the server to require X.509 certificate authentication, set this option to `requireTLS`. |
| `net.tls.certificateKeyFile` | `--tlsCertificateKeyFile` | Sets the path to the `.pem` file that contains the TLS certificate for client connections. |
| `net.tls.CAFile` | `--tlsCAFile` | Sets the path to the file that contains the root certificate chain for the Certificate Authority (CA). |
| `net.tls.clusterFile` | `--tlsClusterFile` | Sets the path to the `.pem` file that contains the TLS certificate for cluster member connections. |
| `security.clusterAuthMode` | `--clusterAuthMode` | Sets the mode used to authenticate cluster members. To use X.509 authentication, set this option to `x509`. |

For example:

```yaml
replication:
  replSetName: "rs0"
security:
  clusterAuthMode: x509
net:
  tls:
    mode: requireTLS
    certificateKeyFile: /etc/mongodb/client.pem
    CAFile: /etc/mongodb/ca.pem
    clusterFile: /etc/mongodb/member.pem
```

**config-rs-keyfile:**

Configure the replica set to use keyfiles for internal member authentication.
To authenticate, each member must have a copy of the same keyfile.

| Setting | Option | Description |
|---|---|---|
| `security.keyFile` | `--keyFile` | Sets the path to the replica set keyfile. |

For example:

```yaml
replication:
   replSetName: "rs0"
security:
    keyFile: /etc/mongodb/keyfile
```

**config-rs-noauth:**

Configures a replica set without authorization.

**Warning:**

You should only use this configuration for internal replica sets that
are **not** accessible through the network.

| Setting | Option | Description |
|---|---|---|
| `net.bindIp` | `--bind_ip` | Sets the hostnames or IP addresses that MongoDB listens on for client connections. To block network access to the server, set this option to `localhost`. |

For example:

```yaml
replication:
  replSetName: "rs0"
net:
   bindIp: localhost
```

**Step 4: Start MongoDB**

Start `mongod` for each member.

**Step 5: Initialize the replica set.**

To initialize the replica set, use `mongosh` to reconnect to
your server instance.

```shell
mongosh "mongodb://mongodb0.example.net:27017"
```

Then, run the `rs.initiate` method:

```javascript
rs.initiate()
```

You only have to initiate the replica set once.

To view the replica set configuration, use `rs.conf()`.

To check the status of the replica set, use `rs.status()`.

**Step 6: Add nodes to the replica set.**

The new replica set has a single, primary node. Review the
documentation on clusters before you add additional nodes:

- Replica set architectures
- Adding members to a replica set

To add nodes, run the `rs.add` method:

```javascript
rs.add("mongodb1.example.net:27017")
rs.add("mongodb2.example.net:27017")
```

**Step 7: Check replication status.**

To check that the replica set is correctly configured, run
the `rs.status` method and check that the new
members are listed in the `members`
field:

```javascript
rs.status()
```

**Step 8: Update Your Application Connection String.**

After you convert the standalone server to a replica set,
update the connection string used by
your applications to the connection string for your
replica set:

- `mongodb0.example.net:27017`
- `mongodb1.example.net:27017`
- `mongodb2.example.net:27017`

```none
mongodb://mongodb0.example.net:27017,mongodb1.example.net:27017,mongodb2.example.net:27017
```

Then, restart your applications.

## Learn More

- Configuration options
- Deploy a standalone instance
- Deploy a new replica set
