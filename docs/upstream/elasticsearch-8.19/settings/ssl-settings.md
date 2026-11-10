<!-- Converted from settings/ssl-settings.asciidoc (AsciiDoc). Includes are inlined. -->

#### {component} TLS/SSL settings

You can configure the following TLS/SSL settings.

{ssl-prefix}.ssl.enabled::
(Static)
Used to enable or disable TLS/SSL on the {ssl-layer}.
The default is `true`.
The default is `false`.

{ssl-prefix}.ssl.supported_protocols::
(Static)
Supported protocols with versions. Valid protocols: `SSLv2Hello`,
`SSLv3`, `TLSv1`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`. If the JVM's SSL provider supports TLSv1.3,
the default is `TLSv1.3,TLSv1.2,TLSv1.1`. Otherwise, the default is
`TLSv1.2,TLSv1.1`.
Elasticsearch relies on your JDK’s implementation of SSL and TLS.
View jdk-tls-versions for more information.
**Note:** If `xpack.security.fips_mode.enabled` is `true`, you cannot use `SSLv2Hello`
or `SSLv3`. See fips-140-compliance.

{ssl-prefix}.ssl.client_authentication::
(Static)
Controls the server's behavior in regard to requesting a certificate
from client connections. Valid values are `required`, `optional`, and `none`.
`required` forces a client to present a certificate, while `optional`
requests a client certificate but the client is not required to present one.
Defaults to `required`.
Defaults to {client-auth-default}.

{ssl-prefix}.ssl.verification_mode::
(Static)
The SSL settings in `pass:a[{ssl-prefix}.ssl]` control a _server context_ for TLS, which
defines the settings for the TLS connection. The use of `verification_mode` in
a TLS _server_ is discouraged.
Defines how to verify the certificates presented by another party in the TLS
connection:
**Valid values**
=====
`full`::
Validates that the provided certificate: has an issue date that's
within the `not_before` and `not_after` dates; chains to a trusted Certificate
Authority (CA); has a `hostname` or IP address that matches the names within
the certificate.

`certificate`::
Validates the provided certificate and verifies that it's signed by a
trusted authority (CA), but doesn't check the certificate `hostname`.

`none`::
Performs no certificate validation.
**Important:** Setting certificate validation to `none` disables many security
benefits of SSL/TLS, which is very dangerous. Only set this value if instructed
by Elastic Support as a temporary diagnostic mechanism when attempting to
resolve TLS errors.
=====
Defaults to `full`.
{ssl-prefix}.ssl.cipher_suites::
(Static)
Supported cipher suites vary depending on which version of Java you use. For
example, for version 12 the default value is `TLS_AES_256_GCM_SHA384`,
`TLS_AES_128_GCM_SHA256`, `TLS_CHACHA20_POLY1305_SHA256`,
`TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`,
`TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`,
`TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`,
`TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`,
`TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`,
`TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`,
`TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA`, `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`,
`TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_GCM_SHA256`,
`TLS_RSA_WITH_AES_256_CBC_SHA256`, `TLS_RSA_WITH_AES_128_CBC_SHA256`,
`TLS_RSA_WITH_AES_256_CBC_SHA`, `TLS_RSA_WITH_AES_128_CBC_SHA`.
For more information, see Oracle's
[Java Cryptography Architecture documentation](https://docs.oracle.com/en/java/javase/11/security/oracle-providers.html#GUID-7093246A-31A3-4304-AC5F-5FB6400405E2).

##### {component} TLS/SSL key and trusted certificate settings

The following settings are used to specify a private key, certificate, and the
trusted certificates that should be used when communicating over an SSL/TLS connection.
A private key and certificate must be configured.
A private key and certificate are optional and would be used if the server requires client authentication for PKI
authentication.

##### PEM encoded files

When using PEM encoded files, use the following settings:

{ssl-prefix}.ssl.key::
(Static)
Path to a PEM encoded file containing the private key.
If HTTP client authentication is required, it uses this file. You cannot use
this setting and `ssl.keystore.path` at the same time.
{ssl-prefix}.ssl.key_passphrase::
(Static)
The passphrase that is used to decrypt the private key. Since the key might not
be encrypted, this value is optional. deprecated:[7.17.0] Prefer `ssl.secure_key_passphrase` instead.
You cannot use this setting and `ssl.secure_key_passphrase` at the same time.

{ssl-prefix}.ssl.secure_key_passphrase::
(Secure)
The passphrase that is used to decrypt the private key. Since the key might not
be encrypted, this value is optional.
{ssl-prefix}.ssl.certificate::
(Static)
Specifies the path for the PEM encoded certificate (or certificate chain) that is
associated with the key.
This setting can be used only if `ssl.key` is set.
{ssl-prefix}.ssl.certificate_authorities::
(Static)
List of paths to PEM encoded certificate files that should be trusted.
This setting and `ssl.truststore.path` cannot be used at the same time.

##### Java keystore files

When using Java keystore files (JKS), which contain the private key, certificate
and certificates that should be trusted, use the following settings:

{ssl-prefix}.ssl.keystore.path::
(Static)
The path for the keystore file that contains a private key and certificate.
It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this
setting and `ssl.key` at the same time.
{ssl-prefix}.ssl.keystore.password::
(Static)
The password for the keystore. deprecated:[7.17.0] Prefer `ssl.keystore.secure_password` instead.

{ssl-prefix}.ssl.keystore.secure_password::
(Secure)
The password for the keystore.
{ssl-prefix}.ssl.keystore.key_password::
(Static)
The password for the key in the keystore. The default is the keystore password.
deprecated:[7.17.0] Prefer `ssl.keystore.secure_key_password` instead.
You cannot use this setting and `ssl.keystore.secure_password` at the same time.

{ssl-prefix}.ssl.keystore.secure_key_password::
(Secure)
The password for the key in the keystore. The default is the keystore password.
{ssl-prefix}.ssl.truststore.path::
(Static)
The path for the keystore that contains the certificates to trust. It must be
either a Java keystore (jks) or a PKCS#12 file.
You cannot use this setting and `ssl.certificate_authorities` at the same time.
{ssl-prefix}.ssl.truststore.password::
(Static)
The password for the truststore. deprecated:[7.17.0] Prefer `ssl.truststore.secure_password` instead.
You cannot use this setting and `ssl.truststore.secure_password` at the same
time.

{ssl-prefix}.ssl.truststore.secure_password::
(Secure)
Password for the truststore.

##### PKCS#12 files

Elasticsearch can be configured to use PKCS#12 container files (`.p12` or `.pfx` files)
that contain the private key, certificate and certificates that should be trusted.

PKCS#12 files are configured in the same way as Java keystore files:

{ssl-prefix}.ssl.keystore.path::
(Static)
The path for the keystore file that contains a private key and certificate.
It must be either a Java keystore (jks) or a PKCS#12 file. You cannot use this
setting and `ssl.key` at the same time.
{ssl-prefix}.ssl.keystore.type::
(Static)
The format of the keystore file. It must be either `jks` or `PKCS12`. If the
keystore path ends in ".p12", ".pfx", or ".pkcs12", this setting defaults
to `PKCS12`. Otherwise, it defaults to `jks`.
{ssl-prefix}.ssl.keystore.password::
(Static)
The password for the keystore. deprecated:[7.17.0] Prefer `ssl.keystore.secure_password` instead.

{ssl-prefix}.ssl.keystore.secure_password::
(Secure)
The password for the keystore.
{ssl-prefix}.ssl.keystore.key_password::
(Static)
The password for the key in the keystore. The default is the keystore password.
deprecated:[7.17.0] Prefer `ssl.keystore.secure_key_password` instead.
You cannot use this setting and `ssl.keystore.secure_password` at the same time.

{ssl-prefix}.ssl.keystore.secure_key_password::
(Secure)
The password for the key in the keystore. The default is the keystore password.
{ssl-prefix}.ssl.truststore.path::
(Static)
The path for the keystore that contains the certificates to trust. It must be
either a Java keystore (jks) or a PKCS#12 file.
You cannot use this setting and `ssl.certificate_authorities` at the same time.
{ssl-prefix}.ssl.truststore.type::
(Static)
Set this to `PKCS12` to indicate that the truststore is a PKCS#12 file.

{ssl-prefix}.ssl.truststore.password::
(Static)
The password for the truststore. deprecated:[7.17.0] Prefer `ssl.truststore.secure_password` instead.
You cannot use this setting and `ssl.truststore.secure_password` at the same
time.

{ssl-prefix}.ssl.truststore.secure_password::
(Secure)
Password for the truststore.
