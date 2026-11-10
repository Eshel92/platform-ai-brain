<!-- Converted from cluster/get-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Cluster get settings API

**New API reference**
For the most up-to-date API details, refer to [Cluster APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster).

Returns cluster-wide settings.

```console
GET /_cluster/settings
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Request

`GET /_cluster/settings`

#### Description

By default, this API call only returns settings that have been explicitly 
defined, but can also include the default settings by calling the 
`include_defaults` parameter.

#### Query parameters

`flat_settings`::
(Optional, Boolean) If `true`, returns settings in flat format. Defaults to
`false`.
`include_defaults`::
    (Optional, Boolean) If `true`, returns default cluster settings from the local node. 
    Defaults to `false`.

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
