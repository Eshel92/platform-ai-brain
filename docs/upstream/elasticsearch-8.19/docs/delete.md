<!-- Converted from docs/delete.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete API

**New API reference**
For the most up-to-date API details, refer to [Document APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-document).

Removes a JSON document from the specified index.

#### Request

`DELETE /<index>/_doc/<_id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `delete` or
`write` index privilege for the target index or
index alias.

#### Description

You use DELETE to remove a document from an index. You must specify the
index name and document ID.

**Note:** You cannot send deletion requests directly to a data stream. To delete a
document in a data stream, you must target the backing index containing the
document. See update-delete-docs-in-a-backing-index.

##### Optimistic concurrency control

Delete operations can be made conditional and only be performed if the last
modification to the document was assigned the sequence number and primary
term specified by the `if_seq_no` and `if_primary_term` parameters. If a
mismatch is detected, the operation will result in a `VersionConflictException`
and a status code of 409. See optimistic-concurrency-control for more details.

##### Versioning

Each document indexed is versioned. When deleting a document, the `version` can
be specified to make sure the relevant document we are trying to delete is
actually being deleted and it has not changed in the meantime. Every write
operation executed on a document, deletes included, causes its version to be
incremented. The version number of a deleted document remains available for a
short time after deletion to allow for control of concurrent operations. The
length of time for which a deleted document's version remains available is
determined by the `index.gc_deletes` index setting and defaults to 60 seconds.

##### Routing

If routing is used during indexing, the routing value also needs to be
specified to delete a document.

If the `_routing` mapping is set to `required` and no routing value is
specified, the delete API throws a `RoutingMissingException` and rejects
the request.

For example:

```console
DELETE /my-index-000001/_doc/1?routing=shard-1
```

This request deletes the document with id `1`, but it is routed based on the
user. The document is not deleted if the correct routing is not specified.

##### Automatic index creation

If an external versioning variant is used,
the delete operation automatically creates the specified index if it does not
exist. For information about manually creating indices, see
create index API.

##### Distributed

The delete operation gets hashed into a specific shard id. It then gets
redirected into the primary shard within that id group, and replicated
(if needed) to shard replicas within that id group.

##### Wait for active shards

When making delete requests, you can set the `wait_for_active_shards`
parameter to require a minimum number of shard copies to be active
before starting to process the delete request. See
here for further details and a usage
example.

##### Refresh

Control when the changes made by this request are visible to search. See
docs-refresh.

##### Timeout

The primary shard assigned to perform the delete operation might not be
available when the delete operation is executed. Some reasons for this
might be that the primary shard is currently recovering from a store
or undergoing relocation. By default, the delete operation will wait on
the primary shard to become available for up to 1 minute before failing
and responding with an error. The `timeout` parameter can be used to
explicitly specify how long it waits. Here is an example of setting it
to 5 minutes:

```console
DELETE /my-index-000001/_doc/1?timeout=5m
```

#### Path parameters

`<index>`::
(Required, string) Name of the target index.

`<_id>`::
(Required, string) Unique identifier for the document.

#### Query parameters

`if_seq_no`::
(Optional, integer) Only perform the operation if the document has this
sequence number. See optimistic-concurrency-control-index.
`if_primary_term`::
(Optional, integer) Only perform the operation if the document has
this primary term. See optimistic-concurrency-control-index.
`refresh`::
(Optional, enum) If `true`, Elasticsearch refreshes the affected shards to make this
operation visible to search, if `wait_for` then wait for a refresh to make
this operation visible to search, if `false` do nothing with refreshes.
Valid values: `true`, `false`, `wait_for`. Default: `false`.
`routing`::
(Optional, string)
Custom value used to route operations to a specific shard.
`timeout`::
(Optional, time units)
Period to wait for active shards. Defaults to
`1m` (one minute).

`version`::
(Optional, integer) Explicit version number for concurrency control.
The specified version must match the current version of the document for the
request to succeed.
`version_type`::
(Optional, enum) Specific version type: `external`,
`external_gte`.
`wait_for_active_shards`::
(Optional, string) The number of copies of each shard that must be active
before proceeding with the operation. Set to `all` or any non-negative integer
up to the total number of copies of each shard in the index
(`number_of_replicas+1`). Defaults to `1`, meaning to wait just for each
primary shard to be active.

See index-wait-for-active-shards.

#### Examples

Delete the JSON document `1` from the `my-index-000001` index:

```console
DELETE /my-index-000001/_doc/1
```

The API returns the following result:

```console-result
{
  "_shards": {
    "total": 2,
    "failed": 0,
    "successful": 2
  },
  "_index": "my-index-000001",
  "_id": "1",
  "_version": 2,
  "_primary_term": 1,
  "_seq_no": 5,
  "result": "deleted"
}
```
