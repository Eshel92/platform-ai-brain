<!-- Converted from security/authentication/pki-realm.asciidoc (AsciiDoc). Includes are inlined. -->

### PKI user authentication

You can configure Elasticsearch to use Public Key Infrastructure (PKI) certificates to
authenticate users. In this scenario, clients connecting directly to Elasticsearch must
present X.509 certificates. First, the certificates must be accepted for
authentication on the SSL/TLS layer on Elasticsearch. Then they are optionally
further validated by a PKI realm. See pki-realm-for-direct-clients.

You can also use PKI certificates to authenticate to Kibana, however this
requires some additional configuration. On Elasticsearch, this configuration enables Kibana 
to act as a proxy for SSL/TLS authentication and to submit the client
certificates to Elasticsearch for further validation by a PKI realm. See
pki-realm-for-proxied-clients.

(See `security/authentication/configuring-pki-realm.md`)
