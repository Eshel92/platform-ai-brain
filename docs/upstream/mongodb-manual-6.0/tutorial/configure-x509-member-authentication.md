<!-- Converted from tutorial/configure-x509-member-authentication.txt (reStructuredText). Includes are inlined. -->

# Use X.509 Certificate for Membership Authentication with Self-Managed MongoDB

MongoDB supports X.509 certificate authentication for use with a secure
TLS/SSL connection. Sharded cluster
members and replica set members can use x.509 certificates to verify
their membership to the cluster or the replica set instead of using
keyfiles. The membership authentication is
an internal process.

**Note:**

MongoDB disables support for TLS 1.0
encryption on systems where TLS 1.1+ is available. 

Enabling internal authentication also enables 
/core/authorization. Clients must authenticate as a user in order to 
connect and perform operations in the deployment.

* See the /tutorial/manage-users-and-roles tutorial for 
  instructions on adding users to the deployment.

* See the /tutorial/configure-x509-client-authentication tutorial 
  for instructions on using X.509 certificates for user authentication.

**Important:**

A full description of TLS/SSL, PKI (Public Key Infrastructure) certificates, in particular X.509 certificates, and Certificate Authority is beyond the scope of this document.
This tutorial assumes prior knowledge of TLS/SSL as well as access to valid X.509 certificates.

## Member X.509 Certificate

**Note:**

You must have valid X.509 certificates.

If you specify `--tlsAllowInvalidCertificates` or 
`net.tls.allowInvalidCertificates: true`, an invalid certificate is
sufficient only to establish a TLS connection but it is
*insufficient* for authentication.

### Certificate Requirements

Use member certificates to verify membership to a sharded 
cluster or a replica set. Member certificates are stored in 
`net.tls.clusterFile` and `net.tls.certificateKeyFile`. 
Member certificate requirements:

- A single Certificate Authority (CA) must issue all x.509
  certificates for the members of a sharded cluster or a replica set.

- The x.509 certificate must *not* be expired.

  **Note:**

  `mongod` / `mongos` logs a warning on
  connection if the presented X.509 certificate expires within `30`
  days of the `mongod/mongos` host system time.

- The Distinguished Name (`DN`), found in the member certificate's
  `subject`, must specify a non-empty value for *at least one* of
  the following attributes:

  - the Organization (`O`)
  - the Organizational Unit (`OU`)
  - the Domain Component (`DC`)

- In multi-cluster deployments, each cluster must use a different X.509
  member certificate.  Each certificate **must** have unique values
  on the `O`, `OU`, and `DC` Distinguished Name (DN) fields.

  If two clusters have certificates with the same DN values, a
  compromised server on one cluster can authenticate as a
  member of the other.

- Each cluster member certificate must have identical `O`\s, `OU`\s, 
  and `DC`\s in their `net.tls.clusterFile` and
  `net.tls.certificateKeyFile` certificates. This also applies to 
  the `tlsX509ClusterAuthDNOverride` value, if set. Attribute 
  order doesn't matter.

  Here's an example. The two `DN`\s below have matching
  specifications for `O` and `OU`, and `DC` is not specified.

  ```none
  CN=host1,OU=Dept1,O=MongoDB,ST=NY,C=US
  C=US, ST=CA, O=MongoDB, OU=Dept1, CN=host2
  ```

  The following example is incorrect, because the `DN`\s don't match. One 
  `DN` has two `OU` specifications and the other has only one `OU`
  specification.

  ```none
  CN=host1,OU=Dept1,OU=Sales,O=MongoDB
  CN=host2,OU=Dept1,O=MongoDB
  ```

- Either the Common Name (`CN`) or one of the Subject Alternative
  Name (`SAN`) entries must match the server hostname for other cluster
  members. Starting in MongoDB 4.2, when comparing `SAN`\s, MongoDB can 
  compare either DNS names or IP addresses. In previous versions, MongoDB 
  only compares DNS names.

  For example, the certificates for a cluster could have the
  following `subject`\s:

  ```bash
  subject= CN=<myhostname1>,OU=Dept1,O=MongoDB,ST=NY,C=US
  subject= CN=<myhostname2>,OU=Dept1,O=MongoDB,ST=NY,C=US
  subject= CN=<myhostname3>,OU=Dept1,O=MongoDB,ST=NY,C=US
  ```

- If the certificate used as the `certificateKeyFile` includes 
  `extendedKeyUsage`, the value must include both
  `clientAuth` ("TLS Web Client Authentication") and `serverAuth`
  ("TLS Web Server Authentication").

  ```none
  extendedKeyUsage = clientAuth, serverAuth
  ```

- If the certificate used as the `clusterFile` includes 
  `extendedKeyUsage`, the value must include `clientAuth`.

  ```none
  extendedKeyUsage = clientAuth
  ```

