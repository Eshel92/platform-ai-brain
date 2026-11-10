<!-- Converted from security/enroll-nodes.asciidoc (AsciiDoc). Includes are inlined. -->

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
