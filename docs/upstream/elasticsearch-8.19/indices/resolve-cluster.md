<!-- Converted from indices/resolve-cluster.asciidoc (AsciiDoc). Includes are inlined. -->

### Resolve cluster API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Resolves the specified index expressions to return information about
each cluster, including the local "querying" cluster, if included. If no index expression
is provided, this endpoint will return information about all the remote
clusters that are configured on the querying cluster.

This endpoint is useful before doing a cross-cluster search in
order to determine which remote clusters should be included in a search.

You use the same index expression with this endpoint as you would for cross-cluster
search. Index and cluster exclusions are also supported
with this endpoint.

For each cluster in scope, information is returned about:

1. whether the querying ("local") cluster was able to connect to each remote cluster
   specified in the index expression. Note that this endpoint actively attempts to
   contact the remote clusters, unlike the remote/info endpoint.
2. whether each remote cluster is configured with `skip_unavailable` as `true` or `false`
3. whether there are any indices, aliases or data streams on that cluster that match
   the index expression (if one provided)
4. whether the search is likely to have errors returned when you do a cross-cluster search (including any
   authorization errors if your user does not have permission to query a remote cluster or
   the indices on that cluster)
5. (in some cases) cluster version information, including the Elasticsearch server version

**Tip:**
Whenever a security exception is returned for a remote cluster, that remote
will always be marked as connected=false in the response, since your user does not have
permissions to access that cluster (or perhaps the remote index) you are querying.
Once the proper security permissions are obtained, then you can rely on the `connected` field
in the response to determine whether the remote cluster is available and ready for querying.

**Note:** The ability to query without an index expression was added in 8.18, so when
querying remote clusters older than that, the local cluster will send the index
expression `dummy*` to those remote clusters. Thus, if an errors occur, you may see a reference
to that index expression even though you didn't request it. If it causes a problem, you can
instead include an index expression like `*:*` to bypass the issue.

```console
GET /_resolve/cluster
```

Returns information about all remote clusters configured on the local cluster
without doing any index matching.

```console
GET /_resolve/cluster/my-index-*,cluster*:my-index-*
```

Returns information about the local cluster and all remote clusters that
start with the alias `cluster*`. Each cluster will return information
about whether it has any indices, aliases or data streams that match `my-index-*`.

#### Request

`GET /_resolve/cluster`

or

