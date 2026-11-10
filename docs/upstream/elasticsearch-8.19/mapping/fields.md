<!-- Converted from mapping/fields.asciidoc (AsciiDoc). Includes are inlined. -->

## Metadata fields

Each document has metadata associated with it, such as the `_index`
and `_id` metadata fields. The behavior of some of these metadata
fields can be customized when a mapping is created.

### Identity metadata fields

`_index`::

    The index to which the document belongs.

`_id`::

    The document's ID.

### Document source metadata fields

`_source`::

    The original JSON representing the body of the document.

{plugins}/mapper-size.html[`_size`]::

    The size of the `_source` field in bytes, provided by the
    {plugins}/mapper-size.html[`mapper-size` plugin].

### Doc count metadata field

`_doc_count`::

    A custom field used for storing doc counts when a document represents pre-aggregated data.

### Indexing metadata fields

`_field_names`::

    All fields in the document which contain non-null values.

`_ignored`::

    All fields in the document that have been ignored at index time because of
    `ignore_malformed`.

### Routing metadata field

`_routing`::

    A custom routing value which routes a document to a particular shard.

### Other metadata field

`_meta`::

    Application specific metadata.

`_tier`::

    The current data tier preference of the index to which the document belongs.

(See `mapping/fields/doc-count-field.md`)
(See `mapping/fields/field-names-field.md`)
(See `mapping/fields/ignored-field.md`)
(See `mapping/fields/id-field.md`)
(See `mapping/fields/index-field.md`)
(See `mapping/fields/meta-field.md`)
(See `mapping/fields/routing-field.md`)
(See `mapping/fields/source-field.md`)
(See `mapping/fields/tier-field.md`)
