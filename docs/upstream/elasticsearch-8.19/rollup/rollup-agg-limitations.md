<!-- Converted from rollup/rollup-agg-limitations.asciidoc (AsciiDoc). Includes are inlined. -->

### {rollup-cap} aggregation limitations

deprecated::[8.11.0,"Rollups will be removed in a future version. Please migrate to downsampling instead."]

There are some limitations to how fields can be rolled up / aggregated. This page highlights the major limitations so that
you are aware of them.

#### Limited aggregation components

The Rollup functionality allows fields to be grouped with the following aggregations:

- Date Histogram aggregation
- Histogram aggregation
- Terms aggregation

And the following metrics are allowed to be specified for numeric fields:

- Min aggregation
- Max aggregation
- Sum aggregation
- Average aggregation
- Value Count aggregation
