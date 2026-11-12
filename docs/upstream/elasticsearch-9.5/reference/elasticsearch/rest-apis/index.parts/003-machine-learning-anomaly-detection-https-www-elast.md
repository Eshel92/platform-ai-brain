<!-- Part 3 of 4 of reference/elasticsearch/rest-apis/index.md (split because the page is big). -->

### [Machine learning anomaly detection](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-ml-anomaly)

The machine learning anomaly detection APIs enable you to perform anomaly detection activities.


| API | Description |
| --- | ----------- |
| [Put Job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-put-job) | Creates an anomaly detection job. |
| [Get Job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-jobs) | Retrieves configuration info for anomaly detection jobs. |
| [Delete Job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-delete-job) | Deletes an anomaly detection job. |
| [Open Job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-open-job) | Opens an existing anomaly detection job. |
| [Close anomaly detection jobs](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-close-job) | Closes an anomaly detection job. |
| [Flush Job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-flush-job) | Forces any buffered data to be processed. |
| [Forecast Job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-forecast) | Generates forecasts for anomaly detection jobs. |
| [Get Buckets](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-buckets) | Retrieves bucket results from a job. |
| [Get Records](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-records) | Retrieves anomaly records for a job. |
| [Get calendar configuration info](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-calendars) | Gets calendar configuration information. |
| [Create a calendar](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-put-calendar) | Create a calendar. |
| [Delete a calendar](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-delete-calendar) | Delete a calendar. |
| [Delete events from a calendar](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-delete-calendar) | Delete events from a calendar. |
| [Add anomaly detection job to calendar](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-put-calendar-job) | Add an anomaly detection job to a calendar. |
| [Delete anomaly detection jobs from calendar](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-delete-calendar-job) | Deletes anomaly detection jobs from a calendar. |
| [Get datafeeds configuration info](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-datafeeds) | Get configuration information for a datafeed. |
| [Create datafeed](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-put-datafeed) | Creates a datafeed. |
| [Delete a datafeed](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-delete-datafeed) | Deletes a datafeed. |
| [Delete expired ML data](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-delete-expired-data) | Delete all job results, model snapshots and forecast data that have exceeded their retention days period.  |
| [Delete expired ML data](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-delete-expired-data) | Delete all job results, model snapshots and forecast data that have exceeded their retention days period.  |
| [Get filters](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-filters) | Get a single filter or all filters. |
| [Get anomaly detection job results for influencers](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-influencers) | Get anomaly detection job results for entities that contributed to or are to blame for anomalies. |
| [Get anomaly detection job stats](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-job-stats) | Get anomaly detection job stats. |
| [Get anomaly detection jobs configuration info](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-jobs) | You can get information for multiple anomaly detection jobs in a single API request by using a group name, a comma-separated list of jobs, or a wildcard expression. |


### [Machine learning data frame analytics](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-ml-data-frame)

The machine learning data frame analytics APIs enable you to perform data frame analytics activities.

| API | Description |
| --- | ----------- |
| [Create a data frame analytics job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-put-data-frame-analytics) | Creates a data frame analytics job. |
| [Get data frame analytics job configuration info](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-data-frame-analytics) | Retrieves configuration and results for analytics jobs. |
| [Delete a data frame analytics job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-delete-data-frame-analytics) | Deletes a data frame analytics job. |
| [Start a data frame analytics job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-start-data-frame-analytics) | Starts a data frame analytics job. |
| [Stop data frame analytics jobs](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-stop-data-frame-analytics) | Stops a running data frame analytics job. |


### [Machine learning trained models](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-ml-trained-model)

The machine learning trained models APIs enable you to perform model management operations.

| API | Description |
| --- | ----------- |
| [Put Trained Model](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-put-trained-model) | Uploads a trained model for inference. |
| [Get Trained Models](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-trained-models) | Retrieves configuration and stats for trained models. |
| [Delete Trained Model](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-delete-trained-model) | Deletes a trained model. |
| [Start Deployment](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-start-trained-model-deployment) | Starts a trained model deployment. |
| [Stop Deployment](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-stop-trained-model-deployment) | Stops a trained model deployment. |
| [Get Deployment Stats](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ml-get-trained-models-stats) | Retrieves stats for deployed models. |


### [Migration](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-migration)

The migration APIs power Kibana's Upgrade Assistant feature.


| API | Description |
| --- | ----------- |
| [Deprecation Info](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-migration-deprecations) | Retrieves deprecation warnings for cluster and indices. |
| [Get Feature Upgrade Status](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-migration-get-feature-upgrade-status) | Checks upgrade status of system features. |
| [Post Feature Upgrade](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-migration-post-feature-upgrade) | Upgrades internal system features after a version upgrade. |


### [Query rules](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-query_rules)

Query rules enable you to configure per-query rules that are applied at query time to queries that match the specific rule. Query rules are organized into rulesets, collections of query rules that are matched against incoming queries. Query rules are applied using the rule query. If a query matches one or more rules in the ruleset, the query is re-written to apply the rules before searching. This allows pinning documents for only queries that match a specific term.

| API | Description |
| --- | ----------- |
| [Create or update query ruleset](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-query-rules-put-ruleset) | Creates or updates a query ruleset. |
| [Get query ruleset](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-query-rules-get-ruleset) | Retrieves one or more query rulesets. |
| [Delete query ruleset](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-query-rules-delete-ruleset) | Deletes a query ruleset. |


### [Rollup](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-rollup)

