<!-- Converted from tutorial/convert-replica-set-to-replicated-shard-cluster.txt (reStructuredText). Includes are inlined. -->

# Convert a Self-Managed Replica Set to a Sharded Cluster

## Overview

This tutorial converts a single three-member replica set to a sharded
cluster with two shards. Each shard is an independent three-member
replica set. This tutorial is specific to MongoDB 6.0.
For other versions of MongoDB, refer to the corresponding version of the
MongoDB Manual.

You can convert to a sharded cluster in the UI for deployments hosted in [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server).

## Considerations

Individual steps in these procedures note when downtime will occur.

**Important:**

These procedures cause some downtime for your deployment.

## Prerequisites

This tutorial uses a total of ten servers: one server for the
`mongos` and three servers each for the first replica
set, the second replica set, and the config server replica set. 

Each server must have a resolvable domain, hostname, or IP address
within your system.

The tutorial uses the default data directories (e.g. `/data/db` and
`/data/configdb`). Create the appropriate directories with
appropriate permissions. To use different paths, see
/reference/configuration-options .

## Procedures

**Step 1: Get the Existing Users and Roles from the Replica Set**

To get existing users and roles, run `mongodump`:

```sh
mongodump -d=admin --out=adminDump -u <adminUser> -p <password> --host <replicaSetURI> --dumpDbUsersAndRoles
```

**Step 2: Deploy the Config Server Replica Set**

Deploy a three-member replica set for the config servers. In this
example, the config servers use the following hosts:

- `mongodb7.example.net`
- `mongodb8.example.net`
- `mongodb9.example.net`

a. Configure the Config Servers

   Configure a `mongod` instance on each config server host.
   Specify these options in the configuration file for each `mongod` instance:

   | Option | Value |
   |---|---|
   | `replication.replSetName` | `configReplSet` |
   | `sharding.clusterRole` | `configsvr` |
   | `net.bindIp` | `localhost`, followed by any other hostnames on which the `mongod` should listen for client connections. |

   ```yaml
   replication:
     replSetName: configReplSet
   sharding:
     clusterRole: configsvr
   net:
     bindIp: localhost,<ipaddress>
   ```

   Include additional options as appropriate for your deployment.

#. Start the Config Servers

   Deploy the `mongod` with your specified configuration:

   ```sh
   mongod --config <PATH_TO_CONFIG_FILE>
   ```

   The config servers use the default data directory
   `/data/configdb` and the default port `27019`.

#. Connect to one of the config servers.

   Use `mongosh` to connect to one of the config
   servers. For example:

   ```sh
   mongosh "mongodb://mongodb7.example.net:27019"
   ```

#. Initiate the config server replica set.

   To initiate the replica set, run `rs.initiate()`:

   ```javascript
   rs.initiate( {
      _id: "configReplSet",
      configsvr: true,
      members: [
         { _id: 0, host: "mongodb7.example.net:27019" },
         { _id: 1, host: "mongodb8.example.net:27019" },
         { _id: 2, host: "mongodb9.example.net:27019" }
      ]
   } )
   ```

   The preceding command uses the localhost exception to perform administrative actions without
   authentication.

   **Important:**

   Run `rs.initiate()` on *just one and only one*
   `mongod` instance for the replica set.

**Step 3: Restore Existing Users and Roles to the New Config**

Restore the existing users and roles you got when you ran `mongodump`.

```sh
mongorestore ./adminDump --nsInclude "admin.*" --host <configPrimaryURI>
```

The preceding command uses the localhost exception to perform administrative actions without
authentication.

The output from running this command may be similar to:

```sh
0 document(s) restored successfully
```

This message does not indicate a problem. This output means that 0 documents
other than the users and roles were restored.

**Step 4: Secure Config Server Replica Set**

Reconfigure and restart the config server replica set.

