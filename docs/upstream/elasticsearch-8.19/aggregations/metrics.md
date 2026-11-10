<!-- Converted from aggregations/metrics.asciidoc (AsciiDoc). Includes are inlined. -->

## Metrics aggregations

The aggregations in this family compute metrics based on values extracted in one way or another from the documents that
are being aggregated. The values are typically extracted from the fields of the document (using the field data), but
can also be generated using scripts.

Numeric metrics aggregations are a special type of metrics aggregation which output numeric values. Some aggregations output
a single numeric metric (e.g. `avg`) and are called `single-value numeric metrics aggregation`, others generate multiple
metrics (e.g. `stats`) and are called `multi-value numeric metrics aggregation`. The distinction between single-value and
multi-value numeric metrics aggregations plays a role when these aggregations serve as direct sub-aggregations of some
bucket aggregations (some bucket aggregations enable you to sort the returned buckets based on the numeric metrics in each bucket).

(See `aggregations/metrics/avg-aggregation.md`)
(See `aggregations/metrics/boxplot-aggregation.md`)
(See `aggregations/metrics/cardinality-aggregation.md`)
(See `aggregations/metrics/extendedstats-aggregation.md`)
(See `aggregations/metrics/geobounds-aggregation.md`)
(See `aggregations/metrics/geocentroid-aggregation.md`)
(See `aggregations/metrics/geoline-aggregation.md`)
(See `aggregations/metrics/cartesian-bounds-aggregation.md`)
(See `aggregations/metrics/cartesian-centroid-aggregation.md`)
(See `aggregations/metrics/matrix-stats-aggregation.md`)
(See `aggregations/metrics/max-aggregation.md`)
(See `aggregations/metrics/median-absolute-deviation-aggregation.md`)
(See `aggregations/metrics/min-aggregation.md`)
(See `aggregations/metrics/percentile-rank-aggregation.md`)
(See `aggregations/metrics/percentile-aggregation.md`)
(See `aggregations/metrics/rate-aggregation.md`)
(See `aggregations/metrics/scripted-metric-aggregation.md`)
(See `aggregations/metrics/stats-aggregation.md`)
(See `aggregations/metrics/string-stats-aggregation.md`)
(See `aggregations/metrics/sum-aggregation.md`)
(See `aggregations/metrics/t-test-aggregation.md`)
(See `aggregations/metrics/tophits-aggregation.md`)
(See `aggregations/metrics/top-metrics-aggregation.md`)
(See `aggregations/metrics/valuecount-aggregation.md`)
(See `aggregations/metrics/weighted-avg-aggregation.md`)
