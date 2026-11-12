<!-- Part 4 of 4 of reference/elasticsearch/rest-apis/index.md (split because the page is big). -->

### [Snapshot lifecycle management](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-slm)

The snapshot lifecycle management APIs enable you to set up policies to automatically take snapshots and control how long they are retained.

| API | Description |
| --- | ----------- |
| [Get snapshot lifecycle policy](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-slm-get-lifecycle) | Retrieves one or more snapshot lifecycle policies. |
| [Create or update snapshot lifecycle policy](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-slm-put-lifecycle) | Creates or updates a snapshot lifecycle policy. |
| [Delete snapshot lifecycle policy](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-slm-delete-lifecycle) | Deletes a snapshot lifecycle policy. |
| [Execute snapshot lifecycle policy](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-slm-execute-lifecycle) | Triggers a snapshot lifecycle policy manually. |
| [Execute snapshot retention](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-slm-execute-retention) | Manually apply the retention policy to force immediate removal of snapshots that are expired according to the snapshot lifecycle policy retention rules. |
| [Get snapshot lifecycle stats](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-slm-get-stats) | Returns statistics about snapshot lifecycle executions. |
| [Get snapshot lifecycle status](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-slm-get-status) | Returns the status of the snapshot lifecycle management feature. |
| [Start snapshot lifecycle management](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-slm-start) | Starts the snapshot lifecycle management feature. |
| [Stop snapshot lifecycle management](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-slm-stop) | Stops the snapshot lifecycle management feature. |


### [SQL](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-sql)

The SQL APIs enable you to run SQL queries on Elasticsearch indices and data streams.

| API | Description |
| --- | ----------- |
| [Clear SQL cursor](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-sql-clear-cursor) | Clears the server-side cursor for an SQL search. |
| [Delete async SQL search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-sql-delete-async) | Deletes an async SQL search. |
| [Get async SQL search results](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-sql-get-async) | Retrieves results of an async SQL query. |
| [Get async SQL search status](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-sql-get-async-status) | Gets the current status of an async SQL search or a stored synchronous SQL search. |
| [SQL query](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-sql-query) | Executes an SQL query. |
| [Translate SQL](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-sql-translate) | Translates SQL into Elasticsearch DSL. |


### [Synonyms](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-synonyms)

The synonyms management APIs provide a convenient way to define and manage synonyms in an internal system index. Related synonyms can be grouped in a "synonyms set".

| API | Description |
| --- | ----------- |
| [Get synonym set](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-synonyms-get-synonym) | Retrieves a synonym set by ID. |
| [Create of update synonym set](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-synonyms-put-synonym) | Creates or updates a synonym set. |
| [Delete synonym set](https://www.elastic.co/docs/api/doc/elasticsearch/endpoint/operation/operation-synonyms-delete-synonym) | Deletes a synonym set. |
| [Get synonym rule](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-synonyms-get-synonym-rule) | |
| [Get synonym sets](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-synonyms-get-synonyms-sets) | Lists all synonym sets. |


### [Task management](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-tasks)

The task management APIs enable you to retrieve information about tasks or cancel tasks running in a cluster.

| API | Description |
| --- | ----------- |
| [Cancel a task](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-tasks-cancel) | Cancels a running task. |
| [Get task information](https://www.elastic.co/docs/api/doc/elasticsearch/v9/operation/operation-tasks-get) |  |
| [Get all tasks](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-tasks-list) | Retrieves information about running tasks. |


### [Text structure](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-text_structure)

The text structure APIs enable you to find the structure of a text field in an Elasticsearch index.

| API | Description |
| --- | ----------- |
| [Find the structure of a text field](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-text-structure-find-field-structure) |  |
| [Find the structure of a text message](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-text-structure-find-message-structure) |  |
| [Find the structure of a text file](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-text-structure-find-structure) | Analyzes a text file and returns its structure. |
| [Test a Grok pattern](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-text-structure-test-grok-pattern) |  |


### [Transform](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-transform)

The transform APIs enable you to create and manage transforms.

| API | Description |
| --- | ----------- |
| [Get transforms](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-transform-get-transform) | Retrieves configuration for one or more transforms. |
| [Create a transform](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-transform-put-transform) | Creates or updates a transform job. |
| [Get transform stats](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-transform-get-transform-stats) | Get usage information for transforms. |
| [Preview transform](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-transform-preview-transform) | Previews the results of a transform job. |
| [Reset a transform](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-transform-reset-transform) | Previews the results of a transform job. |
| [Delete transform](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-transform-delete-transform) | Deletes a transform job. |
| [Schedule a transform](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-transform-schedule-now-transform) | Previews the results of a transform job. |
| [Start transform](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-transform-start-transform) | Starts a transform job. |
| [Stop transform](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-transform-stop-transform) | Stops a running transform job. |
| [Update transform](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-transform-update-transform) | Updates certain properties of a transform. |
| [Upgrade all transforms](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-transform-upgrade-transforms) | Updates certain properties of a transform. |


### [Usage](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-xpack)

The usage API provides usage information about the installed X-Pack features.

| API | Description |
| --- | ----------- |
| [Get information](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-xpack-info) | Gets information about build details, license status, and a list of features currently available under the installed license. |
| [Get usage information](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-xpack-usage) | Get information about the features that are currently enabled and available under the current license. |



### [Watcher](https://www.elastic.co/docs/api/doc/elasticsearch/v9/group/endpoint-watcher)

You can use Watcher to watch for changes or anomalies in your data and perform the necessary actions in response.

| API | Description |
| --- | ----------- |
| [Acknowledge a watch](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-watcher-ack-watch) | Acknowledges a watch action. |
| [Activate a watch](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-watcher-activate-watch) | Activates a watch. |
| [Deactivates a watch](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-watcher-deactivate-watch) | Deactivates a watch. |
| [Get a watch](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-watcher-get-watch) | Retrieves a watch by ID. |
| [Create or update a watch](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-watcher-put-watch) | Creates or updates a watch. |
| [Delete a watch](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-watcher-delete-watch) | Deletes a watch. |
| [Run a watch](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-watcher-execute-watch) | Executes a watch manually. |
| [Get Watcher index settings](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-watcher-get-settings) | Get settings for the Watcher internal index |
| [Update Watcher index settings](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-watcher-update-settings) | Update settings for the Watcher internal index |
| [Query watches](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-watcher-query-watches) | Get all registered watches in a paginated manner and optionally filter watches by a query. |
| [Start the watch service](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-watcher-start) | Starts the Watcher service. |
| [Get Watcher statistics](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-watcher-stats) | Returns statistics about the Watcher service. |
| [Stop the watch service](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-watcher-stop) | Stops the Watcher service. |