a. Reconfigure the Config Servers

   Select the tab for your authentication mechanism:

   **keyfile:**

   Restart a `mongod` instance on each of these hosts:

   - `mongodb7.example.net`
   - `mongodb8.example.net`
   - `mongodb9.example.net`

   Specify these options in the configuration file for each `mongod` instance:

   | Option | Value |
   |---|---|
   | `security.keyFile` | The path to the key file used for your initial replica set. |

   ```yaml
   security:
      keyFile: <PATH_TO_KEYFILE>
   replication:
      replSetName: configReplSet
   sharding:
      clusterRole: configsvr
   net:
      bindIp: localhost,<ipaddress>
   ```

   Include additional options as appropriate for your deployment.

   **x509:**

   Restart a `mongod` instance on each of these hosts:

   - `mongodb7.example.net`
   - `mongodb8.example.net`
   - `mongodb9.example.net`

   Specify these options in the configuration file for each `mongod` instance
   in addition to the options you already configured:

   | Option | Value |
   |---|---|
   | `security.clusterAuthMode` | `x509` |
   | `net.tls.mode` | `requireTLS` |
   | `net.tls.certificateKeyFile` | The absolute path to the `.pem` file that contains both the TLS certificate and key. |
   | `net.tls.CAFile` | The absolute path to the `.pem` file that contains the root certificate chain from the Certificate Authority. |
   | `net.bindIp` | `localhost`, followed by any other hostnames on which the `mongod` should listen for client connections. WARNING: Before binding to a non-localhost (e.g. publicly accessible) IP address, ensure you have secured your cluster from unauthorized access. For a complete list of security recommendations, see /administration/security-checklist. At minimum, consider enabling authentication and hardening network infrastructure. |

   ```yaml
   sharding:
      clusterRole: configsvr
   replication:
      replSetName: configReplSet
   security:
      clusterAuthMode: x509
   net:
      tls:
         mode: requireTLS
         certificateKeyFile: <FILE_WITH_COMBINED_CERT_AND_KEY>
         CAFile: <CA_FILE>
      bindIp: localhost,<ipaddress>
   ```

   Include additional options as appropriate for your deployment, such as
   `net.tls.certificateKeyFilePassword` if your TLS certificate-key file is
   encrypted with a password.

#. Restart MongoDB

   Restart the `mongod` with your specified configuration:

   ```sh
   mongod --config <PATH_TO_CONFIG_FILE> --shutdown
   mongod --config <PATH_TO_CONFIG_FILE>
   ```

**Step 5: Deploy the `mongos`**

The `mongos` provides the interface between the client
applications and the sharded cluster.

a. Create a configuration file for the mongos.

   **keyfile:**

   Specify these options in your `mongos` configuration file:

   | Option | Value |
   |---|---|
   | `sharding.configDB` | `configReplSet`, followed by a slash `/` and at least one of the config server hostnames and ports. |
   | `security.keyFile` | The path to the key file used for your initial replica set. |
   | `net.bindIp` | `localhost`, followed by any other hostnames on which the `mongos` should listen for client connections. |

   ```yaml
   sharding:
      configDB: configReplSet/mongodb7.example.net:27019,mongodb8.example.net:27019,mongodb9.example.net:27019
   security:
      keyFile: <PATH_TO_KEYFILE>
   net:
      bindIp: localhost,<ipaddress>
   ```

   Include additional options as appropriate for your deployment.

   **x509:**

   Specify these options in your `mongos` configuration file:

   | Option | Value |
   |---|---|
   | `sharding.configDB` | `configReplSet`, followed by a slash `/` and at least one of the config server hostnames and ports. |
   | `security.clusterAuthMode` | `x509` |
   | `net.tls.mode` | `requireTLS` |
   | `net.tls.certificateKeyFile` | The absolute path to the `.pem` file that contains both the TLS certificate and key. |
   | `net.tls.CAFile` | The absolute path to the `.pem` file that contains the root certificate chain from the Certificate Authority. |
   | `net.bindIp` | `localhost`, followed by any other hostnames on which the `mongos` should listen for client connections. |

   ```yaml
   sharding:
      configDB: configReplSet/mongodb7.example.net:27019,mongodb8.example.net:27019,mongodb9.example.net:27019
   security:
      clusterAuthMode: x509
   net:
      tls:
         mode: requireTLS
         certificateKeyFile: <FILE_WITH_COMBINED_CERT_AND_KEY>
         CAFile: <CA_FILE>
      bindIp: localhost,<ipaddress>
   ```

   Include any additional options appropriate for your deployment.

