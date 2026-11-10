<!-- Converted from tab-widgets/troubleshooting/data/start-ilm-widget.asciidoc (AsciiDoc). Includes are inlined. -->

In order to start index lifecycle management we need to go to Kibana and execute the start command.

**Use Kibana**

. Log in to the {ess-console}[Elastic Cloud console].

. On the **Elasticsearch Service** panel, click the name of your deployment. 

**Note:** If the name of your deployment is disabled your Kibana instances might be
unhealthy, in which case please contact [Elastic Support](https://support.elastic.co).
If your deployment doesn't include Kibana, all you need to do is 
{cloud}/ec-access-kibana.html[enable it first].

. Open your deployment's side navigation menu (placed under the Elastic logo in the upper left corner)
and go to **Dev Tools > Console**.
(Figure: images/kibana-console.png)

. Start index lifecycle management:
```console
POST _ilm/start
```
The response will look like this:
```console-result
{
  "acknowledged": true
}
```

. Verify index lifecycle management is now running:
```console
GET _ilm/status
```
The response will look like this:
```console-result
{
  "operation_mode": "RUNNING"
}
```

Start index lifecycle management:

```console
POST _ilm/start
```

The response will look like this:

```console-result
{
  "acknowledged": true
}
```

Verify index lifecycle management is now running:

```console
GET _ilm/status
```

The response will look like this:

```console-result
{
  "operation_mode": "RUNNING"
}
```
