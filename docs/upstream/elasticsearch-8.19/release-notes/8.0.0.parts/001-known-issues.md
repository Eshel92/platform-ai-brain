<!-- Part 1 of 5 of release-notes/8.0.0.md (split because the page is big). -->

### Known issues

* If you installed Elasticsearch from an archive on an aarch64 platform like Linux ARM or macOS M1, the
`elastic` user password and Kibana enrollment token are not generated
automatically when starting your node for the first time.
After the node starts, generate the `elastic` password with the
`bin/elasticsearch-reset-password` tool:

```bash
bin/elasticsearch-reset-password -u elastic
```

Then, create an enrollment token for Kibana with the
`bin/elasticsearch-create-enrollment-token` tool:

```bash
bin/elasticsearch-create-enrollment-token -s kibana
```
* Parsing a request when the last element in an array is filtered out
(for instance using `_source_includes`) fails. This
is due to [a bug in Jackson parser](https://github.com/FasterXML/jackson-core/issues/882).
Fixed in Elasticsearch 8.6.1 ([#91456](https://github.com/elastic/elasticsearch/pull/92480))
* Elasticsearch versions 8.0.0–8.4.3 fail to start on Linux hosts that use
[cgroups](https://man7.org/linux/man-pages/man7/cgroups.7.html) version 2 exclusively
with the bundled JDK. Upgrade to 8.5.0 or later to resolve this.
Refer to [our KB article](https://ela.st/es-may-fail-on-cgroup-v2) for more guidance.
