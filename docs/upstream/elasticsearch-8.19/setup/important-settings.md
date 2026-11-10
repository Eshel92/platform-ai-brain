<!-- Converted from setup/important-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Important Elasticsearch configuration

Elasticsearch requires very little configuration to get started, but there are a number
of items which *must* be considered before using your cluster in production:

* Path settings
* Cluster name setting
* Node name setting
* Network host settings
* Discovery settings
* Heap size settings
* JVM heap dump path setting
* GC logging settings
* Temporary directory settings
* JVM fatal error log setting
* Cluster backups

Our {ess-trial}[Elastic Cloud] service configures these items automatically, making
your cluster production-ready by default.

#### Path settings

Elasticsearch writes the data you index to indices and data streams to a `data`
directory. Elasticsearch writes its own application logs, which contain information about
cluster health and operations, to a `logs` directory.

For macOS `.tar.gz`, Linux `.tar.gz`, and
Windows `.zip` installations, `data` and `logs` are
subdirectories of `$ES_HOME` by default. However, files in `$ES_HOME` risk
deletion during an upgrade.

In production, we strongly recommend you set the `path.data` and `path.logs` in
`elasticsearch.yml` to locations outside of `$ES_HOME`. Docker,
Debian, and RPM installations write
data and log to locations outside of `$ES_HOME` by default.

Supported `path.data` and `path.logs` values vary by platform:

Linux and macOS installations support Unix-style paths:

```yaml
path:
  data: /var/data/elasticsearch
  logs: /var/log/elasticsearch
```

Windows installations support DOS paths with escaped backslashes:

```yaml
path:
  data: "C:\\Elastic\\Elasticsearch\\data"
  logs: "C:\\Elastic\\Elasticsearch\\logs"
```
**Warning:** Don't modify anything within the data directory or run processes that
might interfere with its contents. If something other than Elasticsearch modifies the
contents of the data directory, then Elasticsearch may fail, reporting corruption or
other data inconsistencies, or may appear to work correctly having silently
lost some of your data. Don't attempt to take filesystem backups of the data
directory; there is no supported way to restore such a backup. Instead, use
snapshot-restore to take backups safely. Don't run virus scanners on the
data directory. A virus scanner can prevent Elasticsearch from working correctly and may
modify the contents of the data directory. The data directory contains no
executables so a virus scan will only find false positives.
Elasticsearch offers a deprecated setting that allows you to specify multiple paths in `path.data`. 
To learn about this setting, and how to migrate away from it, refer to multiple-data-paths.

(See `setup/important-settings/cluster-name.md`)

#### Node name setting

Elasticsearch uses `node.name` as a human-readable identifier for a
particular instance of Elasticsearch. This name is included in the response
of many APIs. The node name defaults to the hostname of the machine when
Elasticsearch starts, but can be configured explicitly in
`elasticsearch.yml`:

```yaml
node.name: prod-data-2
```

(See `setup/important-settings/network-host.md`)
(See `setup/important-settings/discovery-settings.md`)
(See `setup/important-settings/heap-size.md`)
(See `setup/important-settings/heap-dump-path.md`)
(See `setup/important-settings/gc-logging.md`)
(See `setup/important-settings/es-tmpdir.md`)
(See `setup/important-settings/error-file.md`)
(See `setup/important-settings/snapshot.md`)
