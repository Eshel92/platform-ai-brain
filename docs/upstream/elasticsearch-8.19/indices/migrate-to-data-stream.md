<!-- Converted from indices/migrate-to-data-stream.asciidoc (AsciiDoc). Includes are inlined. -->

### Migrate to data stream API

**New API reference**
For the most up-to-date API details, refer to [Data stream APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-data-stream).

Converts an index alias to a data stream.

```console
POST /_data_stream/_migrate/my-logs
```

#### Request

`POST /_data_stream/_migrate/<alias>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the index alias.

* A matching index template with data stream enabled.
See set-up-a-data-stream.

#### Path parameters

`<alias>`::
(Required, string)
Name of the index alias to convert to a data stream. The alias must meet the
following criteria:

- The alias must have a write index.
- All indices for the alias have a `@timestamp` field mapping of a `date` or `date_nanos` field type.
- The alias must not have any filters.
- The alias must not use custom routing.

If successful, the request removes the alias and creates a data stream with the
same name. The alias's indices become hidden backing indices for the stream. The
alias's write index becomes the stream's write index.
