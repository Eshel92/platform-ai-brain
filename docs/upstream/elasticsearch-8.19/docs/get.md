<!-- Converted from docs/get.asciidoc (AsciiDoc). Includes are inlined. -->

### Get API

**New API reference**
For the most up-to-date API details, refer to [Document APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-document).

Retrieves the specified JSON document from an index.

```console
GET my-index-000001/_doc/0
```

#### Request

`GET <index>/_doc/<_id>`

`HEAD <index>/_doc/<_id>`

`GET <index>/_source/<_id>`

`HEAD <index>/_source/<_id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for the target index or index alias.

#### Description

You use GET to retrieve a document and its source or stored fields from a
particular index. Use HEAD to verify that a document exists. You can
use the `_source` resource retrieve just the document source or verify
that it exists.

##### Realtime

By default, the get API is realtime, and is not affected by the refresh
rate of the index (when data will become visible for search). In case where
stored fields are requested (see `stored_fields` parameter) and the document
has been updated but is not yet refreshed, the get API will have to parse
and analyze the source to extract the stored fields. In order to disable
realtime GET, the `realtime` parameter can be set to `false`.

##### Source filtering

By default, the get operation returns the contents of the `_source` field unless
you have used the `stored_fields` parameter or if the `_source` field is disabled.
You can turn off `_source` retrieval by using the `_source` parameter:

```console
GET my-index-000001/_doc/0?_source=false
```

If you only need one or two fields from the `_source`, use the `_source_includes`
or `_source_excludes` parameters to include or filter out particular fields.
This can be especially helpful with large documents where partial retrieval can
save on network overhead. Both parameters take a comma separated list
of fields or wildcard expressions. Example:

```console
GET my-index-000001/_doc/0?_source_includes=*.id&_source_excludes=entities
```

If you only want to specify includes, you can use a shorter notation:

```console
GET my-index-000001/_doc/0?_source=*.id
```

##### Routing

If routing is used during indexing, the routing value also needs to be
specified to retrieve a document. For example:

```console
GET my-index-000001/_doc/2?routing=user1
```

This request gets the document with id `2`, but it is routed based on the
user. The document is not fetched if the correct routing is not specified.

##### Preference

Controls a `preference` of which shard replicas to execute the get
request on. By default, the operation is randomized between the shard
replicas.

The `preference` can be set to:

`_local`::
	The operation will prefer to be executed on a local
	allocated shard if possible.

Custom (string) value::
	A custom value will be used to guarantee that
	the same shards will be used for the same custom value. This can help
	with "jumping values" when hitting different shards in different refresh
	states. A sample value can be something like the web session id, or the
	user name.

##### Refresh

The `refresh` parameter can be set to `true` in order to refresh the
relevant shard before the get operation and make it searchable. Setting
it to `true` should be done after careful thought and verification that
this does not cause a heavy load on the system (and slows down
indexing).

##### Distributed

The get operation gets hashed into a specific shard id. It then gets
redirected to one of the replicas within that shard id and returns the
result. The replicas are the primary shard and its replicas within that
shard id group. This means that the more replicas we have, the
better GET scaling we will have.

##### Versioning support

You can use the `version` parameter to retrieve the document only if
its current version is equal to the specified one.

Internally, Elasticsearch has marked the old document as deleted and added an
entirely new document. The old version of the document doesn’t disappear
immediately, although you won’t be able to access it. Elasticsearch cleans up
deleted documents in the background as you continue to index more data.

#### Path parameters

`<index>`::
(Required, string) Name of the index that contains the document.

`<_id>`::
(Required, string) Unique identifier of the document.

#### Query parameters

`preference`::
(Optional, string) Specifies the node or shard the operation should be
performed on. Random by default.
`realtime`::
(Optional, Boolean) If `true`, the request is real-time as opposed to near-real-time.
Defaults to `true`. See realtime.
`refresh`::
(Optional, Boolean) If `true`, the request refreshes the relevant shard before
retrieving the document. Defaults to `false`.

`routing`::
(Optional, string)
Custom value used to route operations to a specific shard.
`stored_fields`::
(Optional, string)
A comma-separated list of `stored fields` to include in the response.
`_source`::
(Optional, string) True or false to return the `_source` field or not, or a
list of fields to return.
`_source_excludes`::
(Optional, string)
A comma-separated list of source fields to exclude from
the response.
You can also use this parameter to exclude fields from the subset specified in
`_source_includes` query parameter.
If the `_source` parameter is `false`, this parameter is ignored.
`_source_includes`::
(Optional, string)
A comma-separated list of source fields to
include in the response.
If this parameter is specified, only these source fields are returned. You can
exclude fields from this subset using the `_source_excludes` query parameter.
If the `_source` parameter is `false`, this parameter is ignored.
`version`::
(Optional, integer) Explicit version number for concurrency control.
The specified version must match the current version of the document for the
request to succeed.
`version_type`::
(Optional, enum) Specific version type: `external`,
`external_gte`.

#### Response body

`_index`::
The name of the index the document belongs to.

`_id`::
The unique identifier for the document.

`_version`::
The document version. Incremented each time the document is updated.

`_seq_no`::
The sequence number assigned to the document for the indexing
operation. Sequence numbers are used to ensure an older version of a document
doesn’t overwrite a newer version. See optimistic-concurrency-control-index.

`_primary_term`::
The primary term assigned to the document for the indexing operation.
See optimistic-concurrency-control-index.

`found`::
Indicates whether the document exists: `true` or `false`.

`_routing`::
The explicit routing, if set.

'_source'::
If `found` is `true`, contains the document data formatted in JSON.
Excluded if the `_source` parameter is set to `false` or the `stored_fields`
parameter is set to `true`.

'_fields'::
If the `stored_fields` parameter is set to `true` and `found` is
`true`, contains the document fields stored in the index.

#### Examples

Retrieve the JSON document with the `_id` 0 from the `my-index-000001` index:

```console
GET my-index-000001/_doc/0
```

The API returns the following result:

```console-result
{
  "_index": "my-index-000001",
  "_id": "0",
  "_version": 1,
  "_seq_no": 0,
  "_primary_term": 1,
  "found": true,
  "_source": {
    "@timestamp": "2099-11-15T14:12:12",
    "http": {
      "request": {
        "method": "get"
      },
      "response": {
        "status_code": 200,
        "bytes": 1070000
      },
      "version": "1.1"
    },
    "source": {
      "ip": "127.0.0.1"
    },
    "message": "GET /search HTTP/1.1 200 1070000",
    "user": {
      "id": "kimchy"
    }
  }
}
```

Check to see if a document with the `_id` 0 exists:

```console
HEAD my-index-000001/_doc/0
```

Elasticsearch returns a status code of `200 - OK` if the document exists, or
`404 - Not Found` if it doesn't.

##### Get the source field only

Use the `<index>/_source/<id>` resource to get
just the `_source` field of a document. For example:

```console
GET my-index-000001/_source/1
```

You can use the source filtering parameters to control which parts of the
`_source` are returned:

```console
GET my-index-000001/_source/1/?_source_includes=*.id&_source_excludes=entities
```

You can use HEAD with the `_source` endpoint to efficiently
test whether or not the document _source exists. A document's source is not
available if it is disabled in the mapping.

```console
HEAD my-index-000001/_source/1
```

##### Get stored fields

Use the `stored_fields` parameter to specify the set of stored fields you want
to retrieve. Any requested fields that are not stored are ignored.
Consider for instance the following mapping:

```console
PUT my-index-000001
{
   "mappings": {
       "properties": {
          "counter": {
             "type": "integer",
             "store": false
          },
          "tags": {
             "type": "keyword",
             "store": true
          }
       }
   }
}
```

Now we can add a document:

```console
PUT my-index-000001/_doc/1
{
  "counter": 1,
  "tags": [ "production" ]
}
```

And then try to retrieve it:

```console
GET my-index-000001/_doc/1?stored_fields=tags,counter
```

The API returns the following result:

```console-result
{
   "_index": "my-index-000001",
   "_id": "1",
   "_version": 1,
   "_seq_no" : 22,
   "_primary_term" : 1,
   "found": true,
   "fields": {
      "tags": [
         "production"
      ]
   }
}
```

Field values fetched from the document itself are always returned as an array.
Since the `counter` field is not stored, the get request ignores it.

You can also retrieve metadata fields like the `_routing` field:

```console
PUT my-index-000001/_doc/2?routing=user1
{
  "counter" : 1,
  "tags" : ["env2"]
}
```

```console
GET my-index-000001/_doc/2?routing=user1&stored_fields=tags,counter
```

The API returns the following result:

```console-result
{
   "_index": "my-index-000001",
   "_id": "2",
   "_version": 1,
   "_seq_no" : 13,
   "_primary_term" : 1,
   "_routing": "user1",
   "found": true,
   "fields": {
      "tags": [
         "env2"
      ]
   }
}
```

Only leaf fields can be retrieved with the `stored_field` option. Object fields
can't be returned--if specified, the request fails.
