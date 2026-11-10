<!-- Converted from setup/access.asciidoc (AsciiDoc). Includes are inlined. -->

## Access Kibana

The fastest way to access Kibana is to use our hosted Elasticsearch Service. If you installed Kibana on your own, access Kibana through the web application.

### Set up on cloud

(Include not available offline: {docs-root}/shared/cloud/ess-getting-started.asciidoc)

### Log on to the web application

If you are using a self-managed deployment, access Kibana through the web application on port 5601.

. Point your web browser to the machine where you are running Kibana and specify the port number. For example, `localhost:5601` or `<HOST_URL>:5601`.
To remotely connect to Kibana, set server.host to a non-loopback address.

. Log on to your account.

. Go to the home page, then click *Kibana*.

. To make the Kibana page your landing page, click *Make this my landing page*.

### Check the Kibana status

The status page displays information about the server resource usage and installed plugins.

To view the Kibana status page, use the status endpoint. For example, `localhost:5601/status`. 

(Figure: images/kibana-status-page-7_14_0.png)

For JSON-formatted server status details, use the `localhost:5601/api/status` API endpoint. 

### Troubleshoot Kibana UI error

Troubleshoot the `Kibana Server is not Ready yet` error.

. From within a Kibana node, confirm the connection to Elasticsearch:
```sh
curl -XGET elasticsearch_ip_or_hostname:9200/
```
. Guarantee the health of the three Kibana-backing indices.  All indices must appear and display `status:green` and `status:open`:
```sh
curl -XGET elasticsearch_ip_or_hostname:9200/_cat/indices/.kibana,.kibana_task_manager,.kibana_security_session?v=true
```
These Kibana-backing indices must also not have [index settings](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/indices-get-settings.html) flagging `read_only_allow_delete` or `write` [index blocks](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/index-modules-blocks.html). 
. Shut down all Kibana nodes. 
. Choose any Kibana node, then update the config to set the debug logging.
. Start the node, then check the start-up debug logs for `ERROR` messages or other start-up issues. 
For example:

* When Kibana is unable to connect to a healthy Elasticsearch cluster, errors like `master_not_discovered_exception` or `unable to revive connection` or `license is not available` errors appear.
* When one or more Kibana-backing indices are unhealthy, the `index_not_green_timeout` error appears.

You can find a Kibana health troubleshooting walkthrough in [this blog](https://www.elastic.co/blog/troubleshooting-kibana-health) or in [this video](https://www.youtube.com/watch?v=AlgGYcpGvOA).
