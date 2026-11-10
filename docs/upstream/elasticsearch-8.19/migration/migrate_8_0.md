<!-- Converted from migration/migrate_8_0.asciidoc (AsciiDoc). Includes are inlined. -->

## Migrating to 8.0

This section discusses the changes that you need to be aware of when migrating
your application to Elasticsearch 8.0.

See also release-highlights and es-release-notes.

### Breaking changes

The following changes in Elasticsearch 8.0 might affect your applications
and prevent them from operating normally.
Before upgrading to 8.0, review these changes and take the described steps
to mitigate the impact.

(See `migration/migrate_8_0/cluster-node-setting-changes.md`)
(See `migration/migrate_8_0/command-line-tool-changes.md`)
(See `migration/migrate_8_0/index-setting-changes.md`)
(See `migration/migrate_8_0/java-api-changes.md`)
(See `migration/migrate_8_0/jvm-option-changes.md`)
(See `migration/migrate_8_0/logging-changes.md`)
(See `migration/migrate_8_0/mapping-changes.md`)
(See `migration/migrate_8_0/packaging-changes.md`)
(See `migration/migrate_8_0/painless-changes.md`)
(See `migration/migrate_8_0/plugin-changes.md`)
(See `migration/migrate_8_0/rest-api-changes.md`)
(See `migration/migrate_8_0/sql-jdbc-changes.md`)
(See `migration/migrate_8_0/system-req-changes.md`)
(See `migration/migrate_8_0/transform.md`)

### Deprecations

The following functionality has been deprecated in Elasticsearch 8.0
and will be removed in a future version.
While this won't have an immediate impact on your applications,
we strongly encourage you take the described steps to update your code
after upgrading to 8.0.

To find out if you are using any deprecated functionality,
enable deprecation logging.

#### Cluster and node setting deprecations

**We no longer recommend using transient cluster settings.**
*Details* +
We no longer recommend using transient cluster settings. Use persistent cluster
settings instead. If a cluster becomes unstable, transient settings can clear
unexpectedly, resulting in an undesired cluster configuration.

*Impact* +
Transient cluster settings are not yet deprecated, but we plan to deprecate them
in a future release. For migration steps, see the
https://www.elastic.co/guide/en/elasticsearch/reference/8.19/transient-settings-migration-guide.html[Transient settings migration
guide].

#### Command line tool deprecations

**Tip:** {ess-skip-section}

**The `elasticsearch-setup-passwords` tool is deprecated.**
*Details* +
The `elasticsearch-setup-passwords` tool is deprecated in 8.0. To
manually reset the password for built-in users (including the `elastic` user), use
the [`elasticsearch-reset-password`](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/reset-password.html) tool, the Elasticsearch
[change passwords API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-api-change-password.html), or the
User Management features in Kibana.
`elasticsearch-setup-passwords` will be removed in a future release.

*Impact* +
Passwords are generated automatically for the `elastic` user when you start Elasticsearch for the first time. If you run `elasticsearch-setup-passwords` after
starting Elasticsearch, it will fail because the `elastic`
user password is already configured.

(See `migration/migrate_8_0/migrate_to_java_time.md`)
(See `migration/transient-settings-migration-guide.md`)
