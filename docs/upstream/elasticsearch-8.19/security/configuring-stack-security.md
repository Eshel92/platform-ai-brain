<!-- Converted from security/configuring-stack-security.asciidoc (AsciiDoc). Includes are inlined. -->

## Start the Elastic Stack with security enabled automatically

When you start Elasticsearch for the first time, the following security configuration
occurs automatically:

* Certificates and keys for TLS are
generated for the transport and HTTP layers.
* The TLS configuration settings are written to `elasticsearch.yml`.
* A password is generated for the `elastic` user.
* An enrollment token is generated for Kibana.

You can then start Kibana and enter the enrollment token, which is valid for 30
minutes. This token automatically applies the security settings from your Elasticsearch
cluster, authenticates to Elasticsearch with the built-in `kibana` service account, and
writes the security configuration to `kibana.yml`.

**Note:** There are some cases where security
can't be configured automatically because the node startup process detects that
the node is already part of a cluster, or that security is already configured or
explicitly disabled.

### Prerequisites

* [Download](https://www.elastic.co/downloads/elasticsearch) and
unpack the `elasticsearch` package distribution for your
environment.
* [Download](https://www.elastic.co/downloads/kibana) and unpack
the `kibana` package distribution for your environment.

### Start Elasticsearch and enroll Kibana with security enabled

. From the installation directory, start Elasticsearch.
```shell
bin/elasticsearch
```
The command prints the `elastic` user password and an enrollment token for Kibana.

. Copy the generated `elastic` password and enrollment token. These credentials
are only shown when you start Elasticsearch for the first time.

**Note:**
If you need to reset the password for the `elastic` user or other
built-in users, run the `elasticsearch-reset-password` tool.
To generate new enrollment tokens for Kibana or Elasticsearch nodes, run the
`elasticsearch-create-enrollment-token` tool.
These tools are available in the Elasticsearch `bin` directory.
We recommend storing the `elastic` password as an environment variable in your shell. Example:
```sh
export ELASTIC_PASSWORD="your_password"
```

. (Optional) Open a new terminal and verify that you can connect to your Elasticsearch
cluster by making an authenticated call.
```shell
curl --cacert config/certs/http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200
```

. From the directory where you installed Kibana, start Kibana.
```shell
bin/kibana
```

. Enroll Kibana using either interactive or detached mode.

  * *Interactive mode* (browser)

  .. In your terminal, click the generated link to open Kibana in your browser.
  .. In your browser, paste the enrollment token that you copied and click the
  button to connect your Kibana instance with Elasticsearch.

**Note:**
Kibana won't enter interactive mode if it detects existing credentials for Elasticsearch
(`elasticsearch.username` and `elasticsearch.password`) or an existing URL for
`elasticsearch.hosts`.

  * *Detached mode* (non-browser)
Run the `kibana-setup` tool and pass the generated enrollment token with the
`--enrollment-token` parameter.
```
bin/kibana-setup --enrollment-token <enrollment-token>
```

### Enroll additional nodes in your cluster

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

(See `setup/install/connect-clients.md`)

### What's next?

Congratulations! You've successfully started the Elastic Stack with security enabled.
Elasticsearch and Kibana are secured with TLS on the HTTP layer, and internode
communication is encrypted. If you want to enable HTTPS for web traffic, you
can encrypt traffic between your browser and Kibana.

(See `setup/install/security-files-reference.md`)
Additionally, when you use the enrollment token to connect Kibana to a secured Elasticsearch cluster, the HTTP layer CA certificate is retrieved from Elasticsearch and stored in the
Kibana `/data` directory. This file establishes trust between Kibana and the Elasticsearch
Certificate Authority (CA) for the HTTP layer.

### Cases when security auto configuration is skipped

When you start Elasticsearch for the first time, the node startup process tries to
automatically configure security for you. The process runs some checks to
determine:

* If this is the first time that the node is starting
* Whether security is already configured
* If the startup process can modify the node configuration

If any of those checks fail, there's a good indication that you
manually configured security, or don't want
security to be configured automatically. In these cases, the node starts
normally using the existing configuration.

**Important:** If you redirect Elasticsearch output to a file, security autoconfiguration is skipped.
Autoconfigured credentials can only be viewed on the terminal the first time you start Elasticsearch.
If you need to redirect output to a file, start Elasticsearch without redirection the first time
and use redirection on all subsequent starts.

#### Existing environment detected

If certain directories already exist, there's a strong indication that the node
was started previously. Similarly, if certain files _don't_ exist, or we can't
read or write to specific files or directories, then we're likely not running as
the user who installed Elasticsearch or an administrator imposed restrictions. If any of
the following environment checks are true, security isn't configured
automatically.

The Elasticsearch `/data` directory exists and isn't empty::
The existence of this directory is a strong indicator that the node was started
previously, and might already be part of a cluster.

The `elasticsearch.yml` file doesn't exist (or isn't readable), or the `elasticsearch.keystore` isn't readable::
If either of these files aren't readable, we can't determine whether Elasticsearch security
features are already enabled. This state can also indicate that the node startup
process isn't running as a user with sufficient privileges to modify the
node configuration.

The Elasticsearch configuration directory isn't writable::
This state likely indicates that an administrator made this directory read-only,
or that the user who is starting Elasticsearch is not the user that installed Elasticsearch.

#### Existing settings detected

The following settings are incompatible with security auto configuration. If any
of these settings exist, the node startup process skips configuring security
automatically and the node starts normally.

* [`node.roles`](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/modules-node.html#node-roles) is set to a value where the
node can't be elected as `master`, or if the node can't hold data
* [`xpack.security.autoconfiguration.enabled`](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-settings.html#general-security-settings) is set to `false`
* [`xpack.security.enabled`](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-settings.html#general-security-settings) has a value set
* Any of the
[`xpack.security.transport.ssl.*`](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-settings.html#transport-tls-ssl-settings) or
[`xpack.security.http.ssl.*`](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-settings.html#http-tls-ssl-settings)
settings have a value set in the `elasticsearch.yml` configuration file or in
the `elasticsearch.keystore`
* Any of the `discovery.type`, `discovery.seed_hosts`, or
`cluster.initial_master_nodes`
[discovery and cluster formation settings](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/modules-discovery-settings.html)
have a value set

**Note:**
Exceptions are when `discovery.type` is set to `single-node`, or when
`cluster.initial_master_nodes` exists but contains only the name of the current
node.
