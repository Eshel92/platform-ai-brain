<!-- Converted from rest-api/watcher/start.asciidoc (AsciiDoc). Includes are inlined. -->

### Start watch service API

**New API reference**
For the most up-to-date API details, refer to [Watcher APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-watcher).

Starts the Watcher service if it is not already running.

#### Request

`POST _watcher/_start`

#### Prerequisites

* You must have `manage_watcher` cluster privileges to use this API. For more
information, see security-privileges.

#### Examples

```console
POST _watcher/_start
```

Watcher returns the following response if the request is successful:

```console-result
{
   "acknowledged": true
}
```
