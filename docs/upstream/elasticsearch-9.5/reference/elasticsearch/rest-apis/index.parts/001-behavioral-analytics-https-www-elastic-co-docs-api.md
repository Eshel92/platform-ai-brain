<!-- Part 1 of 4 of reference/elasticsearch/rest-apis/index.md (split because the page is big). -->

### [Behavioral analytics](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-analytics)

```{applies_to}
stack: deprecated
```

The behavioral analytics APIs enable you to create and manage analytics collections and retrieve information about analytics collections. Behavioral Analytics is an analytics event collection platform. You can use it to analyze your users' searching and clicking behavior. Leverage this information to improve the relevance of your search results and identify gaps in your content.

| API | Description |
| --- | ----------- |
| [Get Collections](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search-application-get-behavioral-analytics) | Lists all behavioral analytics collections. |
| [Create Collection](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search-application-put-behavioral-analytics) | Creates a new behavioral analytics collection. |
| [Delete Collection](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search-application-delete-behavioral-analytics) | Deletes a behavioral analytics collection. |
| [Create Event](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search-application-post-behavioral-analytics-event) | Sends a behavioral analytics event to a collection. |


### [Compact and aligned text (CAT)](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)

The compact and aligned text (CAT) APIs return human-readable text as a response, instead of a JSON object. The CAT APIs aim are intended only for human consumption using the Kibana console or command line. They are not intended for use by applications. For application consumption, it's recommend to use a corresponding JSON API.

| API | Description |
| --- | ----------- |
| [Get aliases](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-aliases) | Returns index aliases. |
| [Get allocation](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-allocation) | Provides a snapshot of shard allocation across nodes. |
| [Get component templates](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-component-templates) | Returns information about component templates. |
| [Get count](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-count) | Returns document count for specified indices. |
| [Get fielddata](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-fielddata) | Shows fielddata memory usage by field. |
| [Get health](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-health) | Returns cluster health status. |
| [Get help](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-help) | Shows help for CAT APIs. |
| [Get index information](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-indices) | Returns index statistics. |
| [Get master](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-master) | Returns information about the elected master node. |
| [Get ml data frame analytics](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-ml-data-frame-analytics) | Returns data frame analytics jobs. |
| [Get ml datafeeds](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-ml-datafeeds) | Returns information about datafeeds. |
| [Get ml jobs](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-ml-jobs) | Returns anomaly detection jobs. |
| [Get ml trained models](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-ml-trained-models) | Returns trained machine learning models. |
| [Get nodeattrs](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-nodeattrs) | Returns custom node attributes. |
| [Get node information](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-nodes) | Returns cluster node info and statistics. |
| [Get pending tasks](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-pending-tasks) | Returns cluster pending tasks. |
| [Get plugins](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-plugins) | Returns information about installed plugins. |
| [Get recovery](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-recovery) | Returns shard recovery information. |
| [Get repositories](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-repositories) | Returns snapshot repository information. |
| [Get segments](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-segments) | Returns low-level segment information. |
| [Get shard information](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-shards) | Returns shard allocation across nodes. |
| [Get snapshots](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-snapshots) | Returns snapshot information. |
| [Get tasks](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-tasks) | Returns information about running tasks. |
| [Get templates](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-templates) | Returns index template information. |
| [Get thread pool](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-thread-pool) | Returns thread pool statistics. |
| [Get transforms](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cat-transforms) | Returns transform information. |


### [Cluster](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cluster)

The cluster APIs enable you to retrieve information about your infrastructure on cluster, node, or shard level. You can manage cluster settings and voting configuration exceptions, collect node statistics and retrieve node information.

| API | Description |
| --- | ----------- |
| [Get cluster health](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-health) | Returns health status of the cluster. |
| [Get cluster info](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-info) | Returns basic information about the cluster. |
| [Reroute cluster](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-reroute) | Manually reassigns shard allocations. |
| [Get cluster state](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-state) | Retrieves the current cluster state. |
| [Explain shard allocation](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-allocation-explain) | Get explanations for shard allocations in the cluster. |
| [Update cluster settings](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-put-settings) | Updates persistent or transient cluster settings. |
| [Get cluster stats](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-stats) | Returns cluster-wide statistics, including node, index, and shard metrics. |
| [Get cluster pending tasks](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-pending-tasks) | Lists cluster-level tasks that are pending execution. |
| [Get cluster settings](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-get-settings) | Retrieves the current cluster-wide settings, including persistent and transient settings. |
| [Get cluster remote info](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-remote-info) | Returns information about configured remote clusters for cross-cluster search and replication. |
| [Update cluster voting config exclusions](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-post-voting-config-exclusions) | Update the cluster voting config exclusions by node IDs or node names. |
| [Delete voting config exclusions](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-delete-voting-config-exclusions) | Clears voting configuration exclusions, allowing previously excluded nodes to participate in master elections. |
| [Exclude nodes from voting](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-post-voting-config-exclusions) | Excludes nodes from voting in master elections. |
| [Clear voting config exclusions](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-delete-voting-config-exclusions) | Clears voting config exclusions. |


### [Cluster - Health](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-health_report)

The cluster - health API provides you a report with the health status of an Elasticsearch cluster.

| API | Description |
| --- | ----------- |
| [Get cluster health report](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-health-report) | Returns health status of the cluster, including index-level details. |


### [Connector](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-connector)

The connector and sync jobs APIs provide a convenient way to create and manage Elastic connectors and sync jobs in an internal index.

