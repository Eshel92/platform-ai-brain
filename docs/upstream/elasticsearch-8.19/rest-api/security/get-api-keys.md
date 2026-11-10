<!-- Converted from rest-api/security/get-api-keys.asciidoc (AsciiDoc). Includes are inlined. -->

### Get API key information API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Retrieves information for one or more API keys.

#### Request

`GET /_security/api_key`

#### Prerequisites

* To use this API, you must have at least the `manage_own_api_key` or the
`read_security` cluster privileges.
** If you only have the `manage_own_api_key` privilege, this API only returns
the API keys that you own.
**Note:** Authenticating with an API key that has the `manage_own_api_key` privilege
does not allow retrieving the authenticated user's own keys. Instead,
authenticate the user with basic credentials.
** If you have `read_security`, `manage_api_key` or greater
privileges (including `manage_security`), this API returns all API keys
regardless of ownership.

#### Description

The information for the API keys created by
create API Key can be retrieved using this API.

#### Path parameters

The following parameters can be specified in the query parameters of a GET request and
pertain to retrieving api keys:

`id`::
(Optional, string) An API key id. This parameter cannot be used with any of
`name`, `realm_name` or `username` are used.

`name`::
(Optional, string) An API key name. This parameter cannot be used with any of
`id`, `realm_name` or `username` are used. It supports prefix search with wildcard.

`realm_name`::
(Optional, string) The name of an authentication realm. This parameter cannot be
used with either `id` or `name` or when `owner` flag is set to `true`.

`username`::
(Optional, string) The username of a user. This parameter cannot be used with
either `id` or `name` or when `owner` flag is set to `true`.

`owner`::
(Optional, Boolean) A boolean flag that can be used to query API keys owned
by the currently authenticated user. Defaults to false.
The 'realm_name' or 'username' parameters cannot be specified when this
parameter is set to 'true' as they are assumed to be the currently authenticated ones.

`with_limited_by`::
(Optional, Boolean) A boolean flag to return the snapshot of the owner user's role descriptors
associated with the API key. An API key's actual permission is the intersection of
its assigned role descriptors and the owner user's role descriptors
(effectively limited by it). An API key must have `manage_api_key` or higher privileges to retrieve the limited-by role descriptors of any API key, including itself.

`with_profile_uid`::
(Optional, boolean) Determines whether to also retrieve the user profile `uid`, for the API key owner user.
If it exists, the profile uid is returned under the `profile_uid` response field for each API key.
Defaults to `false`.

`active_only`::
(Optional, Boolean) A boolean flag that can be used to query API keys that are currently active.
An API key is considered active if it is neither invalidated, nor expired at query time. You can specify this together
with other parameters such as `owner` or `name`.  If `active_only` is `false`, the response will
include both active and inactive (expired or invalidated) keys. Defaults to `false`.

**Note:** When none of the parameters "id", "name", "username" and "realm_name"
are specified, and the "owner" is set to false then it will retrieve all API
keys if the user is authorized. If the user is not authorized to retrieve other user's
API keys, then an error will be returned.

#### Examples

If you create an API key as follows:

```console
POST /_security/api_key
{
  "name": "my-api-key",
  "role_descriptors": {},
  "metadata": {
    "application": "myapp"
  }
}
```

A successful call returns a JSON structure that provides
API key information. For example:

```console-result
{
  "id":"VuaCfGcBCdbkQm-e5aOx",
  "name":"my-api-key",
  "api_key":"ui2lp2axTNmsyakw9tvNnw",
  "encoded": "VnVhQ2ZHY0JDZGJrUW0tZTVhT3g6dWkybHAyYXhUTm1zeWFrdzl0dk5udw=="
}
```

You can use the following example to retrieve the API key by ID:

```console
GET /_security/api_key?id=VuaCfGcBCdbkQm-e5aOx&with_limited_by=true
```

A successful call returns a JSON structure that contains the information of the API key:

```js
{
  "api_keys": [ <1>
    {
      "id": "VuaCfGcBCdbkQm-e5aOx", <2>
      "name": "my-api-key", <3>
      "creation": 1548550550158, <4>
      "expiration": 1548551550158, <5>
      "invalidated": false, <6>
      "username": "myuser", <7>
      "realm": "native1", <8>
      "realm_type": "native",
      "metadata": { <9>
        "application": "myapp"
      },
      "role_descriptors": { }, <10>
      "limited_by": [  <11>
        {
          "role-power-user": {
            "cluster": [
              "monitor"
            ],
            "indices": [
              {
                "names": [
                  "*"
                ],
                "privileges": [
                  "read"
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
        }
      ]
    }
  ]
}
```
<1> The list of API keys that were retrieved for this request.
<2> Id for the API key
<3> Name of the API key
<4> Creation time for the API key in milliseconds
<5> Optional expiration time for the API key in milliseconds
<6> Invalidation status for the API key. If the key has been invalidated, it has
a value of `true` and an additional field with the `invalidation` time in milliseconds. Otherwise, it is `false`.
<7> Principal for which this API key was created
<8> Realm name of the principal for which this API key was created
<9> Metadata of the API key
<10> The role descriptors assigned to this API key when it was created
or last updated.
An empty role descriptor means the API key inherits the owner user's
permissions.
<11> The owner user's permissions associated with the API key.
It is a point-in-time snapshot captured at creation and
subsequent updates. An API key's
effective permissions are an intersection of its assigned privileges and
the owner user's permissions.

You can use the following example to retrieve the API key by name:

```console
GET /_security/api_key?name=my-api-key
```

API key name supports prefix search by using wildcard:

```console
GET /_security/api_key?name=my-*
```

The following example retrieves all API keys for the `native1` realm:

```console
GET /_security/api_key?realm_name=native1
```

The following example retrieves all API keys for the user `myuser` in all realms:

```console
GET /_security/api_key?username=myuser
```

The following example retrieves all API keys owned by the currently authenticated user:

```console
GET /_security/api_key?owner=true
```

The following example retrieves all API keys if the user is authorized to do so:
```console
GET /_security/api_key
```

The following example retrieves all active API keys if the user is authorized to do so:
```console
GET /_security/api_key?active_only=true
```

Following creates an API key

```console
POST /_security/api_key
{
  "name": "my-api-key-1",
  "metadata": {
    "application": "my-application"
  }
}
```

The following example retrieves the API key identified by the specified `id` if
it is owned by the currently authenticated user:

```console
GET /_security/api_key?id=VuaCfGcBCdbkQm-e5aOx&owner=true
```

Finally, the following example retrieves all API keys for the user `myuser` in
 the `native1` realm immediately:

```console
GET /_security/api_key?username=myuser&realm_name=native1
```

A successful call returns a JSON structure that contains the information of one or more API keys that were retrieved.

```js
{
  "api_keys": [
    {
      "id": "0GF5GXsBCXxz2eDxWwFN",
      "name": "hadoop_myuser_key",
      "creation": 1548550550158,
      "expiration": 1548551550158,
      "invalidated": false,
      "username": "myuser",
      "realm": "native1",
      "realm_type": "native",
      "metadata": {
        "application": "myapp"
      },
      "role_descriptors": {
        "role-a": {
          "cluster": [
            "monitor"
          ],
          "indices": [
            {
              "names": [
                "index-a"
              ],
              "privileges": [
                "read"
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
      }
    },
    {
      "id": "6wHJmcQpReKBa42EHV5SBw",
      "name": "api-key-name-2",
      "creation": 1548550550158,
      "invalidated": false,
      "username": "user-y",
      "realm": "realm-2",
      "metadata": {},
      "role_descriptors": { }
    }
  ]
}
```