#. Deploy the mongos.

   Deploy the `mongos` with your specified configuration:

   ```sh
   mongos --config <PATH_TO_CONFIG_FILE>
   ```

**Step 6: Restart the Initial Replica Set as a Shard**

In this example, your initial replica set is a three-member replica set.
This step updates the initial replica set so that it can be added as a
shard to your sharded cluster.

The replica set runs on these hosts:

- `mongodb0.example.net:27017`
- `mongodb1.example.net:27017`
- `mongodb2.example.net:27017`

For sharded clusters, you must set the role for each
`mongod` instance in the shard to `shardsvr`. To specify
the server role, set the `sharding.clusterRole` setting in the
`mongod` configuration file.

**Note:**

The default port for `mongod` instances with the
`shardsvr` role is `27018`. To use a different port, specify the
`net.port` setting.

a. Connect to a member of your initial replica set.

   Use `mongosh` to connect to one of the members of your
   **initial replica set**.

   **keyfile:**

   ```sh
   mongosh "mongodb://<username>@mongodb0.example.net:27017"
   ```

   **x509:**

   If your deployment uses X.509 authentication, specify these
   `mongosh` options:

   - `--tls`
   - `--tlsCAFile`
   - `--tlsCertificateKeyFile`

   For example:

   ```sh
   mongosh "mongodb://<username>@mongodb0.example.net:27017" --tls --tlsCAFile <CA_FILE> --tlsCertificateKeyFile <filename>
   ```

#. Determine the replica set's primary and secondaries.

   Run `rs.status()` to determine the primary and
   secondaries:

   ```sh
   rs.status()
   ```

   In the command output, the
   `replSetGetStatus.members[n].stateStr` field indicates which
   member is the primary and which members are secondaries.

#. Restart the secondaries with the `--shardsvr` option.

   **Warning:**

   This step requires some downtime for applications
   connected to the replica set secondaries.

   **keyfile:**

   i. Connect to a secondary.

      Use `mongosh` to connect to one of the
      secondaries.

      ```sh
      mongosh "mongodb://<username>@<host>:<port>"
      ```

   #. Shut down the secondary.

      Run the following commands:

      ```javascript
      use admin
      db.shutdownServer()
      ```

   #. Edit the secondary's configuration file.

      In the secondary's configuration file, set
      `sharding.clusterRole` to `shardsvr`:

      ```yaml
      security:
         keyFile: <PATH_TO_KEYFILE>
      replication:
        replSetName: rs0
      sharding:
         clusterRole: shardsvr
      net:
         port: 27017
         bindIp: localhost,<ipaddress>
      ```

      Include additional options as appropriate for your deployment.

   #. Restart the secondary as a shard server.

      Run the following command on the host containing the secondary:

      ```sh
      mongod --config <PATH_TO_CONFIG_FILE>
      ```

   #. Repeat the shut down and restart steps for the other secondary.

   **x509:**

   i. Connect to a secondary.

      Use `mongosh` to connect to one of the secondaries.

      If your deployment uses X.509 authentication, specify these
      `mongosh` options:

      - `--tls`
      - `--tlsCAFile`
      - `--tlsCertificateKeyFile`

      ```sh
      mongosh "mongodb://<username>@<host>:<port>" --tls --tlsCAFile <CA_FILE> --tlsCertificateKeyFile <filename>
      ```

   #. Shut down the secondary.

      Run the following commands:

      ```javascript
      use admin
      db.shutdownServer()
      ```

   #. Edit the secondary's configuration file.

      In the secondary's configuration file, set
      `sharding.clusterRole` to `shardsvr`:

      ```yaml
      replication:
         replSetName: rs0
      sharding:
         clusterRole: shardsvr
      security:
         clusterAuthMode: x509
      net:
         port: 27017
         tls:
            mode: requireTLS
            certificateKeyFile: <FILE_WITH_COMBINED_CERT_AND_KEY>
            CAFile: <CA_FILE>
         bindIp: localhost,<ipaddress>
      ```

      Include additional options as appropriate for your deployment, such as
      `net.tls.certificateKeyFilePassword` if your TLS certificate-key file is
      encrypted with a password.

   #. Restart the secondary as a shard server.

      Run the following command on the host containing the secondary:

      ```sh
      mongod --config <PATH_TO_CONFIG_FILE>
      ```

   #. Repeat the shut down and restart steps for the other secondary.

