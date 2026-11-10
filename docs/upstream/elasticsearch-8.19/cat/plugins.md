<!-- Converted from cat/plugins.asciidoc (AsciiDoc). Includes are inlined. -->

### cat plugins API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana
console. They are _not_ intended for use by applications. For application
consumption, use the nodes info API.

Returns a list of plugins running on each node of a cluster.

#### Request

`GET /_cat/plugins`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Query parameters

`format`::
(Optional, string) Short version of the
[HTTP accept header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
Valid values include JSON, YAML, etc.
`h`::
(Optional, string) Comma-separated list of column names to display.
`help`::
(Optional, Boolean) If `true`, the response includes help information. Defaults
to `false`.
`local`::
(Optional, Boolean) If `true`, the request retrieves information from the local
node only. Defaults to `false`, which means information is retrieved from
the master node.
`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`s`::
(Optional, string) Comma-separated list of column names or column aliases used
to sort the response.
`v`::
(Optional, Boolean) If `true`, the response includes column headings.
Defaults to `false`.

#### Examples

```console
GET /_cat/plugins?v=true&s=component&h=name,component,version,description
```

The API returns the following response:

```
name    component               version   description
U7321H6 analysis-icu            {version_qualified} The ICU Analysis plugin integrates the Lucene ICU module into Elasticsearch, adding ICU-related analysis components.
U7321H6 analysis-kuromoji       {version_qualified} The Japanese (kuromoji) Analysis plugin integrates Lucene kuromoji analysis module into elasticsearch.
U7321H6 analysis-nori           {version_qualified} The Korean (nori) Analysis plugin integrates Lucene nori analysis module into elasticsearch.
U7321H6 analysis-phonetic       {version_qualified} The Phonetic Analysis plugin integrates phonetic token filter analysis with elasticsearch.
U7321H6 analysis-smartcn        {version_qualified} Smart Chinese Analysis plugin integrates Lucene Smart Chinese analysis module into elasticsearch.
U7321H6 analysis-stempel        {version_qualified} The Stempel (Polish) Analysis plugin integrates Lucene stempel (polish) analysis module into elasticsearch.
U7321H6 analysis-ukrainian      {version_qualified} The Ukrainian Analysis plugin integrates the Lucene UkrainianMorfologikAnalyzer into elasticsearch.
U7321H6 discovery-azure-classic {version_qualified} The Azure Classic Discovery plugin allows to use Azure Classic API for the unicast discovery mechanism
U7321H6 discovery-ec2           {version_qualified} The EC2 discovery plugin allows to use AWS API for the unicast discovery mechanism.
U7321H6 discovery-gce           {version_qualified} The Google Compute Engine (GCE) Discovery plugin allows to use GCE API for the unicast discovery mechanism.
U7321H6 mapper-annotated-text   {version_qualified} The Mapper Annotated_text plugin adds support for text fields with markup used to inject annotation tokens into the index.
U7321H6 mapper-murmur3          {version_qualified} The Mapper Murmur3 plugin allows to compute hashes of a field's values at index-time and to store them in the index.
U7321H6 mapper-size             {version_qualified} The Mapper Size plugin allows document to record their uncompressed size at index time.
U7321H6 store-smb               {version_qualified} The Store SMB plugin adds support for SMB stores.
```
