<!-- Converted from setup/install/security-files-reference.asciidoc (AsciiDoc). Includes are inlined. -->

##### Security certificates and keys

When you install Elasticsearch, the following certificates and keys are
generated in the Elasticsearch configuration directory, which are used to connect a Kibana
instance to your secured Elasticsearch cluster and to encrypt internode communication.
The files are listed here for reference.

`http_ca.crt`::
The CA certificate that is used to sign the certificates for the HTTP layer of
this Elasticsearch cluster.

`http.p12`::
Keystore that contains the key and certificate for the HTTP layer for this node.

`transport.p12`::
Keystore that contains the key and certificate for the transport layer for all
the nodes in your cluster.

`http.p12` and `transport.p12` are password-protected PKCS#12 keystores. Elasticsearch
stores the passwords for these keystores as <<secure-settings,secure
settings>>. To retrieve the passwords so that you can inspect or change the
keystore contents, use the
`bin/elasticsearch-keystore` tool.

Use the following command to retrieve the password for `http.p12`:
```sh
bin/elasticsearch-keystore show xpack.security.http.ssl.keystore.secure_password
```

Use the following command to retrieve the password for `transport.p12`:
```sh
bin/elasticsearch-keystore show xpack.security.transport.ssl.keystore.secure_password
```
