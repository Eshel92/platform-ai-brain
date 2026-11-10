<!-- Converted from rest-api/security/update-api-key.asciidoc (AsciiDoc). Includes are inlined. -->

### Update API key API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

#### Request

`PUT /_security/api_key/<id>`

#### Prerequisites

* To use this API, you must have at least the `manage_own_api_key` cluster privilege.
Users can only update API keys that they created or that were granted to them.
To update another user's API key, use the `run_as` feature
to submit a request on behalf of another user.

**Important:** It's not possible to use an API key as the authentication credential for this API.
To update an API key, the owner user's credentials are required.

#### Description

Use this API to update API keys created by the create API Key or grant API Key APIs.
If you need to apply the same update to many API keys, you can use bulk update API Keys to reduce overhead.

It's not possible to update expired API keys, or API keys that have been invalidated by invalidate API Key.

This API supports updates to an API key's access scope, metadata and expiration.
The access scope of an API key is derived from the `role_descriptors` you specify in the request, and a snapshot of the owner user's permissions at the time of the request.
The snapshot of the owner's permissions is updated automatically on every call.

**Important:**
If you don't specify `role_descriptors` in the request, a call to this API might still change the API key's access scope.
This change can occur if the owner user's permissions have changed since the API key was created or last modified.

#### Path parameters

`id`::
(Required, string) The ID of the API key to update.

#### Request body

You can specify the following parameters in the request body, which is optional.

`role_descriptors`::
(Optional, object) The role descriptors to assign to this API key.
The API key's effective permissions are an intersection of its assigned privileges and the point in time snapshot of permissions of the owner user.
You can assign new privileges by specifying them in this parameter.
To remove assigned privileges, you can supply an empty `role_descriptors` parameter, i.e., an empty object `{}`.
If an API key has no assigned privileges, it inherits the owner user's full permissions.
The snapshot of the owner's permissions is always updated, whether you supply the `role_descriptors` parameter or not.
The structure of a role descriptor is the same as the request for the create API keys API.

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

If you create an API key as follows:

```console
POST /_security/api_key
{
  "name": "my-api-key",
  "role_descriptors": {
    "role-a": {
      "cluster": ["all"],
      "indices": [
        {
          "names": ["index-a*"],
          "privileges": ["read"]
        }
      ]
    }
  },
  "metadata": {
    "application": "my-application",
    "environment": {
       "level": 1,
       "trusted": true,
       "tags": ["dev", "staging"]
    }
  }
}
```

A successful call returns a JSON structure that provides API key information.
For example:

```console-result
{
  "id": "VuaCfGcBCdbkQm-e5aOx",
  "name": "my-api-key",
  "api_key": "ui2lp2axTNmsyakw9tvNnw",
  "encoded": "VnVhQ2ZHY0JDZGJrUW0tZTVhT3g6dWkybHAyYXhUTm1zeWFrdzl0dk5udw=="
}
```

For the examples below, assume that the owner user's permissions are:

```js
{
  "cluster": ["all"],
  "indices": [
    {
      "names": ["*"],
      "privileges": ["all"]
    }
  ]
}
```

The following example updates the API key created above, assigning it new role descriptors and metadata:

```console
PUT /_security/api_key/VuaCfGcBCdbkQm-e5aOx
{
  "role_descriptors": {
    "role-a": {
      "indices": [
        {
          "names": ["*"],
          "privileges": ["write"]
        }
      ]
    }
  },
  "metadata": {
    "environment": {
       "level": 2,
       "trusted": true,
       "tags": ["production"]
    }
  }
}
```

A successful call returns a JSON structure indicating that the API key was updated:

```console-result
{
  "updated": true
}
```

The API key's effective permissions after the update will be the intersection of the supplied role descriptors and the owner user's permissions:

```js
{
  "indices": [
    {
      "names": ["*"],
      "privileges": ["write"]
    }
  ]
}
```

The following example removes the API key's previously assigned permissions, making it inherit the owner user's full permissions.

```console
PUT /_security/api_key/VuaCfGcBCdbkQm-e5aOx
{
  "role_descriptors": {}
}
```

Which returns the response:

```console-result
{
  "updated": true
}
```

The API key's effective permissions after the update will be the same as the owner user's:

```js
{
  "cluster": ["all"],
  "indices": [
    {
      "names": ["*"],
      "privileges": ["all"]
    }
  ]
}
```

For the next example, assume that the owner user's permissions have changed from the original permissions to:

```js
{
  "cluster": ["manage_security"],
  "indices": [
    {
      "names": ["*"],
      "privileges": ["read"]
    }
  ]
}
```

The following request auto-updates the snapshot of the user's permissions associated with the API key:

```console
PUT /_security/api_key/VuaCfGcBCdbkQm-e5aOx
```

Which returns the response:

```console-result
{
  "updated": true
}
```

Resulting in the following effective permissions for the API key:

```js
{
  "cluster": ["manage_security"],
  "indices": [
    {
      "names": ["*"],
      "privileges": ["read"]
    }
  ]
}
```
