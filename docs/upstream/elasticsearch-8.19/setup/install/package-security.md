<!-- Converted from setup/install/package-security.asciidoc (AsciiDoc). Includes are inlined. -->

#### Start Elasticsearch with security enabled

When installing Elasticsearch, security features are enabled and configured by default.
When you install Elasticsearch, the following security configuration
occurs automatically:

* Authentication and authorization are enabled, and a password is generated for
the `elastic` built-in superuser.
* Certificates and keys for TLS are generated for the transport and HTTP layer,
and TLS is enabled and configured with these keys and certificates.

The password and certificate and keys are output to your terminal.
You can reset the password for the `elastic` user with the `elasticsearch-reset-password` command.

We recommend storing the `elastic` password as an environment variable in your shell. For example:

```sh
export ELASTIC_PASSWORD="your_password"
```

##### Reconfigure a node to join an existing cluster

When you install Elasticsearch, the installation process configures a
single-node cluster by default. If you want a node to join an existing cluster
instead, generate an enrollment token on an existing node _before_ you start
the new node for the first time.

. On any node in your existing cluster, generate a node enrollment token:
```sh
/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s node
```

. Copy the enrollment token, which is output to your terminal.

. On your new Elasticsearch node, pass the enrollment token as a parameter to the
`elasticsearch-reconfigure-node` tool:
```sh
/usr/share/elasticsearch/bin/elasticsearch-reconfigure-node --enrollment-token <enrollment-token>
```
Elasticsearch is now configured to join the existing cluster.

. Start your new node using `systemd`.
