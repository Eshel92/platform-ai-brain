<!-- Converted from setup/important-settings/path-settings.asciidoc (AsciiDoc). Includes are inlined. -->

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
