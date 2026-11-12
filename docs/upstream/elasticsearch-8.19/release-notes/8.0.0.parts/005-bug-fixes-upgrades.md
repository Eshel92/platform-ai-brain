<!-- Part 5 of 5 of release-notes/8.0.0.md (split because the page is big). -->

### Bug fixes

Aggregations::
* Fix BWC issues for `x_pack/usage` [#55181](https://github.com/elastic/elasticsearch/pull/55181) (issue: [#54847](https://github.com/elastic/elasticsearch/issues/54847))
* Fix `DoubleBounds` null serialization [#59475](https://github.com/elastic/elasticsearch/pull/59475)
* Fix `TopHitsAggregationBuilder` adding duplicate `_score` sort clauses [#42179](https://github.com/elastic/elasticsearch/pull/42179) (issue: [#42154](https://github.com/elastic/elasticsearch/issues/42154))
* Fix `t_test` usage stats [#54753](https://github.com/elastic/elasticsearch/pull/54753) (issue: [#54744](https://github.com/elastic/elasticsearch/issues/54744))
* Throw exception if legacy interval cannot be parsed in `DateIntervalWrapper` [#41972](https://github.com/elastic/elasticsearch/pull/41972) (issue: [#41970](https://github.com/elastic/elasticsearch/issues/41970))

Autoscaling::
* Autoscaling use adjusted total memory [#80528](https://github.com/elastic/elasticsearch/pull/80528) (issue: [#78750](https://github.com/elastic/elasticsearch/issues/78750))

CCR::
* Fix `AutoFollow` version checks [#73776](https://github.com/elastic/elasticsearch/pull/73776) (issue: [#72935](https://github.com/elastic/elasticsearch/issues/72935))

Cluster Coordination::
* Apply cluster states in system context [#53785](https://github.com/elastic/elasticsearch/pull/53785) (issue: [#53751](https://github.com/elastic/elasticsearch/issues/53751))

Data streams::
* Prohibit restoring a data stream alias with a conflicting write data stream [#81217](https://github.com/elastic/elasticsearch/pull/81217) (issue: [#80976](https://github.com/elastic/elasticsearch/issues/80976))

Distributed::
* Introduce `?wait_for_active_shards=index-setting` [#67158](https://github.com/elastic/elasticsearch/pull/67158) (issue: [#66419](https://github.com/elastic/elasticsearch/issues/66419))
* Fixes to task result index mapping [#50359](https://github.com/elastic/elasticsearch/pull/50359) (issue: [#50248](https://github.com/elastic/elasticsearch/issues/50248))

Features/CAT APIs::
* Fix cat recovery display of bytes fields [#40379](https://github.com/elastic/elasticsearch/pull/40379) (issue: [#40335](https://github.com/elastic/elasticsearch/issues/40335))

Features/ILM+SLM::
* Ensuring that the `ShrinkAction` does not hang if total shards per node is too low [#76732](https://github.com/elastic/elasticsearch/pull/76732) (issue: [#44070](https://github.com/elastic/elasticsearch/issues/44070))
* Less verbose serialization of snapshot failure in SLM metadata [#80942](https://github.com/elastic/elasticsearch/pull/80942) (issue: [#77466](https://github.com/elastic/elasticsearch/issues/77466))

Features/Indices APIs::
* Fix `ComposableIndexTemplate` equals when `composed_of` is null [#80864](https://github.com/elastic/elasticsearch/pull/80864)

Features/Java High Level REST Client::
* The Java High Level Rest Client (HLRC) has been removed and replaced by a new
Elasticsearch Java client. For migration steps, refer to
{java-api-client}/migrate-hlrc.html[Migrate from the High Level Rest Client].

Geo::
* Preprocess polygon rings before processing it for decomposition [#59501](https://github.com/elastic/elasticsearch/pull/59501) (issues: [#54441](https://github.com/elastic/elasticsearch/issues/54441), [#59386](https://github.com/elastic/elasticsearch/issues/59386))

Infra/Core::
* Add searchable snapshot cache folder to `NodeEnvironment` [#66297](https://github.com/elastic/elasticsearch/pull/66297) (issue: [#65725](https://github.com/elastic/elasticsearch/issues/65725))
* CLI tools: Write errors to stderr instead of stdout [#45586](https://github.com/elastic/elasticsearch/pull/45586) (issue: [#43260](https://github.com/elastic/elasticsearch/issues/43260))
* Precompute `ParsedMediaType` for XContentType [#67409](https://github.com/elastic/elasticsearch/pull/67409)
* Prevent stack overflow in rounding [#80450](https://github.com/elastic/elasticsearch/pull/80450)

Infra/Logging::
* Fix NPE when logging null values in JSON [#53715](https://github.com/elastic/elasticsearch/pull/53715) (issue: [#46702](https://github.com/elastic/elasticsearch/issues/46702))
* Fix stats in slow logs to be a escaped JSON [#44642](https://github.com/elastic/elasticsearch/pull/44642)
* Populate data stream fields when `xOpaqueId` not provided [#62156](https://github.com/elastic/elasticsearch/pull/62156)

Infra/REST API::
* Do not allow spaces within `MediaType's` parameters [#64650](https://github.com/elastic/elasticsearch/pull/64650) (issue: [#51816](https://github.com/elastic/elasticsearch/issues/51816))
* Handle incorrect header values [#64708](https://github.com/elastic/elasticsearch/pull/64708) (issues: [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#64689](https://github.com/elastic/elasticsearch/issues/64689))
* Ignore media ranges when parsing [#64721](https://github.com/elastic/elasticsearch/pull/64721) (issues: [#51816](https://github.com/elastic/elasticsearch/issues/51816), [#64689](https://github.com/elastic/elasticsearch/issues/64689))
* `RestController` should not consume request content [#44902](https://github.com/elastic/elasticsearch/pull/44902) (issue: [#37504](https://github.com/elastic/elasticsearch/issues/37504))
* Handle exceptions thrown from `RestCompatibleVersionHelper` [#80253](https://github.com/elastic/elasticsearch/pull/80253) (issues: [#78214](https://github.com/elastic/elasticsearch/issues/78214), [#79060](https://github.com/elastic/elasticsearch/issues/79060))

Infra/Scripting::
* Change compound assignment structure to support string concatenation [#61825](https://github.com/elastic/elasticsearch/pull/61825)
* Fixes casting in constant folding [#61508](https://github.com/elastic/elasticsearch/pull/61508)
* Several minor Painless fixes [#61594](https://github.com/elastic/elasticsearch/pull/61594)
* Fix duplicated allow lists upon script engine creation [#82820](https://github.com/elastic/elasticsearch/pull/82820) (issue: [#82778](https://github.com/elastic/elasticsearch/issues/82778))

Infra/Settings::
* Stricter `UpdateSettingsRequest` parsing on the REST layer [#79227](https://github.com/elastic/elasticsearch/pull/79227) (issue: [#29268](https://github.com/elastic/elasticsearch/issues/29268))
* Set Auto expand replica on deprecation log data stream [#79226](https://github.com/elastic/elasticsearch/pull/79226) (issue: [#78991](https://github.com/elastic/elasticsearch/issues/78991))

Ingest::
* Adjust default geoip logging to be less verbose [#81404](https://github.com/elastic/elasticsearch/pull/81404) (issue: [#81356](https://github.com/elastic/elasticsearch/issues/81356))

Machine Learning::
* Add timeout parameter for delete trained models API [#79739](https://github.com/elastic/elasticsearch/pull/79739) (issue: [#77070](https://github.com/elastic/elasticsearch/issues/77070))
* Tone down ML unassigned job notifications [#79578](https://github.com/elastic/elasticsearch/pull/79578) (issue: [#79270](https://github.com/elastic/elasticsearch/issues/79270))
* Use a new annotations index for future annotations [#79006](https://github.com/elastic/elasticsearch/pull/79006) (issue: [#78439](https://github.com/elastic/elasticsearch/issues/78439))
* Set model state compatibility version to 8.0.0 {ml-pull}2139[#2139]
* Check that `total_definition_length` is consistent before starting a deployment [#80553](https://github.com/elastic/elasticsearch/pull/80553)
* Fail inference processor more consistently on certain error types [#81475](https://github.com/elastic/elasticsearch/pull/81475)
* Optimize the job stats call to do fewer searches [#82362](https://github.com/elastic/elasticsearch/pull/82362) (issue: [#82255](https://github.com/elastic/elasticsearch/issues/82255))

Mapping::
* Remove assertions that mappings have one top-level key [#58779](https://github.com/elastic/elasticsearch/pull/58779) (issue: [#58521](https://github.com/elastic/elasticsearch/issues/58521))

Packaging::
* Suppress illegal access in plugin install [#41620](https://github.com/elastic/elasticsearch/pull/41620) (issue: [#41478](https://github.com/elastic/elasticsearch/issues/41478))

Recovery::
* Make shard started response handling only return after the cluster state update completes [#82790](https://github.com/elastic/elasticsearch/pull/82790) (issue: [#81628](https://github.com/elastic/elasticsearch/issues/81628))

SQL::
* Introduce dedicated node for `HAVING` declaration [#71279](https://github.com/elastic/elasticsearch/pull/71279) (issue: [#69758](https://github.com/elastic/elasticsearch/issues/69758))
* Make `RestSqlQueryAction` thread-safe [#69901](https://github.com/elastic/elasticsearch/pull/69901)

Search::
* Check for negative `from` values in search request body [#54953](https://github.com/elastic/elasticsearch/pull/54953) (issue: [#54897](https://github.com/elastic/elasticsearch/issues/54897))
* Fix `VectorsFeatureSetUsage` serialization in BWC mode [#55399](https://github.com/elastic/elasticsearch/pull/55399) (issue: [#55378](https://github.com/elastic/elasticsearch/issues/55378))
* Handle total hits equal to `track_total_hits` [#37907](https://github.com/elastic/elasticsearch/pull/37907) (issue: [#37897](https://github.com/elastic/elasticsearch/issues/37897))
* Improve error msg for CCS request on node without remote cluster role [#60351](https://github.com/elastic/elasticsearch/pull/60351) (issue: [#59683](https://github.com/elastic/elasticsearch/issues/59683))
* Remove unsafe assertion in wildcard field [#78966](https://github.com/elastic/elasticsearch/pull/78966)

Security::
* Allow access to restricted system indices for reserved system roles [#76845](https://github.com/elastic/elasticsearch/pull/76845)

Snapshot/Restore::
* Fix `GET /_snapshot/_all/_all` if there are no repos [#43558](https://github.com/elastic/elasticsearch/pull/43558) (issue: [#43547](https://github.com/elastic/elasticsearch/issues/43547))
* Don't fill stack traces in `SnapshotShardFailure` [#80009](https://github.com/elastic/elasticsearch/pull/80009) (issue: [#79718](https://github.com/elastic/elasticsearch/issues/79718))
* Remove custom metadata if there is nothing to restore [#81373](https://github.com/elastic/elasticsearch/pull/81373) (issues: [#81247](https://github.com/elastic/elasticsearch/issues/81247), [#82019](https://github.com/elastic/elasticsearch/issues/82019))


### Regressions

Search::
* Disable numeric sort optimization conditionally [#78103](https://github.com/elastic/elasticsearch/pull/78103)


### Upgrades

Authentication::
* Upgrade to UnboundID LDAP SDK v6.0.2 [#79332](https://github.com/elastic/elasticsearch/pull/79332)

Infra/Logging::
* Upgrade ECS logging layout to latest version [#80500](https://github.com/elastic/elasticsearch/pull/80500)

Search::
* Upgrade to Lucene 9 [#81426](https://github.com/elastic/elasticsearch/pull/81426)

Security::
* Update to OpenSAML 4 [#77012](https://github.com/elastic/elasticsearch/pull/77012) (issue: [#71983](https://github.com/elastic/elasticsearch/issues/71983))

Snapshot/Restore::
* Upgrade repository-hdfs plugin to Hadoop 3 [#76897](https://github.com/elastic/elasticsearch/pull/76897)