`GET /_resolve/cluster/<index_expression>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`view_index_metadata`, `read`, or `manage` <<privileges-list-indices,index
privilege>> for the target data stream, index, or alias.

#### Path parameters

`<index_expression>`::
(Optional, string) Comma-separated name(s) or index pattern(s) of the
indices, aliases, and data streams to resolve, using api-multi-index.
Resources on remote clusters can be specified using the
`<cluster>:<name>` syntax.

#### Query parameters

`timeout`::
(Optional, TimeValue) Specify a max wait time for remote clusters to respond.
If a remote cluster does not respond within this timeout period, the API response
will show the cluster as not connected and include an error message that the
request timed out. The default timeout is unset and the query can take
as long as the networking layer is configured to wait for remote clusters that are
not responding (typically 30 seconds).

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
Defaults to `false`.

`allow_no_indices`::
(Optional, Boolean)
If `false`, the request returns an error if any wildcard expression,
index alias, or `_all` value targets only missing or closed indices.
This behavior applies even if the request targets other open indices. For
example, a request targeting `foo*,bar*` returns an error if an index starts
with `foo` but no index starts with `bar`.
Defaults to `true`.

`ignore_throttled`::
(Optional, Boolean) If `true`, concrete, expanded or aliased indices are
ignored when frozen. Defaults to `false`.
deprecated:[7.16.0]

**Tip:**
The index options above are only allowed when specifying an index expression.
You will get an error if you specify index options to the _resolve/cluster API
that takes no index expression.

### Test availability of remote clusters

The remote/info endpoint is commonly used to test whether the "local"
cluster (the cluster being queried) is connected to its remote clusters, but it does not
necessarily reflect whether the remote cluster is available or not. The remote cluster may
be available, while the local cluster is not currently connected to it.

You can use the resolve-cluster API to attempt to reconnect to remote clusters
(for example with `GET _resolve/cluster` or `GET _resolve/cluster/*:*` ).
The `connected` field in the response will indicate whether it was successful.
If a connection was (re-)established, this will also cause the
remote/info endpoint to now indicate a connected status.

### Advantages of using this endpoint before a cross-cluster search

You may want to exclude a cluster or index from a search when:

1. A remote cluster could not be connected to and is configured with `skip_unavailable`=`false`.
Executing a cross-cluster search under those conditions will cause
the entire search to fail.

2. A cluster has no matching indices, aliases or data streams for the index expression
(or your user does not have permissions to search them). For example, suppose your
index expression is `logs*,remote1:logs*` and the `remote1` cluster has no indices, aliases or data
streams that match `logs*`. In that case, that cluster will return no results from that cluster if
you include it in a cross-cluster search.

3. The index expression (combined with any query parameters you specify) will likely cause an exception
to be thrown when you do the search. In these cases, the "error" field in the `_resolve/cluster` response
will be present. (This is also where security/permission errors will be shown.)

4. A remote cluster is an older version that does not support the feature you want to
use in your search.

#### Examples

```console
GET /_resolve/cluster/my-index*,clust*:my-index*
```

The API returns the following response:

```console-result
{
  "(local)": {          <1>
    "connected": true,
    "skip_unavailable": false,
    "matching_indices": true,
    "version": {
      "number": "8.13.0",
      "build_flavor": "default",
      "minimum_wire_compatibility_version": "7.17.0",
      "minimum_index_compatibility_version": "7.0.0"
    }
  },
  "cluster_one": {
    "connected": true,         <2>
    "skip_unavailable": true,  <3>
    "matching_indices": true,  <4>
    "version": {
      "number": "8.13.0",      <5>
      "build_flavor": "default",
      "minimum_wire_compatibility_version": "7.17.0",
      "minimum_index_compatibility_version": "7.0.0"
    }
  },
  "cluster_two": {
    "connected": true,
    "skip_unavailable": false,
    "matching_indices": true,
    "version": {
      "number": "8.13.0",
      "build_flavor": "default",
      "minimum_wire_compatibility_version": "7.17.0",
      "minimum_index_compatibility_version": "7.0.0"
    }
  }
}
```

<1> Each cluster has its own response section. The cluster you sent the request to is labelled as "(local)".
<2> The querying cluster attempts to make a request to each remote cluster. If successful, `connected`=`true`.
<3> The `skip_unavailable` setting for each remote cluster, as configured on the local cluster.
<4> Indicates whether any index, alias or data stream matches the index expression specified for that cluster.
<5> The Elasticsearch server version.

#### Identifying potential problems with your cross-cluster search

The following request shows several examples of how modifying your query can
prevent search failures. Note also that a `timeout` of 5 seconds is sent, which
sets the maximum time the query will wait for remote clusters to respond.

```console
GET /_resolve/cluster/not-present,clust*:my-index*,oldcluster:*?ignore_unavailable=false&timeout=5s
```

```console-result
{
  "(local)": {
    "connected": true,
    "skip_unavailable": false,
    "error": "no such index [not_present]"  <1>
  },
  "cluster_one": {
    "connected": true,
    "skip_unavailable": true,
    "matching_indices": false,    <2>
    "version": {
      "number": "8.13.0",
      "build_flavor": "default",
      "minimum_wire_compatibility_version": "7.17.0",
      "minimum_index_compatibility_version": "7.0.0"
    }
  },
  "cluster_two": {
    "connected": false,           <3>
    "skip_unavailable": false
  },
  "cluster_three": {
    "connected": false,
    "skip_unavailable": false,
    "error": "Request timed out before receiving a response from the remote cluster"  <4>
  },
  "oldcluster": {         <5>
    "connected": true,
    "skip_unavailable": false,
    "matching_indices": true
  }
}
```

<1> The local cluster has no index called `not_present`. Searching against it
using the specified `ignore_unavailable=false` param will return a "no such
index" error. Other types of errors can show up here as well, such as security
permission errors when the user does not have authorization to search the
specified index.
<2> The `cluster_one` remote cluster has no indices that match the pattern
`my-index*`. There may be no indices that match the pattern or the index
could be closed. (You can check this by using the
resolve index API.)
<3> The `cluster_two` remote cluster is not connected (the attempt to connect
failed). Since this cluster is marked as `skip_unavailable=false`, you should
probably exclude this cluster from the search by adding `-cluster_two:*` to the
search index expression.
<4> For `cluster_three`, the error message indicates that this remote cluster did
not respond within the 5-second timeout window specified, so it is also marked as
not connected.
<5> The `oldcluster` remote cluster shows that it has matching indices, but no
version information is included. This indicates that the cluster version predates
the introduction of the `_resolve/cluster` API in 8.13.0., so you may want to
exclude it from your cross-cluster search. (Note: the endpoint was able to tell there were
matching indices because it fell back to using the <<indices-resolve-index-api,
resolve index>> API.)
