<!-- Converted from indices/get-field-mapping.asciidoc (AsciiDoc). Includes are inlined. -->

### Get field mapping API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Retrieves mapping definitions for one or more fields. For data
streams, the API retrieves field mappings for the stream's backing indices.

This API is useful if you don't need a complete mapping
or if an index mapping contains a large number of fields.

```console
GET /my-index-000001/_mapping/field/user
```

#### Request

`GET /_mapping/field/<field>`

`GET /<target>/_mapping/field/<field>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`view_index_metadata` or `manage` index privilege
for the target data stream, index, or alias.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases
used to limit the request. Supports wildcards (`*`). To target all data streams
and indices, omit this parameter or use `*` or `_all`.

`<field>`::
(Optional, string) Comma-separated list or wildcard expression of fields used to
limit returned information.

#### Query parameters

`allow_no_indices`::
(Optional, Boolean)
If `false`, the request returns an error if any wildcard expression,
index alias, or `_all` value targets only missing or closed indices.
This behavior applies even if the request targets other open indices. For
example, a request targeting `foo*,bar*` returns an error if an index starts
with `foo` but no index starts with `bar`.
Defaults to `true`.

`expand_wildcards`::
(Optional, string)
Type of index that wildcard patterns can match. If the request can target data
streams, this argument determines whether wildcard expressions match hidden data
streams. Supports comma-separated values, such as `open,hidden`. Valid values
are:

`all`::
Match any data stream or index, including hidden ones.

`open`::
Match open, non-hidden indices. Also matches any non-hidden data stream.

`closed`::
Match closed, non-hidden indices. Also matches any non-hidden data stream. Data
streams cannot be closed.

`hidden`::
Match hidden data streams and hidden indices. Must be combined with `open`,
`closed`, or both.

`none`::
Wildcard patterns are not accepted.
`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`include_defaults`::
(Optional, Boolean) If `true`, the response includes default mapping values.
Defaults to `false`.

#### Examples

##### Example with index setup

You can provide field mappings when creating a new index. The following
create index API request creates the `publications`
index with several field mappings.

```console
PUT /publications
{
  "mappings": {
    "properties": {
      "id": { "type": "text" },
      "title": { "type": "text" },
      "abstract": { "type": "text" },
      "author": {
        "properties": {
          "id": { "type": "text" },
          "name": { "type": "text" }
        }
      }
    }
  }
}
```

The following returns the mapping of the field `title` only:

```console
GET publications/_mapping/field/title
```

The API returns the following response:

```console-result
{
   "publications": {
      "mappings": {
          "title": {
             "full_name": "title",
             "mapping": {
                "title": {
                   "type": "text"
                }
             }
          }
       }
   }
}
```

##### Specifying fields

The get mapping API allows you to specify a comma-separated list of fields.

For instance to select the `id` of the `author` field, you must use its full name `author.id`.

```console
GET publications/_mapping/field/author.id,abstract,name
```

returns:

```console-result
{
   "publications": {
      "mappings": {
        "author.id": {
           "full_name": "author.id",
           "mapping": {
              "id": {
                 "type": "text"
              }
           }
        },
        "abstract": {
           "full_name": "abstract",
           "mapping": {
              "abstract": {
                 "type": "text"
              }
           }
        }
     }
   }
}
```

The get field mapping API also supports wildcard notation.

```console
GET publications/_mapping/field/a*
```

returns:

```console-result
{
   "publications": {
      "mappings": {
         "author.name": {
            "full_name": "author.name",
            "mapping": {
               "name": {
                 "type": "text"
               }
            }
         },
         "abstract": {
            "full_name": "abstract",
            "mapping": {
               "abstract": {
                  "type": "text"
               }
            }
         },
         "author.id": {
            "full_name": "author.id",
            "mapping": {
               "id": {
                  "type": "text"
               }
            }
         }
      }
   }
}
```

##### Multiple targets and fields

The get field mapping API can be used to get mappings for multiple fields from
multiple data streams or indices with a single request.

The `<target>` and `<field>` request path parameters both support
comma-separated lists and wildcard expressions.

You can omit the `<target>` parameter or use a value of `*` or `_all` to target
all data streams and indices in a cluster.

Similarly, you can omit the `<field>` parameter or use a value of `*` to
retrieve mappings for all fields in the targeted data streams or indices.
However, the `<field>` parameter does not support the `_all` value.

For example, the following request retrieves mappings for the `message` field in
any data stream or index named `my-index-000001` or `my-index-000002`.

```console
GET /my-index-000001,my-index-000002/_mapping/field/message
```

The following request retrieves mappings for the `message` and `user.id` fields
in any data stream or index in the cluster.

```console
GET /_all/_mapping/field/message
```

The following request retrieves mappings for fields with an `id` property in any
data stream or index in the cluster.

```console
GET /_all/_mapping/field/*.id
```
