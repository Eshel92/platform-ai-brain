<!-- Converted from ingest/apis/index.asciidoc (AsciiDoc). Includes are inlined. -->

## Ingest APIs

**New API reference**
For the most up-to-date API details, refer to [Ingest APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ingest).

Use ingest APIs to manage tasks and resources related to <<ingest,ingest
pipelines>> and processors.

### Ingest pipeline APIs

Use the following APIs to create, manage, and test ingest pipelines:

* put-pipeline-api to create or update a pipeline
* get-pipeline-api to retrieve a pipeline configuration
* delete-pipeline-api to delete a pipeline
* simulate-pipeline-api and simulate-ingest-api to test ingest pipelines

### Stat APIs

Use the following APIs to get statistics about ingest processing:

* geoip-stats-api to get download statistics for IP geolocation databases used with
the `geoip` processor.

### Ingest IP Location Database APIs

Use the following APIs to configure and manage commercial IP geolocation database downloads:

* put-ip-location-database-api to create or update a database configuration
* get-ip-location-database-api to retrieve a database configuration
* delete-ip-location-database-api to delete a database configuration

(See `ingest/apis/put-pipeline.md`)
(See `ingest/apis/get-pipeline.md`)
(See `ingest/apis/delete-pipeline.md`)
(See `ingest/apis/simulate-pipeline.md`)
(See `ingest/apis/simulate-ingest.md`)
(See `ingest/apis/geoip-stats.md`)
(See `ingest/apis/put-ip-location-database.md`)
(See `ingest/apis/get-ip-location-database.md`)
(See `ingest/apis/delete-ip-location-database.md`)
