<!-- Converted from security/securing-communications/security-basic-setup-https.asciidoc (AsciiDoc). Includes are inlined. -->

### Set up basic security for the Elastic Stack plus secured HTTPS traffic

When you enable TLS on the HTTP layer it provides an additional layer of
security to ensure that all communications to and from your
cluster are encrypted.

When you run the `elasticsearch-certutil` tool in `http` mode, the tool asks
several questions about how you want to generate certificates. While there are
numerous options, the following choices result in certificates that should
work for most environments.

**Signing certificates**
****
The first question that the `elasticsearch-certutil` tool prompts you with is
whether you want to generate a Certificate Signing Request (CSR). Answer
`n` if you want to sign your own certificates, or `y` if you want to sign
certificates with a central CA.

##### Sign your own certificates

If you want to use the CA that you created when
Generating the certificate authority answer `n` when
asked if you want to generate a CSR. You then specify the location of your CA,
which the tool uses to sign and generate a `.p12` certificate. The steps in
this procedure follow this workflow.

##### Sign certificates with a central CA

If you work in an environment with a central security team, they can likely
generate a certificate for you. Infrastructure within your organization
might already be configured to trust an existing CA, so it may be easier
for clients to connect to Elasticsearch if you use a CSR and send that
request to the team that controls your CA. To use a central CA, answer `y` to
the first question.
****

#### Prerequisites

Complete all steps in Set up basic security for the Elastic Stack.

#### Encrypt HTTP client communications for Elasticsearch

. On *every* node in your cluster, stop Elasticsearch and Kibana if they are running.

. On any single node, from the directory where you installed Elasticsearch, run the Elasticsearch
   HTTP certificate tool to generate a Certificate Signing Request (CSR).
```shell
./bin/elasticsearch-certutil http
```
This command generates a `.zip` file that contains certificates and keys
to use with Elasticsearch and Kibana. Each folder contains a `README.txt`
explaining how to use these files.

   a. When asked if you want to generate a CSR, enter `n`.

   b. When asked if you want to use an existing CA, enter `y`.

   c. Enter the path to your CA. This is the absolute path to
   the `elastic-stack-ca.p12` file that you generated for your cluster.

   d. Enter the password for your CA.

   e. Enter an expiration value for your certificate. You can enter the
   validity period in years, months, or days. For example, enter `90D` for 90
   days.

   f. When asked if you want to generate one certificate per node, enter `y`.
Each certificate will have its own private key, and will be issued for a
specific hostname or IP address.

   g. When prompted, enter the name of the first node in your cluster. Use the same node name that you used when generating node certificates.

   h. Enter all hostnames used to connect to your first node. These hostnames
   will be added as DNS names in the Subject Alternative Name (SAN) field in your certificate.
List every hostname and variant used to connect to your cluster over HTTPS.

   i. Enter the IP addresses that clients can use to connect to your node.

   j. Repeat these steps for each additional node in your cluster.

. After generating a certificate for each of your nodes, enter a password for
   your private key when prompted.

. Unzip the generated `elasticsearch-ssl-http.zip` file. This compressed file
   contains one directory for both Elasticsearch and Kibana.
```txt
/elasticsearch
|_ README.txt
|_ http.p12
|_ sample-elasticsearch.yml
```

```txt
/kibana
|_ README.txt
|_ elasticsearch-ca.pem
|_ sample-kibana.yml
```

. On *every* node in your cluster, complete the following steps:

  .. Copy the relevant `http.p12` certificate to the `$ES_PATH_CONF` directory.

  .. Edit the `elasticsearch.yml` file to enable HTTPS security and specify the
  location of the `http.p12` security certificate.
```yaml
xpack.security.http.ssl.enabled: true
xpack.security.http.ssl.keystore.path: http.p12
```

  .. Add the password for your private key to the secure settings in Elasticsearch.
```shell
./bin/elasticsearch-keystore add xpack.security.http.ssl.keystore.secure_password
```

  .. Start Elasticsearch.

**Next**: Encrypt HTTP client communications for Kibana

#### Encrypt HTTP client communications for Kibana

Browsers send traffic to Kibana and Kibana sends traffic to Elasticsearch.
These communication channels are configured separately to use TLS. You encrypt
traffic between Kibana and Elasticsearch, and then encrypt traffic between your browser
and Kibana.

##### Encrypt traffic between Kibana and Elasticsearch

When you ran the `elasticsearch-certutil` tool with the `http` option, it
created a `/kibana` directory containing an `elasticsearch-ca.pem` file. You
use this file to configure Kibana to trust the Elasticsearch CA for the HTTP
layer.

. Copy the `elasticsearch-ca.pem` file to the Kibana configuration directory,
as defined by the `$KBN_PATH_CONF` path.

