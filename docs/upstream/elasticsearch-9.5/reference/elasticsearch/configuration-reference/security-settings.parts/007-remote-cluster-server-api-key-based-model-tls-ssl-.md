<!-- Part 7 of 8 of reference/elasticsearch/configuration-reference/security-settings.md (split because the page is big). -->

## Remote cluster server (API key based model) TLS/SSL settings [remote-cluster-server-tls-ssl-settings]

You can configure the following TLS/SSL settings.

`xpack.security.remote_cluster_server.ssl.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Used to enable or disable TLS/SSL on the remote cluster server networking layer, which Elasticsearch uses to communicate with remote cluster clients. The default is `true`.

`xpack.security.remote_cluster_server.ssl.supported_protocols`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Supported protocols with versions. Valid protocols: `SSLv2Hello`, `SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. If the JVM’s SSL provider supports TLSv1.3, the default is `TLSv1.3,TLSv1.2,TLSv1.1`. Otherwise, the default is `TLSv1.2,TLSv1.1`.

    Elasticsearch relies on your JDK’s implementation of SSL and TLS. View [Supported SSL/TLS versions by JDK version](docs-content://deploy-manage/security/supported-ssltls-versions-by-jdk-version.md) for more information.

    ::::{note}
    If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello` or `SSLv3`. See [FIPS 140-2](docs-content://deploy-manage/security/fips-140-2.md).
    ::::


`xpack.security.remote_cluster_server.ssl.client_authentication`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Controls the server’s behavior in regard to requesting a certificate from client connections. Valid values are `required`, `optional`, and `none`. `required` forces a client to present a certificate, while `optional` requests a client certificate but the client is not required to present one. Defaults to `none`.

`xpack.security.remote_cluster_server.ssl.verification_mode`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The SSL settings in `xpack.security.remote_cluster_server.ssl` control a *server context* for TLS, which defines the settings for the TLS connection. The use of `verification_mode` in a TLS *server* is discouraged. Defines how to verify the certificates presented by another party in the TLS connection:

    Defaults to `full`.

    **Valid values**:
    * `full`:   Validates that the provided certificate: has an issue date that’s within the `not_before` and `not_after` dates; chains to a trusted Certificate Authority (CA); has a `hostname` or IP address that matches the names within the certificate.
    * `certificate`:   Validates the provided certificate and verifies that it’s signed by a trusted authority (CA), but doesn’t check the certificate `hostname`.
    * `none`:   Performs no certificate validation.

      ::::{important}
      Setting certificate validation to `none` disables many security benefits of SSL/TLS, which is very dangerous. Only set this value if instructed by Elastic Support as a temporary diagnostic mechanism when attempting to resolve TLS errors.
      ::::

`xpack.security.remote_cluster_server.ssl.cipher_suites`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Supported cipher suites vary depending on which version of Java you use. For example, for version 12 the default value is `TLS_AES_256_GCM_SHA384`, `TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`, `TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_GCM_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA256`, `TLS_RSA_WITH_AES_128_CBC_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA`, `TLS_RSA_WITH_AES_128_CBC_SHA`.

    For more information, see Oracle’s [Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/11/security/java-cryptography-architecture-jca-reference-guide.html).

`xpack.security.remote_cluster_server.ssl.handshake_timeout` {applies_to}`stack: ga 9.2`
:   Specifies the timeout for a TLS handshake when handling an inbound remote-cluster connection. Defaults to `10s`.


### Remote cluster server (API key based model) TLS/SSL key and trusted certificate settings [security-remote-cluster-server-tls-ssl-key-trusted-certificate-settings]

The following settings are used to specify a private key, certificate, and the trusted certificates that should be used when communicating over an SSL/TLS connection. A private key and certificate must be configured.


### PEM encoded files [_pem_encoded_files_4]

When using PEM encoded files, use the following settings:

`xpack.security.remote_cluster_server.ssl.key`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Path to a PEM encoded file containing the private key.

    If HTTP client authentication is required, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.


`xpack.security.remote_cluster_server.ssl.secure_key_passphrase`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

`xpack.security.remote_cluster_server.ssl.certificate`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the path for the PEM encoded certificate (or certificate chain) that is associated with the key.

    This setting can be used only if `ssl.key` is set.


`xpack.security.remote_cluster_server.ssl.certificate_authorities`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) List of paths to PEM encoded certificate files that should be trusted.

    This setting and `ssl.truststore.path` cannot be used at the same time.



### Java keystore files [_java_keystore_files_4]

When using Java keystore files (JKS), which contain the private key, certificate and certificates that should be trusted, use the following settings:

`xpack.security.remote_cluster_server.ssl.keystore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


`xpack.security.remote_cluster_server.ssl.keystore.secure_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The password for the keystore.

`xpack.security.remote_cluster_server.ssl.keystore.secure_key_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

`xpack.security.remote_cluster_server.ssl.truststore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


`xpack.security.remote_cluster_server.ssl.truststore.secure_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) Password for the truststore.


