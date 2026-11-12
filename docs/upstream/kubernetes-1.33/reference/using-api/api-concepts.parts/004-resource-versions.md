<!-- Part 4 of 4 of reference/using-api/api-concepts.md (split because the page is big). -->

## Resource versions

Resource versions are strings that identify the server's internal version of an
object. Resource versions can be used by clients to determine when objects have
changed, or to express data consistency requirements when getting, listing and
watching resources. Resource versions must be treated as opaque by clients and passed
unmodified back to the server.

You must not assume resource versions are numeric or collatable. API clients may
only compare two resource versions for equality (this means that you must not compare
resource versions for greater-than or less-than relationships).

### `resourceVersion` fields in metadata {#resourceversion-in-metadata}

Clients find resource versions in resources, including the resources from the response
stream for a **watch**, or when using **list** to enumerate resources.

[v1.meta/ObjectMeta](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#objectmeta-v1-meta) -
The `metadata.resourceVersion` of a resource instance identifies the resource version the instance was last modified at.

[v1.meta/ListMeta](/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#listmeta-v1-meta) -
The `metadata.resourceVersion` of a resource collection (the response to a **list**) identifies the
resource version at which the collection was constructed.

### `resourceVersion` parameters in query strings {#the-resourceversion-parameter}

The **get**, **list**, and **watch** operations support the `resourceVersion` parameter.
From version v1.19, Kubernetes API servers also support the `resourceVersionMatch`
parameter on _list_ requests.

The API server interprets the `resourceVersion` parameter differently depending
on the operation you request, and on the value of `resourceVersion`. If you set
`resourceVersionMatch` then this also affects the way matching happens.

### Semantics for **get** and **list**

For **get** and **list**, the semantics of `resourceVersion` are:

**get:**

| resourceVersion unset | resourceVersion="0" | resourceVersion="{value other than 0}" |
|-----------------------|---------------------|----------------------------------------|
| Most Recent           | Any                 | Not older than                         |

**list:**

From version v1.19, Kubernetes API servers support the `resourceVersionMatch` parameter
on _list_ requests. If you set both `resourceVersion` and `resourceVersionMatch`, the
`resourceVersionMatch` parameter determines how the API server interprets
`resourceVersion`.

You should always set the `resourceVersionMatch` parameter when setting
`resourceVersion` on a **list** request. However, be prepared to handle the case
where the API server that responds is unaware of `resourceVersionMatch`
and ignores it.

Unless you have strong consistency requirements, using `resourceVersionMatch=NotOlderThan` and
a known `resourceVersion` is preferable since it can achieve better performance and scalability
of your cluster than leaving `resourceVersion` and `resourceVersionMatch` unset, which requires
quorum read to be served.

Setting the `resourceVersionMatch` parameter without setting `resourceVersion` is not valid.

This table explains the behavior of **list** requests with various combinations of
`resourceVersion` and `resourceVersionMatch`:

{{< table caption="resourceVersionMatch and paging parameters for list" >}}

| resourceVersionMatch param          | paging params                  | resourceVersion not set | resourceVersion="0" | resourceVersion="{value other than 0}" |
|-------------------------------------|--------------------------------|-------------------------|---------------------|----------------------------------------|
| _unset_                             | _limit unset_                  | Most Recent             | Any                 | Not older than                         |
| _unset_                             | limit=\<n\>, _continue unset_  | Most Recent             | Any                 | Exact                                  |
| _unset_                             | limit=\<n\>, continue=\<token\>| Continuation            | Continuation        | Invalid, HTTP `400 Bad Request`        |
| `resourceVersionMatch=Exact`        | _limit unset_                  | Invalid                 | Invalid             | Exact                                  |
| `resourceVersionMatch=Exact`        | limit=\<n\>, _continue unset_  | Invalid                 | Invalid             | Exact                                  |
| `resourceVersionMatch=NotOlderThan` | _limit unset_                  | Invalid                 | Any                 | Not older than                         |
| `resourceVersionMatch=NotOlderThan` | limit=\<n\>, _continue unset_  | Invalid                 | Any                 | Not older than                         |

{{< /table >}}

{{< note >}}
If your cluster's API server does not honor the `resourceVersionMatch` parameter,
the behavior is the same as if you did not set it.
{{< /note >}}

The meaning of the **get** and **list** semantics are:

Any
: Return data at any resource version. The newest available resource version is preferred,
  but strong consistency is not required; data at any resource version may be served. It is possible
  for the request to return data at a much older resource version that the client has previously
  observed, particularly in high availability configurations, due to partitions or stale
  caches. Clients that cannot tolerate this should not use this semantic.
  Always served from _watch cache_, improving performance and reducing etcd load.

Most recent
: Return data at the most recent resource version. The returned data must be
  consistent (in detail: served from etcd via a quorum read).
  For etcd v3.4.31+ and v3.5.13+, Kubernetes {{< skew currentVersion >}} serves “most recent” reads from the _watch cache_:
  an internal, in-memory store within the API server that caches and mirrors the state of data
  persisted into etcd. Kubernetes requests progress notification to maintain cache consistency against
  the etcd persistence layer. Kubernetes v1.28 through to v1.30 also supported this
  feature, although as Alpha it was not recommended for production nor enabled by default until the v1.31 release.

Not older than
: Return data at least as new as the provided `resourceVersion`. The newest
  available data is preferred, but any data not older than the provided `resourceVersion` may be
  served. For **list** requests to servers that honor the `resourceVersionMatch` parameter, this
  guarantees that the collection's `.metadata.resourceVersion` is not older than the requested
  `resourceVersion`, but does not make any guarantee about the `.metadata.resourceVersion` of any
  of the items in that collection.
  Always served from _watch cache_, improving performance and reducing etcd load.

Exact
: Return data at the exact resource version provided. If the provided `resourceVersion` is
  unavailable, the server responds with HTTP `410 Gone`. For **list** requests to servers that honor the
  `resourceVersionMatch` parameter, this guarantees that the collection's `.metadata.resourceVersion`
  is the same as the `resourceVersion` you requested in the query string. That guarantee does
  not apply to the `.metadata.resourceVersion` of any items within that collection.
  By default served from _etcd_, but with the `ListFromCacheSnapshot` feature gate enabled,
  API server will attempt to serve the response from snapshot if available.
  This improves performance and reduces etcd load. Cache snapshots are kept by default for 75 seconds,
  so if the provided `resourceVersion` is unavailable, the server will fallback to etcd.

Continuation
: Return the next page of data for a paginated list request, ensuring consistency with the exact `resourceVersion` established by the initial request in the sequence.
  Response to **list** requests with limit include _continue token_, that encodes the  `resourceVersion` and last observed position from which to resume the list.
  If the `resourceVersion` in the provided _continue token_ is unavailable, the server responds with HTTP `410 Gone`.
  By default served from _etcd_, but with the `ListFromCacheSnapshot` feature gate enabled,
  API server will attempt to serve the response from snapshot if available.
  This improves performance and reduces etcd load. Cache snapshots are kept by default for 75 seconds,
  so if the `resourceVersion` in provided _continue token_ is unavailable, the server will fallback to etcd.

{{< note >}}
When you **list** resources and receive a collection response, the response includes the
[list metadata](/docs/reference/generated/kubernetes-api/v{{<skew currentVersion >}}/#listmeta-v1-meta)
of the collection as well as
[object metadata](/docs/reference/generated/kubernetes-api/v{{<skew currentVersion >}}/#objectmeta-v1-meta)
for each item in that collection. For individual objects found within a collection response,
`.metadata.resourceVersion` tracks when that object was last updated, and not how up-to-date
the object is when served.
{{< /note >}}

When using `resourceVersionMatch=NotOlderThan` and limit is set, clients must
handle HTTP `410 Gone` responses. For example, the client might retry with a
newer `resourceVersion` or fall back to `resourceVersion=""`.

When using `resourceVersionMatch=Exact` and `limit` is unset, clients must
verify that the collection's `.metadata.resourceVersion` matches
the requested `resourceVersion`, and handle the case where it does not. For
example, the client might fall back to a request with `limit` set.

### Semantics for **watch**

For **watch**, the semantics of resource version are:

**watch:**

{{< table caption="resourceVersion for watch" >}}

| resourceVersion unset               | resourceVersion="0"        | resourceVersion="{value other than 0}" |
|-------------------------------------|----------------------------|----------------------------------------|
| Get State and Start at Most Recent  | Get State and Start at Any | Start at Exact                         |

{{< /table >}}

The meaning of those **watch** semantics are:

Get State and Start at Any
: Start a **watch** at any resource version; the most recent resource version
  available is preferred, but not required. Any starting resource version is
  allowed. It is possible for the **watch** to start at a much older resource
  version that the client has previously observed, particularly in high availability
  configurations, due to partitions or stale caches. Clients that cannot tolerate
  this apparent rewinding should not start a **watch** with this semantic. To
  establish initial state, the **watch** begins with synthetic "Added" events for
  all resource instances that exist at the starting resource version. All following
  watch events are for all changes that occurred after the resource version the
  **watch** started at.

  {{< caution >}}
  **watches** initialized this way may return arbitrarily stale
  data. Please review this semantic before using it, and favor the other semantics
  where possible.
  {{< /caution >}}

Get State and Start at Most Recent
: Start a **watch** at the most recent resource version, which must be consistent
  (in detail: served from etcd via a quorum read). To establish initial state,
  the **watch** begins with synthetic "Added" events of all resources instances
  that exist at the starting resource version. All following watch events are for
  all changes that occurred after the resource version the **watch** started at.

Start at Exact
: Start a **watch** at an exact resource version. The watch events are for all changes
  after the provided resource version. Unlike "Get State and Start at Most Recent"
  and "Get State and Start at Any", the **watch** is not started with synthetic
  "Added" events for the provided resource version. The client is assumed to already
  have the initial state at the starting resource version since the client provided
  the resource version.

### "410 Gone" responses

Servers are not required to serve all older resource versions and may return a HTTP
`410 (Gone)` status code if a client requests a `resourceVersion` older than the
server has retained. Clients must be able to tolerate `410 (Gone)` responses. See
[Efficient detection of changes](#efficient-detection-of-changes) for details on
how to handle `410 (Gone)` responses when watching resources.

If you request a `resourceVersion` outside the applicable limit then, depending
on whether a request is served from cache or not, the API server may reply with a
`410 Gone` HTTP response.

### Unavailable resource versions

Servers are not required to serve unrecognized resource versions. If you request
**list** or **get** for a resource version that the API server does not recognize,
then the API server may either:

* wait briefly for the resource version to become available, then timeout with a
  `504 (Gateway Timeout)` if the provided resource versions does not become available
  in a reasonable amount of time;
* respond with a `Retry-After` response header indicating how many seconds a client
  should wait before retrying the request.

If you request a resource version that an API server does not recognize, the
kube-apiserver additionally identifies its error responses with a message
`Too large resource version`.

If you make a **watch** request for an unrecognized resource version, the API server
may wait indefinitely (until the request timeout) for the resource version to become
available.
