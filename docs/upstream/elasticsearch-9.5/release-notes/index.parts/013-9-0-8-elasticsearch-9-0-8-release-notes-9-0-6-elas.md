<!-- Part 13 of 18 of release-notes/index.md (split because the page is big). -->

## 9.0.8 [elasticsearch-9.0.8-release-notes]

### Highlights [elasticsearch-9.0.8-highlights]

::::{dropdown} Security advisory
The 9.0.8 release contains fixes for potential security vulnerabilities. Please see our [security advisory](https://discuss.elastic.co/c/announcements/security-announcements/31) for more details.
::::

### Features and enhancements [elasticsearch-9.0.8-features-enhancements]

Audit:
* Change reindex to use ::es-redacted:: filtering [#135414](https://github.com/elastic/elasticsearch/pull/135414)

Authorization:
* [Island Browser] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third party agent indices `kibana_system` [#134636](https://github.com/elastic/elasticsearch/pull/134636) (issue: [#134136](https://github.com/elastic/elasticsearch/issues/134136))

Infra/Plugins:
* Add Reason field to elastic-agent upgrade details metadata [#134711](https://github.com/elastic/elasticsearch/pull/134711)


### Fixes [elasticsearch-9.0.8-fixes]

Aggregations:
* Propagates filter() to aggregation functions' surrogates [#134461](https://github.com/elastic/elasticsearch/pull/134461) (issue: [#134380](https://github.com/elastic/elasticsearch/issues/134380))

ES|QL:
* Fix async get results with inconsistent headers [#135078](https://github.com/elastic/elasticsearch/pull/135078) (issue: [#135042](https://github.com/elastic/elasticsearch/issues/135042))

Engine:
* Bypass MMap arena grouping as this has caused issues with too many regions being mapped [#135012](https://github.com/elastic/elasticsearch/pull/135012)
* Fix deadlock in `ThreadPoolMergeScheduler` when a failing merge closes the `IndexWriter` [#134656](https://github.com/elastic/elasticsearch/pull/134656)

Geo:
* `CentroidCalculator` does not return negative summation weights [#135176](https://github.com/elastic/elasticsearch/pull/135176) (issue: [#131861](https://github.com/elastic/elasticsearch/issues/131861))

Infra/Node Lifecycle:
* Fix systemd notify to use a shared arena [#135235](https://github.com/elastic/elasticsearch/pull/135235)

Ingest Node:
* Correctly apply field path to JSON processor when adding contents to document root [#135479](https://github.com/elastic/elasticsearch/pull/135479)

Machine Learning:
* Add .reindexed-v7-ml-anomalies-* to anomaly results template index pattern [#135270](https://github.com/elastic/elasticsearch/pull/135270)
* Gracefully shutdown model deployment when node is removed from assignment routing [#134673](https://github.com/elastic/elasticsearch/pull/134673)
* Reset health status on successful empty checkpoint [#135653](https://github.com/elastic/elasticsearch/pull/135653) (issue: [#135650](https://github.com/elastic/elasticsearch/issues/135650))

Mapping:
* Fix for creating semantic_text fields on pre-8.11 indices crashing Elasticsearch [#135845](https://github.com/elastic/elasticsearch/pull/135845)

Search:
* Fix KQL case-sensitivity for keyword fields in ES|QL [#135776](https://github.com/elastic/elasticsearch/pull/135776) (issue: [#135772](https://github.com/elastic/elasticsearch/issues/135772))
* Prevent field caps from failing due to can match failure [#134134](https://github.com/elastic/elasticsearch/pull/134134) (issue: [#116106](https://github.com/elastic/elasticsearch/issues/116106))

Transform:
* Fix a bug in the GET _transform API that incorrectly claims some Transform configurations are missing [#134963](https://github.com/elastic/elasticsearch/pull/134963) (issue: [#134263](https://github.com/elastic/elasticsearch/issues/134263))
* Prevent Transform from queuing too many PIT close requests by waiting for PIT to close before finishing the checkpoint [#134955](https://github.com/elastic/elasticsearch/pull/134955) (issue: [#134925](https://github.com/elastic/elasticsearch/issues/134925))




## 9.1.5 [elasticsearch-9.1.5-release-notes]

### Highlights [elasticsearch-9.1.5-highlights]

::::{dropdown} Security advisory
The 9.1.5 release contains fixes for potential security vulnerabilities. Please see our [security advisory](https://discuss.elastic.co/c/announcements/security-announcements/31) for more details.
::::

::::{dropdown} Prevent LIMIT + MV_EXPAND before remote ENRICH
Queries using LIMIT followed by MV_EXPAND before a remote ENRICH can produce incorrect results due to distributed execution semantics.
These queries are now unsupported and produce an error. Example:

```yaml
FROM *:events | SORT @timestamp | LIMIT 2 | MV_EXPAND ip | ENRICH _remote:clientip_policy ON ip
```

To avoid this error, reorder your query, for example by moving ENRICH earlier in the pipeline.
::::

### Features and enhancements [elasticsearch-9.1.5-features-enhancements]

Audit:
* Change reindex to use ::es-redacted:: filtering [#135414](https://github.com/elastic/elasticsearch/pull/135414)

Authorization:
* [Island Browser] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third party agent indices `kibana_system` [#134636](https://github.com/elastic/elasticsearch/pull/134636) (issue: [#134136](https://github.com/elastic/elasticsearch/issues/134136))


### Fixes [elasticsearch-9.1.5-fixes]

Aggregations:
* Propagates filter() to aggregation functions' surrogates [#134461](https://github.com/elastic/elasticsearch/pull/134461) (issue: [#134380](https://github.com/elastic/elasticsearch/issues/134380))

Codec:
* Address es819 tsdb doc values format performance bug [#135505](https://github.com/elastic/elasticsearch/pull/135505) (issue: [#135340](https://github.com/elastic/elasticsearch/issues/135340))

ES|QL:
* Ban Limit + `MvExpand` before remote Enrich [#135051](https://github.com/elastic/elasticsearch/pull/135051)
* Fix async get results with inconsistent headers [#135078](https://github.com/elastic/elasticsearch/pull/135078) (issue: [#135042](https://github.com/elastic/elasticsearch/issues/135042))
* Fix expiration time in ES|QL async [#135209](https://github.com/elastic/elasticsearch/pull/135209) (issue: [#135169](https://github.com/elastic/elasticsearch/issues/135169))

Engine:
* Bypass MMap arena grouping as this has caused issues with too many regions being mapped [#135012](https://github.com/elastic/elasticsearch/pull/135012)
* Fix deadlock in `ThreadPoolMergeScheduler` when a failing merge closes the `IndexWriter` [#134656](https://github.com/elastic/elasticsearch/pull/134656)

Geo:
* `CentroidCalculator` does not return negative summation weights [#135176](https://github.com/elastic/elasticsearch/pull/135176) (issue: [#131861](https://github.com/elastic/elasticsearch/issues/131861))

Infra/Core:
* Bug fix: Facilitate second retrieval of the same value [#134790](https://github.com/elastic/elasticsearch/pull/134790) (issue: [#134770](https://github.com/elastic/elasticsearch/issues/134770))

Infra/Node Lifecycle:
* Fix systemd notify to use a shared arena [#135235](https://github.com/elastic/elasticsearch/pull/135235)

Ingest Node:
* Correctly apply field path to JSON processor when adding contents to document root [#135479](https://github.com/elastic/elasticsearch/pull/135479)

Machine Learning:
* Add .reindexed-v7-ml-anomalies-* to anomaly results template index pattern [#135270](https://github.com/elastic/elasticsearch/pull/135270)
* Gracefully shutdown model deployment when node is removed from assignment routing [#134673](https://github.com/elastic/elasticsearch/pull/134673)
* Reset health status on successful empty checkpoint [#135653](https://github.com/elastic/elasticsearch/pull/135653) (issue: [#135650](https://github.com/elastic/elasticsearch/issues/135650))
* Tolerate mixed types in datafeed stats sort [#135096](https://github.com/elastic/elasticsearch/pull/135096)

Mapping:
* Avoid holding references to `SearchExecutionContext` in `SourceConfirmedTextQuery` [#134887](https://github.com/elastic/elasticsearch/pull/134887)
* Fix for creating semantic_text fields on pre-8.11 indices crashing Elasticsearch [#135845](https://github.com/elastic/elasticsearch/pull/135845)
* Fixed match only text block loader not working when a keyword multi field is present [#134582](https://github.com/elastic/elasticsearch/pull/134582)

Search:
* Fix KQL case-sensitivity for keyword fields in ES|QL [#135776](https://github.com/elastic/elasticsearch/pull/135776) (issue: [#135772](https://github.com/elastic/elasticsearch/issues/135772))

Transform:
* Fix a bug in the GET _transform API that incorrectly claims some Transform configurations are missing [#134963](https://github.com/elastic/elasticsearch/pull/134963) (issue: [#134263](https://github.com/elastic/elasticsearch/issues/134263))
* Prevent Transform from queuing too many PIT close requests by waiting for PIT to close before finishing the checkpoint [#134955](https://github.com/elastic/elasticsearch/pull/134955) (issue: [#134925](https://github.com/elastic/elasticsearch/issues/134925))




## 9.1.4 [elasticsearch-9.1.4-release-notes]

### Features and enhancements [elasticsearch-9.1.4-features-enhancements]

Authorization:
* [Sentinel One] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third party agent indices `kibana_system` [#133793](https://github.com/elastic/elasticsearch/pull/133793) (issue: [#133703](https://github.com/elastic/elasticsearch/issues/133703))

FIPS:
* Bump bc-fips to 1.0.2.6 [#133198](https://github.com/elastic/elasticsearch/pull/133198)

Infra/Plugins:
* Add Reason field to elastic-agent upgrade details metadata [#134711](https://github.com/elastic/elasticsearch/pull/134711)

Network:
* Upgrade Netty to 4.1.126.Final [#134182](https://github.com/elastic/elasticsearch/pull/134182)

Security:
* Bump bcpkix version [#132853](https://github.com/elastic/elasticsearch/pull/132853)


### Fixes [elasticsearch-9.1.4-fixes]

Aggregations:
* Aggs: Fix CB on reduction phase [#133398](https://github.com/elastic/elasticsearch/pull/133398)

Authorization:
* Remove `DocumentSubsetBitsetCache` locking [#133681](https://github.com/elastic/elasticsearch/pull/133681) (issue: [#132842](https://github.com/elastic/elasticsearch/issues/132842))

ES|QL:
* Reserve memory for Lucene's TopN [#134235](https://github.com/elastic/elasticsearch/pull/134235)
* Track memory in evaluators [#133392](https://github.com/elastic/elasticsearch/pull/133392)

Indices APIs:
* Fix unnecessary determinization in index pattern conflict checks [#134231](https://github.com/elastic/elasticsearch/pull/134231) (issue: [#133652](https://github.com/elastic/elasticsearch/issues/133652))

Infra/Core:
* Remove `java.xml` from system modules [#133671](https://github.com/elastic/elasticsearch/pull/133671)

Infra/Scripting:
* Update `DefBootstrap` to handle Error from `ClassValue` [#133604](https://github.com/elastic/elasticsearch/pull/133604)

Infra/Settings:
* Use latest setting value when initializing setting watch [#134091](https://github.com/elastic/elasticsearch/pull/134091) (issue: [#133701](https://github.com/elastic/elasticsearch/issues/133701))

Ingest Node:
* Avoid stale enrich results after policy execution [#133752](https://github.com/elastic/elasticsearch/pull/133752)
* Fix `allow_duplicates` edge case bug in append processor [#134319](https://github.com/elastic/elasticsearch/pull/134319)
* Fix enrich caches outdated value after policy run [#133680](https://github.com/elastic/elasticsearch/pull/133680)

Machine Learning:
* Ensuring only a single request executor object is created [#133424](https://github.com/elastic/elasticsearch/pull/133424)
* Fix double-counting of inference memory in the assignment rebalancer [#133919](https://github.com/elastic/elasticsearch/pull/133919)

Mapping:
* Allow trailing empty string field names in paths of flattened field [#133611](https://github.com/elastic/elasticsearch/pull/133611) (issue: [#130139](https://github.com/elastic/elasticsearch/issues/130139))
* Fixed a bug where text fields in LogsDB indices did not use their keyword multi fields for block loading [#134253](https://github.com/elastic/elasticsearch/pull/134253)

Network:
* Remove Transfer-Encoding from HTTP request with no content [#133775](https://github.com/elastic/elasticsearch/pull/133775)

Relevance:
* Disallow creating `semantic_text` fields in indices created prior to 8.11.0 [#133080](https://github.com/elastic/elasticsearch/pull/133080)

Search:
* KQL: Support boolean operators in field queries [#133737](https://github.com/elastic/elasticsearch/pull/133737) (issue: [#132366](https://github.com/elastic/elasticsearch/issues/132366))
* Prevent field caps from failing due to can match failure [#134134](https://github.com/elastic/elasticsearch/pull/134134) (issue: [#116106](https://github.com/elastic/elasticsearch/issues/116106))
* Use inner query for equals/hashCode() in `SourceConfirmedTextQuery` [#134451](https://github.com/elastic/elasticsearch/pull/134451) (issue: [#134432](https://github.com/elastic/elasticsearch/issues/134432))

Snapshot/Restore:
* Delay S3 repo warning if default region absent [#133848](https://github.com/elastic/elasticsearch/pull/133848)




## 9.0.7 [elasticsearch-9.0.7-release-notes]

### Features and enhancements [elasticsearch-9.0.7-features-enhancements]

Authorization:
* [Sentinel One] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third party agent indices `kibana_system` [#133793](https://github.com/elastic/elasticsearch/pull/133793) (issue: [#133703](https://github.com/elastic/elasticsearch/issues/133703))

FIPS:
* Bump bc-fips to 1.0.2.6 [#133198](https://github.com/elastic/elasticsearch/pull/133198)

Network:
* Upgrade Netty to 4.1.126.Final [#134182](https://github.com/elastic/elasticsearch/pull/134182)

Security:
* Bump bcpkix version [#132853](https://github.com/elastic/elasticsearch/pull/132853)


### Fixes [elasticsearch-9.0.7-fixes]

Authorization:
* Remove `DocumentSubsetBitsetCache` locking [#133681](https://github.com/elastic/elasticsearch/pull/133681) (issue: [#132842](https://github.com/elastic/elasticsearch/issues/132842))

Indices APIs:
* Fix unnecessary determinization in index pattern conflict checks [#134231](https://github.com/elastic/elasticsearch/pull/134231) (issue: [#133652](https://github.com/elastic/elasticsearch/issues/133652))

Infra/Core:
* Remove `java.xml` from system modules [#133671](https://github.com/elastic/elasticsearch/pull/133671)

Infra/Scripting:
* Update `DefBootstrap` to handle Error from `ClassValue` [#133604](https://github.com/elastic/elasticsearch/pull/133604)

Infra/Settings:
* Use latest setting value when initializing setting watch [#134091](https://github.com/elastic/elasticsearch/pull/134091) (issue: [#133701](https://github.com/elastic/elasticsearch/issues/133701))

Ingest Node:
* Fix `allow_duplicates` edge case bug in append processor [#134319](https://github.com/elastic/elasticsearch/pull/134319)
* Fix enrich caches outdated value after policy run [#133680](https://github.com/elastic/elasticsearch/pull/133680)

Machine Learning:
* Ensuring only a single request executor object is created [#133424](https://github.com/elastic/elasticsearch/pull/133424)
* Fix double-counting of inference memory in the assignment rebalancer [#133919](https://github.com/elastic/elasticsearch/pull/133919)

Mapping:
* Allow trailing empty string field names in paths of flattened field [#133611](https://github.com/elastic/elasticsearch/pull/133611) (issue: [#130139](https://github.com/elastic/elasticsearch/issues/130139))

Relevance:
* Disallow creating `semantic_text` fields in indices created prior to 8.11.0 [#133080](https://github.com/elastic/elasticsearch/pull/133080)

Search:
* KQL: Support boolean operators in field queries [#133737](https://github.com/elastic/elasticsearch/pull/133737) (issue: [#132366](https://github.com/elastic/elasticsearch/issues/132366))




## 9.0.6 [elasticsearch-9.0.6-release-notes]

### Highlights [elasticsearch-9.0.6-highlights]

::::{dropdown} Security advisory
The 9.0.6 release contains fixes for potential security vulnerabilities. Please see our [security advisory](https://discuss.elastic.co/c/announcements/security-announcements/31) for more details.
::::

### Features and enhancements [elasticsearch-9.0.6-features-enhancements]

Authorization:
* [ExtraHop & QualysGAV] Add `manage`, `create_index`, `read`, `index`, `write`, `delete`, permission for third party agent indices `kibana_system` [#132387](https://github.com/elastic/elasticsearch/pull/132387) (issue: [#131825](https://github.com/elastic/elasticsearch/issues/131825))

Infra/REST API:
* Limit the depth of a filter [#133113](https://github.com/elastic/elasticsearch/pull/133113)

Ingest Node:
* Upgrading to tika 3.2.2 [#133410](https://github.com/elastic/elasticsearch/pull/133410)

Packaging:
* Update bundled JDK to Java 24.0.2+12 [#133119](https://github.com/elastic/elasticsearch/pull/133119)


### Fixes [elasticsearch-9.0.6-fixes]

EQL:
* Better error message for sequences with only one clause plus UNTIL [#132638](https://github.com/elastic/elasticsearch/pull/132638)
* Fix sequences with conditions involving keys and non-keys [#133134](https://github.com/elastic/elasticsearch/pull/133134)

Ingest Node:
* Change GeoIpCache and EnrichCache to LongAdder [#132922](https://github.com/elastic/elasticsearch/pull/132922)

License:
* Limit frequency of feature last-used time updates [#133004](https://github.com/elastic/elasticsearch/pull/133004)

Machine Learning:
* Disable child span for streaming tasks [#132945](https://github.com/elastic/elasticsearch/pull/132945)
* Improve EIS auth call logs and fix revocation bug [#132546](https://github.com/elastic/elasticsearch/pull/132546)
* Preserve lost thread context in node inference action. A lost context causes a memory leak if APM tracing is enabled [#132973](https://github.com/elastic/elasticsearch/pull/132973)
