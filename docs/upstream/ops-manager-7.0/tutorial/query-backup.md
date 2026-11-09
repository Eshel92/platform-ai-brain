<!-- Converted from tutorial/query-backup.txt (reStructuredText). Includes are inlined. -->

# Query a Backup Snapshot

Ops Manager provides `queryable backups`. This
functionality allows you to more quickly query specific backup
snapsnots. You can use the queryable backups to:

- Restore a subset of data within the MongoDB deployment.

- Compare previous versions of data against the current data.

- Identify the best point in time to restore a system by comparing data
  from multiple snapshots.

## Considerations

### Read-Only Instance

Ops Manager provisions these queryable snapshots as *read-only* MongoDB
instances. Specifically, Ops Manager spins up a mongod with
data from the selected snapshot store.

**Important:**

By default, these instances are available for up to 24 hours. You
can configure the duration using
`Expiration (Hours)`.
For other queryable backup settings, see
queryable-snapshot-settings.

### Query Restrictions on the Queryable Snapshots

You cannot perform the following operations on queryable snapshots:

- Map-reduce operations.

- Queries that require disk usage, such as
  running aggregation
  with the `allowDiskUse` option to perform large sort
  operations.

### Cannot Query Namespace Filtered Snapshots

If you applied namespace filters to a
snapshot, you can't query that snapshot.

If snapshots are compressed in a
`file system store`,
the snapshot contents cannot be queried.

If you want to be able to query snapshots on a
`file system store`, you need to
create a new file system store with
compression disabled.

### Connection Methods

Connections to these instances are over TLS (Transport Layer Security)/SSL (Secure Sockets Layer)  and require
x.509 authentication.  Ops Manager provides:

- An executable that creates a tunnel which
  handles the connection, including the client TLS (Transport Layer Security)/SSL (Secure Sockets Layer) and the x.509
  authentication.

  Requests are routed through the tunnel. The tunnel ensures that
  the request is speaking to the correct mongod instance.

- x.509 certificates if you want to handle the connection details
  manually, including the TLS (Transport Layer Security)/SSL (Secure Sockets Layer) and the x.509 authentication.

  Requests come in through the web server, which acts as a proxy to
  the mongod.

### Multi-Region Backups

If you enabled multi-region backups,
queryable backup is disabled at the cluster-level to prevent
cross-regional data transfer. You can associate cluster members, such as
shards and config server, to different deployment regions. This enables
Ops Manager to route all cluster-level queries through the config server's
`bqProxyEndpoint`. To enable queryable backups at the cluster-level,
set `mms.backup.enableClusterLevelMultiRegionQueryable` to `true` in
the `/opt/mongodb/mms/conf/conf-mms.properties` file. By default, the
value for this app setting is `false`.  

**Note:**

Querying a shard or config server directly doesn't cause any data
transfer across regions. 

### Restore from Regional Backup

If you enable Regional Backup for your
sharded cluster, you must initiate queryable restore jobs on a
shard-by-shard basis to ensure regional data isolation. Because
deployment regions bind to
individual shards rather than to sharded clusters, when you initiate a
restore job at the sharded cluster level, Ops Manager can't guarantee
data isolation.

## Prerequisites

**Important:**

Use the latest versions of `MongoDB Database Tools`,
which include `mongodump` and `mongorestore`.
Use  the latest version of `mongosh`.

