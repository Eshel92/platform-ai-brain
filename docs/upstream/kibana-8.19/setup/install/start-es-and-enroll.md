<!-- Converted from setup/install/start-es-and-enroll.asciidoc (AsciiDoc). Includes are inlined. -->

#### Start Elasticsearch and generate an enrollment token for Kibana

When you start Elasticsearch for the first time, the following security configuration
occurs automatically:

* [Certificates and keys](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/configuring-stack-security.html#stack-security-certificates) for TLS are
generated for the transport and HTTP layers.
* The TLS configuration settings are written to `elasticsearch.yml`.
* A password is generated for the `elastic` user.
* An enrollment token is generated for Kibana.

You can then start Kibana and enter the enrollment token to securely connect 
Kibana with Elasticsearch. The enrollment token is valid for 30 minutes.
