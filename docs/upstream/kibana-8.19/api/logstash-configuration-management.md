<!-- Converted from api/logstash-configuration-management.asciidoc (AsciiDoc). Includes are inlined. -->

## Logstash configuration management APIs

Programmatically integrate with Logstash configuration management.

**Warning:** Do not directly access the `.logstash` index. The structure of the `.logstash` index is subject to change, which could cause your integration to break. Instead, use the Logstash configuration management APIs.

The following Logstash configuration management APIs are available:

* Delete Logstash pipeline API to delete a centrally-managed Logstash pipeline

* List Logstash pipeline API to list all centrally-managed Logstash pipelines

* Create Logstash pipeline API to create a centrally-managed Logstash pipeline, or update an existing pipeline

* Retrieve pipeline API to retrieve a centrally-managed Logstash pipeline

(See `api/logstash-configuration-management/delete-pipeline.md`)
(See `api/logstash-configuration-management/list-pipeline.md`)
(See `api/logstash-configuration-management/create-logstash.md`)
(See `api/logstash-configuration-management/retrieve-pipeline.md`)
