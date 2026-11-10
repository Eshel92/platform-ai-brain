<!-- Converted from rest-api/security/get-service-credentials.asciidoc (AsciiDoc). Includes are inlined. -->

### Get service account credentials API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Retrieves all service credentials for a  service account.

#### Request

`GET /_security/service/<namespace>/<service>/credential`

#### Prerequisites

* To use this API, you must have at least the `read_security`
cluster privilege (or a greater privilege
such as `manage_service_account` or `manage_security`).

#### Description

Use this API to retrieve a list of credentials for a service account.
The response includes service account tokens that were created with the
create service account tokens API
as well as file-backed tokens from all nodes of the cluster.

**Note:** For tokens backed by the `service_tokens` file, the API collects
them from all nodes of the cluster. Tokens with the same name from
different nodes are assumed to be the same token and are only counted once
towards the total number of service tokens.

#### Path parameters

`namespace`::
(Required, string) Name of the namespace.

`service`::
(Required, string) Name of the service name.

#### Examples

The following request uses the create service account token API to create a service account token named `token1`
in the `elastic/fleet-server` service account:

```console
POST /_security/service/elastic/fleet-server/credential/token/token1
```

The following request returns all credentials for the `elastic/fleet-server`
service account:

```console
GET /_security/service/elastic/fleet-server/credential
```

The response includes all credentials related to the specified service account:

```js
{
  "service_account": "elastic/fleet-server",
  "count": 3,
  "tokens": {
    "token1": {},        <1>
    "token42": {}        <2>
  },
  "nodes_credentials": { <3>
    "_nodes": {          <4>
      "total": 3,
      "successful": 3,
      "failed": 0
    },
    "file_tokens": {      <5>
      "my-token": {
        "nodes": [ "node0", "node1" ] <6>
      }
    }
  }
}
```
<1> A new service account token backed by the `.security` index
<2> An existing service account token backed by the `.security` index
<3> This section contains service account credentials collected from all nodes of the cluster
<4> General status showing how nodes respond to the above collection request
<5> File-backed tokens collected from all nodes
<6> List of nodes that (file-backed) `my-token` is found
