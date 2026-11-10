<!-- Converted from ingest/processors.asciidoc (AsciiDoc). Includes are inlined. -->

## Ingest processor reference

An ingest pipeline is made up of a sequence of processors that are applied to documents as they are ingested into an index.
Each processor performs a specific task, such as filtering, transforming, or enriching data.

Each successive processor depends on the output of the previous processor, so the order of processors is important.
The modified documents are indexed into Elasticsearch after all processors are applied.

Elasticsearch includes over 40 configurable processors.
The subpages in this section contain reference documentation for each processor.
To get a list of available
processors, use the nodes info API.

```console
GET _nodes/ingest?filter_path=nodes.*.ingest.processors
```

### Ingest processors by category

We've categorized the available processors on this page and summarized their functions.
This will help you find the right processor for your use case.

* ingest-process-category-data-enrichment
* ingest-process-category-data-transformation
* ingest-process-category-data-filtering
* ingest-process-category-pipeline-handling
* ingest-process-category-array-json-handling

### Data enrichment processors

#### General outcomes

`append` processor::
Appends a value to a field.

`date_index_name` processor::
Points documents to the right time-based index based on a date or timestamp field.

`enrich` processor::
Enriches documents with data from another index.

**Tip:**
Refer to Enrich your data for detailed examples of how to use the `enrich` processor to add data from your existing indices to incoming documents during ingest.

`inference` processor::
Uses machine learning to classify and tag text fields.

#### Specific outcomes

`attachment` processor::
Parses and indexes binary data, such as PDFs and Word documents.

`circle` processor::
Converts a location field to a Geo-Point field.

`community_id` processor::
Computes the Community ID for network flow data.

`fingerprint` processor::
Computes a hash of the document’s content.

`geo_grid` processor::
Converts geo-grid definitions of grid tiles or cells to regular bounding boxes or polygons which describe their shape.

`geoip` processor::
Adds information about the geographical location of an IPv4 or IPv6 address from a Maxmind database.

`ip_location` processor::
Adds information about the geographical location of an IPv4 or IPv6 address from an ip geolocation database.

`network_direction` processor::
Calculates the network direction given a source IP address, destination IP address, and a list of internal networks.

`normalize_for_stream` processor::
Normalizes non-OpenTelemetry documents to be OpenTelemetry-compliant.

`registered_domain` processor::
Extracts the registered domain (also known as the effective top-level domain or eTLD), sub-domain, and top-level domain from a fully qualified domain name (FQDN).

`set_security_user` processor::
Sets user-related details (such as `username`,  `roles`, `email`, `full_name`,`metadata`, `api_key`, `realm` and `authentication_type`) from the current authenticated user.

`uri_parts` processor::
Parses a Uniform Resource Identifier (URI) string and extracts its components as an object.

`urldecode` processor::
URL-decodes a string.

`user_agent` processor::
Parses user-agent strings to extract information about web clients.

### Data transformation processors

#### General outcomes

`convert` processor::
Converts a field in the currently ingested document to a different type, such as converting a string to an integer.

`dissect` processor::
Extracts structured fields out of a single text field within a document.
Unlike the grok processor, dissect does not use regular expressions.
This makes the dissect's a simpler and often faster alternative.

`grok` processor::
Extracts structured fields out of a single text field within a document, using the Grok regular expression dialect that supports reusable aliased expressions.

`gsub` processor::
Converts a string field by applying a regular expression and a replacement.

`redact` processor::
Uses the Grok rules engine to obscure text in the input document matching the given Grok patterns.

`rename` processor::
Renames an existing field.

`set` processor::
Sets a value on a field.

#### Specific outcomes

`bytes` processor::
Converts a human-readable byte value to its value in bytes (for example `1kb` becomes `1024`).

`csv` processor::
Extracts a single line of CSV data from a text field.

`date` processor::
Extracts and converts date fields.

`dot_expand` processor::
Expands a field with dots into an object field.

`html_strip` processor::
Removes HTML tags from a field.

`join` processor::
Joins each element of an array into a single string using a separator character between each element.

`kv` processor::
Parse messages (or specific event fields) containing key-value pairs.

`lowercase` processor and `uppercase` processor::
Converts a string field to lowercase or uppercase.

`split` processor::
Splits a field into an array of values.

`trim` processor::
Trims whitespace from field. 

### Data filtering processors

`drop` processor::
Drops the document without raising any errors.

`remove` processor::
Removes fields from documents.

### Pipeline handling processors

`fail` processor::
Raises an exception. Useful for when you expect a pipeline to fail and want to relay a specific message to the requester.

`pipeline` processor::
Executes another pipeline.

`reroute` processor::
Reroutes documents to another target index or data stream.

`terminate` processor::
Terminates the current ingest pipeline, causing no further processors to be run.

### Array/JSON handling processors

`for_each` processor::
Runs an ingest processor on each element of an array or object.

`json` processor::
Converts a JSON string into a structured JSON object.

`script` processor::
Runs an inline or stored script on incoming documents.
The script runs in the {painless}/painless-ingest-processor-context.html[painless `ingest` context].

`sort` processor::
Sorts the elements of an array in ascending or descending order.

### Add additional processors

You can install additional processors as {plugins}/ingest.html[plugins].

You must install any plugin processors on all nodes in your cluster. Otherwise,
Elasticsearch will fail to create pipelines containing the processor.

Mark a plugin as mandatory by setting `plugin.mandatory` in
`elasticsearch.yml`. A node will fail to start if a mandatory plugin is not
installed.

```yaml
plugin.mandatory: my-ingest-plugin
```

(See `ingest/processors/append.md`)
(See `ingest/processors/attachment.md`)
(See `ingest/processors/bytes.md`)
(See `ingest/processors/circle.md`)
(See `ingest/processors/community-id.md`)
(See `ingest/processors/convert.md`)
(See `ingest/processors/csv.md`)
(See `ingest/processors/date.md`)
(See `ingest/processors/date-index-name.md`)
(See `ingest/processors/dissect.md`)
(See `ingest/processors/dot-expand.md`)
(See `ingest/processors/drop.md`)
(See `ingest/processors/enrich.md`)
(See `ingest/processors/fail.md`)
(See `ingest/processors/fingerprint.md`)
(See `ingest/processors/foreach.md`)
(See `ingest/processors/geo-grid.md`)
(See `ingest/processors/geoip.md`)
(See `ingest/processors/grok.md`)
(See `ingest/processors/gsub.md`)
(See `ingest/processors/html_strip.md`)
(See `ingest/processors/inference.md`)
(See `ingest/processors/ip-location.md`)
(See `ingest/processors/join.md`)
(See `ingest/processors/json.md`)
(See `ingest/processors/kv.md`)
(See `ingest/processors/lowercase.md`)
(See `ingest/processors/network-direction.md`)
(See `ingest/processors/normalize-for-stream.md`)
(See `ingest/processors/pipeline.md`)
(See `ingest/processors/redact.md`)
(See `ingest/processors/registered-domain.md`)
(See `ingest/processors/remove.md`)
(See `ingest/processors/rename.md`)
(See `ingest/processors/reroute.md`)
(See `ingest/processors/script.md`)
(See `ingest/processors/set.md`)
(See `ingest/processors/set-security-user.md`)
(See `ingest/processors/sort.md`)
(See `ingest/processors/split.md`)
(See `ingest/processors/terminate.md`)
(See `ingest/processors/trim.md`)
(See `ingest/processors/uppercase.md`)
(See `ingest/processors/url-decode.md`)
(See `ingest/processors/uri-parts.md`)
(See `ingest/processors/user-agent.md`)
