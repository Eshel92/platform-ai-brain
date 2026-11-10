<!-- Converted from text-structure/apis/find-message-structure.asciidoc (AsciiDoc). Includes are inlined. -->

# Find messages structure API

**New API reference**
For the most up-to-date API details, refer to [Text structure APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-text_structure).

Finds the structure of a list of text messages.

## Request

`GET _text_structure/find_message_structure` +
`POST _text_structure/find_message_structure`

## Prerequisites

* If the Elasticsearch security features are enabled, you must have `monitor_text_structure` or
`monitor` cluster privileges to use this API. See
security-privileges.

## Description

This API provides a starting point for ingesting data into Elasticsearch in a format that
is suitable for subsequent use with other Elastic Stack functionality. Use this
API in preference to `find_structure` when your input text has already been
split up into separate messages by some other process.

The response from the API contains:

* Sample messages.
* Statistics that reveal the most common values for all fields detected within
the text and basic numeric statistics for numeric fields.
* Information about the structure of the text, which is useful when you write
ingest configurations to index it or similarly formatted text.
* Appropriate mappings for an Elasticsearch index, which you could use to ingest the text.

All this information can be calculated by the structure finder with no guidance.
However, you can optionally override some of the decisions about the text
structure by specifying one or more query parameters.

Details of the output can be seen in the examples.

If the structure finder produces unexpected results,
specify the `explain` query parameter and an `explanation` will appear in
the response. It helps determine why the returned structure was
chosen.

## Query parameters

`column_names`::
(Optional, string) If you have set `format` to `delimited`, you can specify the
column names in a comma-separated list. If this parameter is not specified, the
structure finder uses the column names from the header row of the text. If the
text does not have a header row, columns are named "column1", "column2",
"column3", etc.
`delimiter`::
(Optional, string) If you have set `format` to `delimited`, you can specify the
character used to delimit the values in each row. Only a single character is
supported; the delimiter cannot have multiple characters. By default, the API
considers the following possibilities: comma, tab, semi-colon, and pipe (`|`).
In this default scenario, all rows must have the same number of fields for the
delimited format to be detected. If you specify a delimiter, up to 10% of the
rows can have a different number of columns than the first row.
`explain`::
(Optional, Boolean) If `true`, the response includes a
field named `explanation`, which is an array of strings that indicate how the
structure finder produced its result. The default value is `false`.
`format`::
(Optional, string) The high level structure of the text. Valid values are
`ndjson`, `xml`, `delimited`, and `semi_structured_text`. By default, the API
chooses the format. In this default scenario, all rows must have the same number
of fields for a delimited format to be detected. If the `format` is set to
`delimited` and the `delimiter` is not set, however, the API tolerates up to 5%
of rows that have a different number of columns than the first row.
`grok_pattern`::
(Optional, string) If you have set `format` to `semi_structured_text`, you can
specify a Grok pattern that is used to extract fields from every message in the
text. The name of the timestamp field in the Grok pattern must match what is
specified in the `timestamp_field` parameter. If that parameter is not
specified, the name of the timestamp field in the Grok pattern must match
"timestamp". If `grok_pattern` is not specified, the structure finder creates a
Grok pattern.
`ecs_compatibility`::
(Optional, string) The mode of compatibility with ECS compliant Grok patterns.
Use this parameter to specify whether to use ECS Grok patterns instead of
legacy ones when the structure finder creates a Grok pattern. Valid values
are `disabled` and `v1`. The default value is `disabled`. This setting primarily
has an impact when a whole message Grok pattern such as `%{CATALINALOG}`
matches the input. If the structure finder identifies a common structure but
has no idea of meaning then generic field names such as `path`, `ipaddress`,
`field1` and `field2` are used in the `grok_pattern` output, with the intention
that a user who knows the meanings rename these fields before using it.
`quote`::
(Optional, string) If you have set `format` to `delimited`, you can specify the
character used to quote the values in each row if they contain newlines or the
delimiter character. Only a single character is supported. If this parameter is
not specified, the default value is a double quote (`"`). If your delimited text
format does not use quoting, a workaround is to set this argument to a character
that does not appear anywhere in the sample.
`should_trim_fields`::
(Optional, Boolean) If you have set `format` to `delimited`, you can specify
whether values between delimiters should have whitespace trimmed from them. If
this parameter is not specified and the delimiter is pipe (`|`), the default
value is `true`. Otherwise, the default value is `false`.
`timeout`::
(Optional, time units) Sets the maximum amount of time that the
structure analysis may take. If the analysis is still running when the timeout
expires then it will be stopped. The default value is 25 seconds.
`timestamp_field`::
(Optional, string) The name of the field that contains the primary timestamp of
each record in the text. In particular, if the text were ingested into an index,
this is the field that would be used to populate the `@timestamp` field.
If the `format` is `semi_structured_text`, this field must match the name of the
appropriate extraction in the `grok_pattern`. Therefore, for semi-structured
text, it is best not to specify this parameter unless `grok_pattern` is
also specified.

