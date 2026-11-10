<!-- Converted from user/monitoring/viewing-metrics.asciidoc (AsciiDoc). Includes are inlined. -->

# View monitoring data in Kibana

After you collect monitoring data for one or more products in the Elastic Stack, you
can configure Kibana to retrieve that information and display it in on the
*Stack Monitoring* page.

At a minimum, you must have monitoring data for the Elasticsearch production cluster.
Once that data exists, Kibana can display monitoring data for other products in
the cluster.

**Tip:** If you use a separate monitoring cluster to store the monitoring data, it
is strongly recommended that you use a separate Kibana instance to view it. If
you log in to Kibana using SAML, Kerberos, PKI, OpenID Connect, or token
authentication providers, a dedicated Kibana instance is *required*. The security
tokens that are used in these contexts are cluster-specific, therefore you
cannot use a single Kibana instance to connect to both production and monitoring
clusters. For more information about the recommended configuration, see
[Monitoring overview](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/monitoring-overview.html).

. Identify where to retrieve monitoring data from.
If the monitoring data is stored on a dedicated monitoring cluster, it is
accessible even when the cluster you're monitoring is not. If you have at least
a gold license, you can send data from multiple clusters to the same monitoring
cluster and view them all through the same instance of Kibana.

By default, data is retrieved from the cluster specified in the
`elasticsearch.hosts` value in the `kibana.yml` file. If you want to retrieve it
from a different cluster, set `monitoring.ui.elasticsearch.hosts`.

To learn more about typical monitoring architectures,
see [How monitoring works](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/how-monitoring-works.html) and
[Monitoring in a production environment](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/monitoring-production.html).

. Verify that `monitoring.ui.enabled` is set to `true`, which is the
default value, in the `kibana.yml` file. For more information, see
monitoring-settings-kb.

. If the Elastic security features are enabled on the monitoring cluster, you
must provide a user ID and password so Kibana can retrieve the data.

.. Create a user that has the `monitoring_user`
[built-in role](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/built-in-roles.html) on the monitoring cluster.
**Note:** Make sure the `monitoring_user` role has read privileges on `metrics-*`
indices. If it doesn't, create a new role with `read` and `read_cross_cluster`
index privileges on `metrics-*`, then assign the new role (along with
`monitoring_user`) to your user.

.. Add the `monitoring.ui.elasticsearch.username` and
`monitoring.ui.elasticsearch.password` settings in the `kibana.yml` file.
If these settings are omitted, Kibana uses the `elasticsearch.username` and
`elasticsearch.password` setting values. For more
information, see [Configuring security in Kibana](https://www.elastic.co/guide/en/kibana/8.19/using-kibana-with-security.html).

. (Optional) Configure Kibana to encrypt communications between the Kibana server
and the monitoring cluster. See configuring-tls.

. If the Elastic security features are enabled on the Kibana server, only users
that have the authority to access Kibana indices and to read the monitoring indices
can use the monitoring dashboards.
**Note:** These users must exist on the monitoring cluster. If you are accessing a
remote monitoring cluster, you must use credentials that are valid on both the
Kibana server and the monitoring cluster.

.. Create users that have the `monitoring_user` and `kibana_admin`
[built-in roles](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/built-in-roles.html). If you created a new role with
read privileges on `metrics-*` indices, also assign that role to the users.

. Open Kibana in your web browser.
By default, if you are running Kibana locally, go to `http://localhost:5601/`.

If the Elastic security features are enabled, log in.

. Go to the *Stack Monitoring* page using the
global search field. 
If data collection is disabled, you are prompted to turn on data collection.
If Elasticsearch security features are enabled, you must have `manage` cluster
privileges to turn on data collection.

**Note:** If you are using a separate monitoring cluster, you do not need to turn on
data collection. The dashboards appear when there is data in the monitoring
cluster.

You'll see cluster alerts
that require your attention and a summary of the available monitoring metrics
for Elasticsearch, Logstash, Kibana, and Beats. To view additional information, click the
Overview, Nodes, Indices, or Instances links.  See xpack-monitoring.

(Figure: images/monitoring-dashboard.png)

If you encounter problems, see Troubleshooting monitoring.