. Open `kibana.yml` and add the following line to specify the location of the
security certificate for the HTTP layer.
```yaml
elasticsearch.ssl.certificateAuthorities: $KBN_PATH_CONF/elasticsearch-ca.pem
```

. Add the following line to specify the HTTPS URL for your Elasticsearch
cluster.
```yaml
elasticsearch.hosts: https://<your_elasticsearch_host>:9200
```

. Restart Kibana.

**Connect to a secure monitoring cluster**
****
If the Elastic monitoring features are enabled and you configured a separate
Elasticsearch monitoring cluster, you can also configure Kibana to connect to
the monitoring cluster via HTTPS. The steps are the same, but each setting is
prefixed by `monitoring`. For example, `monitoring.ui.elasticsearch.hosts` and
`monitoring.ui.elasticsearch.ssl.truststore.path`.

**Note:** You must create a separate `elasticsearch-ca.pem` security file for the
monitoring cluster.
****

**Next**: Encrypt traffic between your browser and Kibana

##### Encrypt traffic between your browser and Kibana

You create a server certificate and private key for Kibana. Kibana uses this
server certificate and corresponding private key when receiving connections
from web browsers.

When you obtain a server certificate, you must set its subject alternative
name (SAN) correctly to ensure that browsers will trust it. You can set one or
more SANs to the Kibana server’s fully-qualified domain name (FQDN), hostname,
or IP address. When choosing the SAN, pick whichever attribute you'll use to
connect to Kibana in your browser, which is likely the FQDN.

The following instructions create a Certificate Signing Request (CSR) for Kibana.
A CSR contains information that a CA uses to generate and sign a security
certificate. The certificate can be trusted (signed by a public, trusted CA)
or untrusted (signed by an internal CA). A self-signed or internally-signed
certificate is acceptable for development environments and building a proof of
concept, but should not be used in a production environment.

**Warning:** Before going to production, use a trusted CA such as https://letsencrypt.org/[Let's
Encrypt] or your organization's internal CA to sign the certificate. Using a
signed certificate establishes browser trust for connections to Kibana for
internal access or on the public internet.

. Generate a server certificate and private key for Kibana.
```shell
./bin/elasticsearch-certutil csr -name kibana-server -dns example.com,www.example.com
```
The CSR has a common name (CN) of `kibana-server`, a SAN of `example.com`,
and another SAN of `www.example.com`.
This command generates a `csr-bundle.zip` file by default with the following
contents:
```txt
/kibana-server
|_ kibana-server.csr
|_ kibana-server.key
```

. Unzip the `csr-bundle.zip` file to obtain the `kibana-server.csr` unsigned
security certificate and the `kibana-server.key` unencrypted private key.

. Send the `kibana-server.csr` certificate signing request to your internal
CA or trusted CA for signing to obtain a signed certificate. The signed file
can be in different formats, such as a `.crt` file like `kibana-server.crt`.

. Open `kibana.yml` and add the following lines to configure Kibana to access
the server certificate and unencrypted private key.
```yaml
server.ssl.certificate: $KBN_PATH_CONF/kibana-server.crt
server.ssl.key: $KBN_PATH_CONF/kibana-server.key
```
**Note:** `$KBN_PATH_CONF` contains the path for the Kibana configuration files. If
you installed Kibana using archive distributions (`zip` or `tar.gz`), the
path defaults to `$KBN_HOME/config`. If you used package distributions
(Debian or RPM), the path defaults to `/etc/kibana`.

. Add the following line to `kibana.yml` to enable TLS for inbound
connections.
```yaml
server.ssl.enabled: true
```

. Start Kibana.

**Note:** After making these changes, you must always access Kibana via HTTPS. For
example, `https://<your_kibana_host>.com`.

**Next**: Configure Beats security

#### Configure Beats security

Beats are open source data shippers that you install as agents on your
servers to send operational data to Elasticsearch. Each Beat is a separately
installable product. The following steps cover configuring security for
{metricbeat}. Follow these steps for each 
{beats-ref}/getting-started.html[additional Beat] you want to configure security
for.

##### Prerequisites

{metricbeat-ref}/metricbeat-installation-configuration.html[Install {metricbeat}] using your preferred method.

**Important:** You cannot connect to the Elastic Stack or configure assets for {metricbeat}
before completing the following steps.

##### Create roles for {metricbeat}

Typically, you need to create the following separate roles:

- **setup** role for setting up index templates and other dependencies
- **monitoring** role for sending monitoring information
- **writer** role for publishing events collected by {metricbeat}
- **reader** role for Kibana users who need to view and create visualizations that access {metricbeat} data

