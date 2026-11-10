<!-- Converted from cat/pending_tasks.asciidoc (AsciiDoc). Includes are inlined. -->

### cat pending tasks API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana 
console. They are _not_ intended for use by applications. For application 
consumption, use the pending cluster tasks API.

Returns cluster-level changes that have not yet been executed, similar to the
pending cluster tasks API.

#### Request

`GET /_cat/pending_tasks`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Query parameters

`format`::
(Optional, string) Short version of the
[HTTP accept header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
Valid values include JSON, YAML, etc.
`h`::
(Optional, string) Comma-separated list of column names to display.
`help`::
(Optional, Boolean) If `true`, the response includes help information. Defaults
to `false`.
`local`::
(Optional, Boolean) If `true`, the request retrieves information from the local
node only. Defaults to `false`, which means information is retrieved from
the master node.
`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`s`::
(Optional, string) Comma-separated list of column names or column aliases used
to sort the response.
`time`::
(Optional, time units)
Unit used to display time values.
`v`::
(Optional, Boolean) If `true`, the response includes column headings.
Defaults to `false`.

#### Examples

```console
GET /_cat/pending_tasks?v=true
```

The API returns the following response:

```txt
insertOrder timeInQueue priority source
       1685       855ms HIGH     update-mapping [foo][t]
       1686       843ms HIGH     update-mapping [foo][t]
       1693       753ms HIGH     refresh-mapping [foo][[t]]
       1688       816ms HIGH     update-mapping [foo][t]
       1689       802ms HIGH     update-mapping [foo][t]
       1690       787ms HIGH     update-mapping [foo][t]
       1691       773ms HIGH     update-mapping [foo][t]
```