For structured text, if you specify this parameter, the field must exist
within the text.

If this parameter is not specified, the structure finder makes a decision about
which field (if any) is the primary timestamp field. For structured text,
it is not compulsory to have a timestamp in the text.
`timestamp_format`::
(Optional, string) The Java time format of the timestamp field in the text.
Only a subset of Java time format letter groups are supported:

* `a`
* `d`
* `dd`
* `EEE`
* `EEEE`
* `H`
* `HH`
* `h`
* `M`
* `MM`
* `MMM`
* `MMMM`
* `mm`
* `ss`
* `XX`
* `XXX`
* `yy`
* `yyyy`
* `zzz`

Additionally `S` letter groups (fractional seconds) of length one to nine are
supported providing they occur after `ss` and separated from the `ss` by a `.`,
`,` or `:`. Spacing and punctuation is also permitted with the exception of `?`,
newline and carriage return, together with literal text enclosed in single
quotes. For example, `MM/dd HH.mm.ss,SSSSSS 'in' yyyy` is a valid override
format.

One valuable use case for this parameter is when the format is semi-structured
text, there are multiple timestamp formats in the text, and you know which
format corresponds to the primary timestamp, but you do not want to specify the
full `grok_pattern`. Another is when the timestamp format is one that the
structure finder does not consider by default.

If this parameter is not specified, the structure finder chooses the best
format from a built-in set.

If the special value `null` is specified the structure finder will not look
for a primary timestamp in the text. When the format is semi-structured text
this will result in the structure finder treating the text as single-line
messages.

The following table provides the appropriate `timeformat` values for some example timestamps:

|===
| Timeformat                 | Presentation

| yyyy-MM-dd HH:mm:ssZ       | 2019-04-20 13:15:22+0000
| EEE, d MMM yyyy HH:mm:ss Z | Sat, 20 Apr 2019 13:15:22 +0000
| dd.MM.yy HH:mm:ss.SSS      | 20.04.19 13:15:22.285
|===

Refer to
[the Java date/time format documentation](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html)
for more information about date and time format syntax.

## Request body

`messages`::
(Required, array of strings)
The list of messages you want to analyze.

## Examples

### Analyzing Elasticsearch log files

Suppose you have a list of Elasticsearch logs messages.
You can send it to the `find_message_structure` endpoint as follows:

```console
POST _text_structure/find_message_structure
{
  "messages": [
    "[2024-03-05T10:52:36,256][INFO ][o.a.l.u.VectorUtilPanamaProvider] [laptop] Java vector incubator API enabled; uses preferredBitSize=128",
    "[2024-03-05T10:52:41,038][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [repository-url]",
    "[2024-03-05T10:52:41,042][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [rest-root]",
    "[2024-03-05T10:52:41,043][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [x-pack-core]",
    "[2024-03-05T10:52:41,043][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [x-pack-redact]",
    "[2024-03-05T10:52:41,043][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [ingest-user-agent]",
    "[2024-03-05T10:52:41,044][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [x-pack-monitoring]",
    "[2024-03-05T10:52:41,044][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [repository-s3]",
    "[2024-03-05T10:52:41,044][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [x-pack-analytics]",
    "[2024-03-05T10:52:41,044][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [x-pack-ent-search]",
    "[2024-03-05T10:52:41,044][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [x-pack-autoscaling]",
    "[2024-03-05T10:52:41,044][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [lang-painless]]",
    "[2024-03-05T10:52:41,059][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [lang-expression]",
    "[2024-03-05T10:52:41,059][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [x-pack-eql]",
    "[2024-03-05T10:52:43,291][INFO ][o.e.e.NodeEnvironment    ] [laptop] heap size [16gb], compressed ordinary object pointers [true]",
    "[2024-03-05T10:52:46,098][INFO ][o.e.x.s.Security         ] [laptop] Security is enabled",
    "[2024-03-05T10:52:47,227][INFO ][o.e.x.p.ProfilingPlugin  ] [laptop] Profiling is enabled",
    "[2024-03-05T10:52:47,259][INFO ][o.e.x.p.ProfilingPlugin  ] [laptop] profiling index templates will not be installed or reinstalled",
    "[2024-03-05T10:52:47,755][INFO ][o.e.i.r.RecoverySettings ] [laptop] using rate limit [40mb] with [default=40mb, read=0b, write=0b, max=0b]",
    "[2024-03-05T10:52:47,787][INFO ][o.e.d.DiscoveryModule    ] [laptop] using discovery type [multi-node] and seed hosts providers [settings]",
    "[2024-03-05T10:52:49,188][INFO ][o.e.n.Node               ] [laptop] initialized",
    "[2024-03-05T10:52:49,199][INFO ][o.e.n.Node               ] [laptop] starting ..."
  ]
}
```

If the request does not encounter errors, you receive the following result:

