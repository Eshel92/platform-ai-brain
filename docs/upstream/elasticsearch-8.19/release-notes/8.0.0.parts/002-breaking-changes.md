<!-- Part 2 of 5 of release-notes/8.0.0.md (split because the page is big). -->

### Breaking changes

Aggregations::
* Percentiles aggregation: disallow specifying same percentile values twice [#52257](https://github.com/elastic/elasticsearch/pull/52257) (issue: [#51871](https://github.com/elastic/elasticsearch/issues/51871))
* Remove adjacency matrix setting [#46327](https://github.com/elastic/elasticsearch/pull/46327) (issues: [#46257](https://github.com/elastic/elasticsearch/issues/46257), [#46324](https://github.com/elastic/elasticsearch/issues/46324))
* Remove `MovingAverage` pipeline aggregation [#39328](https://github.com/elastic/elasticsearch/pull/39328)
* Remove deprecated `_time` and `_term` sort orders [#39450](https://github.com/elastic/elasticsearch/pull/39450)
* Remove deprecated date histo interval [#75000](https://github.com/elastic/elasticsearch/pull/75000)

Allocation::
* Require single data nodes to respect disk watermarks [#73737](https://github.com/elastic/elasticsearch/pull/73737) (issues: [#55805](https://github.com/elastic/elasticsearch/issues/55805), [#73733](https://github.com/elastic/elasticsearch/issues/73733))
* Remove `include_relocations` setting [#47717](https://github.com/elastic/elasticsearch/pull/47717) (issues: [#46079](https://github.com/elastic/elasticsearch/issues/46079), [#47443](https://github.com/elastic/elasticsearch/issues/47443))

Analysis::
* Cleanup versioned deprecations in analysis [#41560](https://github.com/elastic/elasticsearch/pull/41560) (issue: [#41164](https://github.com/elastic/elasticsearch/issues/41164))
* Remove preconfigured `delimited_payload_filter` [#43686](https://github.com/elastic/elasticsearch/pull/43686) (issues: [#41560](https://github.com/elastic/elasticsearch/issues/41560), [#43684](https://github.com/elastic/elasticsearch/issues/43684))

Authentication::
* Always add file and native realms unless explicitly disabled [#69096](https://github.com/elastic/elasticsearch/pull/69096) (issue: [#50892](https://github.com/elastic/elasticsearch/issues/50892))
* Do not set a NameID format in Policy by default [#44090](https://github.com/elastic/elasticsearch/pull/44090) (issue: [#40353](https://github.com/elastic/elasticsearch/issues/40353))
* Make order setting mandatory for Realm config [#51195](https://github.com/elastic/elasticsearch/pull/51195) (issue: [#37614](https://github.com/elastic/elasticsearch/issues/37614))

CCR::
* Avoid auto following leader system indices in CCR [#72815](https://github.com/elastic/elasticsearch/pull/72815) (issue: [#67686](https://github.com/elastic/elasticsearch/issues/67686))

Cluster Coordination::
* Remove join timeout [#60873](https://github.com/elastic/elasticsearch/pull/60873) (issue: [#60872](https://github.com/elastic/elasticsearch/issues/60872))
* Remove node filters for voting config exclusions [#55673](https://github.com/elastic/elasticsearch/pull/55673) (issues: [#47990](https://github.com/elastic/elasticsearch/issues/47990), [#50836](https://github.com/elastic/elasticsearch/issues/50836))
* Remove support for delaying state recovery pending master [#53845](https://github.com/elastic/elasticsearch/pull/53845) (issue: [#51806](https://github.com/elastic/elasticsearch/issues/51806))

Distributed::
* Remove synced flush [#50882](https://github.com/elastic/elasticsearch/pull/50882) (issues: [#50776](https://github.com/elastic/elasticsearch/issues/50776), [#50835](https://github.com/elastic/elasticsearch/issues/50835))
* Remove the `cluster.remote.connect` setting [#54175](https://github.com/elastic/elasticsearch/pull/54175) (issue: [#53924](https://github.com/elastic/elasticsearch/issues/53924))

Engine::
* Force merge should reject requests with `only_expunge_deletes` and `max_num_segments` set [#44761](https://github.com/elastic/elasticsearch/pull/44761) (issue: [#43102](https://github.com/elastic/elasticsearch/issues/43102))
* Remove per-type indexing stats [#47203](https://github.com/elastic/elasticsearch/pull/47203) (issue: [#41059](https://github.com/elastic/elasticsearch/issues/41059))
* Remove translog retention settings [#51697](https://github.com/elastic/elasticsearch/pull/51697) (issue: [#50775](https://github.com/elastic/elasticsearch/issues/50775))

Features/CAT APIs::
* Remove the deprecated `local` parameter for `_cat/indices` [#64868](https://github.com/elastic/elasticsearch/pull/64868) (issue: [#62198](https://github.com/elastic/elasticsearch/issues/62198))
* Remove the deprecated `local` parameter for `_cat/shards` [#64867](https://github.com/elastic/elasticsearch/pull/64867) (issue: [#62197](https://github.com/elastic/elasticsearch/issues/62197))

Features/Features::
* Remove deprecated `._tier` allocation filtering settings [#73074](https://github.com/elastic/elasticsearch/pull/73074) (issue: [#72835](https://github.com/elastic/elasticsearch/issues/72835))

Features/ILM+SLM::
* Add lower bound on `poll_interval` [#39593](https://github.com/elastic/elasticsearch/pull/39593) (issue: [#39163](https://github.com/elastic/elasticsearch/issues/39163))
* Make the ILM `freeze` action a no-op [#77158](https://github.com/elastic/elasticsearch/pull/77158) (issue: [#70192](https://github.com/elastic/elasticsearch/issues/70192))
* Always enforce default tier preference [#79751](https://github.com/elastic/elasticsearch/pull/79751) (issue: [#76147](https://github.com/elastic/elasticsearch/issues/76147))
* Validate that snapshot repository exists for ILM policies at creation/update time [#78468](https://github.com/elastic/elasticsearch/pull/78468) (issues: [#72957](https://github.com/elastic/elasticsearch/issues/72957), [#77657](https://github.com/elastic/elasticsearch/issues/77657))
* Default `cluster.routing.allocation.enforce_default_tier_preference` to `true` [#79275](https://github.com/elastic/elasticsearch/pull/79275) (issues: [#76147](https://github.com/elastic/elasticsearch/issues/76147), [#79210](https://github.com/elastic/elasticsearch/issues/79210))

Features/Indices APIs::
* Change `prefer_v2_templates` parameter to default to true [#55489](https://github.com/elastic/elasticsearch/pull/55489) (issues: [#53101](https://github.com/elastic/elasticsearch/issues/53101), [#55411](https://github.com/elastic/elasticsearch/issues/55411))
* Remove deprecated `_upgrade` API [#64732](https://github.com/elastic/elasticsearch/pull/64732) (issue: [#21337](https://github.com/elastic/elasticsearch/issues/21337))
* Remove local parameter for get field mapping request [#55100](https://github.com/elastic/elasticsearch/pull/55100) (issue: [#55099](https://github.com/elastic/elasticsearch/issues/55099))
* Remove `include_type_name` parameter from REST layer [#48632](https://github.com/elastic/elasticsearch/pull/48632) (issue: [#41059](https://github.com/elastic/elasticsearch/issues/41059))
* Remove the `template` field in index templates [#49460](https://github.com/elastic/elasticsearch/pull/49460) (issue: [#21009](https://github.com/elastic/elasticsearch/issues/21009))
* Remove endpoint for freezing indices [#78918](https://github.com/elastic/elasticsearch/pull/78918) (issues: [#70192](https://github.com/elastic/elasticsearch/issues/70192), [#77273](https://github.com/elastic/elasticsearch/issues/77273))

Features/Watcher::
* Move watcher history to data stream [#64252](https://github.com/elastic/elasticsearch/pull/64252)

Geo::
* Disallow creating `geo_shape` mappings with deprecated parameters [#70850](https://github.com/elastic/elasticsearch/pull/70850) (issue: [#32039](https://github.com/elastic/elasticsearch/issues/32039))
* Remove bounding box query `type` parameter [#74536](https://github.com/elastic/elasticsearch/pull/74536)

Infra/Circuit Breakers::
* Fixed synchronizing inflight breaker with internal variable [#40878](https://github.com/elastic/elasticsearch/pull/40878)

Infra/Core::
* Limit processors by available processors [#44894](https://github.com/elastic/elasticsearch/pull/44894) (issue: [#44889](https://github.com/elastic/elasticsearch/issues/44889))
* Remove `nodes/0` folder prefix from data path [#42489](https://github.com/elastic/elasticsearch/pull/42489)
* Remove `bootstrap.system_call_filter` setting [#72848](https://github.com/elastic/elasticsearch/pull/72848)
* Remove `fixed_auto_queue_size` threadpool type [#52280](https://github.com/elastic/elasticsearch/pull/52280)
* Remove `node.max_local_storage_nodes` [#42428](https://github.com/elastic/elasticsearch/pull/42428) (issue: [#42426](https://github.com/elastic/elasticsearch/issues/42426))
* Remove camel case named date/time formats [#60044](https://github.com/elastic/elasticsearch/pull/60044)
* Remove legacy role settings [#71163](https://github.com/elastic/elasticsearch/pull/71163) (issues: [#54998](https://github.com/elastic/elasticsearch/issues/54998), [#66409](https://github.com/elastic/elasticsearch/issues/66409), [#71143](https://github.com/elastic/elasticsearch/issues/71143))
* Remove `processors` setting [#45905](https://github.com/elastic/elasticsearch/pull/45905) (issue: [#45855](https://github.com/elastic/elasticsearch/issues/45855))
* Remove the `local` parameter of `/_cat/nodes` [#50594](https://github.com/elastic/elasticsearch/pull/50594) (issues: [#50088](https://github.com/elastic/elasticsearch/issues/50088), [#50499](https://github.com/elastic/elasticsearch/issues/50499))
* Remove the listener thread pool [#53314](https://github.com/elastic/elasticsearch/pull/53314) (issue: [#53049](https://github.com/elastic/elasticsearch/issues/53049))
* Remove the node local storage setting [#54381](https://github.com/elastic/elasticsearch/pull/54381) (issue: [#54374](https://github.com/elastic/elasticsearch/issues/54374))
* Remove the `pidfile` setting [#45940](https://github.com/elastic/elasticsearch/pull/45940) (issue: [#45938](https://github.com/elastic/elasticsearch/issues/45938))
* Removes `week_year` date format [#63384](https://github.com/elastic/elasticsearch/pull/63384) (issue: [#60707](https://github.com/elastic/elasticsearch/issues/60707))
* System indices treated as restricted indices [#74212](https://github.com/elastic/elasticsearch/pull/74212) (issue: [#69298](https://github.com/elastic/elasticsearch/issues/69298))
* Remove Joda dependency [#79007](https://github.com/elastic/elasticsearch/pull/79007)
* Remove Joda support from date formatters [#78990](https://github.com/elastic/elasticsearch/pull/78990)
* All system indices are hidden indices [#79512](https://github.com/elastic/elasticsearch/pull/79512)

Infra/Logging::
* Remove slowlog level [#57591](https://github.com/elastic/elasticsearch/pull/57591) (issue: [#56171](https://github.com/elastic/elasticsearch/issues/56171))

Infra/Plugins::
* Remove deprecated basic license feature enablement settings [#56211](https://github.com/elastic/elasticsearch/pull/56211) (issue: [#54745](https://github.com/elastic/elasticsearch/issues/54745))

Infra/REST API::
* Remove content type required setting [#61043](https://github.com/elastic/elasticsearch/pull/61043)
* Remove deprecated endpoints containing `_xpack` [#48170](https://github.com/elastic/elasticsearch/pull/48170) (issue: [#35958](https://github.com/elastic/elasticsearch/issues/35958))
* Remove deprecated endpoints of hot threads API [#55109](https://github.com/elastic/elasticsearch/pull/55109) (issue: [#52640](https://github.com/elastic/elasticsearch/issues/52640))
* Allow parsing Content-Type and Accept headers with version [#61427](https://github.com/elastic/elasticsearch/pull/61427)

Infra/Resiliency::
* Fail node containing ancient closed index [#44264](https://github.com/elastic/elasticsearch/pull/44264) (issues: [#21830](https://github.com/elastic/elasticsearch/issues/21830), [#41731](https://github.com/elastic/elasticsearch/issues/41731), [#44230](https://github.com/elastic/elasticsearch/issues/44230))

Infra/Scripting::
* Consolidate script parsing from object [#59507](https://github.com/elastic/elasticsearch/pull/59507) (issue: [#59391](https://github.com/elastic/elasticsearch/issues/59391))
* Move `script_cache` into _nodes/stats [#59265](https://github.com/elastic/elasticsearch/pull/59265) (issues: [#50152](https://github.com/elastic/elasticsearch/issues/50152), [#59262](https://github.com/elastic/elasticsearch/issues/59262))
* Remove general cache settings [#59262](https://github.com/elastic/elasticsearch/pull/59262) (issue: [#50152](https://github.com/elastic/elasticsearch/issues/50152))

Infra/Settings::
* Change default value of `action.destructive_requires_name` to `true` [#66908](https://github.com/elastic/elasticsearch/pull/66908) (issue: [#61074](https://github.com/elastic/elasticsearch/issues/61074))
* Forbid settings without a namespace [#45947](https://github.com/elastic/elasticsearch/pull/45947) (issues: [#45905](https://github.com/elastic/elasticsearch/issues/45905), [#45940](https://github.com/elastic/elasticsearch/issues/45940))

Ingest::
* Remove default maxmind GeoIP databases from distribution [#78362](https://github.com/elastic/elasticsearch/pull/78362) (issue: [#68920](https://github.com/elastic/elasticsearch/issues/68920))

License::
* Set `xpack.security.enabled` to true for all licenses [#72300](https://github.com/elastic/elasticsearch/pull/72300)
* Enforce license expiration [#79671](https://github.com/elastic/elasticsearch/pull/79671)

Machine Learning::
* Remove deprecated `_xpack` endpoints [#59870](https://github.com/elastic/elasticsearch/pull/59870) (issues: [#35958](https://github.com/elastic/elasticsearch/issues/35958), [#48170](https://github.com/elastic/elasticsearch/issues/48170))
* Remove the ability to update datafeed's `job_id` [#44752](https://github.com/elastic/elasticsearch/pull/44752) (issue: [#44616](https://github.com/elastic/elasticsearch/issues/44616))
* Remove `allow_no_datafeeds` and `allow_no_jobs` parameters from APIs [#80048](https://github.com/elastic/elasticsearch/pull/80048) (issue: [#60732](https://github.com/elastic/elasticsearch/issues/60732))

Mapping::
* Remove `boost` mapping parameter [#62639](https://github.com/elastic/elasticsearch/pull/62639) (issue: [#62623](https://github.com/elastic/elasticsearch/issues/62623))
* Remove support for chained multi-fields [#42333](https://github.com/elastic/elasticsearch/pull/42333) (issues: [#41267](https://github.com/elastic/elasticsearch/issues/41267), [#41926](https://github.com/elastic/elasticsearch/issues/41926))
* Remove support for string in `unmapped_type` [#45675](https://github.com/elastic/elasticsearch/pull/45675)
* Removes typed URLs from mapping APIs [#41676](https://github.com/elastic/elasticsearch/pull/41676)

Network::
* Remove client feature tracking [#44929](https://github.com/elastic/elasticsearch/pull/44929) (issues: [#31020](https://github.com/elastic/elasticsearch/issues/31020), [#42538](https://github.com/elastic/elasticsearch/issues/42538), [#44667](https://github.com/elastic/elasticsearch/issues/44667))
* Remove escape hatch permitting incompatible builds [#65753](https://github.com/elastic/elasticsearch/pull/65753) (issues: [#65249](https://github.com/elastic/elasticsearch/issues/65249), [#65601](https://github.com/elastic/elasticsearch/issues/65601))

Packaging::
* Remove SysV init support [#51716](https://github.com/elastic/elasticsearch/pull/51716) (issue: [#51480](https://github.com/elastic/elasticsearch/issues/51480))
* Remove support for `JAVA_HOME` [#69149](https://github.com/elastic/elasticsearch/pull/69149) (issue: [#55820](https://github.com/elastic/elasticsearch/issues/55820))
* Remove no-jdk distributions [#76896](https://github.com/elastic/elasticsearch/pull/76896) (issue: [#65109](https://github.com/elastic/elasticsearch/issues/65109))
* Require Java 17 for running Elasticsearch [#79873](https://github.com/elastic/elasticsearch/pull/79873)

Recovery::
* Remove dangling index auto import functionality [#59698](https://github.com/elastic/elasticsearch/pull/59698) (issue: [#48366](https://github.com/elastic/elasticsearch/issues/48366))

Reindex::
* Reindex from Remote encoding [#41007](https://github.com/elastic/elasticsearch/pull/41007) (issue: [#40303](https://github.com/elastic/elasticsearch/issues/40303))
* Reindex remove outer level size [#43373](https://github.com/elastic/elasticsearch/pull/43373) (issues: [#24344](https://github.com/elastic/elasticsearch/issues/24344), [#41894](https://github.com/elastic/elasticsearch/issues/41894))

Rollup::
* `RollupStart` endpoint should return OK if job already started [#41502](https://github.com/elastic/elasticsearch/pull/41502) (issues: [#35928](https://github.com/elastic/elasticsearch/issues/35928), [#39845](https://github.com/elastic/elasticsearch/issues/39845))

Search::
* Decouple shard allocation awareness from search and get requests [#45735](https://github.com/elastic/elasticsearch/pull/45735) (issue: [#43453](https://github.com/elastic/elasticsearch/issues/43453))
* Fix range query on date fields for number inputs [#63692](https://github.com/elastic/elasticsearch/pull/63692) (issue: [#63680](https://github.com/elastic/elasticsearch/issues/63680))
* Make fuzziness reject illegal values earlier [#33511](https://github.com/elastic/elasticsearch/pull/33511)
* Make remote cluster resolution stricter [#40419](https://github.com/elastic/elasticsearch/pull/40419) (issue: [#37863](https://github.com/elastic/elasticsearch/issues/37863))
* Parse empty first line in msearch request body as action metadata [#41011](https://github.com/elastic/elasticsearch/pull/41011) (issue: [#39841](https://github.com/elastic/elasticsearch/issues/39841))
* Remove `CommonTermsQuery` and `cutoff_frequency` param [#42654](https://github.com/elastic/elasticsearch/pull/42654) (issue: [#37096](https://github.com/elastic/elasticsearch/issues/37096))
* Remove `type` query [#47207](https://github.com/elastic/elasticsearch/pull/47207) (issue: [#41059](https://github.com/elastic/elasticsearch/issues/41059))
* Remove `use_field_mapping` format option for docvalue fields [#55622](https://github.com/elastic/elasticsearch/pull/55622)
* Remove deprecated `SimpleQueryStringBuilder` parameters [#57200](https://github.com/elastic/elasticsearch/pull/57200)
* Remove deprecated `search.remote` settings [#42381](https://github.com/elastic/elasticsearch/pull/42381) (issues: [#33413](https://github.com/elastic/elasticsearch/issues/33413), [#38556](https://github.com/elastic/elasticsearch/issues/38556))
* Remove deprecated sort options: `nested_path` and `nested_filter` [#42809](https://github.com/elastic/elasticsearch/pull/42809) (issue: [#27098](https://github.com/elastic/elasticsearch/issues/27098))
* Remove deprecated vector functions [#48725](https://github.com/elastic/elasticsearch/pull/48725) (issue: [#48604](https://github.com/elastic/elasticsearch/issues/48604))
* Remove support for `_type` in searches [#68564](https://github.com/elastic/elasticsearch/pull/68564) (issues: [#41059](https://github.com/elastic/elasticsearch/issues/41059), [#68311](https://github.com/elastic/elasticsearch/issues/68311))
* Remove support for sparse vectors [#48781](https://github.com/elastic/elasticsearch/pull/48781) (issue: [#48368](https://github.com/elastic/elasticsearch/issues/48368))
* Remove the object format for `indices_boost` [#55078](https://github.com/elastic/elasticsearch/pull/55078)
* Removes type from `TermVectors` APIs [#42198](https://github.com/elastic/elasticsearch/pull/42198) (issue: [#41059](https://github.com/elastic/elasticsearch/issues/41059))
* Removes typed endpoint from search and related APIs [#41640](https://github.com/elastic/elasticsearch/pull/41640)
* Set max allowed size for stored async response [#74455](https://github.com/elastic/elasticsearch/pull/74455) (issue: [#67594](https://github.com/elastic/elasticsearch/issues/67594))
* `indices.query.bool.max_clause_count` now limits all query clauses [#75297](https://github.com/elastic/elasticsearch/pull/75297)

Security::
* Remove obsolete security settings [#40496](https://github.com/elastic/elasticsearch/pull/40496)
* Remove support of creating CA on the fly when generating certificates [#65590](https://github.com/elastic/elasticsearch/pull/65590) (issue: [#61884](https://github.com/elastic/elasticsearch/issues/61884))
* Remove the `id` field from the `InvalidateApiKey` API [#66671](https://github.com/elastic/elasticsearch/pull/66671) (issue: [#66317](https://github.com/elastic/elasticsearch/issues/66317))
* Remove the migrate tool [#42174](https://github.com/elastic/elasticsearch/pull/42174)
* Compress audit logs [#64472](https://github.com/elastic/elasticsearch/pull/64472) (issue: [#63843](https://github.com/elastic/elasticsearch/issues/63843))
* Remove insecure settings [#46147](https://github.com/elastic/elasticsearch/pull/46147) (issue: [#45947](https://github.com/elastic/elasticsearch/issues/45947))
* Remove `kibana_dashboard_only_user` reserved role [#76507](https://github.com/elastic/elasticsearch/pull/76507)

Snapshot/Restore::
* Blob store compress default to `true` [#40033](https://github.com/elastic/elasticsearch/pull/40033)
* Get snapshots support for multiple repositories [#42090](https://github.com/elastic/elasticsearch/pull/42090) (issue: [#41210](https://github.com/elastic/elasticsearch/issues/41210))
* Remove repository stats API [#62309](https://github.com/elastic/elasticsearch/pull/62309) (issue: [#62297](https://github.com/elastic/elasticsearch/issues/62297))
* Remove frozen cache setting leniency [#71013](https://github.com/elastic/elasticsearch/pull/71013) (issue: [#70341](https://github.com/elastic/elasticsearch/issues/70341))
* Adjust snapshot index resolution behavior to be more intuitive [#79670](https://github.com/elastic/elasticsearch/pull/79670) (issue: [#78320](https://github.com/elastic/elasticsearch/issues/78320))

TLS::
* Reject misconfigured/ambiguous SSL server config [#45892](https://github.com/elastic/elasticsearch/pull/45892)
* Remove support for configurable PKCS#11 keystores [#75404](https://github.com/elastic/elasticsearch/pull/75404)
* Remove the client transport profile filter [#43236](https://github.com/elastic/elasticsearch/pull/43236)
