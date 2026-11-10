<!-- Converted from tab-widgets/esql/esql-getting-started-widget-enrich-policy.asciidoc (AsciiDoc). Includes are inlined. -->

The following requests create and execute a policy called `clientip_policy`. The
policy links an IP address to an environment ("Development", "QA", or
"Production"):

```console
PUT clientips
{
  "mappings": {
    "properties": {
      "client_ip": {
        "type": "keyword"
      },
      "env": {
        "type": "keyword"
      }
    }
  }
}

PUT clientips/_bulk
{ "index" : {}}
{ "client_ip": "172.21.0.5", "env": "Development" }
{ "index" : {}}
{ "client_ip": "172.21.2.113", "env": "QA" }
{ "index" : {}}
{ "client_ip": "172.21.2.162", "env": "QA" }
{ "index" : {}}
{ "client_ip": "172.21.3.15", "env": "Production" }
{ "index" : {}}
{ "client_ip": "172.21.3.16", "env": "Production" }

PUT /_enrich/policy/clientip_policy
{
  "match": {
    "indices": "clientips",
    "match_field": "client_ip",
    "enrich_fields": ["env"]
  }
}

PUT /_enrich/policy/clientip_policy/_execute?wait_for_completion=false
```

On the demo environment at [ela.st/ql](https://ela.st/ql/),
an enrich policy called `clientip_policy` has already been created an executed.
The policy links an IP address to an environment ("Development", "QA", or
"Production").
