<!-- Converted from mapping/types.asciidoc (AsciiDoc). Includes are inlined. -->

## Field data types

Each field has a _field data type_, or _field type_. This type indicates the
kind of data the field contains, such as strings or boolean values, and its
intended use. For example, you can index strings to both `text` and `keyword`
fields. However, `text` field values are analyzed for full-text
search while `keyword` strings are left as-is for filtering and sorting.

Field types are grouped by _family_. Types in the same family have exactly the
same search behavior but may have different space usage or performance
characteristics.

Currently, there are two type families, `keyword` and `text`. Other type
families have only a single field type. For example, the `boolean` type family
consists of one field type: `boolean`.

#### Common types

`binary`::   Binary value encoded as a Base64 string.
`boolean`:: `true` and `false` values.
Keywords:: The keyword family, including `keyword`, `constant_keyword`,
                        and `wildcard`.
Numbers::    Numeric types, such as `long` and `double`, used to
                        express amounts.
Dates::                 Date types, including `date` and
                        `date_nanos`.
`alias`::     Defines an alias for an existing field.

#### Objects and relational types

`object`::           A JSON object.
`flattened`::     An entire JSON object as a single field value.
`nested`::           A JSON object that preserves the relationship
                                between its subfields.
`join`::        Defines a parent/child relationship for documents
                                in the same index.
`passthrough`:: Provides aliases for sub-fields at the same level.

#### Structured data types

Range::   Range types, such as `long_range`, `double_range`,
                    `date_range`, and `ip_range`.
`ip`::       IPv4 and IPv6 addresses.
`version`::  Software versions. Supports [Semantic Versioning](https://semver.org/)
precedence rules.
{plugins}/mapper-murmur3.html[`murmur3`]:: Compute and stores hashes of
values.

#### Aggregate data types

`aggregate_metric_double`:: Pre-aggregated metric values.
`histogram`:: Pre-aggregated numerical values in the form of a histogram.

#### Text search types

`text` fields:: The text family, including `text` and `match_only_text`.
                         Analyzed, unstructured text.
{plugins}/mapper-annotated-text.html[`annotated-text`]:: Text containing special
markup. Used for identifying named entities.
`completion`:: Used for auto-complete suggestions.
`search_as_you_type`:: `text`-like type for
as-you-type completion.
`semantic_text`:: Used for performing semantic search.
`token_count`:: A count of tokens in a text.

#### Document ranking types

`dense_vector`::   Records dense vectors of float values.
`sparse_vector`:: Records sparse vectors of float values.
`rank_feature`::   Records a numeric feature to boost hits at
                                    query time.
`rank_features`:: Records numeric features to boost hits at
                                    query time.

#### Spatial data types

`geo_point`::     Latitude and longitude points.
`geo_shape`::     Complex shapes, such as polygons.
`point`::             Arbitrary cartesian points.
`shape`::             Arbitrary cartesian geometries.

#### Other types

`percolator`::   Indexes queries written in Query DSL.

### Arrays

In Elasticsearch, arrays do not require a dedicated field data type. Any field can contain
zero or more values by default, however, all values in the array must be of the
same field type. See array.

### Multi-fields

It is often useful to index the same field in different ways for different
purposes. For instance, a `string` field could be mapped as
a `text` field for full-text search, and as a `keyword` field for
sorting or aggregations. Alternatively, you could index a text field with
the `standard` analyzer, the
`english` analyzer, and the
`french` analyzer.

This is the purpose of _multi-fields_. Most field types support multi-fields
via the multi-fields parameter.

(See `mapping/types/aggregate-metric-double.md`)
(See `mapping/types/alias.md`)
(See `mapping/types/array.md`)
(See `mapping/types/binary.md`)
(See `mapping/types/boolean.md`)
(See `mapping/types/completion.md`)
(See `mapping/types/date.md`)
(See `mapping/types/date_nanos.md`)
(See `mapping/types/dense-vector.md`)
(See `mapping/types/flattened.md`)
(See `mapping/types/geo-point.md`)
(See `mapping/types/geo-shape.md`)
(See `mapping/types/histogram.md`)
(See `mapping/types/ip.md`)
(See `mapping/types/parent-join.md`)
(See `mapping/types/keyword.md`)
(See `mapping/types/nested.md`)
(See `mapping/types/numeric.md`)
(See `mapping/types/object.md`)
(See `mapping/types/passthrough.md`)
(See `mapping/types/percolator.md`)
(See `mapping/types/point.md`)
(See `mapping/types/range.md`)
(See `mapping/types/rank-feature.md`)
(See `mapping/types/rank-features.md`)
(See `mapping/types/rank-vectors.md`)
(See `mapping/types/search-as-you-type.md`)
(See `mapping/types/semantic-text.md`)
(See `mapping/types/shape.md`)
(See `mapping/types/sparse-vector.md`)
(See `mapping/types/text.md`)
(See `mapping/types/token-count.md`)
(See `mapping/types/unsigned_long.md`)
(See `mapping/types/version.md`)
