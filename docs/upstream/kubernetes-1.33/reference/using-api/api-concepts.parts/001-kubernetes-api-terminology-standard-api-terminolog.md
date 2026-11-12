<!-- Part 1 of 4 of reference/using-api/api-concepts.md (split because the page is big). -->

## Kubernetes API terminology {#standard-api-terminology}

Kubernetes generally leverages common RESTful terminology to describe the
API concepts:

* A *resource type* is the name used in the URL (`pods`, `namespaces`, `services`)
* All resource types have a concrete representation (their object schema) which is called a *kind*
* A list of instances of a resource type is known as a *collection*
* A single instance of a resource type is called a *resource*, and also usually represents an *object*
* For some resource types, the API includes one or more *sub-resources*, which are represented as URI paths below the resource

Most Kubernetes API resource types are
{{< glossary_tooltip text="objects" term_id="object" >}} –
they represent a concrete instance of a concept on the cluster, like a
pod or namespace. A smaller number of API resource types are *virtual* in
that they often represent operations on objects, rather than objects, such
as a permission check
(use a POST with a JSON-encoded body of `SubjectAccessReview` to the
`subjectaccessreviews` resource), or the `eviction` sub-resource of a Pod
(used to trigger
[API-initiated eviction](/docs/concepts/scheduling-eviction/api-eviction/)).

### Object names

All objects you can create via the API have a unique object
{{< glossary_tooltip text="name" term_id="name" >}} to allow idempotent creation and
retrieval, except that virtual resource types may not have unique names if they are
not retrievable, or do not rely on idempotency.
Within a {{< glossary_tooltip text="namespace" term_id="namespace" >}}, only one object
of a given kind can have a given name at a time. However, if you delete the object,
you can make a new object with the same name. Some objects are not namespaced (for
example: Nodes), and so their names must be unique across the whole cluster.

### API verbs

Almost all object resource types support the standard HTTP verbs - GET, POST, PUT, PATCH,
and DELETE. Kubernetes also uses its own verbs, which are often written in lowercase to distinguish
them from HTTP verbs.

