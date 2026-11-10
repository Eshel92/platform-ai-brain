<!-- Converted from security/securing-communications/security-minimal-setup.asciidoc (AsciiDoc). Includes are inlined. -->

### Set up minimal security for Elasticsearch

**Important:** You only need to complete the following steps if you're running an
existing, unsecured cluster and want to enable the Elasticsearch security features.

In Elasticsearch 8.0 and later, security is
enabled automatically when you start Elasticsearch for the
first time.

If you're running an existing Elasticsearch cluster where security is disabled, you can
manually enable the Elasticsearch security features and then create passwords for
built-in users. You can add more users later, but using the built-in users
simplifies the process of enabling security for your cluster.

**Important:** The minimal security scenario is not sufficient for
production mode clusters. If your cluster has multiple
nodes, you must enable minimal security and then
configure Transport Layer Security (TLS) between
nodes.

#### Enable Elasticsearch security features

Enabling the Elasticsearch security features provides basic authentication so
that you can run a local cluster with username and password authentication.

. On *every* node in your cluster, stop both Kibana and Elasticsearch if they are running.

. On *every* node in your cluster, add the `xpack.security.enabled` setting to
the `$ES_PATH_CONF/elasticsearch.yml` file and set the value to `true`:
```yaml
xpack.security.enabled: true
```
**Note:** The `$ES_PATH_CONF` variable is the path for the Elasticsearch
configuration files. If you installed Elasticsearch using archive distributions
(`zip` or `tar.gz`), the variable defaults to `$ES_HOME/config`. If you used
package distributions (Debian or RPM), the variable defaults to `/etc/elasticsearch`.

. If your cluster has a single node, add the `discovery.type` setting in the
`$ES_PATH_CONF/elasticsearch.yml` file and set the value to `single-node`. This
setting ensures that your node does not inadvertently connect to other clusters
that might be running on your network.
```yaml
discovery.type: single-node
```

#### Set passwords for built-in users

To communicate with your cluster, you must configure a password for
the `elastic` and `kibana_system` built-in users. Unless you enable anonymous
access (not recommended), all requests that don’t include credentials are
rejected.

**Note:** You only need to set passwords for the `elastic` and `kibana_system` users
when enabling minimal or basic security.

. On *every* node in your cluster, start Elasticsearch. For example, if you installed
Elasticsearch with a `.tar.gz` package, run the following command from the `ES_HOME`
directory:
```shell
./bin/elasticsearch
```

. On any node in your cluster, open another terminal window and set the password
for the `elastic` built-in user by running the
`elasticsearch-reset-password` utility.
This command resets the password to an auto-generated value.
```shell
./bin/elasticsearch-reset-password -u elastic
```
If you want to set the password to a specific value, run the command with the
interactive (`-i`) parameter.
```shell
./bin/elasticsearch-reset-password -i -u elastic
```

. Set the password for the `kibana_system` built-in user.
```shell
./bin/elasticsearch-reset-password -u kibana_system
```

. Save the new passwords. In the next step, you'll add the password for the
`kibana_system` user to Kibana.

*Next*: Configure Kibana to connect to Elasticsearch with a password

#### Configure Kibana to connect to Elasticsearch with a password

When the Elasticsearch security features are enabled, users must log in to Kibana with a
valid username and password.

You'll configure Kibana to use the built-in `kibana_system` user and the password that
you created earlier. Kibana performs some background tasks that require use of the
`kibana_system` user.

This account is not meant for individual users and does not have permission to log in
to Kibana from a browser. Instead, you'll log in to Kibana as the `elastic` superuser.

. Add the `elasticsearch.username` setting to the `KBN_PATH_CONF/kibana.yml`
file and set the value to the `kibana_system` user:
```yaml
elasticsearch.username: "kibana_system"
```
**Note:** The `KBN_PATH_CONF` variable is the path for the Kibana
configuration files. If you installed Kibana using archive distributions
(`zip` or `tar.gz`), the variable defaults to `KIB_HOME/config`. If you used
package distributions (Debian or RPM), the variable defaults to `/etc/kibana`.

. From the directory where you installed Kibana, run the following commands
to create the Kibana keystore and add the secure settings:

   a. Create the Kibana keystore:
```shell
./bin/kibana-keystore create
```

   b. Add the password for the `kibana_system` user to the Kibana keystore:
```shell
./bin/kibana-keystore add elasticsearch.password
```
When prompted, enter the password for the `kibana_system` user.

. Restart Kibana. For example, if you installed Kibana with a `.tar.gz` package, run the following command from the Kibana directory:
```shell
./bin/kibana
```

. Log in to Kibana as the `elastic` user. Use this superuser account to
[manage spaces, create new users, and assign roles](https://www.elastic.co/guide/en/kibana/8.19/tutorial-secure-access-to-kibana.html). If you're running Kibana locally, go to `http://localhost:5601` to view the login page.

#### What's next?

Congratulations! You enabled password protection for your local cluster to
prevent unauthorized access. You can log in to Kibana securely as the `elastic`
user and create additional users and roles. If you're running a single-node cluster, then you can stop here.

If your cluster has multiple nodes, then you must configure Transport Layer
Security (TLS) between nodes. Production mode clusters
will not start if you do not enable TLS.

Set up basic security for the Elastic Stack to
secure all internal communication between nodes in your cluster.
