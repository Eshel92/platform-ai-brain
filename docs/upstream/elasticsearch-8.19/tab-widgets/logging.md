<!-- Converted from tab-widgets/logging.asciidoc (AsciiDoc). Includes are inlined. -->

On Docker, log messages go to the console and are handled by the
configured Docker logging driver. To access logs, run `docker logs`.

For Debian installations, Elasticsearch writes logs to `/var/log/elasticsearch`.

For RPM installations, Elasticsearch writes logs to `/var/log/elasticsearch`.

For macOS `.tar.gz` installations, Elasticsearch writes logs to
`$ES_HOME/logs`.

Files in `$ES_HOME` risk deletion during an upgrade. In production, we strongly
recommend you set `path.logs` to a location outside of `$ES_HOME`.
See path-settings.

For Linux `.tar.gz` installations, Elasticsearch writes logs to
`$ES_HOME/logs`.

Files in `$ES_HOME` risk deletion during an upgrade. In production, we strongly
recommend you set `path.logs` to a location outside of `$ES_HOME`.
See path-settings.

For Windows `.zip` installations, Elasticsearch writes logs to
`%ES_HOME%\logs`.

Files in `%ES_HOME%` risk deletion during an upgrade. In production, we strongly
recommend you set `path.logs` to a location outside of `%ES_HOME%``.
See path-settings.
