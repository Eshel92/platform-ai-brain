<!-- Converted from rest-api/security/update-cross-cluster-api-key.asciidoc (AsciiDoc). Includes are inlined. -->

### Update Cross-Cluster API key API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Update an existing cross-cluster API Key that is used for API key based remote cluster access.

#### Request

`PUT /_security/cross_cluster/api_key/<id>`

#### Prerequisites

* To use this API, you must have at least the `manage_security` cluster privilege.
Users can only update API keys that they created.
To update another user's API key, use the `run_as` feature
to submit a request on behalf of another user.

**Important:** It's not possible to use an API key as the authentication credential for this API.
To update an API key, the owner user's credentials are required.

#### Description

Use this API to update cross-cluster API keys created by the Create Cross-Cluster API key API.
It's not possible to update expired API keys, or API keys that have been invalidated by
invalidate API Key.

This API supports updates to an API key's access scope, metadata and expiration.
The owner user's information, e.g. `username`, `realm`, is also updated automatically on every call.

**Note:** This API cannot update REST API keys, which should be updated by
either security-api-update-api-key or security-api-bulk-update-api-keys API.

#### Path parameters

`id`::
(Required, string) The ID of the API key to update.

#### Request body

You can specify the following parameters in the request body. The parameters are optional. But they cannot all be absent.

`access`::
(Optional, object) The access to be granted to this API key. The access is
composed of permissions for cross cluster search and cross cluster replication.
At least one of them must be specified.
When specified, the new access assignment fully replaces the previously assigned access.
Refer to the parameter of the same of the Create Cross-Cluster API key API
for the field's structure.

`metadata`::
(Optional, object) Arbitrary metadata that you want to associate with the API key.
It supports nested data structure.
Within the `metadata` object, top-level keys beginning with `_` are reserved for system usage.
When specified, this fully replaces metadata previously associated with the API key.

`expiration`::
(Optional, string) Expiration time for the API key. By default, API keys never expire. Can be omitted to leave unchanged.

#### Response body

`updated`::
(boolean) If `true`, the API key was updated.
If `false`, the API key didn't change because no change was detected.

#### Examples

If you create a cross-cluster API key as follows:

```console
POST /_security/cross_cluster/api_key
{
  "name": "my-cross-cluster-api-key",
  "access": {
    "search": [
      {
        "names": ["logs*"]
      }
    ]
  },
  "metadata": {
    "application": "search"
  }
}
```

A successful call returns a JSON structure that provides API key information.
For example:

```console-result
{
  "id": "VuaCfGcBCdbkQm-e5aOx",
  "name": "my-cross-cluster-api-key",
  "api_key": "ui2lp2axTNmsyakw9tvNnw",
  "encoded": "VnVhQ2ZHY0JDZGJrUW0tZTVhT3g6dWkybHAyYXhUTm1zeWFrdzl0dk5udw=="
}
```

Information of the API key, including its exact role descriptor can be inspected with
the Get API key API

```console
GET /_security/api_key?id=VuaCfGcBCdbkQm-e5aOx
```

A successful call returns a JSON structure that contains the information of the API key:

```js
{
  "api_keys": [
    {
      "id": "VuaCfGcBCdbkQm-e5aOx",
      "name": "my-cross-cluster-api-key",
      "type": "cross_cluster",
      "creation": 1548550550158,
      "expiration": null,
      "invalidated": false,
      "username": "myuser",
      "realm": "native1",
      "metadata": {
        "application": "search"
      },
      "role_descriptors": {
        "cross_cluster": {  <1>
          "cluster": [
              "cross_cluster_search"
          ],
          "indices": [
            {
              "names": [
                "logs*"
              ],
              "privileges": [
                "read", "read_cross_cluster", "view_index_metadata"
              ],
              "allow_restricted_indices": false
            }
          ],
          "applications": [ ],
          "run_as": [ ],
          "metadata": { },
          "transient_metadata": {
            "enabled": true
          }
        }
      },
      "access": {  <2>
        "search": [
          {
            "names": [
              "logs*"
            ],
            "allow_restricted_indices": false
          }
        ]
      }
    }
  ]
}
```
<1> Role descriptor corresponding to the specified `access` scope at creation time.
In this example, it grants cross cluster search permission for the `logs*` index pattern.
<2> The `access` corresponds to the value specified at API key creation time.

The following example updates the API key created above, assigning it new access scope and metadata:

```console
PUT /_security/cross_cluster/api_key/VuaCfGcBCdbkQm-e5aOx
{
  "access": {
    "replication": [
      {
        "names": ["archive"]
      }
    ]
  },
  "metadata": {
    "application": "replication"
  }
}
```

A successful call returns a JSON structure indicating that the API key was updated:

```console-result
{
  "updated": true
}
```

The API key's permissions after the update can be inspected again with the Get API key API
and it will be:

```js
{
  "api_keys": [
    {
      "id": "VuaCfGcBCdbkQm-e5aOx",
      "name": "my-cross-cluster-api-key",
      "type": "cross_cluster",
      "creation": 1548550550158,
      "expiration": null,
      "invalidated": false,
      "username": "myuser",
      "realm": "native1",
      "metadata": {
        "application": "replication"
      },
      "role_descriptors": {
        "cross_cluster": {  <1>
          "cluster": [
              "cross_cluster_replication"
          ],
          "indices": [
            {
              "names": [
                "archive*"
              ],
              "privileges": [
                "cross_cluster_replication", "cross_cluster_replication_internal"
              ],
              "allow_restricted_indices": false
            }
          ],
          "applications": [ ],
          "run_as": [ ],
          "metadata": { },
          "transient_metadata": {
            "enabled": true
          }
        }
      },
      "access": {  <2>
        "replication": [
          {
            "names": [
              "archive*"
            ],
            "allow_restricted_indices": false
          }
        ]
      }
    }
  ]
}
```
<1> Role descriptor is updated to be the `access` scope specified at update time.
In this example, it is updated to grant the cross cluster replication permission
for the `archive*` index pattern.
<2> The `access` corresponds to the value specified at API key update time.
