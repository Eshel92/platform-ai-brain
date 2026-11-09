<!-- Converted from tutorial/configure-x509-member-authentication.txt (reStructuredText). Includes are inlined. -->

# Verify Cluster Membership with X.509 on Self-Managed MongoDB

MongoDB supports X.509 certificate authentication for use with a secure
TLS/SSL connection. Sharded cluster
members and replica set members can use X.509 certificates to verify
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

When TLS is enabled, use member certificates to verify membership 
to internal connections in a sharded cluster or a replica set. 
You can configure member certificate file paths with the 
`net.tls.clusterFile` and `net.tls.certificateKeyFile` 
options. Members have the following configuration requirements:

- Cluster member configuration must specify a non-empty value for 
  at least one of the attributes used for authentication. By default, MongoDB accepts:

  - the Organization (`O`)
  - the Organizational Unit (`OU`)
  - the Domain Component (`DC`)

  MongoDB verifies that entries match exactly across all member certificates.
  If you list multiple `OU` values, all certificates must use an identical
  list.

  You can specify alternative attributes to use for authentication by
  setting `net.tls.clusterAuthX509.extensionValue`.

- Cluster member configuration must include the same
  `net.tls.clusterAuthX509.attributes` and use matching values.
  Attribute order doesn't matter. The following example sets `O` and
  `OU`, but not `DC`:

  ```yaml
  net:
    tls:
      clusterAuthX509:
        attributes: O=MongoDB, OU=MongoDB Server
  ```

The certificates have the following requirements:

- A single Certificate Authority (CA) must issue all X.509 certificates 
  for the members of a sharded cluster or a replica set.

- At least one of the Subject Alternative Name (`SAN`) entries must
  match the server hostname used by other cluster members. When
  comparing `SAN`\s, MongoDB can compare either DNS names or IP addresses.

  If you don't specify `subjectAltName`, MongoDB compares the Common
  Name (CN) instead. However, this usage of CN is deprecated per
  [RFC2818](https://datatracker.ietf.org/doc/html/rfc2818)

Key Usage and Extended Key Usage are X.509 extensions that strictly
define and restrict the use of the key associated with a
certificate. Both of these extensions are optional. If
`tlsCertificateKeyFile` or `tlsClusterFile` point to certificates
that omit these extensions, no restrictions apply to using the
certificate.

If X.509 certificates used for `tlsCertificateKeyFile` or
`tlsClusterFile` include the Extended Key Usage (EKU) extension, they
must comply with the following rules:

- `tlsCertificateKeyFile` must include `serverAuth` in EKU.

  ```none
  extendedKeyUsage = serverAuth
  ```

- `tlsClusterFile` must include `clientAuth` in EKU:

  ```none
  extendedKeyUsage = clientAuth
  ```

- If `tlsClusterFile` is omitted and only `tlsCertificateKeyFile`
  is configured, then `tlsCertificateKeyFile` must include both
  `serverAuth` and `clientAuth` in EKU:

  ```none
  extendedKeyUsage = clientAuth, serverAuth
  ```

If X.509 certificates used for `tlsCertificateKeyFile` or
`tlsClusterFile` include the Key Usage (KU) extension, set it
as follows:

- `tlsCertificateKeyFile` should contain `digitalSignature`,
  `keyEncipherment`, and `keyAgreement` in its KU extension:

  ```none
  keyUsage = digitalSignature, keyEncipherment, keyAgreement
  ```

- `tlsClusterFile` should contain `digitalSignature` in its
  KU extension:

  ```none
  keyUsage = digitalSignature
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
        mongod --replSet <name> --tlsMode requireTLS --clusterAuthMode x509 --tlsClusterFile <path to membership certificate and key PEM file> --tlsCertificateKeyFile <path to TLS/SSL certificate and key file> --tlsCAFile <path to root CA file> --bind_ip localhost,<hostname(s)|ip address(es)>
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
