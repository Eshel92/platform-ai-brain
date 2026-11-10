<!-- Converted from docs/multi-get.asciidoc (AsciiDoc). Includes are inlined. -->

### Multi get (mget) API

**New API reference**
For the most up-to-date API details, refer to [Document APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-document).

Retrieves multiple JSON documents by ID. 

```console
GET /_mget
{
  "docs": [
    {
      "_index": "my-index-000001",
      "_id": "1"
    },
    {
      "_index": "my-index-000001",
      "_id": "2"
    }
  ]
}
```

#### Request

`GET /_mget`

`GET /<index>/_mget`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for the target index or index alias.

#### Description

You use `mget` to retrieve multiple documents from one or more indices.
If you specify an index in the request URI, you only need to specify the document IDs in the request body.

##### Security

See api-url-access-control.

##### Partial responses

To ensure fast responses, the multi get API responds with partial results if one or more shards fail. 
See Shard failures for more information.

#### Path parameters

`<index>`::
(Optional, string) Name of the index to retrieve documents from when `ids` are specified,
or when a document in the `docs` array does not specify an index.

#### Query parameters

`preference`::
(Optional, string) Specifies the node or shard the operation should be
performed on. Random by default.
`realtime`::
(Optional, Boolean) If `true`, the request is real-time as opposed to near-real-time.
Defaults to `true`. See realtime.
`refresh`::
(Optional, Boolean) If `true`, the request refreshes relevant shards before
retrieving documents. Defaults to `false`.

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

#### Request body

`docs`::
(Optional, array) The documents you want to retrieve.
Required if no index is specified in the request URI.
You can specify the following attributes for each
document:
`_id`::
(Required, string) The unique document ID.

`_index`::
(Optional, string)
The index that contains the document.
Required if no index is specified in the request URI.

`routing`::
(Optional, string) The key for the primary shard the document resides on.
Required if routing is used during indexing.

`_source`::
(Optional, Boolean) If `false`,  excludes all `_source` fields. Defaults to `true`.
`source_include`:::
(Optional, array) The fields to extract and return from the `_source` field.
`source_exclude`:::
(Optional, array) The fields to exclude from the returned `_source` field.

`_stored_fields`::
(Optional, array) The stored fields you want to retrieve.

`ids`::
(Optional, array) The IDs of the documents you want to retrieve.
Allowed when the index is specified in the request URI.

#### Response body

The response includes a `docs` array that contains the documents in the order specified in the request. 
The structure of the returned documents is similar to that returned by the get API.
If there is a failure getting a particular document, the error is included in place of the document. 

#### Examples

##### Get documents by ID

If you specify an index in the request URI, only the document IDs are required in the request body:

```console
GET /my-index-000001/_mget
{
  "docs": [
    {
      "_id": "1"
    },
    {
      "_id": "2"
    }
  ]
}
```

You can use the `ids` element to simplify the request:

```console
GET /my-index-000001/_mget
{
  "ids" : ["1", "2"]
}
```

##### Filter source fields

By default, the `_source` field is returned for every document (if stored). 
Use the `_source` and `_source_include` or `source_exclude` attributes to 
filter what fields are returned for a particular document.
You can include the `_source`, `_source_includes`, and `_source_excludes` query parameters in the
request URI to specify the defaults to use when there are no per-document instructions.

For example, the following request sets `_source` to false for document 1 to exclude the
source entirely, retrieves `field3` and `field4` from document 2, and retrieves the `user` field
from document 3 but filters out the `user.location` field.

```console
GET /_mget
{
  "docs": [
    {
      "_index": "test",
      "_id": "1",
      "_source": false
    },
    {
      "_index": "test",
      "_id": "2",
      "_source": [ "field3", "field4" ]
    },
    {
      "_index": "test",
      "_id": "3",
      "_source": {
        "include": [ "user" ],
        "exclude": [ "user.location" ]
      }
    }
  ]
}
```

##### Get stored fields

Use the `stored_fields` attribute to specify the set of stored fields you want
to retrieve. Any requested fields that are not stored are ignored. 
You can include the `stored_fields` query parameter in the request URI to specify the defaults 
to use when there are no per-document instructions. 

For example, the following request retrieves `field1` and `field2` from document 1, and
`field3` and `field4` from document 2:

```console
GET /_mget
{
  "docs": [
    {
      "_index": "test",
      "_id": "1",
      "stored_fields": [ "field1", "field2" ]
    },
    {
      "_index": "test",
      "_id": "2",
      "stored_fields": [ "field3", "field4" ]
    }
  ]
}
```

The following request retrieves `field1` and `field2` from all documents by default.
These default fields are returned for document 1, but 
overridden to return `field3` and `field4` for document 2.

```console
GET /test/_mget?stored_fields=field1,field2
{
  "docs": [
    {
      "_id": "1"
    },
    {
      "_id": "2",
      "stored_fields": [ "field3", "field4" ]
    }
  ]
}
```

##### Specify document routing

If routing is used during indexing, you need to specify the routing value to retrieve documents. 
For example, the following request fetches `test/_doc/2`  from the shard corresponding to routing key `key1`,
and fetches `test/_doc/1` from the shard corresponding to routing key `key2`.

```console
GET /_mget?routing=key1
{
  "docs": [
    {
      "_index": "test",
      "_id": "1",
      "routing": "key2"
    },
    {
      "_index": "test",
      "_id": "2"
    }
  ]
}
```