The rollup APIs enable you to create, manage, and retrieve information about rollup jobs.

| API | Description |
| --- | ----------- |
| [Create or update rollup job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-rollup-put-job) | Creates or updates a rollup job for summarizing historical data. |
| [Get rollup jobs](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-rollup-get-jobs) | Retrieves configuration for one or more rollup jobs. |
| [Delete rollup job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-rollup-delete-job) | Deletes a rollup job. |
| [Start rollup job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-rollup-start-job) | Starts a rollup job. |
| [Stop rollup job](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-rollup-stop-job) | Stops a running rollup job. |
| [Get rollup capabilities](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-rollup-get-rollup-caps) | Returns the capabilities of rollup jobs. |
| [Search rollup data](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-rollup-rollup-search) | Searches rolled-up data using a rollup index. |


### [Script](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-script)

Use the script support APIs to get a list of supported script contexts and languages. Use the stored script APIs to manage stored scripts and search templates.


| API | Description |
| --- | ----------- |
| [Add or update stored script](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-put-script) | Adds or updates a stored script. |
| [Get stored script](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-get-script) | Retrieves a stored script. |
| [Delete stored script](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-delete-script) | Deletes a stored script. |
| [Execute Painless script](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-scripts-painless-execute) | Executes a script using the Painless language. |
| [Get script contexts](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-get-script-context) | Returns available script execution contexts. |
| [Get script languages](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-get-script-languages) | Returns available scripting languages. |


### [Search](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-search)

The search APIs enable you to search and aggregate data stored in Elasticsearch indices and data streams.

| API | Description |
| --- | ----------- |
| [Search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search) | Executes a search query on one or more indices. |
| [Multi search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-msearch) | Executes multiple search requests in a single API call. |
| [Search template](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search-template) | Executes a search using a stored or inline template. |
| [Render search template](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-render-search-template) | Renders a search template with parameters. |
| [Explain search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-explain) | Explains how a document scores against a query. |
| [Get field capabilities](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-field-caps) | Returns the capabilities of fields across indices. |
| [Scroll search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-scroll) | Efficiently retrieves large numbers of results (pagination). |
| [Clear scroll](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-clear-scroll) | Clears search contexts for scroll requests. |


### [Search application](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-search_application)

The search application APIs enable you to manage tasks and resources related to Search Applications.

| API | Description |
| --- | ----------- |
| [Create or update search application](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search-application-put) | Creates or updates a search application. |
| [Get search application](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search-application-get) | Retrieves a search application by name. |
| [Delete search application](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search-application-delete) | Deletes a search application. |
| [Search search application](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search-application-search) | Executes a search using a search application. |


### [Searchable snapshots](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-searchable_snapshots)

The searchable snapshots APIs enable you to perform searchable snapshots operations.

| API | Description |
| --- | ----------- |
| [Mount searchable snapshot](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-searchable-snapshots-mount) | Mounts a snapshot as a searchable index. |
| [Clear searchable snapshot cache](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-searchable-snapshots-clear-cache) | Clears the cache of searchable snapshots. |
| [Get searchable snapshot stats](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-searchable-snapshots-stats) | Returns stats about searchable snapshots. |


### [Security](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-security)

The security APIs enable you to perform security activities, and add, update, retrieve, and remove application privileges, role mappings, and roles. You can also create and update API keys and create and invalidate bearer tokens.


| API | Description |
| --- | ----------- |
| [Create or update user](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-put-user) | Creates or updates a user in the native realm. |
| [Get user](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-get-user) | Retrieves one or more users. |
| [Delete user](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-delete-user) | Deletes a user from the native realm. |
| [Create or update role](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-put-role) | Creates or updates a role. |
| [Get role](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-get-role) | Retrieves one or more roles. |
| [Delete role](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-delete-role) | Deletes a role. |
| [Create API key](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-create-api-key) | Creates an API key for access without basic auth. |
| [Invalidate API key](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-invalidate-api-key) | Invalidates one or more API keys. |
| [Authenticate](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-authenticate) | Retrieves information about the authenticated user. |


### [Snapshot and restore](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-snapshot)

The snapshot and restore APIs enable you to set up snapshot repositories, manage snapshot backups, and restore snapshots to a running cluster.

| API | Description |
| --- | ----------- |
| [Clean up snapshot repository](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-snapshot-cleanup-repository) | Removes stale data from a repository. |
| [Clone snapshot](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-snapshot-clone) | Clones indices from a snapshot into a new snapshot. |
| [Get snapshot](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-snapshot-get) | Retrieves information about snapshots. |
| [Create snapshot](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-snapshot-create) | Creates a snapshot of one or more indices. |
| [Delete snapshot](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-snapshot-delete) | Deletes a snapshot from a repository. |
| [Get snapshot repository](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-snapshot-get-repository) | Retrieves information about snapshot repositories. |
| [Create or update snapshot repository](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-snapshot-create-repository) | Registers or updates a snapshot repository. |
| [Delete snapshot repository](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-snapshot-delete-repository) | Deletes a snapshot repository. |
| [Restore snapshot](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-snapshot-restore) | Restores a snapshot. |
| [Analyze snapshot repository](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-snapshot-repository-analyze) | Analyzes a snapshot repository for correctness and performance. |
| [Verify snapshot repository](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-snapshot-repository-verify-integrity) | Verifies access to a snapshot repository. |
| [Get snapshot status](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-snapshot-status) | Gets the status of a snapshot. |
