<!-- Converted from api/upgrade-assistant/reindexing.asciidoc (AsciiDoc). Includes are inlined. -->

### Start or resume reindex API

experimental["The underlying Upgrade Assistant concepts are stable, but the APIs for managing Upgrade Assistant are experimental."]

Start a new reindex or resume a paused reindex. Following steps are performed during 
a reindex task:

. Setting the index to read-only
. Creating a new index
. [Reindexing](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-reindex.html) documents into the new index
. Creating an index alias for the new index
. Deleting the old index

#### Request

`POST <kibana host>:<port>/api/upgrade_assistant/reindex/myIndex`

#### Response code

`200`::
  Indicates a successful call.

#### Example

The API returns the following:

```sh
{
  "indexName": ".ml-state",
  "newIndexName": ".reindexed-v7-ml-state", <1>
  "status": 0, <2>
  "lastCompletedStep": 0, <3>
  "reindexTaskId": null, <4>
  "reindexTaskPercComplete": null, <5>
  "errorMessage": null <6>
}
```

<1> The name of the new index.
<2> The reindex status. For more information, refer to Status codes.
<3> The last successfully completed step of the reindex. For more information, refer to Step codes.
<4> The task ID of the [reindex](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-reindex.html) task in Elasticsearch. Appears when the reindexing starts.
<5> The progress of the [reindexing](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-reindex.html) task in Elasticsearch. Appears in decimal form, from 0 to 1.
<6> The error that caused the reindex to fail, if it failed.
