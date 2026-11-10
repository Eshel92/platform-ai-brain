<!-- Converted from repositories-metering-api/apis/clear-repositories-metering-archive.asciidoc (AsciiDoc). Includes are inlined. -->

### Clear repositories metering archive

**New API reference**
For the most up-to-date API details, refer to [Clear the archived repositories metering API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-nodes-clear-repositories-metering-archive).

Removes the archived repositories metering information present in the cluster.

#### Request

`DELETE /_nodes/<node_id>/_repositories_metering/<max_version_to_clear>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.

#### Description

You can use this API to clear the archived repositories metering information in the cluster.

#### Path parameters

`<node_id>`::
(Optional, string) Comma-separated list of node IDs or names used to limit
returned information.
`<max_version_to_clear>`::
    (long) Specifies the maximum archive_version to be cleared from the archive.

All the nodes selective options are explained here.

#### Response body

Returns the deleted archived repositories metering information.

`_nodes`::
(object)
Contains statistics about the number of nodes selected by the request.
**Properties of `_nodes`**
`total`::
(integer)
Total number of nodes selected by the request.

`successful`::
(integer)
Number of nodes that responded successfully to the request.

`failed`::
(integer)
Number of nodes that rejected the request or failed to respond. If this value
is not `0`, a reason for the rejection or failure is included in the response.

`cluster_name`::
(string)
Name of the cluster. Based on the cluster-name setting.

`nodes`::
(object)
Contains repositories metering information for the nodes selected by the request.
**Properties of `nodes`**
`<node_id>`::
(array)
An array of repository metering information for the node.
**Properties of objects in `node_id`**
=====
`repository_name`::
(string)
Repository name.

`repository_type`::
(string)
Repository type.

`repository_location`::
(object)
Represents an unique location within the repository.
**Properties of `repository_location` for repository type `Azure`**
======
`base_path`::
(string)
The path within the container where the repository stores data.

`container`::
(string)
Container name.
======
**Properties of `repository_location` for repository type `GCP`**
======
`base_path`::
(string)
The path within the bucket where the repository stores data.

`bucket`::
(string)
Bucket name.
======
**Properties of `repository_location` for repository type `S3`**
======
`base_path`::
(string)
The path within the bucket where the repository stores data.

`bucket`::
(string)
Bucket name.
======
`repository_ephemeral_id`::
(string)
An identifier that changes every time the repository is updated.

`repository_started_at`::
(long)
Time the repository was created or updated. Recorded in milliseconds
since the [Unix Epoch](https://en.wikipedia.org/wiki/Unix_time).

`repository_stopped_at`::
(Optional, long)
Time the repository was deleted or updated. Recorded in milliseconds
since the [Unix Epoch](https://en.wikipedia.org/wiki/Unix_time).

`archived`::
(Boolean)
A flag that tells whether or not this object has been archived.
When a repository is closed or updated the repository metering information
is archived and kept for a certain period of time. This allows retrieving
the repository metering information of previous repository instantiations.

`cluster_version`::
(Optional, long)
The cluster state version when this object was archived, this field
can be used as a logical timestamp to delete all the archived metrics up
to an observed version. This field is only present for archived
repository metering information objects. The main purpose of this
field is to avoid possible race conditions during repository metering
information deletions, i.e. deleting archived repositories metering
information that we haven't observed yet.

`request_counts`::
(object)
An object with the number of request performed against the repository
grouped by request type.
**Properties of `request_counts` for repository type `Azure`**
======
`GetBlobProperties`::
(long) Number of [Get Blob Properties](https://docs.microsoft.com/en-us/rest/api/storageservices/get-blob-properties) requests.
`GetBlob`::
(long) Number of [Get Blob](https://docs.microsoft.com/en-us/rest/api/storageservices/get-blob) requests.
`ListBlobs`::
(long) Number of [List Blobs](https://docs.microsoft.com/en-us/rest/api/storageservices/list-blobs) requests.
`PutBlob`::
(long) Number of [Put Blob](https://docs.microsoft.com/en-us/rest/api/storageservices/put-blob) requests.
`PutBlock`::
(long) Number of [Put Block](https://docs.microsoft.com/en-us/rest/api/storageservices/put-block).
`PutBlockList`::
(long) Number of [Put Block List](https://docs.microsoft.com/en-us/rest/api/storageservices/put-block-list) requests.

Azure storage [pricing](https://azure.microsoft.com/en-us/pricing/details/storage/blobs/).
======
**Properties of `request_counts` for repository type `GCP`**
======
`GetObject`::
(long) Number of [get object](https://cloud.google.com/storage/docs/json_api/v1/objects/get) requests.
`ListObjects`::
(long) Number of [list objects](https://cloud.google.com/storage/docs/json_api/v1/objects/list) requests.
`InsertObject`::
(long) Number of [insert object](https://cloud.google.com/storage/docs/json_api/v1/objects/insert) requests,
including [simple](https://cloud.google.com/storage/docs/uploading-objects), [multipart](https://cloud.google.com/storage/docs/json_api/v1/how-tos/multipart-upload) and
[resumable](https://cloud.google.com/storage/docs/resumable-uploads) uploads. Resumable uploads can perform multiple http requests to
insert a single object but they are considered as a single request since they are [billed](https://cloud.google.com/storage/docs/resumable-uploads#introduction) as an individual operation.

Google Cloud storage [pricing](https://cloud.google.com/storage/pricing).
======
**Properties of `request_counts` for repository type `S3`**
======
`GetObject`::
(long) Number of [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) requests.
`ListObjects`::
(long) Number of [ListObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html) requests.
`PutObject`::
(long) Number of [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) requests.
`PutMultipartObject`::
(long) Number of [Multipart](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html) requests,
including [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html),
[UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html) and [CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html)
requests.

Amazon Web Services Simple Storage Service [pricing](https://aws.amazon.com/s3/pricing/).
======
=====
