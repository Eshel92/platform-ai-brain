<!-- Part 10 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.17.4

The 8.17.4 release includes the following known issues and bug fixes.

### Known issues

**Observability AI assistant Knowledge Base entries with empty text can lead to Kibana OOM or restarts.**
*Details* +
The semantic text migration can cause excessive traffic to a cluster and might eventually cause the Kibana instance to crash due to OOM, together with increase of requests to Elasticsearch & ML nodes.

The problem can occur when there is one or more empty text Knowledge Base documents.

The migration script does not handle this scenario and will indefinitely update the same document.

Because the document update involves semantic_text an ML node is kept warm further increasing the costs.

The issue involves semantic_text field type (and thus the semantic_text migration which is causing this issue), introduced in the knowledge base feature in 8.17.

*Workaround* +

1. Pause the Kibana instance if possible. If not possible, skip this step.
2. Run a dry run query to identify if you have empty Knowledge Base documents. If you have at least 1 hit, you can be affected by the problem.
```sh
GET .kibana-observability-ai-assistant-kb/_search
{
  "query": {
    "bool": {
      "must": [{ "exists": { "field": "text" }}],
      "must_not": [ { "wildcard": { "text": "*" } }
      ]
    }
  }
}
```
3. Execute the deletion. For extra safety, you might want to trigger a snapshot before executing it.
```sh
POST .kibana-observability-ai-assistant-kb/_delete_by_query
{
  "query": {
    "bool": {
      "must": [{ "exists": { "field": "text" }}],
      "must_not": [ { "wildcard": { "text": "*" } }
      ]
    }
  }
}
```

For more information, check:

