<!-- Converted from indices/put-mapping.asciidoc (AsciiDoc). Includes are inlined. -->

### Update mapping API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

You can use this API to:

* Add new fields to an existing index
* Change the search settings of existing fields

**Note:** Elasticsearch does not allow in-place field type changes. If you need to change a field’s type, you must create a new index with the updated mapping and reindex the data. 

For data streams, these changes are applied to all backing indices by default.

```console
PUT /my-index-000001/_mapping
{
  "properties": {
    "email": {
      "type": "keyword"
    }
  }
}
```

#### Request

`PUT /<target>/_mapping`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the target data stream, index,
or alias.
deprecated:[7.9] If the request targets an index or index alias, you can also
update its mapping with the `create`, `create_doc`, `index`, or `write` index
privilege.

#### Path parameters

`<target>`::
(Required, string) Comma-separated list of data streams, indices, and aliases
used to limit the request. Supports wildcards (`*`). To target all data streams
and indices, omit this parameter or use `*` or `_all`.

#### Query parameters

`allow_no_indices`::
(Optional, Boolean)
If `false`, the request returns an error if any wildcard expression,
index alias, or `_all` value targets only missing or closed indices.
This behavior applies even if the request targets other open indices. For
example, a request targeting `foo*,bar*` returns an error if an index starts
with `foo` but no index starts with `bar`.
Defaults to `false`.

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
Defaults to `open`.

`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

`timeout`::
(Optional, time units) Period to wait for a response from all relevant nodes in the cluster after updating the cluster metadata.
If no response is received before the timeout expires, the cluster metadata update still applies but the response will indicate that it was not completely acknowledged.
Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`write_index_only`::
(Optional, Boolean)
If `true`,
the mappings are applied only to the current write index for the target.
Defaults to `false`.

#### Request body

`properties`::
(Required, mapping object) Mapping for a field. For new
fields, this mapping can include:

* Field name
* Field data type
* Mapping parameters

For existing fields, see updating-field-mappings.

#### Examples

##### Example with single target

The update mapping API requires an existing data stream or index. The following
create index API request creates the `publications`
index with no mapping.

```console
PUT /publications
```

The following update mapping API request adds `title`, a new `text` field,
to the `publications` index.

```console
PUT /publications/_mapping
{
  "properties": {
    "title":  { "type": "text"}
  }
}
```

##### Multiple targets

The update mapping API can be applied to multiple data streams or indices with a single request.
For example, you can update mappings for the `my-index-000001` and `my-index-000002` indices at the same time:

```console
# Create the two indices
PUT /my-index-000001
PUT /my-index-000002

# Update both mappings
PUT /my-index-000001,my-index-000002/_mapping
{
  "properties": {
    "user": {
      "properties": {
        "name": {
          "type": "keyword"
        }
      }
    }
  }
}
```

##### Add new properties to an existing object field

You can use the update mapping API to add new properties to an existing
`object` field. To see how this works, try the following example.

Use the create index API to create an index with the
`name` object field and an inner `first` text field.

```console
PUT /my-index-000001
{
  "mappings": {
    "properties": {
      "name": {
        "properties": {
          "first": {
            "type": "text"
          }
        }
      }
    }
  }
}
```

Use the update mapping API to add a new inner `last` text field to the `name`
field.

```console
PUT /my-index-000001/_mapping
{
  "properties": {
    "name": {
      "properties": {
        "last": {
          "type": "text"
        }
      }
    }
  }
}
```

##### Add multi-fields to an existing field

Multi-fields let you index the same field in different ways.
You can use the update mapping API to update the `fields` mapping parameter and
enable multi-fields for an existing field.

**Warning:** If an index (or data stream) contains documents when you add a
multi-field, those documents will not have values for the new multi-field. You
can populate the new multi-field with the <<picking-up-a-new-property,update by
query API>>.

To see how this works, try the following example.

Use the create index API to create an index with the
`city` text field.

```console
PUT /my-index-000001
{
  "mappings": {
    "properties": {
      "city": {
        "type": "text"
      }
    }
  }
}
```

While text fields work well for full-text search, keyword fields are
not analyzed and may work better for sorting or aggregations.

Use the update mapping API to enable a multi-field for the `city` field. This
request adds the `city.raw` keyword multi-field, which can be used for sorting.

```console
PUT /my-index-000001/_mapping
{
  "properties": {
    "city": {
      "type": "text",
      "fields": {
        "raw": {
          "type": "keyword"
        }
      }
    }
  }
}
```

##### Change supported mapping parameters for an existing field

The documentation for each mapping parameter indicates
whether you can update it for an existing field using the update mapping API. For
example, you can use the update mapping API to update the
`ignore_above` parameter.

To see how this works, try the following example.

Use the create index API to create an index containing
a `user_id` keyword field. The `user_id` field has an `ignore_above` parameter
value of `20`.

```console
PUT /my-index-000001
{
  "mappings": {
    "properties": {
      "user_id": {
        "type": "keyword",
        "ignore_above": 20
      }
    }
  }
}
```

Use the update mapping API to change the `ignore_above` parameter value to `100`.

```console
PUT /my-index-000001/_mapping
{
  "properties": {
    "user_id": {
      "type": "keyword",
      "ignore_above": 100
    }
  }
}
```

##### Change the mapping of an existing field

Except for supported mapping parameters,
you can't change the mapping or field type of an existing field.
Changing an existing field could invalidate data that's already indexed.

If you need to change the mapping of a field in a data stream's backing indices,
see data-streams-change-mappings-and-settings.

If you need to change the mapping of a field in other indices,
create a new index with the correct mapping
and reindex your data into that index.

To see how you can change the mapping of an existing field in an index,
try the following example.

Use the create index API
to create an index
with the `user_id` field
with the `long` field type.

```console
PUT /my-index-000001
{
  "mappings" : {
    "properties": {
      "user_id": {
        "type": "long"
      }
    }
  }
}
```

Use the index API
to index several documents
with `user_id` field values.

```console
POST /my-index-000001/_doc?refresh=wait_for
{
  "user_id" : 12345
}

POST /my-index-000001/_doc?refresh=wait_for
{
  "user_id" : 12346
}
```

To change the `user_id` field
to the `keyword` field type,
use the create index API
to create a new index with the correct mapping.

```console
PUT /my-new-index-000001
{
  "mappings" : {
    "properties": {
      "user_id": {
        "type": "keyword"
      }
    }
  }
}
```

Use the reindex API
to copy documents from the old index
to the new one.

```console
POST /_reindex
{
  "source": {
    "index": "my-index-000001"
  },
  "dest": {
    "index": "my-new-index-000001"
  }
}
```

##### Rename a field

Renaming a field would invalidate data already indexed under the old field name.
Instead, add an `alias` field to create an alternate field name.

For example,
use the create index API
to create an index
with the `user_identifier` field.

```console
PUT /my-index-000001
{
  "mappings": {
    "properties": {
      "user_identifier": {
        "type": "keyword"
      }
    }
  }
}
```

Use the update mapping API to add the `user_id` field alias
for the existing `user_identifier` field.

```console
PUT /my-index-000001/_mapping
{
  "properties": {
    "user_id": {
      "type": "alias",
      "path": "user_identifier"
    }
  }
}
```
