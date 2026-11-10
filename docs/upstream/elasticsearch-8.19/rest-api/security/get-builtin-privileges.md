<!-- Converted from rest-api/security/get-builtin-privileges.asciidoc (AsciiDoc). Includes are inlined. -->

### Get builtin privileges API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Retrieves the list of cluster privileges and
index privileges that are
available in this version of Elasticsearch.

#### Request

`GET /_security/privilege/_builtin`

#### Prerequisites

* To use this API, you must have the `read_security` cluster privilege
(or a greater privilege such as `manage_security` or `all`).

#### Description

This API retrieves the set of cluster and index privilege names that are
available in the version of Elasticsearch that is being queried.

To check whether a user has particular privileges, use the
has privileges API.

#### Response body

The response is an object with two fields:

`cluster`:: (array of string) The list of
cluster privileges that are understood by this
version of Elasticsearch.

`index`:: (array of string) The list of
index privileges that are understood by this version
of Elasticsearch.

`remote_cluster`:: (array of string) The list of
remote_cluster privileges that are understood by this version
of Elasticsearch.

#### Examples

The following example retrieves the names of all builtin privileges:

```console
GET /_security/privilege/_builtin
```

A successful call returns an object with "cluster", "index", and "remote_cluster" fields.

```console-result
{
  "cluster" : [
    "all",
    "cancel_task",
    "create_snapshot",
    "cross_cluster_replication",
    "cross_cluster_search",
    "delegate_pki",
    "grant_api_key",
    "manage",
    "manage_api_key",
    "manage_autoscaling",
    "manage_behavioral_analytics",
    "manage_ccr",
    "manage_connector",
    "manage_data_frame_transforms",
    "manage_data_stream_global_retention",
    "manage_enrich",
    "manage_ilm",
    "manage_index_templates",
    "manage_inference",
    "manage_ingest_pipelines",
    "manage_logstash_pipelines",
    "manage_ml",
    "manage_oidc",
    "manage_own_api_key",
    "manage_pipeline",
    "manage_rollup",
    "manage_saml",
    "manage_search_application",
    "manage_search_query_rules",
    "manage_search_synonyms",
    "manage_security",
    "manage_service_account",
    "manage_slm",
    "manage_token",
    "manage_transform",
    "manage_user_profile",
    "manage_watcher",
    "monitor",
    "monitor_connector",
    "monitor_data_frame_transforms",
    "monitor_data_stream_global_retention",
    "monitor_enrich",
    "monitor_inference",
    "monitor_ml",
    "monitor_rollup",
    "monitor_snapshot",
    "monitor_stats",
    "monitor_text_structure",
    "monitor_transform",
    "monitor_watcher",
    "none",
    "post_behavioral_analytics_event",
    "read_ccr",
    "read_connector_secrets",
    "read_fleet_secrets",
    "read_ilm",
    "read_pipeline",
    "read_security",
    "read_slm",
    "transport_client",
    "write_connector_secrets",
    "write_fleet_secrets"
  ],
  "index" : [
    "all",
    "auto_configure",
    "create",
    "create_doc",
    "create_index",
    "cross_cluster_replication",
    "cross_cluster_replication_internal",
    "delete",
    "delete_index",
    "index",
    "maintenance",
    "manage",
    "manage_data_stream_lifecycle",
    "manage_failure_store",
    "manage_follow_index",
    "manage_ilm",
    "manage_leader_index",
    "monitor",
    "none",
    "read",
    "read_cross_cluster",
    "read_failure_store",
    "view_index_metadata",
    "write"
  ],
  "remote_cluster" : [
    "monitor_enrich",
    "monitor_stats"
  ]
}
```
