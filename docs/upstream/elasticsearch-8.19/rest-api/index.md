<!-- Converted from rest-api/index.asciidoc (AsciiDoc). Includes are inlined. -->

# REST APIs

Elasticsearch exposes REST APIs that are used by the UI components and can be called
directly to configure and access Elasticsearch features.

**New API reference**
For the most up-to-date API details, refer to [Elasticsearch APIs](https://www.elastic.co/docs/api/doc/elasticsearch).

* API conventions
* Common Options
* REST API Compatibility
* Autoscaling APIs
* Behavioral Analytics APIs
* cat APIs
* Cluster APIs
* Features APIs
* Connector APIs
* Cross-cluster replication APIs
* Data stream APIs
* Document APIs
* Enrich APIs
* EQL search APIs
* ES|QL query APIs
* Fleet APIs
* Graph explore API
* Index APIs
* Index lifecycle management APIs
* Inference APIs
* Info API
* Ingest APIs
* Licensing APIs
* Logstash APIs
* Machine learning APIs
* Machine learning anomaly detection APIs
* Machine learning {dfanalytics} APIs
* Machine learning trained model APIs
* Migration APIs
* Node lifecycle API
* Query rules APIs
* Reload search analyzers API
* Repositories metering APIs
* Rollup APIs
* Root API
* Script APIs
* Search APIs
* Search Application APIs
* Searchable snapshots APIs
* Security APIs
* Snapshot and restore APIs
* Snapshot lifecycle management APIs
* SQL APIs
* Synonyms APIs
* Text structure APIs
* Transform APIs
* Usage API
* Watcher APIs

(See `api-conventions.md`)
(See `rest-api/common-options.md`)
(See `rest-api/rest-api-compatibility.md`)
(See `autoscaling/apis/autoscaling-apis.md`)
(See `behavioral-analytics/apis/index.md`)
(See `cat.md`)
(See `cluster.md`)
(See `ccr/apis/ccr-apis.md`)
(See `connector/apis/connector-apis.md`)
(See `data-streams/data-stream-apis.md`)
(See `docs.md`)
(See `ingest/apis/enrich/index.md`)
(See `eql/eql-apis.md`)
(See `esql/esql-apis.md`)
(See `features/apis/features-apis.md`)
(See `fleet/index.md`)
(See `graph/explore.md`)
(See `indices.md`)
(See `ilm/apis/ilm-api.md`)
(See `inference/inference-apis.md`)
(See `rest-api/info.md`)
(See `ingest/apis/index.md`)
(See `licensing/index.md`)
(See `rest-api/logstash/index.md`)
(See `ml/common/apis/ml-apis.md`)
(See `ml/common/apis/get-ml-info.md`)
(See `ml/common/apis/get-ml-memory.md`)
(See `ml/common/apis/set-upgrade-mode.md`)
(See `ml/anomaly-detection/apis/ml-ad-apis.md`)
(See `ml/anomaly-detection/apis/post-calendar-event.md`)
(See `ml/anomaly-detection/apis/put-calendar-job.md`)
(See `ml/anomaly-detection/apis/close-job.md`)
(See `ml/anomaly-detection/apis/put-job.md`)
(See `ml/anomaly-detection/apis/put-calendar.md`)
(See `ml/anomaly-detection/apis/put-datafeed.md`)
(See `ml/anomaly-detection/apis/put-filter.md`)
(See `ml/anomaly-detection/apis/delete-calendar.md`)
(See `ml/anomaly-detection/apis/delete-datafeed.md`)
(See `ml/anomaly-detection/apis/delete-calendar-event.md`)
(See `ml/anomaly-detection/apis/delete-filter.md`)
(See `ml/anomaly-detection/apis/delete-forecast.md`)
(See `ml/anomaly-detection/apis/delete-job.md`)
(See `ml/anomaly-detection/apis/delete-calendar-job.md`)
(See `ml/anomaly-detection/apis/delete-snapshot.md`)
(See `ml/anomaly-detection/apis/delete-expired-data.md`)
(See `ml/anomaly-detection/apis/estimate-model-memory.md`)
(See `ml/anomaly-detection/apis/flush-job.md`)
(See `ml/anomaly-detection/apis/forecast.md`)
(See `ml/anomaly-detection/apis/get-bucket.md`)
(See `ml/anomaly-detection/apis/get-calendar.md`)
(See `ml/anomaly-detection/apis/get-category.md`)
(See `ml/anomaly-detection/apis/get-datafeed.md`)
(See `ml/anomaly-detection/apis/get-datafeed-stats.md`)
(See `ml/anomaly-detection/apis/get-influencer.md`)
(See `ml/anomaly-detection/apis/get-job.md`)
(See `ml/anomaly-detection/apis/get-job-stats.md`)
(See `ml/anomaly-detection/apis/get-snapshot.md`)
(See `ml/anomaly-detection/apis/get-job-model-snapshot-upgrade-stats.md`)
(See `ml/anomaly-detection/apis/get-overall-buckets.md`)
(See `ml/anomaly-detection/apis/get-calendar-event.md`)
(See `ml/anomaly-detection/apis/get-filter.md`)
(See `ml/anomaly-detection/apis/get-record.md`)
(See `ml/anomaly-detection/apis/open-job.md`)
(See `ml/anomaly-detection/apis/post-data.md`)
(See `ml/anomaly-detection/apis/preview-datafeed.md`)
(See `ml/anomaly-detection/apis/reset-job.md`)
(See `ml/anomaly-detection/apis/revert-snapshot.md`)
(See `ml/anomaly-detection/apis/start-datafeed.md`)
(See `ml/anomaly-detection/apis/stop-datafeed.md`)
(See `ml/anomaly-detection/apis/update-datafeed.md`)
(See `ml/anomaly-detection/apis/update-filter.md`)
(See `ml/anomaly-detection/apis/update-job.md`)
(See `ml/anomaly-detection/apis/update-snapshot.md`)
(See `ml/anomaly-detection/apis/upgrade-job-model-snapshot.md`)

(See `ml/df-analytics/apis/ml-df-analytics-apis.md`)
(See `ml/df-analytics/apis/put-dfanalytics.md`)
(See `ml/df-analytics/apis/delete-dfanalytics.md`)
(See `ml/df-analytics/apis/evaluate-dfanalytics.md`)
(See `ml/df-analytics/apis/explain-dfanalytics.md`)
(See `ml/df-analytics/apis/get-dfanalytics.md`)
(See `ml/df-analytics/apis/get-dfanalytics-stats.md`)
(See `ml/df-analytics/apis/preview-dfanalytics.md`)
(See `ml/df-analytics/apis/start-dfanalytics.md`)
(See `ml/df-analytics/apis/stop-dfanalytics.md`)
(See `ml/df-analytics/apis/update-dfanalytics.md`)
(See `ml/trained-models/apis/ml-trained-models-apis.md`)
(See `ml/trained-models/apis/clear-trained-model-deployment-cache.md`)
(See `ml/trained-models/apis/put-trained-models-aliases.md`)
(See `ml/trained-models/apis/put-trained-model-definition-part.md`)
(See `ml/trained-models/apis/put-trained-models.md`)
(See `ml/trained-models/apis/put-trained-model-vocabulary.md`)
(See `ml/trained-models/apis/delete-trained-models-aliases.md`)
(See `ml/trained-models/apis/delete-trained-models.md`)
(See `ml/trained-models/apis/get-trained-models.md`)
(See `ml/trained-models/apis/get-trained-models-stats.md`)
(See `ml/trained-models/apis/infer-trained-model.md`)
(See `ml/trained-models/apis/start-trained-model-deployment.md`)
(See `ml/trained-models/apis/stop-trained-model-deployment.md`)
(See `ml/trained-models/apis/update-trained-model-deployment.md`)
(See `migration/migration.md`)
(See `shutdown/apis/shutdown-api.md`)
(See `query-rules/apis/index.md`)
(See `indices/apis/reload-analyzers.md`)
(See `repositories-metering-api/repositories-metering-apis.md`)
(See `rollup/rollup-apis.md`)
(See `rest-api/root.md`)
(See `scripting/apis/script-apis.md`)
(See `search.md`)
(See `search-application/apis/index.md`)
(See `searchable-snapshots/apis/searchable-snapshots-apis.md`)
(See `rest-api/security.md`)
(See `snapshot-restore/apis/snapshot-restore-apis.md`)
(See `slm/apis/slm-api.md`)
(See `sql/apis/sql-apis.md`)
(See `synonyms/apis/synonyms-apis.md`)
(See `text-structure/apis/index.md`)
(See `transform/apis/transform-apis.md`)
(See `transform/apis/put-transform.md`)
(See `transform/apis/delete-transform.md`)
(See `transform/apis/get-transform.md`)
(See `transform/apis/get-transform-stats.md`)
(See `transform/apis/preview-transform.md`)
(See `transform/apis/reset-transform.md`)
(See `transform/apis/schedule-now-transform.md`)
(See `transform/apis/start-transform.md`)
(See `transform/apis/stop-transform.md`)
(See `transform/apis/update-transform.md`)
(See `transform/apis/upgrade-transforms.md`)
(See `rest-api/usage.md`)
(See `rest-api/watcher.md`)
(See `rest-api/defs.md`)