**Step 7: Restart the primary with the `--shardsvr` option.**

**Warning:**

This step requires some downtime for applications
connected to the primary of the replica set.

**keyfile:**

a. Connect to the primary.

   Use `mongosh` to connect to the primary:

   ```
   mongosh "mongodb://<username>@<host>:<port>"
   ```

#. Step down the primary.

   Run the following command:

   ```javascript
   rs.stepDown()
   ```

#. Verify that the step down is complete.

   Run `rs.status()` to confirm that the member you are
   connected to has stepped down and is now a secondary:

   ```javascript
   rs.status()
   ```

#. Shut down the former primary.

   Run the following commands:

   ```javascript
   use admin
   db.shutdownServer()
   ```

   Wait for the shutdown to complete.

#. Edit the primary's configuration file.

   In the primary's configuration file, set
   `sharding.clusterRole` to `shardsvr`:

   ```yaml
   security:
      keyFile: <PATH_TO_KEYFILE>
   replication:
      replSetName: rs0
   sharding:
      clusterRole: shardsvr
   net:
      port: 27017
      bindIp: localhost,<ipaddress>
   ```

   Include additional options as appropriate for your deployment.

#. Restart the primary as a shard server.

   Run the following command on the host containing the primary:

   ```sh
   mongod --config <PATH_TO_CONFIG_FILE>
   ```

**x509:**

a. Connect to the primary.

   Use `mongosh` to connect to one of the secondaries.

   If your deployment uses X.509 authentication, specify these
   `mongosh` options:

   If your deployment uses X.509 authentication, specify these
   `mongosh` options:

   - `--tls`
   - `--tlsCAFile`
   - `--tlsCertificateKeyFile`

   ```sh
   mongosh "mongodb://<username>@<host>:<port>" --tls --tlsCAFile <CA_FILE> --tlsCertificateKeyFile <filename>
   ```

#. Step down the primary.

   Run the following command:

   ```javascript
   rs.stepDown()
   ```

#. Verify that the step down is complete.

   Run `rs.status()` to confirm that the member you are
   connected to has stepped down and is now a secondary:

   ```javascript
   rs.status()
   ```

#. Shut down the former primary.

   Run the following commands:

   ```javascript
   use admin
   db.shutdownServer()
   ```

   Wait for the shutdown to complete.

#. Edit the primary's configuration file.

   In the primary's configuration file, set
   `sharding.clusterRole` to `shardsvr`:

   ```yaml
   replication:
      replSetName: rs0
   sharding:
      clusterRole: shardsvr
   security:
      clusterAuthMode: x509
   net:
      port: 27017
      tls:
         mode: requireTLS
         certificateKeyFile: <FILE_WITH_COMBINED_CERT_AND_KEY>
         CAFile: <CA_FILE>
      bindIp: localhost,<ipaddress>
   ```

   Include additional options as appropriate for your deployment, such as
   `net.tls.certificateKeyFilePassword` if your TLS certificate-key file is
   encrypted with a password.

#. Restart the primary as a shard server.

   Run the following command on the host containing the primary:

   ```sh
   mongod --config <PATH_TO_CONFIG_FILE>
   ```

**Step 8: Add the Initial Replica Set as a Shard**

After you convert the initial replica set (`rs0`) to a shard, add it
to the sharded cluster.

a. Connect to the `mongos` as your cluster's administrative user.

   The `mongos` instance is running on host
   `mongodb6.example.net`.

   **keyfile:**

   To connect `mongosh` to the `mongos`,  run the following
   command:

   ```sh
   mongosh "mongodb://admin01@mongodb6.example.net:27017"
   ```

   **x509:**

   If your deployment uses X.509 authentication, specify these
   `mongosh` options:

   If your deployment uses X.509 authentication, specify these
   `mongosh` options:

   - `--tls`
   - `--tlsCAFile`
   - `--tlsCertificateKeyFile`

   ```sh
   mongosh "mongodb://admin01@mongodb6.example.net:27017" --tls --tlsCAFile <CA_FILE> --tlsCertificateKeyFile <filename>
   ```

   This command authenticates you as the `admin01` user you created
   on the sharded cluster. After you enter the command, enter your
   user's password.