| API | Description |
| --- | ----------- |
| [Get connector](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-get) | Retrieves a connector configuration. |
| [Put connector](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-put) | Creates or updates a connector configuration. |
| [Delete connector](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-delete) | Deletes a connector configuration. |
| [Start connector sync job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-sync-job-post) | Starts a sync job for a connector. |
| [Get connector sync job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-sync-job-get) | Retrieves sync job details for a connector. |
| [Get all connectors](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-list) | Retrieves a list of all connector configurations. |
| [Get all connector sync jobs](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-sync-job-list) | Retrieves a list of all connector sync jobs. |
| [Delete connector sync job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-sync-job-delete) | Deletes a connector sync job. |

The connector and sync jobs APIs provide a convenient way to create and manage Elastic connectors and sync jobs in an internal index.

| API | Description |
| --- | ----------- |
| [Get connector](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-get) | Retrieves a connector configuration. |
| [Put connector](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-put) | Creates or updates a connector configuration. |
| [Delete connector](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-delete) | Deletes a connector configuration. |
| [Start connector sync job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-sync-job-post) | Starts a sync job for a connector. |
| [Get connector sync job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-sync-job-get) | Retrieves sync job details for a connector. |


### [Cross-cluster replication (CCR)](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ccr)

The cross-cluster replication (CCR) APIs enable you to run cross-cluster replication operations, such as creating and managing follower indices or auto-follow patterns. With CCR, you can replicate indices across clusters to continue handling search requests in the event of a datacenter outage, prevent search volume from impacting indexing throughput, and reduce search latency by processing search requests in geo-proximity to the user.

| API | Description |
| --- | ----------- |
| [Create or update auto-follow pattern](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ccr-put-auto-follow-pattern) | Creates or updates an auto-follow pattern. |
| [Delete auto-follow pattern](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ccr-delete-auto-follow-pattern) | Deletes an auto-follow pattern. |
| [Get auto-follow pattern](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ccr-get-auto-follow-pattern) | Retrieves auto-follow pattern configuration. |
| [Pause auto-follow pattern](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ccr-pause-auto-follow-pattern) | Pauses an auto-follow pattern. |
| [Resume auto-follow pattern](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ccr-resume-auto-follow-pattern) | Resumes a paused auto-follow pattern. |
| [Forget follower](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ccr-forget-follower) | Removes follower retention leases from leader index. |
| [Create follower](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ccr-follow) | Creates a follower index. |
| [Get follower](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ccr-follow-info) | Retrieves information about follower indices. |
| [Get follower stats](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ccr-follow-stats) | Retrieves stats about follower indices. |
| [Pause follower](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ccr-pause-follow) | Pauses replication of a follower index. |
| [Resume follower](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ccr-resume-follow) | Resumes replication of a paused follower index. |
| [Unfollow index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ccr-unfollow) | Converts a follower index into a regular index. |
| [Get CCR stats](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ccr-stats) | Retrieves overall CCR statistics for the cluster. |


### [Data stream](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-data-stream)

The data stream APIs enable you to create and manage data streams and data stream lifecycles. A data stream lets you store append-only time series data across multiple indices while giving you a single named resource for requests. Data streams are well-suited for logs, events, metrics, and other continuously generated data.

| API | Description |
| --- | ----------- |
| [Create data stream](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-create-data-stream) | Creates a new data stream. |
| [Delete data stream](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-delete-data-stream) | Deletes an existing data stream. |
| [Get data stream](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-get-data-stream) | Retrieves one or more data streams. |
| [Modify data stream](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-modify-data-stream) | Updates the backing index configuration for a data stream. |
| [Promote data stream write index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-promote-data-stream) | Promotes a backing index to be the write index. |
| [Data streams stats](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-data-streams-stats) | Returns statistics about data streams. |
| [Migrate to data stream](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-migrate-to-data-stream) | Migrates an index or indices to a data stream. |


### [Document](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-document)

The document APIs enable you to create and manage documents in an Elasticsearch index.

| API | Description |
| --- | ----------- |
| [Index document](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-create) | Indexes a document into a specific index. |
| [Get document](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-get) | Retrieves a document by ID. |
| [Delete document](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-delete) | Deletes a document by ID. |
| [Update document](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-update) | Updates a document using a script or partial doc. |
| [Bulk](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-bulk) | Performs multiple indexing or delete operations in a single API call. |
| [Multi-get document](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-mget) | Retrieves multiple documents by ID in one request. |
| [Update documents by query](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-update-by-query) | Updates documents that match a query. |
| [Delete documents by query](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-delete-by-query) | Deletes documents that match a query. |
| [Get term vectors](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-termvectors) | Retrieves term vectors for a document. |
| [Multi-termvectors](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-mtermvectors) | Retrieves term vectors for multiple documents. |
| [Reindex](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-reindex) | Copies documents from one index to another. |
| [Reindex Rethrottle](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-reindex-rethrottle) | Changes the throttle for a running reindex task. |
| [Explain](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-explain) | Explains how a document matches (or doesn't match) a query. |
| [Get source](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-get-source) | Retrieves the source of a document by ID. |
| [Exists](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-exists) | Checks if a document exists by ID. |


### [Enrich](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-enrich)

The enrich APIs enable you to manage enrich policies. An enrich policy is a set of configuration options used to add the right enrich data to the right incoming documents.

| API | Description |
| --- | ----------- |
| [Create or update enrich policy](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-enrich-put-policy) | Creates or updates an enrich policy. |
| [Get enrich policy](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-enrich-get-policy) | Retrieves enrich policy definitions. |
| [Delete enrich policy](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-enrich-delete-policy) | Deletes an enrich policy. |
| [Execute enrich policy](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-enrich-execute-policy) | Executes an enrich policy to create an enrich index. |
| [Get enrich stats](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-enrich-stats) | Returns enrich coordinator and policy execution statistics. |
