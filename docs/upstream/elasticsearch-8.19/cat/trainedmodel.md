<!-- Converted from cat/trainedmodel.asciidoc (AsciiDoc). Includes are inlined. -->

### cat trained model API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana 
console. They are _not_ intended for use by applications. For application 
consumption, use the get trained models API.

Returns configuration and usage information about inference trained models.

#### Request

`GET /_cat/ml/trained_models`

#### Prerequisites

If the Elasticsearch security features are enabled, you must have the following 
privileges:

* cluster: `monitor_ml`

For more information, see security-privileges and {ml-docs-setup-privileges}.

#### Query parameters

`bytes`::
(Optional, byte size units) Unit used to display byte values.
`format`::
(Optional, string) Short version of the
[HTTP accept header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
Valid values include JSON, YAML, etc.
`h`::
(Optional, string) Comma-separated list of column names to display.
If you do not specify which columns to include, the API returns the default
columns. If you explicitly specify one or more columns, it returns only the
specified columns.
Valid columns are:

`create_time`, `ct`:::
The time when the trained model was created.

`created_by`, `c`, `createdBy`:::
Information on the creator of the trained model.

`data_frame_analytics_id`, `df`, `dataFrameAnalytics`:::
Identifier for the {dfanalytics-job} that created the model. Only displayed if 
it is still available.

`description`, `d`:::
The description of the trained model.

`heap_size`, `hs`, `modelHeapSize`:::
(Default)
The estimated heap size to keep the trained model in memory.

`id`:::
(Default)
Identifier for the trained model.

`ingest.count`, `ic`, `ingestCount`:::
The total number of documents that are processed by the model.

`ingest.current`, `icurr`, `ingestCurrent`:::
The total number of document that are currently being handled by the trained 
model.

`ingest.failed`, `if`, `ingestFailed`:::
The total number of failed ingest attempts with the trained model.

`ingest.pipelines`, `ip`, `ingestPipelines`:::
(Default)
The total number of ingest pipelines that are referencing the trained model.

`ingest.time`, `it`, `ingestTime`:::
The total time that is spent processing documents with the trained model.

`license`, `l`:::
The license level of the trained model.

`operations`, `o`, `modelOperations`:::
(Default)
The estimated number of operations to use the trained model. This number helps 
measuring the computational complexity of the model.

`version`, `v`:::
The Elasticsearch version number in which the trained model was created.

`help`::
(Optional, Boolean) If `true`, the response includes help information. Defaults
to `false`.
`s`::
(Optional, string) Comma-separated list of column names or column aliases used
to sort the response.
`time`::
(Optional, time units)
Unit used to display time values.
`v`::
(Optional, Boolean) If `true`, the response includes column headings.
Defaults to `false`.

#### Examples

```console
GET _cat/ml/trained_models?h=c,o,l,ct,v&v=ture
```

```console-result
id                           created_by operations license  create_time              version
ddddd-1580216177138              _xpack 196        PLATINUM 2020-01-28T12:56:17.138Z 8.0.0
flight-regress-1580215685537     _xpack 102        PLATINUM 2020-01-28T12:48:05.537Z 8.0.0
lang_ident_model_1               _xpack 39629      BASIC    2019-12-05T12:28:34.594Z 7.6.0
```
