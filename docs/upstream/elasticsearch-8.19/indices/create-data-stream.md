<!-- Converted from indices/create-data-stream.asciidoc (AsciiDoc). Includes are inlined. -->

### Create data stream API

**New API reference**
For the most up-to-date API details, refer to [Data stream APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-data-stream).

Creates a new data stream.

```console
PUT /_data_stream/my-data-stream
```

#### Request

`PUT /_data_stream/<data-stream>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `create_index`
or `manage` index privilege for the data stream.

* A matching index template with data stream enabled.
See set-up-a-data-stream.

#### Path parameters

`<data-stream>`::
(Required, string) Name of the data stream to create. Data stream names must
meet the following criteria:

- Lowercase only
- Cannot include `\`, `/`, `*`, `?`, `"`, `<`, `>`, `|`, `,`, `#`, `:`, or a
space character
- Cannot start with `-`, `_`, `+`, or `.ds-`
- Cannot be `.` or `..`
- Cannot be longer than 255 bytes. Multi-byte characters
count towards this limit faster.