**Note:** These instructions assume that you are using the default name for
{metricbeat} indices. If the indicated index names are not listed, or you are
using a custom name, enter it manually when defining roles and modify the
privileges to match your index naming pattern.

To create users and roles from Stack Management in Kibana, select **Roles**
or **Users** from the side navigation.

**Next**: Create a setup role

###### Create a setup role and user

Administrators who set up {metricbeat} typically need to load mappings,
dashboards, and other objects used to index data into Elasticsearch and visualize it in
Kibana.

**Warning:** Setting up {metricbeat} is an admin-level task that requires extra
privileges. As a best practice, grant the setup role to administrators only,
and use a more restrictive role for event publishing.

. Create the setup role:

   . Enter **metricbeat_setup** as the role name.

   . Choose the **monitor** and **manage_ilm** cluster privileges.

   . On the **metricbeat-\*** indices, choose the **manage** and **write**
   privileges.
If the **metricbeat-\*** indices aren't listed, enter that pattern into the
list of indices.

. Create the setup user:

   . Enter **metricbeat_setup** as the user name.

   . Enter the username, password, and other user details.

   . Assign the following roles to the **metricbeat_setup** user:
|===
| Role               | Purpose

| `metricbeat_setup` | Set up {metricbeat}.
| `kibana_admin`     | Load dependencies, such as example dashboards, if available, into Kibana
| `ingest_admin`     | Set up index templates and, if available, ingest pipelines
|===

**Next**: Create a monitoring role

###### Create a monitoring role and user

To send monitoring data securely, create a monitoring user and grant it the
necessary privileges.

You can use the built-in `beats_system` user, if it’s available in your
environment. Because the built-in users are not available in Elastic Cloud,
these instructions create a user that is explicitly used for monitoring
{metricbeat}.

. If you're using the built-in `beats_system` user, on any node in your cluster,
run the `elasticsearch-reset-password` utility to set the
password for that user:
This command resets the password for the `beats_system` user to an 
auto-generated value.
```shell
./bin/elasticsearch-reset-password -u beats_system
```
If you want to set the password to a specific value, run the command with the 
interactive (`-i`) parameter.
```shell
./bin/elasticsearch-reset-password -i -u beats_system
```

. Create the monitoring role:

   . Enter **metricbeat_monitoring** as the role name.

   . Choose the **monitor** cluster privilege.

   . On the **.monitoring-beats-\*** indices, choose the **create_index** and
   **create_doc** privileges.

. Create the monitoring user:

   . Enter **metricbeat_monitoring** as the user name.

   . Enter the username, password, and other user details.

   . Assign the following roles to the **metricbeat_monitoring** user:
|===
| Role                    | Purpose

| `metricbeat_monitoring` | Monitor {metricbeat}.
| `kibana_admin`          | Use Kibana
| `monitoring_user`       | Use Stack Monitoring in Kibana to monitor {metricbeat}
|===

**Next**: Create a writer role

###### Create a writer role and user

Users who publish events to Elasticsearch need to create and write to {metricbeat} indices. To minimize the privileges required by the writer role, use the setup role to pre-load dependencies. This section assumes that you’ve
created the setup role.

. Create the writer role:

   . Enter **metricbeat_writer** as the role name.

   . Choose the **monitor** and **read_ilm** cluster privileges.

   . On the **metricbeat-\*** indices, choose the **create_doc**, **create_index**, and **view_index_metadata** privileges.

. Create the writer user:

   . Enter **metricbeat_writer** as the user name.

   . Enter the username, password, and other user details.

   . Assign the following roles to the **metricbeat_writer** user:
|===
| Role                          | Purpose

| `metricbeat_writer`           | Monitor {metricbeat}
| `remote_monitoring_collector` | Collect monitoring metrics from {metricbeat}
| `remote_monitoring_agent`     | Send monitoring data to the monitoring cluster
|===

**Next**: Create a reader role

###### Create a reader role and user

Kibana users typically need to view dashboards and visualizations that contain
{metricbeat} data. These users might also need to create and edit dashboards
and visualizations. Create the reader role to assign proper privileges to these
users.

. Create the reader role:

   . Enter **metricbeat_reader** as the role name.

   . On the **metricbeat-\*** indices, choose the **read** privilege.

   . Under **Kibana**, click **Add Kibana privilege**.

   - Under **Spaces**, choose **Default**.

   - Choose **Read** or **All** for Discover, Visualize, Dashboard, and Metrics.

. Create the reader user:

   . Enter **metricbeat_reader** as the user name.

   . Enter the username, password, and other user details.

   . Assign the following roles to the **metricbeat_reader** user:
|===
| Role                          | Purpose