#. Add the shard.

   To add a shard to the cluster, run the `sh.addShard`
   method:

   ```javascript
   sh.addShard( "rs0/mongodb0.example.net:27017,mongodb1.example.net:27017,mongodb2.example.net:27017" )
   ```

**Step 9: Update Your Application Connection String**

After you add the first shard to your cluster, update the
connection string used by your applications to the
connection string for your sharded cluster. Then, restart your
applications.

**Warning:**

Once the new shard is active, `mongosh` and other clients must
**always** connect to the `mongos` instance. Do not connect
directly to the `mongod` instances. If your clients connect to
shards directly, you may create data or metadata inconsistencies.

**Step 10: Deploy a Second Replica Set**

Deploy a new replica set called `rs1`. The members of replica set
`rs1` are on the following hosts:

- `mongodb3.example.net`
- `mongodb4.example.net`
- `mongodb5.example.net`

a. Start each member of the replica set.

   **keyfile:**

   For each `mongod` instance in the replica set,
   create a configuration file with these options:

   | Option | Value |
   |---|---|
   | `security.keyFile` | The path to the key file used for your initial replica set. |
   | `replication.replSetName` | `rs1` |
   | `sharding.clusterRole` | `shardsvr` |
   | `net.bindIp` | `localhost`, followed by any other hostnames on which the `mongod` should listen for client connections. |

   ```yaml
   security:
      keyFile: <PATH_TO_KEYFILE>
   replication:
      replSetName: rs1
   sharding:
      clusterRole: shardsvr
   net:
      bindIp: localhost,<ipaddress>
   ```

   Include additional options as appropriate for your deployment.

   **x509:**

   For each member, start a `mongod` with the
   following options:

   | Option | Value |
   |---|---|
   | `replication.replSetName` | `rs1` |
   | `sharding.clusterRole` | `shardsvr` |
   | `security.clusterAuthMode` | `x509` |
   | `net.tls.mode` | `requireTLS` |
   | `net.tls.certificateKeyFile` | The absolute path to the `.pem` file that contains both the TLS certificate and key. |
   | `net.tls.CAFile` | The absolute path to the `.pem` file that contains the root certificate chain from the Certificate Authority. |
   | `net.bindIp` | `localhost`, followed by any other hostnames on which the `mongod` should listen for client connections. |

   ```yaml
   replication:
      replSetName: rs1
   sharding:
      clusterRole: shardsvr
   security:
      clusterAuthMode: x509
   net:
      tls:
         mode: requireTLS
         certificateKeyFile: <FILE_WITH_COMBINED_CERT_AND_KEY>
         CAFile: <CA_FILE>
      bindIp: localhost,<ipaddress>
   ```

   Deploy the `mongod` with your specified configuration:

   ```sh
   mongod --config <PATH_TO_CONFIG_FILE>
   ```

   **Note:**

   When you specify the `--shardsvr` option for a
   `mongod` instance, the instance runs on port `27018`
   by default.

#. Start each member of the replica set.

#. Connect to a replica set member.

   Use `mongosh` to connect to one of the replica set
   members. For example:

   **keyfile:**

   ```sh
   mongosh "mongodb://mongodb3.example.net:27018"
   ```

   **x509:**

   ```sh
   mongosh "mongodb://mongodb3.example.net:27018" --tls --tlsCAFile <CA_FILE> --tlsCertificateKeyFile <filename>
   ```

#. Initiate the replica set.

   In `mongosh`, run the `rs.initiate()`
   method to initiate a replica set that contains the current member:

   ```javascript
   rs.initiate( {
      _id : "rs1",
      members: [
          { _id: 0, host: "mongodb3.example.net:27018" },
          { _id: 1, host: "mongodb4.example.net:27018" },
          { _id: 2, host: "mongodb5.example.net:27018" }
      ]
   } )
   ```

   The preceding command requires the localhost exception to perform administrative actions without
   authentication. 

   **Important:**

   Run `rs.initiate()` on *just one and only one*
   `mongod` instance for the replica set.

