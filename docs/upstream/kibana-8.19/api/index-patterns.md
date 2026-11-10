<!-- Converted from api/index-patterns.asciidoc (AsciiDoc). Includes are inlined. -->

## Index patterns APIs

deprecated::[8.0.0,Use data-views-api instead.]

experimental[] Manage Kibana index patterns.

**Warning:** Do not write documents directly to the `.kibana` index. When you write directly
to the `.kibana` index, the data becomes corrupted and permanently breaks future Kibana versions.

**Warning:** Use the index patterns API for managing Kibana index patterns instead of lower-level saved objects API.

The following index patterns APIs are available: 

* Index patterns
    ** Get index pattern API to retrieve a single Kibana index pattern
    ** Create index pattern API to create Kibana index pattern
    ** Update index pattern API to partially updated Kibana index pattern
    ** Delete index pattern API to delete Kibana index pattern
* Default index pattern
    ** Get default index pattern API to retrieve a default index pattern
    ** Set default index pattern API to set a default index pattern
* Fields
    ** Update index pattern field to change field metadata, such as `count`, `customLabel` and `format`
* Runtime fields
    ** Get runtime field API to retrieve a runtime field
    ** Create runtime field API to create a runtime field
    ** Upsert runtime field API to create or update a runtime field
    ** Update runtime field API to partially update an existing runtime field
    ** Delete runtime field API to delete a runtime field

(See `api/index-patterns/get.md`)
(See `api/index-patterns/create.md`)
(See `api/index-patterns/update.md`)
(See `api/index-patterns/delete.md`)
(See `api/index-patterns/default-get.md`)
(See `api/index-patterns/default-set.md`)
(See `api/index-patterns/update-fields.md`)
(See `api/index-patterns/runtime-fields/get.md`)
(See `api/index-patterns/runtime-fields/create.md`)
(See `api/index-patterns/runtime-fields/upsert.md`)
(See `api/index-patterns/runtime-fields/update.md`)
(See `api/index-patterns/runtime-fields/delete.md`)