```console-result
{
  "num_lines_analyzed" : 22,
  "num_messages_analyzed" : 22,
  "sample_start" : "[2024-03-05T10:52:36,256][INFO ][o.a.l.u.VectorUtilPanamaProvider] [laptop] Java vector incubator API enabled; uses preferredBitSize=128\n[2024-03-05T10:52:41,038][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [repository-url]\n", <3>
  "charset" : "UTF-8",
  "format" : "semi_structured_text",
  "multiline_start_pattern" : "^\\[\\b\\d{4}-\\d{2}-\\d{2}[T ]\\d{2}:\\d{2}",
  "grok_pattern" : "\\[%{TIMESTAMP_ISO8601:timestamp}\\]\\[%{LOGLEVEL:loglevel} \\]\\[.*",
  "ecs_compatibility" : "disabled",
  "timestamp_field" : "timestamp",
  "joda_timestamp_formats" : [
    "ISO8601"
  ],
  "java_timestamp_formats" : [
    "ISO8601"
  ],
  "need_client_timezone" : true,
  "mappings" : {
    "properties" : {
      "@timestamp" : {
        "type" : "date"
      },
      "loglevel" : {
        "type" : "keyword"
      },
      "message" : {
        "type" : "text"
      }
    }
  },
  "ingest_pipeline" : {
    "description" : "Ingest pipeline created by text structure finder",
    "processors" : [
      {
        "grok" : {
          "field" : "message",
          "patterns" : [
            "\\[%{TIMESTAMP_ISO8601:timestamp}\\]\\[%{LOGLEVEL:loglevel} \\]\\[.*"
          ],
          "ecs_compatibility" : "disabled"
        }
      },
      {
        "date" : {
          "field" : "timestamp",
          "timezone" : "{{ event.timezone }}",
          "formats" : [
            "ISO8601"
          ]
        }
      },
      {
        "remove" : {
          "field" : "timestamp"
        }
      }
    ]
  },
  "field_stats" : {
    "loglevel" : {
      "count" : 22,
      "cardinality" : 1,
      "top_hits" : [
        {
          "value" : "INFO",
          "count" : 22
        }
      ]
    },
    "message" : {
      "count" : 22,
      "cardinality" : 22,
      "top_hits" : [
        {
          "value" : "[2024-03-05T10:52:36,256][INFO ][o.a.l.u.VectorUtilPanamaProvider] [laptop] Java vector incubator API enabled; uses preferredBitSize=128",
          "count" : 1
        },
        {
          "value" : "[2024-03-05T10:52:41,038][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [repository-url]",
          "count" : 1
        },
        {
          "value" : "[2024-03-05T10:52:41,042][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [rest-root]",
          "count" : 1
        },
        {
          "value" : "[2024-03-05T10:52:41,043][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [ingest-user-agent]",
          "count" : 1
        },
        {
          "value" : "[2024-03-05T10:52:41,043][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [x-pack-core]",
          "count" : 1
        },
        {
          "value" : "[2024-03-05T10:52:41,043][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [x-pack-redact]",
          "count" : 1
        },
        {
          "value" : "[2024-03-05T10:52:41,044][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [lang-painless]]",
          "count" : 1
        },
        {
          "value" : "[2024-03-05T10:52:41,044][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [repository-s3]",
          "count" : 1
        },
        {
          "value" : "[2024-03-05T10:52:41,044][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [x-pack-analytics]",
          "count" : 1
        },
        {
          "value" : "[2024-03-05T10:52:41,044][INFO ][o.e.p.PluginsService     ] [laptop] loaded module [x-pack-autoscaling]",
          "count" : 1
        }
      ]
    },
    "timestamp" : {
      "count" : 22,
      "cardinality" : 14,
      "earliest" : "2024-03-05T10:52:36,256",
      "latest" : "2024-03-05T10:52:49,199",
      "top_hits" : [
        {
          "value" : "2024-03-05T10:52:41,044",
          "count" : 6
        },
        {
          "value" : "2024-03-05T10:52:41,043",
          "count" : 3
        },
        {
          "value" : "2024-03-05T10:52:41,059",
          "count" : 2
        },
        {
          "value" : "2024-03-05T10:52:36,256",
          "count" : 1
        },
        {
          "value" : "2024-03-05T10:52:41,038",
          "count" : 1
        },
        {
          "value" : "2024-03-05T10:52:41,042",
          "count" : 1
        },
        {
          "value" : "2024-03-05T10:52:43,291",
          "count" : 1
        },
        {
          "value" : "2024-03-05T10:52:46,098",
          "count" : 1
        },
        {
          "value" : "2024-03-05T10:52:47,227",
          "count" : 1
        },
        {
          "value" : "2024-03-05T10:52:47,259",
          "count" : 1
        }
      ]
    }
  }
}
```

For a detailed description of the response format, or for additional examples
on ingesting delimited text (such as CSV) or newline-delimited JSON, refer to the
examples of the find text structure endpoint.
