<!-- Converted from modules/cluster/remote-clusters-remote-info.asciidoc (AsciiDoc). Includes are inlined. -->

```console
GET /_remote/info
```

The API should return `"connected" : true`. When using
API key authentication, it should also return
`"cluster_credentials": "::es_redacted::"`.

```console-result
{
  "cluster_one" : {
    "seeds" : [
      "127.0.0.1:9443"
    ],
    "connected" : true, <1>
    "num_nodes_connected" : 1, 
    "max_connections_per_cluster" : 3,
    "initial_connect_timeout" : "30s",
    "skip_unavailable" : false,
    "cluster_credentials": "::es_redacted::", <2>
    "mode" : "sniff"
  }
}
```
<1> The remote cluster has connected successfully.
<2> If present, indicates the remote cluster has connected using
API key authentication instead of
certificate based authentication.
