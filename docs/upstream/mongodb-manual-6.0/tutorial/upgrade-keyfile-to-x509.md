<!-- Converted from tutorial/upgrade-keyfile-to-x509.txt (reStructuredText). Includes are inlined. -->

# Upgrade Self-Managed MongoDB from Keyfile Authentication to X.509 Authentication

To upgrade clusters that are currently using keyfile authentication to X.509 authentication, use the following
rolling upgrade processes.

**Note:**

MongoDB disables support for TLS 1.0
encryption on systems where TLS 1.1+ is available. 

## Upgrade Procedures (Using `tls` Options)

**Note:**

MongoDB provides `net.tls` settings (and `--tls` command-line options) that 
correspond to the `net.ssl` settings (and `--ssl` command-line options). 
The new `tls` settings provide **identical** functionality as the `ssl` 
settings since MongoDB has always supported TLS 1.0 and later.

The procedures in this section use the `tls` settings/options. For
procedures using the `ssl` settings/options, see upgrade-to-x509-ssl.

### Upgrade (Using `tls` Options) Clusters Using TLS/SSL and Keyfile

**Note:**

The procedure uses the `tls` settings/options. For procedures
using the `ssl` settings/options, see
upgrade-sslkeyfile-to-x509-ssl.

   
For clusters using TLS/SSL and keyfile authentication, to upgrade to X.509
cluster authentication, use the following rolling upgrade process:

#. For each member of a cluster, add the following settings to the
   configuration file and restart:

   - `security.clusterAuthMode`
         Set to `sendKeyFile`. With this setting value, each node continues
         to send its keyfile to authenticate itself as a member.
         However, each node can receive either a keyfile or an X.509
         certificate from other members to authenticate those members.

   - `net.tls.clusterFile`
         Set to the appropriate path of the node's certificate key file
         for membership authentication. The
         `mongod` / `mongos` presents this file
         to other members of the cluster to identify itself as a member.

   Include other TLS/SSL options and
   any other options as appropriate for your specific configuration.

   For example:

   ```yaml
   net:
      tls:
         mode: requireTLS
         certificateKeyFile: /etc/ssl/mongodb.pem
         CAFile: /etc/ssl/caToValidateReceivedCertificates.pem
         clusterFile: "/etc/ssl/myReplMembershipCertificateKeyFile.pem"
   security:
      clusterAuthMode: sendKeyFile
      keyFile: /my/securely/located/membershipkey
   replication:
      replSetName: myReplicaSet
   net:
      bindIp: localhost,mongodb0.example.net
      port: 27017
   systemLog:
      destination: file
      path: "/var/log/mongodb/mongod.log"
      logAppend: true
   storage:
      dbPath: "/var/lib/mongodb"
   processManagement:
      fork: true
   ```

   Update all nodes of the cluster to include the
   `security.clusterAuthMode` and
   `net.tls.clusterFile` settings before continuing.