## Configure Replica Set/Sharded Cluster

Outside of rolling upgrade procedures, every component of a replica
set or sharded cluster should use the same
`--clusterAuthMode` setting to ensure it can securely connect to all
other components in the deployment.

For replica set deployments, this includes all `mongod` 
members of the replica set.

For sharded cluster deployments, this includes all `mongod` 
or `mongos` instances. 

**Note:**

`mongod` and `mongos`
bind to localhost by default. If the members of your deployment are
run on different hosts or if you wish remote clients to connect to
your deployment, you must specify `--bind_ip` or
`net.bindIp`. 

### Use Command-line Options (`tls`)

**Note:**

The procedures in this section use the `tls` settings/option. For
procedures using the deprecated `ssl` aliases, see
configure-member-ssl.

The `tls` settings/options provide **identical** functionality
as the `ssl` options since MongoDB has always supported TLS 1.0
and later.

   
   

tabs:

   - id: "commandline"
     name: "TLS (Command-Line Options)"
     content: |

        ```bash
        mongod --replSet <name> --tlsMode requireTLS --clusterAuthMode x509 --tlsClusterFile <path to membership certificate and key PEM file> --tlsCertificateKeyFile <path to TLS/SSL certificate and key file> --sslCAFile <path to root CA file> --bind_ip localhost,<hostname(s)|ip address(es)>
        ```

        **Important:**

        To use X.509 authentication, `--tlsCAFile` or `net.tls.CAFile`
        must be specified unless you are using `--tlsCertificateSelector`
        or `--net.tls.certificateSelector`.

        Include any additional options, TLS/SSL or otherwise, that
        are required for your specific configuration. For 

   - id: "config"
     name: "TLS (Configuration File)"
     content: |

        ```yaml
        security:
           clusterAuthMode: x509
        net:
           tls:
              mode: requireTLS
              certificateKeyFile: <path to its TLS/SSL certificate and key file>
              CAFile: <path to root CA PEM file to verify received certificate>
              clusterFile: <path to its certificate key file for membership authentication>
           bindIp: localhost,<hostname(s)|ip address(es)>
        ```

        **Important:**

        To use X.509 authentication, `--tlsCAFile` or `net.tls.CAFile`
        must be specified unless you are using `--tlsCertificateSelector`
        or `--net.tls.certificateSelector`.

        Include any additional options, TLS/SSL or otherwise, that
        are required for your specific configuration.

For more information, see /tutorial/configure-ssl.

### Use Command-line Options (`ssl`)

**Note:**

The procedures in this section use the deprecated `ssl` settings/option.
For procedures that use `tls` aliases, see configure-member-tls.

The `tls` settings/options provide **identical** functionality
as the `ssl` options since MongoDB has always supported TLS 1.0
and later.

tabs:

   - id: "commandline"
     name: "SSL (Command-Line Options)"
     content: |

         To specify the X.509 certificate for internal cluster member
         authentication, append the additional TLS/SSL options
         `--clusterAuthMode` and `--sslClusterFile`, as in the
         following example for a member of a replica set:

         ```bash
         mongod --replSet <name> --sslMode requireSSL --clusterAuthMode x509 --sslClusterFile <path to membership certificate and key PEM file> --sslPEMKeyFile <path to TLS/SSL certificate and key PEM file> --sslCAFile <path to root CA PEM file> --bind_ip localhost,<hostname(s)|ip address(es)>
         ```

         **Important:**

         To use X.509 authentication, `--tlsCAFile` or `net.tls.CAFile`
         must be specified unless you are using `--tlsCertificateSelector`
         or `--net.tls.certificateSelector`.

         Include any additional options, TLS/SSL or otherwise, that
         are required for your specific configuration.

   - id: "config"
     name: "SSL (Configuration File)"
     content: |

         ```yaml
         security:
            clusterAuthMode: x509
         net:
            ssl:
               mode: requireSSL
               PEMKeyFile: <path to TLS/SSL certificate and key PEM file>
               CAFile: <path to root CA PEM file>
               clusterFile: <path to X.509 membership certificate and key PEM file>
            bindIp: localhost,<hostname(s)|ip address(es)>
         ```

         **Important:**

         To use X.509 authentication, `--tlsCAFile` or `net.tls.CAFile`
         must be specified unless you are using `--tlsCertificateSelector`
         or `--net.tls.certificateSelector`.

         Include any additional options, TLS/SSL or otherwise, that
         are required for your specific configuration.

For more information, see /tutorial/configure-ssl.

## Additional Information

To upgrade from keyfile internal authentication to X.509 internal
authentication, see
/tutorial/upgrade-keyfile-to-x509.

To perform a rolling update of the certificates to new certificates
with different `DN`, see
/tutorial/rotate-x509-membership-certificates.
