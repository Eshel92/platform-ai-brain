<!-- Part 2 of 4 of reference/elasticsearch/rest-apis/index.md (split because the page is big). -->

### [EQL](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-eql)

The EQL APIs enable you to run EQL-related operations. Event Query Language (EQL) is a query language for event-based time series data, such as logs, metrics, and traces.

| API | Description |
| --- | ----------- |
| [Submit EQL search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-eql-search) | Runs an EQL search. |
| [Get EQL search status](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-eql-get) | Retrieves the status of an asynchronous EQL search. |
| [Get EQL search results](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-eql-get) | Retrieves results of an asynchronous EQL search. |
| [Delete EQL search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-eql-delete) | Cancels an asynchronous EQL search. |


### [ES|QL](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-esql)

The ES|QL APIs enable you to run ES|QL-related operations. The Elasticsearch Query Language (ES|QL) provides a powerful way to filter, transform, and analyze data stored in Elasticsearch, and in the future in other runtimes.

| API | Description |
| --- | ----------- |
| [ES|QL Query](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-esql-query) | Executes an ES|QL query using a SQL-like syntax. |
| [ES|QL Async Submit](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-esql-async-query) | Submits an ES|QL query to run asynchronously. |
| [ES|QL Async Get](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-esql-async-query-get) | Retrieves results of an asynchronous ES|QL query. |
| [ES|QL Async Delete](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-esql-async-query-delete) | Cancels an asynchronous ES|QL query. |


### [Features](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-features)

The feature APIs enable you to introspect and manage features provided by Elasticsearch and Elasticsearch plugins.

| API | Description |
| --- | ----------- |
| [Get Features](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-features-get-features) | Lists all available features in the cluster. |
| [Reset Features](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-features-reset-features) | Resets internal state for system features. |


### [Fleet](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-fleet)

The Fleet APIs support Fleet’s use of Elasticsearch as a data store for internal agent and action data.

| API | Description |
| --- | ----------- |
| [Run Multiple Fleet Searches](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-fleet-msearch) | Runs several Fleet searches with a single API request. |
| [Run a Fleet Search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-fleet-search) | Runs a Fleet search. |
| [Get global checkpoints](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-fleet-global-checkpoints) | Get the current global checkpoints for an index. |


### [Graph explore](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-graph)

The graph explore APIs enable you to extract and summarize information about the documents and terms in an Elasticsearch data stream or index.

| API | Description |
| --- | ----------- |
| [Graph Explore](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-graph-explore) | Discovers relationships between indexed terms using relevance-based graph exploration. |


### [Index](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-indices)

The index APIs enable you to manage individual indices, index settings, aliases, mappings, and index templates.

| API | Description |
| --- | ----------- |
| [Create index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-create) | Creates a new index with optional settings and mappings. |
| [Delete index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-delete) | Deletes an existing index. |
| [Get index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-get) | Retrieves information about one or more indices. |
| [Open index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-open) | Opens a closed index to make it available for operations. |
| [Close index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-close) | Closes an index to free up resources. |
| [Shrink index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-shrink) | Shrinks an existing index into a new index with fewer primary shards. |
| [Split index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-split) | Splits an existing index into a new index with more primary shards. |
| [Clone index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-clone) | Clones an existing index into a new index. |
| [Check alias](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-exists-alias) | Manages index aliases. |
| [Update field mappings](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-put-mapping) | Updates index mappings. |
| [Get field mappings](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-get-mapping) | Retrieves index mappings. |
| [Get index settings](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-get-settings) | Retrieves settings for one or more indices. |
| [Update index settings](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-put-settings) | Updates index-level settings dynamically. |
| [Get index templates](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-get-template) | Retrieves legacy index templates. |
| [Put index template](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-put-template) | Creates or updates a legacy index template. |
| [Delete index template](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-delete-template) | Deletes a legacy index template. |
| [Get composable index templates](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-get-index-template) | Retrieves composable index templates. |
| [Put composable index template](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-put-index-template) | Creates or updates a composable index template. |
| [Delete composable index template](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-delete-index-template) | Deletes a composable index template. |
| [Get index alias](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-get-alias) | Retrieves index aliases. |
| [Delete index alias](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-delete-alias) | Deletes index aliases. |
| [Refresh index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-refresh) | Refreshes one or more indices, making recent changes searchable. |
| [Flush index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-flush) | Performs a flush operation on one or more indices. |
| [Clear index cache](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-clear-cache) | Clears caches associated with one or more indices. |
| [Force merge index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-forcemerge) | Merges index segments to reduce their number and improve performance. |
| [Rollover index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-rollover) | Rolls over an alias to a new index when conditions are met. |
| [Resolve index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-resolve-index) | Resolves expressions to index names, aliases, and data streams. |
| [Simulate index template](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-simulate-index-template) | Simulates the application of a composable index template. |
| [Simulate template](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-simulate-template) | Simulates the application of a legacy index template. |
| [Get mapping](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-get-mapping) | Retrieves mapping definitions for one or more indices. |
| [Put mapping](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-put-mapping) | Updates mapping definitions for one or more indices. |
| [Reload search analyzers](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-reload-search-analyzers) | Reloads search analyzers for one or more indices. |
| [Shrink index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-shrink) | Shrinks an existing index into a new index with fewer primary shards. |
| [Split index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-split) | Splits an existing index into a new index with more primary shards. |
| [Clone index](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-clone) | Clones an existing index into a new index. |