### PKCS#12 files [security-remote-cluster-server-pkcs12-files]

Elasticsearch can be configured to use PKCS#12 container files (`.p12` or `.pfx` files) that contain the private key, certificate and certificates that should be trusted.

PKCS#12 files are configured in the same way as Java keystore files:

`xpack.security.remote_cluster_server.ssl.keystore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


`xpack.security.remote_cluster_server.ssl.keystore.type`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The format of the keystore file. It must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

`xpack.security.remote_cluster_server.ssl.keystore.secure_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The password for the keystore.

`xpack.security.remote_cluster_server.ssl.keystore.secure_key_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

`xpack.security.remote_cluster_server.ssl.truststore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


`xpack.security.remote_cluster_server.ssl.truststore.type`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Set this to `PKCS12` to indicate that the truststore is a PKCS#12 file.

`xpack.security.remote_cluster_server.ssl.truststore.secure_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) Password for the truststore.




## Remote cluster client (API key based model) TLS/SSL settings [remote-cluster-client-tls-ssl-settings]

You can configure the following TLS/SSL settings.

`xpack.security.remote_cluster_client.ssl.enabled`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Used to enable or disable TLS/SSL on the remote cluster client networking layer, which Elasticsearch uses to communicate with remote cluster servers. The default is `true`.

`xpack.security.remote_cluster_client.ssl.supported_protocols`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Supported protocols with versions. Valid protocols: `SSLv2Hello`, `SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. If the JVM’s SSL provider supports TLSv1.3, the default is `TLSv1.3,TLSv1.2,TLSv1.1`. Otherwise, the default is `TLSv1.2,TLSv1.1`.

    Elasticsearch relies on your JDK’s implementation of SSL and TLS. View [Supported SSL/TLS versions by JDK version](docs-content://deploy-manage/security/supported-ssltls-versions-by-jdk-version.md) for more information.

    ::::{note}
    If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello` or `SSLv3`. See [FIPS 140-2](docs-content://deploy-manage/security/fips-140-2.md).
    ::::


`xpack.security.remote_cluster_client.ssl.verification_mode`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Defines how to verify the certificates presented by another party in the TLS connection:

    Defaults to `full`.

    **Valid values**:
    * `full`:   Validates that the provided certificate: has an issue date that’s within the `not_before` and `not_after` dates; chains to a trusted Certificate Authority (CA); has a `hostname` or IP address that matches the names within the certificate.
    * `certificate`:   Validates the provided certificate and verifies that it’s signed by a trusted authority (CA), but doesn’t check the certificate `hostname`.
    * `none`:   Performs no certificate validation.

      ::::{important}
      Setting certificate validation to `none` disables many security benefits of SSL/TLS, which is very dangerous. Only set this value if instructed by Elastic Support as a temporary diagnostic mechanism when attempting to resolve TLS errors.
      ::::

`xpack.security.remote_cluster_client.ssl.cipher_suites`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Supported cipher suites vary depending on which version of Java you use. For example, for version 12 the default value is `TLS_AES_256_GCM_SHA384`, `TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`, `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`, `TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_GCM_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA256`, `TLS_RSA_WITH_AES_128_CBC_SHA256`, `TLS_RSA_WITH_AES_256_CBC_SHA`, `TLS_RSA_WITH_AES_128_CBC_SHA`.

    For more information, see Oracle’s [Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/11/security/java-cryptography-architecture-jca-reference-guide.html).

`xpack.security.remote_cluster_client.ssl.handshake_timeout` {applies_to}`stack: ga 9.2`
:   Specifies the timeout for a TLS handshake when opening a remote-cluster connection. Defaults to `10s`.


### Remote cluster client (API key based model) TLS/SSL key and trusted certificate settings [security-remote-cluster-client-tls-ssl-key-trusted-certificate-settings]

The following settings are used to specify a private key, certificate, and the trusted certificates that should be used when communicating over an SSL/TLS connection. A private key and certificate are optional and would be used if the server requires client authentication for PKI authentication.


### PEM encoded files [_pem_encoded_files_5]

When using PEM encoded files, use the following settings:

`xpack.security.remote_cluster_client.ssl.key`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Path to a PEM encoded file containing the private key.

    If HTTP client authentication is required, it uses this file. You cannot use this setting and `ssl.keystore.path` at the same time.


`xpack.security.remote_cluster_client.ssl.secure_key_passphrase`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The passphrase that is used to decrypt the private key. Since the key might not be encrypted, this value is optional.

`xpack.security.remote_cluster_client.ssl.certificate`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Specifies the path for the PEM encoded certificate (or certificate chain) that is associated with the key.

    This setting can be used only if `ssl.key` is set.


`xpack.security.remote_cluster_client.ssl.certificate_authorities`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) List of paths to PEM encoded certificate files that should be trusted.

    This setting and `ssl.truststore.path` cannot be used at the same time.



### Java keystore files [_java_keystore_files_5]

When using Java keystore files (JKS), which contain the private key, certificate and certificates that should be trusted, use the following settings:

`xpack.security.remote_cluster_client.ssl.keystore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


`xpack.security.remote_cluster_client.ssl.keystore.secure_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The password for the keystore.

`xpack.security.remote_cluster_client.ssl.keystore.secure_key_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

`xpack.security.remote_cluster_client.ssl.truststore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


`xpack.security.remote_cluster_client.ssl.truststore.secure_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) Password for the truststore.


