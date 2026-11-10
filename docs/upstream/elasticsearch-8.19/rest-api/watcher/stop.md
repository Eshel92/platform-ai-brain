<!-- Converted from rest-api/watcher/stop.asciidoc (AsciiDoc). Includes are inlined. -->

### Stop watch service API

**New API reference**
For the most up-to-date API details, refer to [Watcher APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-watcher).

Stops the Watcher service if it is running.

#### Request

`POST _watcher/_stop`

#### Prerequisites

* You must have `manage_watcher` cluster privileges to use this API. For more
information, see security-privileges.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Examples

```console
POST _watcher/_stop
```

Watcher returns the following response if the request is successful:

```console-result
{
   "acknowledged": true
}
```