Kubernetes uses the term **list** to describe the action of returning a [collection](#collections) of
resources, to distinguish it from retrieving a single resource which is usually called
a **get**. If you sent an HTTP GET request with the `?watch` query parameter,
Kubernetes calls this a **watch** and not a **get**
(see [Efficient detection of changes](#efficient-detection-of-changes) for more details).

For PUT requests, Kubernetes internally classifies these as either **create** or **update**
based on the state of the existing object. An **update** is different from a **patch**; the
HTTP verb for a **patch** is PATCH.


## Resource URIs

All resource types are either scoped by the cluster (`/apis/GROUP/VERSION/*`) or to a
namespace (`/apis/GROUP/VERSION/namespaces/NAMESPACE/*`). A namespace-scoped resource
type will be deleted when its namespace is deleted and access to that resource type
is controlled by authorization checks on the namespace scope.

Note: core resources use `/api` instead of `/apis` and omit the GROUP path segment.

Examples:

* `/api/v1/namespaces`
* `/api/v1/pods`
* `/api/v1/namespaces/my-namespace/pods`
* `/apis/apps/v1/deployments`
* `/apis/apps/v1/namespaces/my-namespace/deployments`
* `/apis/apps/v1/namespaces/my-namespace/deployments/my-deployment`

You can also access collections of resources (for example: listing all Nodes).
The following paths are used to retrieve collections and resources:

* Cluster-scoped resources:

  * `GET /apis/GROUP/VERSION/RESOURCETYPE` - return the collection of resources of the resource type
  * `GET /apis/GROUP/VERSION/RESOURCETYPE/NAME` - return the resource with NAME under the resource type

* Namespace-scoped resources:

  * `GET /apis/GROUP/VERSION/RESOURCETYPE` - return the collection of all
    instances of the resource type across all namespaces
  * `GET /apis/GROUP/VERSION/namespaces/NAMESPACE/RESOURCETYPE` - return
    collection of all instances of the resource type in NAMESPACE
  * `GET /apis/GROUP/VERSION/namespaces/NAMESPACE/RESOURCETYPE/NAME` -
    return the instance of the resource type with NAME in NAMESPACE

Since a namespace is a cluster-scoped resource type, you can retrieve the list
(“collection”) of all namespaces with `GET /api/v1/namespaces` and details about
a particular namespace with `GET /api/v1/namespaces/NAME`.

* Cluster-scoped subresource: `GET /apis/GROUP/VERSION/RESOURCETYPE/NAME/SUBRESOURCE`
* Namespace-scoped subresource: `GET /apis/GROUP/VERSION/namespaces/NAMESPACE/RESOURCETYPE/NAME/SUBRESOURCE`

The verbs supported for each subresource will differ depending on the object -
see the [API reference](/docs/reference/kubernetes-api/) for more information. It
is not possible to access sub-resources across multiple resources - generally a new
virtual resource type would be used if that becomes necessary.


## HTTP media types {#alternate-representations-of-resources}

Over HTTP, Kubernetes supports JSON and Protobuf wire encodings.

By default, Kubernetes returns objects in [JSON serialization](#json-encoding), using the
`application/json` media type. Although JSON is the default, clients may request a response in
YAML, or use the more efficient binary [Protobuf representation](#protobuf-encoding) for better performance at scale.

The Kubernetes API implements standard HTTP content type negotiation: passing an
`Accept` header with a `GET` call will request that the server tries to return
a response in your preferred media type. If you want to send an object in Protobuf to
the server for a `PUT` or `POST` request, you must set the `Content-Type` request header
appropriately.

If you request an available media type, the API server returns a response with a suitable
`Content-Type`; if none of the media types you request are supported, the API server returns
a `406 Not acceptable` error message.
All built-in resource types support the `application/json` media type.

### JSON resource encoding {#json-encoding}

The Kubernetes API defaults to using [JSON](https://www.json.org/json-en.html) for encoding
HTTP message bodies.

For example:

1. List all of the pods on a cluster, without specifying a preferred format

   ```
   GET /api/v1/pods
   ```

   ```
   200 OK
   Content-Type: application/json

   … JSON encoded collection of Pods (PodList object)
   ```

1. Create a pod by sending JSON to the server, requesting a JSON response.

   ```
   POST /api/v1/namespaces/test/pods
   Content-Type: application/json
   Accept: application/json
   … JSON encoded Pod object
   ```

   ```
   200 OK
   Content-Type: application/json

   {
     "kind": "Pod",
     "apiVersion": "v1",
     …
   }
   ```

### YAML resource encoding {#yaml-encoding}

Kubernetes also supports the [`application/yaml`](https://www.rfc-editor.org/rfc/rfc9512.html)
media type for both requests and responses. [`YAML`](https://yaml.org/)
can be used for defining Kubernetes manifests and API interactions.

For example:

1. List all of the pods on a cluster in YAML format

   ```
   GET /api/v1/pods
   Accept: application/yaml
   ```
   
   ```
   200 OK
   Content-Type: application/yaml

   … YAML encoded collection of Pods (PodList object)
   ```

1. Create a pod by sending YAML-encoded data to the server, requesting a YAML response:

   ```
   POST /api/v1/namespaces/test/pods
   Content-Type: application/yaml
   Accept: application/yaml
   … YAML encoded Pod object
   ```

   ```
   200 OK
   Content-Type: application/yaml

   apiVersion: v1
   kind: Pod
   metadata:
     name: my-pod
     …
   ```

### Kubernetes Protobuf encoding {#protobuf-encoding}

Kubernetes uses an envelope wrapper to encode [Protobuf](https://protobuf.dev/) responses.
That wrapper starts with a 4 byte magic number to help identify content in disk or in etcd as Protobuf
(as opposed to JSON). The 4 byte magic number data is followed by a Protobuf encoded wrapper message, which
describes the encoding and type of the underlying object. Within the Protobuf wrapper message,
the inner object data is recorded using the `raw` field of Unknown (see the [IDL](#protobuf-encoding-idl)
for more detail).

For example:

1. List all of the pods on a cluster in Protobuf format.

   ```
   GET /api/v1/pods
   Accept: application/vnd.kubernetes.protobuf
   ```

   ```
   200 OK
   Content-Type: application/vnd.kubernetes.protobuf

   … binary encoded collection of Pods (PodList object)
   ```

1. Create a pod by sending Protobuf encoded data to the server, but request a response
   in JSON.

   ```
   POST /api/v1/namespaces/test/pods
   Content-Type: application/vnd.kubernetes.protobuf
   Accept: application/json
   … binary encoded Pod object
   ```

   ```
   200 OK
   Content-Type: application/json

   {
     "kind": "Pod",
     "apiVersion": "v1",
     ...
   }
   ```

You can use both techniques together and use Kubernetes' Protobuf encoding to interact with any API that
supports it, for both reads and writes. Only some API resource types are [compatible](#protobuf-encoding-compatibility)
with Protobuf.

<a id="protobuf-encoding-idl" />

The wrapper format is:

```
A four byte magic number prefix:
  Bytes 0-3: "k8s\x00" [0x6b, 0x38, 0x73, 0x00]

An encoded Protobuf message with the following IDL:
  message Unknown {
    // typeMeta should have the string values for "kind" and "apiVersion" as set on the JSON object
    optional TypeMeta typeMeta = 1;

    // raw will hold the complete serialized object in protobuf. See the protobuf definitions in the client libraries for a given kind.
    optional bytes raw = 2;

    // contentEncoding is encoding used for the raw data. Unspecified means no encoding.
    optional string contentEncoding = 3;

    // contentType is the serialization method used to serialize 'raw'. Unspecified means application/vnd.kubernetes.protobuf and is usually
    // omitted.
    optional string contentType = 4;
  }

  message TypeMeta {
    // apiVersion is the group/version for this type
    optional string apiVersion = 1;
    // kind is the name of the object schema. A protobuf definition should exist for this object.
    optional string kind = 2;
  }
```

{{< note >}}
Clients that receive a response in `application/vnd.kubernetes.protobuf` that does
not match the expected prefix should reject the response, as future versions may need
to alter the serialization format in an incompatible way and will do so by changing
the prefix.
{{< /note >}}

#### Compatibility with Kubernetes Protobuf {#protobuf-encoding-compatibility}

Not all API resource types support Kubernetes' Protobuf encoding; specifically, Protobuf isn't
available for resources that are defined as
{{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinitions" >}}
or are served via the
{{< glossary_tooltip text="aggregation layer" term_id="aggregation-layer" >}}.

As a client, if you might need to work with extension types you should specify multiple
content types in the request `Accept` header to support fallback to JSON.
For example:

```
Accept: application/vnd.kubernetes.protobuf, application/json
```

### CBOR resource encoding {#cbor-encoding}

{{< feature-state feature_gate_name="CBORServingAndStorage" >}}

With the `CBORServingAndStorage` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/)
enabled, request and response bodies for all built-in resource types and all resources defined by a
{{< glossary_tooltip term_id="CustomResourceDefinition" text="CustomResourceDefinition" >}} may be encoded to the
[CBOR](https://www.rfc-editor.org/rfc/rfc8949) binary data format. CBOR is also supported at the
{{< glossary_tooltip text="aggregation layer" term_id="aggregation-layer" >}} if it is enabled in
individual aggregated API servers.

Clients should indicate the IANA media type `application/cbor` in the `Content-Type` HTTP request
header when the request body contains a single CBOR
[encoded data item](https://www.rfc-editor.org/rfc/rfc8949.html#section-1.2-4.2), and in the `Accept` HTTP request
header when prepared to accept a CBOR encoded data item in the response. API servers will use
`application/cbor` in the `Content-Type` HTTP response header when the response body contains a
CBOR-encoded object.

If an API server encodes its response to a [watch request](#efficient-detection-of-changes) using
CBOR, the response body will be a [CBOR Sequence](https://www.rfc-editor.org/rfc/rfc8742) and the
`Content-Type` HTTP response header will use the IANA media type `application/cbor-seq`. Each entry
of the sequence (if any) is a single CBOR-encoded watch event.

In addition to the existing `application/apply-patch+yaml` media type for YAML-encoded
[server-side apply configurations](#patch-and-apply), API servers that enable CBOR will accept the
`application/apply-patch+cbor` media type for CBOR-encoded server-side apply configurations. There
is no supported CBOR equivalent for `application/json-patch+json` or `application/merge-patch+json`,
or `application/strategic-merge-patch+json`.


## Efficient detection of changes

The Kubernetes API allows clients to make an initial request for an object or a
collection, and then to track changes since that initial request: a **watch**. Clients
can send a **list** or a **get** and then make a follow-up **watch** request.

To make this change tracking possible, every Kubernetes object has a `resourceVersion`
field representing the version of that resource as stored in the underlying persistence
layer. When retrieving a collection of resources (either namespace or cluster scoped),
the response from the API server contains a `resourceVersion` value. The client can
use that `resourceVersion` to initiate a **watch** against the API server.

When you send a **watch** request, the API server responds with a stream of
changes. These changes itemize the outcome of operations (such as **create**, **delete**,
and **update**) that occurred after the `resourceVersion` you specified as a parameter
to the **watch** request. The overall **watch** mechanism allows a client to fetch
the current state and then subscribe to subsequent changes, without missing any events.

If a client **watch** is disconnected then that client can start a new **watch** from
the last returned `resourceVersion`; the client could also perform a fresh **get** /
**list** request and begin again. See [Resource Version Semantics](#resource-versions)
for more detail.

For example:

1. List all of the pods in a given namespace.

   ```http
   GET /api/v1/namespaces/test/pods
   ---
   200 OK
   Content-Type: application/json

   {
     "kind": "PodList",
     "apiVersion": "v1",
     "metadata": {"resourceVersion":"10245"},
     "items": [...]
   }
   ```

2. Starting from resource version 10245, receive notifications of any API operations
   (such as **create**, **delete**, **patch** or **update**) that affect Pods in the
   _test_ namespace. Each change notification is a JSON document. The HTTP response body
   (served as `application/json`) consists a series of JSON documents.

   ```http
   GET /api/v1/namespaces/test/pods?watch=1&resourceVersion=10245
   ---
   200 OK
   Transfer-Encoding: chunked
   Content-Type: application/json

   {
     "type": "ADDED",
     "object": {"kind": "Pod", "apiVersion": "v1", "metadata": {"resourceVersion": "10596", ...}, ...}
   }
   {
     "type": "MODIFIED",
     "object": {"kind": "Pod", "apiVersion": "v1", "metadata": {"resourceVersion": "11020", ...}, ...}
   }
   ...
   ```

A given Kubernetes server will only preserve a historical record of changes for a
limited time. Clusters using etcd 3 preserve changes in the last 5 minutes by default.
When the requested **watch** operations fail because the historical version of that
resource is not available, clients must handle the case by recognizing the status code
`410 Gone`, clearing their local cache, performing a new **get** or **list** operation,
and starting the **watch** from the `resourceVersion` that was returned.

For subscribing to collections, Kubernetes client libraries typically offer some form
of standard tool for this **list**-then-**watch** logic. (In the Go client library,
this is called a `Reflector` and is located in the `k8s.io/client-go/tools/cache` package.)

### Watch bookmarks {#watch-bookmarks}

To mitigate the impact of short history window, the Kubernetes API provides a watch
event named `BOOKMARK`. It is a special kind of event to mark that all changes up
to a given `resourceVersion` the client is requesting have already been sent. The
document representing the `BOOKMARK` event is of the type requested by the request,
but only includes a `.metadata.resourceVersion` field. For example:

```http
GET /api/v1/namespaces/test/pods?watch=1&resourceVersion=10245&allowWatchBookmarks=true
---
200 OK
Transfer-Encoding: chunked
Content-Type: application/json

{
  "type": "ADDED",
  "object": {"kind": "Pod", "apiVersion": "v1", "metadata": {"resourceVersion": "10596", ...}, ...}
}
...
{
  "type": "BOOKMARK",
  "object": {"kind": "Pod", "apiVersion": "v1", "metadata": {"resourceVersion": "12746"} }
}
```

As a client, you can request `BOOKMARK` events by setting the
`allowWatchBookmarks=true` query parameter to a **watch** request, but you shouldn't
assume bookmarks are returned at any specific interval, nor can clients assume that
the API server will send any `BOOKMARK` event even when requested.
