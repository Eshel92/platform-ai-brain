<!-- Converted from user/reporting/reporting-csv-limitations.asciidoc (AsciiDoc). Includes are inlined. -->

We recommend using CSV reports to export moderate amounts of data only. The feature enables analysis of data in external tools, but it is not intended for bulk export or to backup Elasticsearch data. Report timeout and incomplete data issues are likely if you are exporting data where:

- More than 250 MB of data is being exported
- Data is stored on slow storage tiers
- Any shard needed for the search is unavailable
- Network latency between nodes is high
- Cross-cluster search is used
- ES|QL is used and result row count exceeds the limits of ES|QL queries

To work around the limitations, use filters to create multiple smaller reports, or extract the data you need directly with the Elasticsearch APIs.

For more information on using Elasticsearch APIs directly, see [Scroll API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/scroll-api.html), [Point in time API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/point-in-time-api.html), [ES|QL](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/esql-rest.html) or [SQL](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/sql-rest-format.html#_csv) with CSV response data format. We recommend that you use an official Elastic language client: details for each programming language library that Elastic provides are in the [Elasticsearch Client documentation](https://www.elastic.co/guide/en/elasticsearch/client/index.html).

Reporting parameters can be adjusted to overcome some of these limiting scenarios. Results are dependent on data size, availability, and latency factors and are not guaranteed.
