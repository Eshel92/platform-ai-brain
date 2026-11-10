<!-- Converted from upgrade/archive-indices.asciidoc (AsciiDoc). Includes are inlined. -->

## Reading indices from older Elasticsearch versions

Elasticsearch has full query and write support for indices created in the previous major
version. If you have indices created in Elasticsearch versions 5 or 6, you can now use
the archive functionality to import them into newer Elasticsearch versions as well.

The archive functionality provides slower read-only access to older Elasticsearch data,
for compliance or regulatory reasons, the occasional lookback or investigation,
or to rehydrate parts of it. Access to the data is expected to be infrequent,
and can therefore happen with limited performance and query capabilities.

For this, Elasticsearch has the ability to access older snapshot repositories
(going back to version 5). The legacy indices in the snapshot repository
can either be restored, or can be directly accessed
via searchable snapshots so that the archived data
won't even need to fully reside on local disks for access.

### Supported field types

Old mappings are imported as much "as-is" as possible into Elasticsearch 8, but only
provide regular query capabilities on a select subset of fields:

- Numeric types
- `boolean` type
- `ip` type
- `geo_point` type
- `date` types: the date `format` setting on date fields is supported
  as long as it behaves similarly across these versions. In case it is not,
  for example {ref-7x}/migrate-to-java-time.html[when using custom date formats],
  this field can be updated on legacy indices so that it can be changed by a
  user if need be.
- `keyword` type: the `normalizer` setting on keyword
  fields is supported as long as it behaves similarly across these versions.
  In case it is not, this field can be updated on legacy indices if need be.
- `text` type: scoring capabilities are limited, and all
  queries return constant scores that are equal to 1.0. The `analyzer`
  settings on text fields are supported as long as they behave similarly
  across these versions. In case they do not, they can be updated on legacy
  indices if need be.
- Multi-fields
- Field aliases
- `object` fields
- some basic metadata fields, e.g. `_type` for querying Elasticsearch 5 indices
- runtime fields
- `_source` field

Elasticsearch 5 indices with mappings that have {ref-7x}/removal-of-types.html[multiple mapping types]
are collapsed together on a best-effort basis before they are imported.

In case the auto-import of mappings does not work, or the new Elasticsearch version
can't make sense of the mapping, it falls back to importing the index without
the mapping, but stores the original mapping in the _meta
section of the imported index. The legacy mapping can then be introspected
using the GET mapping API and an updated mapping can
be manually put in place using the update mapping API,
copying and adapting relevant sections of the legacy mapping to work with the
current Elasticsearch version. While auto-import is expected to work in most cases,
failures of doing so should be [raised](https://github.com/elastic/elasticsearch/issues/new/choose)
with the Elastic team for future improvements.

### Supported APIs

Archive indices are read-only, and provide data access via the
search and field capabilities APIs.
They do not support the Get API nor any write APIs.

Archive indices allow running queries as well as aggregations in so far as
they are supported by the given field type.

Due to `_source` access the data can also be reindexed
to a new index that has full compatibility with the current Elasticsearch version.

### How to upgrade older Elasticsearch 5 or 6 clusters?

Take a snapshot of the indices in the old cluster, delete indices that are not
directly supported by ES 8 (i.e. indices older than 7.0), upgrade the cluster
without the old indices, and then restore the legacy
indices from the snapshot or mount
them via searchable snapshots.

In the future, we plan on streamlining the upgrade process going forward,
making it easier to take legacy indices along when going to future major
Elasticsearch versions.
