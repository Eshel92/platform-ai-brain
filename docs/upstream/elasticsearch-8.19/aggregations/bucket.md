<!-- Converted from aggregations/bucket.asciidoc (AsciiDoc). Includes are inlined. -->

## Bucket aggregations

Bucket aggregations don't calculate metrics over fields like the metrics aggregations do, but instead, they create
buckets of documents. Each bucket is associated with a criterion (depending on the aggregation type) which determines
whether or not a document in the current context "falls" into it. In other words, the buckets effectively define document
sets. In addition to the buckets themselves, the `bucket` aggregations also compute and return the number of documents
that "fell into" each bucket.

Bucket aggregations, as opposed to `metrics` aggregations, can hold sub-aggregations. These sub-aggregations will be
aggregated for the buckets created by their "parent" bucket aggregation.

There are different bucket aggregators, each with a different "bucketing" strategy. Some define a single bucket, some
define fixed number of multiple buckets, and others dynamically create the buckets during the aggregation process.

**Note:** The `search.max_buckets` cluster setting
limits the number of buckets allowed in a single response.

(See `aggregations/bucket/adjacency-matrix-aggregation.md`)
(See `aggregations/bucket/autodatehistogram-aggregation.md`)
(See `aggregations/bucket/categorize-text-aggregation.md`)
(See `aggregations/bucket/children-aggregation.md`)
(See `aggregations/bucket/composite-aggregation.md`)
(See `aggregations/bucket/datehistogram-aggregation.md`)
(See `aggregations/bucket/daterange-aggregation.md`)
(See `aggregations/bucket/diversified-sampler-aggregation.md`)
(See `aggregations/bucket/filter-aggregation.md`)
(See `aggregations/bucket/filters-aggregation.md`)
(See `aggregations/bucket/frequent-item-sets-aggregation.md`)
(See `aggregations/bucket/geodistance-aggregation.md`)
(See `aggregations/bucket/geohashgrid-aggregation.md`)
(See `aggregations/bucket/geohexgrid-aggregation.md`)
(See `aggregations/bucket/geotilegrid-aggregation.md`)
(See `aggregations/bucket/global-aggregation.md`)
(See `aggregations/bucket/histogram-aggregation.md`)
(See `aggregations/bucket/ipprefix-aggregation.md`)
(See `aggregations/bucket/iprange-aggregation.md`)
(See `aggregations/bucket/missing-aggregation.md`)
(See `aggregations/bucket/multi-terms-aggregation.md`)
(See `aggregations/bucket/nested-aggregation.md`)
(See `aggregations/bucket/parent-aggregation.md`)
(See `aggregations/bucket/random-sampler-aggregation.md`)
(See `aggregations/bucket/range-aggregation.md`)
(See `aggregations/bucket/rare-terms-aggregation.md`)
(See `aggregations/bucket/reverse-nested-aggregation.md`)
(See `aggregations/bucket/sampler-aggregation.md`)
(See `aggregations/bucket/significantterms-aggregation.md`)
(See `aggregations/bucket/significanttext-aggregation.md`)
(See `aggregations/bucket/terms-aggregation.md`)
(See `aggregations/bucket/time-series-aggregation.md`)
(See `aggregations/bucket/variablewidthhistogram-aggregation.md`)
(See `aggregations/bucket/range-field-note.md`)
