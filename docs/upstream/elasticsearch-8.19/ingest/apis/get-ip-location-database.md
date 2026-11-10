<!-- Converted from ingest/apis/get-ip-location-database.asciidoc (AsciiDoc). Includes are inlined. -->

### Get IP geolocation database configuration API

**New API reference**
For the most up-to-date API details, refer to [Ingest APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ingest).

Returns information about one or more IP geolocation database configurations.

```console
GET /_ingest/ip_location/database/my-database-id
```

#### Request

`GET /_ingest/ip_location/database/<database>`

`GET /_ingest/ip_location/database`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
 `manage` cluster privilege to use this API.

#### Path parameters

`<database>`::
(Optional, string)
Comma-separated list of database configuration IDs to retrieve. Wildcard (`*`) expressions are
supported.
To get all database configurations, omit this parameter or use `*`.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Examples

##### Get information for a specific IP geolocation database configuration

```console
GET /_ingest/ip_location/database/my-database-id
```

The API returns the following response:

```console-result
{
  "databases" : [
    {
      "id" : "my-database-id",
      "version" : 1,
      "modified_date_millis" : 1723040276114,
      "database" : {
        "name" : "GeoIP2-Domain",
        "maxmind" : {
          "account_id" : "1234567"
        }
      }
    }
  ]
}
```
