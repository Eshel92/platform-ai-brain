<!-- Converted from tab-widgets/api-call.asciidoc (AsciiDoc). Includes are inlined. -->

**Option 1: Use Kibana**

. Open Kibana's main menu ("*☰*" near Elastic logo) and go to **Dev Tools > Console**.
(Figure: images/kibana-console.png)

. Run the following test API request in Console:
```console
GET /
```

**Option 2: Use `curl`**

To communicate with Elasticsearch using `curl` or another client, you need your cluster's
endpoint.

. Open Kibana's main menu and click **Manage this deployment**.

. From your deployment menu, go to the **Elasticsearch** page. Click **Copy
endpoint**.

. To submit an example API request, run the following `curl` command in a new
terminal session. Replace `<password>` with the password for the `elastic` user.
Replace `<elasticsearch_endpoint>` with your endpoint.
```sh
curl -u elastic:<password> <elasticsearch_endpoint>/
```

**Use Kibana**

. Open Kibana's main menu ("*☰*" near Elastic logo) and go to **Dev Tools > Console**.
(Figure: images/kibana-console.png)

. Run the following test API request in Console:
```console
GET /
```

**Use curl**

To submit an example API request, run the following curl command in a new
terminal session.

```sh
curl -u elastic:$ELASTIC_PASSWORD https://localhost:9200
```
