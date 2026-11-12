<!-- Part 6 of 8 of reference/elasticsearch/configuration-reference/security-settings.md (split because the page is big). -->

## Transport TLS/SSL settings [transport-tls-ssl-settings]

The settings in this section relate to node-to-node transport connections.

By default, Elasticsearch uses mutual TLS (mTLS) to secure node-to-node transport connections within a cluster. With mTLS, data is encrypted in transit and both nodes must present valid certificates when connecting. Each node requires that certificates be issued by a trusted certificate authority, ensuring that only authorized nodes can connect. [Learn about configuring node-to-node mTLS](docs-content://deploy-manage/security/secure-cluster-communications.md#encrypt-internode-communication).

::::{warning}
Transport connections between Elasticsearch nodes are security-critical and you must protect them carefully. Malicious actors who can observe or interfere with unencrypted node-to-node transport traffic can read or modify cluster data. A malicious actor who can establish a transport connection might be able to invoke system-internal APIs, including APIs that read or modify cluster data.
::::

`xpack.security.transport.ssl.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Used to enable or disable TLS/SSL on the transport networking layer, which nodes use to communicate with each other. The default is `false`.

`xpack.security.transport.ssl.supported_protocols`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Supported protocols with versions. Valid protocols: `SSLv2Hello`, `SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. If the JVM’s SSL provider supports TLSv1.3, the default is `TLSv1.3,TLSv1.2,TLSv1.1`. Otherwise, the default is `TLSv1.2,TLSv1.1`.

    Elasticsearch relies on your JDK’s implementation of SSL and TLS. View [Supported SSL/TLS versions by JDK version](docs-content://deploy-manage/security/supported-ssltls-versions-by-jdk-version.md) for more information.

    ::::{note}
    If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello` or `SSLv3`. See [FIPS 140-2](docs-content://deploy-manage/security/fips-140-2.md).
    ::::


`xpack.security.transport.ssl.client_authentication`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Controls the node's behavior in regard to requesting a certificate when accepting an inbound transport connections from another Elasticsearch node. Valid values are `required`, `optional`, and `none`. The default is `required` which means that the connecting node must present a valid client certificate during the connection process. May also be set to `optional` which means that a client certificate is requested but the connecting node may choose not to present one, or `none` which means that no client certificate is even requested during the connection process.

    ::::{warning}
    Turning off mTLS by setting `xpack.security.transport.ssl.client_authentication` to `optional` or `none` allows anyone with network access to establish transport connections. Malicious actors can use these connections to invoke system-internal APIs that might read or modify cluster data. Use mTLS to protect your node-to-node transport connections unless you are absolutely certain that unauthorized network access to these nodes cannot occur.
    ::::

`xpack.security.transport.ssl.verification_mode`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Defines how to verify the certificates presented by another party in the TLS connection:

    Defaults to `full`.

    **Valid values**:
    * `full`:   Validates that the provided certificate: has an issue date that’s within the `not_before` and `not_after` dates; chains to a trusted Certificate Authority (CA); has a `hostname` or IP address that matches the names within the certificate.
    * `certificate`:   Validates the provided certificate and verifies that it’s signed by a trusted authority (CA), but doesn’t check the certificate `hostname`.
    * `none`:   Performs no certificate validation.

      ::::{important}
      Setting certificate validation to `none` disables many security benefits of SSL/TLS, which is very dangerous. Only set this value if instructed by Elastic Support as a temporary diagnostic mechanism when attempting to resolve TLS errors.
      ::::

`xpack.security.transport.ssl.cipher_suites`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Supported cipher suites vary depending on which version of Java you use. For example, for version 12 the default value is `TLS_AES_256_GCM_SHA384`, `TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`, `TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_GCM_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA256`, `TLS_RSA_WITH_AES_128_CBC_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA`, `TLS_RSA_WITH_AES_128_CBC_SHA`.

    For more information, see Oracle’s [Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/11/security/java-cryptography-architecture-jca-reference-guide.html).

`xpack.security.transport.ssl.trust_restrictions.x509_fields` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   Specifies which field(s) from the TLS certificate is used to match for the restricted trust management that is used for remote clusters connections. This should only be set when a self managed cluster can not create certificates that follow the Elastic Cloud pattern. The default value is ["subjectAltName.otherName.commonName"], the Elastic Cloud pattern. "subjectAltName.dnsName" is also supported and can be configured in addition to or in replacement of the default.

`xpack.security.transport.ssl.handshake_timeout` {applies_to}`stack: ga 9.2`
:   Specifies the timeout for a TLS handshake when opening a transport connection. Defaults to `10s`.

### Transport TLS/SSL key and trusted certificate settings [security-transport-tls-ssl-key-trusted-certificate-settings]

The following settings are used to specify a private key, certificate, and the trusted certificates that should be used when communicating over an SSL/TLS connection. A private key and certificate must be configured.


### PEM encoded files [_pem_encoded_files_3]

When using PEM encoded files, use the following settings:

`xpack.security.transport.ssl.key`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Path to a PEM encoded file containing the private key.

    If HTTP client authentication is required, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.


`xpack.security.transport.ssl.key_passphrase`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

    :::{admonition} Deprecated in 7.17.0
    Prefer `ssl.secure_key_passphrase` instead.
    :::

    You cannot use this setting and `ssl.secure_key_passphrase` at the same time.


`xpack.security.transport.ssl.secure_key_passphrase`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

`xpack.security.transport.ssl.certificate`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the path for the PEM encoded certificate (or certificate chain) that is associated with the key.

    This setting can be used only if `ssl.key` is set.


`xpack.security.transport.ssl.certificate_authorities`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) List of paths to PEM encoded certificate files that should be trusted.

    This setting and `ssl.truststore.path` cannot be used at the same time.

`xpack.security.loginAssistanceMessage` ![logo cloud](https://doc-icons.s3.us-east-2.amazonaws.com/logo_cloud.svg "Supported on Elastic Cloud Hosted")
:   Adds a message to the login screen. Useful for displaying corporate messages.


### Java keystore files [_java_keystore_files_3]

When using Java keystore files (JKS), which contain the private key, certificate and certificates that should be trusted, use the following settings:

`xpack.security.transport.ssl.keystore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


`xpack.security.transport.ssl.keystore.password`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The password for the keystore.

    :::{admonition} Deprecated in 7.17.0
    Prefer `ssl.keystore.secure_password` instead.
    :::

`xpack.security.transport.ssl.keystore.secure_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The password for the keystore.

`xpack.security.transport.ssl.keystore.key_password`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The password for the key in the keystore. The default is the keystore password.

    :::{admonition} Deprecated in 7.17.0
    Prefer `ssl.keystore.secure_key_password` instead.
    :::

    You cannot use this setting and `ssl.keystore.secure_password` at the same time.


`xpack.security.transport.ssl.keystore.secure_key_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

`xpack.security.transport.ssl.truststore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


`xpack.security.transport.ssl.truststore.password`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The password for the truststore.

    :::{admonition} Deprecated in 7.17.0
    Prefer `ssl.truststore.secure_password` instead.
    :::

    You cannot use this setting and `ssl.truststore.secure_password` at the same time.


`xpack.security.transport.ssl.truststore.secure_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) Password for the truststore.


### PKCS#12 files [security-transport-pkcs12-files]

Elasticsearch can be configured to use PKCS#12 container files (`.p12` or `.pfx` files) that contain the private key, certificate and certificates that should be trusted.

PKCS#12 files are configured in the same way as Java keystore files:

`xpack.security.transport.ssl.keystore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


`xpack.security.transport.ssl.keystore.type`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The format of the keystore file. It must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

`xpack.security.transport.ssl.keystore.password`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The password for the keystore.

    :::{admonition} Deprecated in 7.17.0
    Prefer `ssl.keystore.secure_password` instead.
    :::

`xpack.security.transport.ssl.keystore.secure_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The password for the keystore.

`xpack.security.transport.ssl.keystore.key_password`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The password for the key in the keystore. The default is the keystore password.

    :::{admonition} Deprecated in 7.17.0
    Prefer `ssl.keystore.secure_key_password` instead.
    :::

    You cannot use this setting and `ssl.keystore.secure_password` at the same time.


`xpack.security.transport.ssl.keystore.secure_key_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

`xpack.security.transport.ssl.truststore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


`xpack.security.transport.ssl.truststore.type`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Set this to `PKCS12` to indicate that the truststore is a PKCS#12 file.

`xpack.security.transport.ssl.truststore.password`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The password for the truststore.

    :::{admonition} Deprecated in 7.17.0
    Prefer `ssl.truststore.secure_password` instead.
    :::

    You cannot use this setting and `ssl.truststore.secure_password` at the same time.


`xpack.security.transport.ssl.truststore.secure_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) Password for the truststore.
