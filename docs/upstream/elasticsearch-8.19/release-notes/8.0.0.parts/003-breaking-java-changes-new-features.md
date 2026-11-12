<!-- Part 3 of 5 of release-notes/8.0.0.md (split because the page is big). -->

### Breaking Java changes

Authentication::
* Mandate x-pack REST handler installed [#71061](https://github.com/elastic/elasticsearch/pull/71061) (issue: [#70523](https://github.com/elastic/elasticsearch/issues/70523))

CCR::
* Remove the `CcrClient` [#42816](https://github.com/elastic/elasticsearch/pull/42816)

CRUD::
* Remove types from `BulkRequest` [#46983](https://github.com/elastic/elasticsearch/pull/46983) (issue: [#41059](https://github.com/elastic/elasticsearch/issues/41059))
* Remove `Client.prepareIndex(index, type, id)` method [#48443](https://github.com/elastic/elasticsearch/pull/48443)

Client::
* Remove `SecurityClient` from x-pack [#42471](https://github.com/elastic/elasticsearch/pull/42471)

Features/ILM+SLM::
* Remove the `ILMClient` [#42817](https://github.com/elastic/elasticsearch/pull/42817)

Features/Monitoring::
* Remove `MonitoringClient` from x-pack [#42770](https://github.com/elastic/elasticsearch/pull/42770)

Features/Watcher::
* Remove `WatcherClient` from x-pack [#42815](https://github.com/elastic/elasticsearch/pull/42815)

Infra/Core::
* Remove `XPackClient` from x-pack [#42729](https://github.com/elastic/elasticsearch/pull/42729)
* Remove the transport client [#42538](https://github.com/elastic/elasticsearch/pull/42538)
* Remove transport client from x-pack [#42202](https://github.com/elastic/elasticsearch/pull/42202)

Infra/REST API::
* Copy HTTP headers to `ThreadContext` strictly [#45945](https://github.com/elastic/elasticsearch/pull/45945)

Machine Learning::
* Remove the `MachineLearningClient` [#43108](https://github.com/elastic/elasticsearch/pull/43108)

Mapping::
* Remove type filter from `GetMappings` API [#47364](https://github.com/elastic/elasticsearch/pull/47364) (issue: [#41059](https://github.com/elastic/elasticsearch/issues/41059))
* Remove `type` parameter from `PutMappingRequest.buildFromSimplifiedDef()` [#50844](https://github.com/elastic/elasticsearch/pull/50844) (issue: [#41059](https://github.com/elastic/elasticsearch/issues/41059))
* Remove unused parameter from `MetadataFieldMapper.TypeParser#getDefault()` [#51219](https://github.com/elastic/elasticsearch/pull/51219)
* Remove `type` parameter from `CIR.mapping(type, object...)` [#50739](https://github.com/elastic/elasticsearch/pull/50739) (issue: [#41059](https://github.com/elastic/elasticsearch/issues/41059))

Search::
* Removes types from `SearchRequest` and `QueryShardContext` [#42112](https://github.com/elastic/elasticsearch/pull/42112)

Snapshot/Restore::
* Remove deprecated repository methods [#42359](https://github.com/elastic/elasticsearch/pull/42359) (issue: [#42213](https://github.com/elastic/elasticsearch/issues/42213))


### Deprecations

Authentication::
* Deprecate setup-passwords tool [#76902](https://github.com/elastic/elasticsearch/pull/76902)

CRUD::
* Remove `indices_segments` 'verbose' parameter [#78451](https://github.com/elastic/elasticsearch/pull/78451) (issue: [#75955](https://github.com/elastic/elasticsearch/issues/75955))

Engine::
* Deprecate setting `max_merge_at_once_explicit` [#80574](https://github.com/elastic/elasticsearch/pull/80574)

Machine Learning::
* Deprecate `estimated_heap_memory_usage_bytes` and replace with `model_size_bytes` [#80554](https://github.com/elastic/elasticsearch/pull/80554)

Monitoring::
* Add deprecation info API entries for deprecated monitoring settings [#78799](https://github.com/elastic/elasticsearch/pull/78799)
* Automatically install monitoring templates at plugin initialization [#78350](https://github.com/elastic/elasticsearch/pull/78350)
* Remove Monitoring ingest pipelines [#77459](https://github.com/elastic/elasticsearch/pull/77459) (issue: [#50770](https://github.com/elastic/elasticsearch/issues/50770))

Search::
* Configure `IndexSearcher.maxClauseCount()` based on node characteristics [#81525](https://github.com/elastic/elasticsearch/pull/81525) (issue: [#46433](https://github.com/elastic/elasticsearch/issues/46433))

Transform::
* Improve transform deprecation messages [#81847](https://github.com/elastic/elasticsearch/pull/81847) (issues: [#81521](https://github.com/elastic/elasticsearch/issues/81521), [#81523](https://github.com/elastic/elasticsearch/issues/81523))


### New features

Security::
* Auto-configure TLS for new nodes of new clusters [#77231](https://github.com/elastic/elasticsearch/pull/77231) (issues: [#75144](https://github.com/elastic/elasticsearch/issues/75144), [#75704](https://github.com/elastic/elasticsearch/issues/75704))

Snapshot/Restore::
* Support IAM roles for Kubernetes service accounts [#81255](https://github.com/elastic/elasticsearch/pull/81255) (issue: [#52625](https://github.com/elastic/elasticsearch/issues/52625))

Watcher::
* Use `startsWith` rather than exact matches for Watcher history template names [#82396](https://github.com/elastic/elasticsearch/pull/82396)
