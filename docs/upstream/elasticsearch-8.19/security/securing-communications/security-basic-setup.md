<!-- Converted from security/securing-communications/security-basic-setup.asciidoc (AsciiDoc). Includes are inlined. -->

### Set up basic security for the Elastic Stack

When you start Elasticsearch for the first time, passwords are generated for the `elastic`
user and TLS is automatically configured for you. If you configure security 
manually _before_ starting your Elasticsearch nodes, the auto-configuration process will 
respect your security configuration. You can adjust your TLS configuration at 
any time, such as updating node certificates.

**Important:** If your cluster has multiple nodes, then you must configure
TLS between nodes. Production mode clusters will not start
if you do not enable TLS.

The transport layer relies on mutual TLS for both encryption and
authentication of nodes. Correctly applying TLS ensures that a malicious node
cannot join the cluster and exchange data with other nodes. While implementing
username and password authentication at the HTTP layer is useful for securing a
local cluster, the security of communication between nodes requires TLS.

Configuring TLS between nodes is the basic security setup to prevent
unauthorized nodes from accessing to your cluster.

**Understanding transport contexts**
****
Transport Layer Security (TLS) is the name of an industry standard protocol for
applying security controls (such as encryption) to network communications. TLS
is the modern name for what used to be called Secure Sockets Layer (SSL). The
Elasticsearch documentation uses the terms TLS and SSL interchangeably.

Transport Protocol is the name of the protocol that Elasticsearch nodes use to
communicate with one another. This name is specific to Elasticsearch and distinguishes
the transport port (default `9300`) from the HTTP port (default `9200`). Nodes
communicate with one another using the transport port, and REST clients
communicate with Elasticsearch using the HTTP port.

Although the word _transport_ appears in both contexts, they mean different
things. It's possible to apply TLS to both the Elasticsearch transport port and the HTTP
port. We know that these overlapping terms can be confusing, so to clarify, in
this scenario we're applying TLS to the Elasticsearch transport port. In
the next scenario, we'll apply TLS to the Elasticsearch
HTTP port.
****

#### Generate the certificate authority

You can add as many nodes as you want in a cluster but they must be able to
communicate with each other. The communication between nodes in a cluster is
handled by the transport module. To secure your cluster, you must ensure that
internode communications are encrypted and verified, which is achieved with
mutual TLS.

In a secured cluster, Elasticsearch nodes use certificates to identify
themselves when communicating with other nodes.

The cluster must validate the authenticity of these certificates. The
recommended approach is to trust a specific certificate authority (CA). When
nodes are added to your cluster they must use a certificate signed by the same
CA.

For the transport layer, we recommend using a separate, dedicated CA instead
of an existing, possibly shared CA so that node membership is tightly controlled. Use the `elasticsearch-certutil` tool to
generate a CA for your cluster.

. Before starting Elasticsearch, use the `elasticsearch-certutil` tool on any single node
to generate a CA for your cluster.
```shell
./bin/elasticsearch-certutil ca
```

   a. When prompted, accept the default file name, which is `elastic-stack-ca.p12`. This file contains the public certificate for your CA and the private key used to sign certificates for each node.

   b. Enter a password for your CA. You can choose to leave the password blank
   if you're not deploying to a production environment.

. On any single node, generate a certificate and private key for the nodes in
your cluster. You include the `elastic-stack-ca.p12` output file that you
generated in the previous step.
```shell
./bin/elasticsearch-certutil cert --ca elastic-stack-ca.p12
```
   `--ca <ca_file>`:: Name of the CA file used to sign your certificates. The
   default file name from the `elasticsearch-certutil` tool is `elastic-stack-ca.p12`.

   a. Enter the password for your CA, or press *Enter* if you did not configure one in the previous step.

   b. Create a password for the certificate and accept the default file name.
The output file is a keystore named `elastic-certificates.p12`. This file
contains a node certificate, node key, and CA certificate.

. On *every* node in your cluster, copy the `elastic-certificates.p12` file to
the `$ES_PATH_CONF` directory.

#### Encrypt internode communications with TLS

The transport networking layer is used for internal communication between
nodes in a cluster. When security features are enabled, you must use TLS to
ensure that communication between the nodes is encrypted.

Now that you've generated a certificate authority and certificates, you'll
update your cluster to use these files.

**Note:** Elasticsearch monitors all files such as certificates, keys, keystores, or
truststores that are configured as values of TLS-related node settings. If
you update any of these files, such as when your hostnames change or your
certificates are due to expire, Elasticsearch reloads them. The files are polled for
changes at a frequency determined by the global Elasticsearch
`resource.reload.interval.high` setting, which defaults to 5 seconds.

Complete the following steps *for each node in your cluster*. To join the
same cluster, all nodes must share the same `cluster.name` value.

. Open the `$ES_PATH_CONF/elasticsearch.yml` file and make the following
changes:

   a. Add the `cluster-name` setting and enter a name for your cluster:
```yaml
cluster.name: my-cluster
```

b. Add the `node.name` setting and enter a name for the node.
The node name defaults to the hostname of the machine when Elasticsearch starts. 
```yaml
node.name: node-1
```

c. Add the following settings to enable internode communication and provide
access to the node's certificate.
Because you are using the same `elastic-certificates.p12` file on every node in
your cluster, set the verification mode to `certificate`:
```yaml
xpack.security.transport.ssl.enabled: true
xpack.security.transport.ssl.verification_mode: certificate <1>
xpack.security.transport.ssl.client_authentication: required
xpack.security.transport.ssl.keystore.path: elastic-certificates.p12
xpack.security.transport.ssl.truststore.path: elastic-certificates.p12
```
<1> If you want to use hostname verification, set the verification mode to
`full`. You should generate a different certificate for each host that
matches the DNS or IP address. See the 
`xpack.security.transport.ssl.verification_mode` parameter in [TLS settings](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-settings.html#transport-tls-ssl-settings).

. If you entered a password when creating the node certificate, run the following commands to store the password in the Elasticsearch keystore:
```shell
./bin/elasticsearch-keystore add xpack.security.transport.ssl.keystore.secure_password
```

```shell
./bin/elasticsearch-keystore add xpack.security.transport.ssl.truststore.secure_password
```

. Complete the previous steps for each node in your cluster.

. On *every* node in your cluster, start Elasticsearch. The method for
starting and stopping Elasticsearch
varies depending on how you installed it.
For example, if you installed Elasticsearch with an archive distribution
(`tar.gz` or `.zip`), you can enter `Ctrl+C` on the command line to stop
Elasticsearch.
**Warning:** You must perform a full cluster restart. Nodes that are configured to
use TLS for transport cannot communicate with nodes that use unencrypted transport connection (and vice-versa).

#### What's next?

Congratulations! You've encrypted communications between the nodes in your
cluster and can pass the
TLS bootstrap check.

To add another layer of security, Set up basic security for the Elastic Stack plus secured HTTPS traffic. In addition to
configuring TLS on the transport interface of your Elasticsearch cluster, you configure
TLS on the HTTP interface for both Elasticsearch and Kibana.
