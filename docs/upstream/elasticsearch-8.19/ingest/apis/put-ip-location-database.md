<!-- Converted from ingest/apis/put-ip-location-database.asciidoc (AsciiDoc). Includes are inlined. -->

### Create or update IP geolocation database configuration API

**New API reference**
For the most up-to-date API details, refer to [Ingest APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ingest).

Creates or updates an IP geolocation database configuration.

**Important:** The Maxmind `account_id` shown below requires a license key. Because the license key is sensitive information,
it is stored as a secure setting in Elasticsearch named `ingest.geoip.downloader.maxmind.license_key`. Only
one Maxmind license key is currently allowed per Elasticsearch cluster. A valid license key must be in the secure settings in order
to download from Maxmind. The license key setting does not take effect until all nodes are restarted or a
`reload_secure_settings` request is executed.

```console
PUT _ingest/ip_location/database/my-database-1
{
  "name": "GeoIP2-Domain",
  "maxmind": {
    "account_id": "1234567"
  }
}
```

**Important:** The IPinfo configuration shown below requires a token. Because the token is sensitive information,
it is stored as a secure setting in Elasticsearch named `ingest.ip_location.downloader.ipinfo.token`. Only
one IPinfo token is currently allowed per Elasticsearch cluster. A valid token must be in the secure settings in order
to download from IPinfo. The token setting does not take effect until all nodes are restarted or a
`reload_secure_settings` request is executed.

```console
PUT _ingest/ip_location/database/my-database-2
{
  "name": "standard_location",
  "ipinfo": {
  }
}
```

#### Request

`PUT /_ingest/ip_location/database/<database>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`manage` cluster privilege to use this API.

#### Path parameters

`<database>`::
__
(Required, string) ID of the database configuration to create or update.

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

#### Request body

`name`::
(Required, string)
The provider-assigned name of the IP geolocation database to download.

`<provider>`::
(Required, a provider object and its associated configuration)
The configuration necessary to identify which IP geolocation provider to use to download
the database, as well as any provider-specific configuration necessary for such downloading.
At present, the only supported providers are `maxmind` and `ipinfo`. The maxmind provider
requires that an `account_id` (string) is configured. The ipinfo provider does not require
additional configuration in the request body.

#### Licensing

Downloading databases from third party providers is a commercial feature that requires an
appropriate license. For more information, refer to https://www.elastic.co/subscriptions.
