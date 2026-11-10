<!-- Converted from user/security/securing-communications/elasticsearch-mutual-tls.asciidoc (AsciiDoc). Includes are inlined. -->

### Mutual TLS authentication between Kibana and Elasticsearch

Secure Sockets Layer (SSL) and Transport Layer Security (TLS) provide encryption
for data-in-transit. While these terms are often used interchangeably, Kibana
supports only TLS, which supersedes the old SSL protocols.

TLS requires X.509 certificates to authenticate the communicating parties and
perform encryption of data-in-transit. Each certificate contains a public key
and has and an associated -- but separate -- private key; these keys are used
for cryptographic operations. Kibana supports certificates and private keys in
PEM or PKCS#12 format.

In a standard TLS configuration, the server presents a signed certificate to
authenticate itself to the client. In a mutual TLS configuration, the client
also presents a signed certificate to authenticate itself to the server.

Elasticsearch security features are enabled on your cluster by default, so each request
that Kibana (the client) makes to Elasticsearch (the server) is authenticated. Most
requests made by end users through Kibana to Elasticsearch are authenticated by using the
credentials of the logged-in user.

To [enroll Kibana with an Elasticsearch cluster](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/configuring-stack-security.html#stack-start-with-security), you pass a generated enrollment token. This token 
configures Kibana to authenticate with Elasticsearch using a
[service account token](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/service-accounts.html#service-accounts-tokens).
Kibana also supports mutual TLS authentication with Elasticsearch via a
[Public Key Infrastructure (PKI) realm](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/pki-realm.html). With this setup,
Elasticsearch needs to verify the signature on the Kibana client certificate, and it also
needs to map the client certificate's distinguished name (DN) to the appropriate
`kibana_system` role.

**Note:** Using a PKI realm is a [subscription feature](https://www.elastic.co/subscriptions).

#### Configure Kibana and Elasticsearch to use mutual TLS authentication

If you haven't already, start Kibana and connect it to Elasticsearch using the
[enrollment token](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/configuring-stack-security.html#stack-start-with-security).

. Obtain a client certificate and private key for Kibana.
Kibana uses the client certificate and corresponding private key when connecting to Elasticsearch.

**Note:** This is not the same as the server certificate that Kibana will present to web browsers.

You may choose to generate a client certificate and private key using the [`elasticsearch-certutil`](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/certutil.html) tool. If you followed the Elasticsearch documentation for [generating the certificates authority](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-basic-setup.html#generate-certificates), then you already have a certificate authority (CA) to sign
the Elasticsearch server certificate. You may choose to use the same CA to sign the Kibana
client certificate. For example:

```sh
bin/elasticsearch-certutil cert -ca elastic-stack-ca.p12 -name kibana-client -dns <your_kibana_hostname>
```

This will generate a client certificate and private key in a PKCS#12 file named `kibana-client.p12`. In this example, the client certificate
has a Common Name (CN) of `"kibana-client"` and a subject alternative name (SAN) of `"<your_kibana_hostname>"`. The SAN may be required if
you have hostname verification enabled on Elasticsearch.

. Obtain the certificate authority (CA) certificate chain for Kibana.
Elasticsearch needs the appropriate CA certificate chain to properly establish trust when receiving connections from Kibana.

If you followed the instructions to generate a client certificate, then you will have a PKCS#12 file for Kibana. You can extract the CA
certificate chain from this file. For example:

```sh
openssl pkcs12 -in kibana-client.p12 -cacerts -nokeys -out kibana-ca.crt
```

This will produce a PEM-formatted file named `kibana-ca.crt` that contains the CA certificate from the PKCS#12 file.

. Configure Elasticsearch with a PKI realm and a native realm.
By default, Elasticsearch provides a native realm for authenticating with a username and password. However, to support both a PKI realm (for Kibana)
and a native realm (for end users), you must configure each realm in `elasticsearch.yml`:

```yaml
xpack.security.authc.realms.pki.realm1.order: 1
xpack.security.authc.realms.pki.realm1.certificate_authorities: "/path/to/kibana-ca.crt"
xpack.security.authc.realms.native.realm2.order: 2
```

. Configure Elasticsearch to request client certificates.
By default, Elasticsearch will not request a client certificate when establishing a TLS connection. To change this, you must set up optional client
certificate authentication in `elasticsearch.yml`:

```yaml
xpack.security.http.ssl.client_authentication: "optional"
```

. Restart Elasticsearch.

. Use Kibana to create a role mapping in Elasticsearch for the client certificate.
This role mapping will assign the `kibana_system` role to any user that matches the included mapping rule, which is set to equal the client
certificate's DN attribute:

image:security/images/mutual-tls-role-mapping.png["Role mapping for the Kibana client certificate"]

For more information, see role mappings.

. Configure Kibana to use the client certificate and private key.
You need to specify the information required to access your client certificate and corresponding private key.

.. If your certificate and private key are contained in a PKCS#12 file:
Specify your PKCS#12 file in `kibana.yml`:

```yaml
elasticsearch.ssl.keystore.path: "/path/to/kibana-client.p12"
```

If your PKCS#12 file is encrypted, add the decryption password to your Kibana keystore:

```yaml
bin/kibana-keystore add elasticsearch.ssl.keystore.password
```

**Tip:** If your PKCS#12 file isn't protected with a password, depending on how it was generated, you may need to set
`elasticsearch.ssl.keystore.password` to an empty string.

.. Otherwise, if your certificate and private key are in PEM format:
Specify your certificate and private key in `kibana.yml`:

```yaml
elasticsearch.ssl.certificate: "/path/to/kibana-client.crt"
elasticsearch.ssl.key: "/path/to/kibana-client.key"
```

If your private key is encrypted, add the decryption password to your Kibana keystore:

```yaml
bin/kibana-keystore add elasticsearch.ssl.keyPassphrase
```

. Configure Kibana _not_ to use a username and password for Elasticsearch.
You must remove the `elasticsearch.username` and `elasticsearch.password` settings from `kibana.yml`. If these are present, Kibana will
attempt to use them to authenticate to Elasticsearch via the native realm.

. Restart Kibana.

These steps enable Kibana to authenticate to Elasticsearch using a certificate. However, end users will only be able to authenticate to
Kibana with a username and password. To allow end users to authenticate to Kibana using a client certificate, see <<pki-authentication,Kibana
PKI authentication>>.
