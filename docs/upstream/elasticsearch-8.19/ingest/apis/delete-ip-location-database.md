<!-- Converted from ingest/apis/delete-ip-location-database.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete IP geolocation database configuration API

**New API reference**
For the most up-to-date API details, refer to [Ingest APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ingest).

Deletes a IP geolocation database configuration.

```console
DELETE /_ingest/ip_location/database/my-database-id
```

#### Request

`DELETE /_ingest/ip_location/database/<database>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`manage` cluster privilege to use this API.

#### Path parameters

`<database>`::
(Required, string) Database configuration ID used to limit the request.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

`timeout`::
(Optional, time units) Period to wait for a response from all relevant nodes in the cluster after updating the cluster metadata.
If no response is received before the timeout expires, the cluster metadata update still applies but the response will indicate that it was not completely acknowledged.
Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Examples

##### Delete a specific IP geolocation database configuration

```console
DELETE /_ingest/ip_location/database/example-database-id
```
