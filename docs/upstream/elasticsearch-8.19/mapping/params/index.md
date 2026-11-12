<!-- Converted from mapping/params/index.asciidoc (AsciiDoc). Includes are inlined. -->

### `index`

The `index` option controls whether field values are indexed. It accepts `true`
or `false` and defaults to `true`. 

Indexing a field creates data structures that enable the field to be queried 
efficiently. Numeric types, date types,
the boolean type, ip type, geo_point type and the
keyword type can also be queried when they are not indexed
 but only have doc values enabled. Queries on these fields are slow as a full scan
 of the index has to be made. All other fields are not queryable.
