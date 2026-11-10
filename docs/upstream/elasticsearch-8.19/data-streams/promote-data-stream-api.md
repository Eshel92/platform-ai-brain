<!-- Converted from data-streams/promote-data-stream-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Promote data stream API

**New API reference**
For the most up-to-date API details, refer to [Data stream APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-data-stream).

The purpose of the promote data stream API is to turn
a data stream that is replicated by CCR into a regular
data stream.

Via CCR Auto Following, a data stream from a remote cluster
can be replicated to the local cluster. These data streams
can't be rolled over in the local cluster. Only if the upstream
data stream rolls over then these replicated data streams roll
over as well. In the event that the remote cluster is no longer
available, the data stream in the local cluster can be promoted
to a regular data stream, which allows these data streams to
be rolled over in the local cluster.

```console
POST /_data_stream/_promote/my-data-stream
```

#### Request

`POST /_data_stream/_promote/<data-stream>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage_follow_index`
cluster privilege to use this API.

#### Path parameters

`<data-stream>`::
(Required, string)
The name of the data stream to promote.
