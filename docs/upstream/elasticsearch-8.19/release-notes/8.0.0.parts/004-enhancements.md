<!-- Part 4 of 5 of release-notes/8.0.0.md (split because the page is big). -->

### Enhancements

Analysis::
* Move `reload_analyzers` endpoint to x-pack [#43559](https://github.com/elastic/elasticsearch/pull/43559)

Authentication::
* Reset elastic password CLI tool [#74892](https://github.com/elastic/elasticsearch/pull/74892) (issues: [#70113](https://github.com/elastic/elasticsearch/issues/70113), [#74890](https://github.com/elastic/elasticsearch/issues/74890))
* Autogenerate and print elastic password on startup [#77291](https://github.com/elastic/elasticsearch/pull/77291)
* Enroll Kibana API uses Service Accounts [#76370](https://github.com/elastic/elasticsearch/pull/76370)
* Add `reset-kibana-system-user` tool [#77322](https://github.com/elastic/elasticsearch/pull/77322)
* New CLI tool to reset password for built-in users [#79709](https://github.com/elastic/elasticsearch/pull/79709)
* Auto-configure the `elastic` user password [#78306](https://github.com/elastic/elasticsearch/pull/78306)

Authorization::
* Granting `kibana_system` reserved role access to "all" privileges to `.internal.preview.alerts*` index [#80889](https://github.com/elastic/elasticsearch/pull/80889) (issues: [#76624](https://github.com/elastic/elasticsearch/issues/76624), [#80746](https://github.com/elastic/elasticsearch/issues/80746), [#116374](https://github.com/elastic/elasticsearch/issues/116374))
* Granting `kibana_system` reserved role access to "all" privileges to .preview.alerts* index [#80746](https://github.com/elastic/elasticsearch/pull/80746)
* Granting editor and viewer roles access to alerts-as-data indices [#81285](https://github.com/elastic/elasticsearch/pull/81285)

Cluster Coordination::
* Prevent downgrades from 8.x to 7.x [#78586](https://github.com/elastic/elasticsearch/pull/78586) (issues: [#42489](https://github.com/elastic/elasticsearch/issues/42489), [#52414](https://github.com/elastic/elasticsearch/issues/52414))
* Prevent downgrades from 8.x to 7.x [#78638](https://github.com/elastic/elasticsearch/pull/78638) (issues: [#42489](https://github.com/elastic/elasticsearch/issues/42489), [#52414](https://github.com/elastic/elasticsearch/issues/52414))
* Make `TaskBatcher` less lock-heavy [#82227](https://github.com/elastic/elasticsearch/pull/82227) (issue: [#77466](https://github.com/elastic/elasticsearch/issues/77466))

Data streams::
* Data stream support read and write with custom routing and partition size [#74394](https://github.com/elastic/elasticsearch/pull/74394) (issue: [#74390](https://github.com/elastic/elasticsearch/issues/74390))

EQL::
* Add option for returning results from the tail of the stream [#64869](https://github.com/elastic/elasticsearch/pull/64869) (issue: [#58646](https://github.com/elastic/elasticsearch/issues/58646))
* Introduce case insensitive variant `in~` [#68176](https://github.com/elastic/elasticsearch/pull/68176) (issue: [#68172](https://github.com/elastic/elasticsearch/issues/68172))
* Optimize redundant `toString` [#71070](https://github.com/elastic/elasticsearch/pull/71070) (issue: [#70681](https://github.com/elastic/elasticsearch/issues/70681))

Engine::
* Always use soft-deletes in `InternalEngine` [#50415](https://github.com/elastic/elasticsearch/pull/50415)
* Remove translog retention policy [#51417](https://github.com/elastic/elasticsearch/pull/51417) (issue: [#50775](https://github.com/elastic/elasticsearch/issues/50775))

Features/CAT APIs::
* Remove `size` and add `time` params to `_cat/threadpool` [#55736](https://github.com/elastic/elasticsearch/pull/55736) (issue: [#54478](https://github.com/elastic/elasticsearch/issues/54478))

Features/ILM+SLM::
* Allow for setting the total shards per node in the Allocate ILM action [#76794](https://github.com/elastic/elasticsearch/pull/76794) (issue: [#76775](https://github.com/elastic/elasticsearch/issues/76775))
* Inject migrate action regardless of allocate action [#79090](https://github.com/elastic/elasticsearch/pull/79090) (issue: [#76147](https://github.com/elastic/elasticsearch/issues/76147))
* Make unchanged ILM policy updates into noop [#82240](https://github.com/elastic/elasticsearch/pull/82240) (issue: [#82065](https://github.com/elastic/elasticsearch/issues/82065))
* Avoid unnecessary `LifecycleExecutionState` recalculation [#81558](https://github.com/elastic/elasticsearch/pull/81558) (issues: [#77466](https://github.com/elastic/elasticsearch/issues/77466), [#79692](https://github.com/elastic/elasticsearch/issues/79692))

Features/Indices APIs::
* Batch rollover cluster state updates [#79945](https://github.com/elastic/elasticsearch/pull/79945) (issues: [#77466](https://github.com/elastic/elasticsearch/issues/77466), [#79782](https://github.com/elastic/elasticsearch/issues/79782))
* Reuse `MappingMetadata` instances in Metadata class [#80348](https://github.com/elastic/elasticsearch/pull/80348) (issues: [#69772](https://github.com/elastic/elasticsearch/issues/69772), [#77466](https://github.com/elastic/elasticsearch/issues/77466))

Features/Stats::
* Add bulk stats track the bulk per shard [#52208](https://github.com/elastic/elasticsearch/pull/52208) (issues: [#47345](https://github.com/elastic/elasticsearch/issues/47345), [#50536](https://github.com/elastic/elasticsearch/issues/50536))

Features/Watcher::
* Remove Watcher history clean up from monitoring [#67154](https://github.com/elastic/elasticsearch/pull/67154)

Infra/Core::
* Remove aliases exist action [#43430](https://github.com/elastic/elasticsearch/pull/43430)
* Remove indices exists action [#43164](https://github.com/elastic/elasticsearch/pull/43164)
* Remove types exists action [#43344](https://github.com/elastic/elasticsearch/pull/43344)
* Retain reference to stdout for exceptional cases [#77460](https://github.com/elastic/elasticsearch/pull/77460)
* Check whether stdout is a real console [#79882](https://github.com/elastic/elasticsearch/pull/79882)
* Share int, long, float, double, and byte pages [#75053](https://github.com/elastic/elasticsearch/pull/75053)
* Revert "Deprecate resolution loss on date field (#78921)" [#79914](https://github.com/elastic/elasticsearch/pull/79914) (issue: [#78921](https://github.com/elastic/elasticsearch/issues/78921))
* Add two missing entries to the deprecation information API [#80290](https://github.com/elastic/elasticsearch/pull/80290) (issue: [#80233](https://github.com/elastic/elasticsearch/issues/80233))
* Prevent upgrades to 8.0 without first upgrading to the last 7.x release [#82321](https://github.com/elastic/elasticsearch/pull/82321) (issue: [#81865](https://github.com/elastic/elasticsearch/issues/81865))

Infra/Logging::
* Make Elasticsearch JSON logs ECS compliant [#47105](https://github.com/elastic/elasticsearch/pull/47105) (issue: [#46119](https://github.com/elastic/elasticsearch/issues/46119))

Infra/REST API::
* Allow for field declaration for future compatible versions [#69774](https://github.com/elastic/elasticsearch/pull/69774) (issue: [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* Introduce stability description to the REST API specification [#38413](https://github.com/elastic/elasticsearch/pull/38413)
* Parsing: Validate that fields are not registered twice [#70243](https://github.com/elastic/elasticsearch/pull/70243)
* Support response content-type with versioned media type [#65500](https://github.com/elastic/elasticsearch/pull/65500) (issue: [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* [REST API Compatibility] Typed endpoints for index and get APIs [#69131](https://github.com/elastic/elasticsearch/pull/69131) (issue: [#54160](https://github.com/elastic/elasticsearch/issues/54160))
* [REST API Compatibility] Typed endpoints for put and get mapping and get field mappings [#71721](https://github.com/elastic/elasticsearch/pull/71721) (issues: [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#54160](https://github.com/elastic/elasticsearch/issues/54160))
* [REST API Compatibility] Allow `copy_settings` flag for resize operations [#75184](https://github.com/elastic/elasticsearch/pull/75184) (issues: [#38514](https://github.com/elastic/elasticsearch/issues/38514), [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* [REST API Compatibility] Allow for type in geo shape query [#74553](https://github.com/elastic/elasticsearch/pull/74553) (issues: [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#54160](https://github.com/elastic/elasticsearch/issues/54160))
* [REST API Compatibility] Always return `adjust_pure_negative` value [#75182](https://github.com/elastic/elasticsearch/pull/75182) (issues: [#49543](https://github.com/elastic/elasticsearch/issues/49543), [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* [REST API Compatibility] Clean up x-pack/plugin rest compat tests [#74701](https://github.com/elastic/elasticsearch/pull/74701) (issue: [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* [REST API Compatibility] Do not return `_doc` for empty mappings in template [#75448](https://github.com/elastic/elasticsearch/pull/75448) (issues: [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#54160](https://github.com/elastic/elasticsearch/issues/54160), [#70966](https://github.com/elastic/elasticsearch/issues/70966), [#74544](https://github.com/elastic/elasticsearch/issues/74544))
* [REST API Compatibility] Dummy REST action for `indices.upgrade` API [#75136](https://github.com/elastic/elasticsearch/pull/75136) (issue: [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* [REST API Compatibility] REST Terms vector typed response [#73117](https://github.com/elastic/elasticsearch/pull/73117)
* [REST API Compatibility] Rename `BulkItemResponse.Failure` type field [#74937](https://github.com/elastic/elasticsearch/pull/74937) (issue: [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* [REST API Compatibility] Type metadata for docs used in simulate request [#74222](https://github.com/elastic/elasticsearch/pull/74222) (issues: [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#54160](https://github.com/elastic/elasticsearch/issues/54160))
* [REST API Compatibility] Typed `TermLookups` [#74544](https://github.com/elastic/elasticsearch/pull/74544) (issues: [#46943](https://github.com/elastic/elasticsearch/issues/46943), [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#54160](https://github.com/elastic/elasticsearch/issues/54160))
* [REST API Compatibility] Typed and x-pack graph explore API [#74185](https://github.com/elastic/elasticsearch/pull/74185) (issues: [#46935](https://github.com/elastic/elasticsearch/issues/46935), [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#54160](https://github.com/elastic/elasticsearch/issues/54160))
* [REST API Compatibility] Typed endpoint for bulk API [#73571](https://github.com/elastic/elasticsearch/pull/73571) (issue: [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* [REST API Compatibility] Typed endpoint for multi-get API [#73878](https://github.com/elastic/elasticsearch/pull/73878) (issue: [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* [REST API Compatibility] Typed endpoints for `RestUpdateAction` and `RestDeleteAction` [#73115](https://github.com/elastic/elasticsearch/pull/73115) (issues: [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#54160](https://github.com/elastic/elasticsearch/issues/54160))
* [REST API Compatibility] Typed endpoints for `get_source` API [#73957](https://github.com/elastic/elasticsearch/pull/73957) (issues: [#46587](https://github.com/elastic/elasticsearch/issues/46587), [#46931](https://github.com/elastic/elasticsearch/issues/46931), [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* [REST API Compatibility] Typed endpoints for explain API [#73901](https://github.com/elastic/elasticsearch/pull/73901) (issue: [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* [REST API Compatibility] Typed endpoints for search `_count` API [#73958](https://github.com/elastic/elasticsearch/pull/73958) (issues: [#42112](https://github.com/elastic/elasticsearch/issues/42112), [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* [REST API Compatibility] Typed indexing stats [#74181](https://github.com/elastic/elasticsearch/pull/74181) (issues: [#47203](https://github.com/elastic/elasticsearch/issues/47203), [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#54160](https://github.com/elastic/elasticsearch/issues/54160))
* [REST API Compatibility] Types for percolate query API [#74698](https://github.com/elastic/elasticsearch/pull/74698) (issues: [#46985](https://github.com/elastic/elasticsearch/issues/46985), [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#54160](https://github.com/elastic/elasticsearch/issues/54160), [#74689](https://github.com/elastic/elasticsearch/issues/74689))
* [REST API Compatibility] Validate query typed API [#74171](https://github.com/elastic/elasticsearch/pull/74171) (issues: [#46927](https://github.com/elastic/elasticsearch/issues/46927), [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#54160](https://github.com/elastic/elasticsearch/issues/54160))
* [REST API Compatibility] Voting config exclusion exception message [#75406](https://github.com/elastic/elasticsearch/pull/75406) (issues: [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#55291](https://github.com/elastic/elasticsearch/issues/55291))
* [REST API Compatibility] `MoreLikeThisQuery` with types [#75123](https://github.com/elastic/elasticsearch/pull/75123) (issues: [#42198](https://github.com/elastic/elasticsearch/issues/42198), [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#54160](https://github.com/elastic/elasticsearch/issues/54160))
* [REST API Compatibility] Update and delete by query using size field [#69606](https://github.com/elastic/elasticsearch/pull/69606)
* [REST API Compatibility] Indicies boost in object format [#74422](https://github.com/elastic/elasticsearch/pull/74422) (issues: [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#55078](https://github.com/elastic/elasticsearch/issues/55078))
* [REST API Compatibility] Typed endpoints for search and related endpoints [#72155](https://github.com/elastic/elasticsearch/pull/72155) (issues: [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#54160](https://github.com/elastic/elasticsearch/issues/54160))
* [REST API Compatibility] Allow to use size `-1` [#75342](https://github.com/elastic/elasticsearch/pull/75342) (issues: [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#69548](https://github.com/elastic/elasticsearch/issues/69548), [#70209](https://github.com/elastic/elasticsearch/issues/70209))
* [REST API Compatibility] Ignore `use_field_mapping` option for docvalue [#74435](https://github.com/elastic/elasticsearch/pull/74435) (issue: [#55622](https://github.com/elastic/elasticsearch/issues/55622))
* [REST API Compatibility] `_time` and `_term` sort orders [#74919](https://github.com/elastic/elasticsearch/pull/74919) (issues: [#39450](https://github.com/elastic/elasticsearch/issues/39450), [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* [REST API Compatability] `template` parameter and field on PUT index template [#71238](https://github.com/elastic/elasticsearch/pull/71238) (issues: [#49460](https://github.com/elastic/elasticsearch/issues/49460), [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#68905](https://github.com/elastic/elasticsearch/issues/68905))
* [REST API Compatibility] Make query registration easier [#75722](https://github.com/elastic/elasticsearch/pull/75722) (issue: [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* [REST API Compatibility] Typed query [#75453](https://github.com/elastic/elasticsearch/pull/75453) (issues: [#47207](https://github.com/elastic/elasticsearch/issues/47207), [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#54160](https://github.com/elastic/elasticsearch/issues/54160))
* [REST API Compatibility] Deprecate the use of synced flush [#75372](https://github.com/elastic/elasticsearch/pull/75372) (issues: [#50882](https://github.com/elastic/elasticsearch/issues/50882), [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* [REST API Compatibility] Licence `accept_enterprise` and response changes [#75479](https://github.com/elastic/elasticsearch/pull/75479) (issues: [#50067](https://github.com/elastic/elasticsearch/issues/50067), [#50735](https://github.com/elastic/elasticsearch/issues/50735), [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#58217](https://github.com/elastic/elasticsearch/issues/58217))

Infra/Scripting::
* Update `DeprecationMap` to `DynamicMap` [#56149](https://github.com/elastic/elasticsearch/pull/56149) (issue: [#52103](https://github.com/elastic/elasticsearch/issues/52103))
* Add nio Buffers to Painless [#79870](https://github.com/elastic/elasticsearch/pull/79870) (issue: [#79867](https://github.com/elastic/elasticsearch/issues/79867))
* Restore the scripting general cache [#79453](https://github.com/elastic/elasticsearch/pull/79453) (issue: [#62899](https://github.com/elastic/elasticsearch/issues/62899))

Infra/Settings::
* Fixed inconsistent `Setting.exist()` [#46603](https://github.com/elastic/elasticsearch/pull/46603) (issue: [#41830](https://github.com/elastic/elasticsearch/issues/41830))
* Remove `index.optimize_auto_generated_id` setting (#27583) [#27600](https://github.com/elastic/elasticsearch/pull/27600) (issue: [#27583](https://github.com/elastic/elasticsearch/issues/27583))
* Implement setting deduplication via string interning [#80493](https://github.com/elastic/elasticsearch/pull/80493) (issues: [#77466](https://github.com/elastic/elasticsearch/issues/77466), [#78892](https://github.com/elastic/elasticsearch/issues/78892))

Ingest::
* Add support for `_meta` field to ingest pipelines [#76381](https://github.com/elastic/elasticsearch/pull/76381)
* Remove binary field after attachment processor execution [#79172](https://github.com/elastic/elasticsearch/pull/79172)
* Improving cache lookup to reduce recomputing / searches [#77259](https://github.com/elastic/elasticsearch/pull/77259)
* Extract more standard metadata from binary files [#78754](https://github.com/elastic/elasticsearch/pull/78754) (issue: [#22339](https://github.com/elastic/elasticsearch/issues/22339))

License::
* Add deprecated `accept_enterprise` param to `/_xpack` [#58220](https://github.com/elastic/elasticsearch/pull/58220) (issue: [#58217](https://github.com/elastic/elasticsearch/issues/58217))
* Support `accept_enterprise` param in get license API [#50067](https://github.com/elastic/elasticsearch/pull/50067) (issue: [#49474](https://github.com/elastic/elasticsearch/issues/49474))
* Enforce Transport TLS check on all licenses [#79602](https://github.com/elastic/elasticsearch/pull/79602) (issue: [#75292](https://github.com/elastic/elasticsearch/issues/75292))

Machine Learning::
* The Windows build platform for the machine learning C++ code now uses Visual Studio 2019 {ml-pull}1352[#1352]
* The macOS build platform for the machine learning C++ code is now Mojave running Xcode 11.3.1,
  or Ubuntu 20.04 running clang 8 for cross compilation {ml-pull}1429[#1429]
* Add a new application for evaluating PyTorch models. The app depends on LibTorch - the C++ front end to PyTorch - and performs inference on models stored in the TorchScript format {ml-pull}1902[#1902]
* Adding new PUT trained model vocabulary endpoint [#77387](https://github.com/elastic/elasticsearch/pull/77387)
* Creating new PUT model definition part API [#76987](https://github.com/elastic/elasticsearch/pull/76987)
* Add inference time configuration overrides [#78441](https://github.com/elastic/elasticsearch/pull/78441) (issue: [#77799](https://github.com/elastic/elasticsearch/issues/77799))
* Optimize source extraction for `categorize_text` aggregation [#79099](https://github.com/elastic/elasticsearch/pull/79099)
* The Linux build platform for the machine learning C++ code is now CentOS 7 running gcc 10.3. {ml-pull}2028[#2028]
* Make ML indices hidden when the node becomes master [#77416](https://github.com/elastic/elasticsearch/pull/77416) (issue: [#53674](https://github.com/elastic/elasticsearch/issues/53674))
* Add `deployment_stats` to trained model stats [#80531](https://github.com/elastic/elasticsearch/pull/80531)
* The setting `use_auto_machine_memory_percent` now defaults `max_model_memory_limit` [#80532](https://github.com/elastic/elasticsearch/pull/80532) (issue: [#80415](https://github.com/elastic/elasticsearch/issues/80415))

Mapping::
* Sparse vector to throw exception consistently [#62646](https://github.com/elastic/elasticsearch/pull/62646)
* Add support for configuring HNSW parameters [#79193](https://github.com/elastic/elasticsearch/pull/79193) (issue: [#78473](https://github.com/elastic/elasticsearch/issues/78473))
* Extend `dense_vector` to support indexing vectors [#78491](https://github.com/elastic/elasticsearch/pull/78491) (issue: [#78473](https://github.com/elastic/elasticsearch/issues/78473))

Monitoring::
* Add previously removed Monitoring settings back for 8.0 [#78784](https://github.com/elastic/elasticsearch/pull/78784)
* Change Monitoring plugin cluster alerts to not install by default [#79657](https://github.com/elastic/elasticsearch/pull/79657)
* Adding default templates for Metricbeat ECS data [#81744](https://github.com/elastic/elasticsearch/pull/81744)

Network::
* Enable LZ4 transport compression by default [#76326](https://github.com/elastic/elasticsearch/pull/76326) (issue: [#73497](https://github.com/elastic/elasticsearch/issues/73497))
* Improve slow inbound handling to include response type [#80425](https://github.com/elastic/elasticsearch/pull/80425)

Packaging::
* Make the Docker build more re-usable in Cloud [#50277](https://github.com/elastic/elasticsearch/pull/50277) (issues: [#46166](https://github.com/elastic/elasticsearch/issues/46166), [#49926](https://github.com/elastic/elasticsearch/issues/49926))
* Update docker-compose.yml to fix bootstrap check error [#47650](https://github.com/elastic/elasticsearch/pull/47650)
* Allow total memory to be overridden [#78750](https://github.com/elastic/elasticsearch/pull/78750) (issue: [#65905](https://github.com/elastic/elasticsearch/issues/65905))
* Convert repository plugins to modules [#81870](https://github.com/elastic/elasticsearch/pull/81870) (issue: [#81652](https://github.com/elastic/elasticsearch/issues/81652))

Recovery::
* Use Lucene index in peer recovery and resync [#51189](https://github.com/elastic/elasticsearch/pull/51189) (issue: [#50775](https://github.com/elastic/elasticsearch/issues/50775))
* Fix `PendingReplicationActions` submitting lots of `NOOP` tasks to `GENERIC` [#82092](https://github.com/elastic/elasticsearch/pull/82092) (issues: [#77466](https://github.com/elastic/elasticsearch/issues/77466), [#79837](https://github.com/elastic/elasticsearch/issues/79837))

Reindex::
* Make reindexing managed by a persistent task [#43382](https://github.com/elastic/elasticsearch/pull/43382) (issue: [#42612](https://github.com/elastic/elasticsearch/issues/42612))
* Reindex restart from checkpoint [#46055](https://github.com/elastic/elasticsearch/pull/46055) (issue: [#42612](https://github.com/elastic/elasticsearch/issues/42612))
* Reindex search resiliency [#45497](https://github.com/elastic/elasticsearch/pull/45497) (issues: [#42612](https://github.com/elastic/elasticsearch/issues/42612), [#43187](https://github.com/elastic/elasticsearch/issues/43187))
* Reindex v2 rethrottle sliced fix [#46967](https://github.com/elastic/elasticsearch/pull/46967) (issues: [#42612](https://github.com/elastic/elasticsearch/issues/42612), [#46763](https://github.com/elastic/elasticsearch/issues/46763))
* Do not scroll if max docs is less than scroll size (update/delete by query) [#81654](https://github.com/elastic/elasticsearch/pull/81654) (issue: [#54270](https://github.com/elastic/elasticsearch/issues/54270))

Rollup::
* Adds support for `date_nanos` in Rollup Metric and `DateHistogram` Configs [#59349](https://github.com/elastic/elasticsearch/pull/59349) (issue: [#44505](https://github.com/elastic/elasticsearch/issues/44505))

SQL::
* Add text formatting support for multivalue [#68606](https://github.com/elastic/elasticsearch/pull/68606)
* Add xDBC and CLI support. QA CSV specs [#68966](https://github.com/elastic/elasticsearch/pull/68966)
* Export array values through result sets [#69512](https://github.com/elastic/elasticsearch/pull/69512)
* Improve alias resolution in sub-queries [#67216](https://github.com/elastic/elasticsearch/pull/67216) (issue: [#56713](https://github.com/elastic/elasticsearch/issues/56713))
* Improve the optimization of null conditionals [#71192](https://github.com/elastic/elasticsearch/pull/71192)
* Push `WHERE` clause inside subqueries [#71362](https://github.com/elastic/elasticsearch/pull/71362)
* Use Java `String` methods for `LTRIM/RTRIM` [#57594](https://github.com/elastic/elasticsearch/pull/57594)
* QL: Make canonical form take into account children [#71266](https://github.com/elastic/elasticsearch/pull/71266)
* QL: Polish optimizer expression rule declaration [#71396](https://github.com/elastic/elasticsearch/pull/71396)
* QL: Propagate nullability constraints across conjunctions [#71187](https://github.com/elastic/elasticsearch/pull/71187) (issue: [#70683](https://github.com/elastic/elasticsearch/issues/70683))

Search::
* Completely disallow setting negative size in search [#70209](https://github.com/elastic/elasticsearch/pull/70209) (issue: [#69548](https://github.com/elastic/elasticsearch/issues/69548))
* Make `0` as invalid value for `min_children` in `has_child` query [#41347](https://github.com/elastic/elasticsearch/pull/41347)
* Return error when remote indices are locally resolved [#74556](https://github.com/elastic/elasticsearch/pull/74556) (issue: [#26247](https://github.com/elastic/elasticsearch/issues/26247))
* [REST API Compatibility] Nested path and filter sort options [#76022](https://github.com/elastic/elasticsearch/pull/76022) (issues: [#42809](https://github.com/elastic/elasticsearch/issues/42809), [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* [REST API Compatibility] `CommonTermsQuery` and `cutoff_frequency` parameter [#75896](https://github.com/elastic/elasticsearch/pull/75896) (issues: [#42654](https://github.com/elastic/elasticsearch/issues/42654), [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* [REST API Compatibility] Allow first empty line for `_msearch` [#75886](https://github.com/elastic/elasticsearch/pull/75886) (issues: [#41011](https://github.com/elastic/elasticsearch/issues/41011), [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* Node level can match action [#78765](https://github.com/elastic/elasticsearch/pull/78765)
* TSDB: Add time series information to field caps [#78790](https://github.com/elastic/elasticsearch/pull/78790) (issue: [#74660](https://github.com/elastic/elasticsearch/issues/74660))
* Add new kNN search endpoint [#79013](https://github.com/elastic/elasticsearch/pull/79013) (issue: [#78473](https://github.com/elastic/elasticsearch/issues/78473))
* Disallow kNN searches on nested vector fields [#79403](https://github.com/elastic/elasticsearch/pull/79403) (issue: [#78473](https://github.com/elastic/elasticsearch/issues/78473))
* Ensure kNN search respects authorization [#79693](https://github.com/elastic/elasticsearch/pull/79693) (issue: [#78473](https://github.com/elastic/elasticsearch/issues/78473))
* Load kNN vectors format with mmapfs [#78724](https://github.com/elastic/elasticsearch/pull/78724) (issue: [#78473](https://github.com/elastic/elasticsearch/issues/78473))
* Support cosine similarity in kNN search [#79500](https://github.com/elastic/elasticsearch/pull/79500)
* Node level can match action [#78765](https://github.com/elastic/elasticsearch/pull/78765)
* Check nested fields earlier in kNN search [#80516](https://github.com/elastic/elasticsearch/pull/80516) (issue: [#78473](https://github.com/elastic/elasticsearch/issues/78473))

Security::
* Add a tool for creating enrollment tokens [#74890](https://github.com/elastic/elasticsearch/pull/74890)
* Add the Enroll Kibana API [#72207](https://github.com/elastic/elasticsearch/pull/72207)
* Change default hashing algorithm for FIPS 140 [#55544](https://github.com/elastic/elasticsearch/pull/55544)
* Create enrollment token [#73573](https://github.com/elastic/elasticsearch/pull/73573) (issues: [#71438](https://github.com/elastic/elasticsearch/issues/71438), [#72129](https://github.com/elastic/elasticsearch/issues/72129))
* Enroll node API [#72129](https://github.com/elastic/elasticsearch/pull/72129)
* Configure security for the initial node CLI [#74868](https://github.com/elastic/elasticsearch/pull/74868)
* Generate and store password hash for elastic user [#76276](https://github.com/elastic/elasticsearch/pull/76276) (issue: [#75310](https://github.com/elastic/elasticsearch/issues/75310))
* Set elastic password and generate enrollment token [#75816](https://github.com/elastic/elasticsearch/pull/75816) (issue: [#75310](https://github.com/elastic/elasticsearch/issues/75310))
* Add `elasticsearch-enroll-node` tool [#77292](https://github.com/elastic/elasticsearch/pull/77292)
* Default hasher to `PBKDF2_STRETCH` on FIPS mode [#76274](https://github.com/elastic/elasticsearch/pull/76274)
* Add v7 `restCompat` for invalidating API key with the id field [#78664](https://github.com/elastic/elasticsearch/pull/78664) (issue: [#66671](https://github.com/elastic/elasticsearch/issues/66671))
* Print enrollment token on startup [#78293](https://github.com/elastic/elasticsearch/pull/78293)
* Startup check for security implicit behavior change [#76879](https://github.com/elastic/elasticsearch/pull/76879)
* CLI tool to reconfigure nodes to enroll [#79690](https://github.com/elastic/elasticsearch/pull/79690) (issue: [#7718](https://github.com/elastic/elasticsearch/issues/7718))
* Security auto-configuration for packaged installations [#75144](https://github.com/elastic/elasticsearch/pull/75144) (issue: [#78306](https://github.com/elastic/elasticsearch/issues/78306))

Snapshot/Restore::
* Introduce searchable snapshots index setting for cascade deletion of snapshots [#74977](https://github.com/elastic/elasticsearch/pull/74977)
* Unify blob store compress setting [#39346](https://github.com/elastic/elasticsearch/pull/39346) (issue: [#39073](https://github.com/elastic/elasticsearch/issues/39073))
* Add recovery state tracking for searchable snapshots [#60505](https://github.com/elastic/elasticsearch/pull/60505)
* Allow listing older repositories [#78244](https://github.com/elastic/elasticsearch/pull/78244)
* Optimize SLM Policy Queries [#79341](https://github.com/elastic/elasticsearch/pull/79341) (issue: [#79321](https://github.com/elastic/elasticsearch/issues/79321))

TLS::
* Add `ChaCha20` TLS ciphers on Java 12+ [#42155](https://github.com/elastic/elasticsearch/pull/42155)
* Add support for `KeyStore` filters to `ssl-config` [#75407](https://github.com/elastic/elasticsearch/pull/75407)
* Update TLS ciphers and protocols for JDK 11 [#41808](https://github.com/elastic/elasticsearch/pull/41808) (issues: [#38646](https://github.com/elastic/elasticsearch/issues/38646), [#41385](https://github.com/elastic/elasticsearch/issues/41385))

Transform::
* Prevent old beta transforms from starting [#79712](https://github.com/elastic/elasticsearch/pull/79712)

TSDB::
* Automatically add timestamp mapper [#79136](https://github.com/elastic/elasticsearch/pull/79136)
* Create a coordinating node level reader for tsdb [#79197](https://github.com/elastic/elasticsearch/pull/79197)
* Fix TSDB shrink test in multi-version cluster [#79940](https://github.com/elastic/elasticsearch/pull/79940) (issue: [#79936](https://github.com/elastic/elasticsearch/issues/79936))
* Do not allow shadowing metrics or dimensions [#79757](https://github.com/elastic/elasticsearch/pull/79757)