#. Connect to each node and use the
   `setParameter` command to update the `clusterAuthMode`
   to `sendX509`. [#update-mode-alternative]_

   ```bash
   db.adminCommand( { setParameter: 1, clusterAuthMode: "sendX509" } )
   ```

   With `sendX509`, each node sends its
   `net.tls.clusterFile` to authenticate itself as a member.
   However, each node can receive either a keyfile or an X.509
   certificate from other members to authenticate those members.

   Upgrade all nodes of the cluster to this setting before continuing.

#. Optional but recommended. Finally, for each node of the cluster,
   connect to the node and use the `setParameter` command to
   update the `clusterAuthMode` to `x509` to only use the
   X.509 certificate for authentication. [#update-mode-alternative]_

   ```bash
   db.adminCommand( { setParameter: 1, clusterAuthMode: "x509" } )
   ```

#. After the upgrade of all nodes, edit the configuration file with the appropriate X.509
   settings to ensure that upon subsequent restarts, the cluster uses
   X.509 authentication.  For example:

   ```yaml
   net:
      tls:
         mode: requireTLS
         certificateKeyFile: /etc/ssl/mongodb.pem
         CAFile: /etc/ssl/caToValidateReceivedCertificates.pem
         clusterFile: "/etc/ssl/myReplMembershipCertificateKeyFile.pem"
   security.clusterAuthMode: x509
   replication:
      replSetName: myReplicaSet
   net:
      bindIp: localhost,mongodb0.example.net
      port: 27017
   systemLog:
      destination: file
      path: "/var/log/mongodb/mongod.log"
      logAppend: true
   storage:
      dbPath: "/var/lib/mongodb"
   processManagement:
      fork: true
   ```

**See also:**

You can also configure `mongod` and
`mongos` using command-line options instead of the
configuration file:

- For `mongod`, see:
  - `--tlsMode`
  - `--tlsCertificateKeyFile`
  - `--tlsCAFile`
  - `--tlsClusterFile`
  - `--clusterAuthMode`

- For  `mongos`, see:
  - `--tlsMode`
  - `--tlsCertificateKeyFile`
  - `--tlsCAFile`
  - `--tlsClusterFile`
  - `--clusterAuthMode`

### Update (Using `tls` Options) Clusters Using Keyfile but Not TLS/SSL

**Note:**

The procedure uses the `tls` options. For procedures using the
`ssl` settings/options, see upgrade-keyfile-to-x509-ssl.

For clusters using keyfile authentication but not TLS/SSL, to upgrade
to X.509 membership authentication and TLS/SSL connections:

#. For each member of a cluster, add the following settings to the
   configuration file and restart:

   - `net.tls.mode`
         Set to `allowTLS`. This value allows the node to accept
         both TLS/SSL and non-TLS/non-SSL incoming connections. Its
         outgoing connections do not use TLS/SSL.

   - `net.tls.certificateKeyFile`
         Set to the path of the file that contains the TLS/SSL
         certificate and key. The
         `mongod` / `mongos` presents this file
         to its clients to establish the instance's identity. Required
         when using TLS/SSL.

   - `net.tls.clusterFile`
         Set to the appropriate path of the node's certificate key file
         for membership authentication. The
         `mongod` / `mongos` presents this file
         to other members of the cluster to identify itself as a member.

   - `net.tls.CAFile`
         Set to the path of the file that contains the certificate
         chain for verifying received certificates.

   - `security.clusterAuthMode`
         Set to `sendKeyFile`. This allows each node continues to
         send its keyfile to authenticate itself as a member. However,
         each node can receive either a keyfile or an X.509 certificate
         from other members to authenticate those members.

   Include other TLS/SSL options and
   any other options as appropriate for your specific configuration.

   For example:

   ```yaml
   net:
      tls:
         mode: allowTLS
         certificateKeyFile: /etc/ssl/mongodb.pem
         clusterFile: "/etc/ssl/myReplMembershipCertificateKeyFile.pem" 
         CAFile: /etc/ssl/caToValidateReceivedCertificates.pem
   security:
      clusterAuthMode: sendKeyFile
      keyFile: /my/securely/located/membershipkey
   replication:
      replSetName: myReplicaSet
   net:
      bindIp: localhost,mongodb0.example.net
      port: 27017
   systemLog:
      destination: file
      path: "/var/log/mongodb/mongod.log"
      logAppend: true
   storage:
      dbPath: "/var/lib/mongodb"
   processManagement:
      fork: true
   ```

   Upgrade all nodes of the cluster to include `net.tls.mode`,
   `net.tls.certificateKeyFile`,
   `net.tls.clusterFile`, and
   `security.clusterAuthMode`.

#. Connect to each node and use the
   `setParameter` command [#update-mode-alternative]_ to:
   
   a. Update the `tlsMode`
      to `preferSSL`. With the `tlsMode` set to
      `preferTLS`, the node accepts both TLS/SSL and non-TLS/non-SSL
      incoming connections, and its outgoing connections use TLS/SSL.
     
   #. Update the `clusterAuthMode` to `sendX509`.
      With the `clusterAuthMode` set to `sendX509`, each
      node sends its `net.tls.clusterFile` to authenticate
      itself as a member. However, each node continues to accept either
      a keyfile or an X.509 certificate from other members to
      authenticate those members.

   ```bash
   db.adminCommand( { setParameter: 1, tlsMode: "preferTLS" } );
   db.adminCommand( { setParameter: 1, clusterAuthMode: "sendX509" } );
   ```

   Upgrade all nodes of the cluster to these settings before continuing.

#. After the upgrade of all nodes, edit the configuration file with the appropriate TLS/SSL and
   X.509 settings to ensure that upon subsequent restarts, the cluster
   uses X.509 authentication.

   ```yaml
   net:
      tls:
         mode: preferTLS
         certificateKeyFile: /etc/ssl/mongodb.pem
         clusterFile: "/etc/ssl/myReplMembershipCertificateKeyFile.pem" 
         CAFile: /etc/ssl/caToValidateReceivedCertificates.pem
   security:
      clusterAuthMode: sendX509
   replication:
      replSetName: myReplicaSet
   net:
      bindIp: localhost,mongodb0.example.net
      port: 27017
   systemLog:
      destination: file
      path: "/var/log/mongodb/mongod.log"
      logAppend: true
   storage:
      dbPath: "/var/lib/mongodb"
   processManagement:
      fork: true
   ```

   **Note:**

   At this point, 

   - The nodes in the cluster use TLS/SSL connections. However, the
     nodes can accept non-TLS/SSL connections from client
     applications.

   - The nodes send their X.509 certificates for membership
     authentication, but can accept either X.509 certificates or
     keyfiles from other nodes to verify the other nodes' membership.

   To enforce TLS/SSL connections from client applications as well
   as only accept X.509 for membership authentication, see next step.

#. *Optional but recommended.* Update all nodes to use only `TLS/SSL`
   connections and only X.509 certificate for membership authentication.

   **Important:**

   This TLS/SSL connection requirement applies to all connections;
   that is, with the clients as well as with the members of the
   cluster. That is, clients must specify TLS/SSL connections and
   presents its certificate key file when connecting to the cluster.
   See mongo-connect-require-client-certificates-tls for more
   information on connecting with TLS/SSL. See also
   ssl-mongod-weak-certification.

   Update the `net.tls.mode` to `requireTLS` and
   `security.clusterAuthMode` to `x509`.

   For example:

   ```yaml
   net:
      tls:
         mode: requireTLS
         certificateKeyFile: /etc/ssl/mongodb.pem
         clusterFile: "/etc/ssl/myReplMembershipCertificateKeyFile.pem" 
         CAFile: /etc/ssl/caToValidateReceivedCertificates.pem
   security:
      clusterAuthMode: x509 
   replication:
      replSetName: myReplicaSet
   net:
      bindIp: localhost,mongodb0.example.net
      port: 27017
   systemLog:
      destination: file
      path: "/var/log/mongodb/mongod.log"
      logAppend: true
   storage:
      dbPath: "/var/lib/mongodb"
   processManagement:
      fork: true
   ```

**See also:**

You can also configure `mongod` and
`mongos` using command-line options instead of the
configuration file:

- For `mongod`, see:
  - `--tlsMode`
  - `--tlsCertificateKeyFile`
  - `--tlsCAFile`
  - `--tlsClusterFile`
  - `--clusterAuthMode`

- For  `mongos`, see:
  - `--tlsMode`
  - `--tlsCertificateKeyFile`
  - `--tlsCAFile`
  - `--tlsClusterFile`
  - `--clusterAuthMode`

     

## Upgrade Procedures (Using `ssl` Options)

**Note:**

MongoDB provides `net.tls` settings (and `--tls` command-line options) that 
correspond to the `net.ssl` settings (and `--ssl` command-line options). 
The new `tls` settings provide **identical** functionality as the `ssl` 
settings since MongoDB has always supported TLS 1.0 and later.

The procedures in this section use the `ssl` options. For
procedures using the `tls` options, see
upgrade-to-x509-tls.

### Clusters Currently Using TLS/SSL (Using `ssl` Options)

**Note:**

The procedure uses the `ssl` options. For procedures using the
`tls` options, see upgrade-sslkeyfile-to-x509-ssl.

For clusters using TLS/SSL and keyfile authentication, to upgrade to X.509
cluster authentication, use the following rolling upgrade process:

#. For each node of a cluster, start the node with the option
   `--clusterAuthMode` set to `sendKeyFile` and the option
   `--sslClusterFile` set to the appropriate path of the node's
   certificate. Include other TLS/SSL options as well as any other options that are
   required for your specific configuration. For example:

   ```bash
   mongod --replSet <name> --sslMode requireSSL --clusterAuthMode sendKeyFile --sslClusterFile <path to membership certificate and key PEM file> --sslPEMKeyFile <path to TLS/SSL Certificate and key PEM file>  --sslCAFile <path to root CA PEM file> --bind_ip localhost,<hostname(s)|ip address(es)>
   ```

   With this setting, each node continues to use its keyfile to
   authenticate itself as a member. However, each node can now accept
   either a keyfile or an X.509 certificate from other members to
   authenticate those members. Upgrade all nodes of the cluster to
   this setting.

#. Then, for each node of a cluster, connect to the node and use the
   `setParameter` command to update the `clusterAuthMode`
   to `sendX509`. [#update-mode-alternative]_ For example,

   ```bash
   db.adminCommand( { setParameter: 1, clusterAuthMode: "sendX509" } )
   ```

   With this setting, each node uses its X.509 certificate, specified
   with the `--sslClusterFile` option in the previous step, to
   authenticate itself as a member. However, each node continues to
   accept either a keyfile or an X.509 certificate from other members
   to authenticate those members. Upgrade all nodes of the cluster to
   this setting.

#. Optional but recommended. Finally, for each node of the cluster,
   connect to the node and use the `setParameter` command to
   update the `clusterAuthMode` to `x509` to only use the
   X.509 certificate for authentication. [#update-mode-alternative]_
   For example:

   ```bash
   db.adminCommand( { setParameter: 1, clusterAuthMode: "x509" } )
   ```

#. After the upgrade of all nodes, edit the configuration file with the appropriate X.509
   settings to ensure that upon subsequent restarts, the cluster uses
   X.509 authentication.

See `--clusterAuthMode` for the various modes and their
descriptions.

### Clusters Currently Not Using TLS/SSL  (Using `ssl` Options)

**Note:**

The procedure uses the `ssl` options. For procedures using the
`tls` options, see upgrade-keyfile-to-x509-tls.

For clusters using keyfile authentication but not TLS/SSL, to upgrade to
X.509 authentication, use the following rolling upgrade process:

#. For each node of a cluster, start the node with the option
   `--sslMode` set to `allowSSL`, the option 
   `--clusterAuthMode` set to `sendKeyFile` 
   and the option `--sslClusterFile` set to the appropriate path of the node's
   certificate. Include other TLS/SSL options as well as any other options that are
   required for your specific configuration. For example:

   ```bash
   mongod --replSet <name> --sslMode allowSSL --clusterAuthMode sendKeyFile --sslClusterFile <path to membership certificate and key PEM file> --sslPEMKeyFile <path to TLS/SSL certificate and key PEM file> --sslCAFile <path to root CA PEM file> --bind_ip localhost,<hostname(s)|ip address(es)>
   ```

   The `--sslMode allowSSL` setting allows the node to accept both TLS/SSL 
   and non-TLS/non-SSL incoming connections. The node's outgoing connections do 
   not use TLS/SSL.

   The `--clusterAuthMode sendKeyFile`
   setting allows each node continues to use its keyfile to
   authenticate itself as a member. However, each node can now accept
   either a keyfile or an X.509 certificate from other members to
   authenticate those members.

   Upgrade all nodes of the cluster to these settings.

#. Then, for each node of a cluster, connect to the node and use the
   `setParameter` command to update the `sslMode`
   to `preferSSL` and the `clusterAuthMode` to
   `sendX509`. [#update-mode-alternative]_ For example:

   ```bash
   db.adminCommand( { setParameter: 1, sslMode: "preferSSL", clusterAuthMode: "sendX509" } )
   ```

   With the `sslMode` set to `preferSSL`, the node accepts
   both TLS/SSL and non-TLS/non-SSL incoming connections, and its outgoing
   connections use TLS/SSL.

   With the `clusterAuthMode` set to `sendX509`, each node
   uses its X.509 certificate, specified with the
   `--sslClusterFile` option in the previous step, to
   authenticate itself as a member. However, each node continues to
   accept either a keyfile or an X.509 certificate from other members
   to authenticate those members.

   Upgrade all nodes of the cluster to these settings.

#. Optional but recommended. Finally, for each node of the cluster,
   connect to the node and use the `setParameter` command to
   update the `sslMode` to `requireSSL` and the
   `clusterAuthMode` to `x509`. [#update-mode-alternative]_
   For example:

   ```bash
   db.adminCommand( { setParameter: 1, sslMode: "requireSSL", clusterAuthMode: "x509" } )
   ```

   With the `sslMode` set to `requireSSL`, the node only uses
   TLS/SSLs connections.

   With the `clusterAuthMode` set to `x509`, the node only
   uses the X.509 certificate for authentication.

#. After the upgrade of all nodes, edit the configuration file with the appropriate TLS/SSL and
   X.509 settings to ensure that upon subsequent restarts, the cluster
   uses X.509 authentication.

See `--clusterAuthMode` for the various modes and their
descriptions.