### PKCS#12 files [security-remote-cluster-client-pkcs12-files]

Elasticsearch can be configured to use PKCS#12 container files (`.p12` or `.pfx` files) that contain the private key, certificate and certificates that should be trusted.

PKCS#12 files are configured in the same way as Java keystore files:

`xpack.security.remote_cluster_client.ssl.keystore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path for the keystore file that contains a private key and certificate.

    It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this setting and `ssl.key` at the same time.


`xpack.security.remote_cluster_client.ssl.keystore.type`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The format of the keystore file. It must be either `jks` or `PKCS12`. If the keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults to `PKCS12`. Otherwise, it defaults to `jks`.

`xpack.security.remote_cluster_client.ssl.keystore.secure_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The password for the keystore.

`xpack.security.remote_cluster_client.ssl.keystore.secure_key_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) The password for the key in the keystore. The default is the keystore password.

`xpack.security.remote_cluster_client.ssl.truststore.path`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) The path for the keystore that contains the certificates to trust. It must be either a Java keystore (jks) or a PKCS#12 file.

    You cannot use this setting and `ssl.certificate_authorities` at the same time.


`xpack.security.remote_cluster_client.ssl.truststore.type`
:   ([Static](docs-content://deploy-manage/stack-settings.md#static-cluster-setting)) Set this to `PKCS12` to indicate that the truststore is a PKCS#12 file.

`xpack.security.remote_cluster_client.ssl.truststore.secure_password`
:   ([Secure](docs-content://deploy-manage/security/secure-settings.md)) Password for the truststore.


#### Transport profile TLS/SSL settings [ssl-tls-profile-settings]

The same settings that are available for the [default transport](#transport-tls-ssl-settings) are also available for each transport profile. By default, the settings for a transport profile will be the same as the default transport unless they are specified.

As an example, lets look at the key setting. For the default transport this is `xpack.security.transport.ssl.key`. In order to use this setting in a transport profile, use the prefix `transport.profiles.$PROFILE.xpack.security.` and append the portion of the setting after `xpack.security.transport.`. For the key setting, this would be `transport.profiles.$PROFILE.xpack.security.ssl.key`.