#. Add an administrative user for the replica set.

   After you deploy the replica set, use the localhost exception to create the replica set's first user.

   a. Determine the replica set primary.

      To determine the primary, run `rs.status()`:

      ```sh
      rs.status()
      ```

      In the command output, the
      `replSetGetStatus.members[n].stateStr` field indicates
      which member is the primary.

   #. Connect to the replica set primary.

      Connect to the replica set primary with `mongosh`.
      For example, if the primary is `mongodb4.example.net`, run
      this command:

      **keyfile:**

      ```sh
      mongosh "mongodb://mongodb4.example.net:27018"
      ```

      **x509:**

      ```sh
      mongosh "mongodb://mongodb4.example.net:27018" --tls --tlsCAFile <CA_FILE> --tlsCertificateKeyFile <filename>
      ```

   #. Create an administrative user.

      Run the following `db.createUser()` method to create
      a user named `rs1Admin` with the `userAdmin`
      role:

      ```javascript
      use admin

      db.createUser(
         {
            user: "rs1Admin",
            pwd: passwordPrompt(),
            roles: [
               { role: "userAdmin", db: "admin" }
            ]
         }
      )
      ```

      After you run the command, the database prompts you to enter a
      password for the `rs1Admin` user.

**Step 11: Add the Second Replica Set to the Cluster as a Shard**

Add the new replica set, `rs1`, to the sharded cluster.

a. Connect `mongosh` to the `mongos`.

   Run the following command **from the command line** to connect to
   the `mongos` instance running on host `mongodb6.example.net`:

    :hidden:

   **keyfile:**

   ```sh
   mongosh "mongodb://admin01@mongodb6.example.net:27017/admin"
   ```

   **x509:**

   ```sh
   mongosh "mongodb://admin01@mongodb6.example.net:27017/admin" --tls --tlsCAFile <CA_FILE> --tlsCertificateKeyFile <filename>
   ```

   This command authenticates you as the `admin01` user you created
   on the sharded cluster. After you enter the command, enter your
   user's password.

#. Add the second shard.

   After you connect to the `mongos`, add the replica set
   `rs1` as a shard to the cluster with the `sh.addShard()`
   method:

   ```javascript
   sh.addShard( "rs1/mongodb3.example.net:27018,mongodb4.example.net:27018,mongodb5.example.net:27018" )
   ```

**Step 12: Shard a Collection**

The final step of the procedure is to shard a collection in the sharded
cluster.

a. Determine the shard key.

   Determine the shard key for the
   collection. The shard key indicates how MongoDB distributes the
   documents between shards. Good shard keys:

   - Have values that are evenly distributed among all documents.
   - Group documents that are often accessed at the same time into
     contiguous chunks.
   - Allow for effective distribution of activity among shards.

   For more information, see sharding-shard-key-selection.

   This procedure uses the `number` field as the shard key for
   the `test_collection` collection.

#. Create an index on the shard key.

   Before you shard a non-empty collection, create an index on the
   shard key:

   ```javascript
   use test
   db.test_collection.createIndex( { "number" : 1 } )
   ```

#. Shard the collection.

   In the `test` database, shard the `test_collection`.
   Specify `number` as the shard key.

   ```javascript
   sh.shardCollection( "test.test_collection", { "number" : 1 } )
   ```

   The next time that the balancer runs,
   it redistributes chunks of documents between shards. As clients
   insert additional documents into this collection, the
   `mongos` routes the documents to the appropriate
   shard.

   When the balancer redistributes chunks, it may negatively
   impact your application's performance. To minimize performance
   impact, you can specify when the balancer runs so it does not
   run during peak hours. To learn more, see
   sharding-schedule-balancing-window.

## Learn More

For more sharding tutorials and procedures, see these pages:

- sharding-manage-shards
- back-up-sharded-cluster-metadata
- sharding-high-availability