Older versions of `mongodump` include an issue
that can cause keys in collection options to be dumped in the wrong order.
To learn more, see [TOOLS-3411](https://jira.mongodb.org/browse/TOOLS-3411).

### Encrypted Snapshot Support for Local Mode

You can query encrypted snapshot using Ops Manager
local mode if you
run MongoDB Enterprise 4.2.9 or later.

### MongoDB Version Compatibility between Snapshot and Target Database

You can query snapshots made from replica sets
or sharded clusters with CSRS (Config Servers as Replica Sets) running
MongoDB 3.2 or later.

For a queryable backup to succeed, the MongoDB instance that is the
target of a restore must run a compatible MongoDB version.
The following table lists the compatibility requirements for each
deployment type and MongoDB version.

#### Sharded Clusters

| Snapshot Data MongoDB Version | Compatible MongoDB Version for Target Database | Platform |
|---|---|---|
| 7.0.x | 7.0.0 Enterprise or later | Any |
| 6.0.x | 6.0.0 Enterprise or later | Any |
| 5.0.x | 5.0.0 Enterprise or later | Any |
| 4.4.x | 4.4.0 Enterprise or later | Any |

#### Replica Sets

| Snapshot Data MongoDB Version | Compatible MongoDB Version for Target Database | Platform |
|---|---|---|
| 7.0.x | 7.0.0 Enterprise or later | Any |
| 6.0.x | 6.0.0 Enterprise or later | Any |
| 5.0.x | 5.0.0 Enterprise or later | Any |
| 4.4.x | 4.4.0 Enterprise or later | Any |

### Authentication and Authorization

**Important:**

A full description of
Transport Layer Security,
public key infrastructure,
X.509 certificates, and
Certificate Authorities
exceeds the scope of this tutorial. This tutorial assumes prior
knowledge of TLS (Transport Layer Security) and access to valid X.509 certificates.

Ops Manager needs a separate PEM (Privacy-Enhanced Mail) file to authenticate and authorize
use of Queryable Backup. This PEM (Privacy-Enhanced Mail) file:

- Must belong to the same platform user and group that owns the
  Ops Manager process. On Linux, the `mongodb-mms:mongodb-mms` user
  and group owns this PEM file.

- Must be readable by the platform user only.

- Must be saved in the same location on every Ops Manager host if your
  deployment uses high availability.

- Must be different than the one used for HTTPS (Hypertext Transfer Protocol Secure) connections to
  Ops Manager (`HTTPS PEM Key File`).

- Should use a key length greater than 512-bit. Using a 2048-bit RSA
  key is recommended.

- Should use a message digest stronger than `sha1`, such as
  `sha256`.

At minimum, the PEM (Privacy-Enhanced Mail) file consists of:

- A server certificate / key pair and
- A Certificate Authority certificate

These pairs are merged to create a PEM (Privacy-Enhanced Mail) file that Queryable Backup
can use. The pairs have the following requirements:

#### Certificate Authority Certificate

The Certificate Authority must sign any other certs and keys to be used in the
PEM file. The Certificate Authority can be one of the following:

- A private Certificate Authority (self signed; recommended for test purposes).

- An intermediate Certificate Authority certificate from a
  certificate provider.

- A Certificate Authority that your company security team issued.

#### Server Certificate / Key Pair

The Certificate Authority that you selected must sign this server certificate.

The Common Name setting of the server certificate/key pair depends
on how many hosts your Ops Manager deployment uses:

- For a single Ops Manager host, the Subject Alternative Name (SAN (Subject Alternative Name))
  in the pair must match the FQDN (fully qualified domain name) of the Ops Manager host.

- For high availability, the SAN (Subject Alternative Name) in the pair must match the 
  FQDN (fully qualified domain name) of the load balancer URL (Uniform Resource Locator).

Concatenate the server certificate / key pair and the certificate
chain to create the Proxy Server PEM Key.

#### PEM File Location

For the queryable backup host, you must specify the location of the
PEM file (which contains both a public key certificate and its
associated private key) using the `Proxy Server PEM File`
setting. If you have not already set up the queryable backup
settings:

#. Click on Admin on the upper-right hand corner. From
   the Admin screen, click on General
   arrow-right Ops Manager Config
   arrow-right Backup.

#. Scroll to the Queryable Snapshot Configuration and
   specify the `Proxy Server PEM File` that the tunnel or
   clients can use to connect to the queryable mongod
   instance.

   If the file is encrypted, specify the
   `Proxy Server PEM File Password`.

#. *Optional.* Update other queryable snapshot settings as
   appropriate. For description of the settings, see
   queryable-snapshot-settings.

   **Note:**

   You must restart the Web Server if you change any of the
   following settings:

   - `Proxy Server Port`

   - `Proxy Server PEM File`

   - `Proxy Server PEM File Password`

### Open Ports for App Server

The app server requires that ports 27700-27719 be open for
communication with queryable backup snapshots.

If you use a load balancer, it must pass the TCP (Transmission Control Protocol) connection
through the value in the `Proxy Server Port`.

To learn more about port requirements, see
Firewall Configuration.

### Sufficient Workers for the Ops Manager Backup Daemon

To query a snapshot of a sharded cluster, the
`Backup Daemon` requires at least one worker for the
config server, one
worker for each shard, and one worker for the
`mongos` instance.

To query a snapshot of a replica set, the Backup Daemon
requires at least one worker for the replica set.

For example, if you restore a queryable backup from a 3-shard cluster with 1 shard router 
(mongos), you need 
this value to be at least `5`:

- 1 per shard (`3`) +
- 1 for the config server (`1`) +
- 1 for the `mongos`

When the queryable backup begins, the Backup Daemon spins
up 5 or more workers to manage these components.

### Hostname

The FQDN (fully qualified domain name) that hosts the `mongod` for the queryable
backup must match the one found the Daemons page. To
find that hostname, click the Admin link, then click
Backup, and then click Daemons.

### Queryable Backup Requires Enterprise Downloads

If Ops Manager can connect to the internet, set
Backup Versions Auto Download Enterprise Builds to
**TRUE**. Queryable Backups require MongoDB Enterprise.

## Query Backup (Use Tunnel to Connect)

**Note:**

The tunnel handles the security (TLS (Transport Layer Security)/SSL (Secure Sockets Layer) and x.509 authentication)
for connecting to the instance.

**Step 1: Go to Backup view and click the Overview tab.**

For the deployment whose backup you want to query, click the ellipsis
button under Options column and select Query.

You can also click the deployment to view its snapshots and click the
Query button under the Actions column.

**Step 2: Follow the prompts to query a backup snapshot.**

#. Select the snapshot to query and click Next.

#. Start the process to query a snapshot. You will be
   prompted for 2-factor verification.

#. Select Backup Tunnel as the connection method to the
   queryable snapshot.

#. Select your Platform and download.

#. Uncompress the downloaded file.

   **Note:**

   Wait for the Queryable Snapshot to mount before you
   continue. Snapshot mount time depends on the size of the
   snapshot. Verify the snapshot is mounted by navigating to
   Continuous Backup and selecting the Restore
   History tab. When the snapshot is mounted, the Status
   column reports the date and time of the mount operation.

#. Open a terminal or command prompt and go to the uncompressed
   <tunnel> directory. Run the executable to start the tunnel. 

   The default port for the tunnel is `27017`. To change the port,
   use the `--local` flag, as in the following example:

   ```javascript
   ./<tunnel executable> --local localhost:27020
   ```

   **Note:**

   If you change the port, you must include the port information
   when connecting.

   For the full list of options you can pass to the tunnel, run the
   tunnel exectuable with the `-h` option:

   ```javascript
   ./<tunnel executable> -h
   ```

#. Use `mongosh` or a MongoDB driver to connect 
   to the backup via the tunnel.

   - If connecting locally from the same machine as where the tunnel
     is running, you do not need to specify a connection string or
     host information. Otherwise, specify a connection string or
     host information for the machine where the tunnel is running.

   - If you have changed the port that the tunnel is listening on,
     you must specify the port information when connecting.

**Tip:**

Once you have finished querying this snapshot, you can terminate the
queryable instance:

#. Go to the Restore History and hover over the
   Status column for the deployment item.

#. Click Cancel.

**Note:**

To find the log file for the queryable backup
`mongod` instance, navigate to the following path in
the head directory of the `Backup Daemon` host:

```shell
<daemon-hostname>:/<headDirectory>/queryable/<backupId>/mongod.log
```

**Important:** Rotate Master Key after Restoring Snapshots Encrypted with AES256-GCM

If you restore an
encrypted snapshot that Ops Manager
encrypted with AES256-GCM (Advanced Encryption Standards 256-bit Galois/Counter Mode),
rotate your master key
after completing the restore.

## Query Backup (Handle TLS (Transport Layer Security) Authentication Manually)

**Note:**

The client X.509 certificate is valid for the same length of time as
the queryable instance `Expiration (Hours)`,
which is 24 hours by default.

**Step 1: Go to Backup view and click the Overview tab.**

For the deployment whose backup you want to query, click
`ellipsis` under Options column then select
Query.

You can also click the deployment to view its snapshots and click
the Query button under the Actions column.

**Step 2: Follow the prompts to query a backup snapshot.**

#. Select the snapshot to query and click Next.

#. Start the process to query a snapshot. If prompted
   for your password, enter your password to verify.

#. Select Connect Manually as the connection method to
   the queryable snapshot.

#. Download the X.509 client PEM file.

#. Download the Certificate Authority PEM file.

   **Note:**

   Wait for the Queryable Snapshot to mount before you
   continue. Snapshot mount time depends on the size of the
   snapshot. Verify the snapshot is mounted by navigating to
   Continuous Backup and selecting the Restore
   History tab. When the snapshot is mounted, the Status
   column reports the date and time of the mount operation.

#. Use `mongosh` or a MongoDB driver to connect
   to the queryable backup host. To connect, you must specify the
   hostname and port, the TLS (Transport Layer Security) option, and the X.509 certificates.

   **Example:**

   If using `mongosh` to connect to the instance:

   ```sh
   mongosh my-queryable-backup-host.mongodb.com:27217 \
         --tls --tlsCertificateKeyFile <client certificate> \
         --tlsCAFile mms-backup-ca.pem
   ```

**Tip:**

Once you have finished querying this snapshot, you can terminate the
queryable instance:

#. Go to the Restore History and hover over the
   Status column for the deployment item.

#. Click Cancel.

**Important:** Rotate Master Key after Restoring Snapshots Encrypted with AES256-GCM

If you restore an
encrypted snapshot that Ops Manager
encrypted with AES256-GCM (Advanced Encryption Standards 256-bit Galois/Counter Mode),
rotate your master key
after completing the restore.

## Next Steps

To restore a database or a collection using the queryable backup
MongoDB instance, see restore-from-queryable-backup.
