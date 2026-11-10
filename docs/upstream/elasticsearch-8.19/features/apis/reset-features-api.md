<!-- Converted from features/apis/reset-features-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Reset features API

experimental::[]

**New API reference**
For the most up-to-date API details, refer to [Features APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-features).

Clears all of the state information stored in system indices by Elasticsearch features, including the security and machine learning indices.

**Warning:** Intended for development and testing use only. Do not reset features on a production cluster.

```console
POST /_features/_reset
```

#### Request

`POST /_features/_reset`

#### Description

Return a cluster to the same state as a new installation by resetting the feature state for all Elasticsearch features. This deletes all state information stored in system indices.

The response code is `HTTP 200` if state is successfully reset for all features, or `HTTP 500` if the reset operation failed for any feature.

Note that select features might provide a way to reset particular system indices. Using this API resets _all_ features, both those that are built-in and implemented as plugins.

To list the features that will be affected, use the get features API.

**Important:** The features installed on the node you submit this request to are the features that will be reset. Run on the master node if you have any doubts about which plugins are installed on individual nodes.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Examples

Example response:
```console-result
{
  "features" : [
    {
      "feature_name" : "security",
      "status" : "SUCCESS"
    },
    {
      "feature_name" : "tasks",
      "status" : "SUCCESS"
    }
  ]
}
```