### [Index lifecycle management](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-ilm)

The index lifecycle management APIs enable you to set up policies to automatically manage the index lifecycle.

| API | Description |
| --- | ----------- |
| [Put Lifecycle Policy](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ilm-put-lifecycle) | Creates or updates an ILM policy. |
| [Get Lifecycle Policy](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ilm-get-lifecycle) | Retrieves one or more ILM policies. |
| [Delete Lifecycle Policy](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ilm-delete-lifecycle) | Deletes an ILM policy. |
| [Explain Lifecycle](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ilm-explain-lifecycle) | Shows the current lifecycle step for indices. |
| [Move to Step](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ilm-move-to-step) | Manually moves an index to the next step in its lifecycle. |
| [Retry Lifecycle Step](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ilm-retry) | Retries the current lifecycle step for failed indices. |
| [Start ILM](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ilm-start) | Starts the ILM plugin. |
| [Stop ILM](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ilm-stop) | Stops the ILM plugin. |
| [Get ILM Status](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ilm-get-status) | Returns the status of the ILM plugin. |


### [Inference](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-inference)

The inference APIs enable you to create inference endpoints and integrate with machine learning models of different services - such as Amazon Bedrock, Anthropic, Azure AI Studio, Cohere, Google AI, Groq, Mistral, OpenAI, or HuggingFace.

| API | Description |
| --- | ----------- |
| [Put Inference Endpoint](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put) | Creates an inference endpoint. |
| [Get Inference Endpoint](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-get) | Retrieves one or more inference endpoints. |
| [Delete Inference Endpoint](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-delete) | Deletes an inference endpoint. |
| [Infer](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-inference) | Runs inference using a deployed model. |


### [Info](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-info)

The info API provides basic build, version, and cluster information.

| API | Description |
| --- | ----------- |
| [Get cluster information](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-info) | Returns basic information about the cluster. |


### [Ingest](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-ingest)

The ingest APIs enable you to manage tasks and resources related to ingest pipelines and processors.

| API | Description |
| --- | ----------- |
| [Create or update pipeline](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ingest-put-pipeline) | Creates or updates an ingest pipeline. |
| [Get pipeline](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ingest-get-pipeline) | Retrieves one or more ingest pipelines. |
| [Delete pipeline](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ingest-delete-pipeline) | Deletes an ingest pipeline. |
| [Simulate pipeline](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ingest-simulate) | Simulates a document through an ingest pipeline. |
| [Get built-in grok patterns](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ingest-processor-grok) | Returns a list of built-in grok patterns. |


### [Licensing](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-license)

The licensing APIs enable you to manage your licenses.

| API | Description |
| --- | ----------- |
| [Get license](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-license-get) | Retrieves the current license for the cluster. |
| [Update license](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-license-post) | Updates the license for the cluster. |
| [Delete license](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-license-delete) | Removes the current license. |
| [Start basic license](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-license-post-start-basic) | Starts a basic license. |
| [Start trial license](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-license-post-start-trial) | Starts a trial license. |
| [Get the trial status](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-license-get-trial-status) | Returns the status of the current trial license. |


### [Logstash](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-logstash)

The logstash APIs enable you to manage pipelines that are used by Logstash Central Management.

| API | Description |
| --- | ----------- |
| [Create or update Logstash pipeline](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-logstash-put-pipeline) | Creates or updates a Logstash pipeline. |
| [Get Logstash pipeline](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-logstash-get-pipeline) | Retrieves one or more Logstash pipelines. |
| [Delete Logstash pipeline](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-logstash-delete-pipeline) | Deletes a Logstash pipeline. |


### [Machine learning](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-ml)

The machine learning APIs enable you to retrieve information related to the Elastic Stack machine learning features.

| API | Description |
| --- | ----------- |
| [Get machine learning memory stats](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-memory-stats) | Gets information about how machine learning jobs and trained models are using memory. |
| [Get machine learning info](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-info) | Gets defaults and limits used by machine learning. |
| [Set upgrade mode](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-set-upgrade-mode) | Sets a cluster wide upgrade_mode setting that prepares machine learning indices for an upgrade. |
| [Get ML job stats](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-job-stats) | Retrieves usage statistics for ML jobs. |
| [Get ML calendar events](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-calendar-events) | Retrieves scheduled events for ML calendars. |
| [Get ML filters](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-filters) | Retrieves ML filters. |
| [Put ML filter](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-put-filter) | Creates or updates an ML filter. |
| [Delete ML filter](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-delete-filter) | Deletes an ML filter. |
| [Get ML info](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-info) | Gets overall ML info. |
| [Get ML model snapshots](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-model-snapshots) | Retrieves model snapshots for ML jobs. |
| [Revert ML model snapshot](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-revert-model-snapshot) | Reverts an ML job to a previous model snapshot. |
| [Delete expired ML data](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-delete-expired-data) | Deletes expired ML results and model snapshots. |
