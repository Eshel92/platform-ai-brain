<!-- Converted from migration/apis/feature-migration.asciidoc (AsciiDoc). Includes are inlined. -->

### Feature migration APIs

**New API reference**
For the most up-to-date API details, refer to [Migration APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-migration).

**Tip:** These APIs are designed for indirect use by Kibana's **Upgrade Assistant**.
We strongly recommend you use the **Upgrade Assistant** to upgrade from
{prev-major-last} to {version}. For upgrade instructions, refer to
{stack-ref}/upgrading-elastic-stack.html[Upgrading to Elastic {version}].
Version upgrades sometimes require changes to how features store configuration
information and data in system indices. The feature migration APIs enable you to
see what features require changes, initiate the automatic migration process, and
check migration status.

Some functionality might be temporarily unavailable during the migration
process.

#### Request

`GET /_migration/system_features`

`POST /_migration/system_features`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

#### Description

Submit a GET request to the `_migration/system_features` endpoint to see what
features need to be migrated and the status of any migrations that are in
progress.

Submit a POST request to the endpoint to start the migration process.

#### Examples

When you submit a GET request to the `_migration/system_features` endpoint, the
response indicates the status of any features that need to be migrated.

```console
GET /_migration/system_features
```

Example response:

```console-result
{
  "features" : [
    {
      "feature_name" : "async_search",
      "minimum_index_version" : "8100099",
      "migration_status" : "NO_MIGRATION_NEEDED",
      "indices" : [ ]
    },
    {
      "feature_name" : "enrich",
      "minimum_index_version" : "8100099",
      "migration_status" : "NO_MIGRATION_NEEDED",
      "indices" : [ ]
    },
    {
      "feature_name" : "ent_search",
      "minimum_index_version" : "8100099",
      "migration_status" : "NO_MIGRATION_NEEDED",
      "indices" : [ ]
    },
    {
      "feature_name" : "fleet",
      "minimum_index_version" : "8100099",
      "migration_status" : "NO_MIGRATION_NEEDED",
      "indices" : [ ]
    },
    {
      "feature_name" : "geoip",
      "minimum_index_version" : "8100099",
      "migration_status" : "NO_MIGRATION_NEEDED",
      "indices" : [ ]
    },
    {
      "feature_name" : "kibana",
      "minimum_index_version" : "8100099",
      "migration_status" : "NO_MIGRATION_NEEDED",
      "indices" : [ ]
    },
    {
      "feature_name" : "logstash_management",
      "minimum_index_version" : "8100099",
      "migration_status" : "NO_MIGRATION_NEEDED",
      "indices" : [ ]
    },
    {
      "feature_name" : "machine_learning",
      "minimum_index_version" : "8100099",
      "migration_status" : "NO_MIGRATION_NEEDED",
      "indices" : [ ]
    },
    {
      "feature_name" : "searchable_snapshots",
      "minimum_index_version" : "8100099",
      "migration_status" : "NO_MIGRATION_NEEDED",
      "indices" : [ ]
    },
    {
      "feature_name" : "security",
      "minimum_index_version" : "8100099",
      "migration_status" : "NO_MIGRATION_NEEDED",
      "indices" : [ ]
    },
    {
      "feature_name" : "synonyms",
      "minimum_index_version" : "8100099",
      "migration_status" : "NO_MIGRATION_NEEDED",
      "indices" : [ ]
    },
    {
      "feature_name" : "tasks",
      "minimum_index_version" : "8100099",
      "migration_status" : "NO_MIGRATION_NEEDED",
      "indices" : [ ]
    },
    {
      "feature_name" : "transform",
      "minimum_index_version" : "8100099",
      "migration_status" : "NO_MIGRATION_NEEDED",
      "indices" : [ ]
    },
    {
      "feature_name" : "watcher",
      "minimum_index_version" : "8100099",
      "migration_status" : "NO_MIGRATION_NEEDED",
      "indices" : [ ]
    }
  ],
  "migration_status" : "NO_MIGRATION_NEEDED"
}
```

When you submit a POST request to the `_migration/system_features` endpoint to
start the migration process, the response indicates what features will be
migrated.

```console
POST /_migration/system_features
```

Example response:

```console-result
{
  "accepted" : true,
  "features" : [
    {
      "feature_name" : "security" <1>
    }
  ]
}
```

<1> Elasticsearch security will be migrated before the cluster is upgraded.

Subsequent GET requests will return the status of the migration process.
