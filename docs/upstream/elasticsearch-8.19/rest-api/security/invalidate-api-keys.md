<!-- Converted from rest-api/security/invalidate-api-keys.asciidoc (AsciiDoc). Includes are inlined. -->

### Invalidate API key API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Invalidates one or more API keys.

#### Request

`DELETE /_security/api_key`

#### Prerequisites

* To use this API, you must have at least the `manage_security`, `manage_api_key`, or `manage_own_api_key` cluster privilege.
The `manage_security` privilege allows deleting any API key, including both REST and cross cluster API keys.
The `manage_api_key` privilege allows deleting any REST API key, but not cross cluster API keys.
The `manage_own_api_key` only allows deleting REST API keys owned by the user.
In addition, with the `manage_own_api_key` privilege, an invalidation request must be issued
in one of the three formats:
1. Set the parameter `owner=true`
2. Or, set both `username` and `realm_name` to match the user's identity.
3. Or, if the request is issued by an API key, i.e. an API key invalidates itself, specify its ID in the `ids` field.

#### Description

This API invalidates API keys created by the create API key or grant API key
APIs.
Invalidated API keys fail authentication, but they can still be viewed using the
get API key information and query API key information APIs,
for at least the configured retention period, until they are automatically deleted.

#### Request body

The following parameters can be specified in the body of a DELETE request and
pertain to invalidating api keys:

`ids`::
(Optional, array of string) A list of API key ids. This parameter cannot be used
when any of `name`, `realm_name`, `username` are used

`name`::
(Optional, string) An API key name. This parameter cannot be used with any of
`ids`, `realm_name` or `username` are used.

`realm_name`::
(Optional, string) The name of an authentication realm. This parameter cannot be
used with either `ids` or `name` or when `owner` flag is set to `true`.

`username`::
(Optional, string) The username of a user. This parameter cannot be used with
either `ids` or `name` or when `owner` flag is set to `true`.

`owner`::
(Optional, Boolean) A boolean flag that can be used to query API keys owned
by the currently authenticated user. Defaults to false.
The 'realm_name' or 'username' parameters cannot be specified when this
parameter is set to 'true' as they are assumed to be the currently authenticated ones.

**Note:** At least one of "ids", "name", "username" and "realm_name" must be specified
 if "owner" is "false" (default).

#### Response body

A successful call returns a JSON structure that contains the ids of the API keys
that were invalidated, the ids of the API keys that had already been invalidated,
and potentially a list of errors encountered while invalidating specific api
keys.

#### Examples

If you create an API key as follows:

```console
POST /_security/api_key
{
  "name": "my-api-key"
}
```

A successful call returns a JSON structure that provides
API key information. For example:

```console-result
{
  "id": "VuaCfGcBCdbkQm-e5aOx",
  "name": "my-api-key",
  "api_key": "ui2lp2axTNmsyakw9tvNnw",
  "encoded": "VnVhQ2ZHY0JDZGJrUW0tZTVhT3g6dWkybHAyYXhUTm1zeWFrdzl0dk5udw=="
}
```

The following example invalidates the API key identified by specified `ids`
immediately:

```console
DELETE /_security/api_key
{
  "ids" : [ "VuaCfGcBCdbkQm-e5aOx" ]
}
```

The following example invalidates the API key identified by specified `name`
immediately:

```console
DELETE /_security/api_key
{
  "name" : "my-api-key"
}
```

The following example invalidates all API keys for the `native1` realm
immediately:

```console
DELETE /_security/api_key
{
  "realm_name" : "native1"
}
```

The following example invalidates all API keys for the user `myuser` in all
realms immediately:

```console
DELETE /_security/api_key
{
  "username" : "myuser"
}
```

The following example invalidates the API key identified by the specified `ids` if
 it is owned by the currently authenticated user immediately:

```console
DELETE /_security/api_key
{
  "ids" : ["VuaCfGcBCdbkQm-e5aOx"],
  "owner" : "true"
}
```

The following example invalidates all API keys owned by the currently authenticated
 user immediately:

```console
DELETE /_security/api_key
{
  "owner" : "true"
}
```

Finally, the following example invalidates all API keys for the user `myuser` in
 the `native1` realm immediately:

```console
DELETE /_security/api_key
{
  "username" : "myuser",
  "realm_name" : "native1"
}
```

```js
{
  "invalidated_api_keys": [ <1>
    "api-key-id-1"
  ],
  "previously_invalidated_api_keys": [ <2>
    "api-key-id-2",
    "api-key-id-3"
  ],
  "error_count": 2, <3>
  "error_details": [ <4>
    {
      "type": "exception",
      "reason": "error occurred while invalidating api keys",
      "caused_by": {
        "type": "illegal_argument_exception",
        "reason": "invalid api key id"
      }
    },
    {
      "type": "exception",
      "reason": "error occurred while invalidating api keys",
      "caused_by": {
        "type": "illegal_argument_exception",
        "reason": "invalid api key id"
      }
    }
  ]
}
```

<1> The IDs of the API keys that were invalidated as part of this request.
<2> The IDs of the API keys that were already invalidated.
<3> The number of errors that were encountered when invalidating the API keys.
<4> Details about these errors. This field is not present in the response when
    `error_count` is 0.