| `metricbeat_reader` | Read {metricbeat} data.
| `monitoring_user`   | Allow users to monitor the health of {metricbeat}
itself. Only assign this role to users who manage {metricbeat}
| `beats_admin`       | Create and manage configurations in Beats central
management. Only assign this role to users who need to use Beats central
management.
|===

**Next**: Configure {metricbeat} to use TLS

##### Configure {metricbeat} to use TLS

Before starting {metricbeat}, you configure the connections to Elasticsearch and
Kibana. You can configure authentication to send data to your secured cluster
using basic authentication, API key authentication, or Public Key
Infrastructure (PKI) certificates.

The following instructions use the credentials for the `metricbeat_writer`
and `metricbeat_setup` users that you created. If you need a greater level of
security, we recommend using PKI certificates.

After configuring connections to Elasticsearch and Kibana, you'll enable the
`elasticsearch-xpack` module and configure that module to use HTTPS.

**Warning:** In production environments, we strongly recommend using a separate
cluster (referred to as the monitoring cluster) to store your data. Using a
separate monitoring cluster prevents production cluster outages from impacting
your ability to access your monitoring data. It also prevents monitoring
activities from impacting the performance of your production cluster.

. On the node where you
generated certificates for the HTTP layer,
navigate to the `/kibana` directory.

. Copy the `elasticsearch-ca.pem` certificate to the directory where you
installed {metricbeat}.

. Open the `metricbeat.yml` configuration file and configure the connection
to Elasticsearch.
Under `output.elasticsearch`, specify the following fields:
```yaml
output.elasticsearch:
 hosts: ["<your_elasticsearch_host>:9200"]
 protocol: "https"
 username: "metricbeat_writer"
 password: "<password>"
 ssl:
   certificate_authorities: ["elasticsearch-ca.pem"]
   verification_mode: "certificate"
```

   `hosts`:: Specifies the host where your Elasticsearch cluster is running.

   `protocol`:: Indicates the protocol to use when connecting to Elasticsearch.
   This value must be `https`.

   `username`:: Name of the user with privileges required to publish events to
   Elasticsearch. The `metricbeat_writer` user that you created has these
   privileges.

   `password`:: Password for the indicated `username`.

   `certificate_authorities`:: Indicates the path to the local `.pem` file that
   contains your CA's certificate. 

. Configure the connection to Kibana.
Under `setup.kibana`, specify the following fields:
```yaml
setup.kibana
 host: "https://<your_elasticsearch_host>:5601"
 ssl.enabled: true
 username: "metricbeat_setup"
 password: "p@ssw0rd"
```

   `hosts`:: The URLs of the Elasticsearch instances to use for all your
   queries. Ensure that you include `https` in the URL.

   `username`:: Name of the user with privileges required to set up dashboards in Kibana. The `metricbeat_setup` user that you created has these privileges.

   `password`:: Password for the indicated `username`.

. Enable the `elasticsearch-xpack` module.
```shell
./metricbeat modules enable elasticsearch-xpack
```

. Modify the `elasticsearch-xpack` module to use HTTPS. This module collects
metrics about Elasticsearch.
Open `/modules.d/elasticsearch-xpack.yml` and specify the following fields:
```yaml
- module: elasticsearch
 xpack.enabled: true
 period: 10s
 hosts: ["https://<your_elasticsearch_host>:9200"]
 username: "remote_monitoring_user"
 password: "<password>"
 ssl:     <1>
   enabled: true
   certificate_authorities: ["elasticsearch-ca.pem"]
   verification_mode: "certificate"
```
<1> Configuring SSL is required when monitoring a node with encrypted traffic.
See {metricbeat-ref}/configuration-ssl.html[Configure SSL for {metricbeat}].

   `hosts`:: Specifies the host where your Elasticsearch cluster is running.
   Ensure that you include `https` in the URL.

   `username`:: Name of the user with privileges to collect metric data. The
   built-in `monitoring_user` user has these privileges. Alternatively,
   you can create a user and assign it the `monitoring_user` role.

   `password`:: Password for the indicated `username`.

   `certificate_authorities`:: Indicates the path to the local `.pem` file that
   contains your CA's certificate. 

. If you want to use the predefined assets for parsing, indexing, and
   visualizing your data, run the following command to load these assets:
```shell
./metricbeat setup -e
```

. Start Elasticsearch, and then start {metricbeat}.
```shell
./metricbeat -e
```
`-e` is optional and sends output to standard error instead of the configured
log output.

. Log in to Kibana, open the main menu, and click **Stack Monitoring**.
You’ll see cluster alerts that require your attention and a summary of the available monitoring metrics for Elasticsearch. Click any of the header links on the available cards to view additional information.
