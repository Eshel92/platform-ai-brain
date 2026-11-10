<!-- Converted from data-streams/use-a-data-stream.asciidoc (AsciiDoc). Includes are inlined. -->

## Use a data stream

After you set up a data stream, you can do
the following:

* add-documents-to-a-data-stream
* search-a-data-stream
* get-stats-for-a-data-stream
* manually-roll-over-a-data-stream
* open-closed-backing-indices
* reindex-with-a-data-stream
* update-docs-in-a-data-stream-by-query
* delete-docs-in-a-data-stream-by-query
* update-delete-docs-in-a-backing-index

### Add documents to a data stream

To add an individual document, use the index API.
Ingest pipelines are supported.

```console
POST /my-data-stream/_doc/
{
  "@timestamp": "2099-03-08T11:06:07.000Z",
  "user": {
    "id": "8a4f500d"
  },
  "message": "Login successful"
}
```

You cannot add new documents to a data stream using the index API's `PUT
/<target>/_doc/<_id>` request format. To specify a document ID, use the `PUT
/<target>/_create/<_id>` format instead. Only an
`op_type` of `create` is supported.

To add multiple documents with a single request, use the bulk API.
Only `create` actions are supported.

```console
PUT /my-data-stream/_bulk?refresh
{"create":{ }}
{ "@timestamp": "2099-03-08T11:04:05.000Z", "user": { "id": "vlb44hny" }, "message": "Login attempt failed" }
{"create":{ }}
{ "@timestamp": "2099-03-08T11:06:07.000Z", "user": { "id": "8a4f500d" }, "message": "Login successful" }
{"create":{ }}
{ "@timestamp": "2099-03-09T11:07:08.000Z", "user": { "id": "l7gk7f82" }, "message": "Logout successful" }
```

### Search a data stream

The following search APIs support data streams:

* Search
* Async search
* Multi search
* Field capabilities
* EQL search

### Get statistics for a data stream

Use the data stream stats API to get
statistics for one or more data streams:

```console
GET /_data_stream/my-data-stream/_stats?human=true
```

### Manually roll over a data stream

Use the rollover API to manually
roll over a data stream. You have
two options when manually rolling over:

1. To immediately trigger a rollover:
```console
POST /my-data-stream/_rollover/
```
2. Or to postpone the rollover until the next indexing event occurs:
```console
POST /my-data-stream/_rollover?lazy
```
Use the second to avoid having empty backing indices in data streams
that do not get updated often.

### Open closed backing indices

You cannot search a closed backing index, even by searching
its data stream. You also cannot update
or delete documents in a closed index.

To re-open a closed backing index, submit an <<indices-open-close,open
index API request>> directly to the index:

```console
POST /.ds-my-data-stream-2099.03.07-000001/_open/
```

To re-open all closed backing indices for a data stream, submit an open index
API request to the stream:

```console
POST /my-data-stream/_open/
```

### Reindex with a data stream

Use the reindex API to copy documents from an existing index,
alias, or data stream to a data stream. Because data streams are
append-only, a reindex into a data stream must use
an `op_type` of `create`. A reindex cannot update existing documents in a data
stream.

```console
POST /_reindex
{
  "source": {
    "index": "archive"
  },
  "dest": {
    "index": "my-data-stream",
    "op_type": "create"
  }
}
```

### Update documents in a data stream by query

Use the update by query API to update documents in a
data stream that match a provided query:

```console
POST /my-data-stream/_update_by_query
{
  "query": {
    "match": {
      "user.id": "l7gk7f82"
    }
  },
  "script": {
    "source": "ctx._source.user.id = params.new_id",
    "params": {
      "new_id": "XgdX0NoX"
    }
  }
}
```

### Delete documents in a data stream by query

Use the delete by query API to delete documents in a
data stream that match a provided query:

```console
POST /my-data-stream/_delete_by_query
{
  "query": {
    "match": {
      "user.id": "vlb44hny"
    }
  }
}
```

### Update or delete documents in a backing index

If needed, you can update or delete documents in a data stream by sending
requests to the backing index containing the document. You'll need:

* The document ID
* The name of the backing index containing the document
* If updating the document, its <<optimistic-concurrency-control,sequence number
and primary term>>

To get this information, use a search request:

```console
GET /my-data-stream/_search
{
  "seq_no_primary_term": true,
  "query": {
    "match": {
      "user.id": "yWIumJd7"
    }
  }
}
```

Response:

```console-result
{
  "took": 20,
  "timed_out": false,
  "_shards": {
    "total": 3,
    "successful": 3,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 0.2876821,
    "hits": [
      {
        "_index": ".ds-my-data-stream-2099.03.08-000003",      <1>
        "_id": "bfspvnIBr7VVZlfp2lqX",              <2>
        "_seq_no": 0,                               <3>
        "_primary_term": 1,                         <4>
        "_score": 0.2876821,
        "_source": {
          "@timestamp": "2099-03-08T11:06:07.000Z",
          "user": {
            "id": "yWIumJd7"
          },
          "message": "Login successful"
        }
      }
    ]
  }
}
```

<1> Backing index containing the matching document
<2> Document ID for the document
<3> Current sequence number for the document
<4> Primary term for the document

To update the document, use an index API request with valid
`if_seq_no` and `if_primary_term` arguments:

```console
PUT /.ds-my-data-stream-2099-03-08-000003/_doc/bfspvnIBr7VVZlfp2lqX?if_seq_no=0&if_primary_term=1
{
  "@timestamp": "2099-03-08T11:06:07.000Z",
  "user": {
    "id": "8a4f500d"
  },
  "message": "Login successful"
}
```

To delete the document, use the delete API:

```console
DELETE /.ds-my-data-stream-2099.03.08-000003/_doc/bfspvnIBr7VVZlfp2lqX
```

To delete or update multiple documents with a single request, use the
bulk API's `delete`, `index`, and `update` actions. For `index`
actions, include valid <<bulk-optimistic-concurrency-control,`if_seq_no` and
`if_primary_term`>> arguments.

```console
PUT /_bulk?refresh
{ "index": { "_index": ".ds-my-data-stream-2099.03.08-000003", "_id": "bfspvnIBr7VVZlfp2lqX", "if_seq_no": 0, "if_primary_term": 1 } }
{ "@timestamp": "2099-03-08T11:06:07.000Z", "user": { "id": "8a4f500d" }, "message": "Login successful" }
```
