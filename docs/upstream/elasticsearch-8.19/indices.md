<!-- Converted from indices.asciidoc (AsciiDoc). Includes are inlined. -->

## Index APIs

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Index APIs are used to manage individual indices,
index settings, aliases, mappings, and index templates.

### Index management:

* indices-create-index
* indices-delete-index
* indices-get-index
* indices-exists
* indices-close
* indices-open-close
* indices-shrink-index
* indices-split-index
* indices-clone-index
* indices-rollover-index
* unfreeze-index-api
* indices-resolve-index-api
* indices-resolve-cluster-api
* indices-downsample-data-stream

### Mapping management:

* indices-put-mapping
* indices-get-mapping
* indices-get-field-mapping
* indices-disk-usage

### Alias management:

* indices-aliases
* indices-add-alias
* indices-get-alias
* indices-alias-exists
* indices-delete-alias

### Index settings:

* indices-update-settings
* indices-get-settings
* indices-analyze

### Index templates:

Index templates automatically apply settings, mappings, and aliases to new indices.
They are most often used to configure rolling indices for time series data to
ensure that each new index has the same configuration as the previous one.
The index template associated with a data stream configures its backing indices.
For more information, see Index Templates.

* indices-put-template
* indices-get-template
* indices-delete-template
* indices-component-template
* getting-component-templates
* indices-delete-component-template
* indices-simulate-index
* indices-simulate-template

### Monitoring:

* indices-stats
* field-usage-stats
* indices-segments
* indices-recovery
* indices-shards-stores

### Status management:

* indices-clearcache
* indices-refresh
* indices-flush
* indices-forcemerge

### Dangling indices:

* dangling-indices-list
* dangling-index-import
* dangling-index-delete

(See `indices/alias-exists.md`)
(See `indices/aliases.md`)
(See `indices/analyze.md`)
(See `indices/diskusage.md`)
(See `indices/clearcache.md`)
(See `indices/clone-index.md`)
(See `indices/close.md`)
(See `indices/create-index.md`)
(See `indices/add-alias.md`)
(See `indices/put-component-template.md`)
(See `indices/put-index-template.md`)
(See `indices/put-index-template-v1.md`)
(See `indices/delete-component-template.md`)
(See `indices/dangling-index-delete.md`)
(See `indices/delete-alias.md`)
(See `indices/delete-index.md`)
(See `indices/delete-index-template.md`)
(See `indices/delete-index-template-v1.md`)
(See `indices/indices-exists.md`)
(See `indices/field-usage-stats.md`)
(See `indices/flush.md`)
(See `indices/forcemerge.md`)
(See `indices/get-alias.md`)
(See `indices/get-component-template.md`)
(See `indices/get-field-mapping.md`)
(See `indices/get-index.md`)
(See `indices/get-settings.md`)
(See `indices/get-index-template.md`)
(See `indices/get-index-template-v1.md`)
(See `indices/get-mapping.md`)
(See `indices/dangling-index-import.md`)
(See `indices/recovery.md`)
(See `indices/segments.md`)
(See `indices/shard-stores.md`)
(See `indices/stats.md`)
(See `indices/index-template-exists-v1.md`)
(See `indices/dangling-indices-list.md`)
(See `indices/open-close.md`)
(See `indices/refresh.md`)
(See `indices/resolve.md`)
(See `indices/resolve-cluster.md`)
(See `indices/rollover-index.md`)
(See `indices/shrink-index.md`)
(See `indices/simulate-index.md`)
(See `indices/simulate-template.md`)
(See `indices/split-index.md`)
(See `indices/apis/unfreeze.md`)
(See `indices/update-settings.md`)
(See `indices/put-mapping.md`)
