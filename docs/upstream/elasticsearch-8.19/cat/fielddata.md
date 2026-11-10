<!-- Converted from cat/fielddata.asciidoc (AsciiDoc). Includes are inlined. -->

### cat fielddata API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana 
console. They are _not_ intended for use by applications. For application 
consumption, use the nodes stats API.

Returns the amount of heap memory currently used by the
field data cache on every data node in the cluster.

#### Request

`GET /_cat/fielddata/<field>`

`GET /_cat/fielddata`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Path parameters

`<field>`::
(Optional, string) Comma-separated list of fields used to limit returned
information.

#### Query parameters

`bytes`::
(Optional, byte size units) Unit used to display byte values.
`format`::
(Optional, string) Short version of the
[HTTP accept header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
Valid values include JSON, YAML, etc.
`h`::
(Optional, string) Comma-separated list of column names to display.
`help`::
(Optional, Boolean) If `true`, the response includes help information. Defaults
to `false`.
`s`::
(Optional, string) Comma-separated list of column names or column aliases used
to sort the response.
`v`::
(Optional, Boolean) If `true`, the response includes column headings.
Defaults to `false`.

#### Examples

##### Example with an individual field

You can specify an individual field in the request body or URL path. The
following `fieldata` API request retrieves heap memory size information for the
`body` field.

```console
GET /_cat/fielddata?v=true&fields=body
```

The API returns the following response:

```txt
id                     host      ip        node    field   size
Nqk-6inXQq-OxUfOUI8jNQ 127.0.0.1 127.0.0.1 Nqk-6in body    544b
```

##### Example with a list of fields

You can specify a comma-separated list of fields in the request body or URL
path. The following `fieldata` API request retrieves heap memory size
information for the `body` and `soul` fields.

```console
GET /_cat/fielddata/body,soul?v=true
```

The API returns the following response:

```txt
id                     host      ip        node    field   size
Nqk-6inXQq-OxUfOUI8jNQ 127.0.0.1 127.0.0.1 Nqk-6in body    544b
Nqk-6inXQq-OxUfOUI8jNQ 127.0.0.1 127.0.0.1 Nqk-6in soul    480b
```

The response shows the individual fielddata for the `body` and `soul` fields,
one row per field per node.

##### Example with all fields in a cluster

The following `fieldata` API request retrieves heap memory size
information all fields.

```console
GET /_cat/fielddata?v=true
```

The API returns the following response:

```txt
id                     host      ip        node    field   size
Nqk-6inXQq-OxUfOUI8jNQ 127.0.0.1 127.0.0.1 Nqk-6in body    544b
Nqk-6inXQq-OxUfOUI8jNQ 127.0.0.1 127.0.0.1 Nqk-6in mind    360b
Nqk-6inXQq-OxUfOUI8jNQ 127.0.0.1 127.0.0.1 Nqk-6in soul    480b
```
