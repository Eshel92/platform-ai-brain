<!-- Converted from ingest/apis/geoip-stats.asciidoc (AsciiDoc). Includes are inlined. -->

### GeoIP stats API

**New API reference**
For the most up-to-date API details, refer to [Ingest APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ingest).

Gets statistics about the `geoip` processor, including
download statistics for GeoIP2 databases used with it.

```console
GET _ingest/geoip/stats
```

#### Request

`GET _ingest/geoip/stats`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

* If `ingest.geoip.downloader.enabled` is
disabled and no custom databases are configured, this API returns zero values and an empty `nodes` object.

#### Response body

`stats`::
(object)
Download statistics for all GeoIP2 databases.
**Properties of `stats`**
`successful_downloads`::
(integer)
Total number of successful database downloads.

`failed_downloads`::
(integer)
Total number of failed database downloads.

`total_download_time`::
(integer)
Total milliseconds spent downloading databases.

`database_count`::
(integer)
Current number of databases available for use.

`skipped_updates`::
(integer)
Total number of database updates skipped.

`nodes`::
(object)
Statistics for each node.
**Properties of `nodes`**
`<node_id>`::
(object)
Downloaded databases for the node. The field key is the node ID.
**Properties of `<node_id>`**
=====
`databases`::
(array of objects)
Downloaded databases for the node.
**Properties of `databases` objects**
======
`name`::
(string)
Name of the database.
======
`cache_stats`::
(object)
GeoIP cache stats for the node.
**Properties of `cache_stats`**
======
`count`::
(Long)
Number of cached entries.

`hits`::
(Long)
The number of enrich lookups served from cache.

`misses`::
(Long)
The number of times geoIP lookups couldn't be
served from cache.

`evictions`::
(Long)
The number cache entries evicted from the cache.

`hits_time_in_millis`::
(Long)
The amount of time in milliseconds spent fetching data from the cache on successful cache hits only.

`misses_time_in_millis`::
(Long)
The amount of time in milliseconds spent fetching data from the cache and the backing GeoIP2 database and updating the
cache, on cache misses only.

======

`files_in_temp`::
(array of strings)
Downloaded database files, including related license files. Elasticsearch stores these
files in the node's temporary directory:
`$ES_TMPDIR/geoip-databases/<node_id>`.
=====
