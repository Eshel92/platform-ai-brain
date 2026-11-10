<!-- Converted from setup/install/zip-windows-start.asciidoc (AsciiDoc). Includes are inlined. -->

#### Run Elasticsearch from the command line

Run the following command to start Elasticsearch from the command line:

```sh
.\bin\elasticsearch.bat
```

When starting Elasticsearch for the first time, security features are enabled and
configured by default. The following security configuration occurs
automatically: 

* Authentication and authorization are enabled, and a password is generated for
the `elastic` built-in superuser.
* Certificates and keys for TLS are generated for the transport and HTTP layer,
and TLS is enabled and configured with these keys and certificates.
* An enrollment token is generated for Kibana, which is valid for 30 minutes.

The password for the `elastic` user and the enrollment token for Kibana are
output to your terminal.

We recommend storing the `elastic` password as an environment variable in your shell. Example:

```sh
$ELASTIC_PASSWORD = "your_password"
```

If you have password-protected the Elasticsearch keystore, you will be prompted to
enter the keystore's password. See secure-settings for more details.

By default Elasticsearch prints its logs to the console (`STDOUT`) and to the `<cluster
name>.log` file within the logs directory. Elasticsearch logs some
information while it is starting, but after it has finished initializing it
will continue to run in the foreground and won't log anything further until
something happens that is worth recording. While Elasticsearch is running you can
interact with it through its HTTP interface which is on port `9200` by default.

To stop Elasticsearch, press `Ctrl-C`.

#### Enroll nodes in an existing cluster

When Elasticsearch starts for the first time, the security auto-configuration process
binds the HTTP layer to `0.0.0.0`, but only binds the transport layer to
localhost. This intended behavior ensures that you can start
a single-node cluster with security enabled by default without any additional
configuration.

Before enrolling a new node, additional actions such as binding to an address
other than `localhost` or satisfying bootstrap checks are typically necessary
in production clusters. During that time, an auto-generated enrollment token
could expire, which is why enrollment tokens aren't generated automatically.

Additionally, only nodes on the same host can join the cluster without
additional configuration. If you want nodes from another host to join your
cluster, you need to set `transport.host` to a
[supported value](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/modules-network.html#network-interface-values)
(such as uncommenting the suggested value of `0.0.0.0`), or an IP address
that's bound to an interface where other hosts can reach it. Refer to
[transport settings](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/modules-network.html#transport-settings) for more
information.

To enroll new nodes in your cluster, create an enrollment token with the
`elasticsearch-create-enrollment-token` tool on any existing node in your
cluster. You can then start a new node with the `--enrollment-token` parameter
so that it joins an existing cluster.

. In a separate terminal from where Elasticsearch is running, navigate to the directory
where you installed Elasticsearch and run the
`elasticsearch-create-enrollment-token` tool
to generate an enrollment token for your new nodes.
```
bin{slash}elasticsearch-create-enrollment-token -s node
```
Copy the enrollment token, which you'll use to enroll new nodes with
your Elasticsearch cluster.

. From the installation directory of your new node, start Elasticsearch and pass the
enrollment token with the `--enrollment-token` parameter.
```
bin{slash}elasticsearch --enrollment-token <enrollment-token>
```
Elasticsearch automatically generates certificates and keys in the following directory:
```
config{slash}certs
```

. Repeat the previous step for any new nodes that you want to enroll.
