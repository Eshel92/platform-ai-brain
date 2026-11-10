<!-- Converted from docs/multi-termvectors.asciidoc (AsciiDoc). Includes are inlined. -->

### Multi term vectors API

Retrieves multiple term vectors with a single request. 

```console
POST /_mtermvectors
{
   "docs": [
      {
         "_index": "my-index-000001",
         "_id": "2",
         "term_statistics": true
      },
      {
         "_index": "my-index-000001",
         "_id": "1",
         "fields": [
            "message"
         ]
      }
   ]
}
```

#### Request

`POST /_mtermvectors`

`POST /<index>/_mtermvectors`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for the target index or index alias.

#### Description

You can specify existing documents by index and ID or 
provide artificial documents in the body of the request.  
You can specify the index in the request body or request URI.

The response contains a `docs` array with all the fetched termvectors. 
Each element has the structure provided by the termvectors
API. 

See the termvectors API for more information about the information
that can be included in the response.  

#### Path parameters

`<index>`::
(Optional, string) Name of the index that contains the documents.

#### Query parameters

`fields`::
(Optional, string)
Comma-separated list or wildcard expressions of fields
to include in the statistics.

Used as the default list
unless a specific field list is provided
in the `completion_fields` or `fielddata_fields` parameters.
`field_statistics`::
(Optional, Boolean) If `true`, the response includes the document count, sum of document frequencies,
and sum of total term frequencies.
Defaults to `true`.
`<offsets>`::
(Optional, Boolean) If `true`, the response includes term offsets.
Defaults to `true`.
`payloads`::
(Optional, Boolean) If `true`, the response includes term payloads.
Defaults to `true`.
`positions`::
(Optional, Boolean) If `true`, the response includes term positions.
Defaults to `true`.
`preference`::
(Optional, string) Specifies the node or shard the operation should be
performed on. Random by default.
`routing`::
(Optional, string)
Custom value used to route operations to a specific shard.
`realtime`::
(Optional, Boolean) If `true`, the request is real-time as opposed to near-real-time.
Defaults to `true`. See realtime.
`term_statistics`::
(Optional, Boolean) If `true`, the response includes term frequency and document frequency.
Defaults to `false`.
`version`::
(Optional, Boolean) If `true`, returns the document version as part of a hit.
`version_type`::
(Optional, enum) Specific version type: `external`,
`external_gte`.

#### Examples

If you specify an index in the request URI, the index does not need to be specified for each documents
in the request body:

```console
POST /my-index-000001/_mtermvectors
{
   "docs": [
      {
         "_id": "2",
         "fields": [
            "message"
         ],
         "term_statistics": true
      },
      {
         "_id": "1"
      }
   ]
}
```

If all requested documents are in same index and the parameters are the same, you can use the
following simplified syntax:

```console
POST /my-index-000001/_mtermvectors
{
  "ids": [ "1", "2" ],
  "parameters": {
    "fields": [
      "message"
    ],
    "term_statistics": true
  }
}
```

##### Artificial documents

You can also use `mtermvectors` to generate term vectors for _artificial_ documents provided
in the body of the request. The mapping used is determined by the specified `_index`.

```console
POST /_mtermvectors
{
   "docs": [
      {
         "_index": "my-index-000001",
         "doc" : {
            "message" : "test test test"
         }
      },
      {
         "_index": "my-index-000001",
         "doc" : {
           "message" : "Another test ..."
         }
      }
   ]
}
```