* [#220339](https://github.com/elastic/kibana/issues/220339)
* [#220342](https://github.com/elastic/kibana/issues/220342)

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

### Fixes

Dashboards and Visualizations::
* Prevents unnecessary re-render when switching between View and Edit modes ({kibana-pull}213902[#213902]).
* Fixes an issue with the handling of the `viewMode` check in *Lens* ({kibana-pull}213887[#213887]).
* Adds `event-annotation-group` to saved object privileges for dashboards ({kibana-pull}212926[#212926]).
Elastic Observability Solution::
* Makes Kibana retrieval namespace-specific ({kibana-pull}213505[#213505]).
* Fixes an error with the `retrieve-elastic-doc` function being unavailable ({kibana-pull}212676[#212676]).
Elastic Security solution::
For the Elastic Security 8.17.4 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Management::
* Adds support for rollup data views that reference aliases ({kibana-pull}212592[#212592]).


## Kibana 8.17.3

The 8.17.3 release includes the following known issues and bug fixes.

### Known issues

**Observability AI assistant Knowledge Base entries with empty text can lead to Kibana OOM or restarts.**
*Details* +
The semantic text migration can cause excessive traffic to a cluster and might eventually cause the Kibana instance to crash due to OOM, together with increase of requests to Elasticsearch & ML nodes.

The problem can occur when there is one or more empty text Knowledge Base documents.

The migration script does not handle this scenario and will indefinitely update the same document.

Because the document update involves semantic_text an ML node is kept warm further increasing the costs.

The issue involves semantic_text field type (and thus the semantic_text migration which is causing this issue), introduced in the knowledge base feature in 8.17.

*Workaround* +

1. Pause the Kibana instance if possible. If not possible, skip this step.
2. Run a dry run query to identify if you have empty Knowledge Base documents. If you have at least 1 hit, you can be affected by the problem.
```sh
GET .kibana-observability-ai-assistant-kb/_search
{
  "query": {
    "bool": {
      "must": [{ "exists": { "field": "text" }}],
      "must_not": [ { "wildcard": { "text": "*" } }
      ]
    }
  }
}
```
3. Execute the deletion. For extra safety, you might want to trigger a snapshot before executing it.
```sh
POST .kibana-observability-ai-assistant-kb/_delete_by_query
{
  "query": {
    "bool": {
      "must": [{ "exists": { "field": "text" }}],
      "must_not": [ { "wildcard": { "text": "*" } }
      ]
    }
  }
}
```

For more information, check:

* [#220339](https://github.com/elastic/kibana/issues/220339)
* [#220342](https://github.com/elastic/kibana/issues/220342)

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

### Bug fixes

Elastic Observability solution::
* Allows editing of non-resolving log views ({kibana-pull}210633[#210633]).
* Removes `error.id` in `getErrorGroupMainStatistics` queries ({kibana-pull}210613[#210613]).
Elastic Security solution::
For the Elastic Security 8.17.3 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Kibana security::
* Fixes the generated name for imported package titles ({kibana-pull}210916[#210916]).
* Fixes package name validation on the Data streams page ({kibana-pull}210770[#210770]).
* Handles empty categorization results from LLMs ({kibana-pull}210420[#210420]).
Platform::
* Adds versioning to inventory_view_saved_object ({kibana-pull}207007[#207007]).
Sharing::
* Reinstates switch to support generating public URLs for Embed when supported ({kibana-pull}207383[#207383]).


## Kibana 8.17.2

The 8.17.2 release includes the following known issues and bug fixes.

### Known issues

**Observability AI assistant Knowledge Base entries with empty text can lead to Kibana OOM or restarts.**
*Details* +
The semantic text migration can cause excessive traffic to a cluster and might eventually cause the Kibana instance to crash due to OOM, together with increase of requests to Elasticsearch & ML nodes.

The problem can occur when there is one or more empty text Knowledge Base documents.

The migration script does not handle this scenario and will indefinitely update the same document.

Because the document update involves semantic_text an ML node is kept warm further increasing the costs.

The issue involves semantic_text field type (and thus the semantic_text migration which is causing this issue), introduced in the knowledge base feature in 8.17.

*Workaround* +

1. Pause the Kibana instance if possible. If not possible, skip this step.
2. Run a dry run query to identify if you have empty Knowledge Base documents. If you have at least 1 hit, you can be affected by the problem.
```sh
GET .kibana-observability-ai-assistant-kb/_search
{
  "query": {
    "bool": {
      "must": [{ "exists": { "field": "text" }}],
      "must_not": [ { "wildcard": { "text": "*" } }
      ]
    }
  }
}
```
3. Execute the deletion. For extra safety, you might want to trigger a snapshot before executing it.
```sh
POST .kibana-observability-ai-assistant-kb/_delete_by_query
{
  "query": {
    "bool": {
      "must": [{ "exists": { "field": "text" }}],
      "must_not": [ { "wildcard": { "text": "*" } }
      ]
    }
  }
}
```

For more information, check:

* [#220339](https://github.com/elastic/kibana/issues/220339)
* [#220342](https://github.com/elastic/kibana/issues/220342)

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

### Bug fixes

Discover::
* Fixes an issue where `KEEP` columns are not applied after Elasticsearch error ({kibana-pull}205833[#205833]).
Elastic Observability solution::
* Fixes monitor status rule for empty KQL query results ({kibana-pull}208922[#208922]).
* Fixes knowledge base installation state ({kibana-pull}206130[#206130]).


## Kibana 8.17.1

The 8.17.1 release includes the following known issues, enhancements, and bug fixes.

### Known issues

**Upgrade Assistant displays configured source mode in mappings as critical deprecation issue.**
*Details* +
When upgrading to a newer version, the Upgrade Assistant displays critical warnings for the deprecation of configuring source mode in mappings. These warnings can safely be ignored.

For more information, refer to [#206400](https://github.com/elastic/kibana/issues/206400).
**Observability AI assistant Knowledge Base entries with empty text can lead to Kibana OOM or restarts.**
*Details* +
The semantic text migration can cause excessive traffic to a cluster and might eventually cause the Kibana instance to crash due to OOM, together with increase of requests to Elasticsearch & ML nodes.

The problem can occur when there is one or more empty text Knowledge Base documents.

The migration script does not handle this scenario and will indefinitely update the same document.

Because the document update involves semantic_text an ML node is kept warm further increasing the costs.

The issue involves semantic_text field type (and thus the semantic_text migration which is causing this issue), introduced in the knowledge base feature in 8.17.

*Workaround* +

1. Pause the Kibana instance if possible. If not possible, skip this step.
2. Run a dry run query to identify if you have empty Knowledge Base documents. If you have at least 1 hit, you can be affected by the problem.
```sh
GET .kibana-observability-ai-assistant-kb/_search
{
  "query": {
    "bool": {
      "must": [{ "exists": { "field": "text" }}],
      "must_not": [ { "wildcard": { "text": "*" } }
      ]
    }
  }
}
```
3. Execute the deletion. For extra safety, you might want to trigger a snapshot before executing it.
```sh
POST .kibana-observability-ai-assistant-kb/_delete_by_query
{
  "query": {
    "bool": {
      "must": [{ "exists": { "field": "text" }}],
      "must_not": [ { "wildcard": { "text": "*" } }
      ]
    }
  }
}
```

For more information, check:

* [#220339](https://github.com/elastic/kibana/issues/220339)
* [#220342](https://github.com/elastic/kibana/issues/220342)

**PDF and PNG reports time out and fail with an invalid header error if server.protocol is set to http2**
*Details* +
If you've changed the `server.protocol` value to `http2`, PDF and PNG reports will fail when you export them from the dashboard, visualization, or Canvas workpad that you're generating a report for.

*Workaround* +
To temporarily resolve the issue, set `server.protocol` to `http1`. 

*Resolved* +
This issue is resolved in 8.17.9, 8.18.4, 8.19.0 and later. 

### Enhancements

Management::
* Supports wildcards for transforms in the alerting rule flyout ({kibana-pull}204226[#204226]).

### Bug fixes

Discover::
* Fixes a bug with adding comments in multiple lines ({kibana-pull}203966[#203966]).
Elastic Observability solution::
* Uses architecture-specific ELSER models ({kibana-pull}205851[#205851]).
* Stringifies ignored values before rendering ({kibana-pull}203312[#203312]).
* Fixes an issue with the `ViewInAppUrl` Custom Threshold Rule routing to the default space instead of the space where it was created ({kibana-pull}201793[#201793]).
Elastic Search solution::
* Align native box connector configs ({kibana-pull}203241[#203241]).
Kibana platform::
* Fixes an issue with short URLs not working for dashboards ({kibana-pull}197484[#197484]).
