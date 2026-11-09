<!-- Converted from tutorial/upgrade-cluster-to-ssl.txt (reStructuredText). Includes are inlined. -->

# Upgrade a Cluster to Use TLS/SSL

The MongoDB server supports listening for both TLS/SSL encrypted and
unencrypted connections on the same TCP port. This allows upgrades of
MongoDB clusters to use TLS/SSL encrypted connections. 

**Note:**

MongoDB disables support for TLS 1.0
encryption on systems where TLS 1.1+ is available. 

## Procedure (Using `tls` Settings)

**Important:**

A full description of TLS/SSL, PKI (Public Key Infrastructure) certificates, and Certificate Authority is beyond the scope of this document.
This page assumes prior knowledge of TLS/SSL as well as access to valid certificates.

To upgrade from a MongoDB cluster using no TLS/SSL encryption to one
using *only* TLS/SSL encryption, use the following rolling upgrade
process.

**Note:**

The procedures in this section use the `tls` settings/option. 
For procedures using their `ssl` aliases, see upgrade-to-ssl.

The `tls` settings/options provide **identical** functionality
as the `ssl` options since MongoDB has always supported TLS 1.0
and later.

#. For each node of a cluster, start the node with the command-line option
   `--tlsMode` or the configuration file option `net.tls.mode` set to `allowTLS`. 
   The `allowTLS` setting allows the node to accept both TLS/SSL
   and non-TLS/non-SSL incoming connections. Its connections to other servers
   do not use TLS/SSL. Include other TLS/SSL options [#systemstore]_ as well as any other options that are
   required for your specific configuration. 

   **Note:**

   `mongod` and `mongos`
   bind to localhost by default. If the members of your deployment are
   run on different hosts or if you wish remote clients to connect to
   your deployment, you must specify `--bind_ip` or
   `net.bindIp`. 

   For example:

   tabs:

     - id: commandline
       name: Command-Line Options
       content: |

         ```bash
         mongod --replSet <name> --tlsMode allowTLS --tlsCertificateKeyFile <TLS/SSL certificate and key file> --tlsCAFile <path to root CA PEM file> <additional options>
         ```

     - id: config
       name: Configuration File Options
       content: |

          To specify these options in the configuration file, include the following
          settings in the file:

          ```yaml
          net:
             tls:
                mode: allowTLS
                certificateKeyFile: <path to TLS/SSL certificate and key PEM file>
                CAFile: <path to root CA PEM file>
          ```

   Upgrade all nodes of the cluster to these settings.

#. Switch all clients to use TLS/SSL. See ssl-clients.

#. For each node of a cluster, use the `setParameter`
   command to update the `tlsMode` to `preferTLS`.
   [#update-mode-alternative]_ With `preferTLS` as its
   `net.tls.mode`, the node accepts both TLS/SSL and non-TLS/non-SSL incoming
   connections, and its connections to other servers use TLS/SSL. For
   example:

   ```bash
   db.adminCommand( { setParameter: 1, tlsMode: "preferTLS" } )
   ```

   Upgrade all nodes of the cluster to these settings.

   At this point, all connections should be using TLS/SSL.

#. For each node of the cluster, use the
   `setParameter` command to update the `tlsMode`
   to `requireTLS`. [#update-mode-alternative]_ With `requireTLS`
   as its `net.tls.mode`, the node will reject any non-TLS/non-SSL
   connections. For example:

   ```bash
   db.adminCommand( { setParameter: 1, tlsMode: "requireTLS" } )
   ```

#. After the upgrade of all nodes, edit the configuration file with the appropriate TLS/SSL
   settings to ensure that upon subsequent restarts, the cluster uses
   TLS/SSL.

## Procedure (Using `ssl` Settings)

**Important:**

A full description of TLS/SSL, PKI (Public Key Infrastructure) certificates, and Certificate Authority is beyond the scope of this document.
This page assumes prior knowledge of TLS/SSL as well as access to valid certificates.

To upgrade from a MongoDB cluster using no TLS/SSL encryption to one
using *only* TLS/SSL encryption, use the following rolling upgrade
process.

**Note:**

The procedures in this section use the `ssl` settings/option. For
procedures using their `tls` aliases, see upgrade-to-tls.

The `tls` settings/options provide **identical** functionality
as the `ssl` options since MongoDB has always supported TLS 1.0
and later.

#. For each node of a cluster, start the node with the command-line option
   `--sslMode` or the configuration file option `net.ssl.mode` set to `allowSSL`. 
   The `allowSSL` setting allows the node to accept both TLS/SSL
   and non-TLS/non-SSL incoming connections. Its connections to other servers
   do not use TLS/SSL. Include other TLS/SSL options [#systemstore]_ as well as any other options that are
   required for your specific configuration. 

   **Note:**

   `mongod` and `mongos`
   bind to localhost by default. If the members of your deployment are
   run on different hosts or if you wish remote clients to connect to
   your deployment, you must specify `--bind_ip` or
   `net.bindIp`. 

   For example:

   tabs:

     - id: commandline
       name: Command-Line Options
       content: |

         ```bash
         mongod --replSet <name> --sslMode allowSSL --sslPEMKeyFile <path to TLS/SSL Certificate and key PEM file> --sslCAFile <path to root CA PEM file> <additional options>
         ```

     - id: config
       name: Configuration File Options
       content: |

          To specify these options in the configuration file, include the following
          settings in the file:

          ```yaml
          net:
             ssl:
                mode: <allowSSL>
                PEMKeyFile: <path to TLS/SSL certificate and key PEM file>
                CAFile: <path to root CA PEM file>
          ```

   Upgrade all nodes of the cluster to these settings.

#. Switch all clients to use TLS/SSL. See ssl-clients.

#. For each node of a cluster, use the `setParameter`
   command to update the `sslMode` to `preferSSL`.
   [#update-mode-alternative]_ With `preferSSL` as its
   `net.ssl.mode`, the node accepts both TLS/SSL and non-TLS/non-SSL incoming
   connections, and its connections to other servers use TLS/SSL. For
   example:

   ```bash
   db.adminCommand( { setParameter: 1, sslMode: "preferSSL" } )
   ```

   Upgrade all nodes of the cluster to these settings.

   At this point, all connections should be using TLS/SSL.

#. For each node of the cluster, use the
   `setParameter` command to update the `sslMode`
   to `requireSSL`. [#update-mode-alternative]_ With `requireSSL`
   as its `net.ssl.mode`, the node rejects any non-TLS/non-SSL
   connections. For example:

   ```bash
   db.adminCommand( { setParameter: 1, sslMode: "requireSSL" } )
   ```

#. After the upgrade of all nodes, edit the configuration file with the appropriate TLS/SSL
   settings to ensure that upon subsequent restarts, the cluster uses
   TLS/SSL.
