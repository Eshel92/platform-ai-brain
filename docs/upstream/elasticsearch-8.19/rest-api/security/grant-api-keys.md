<!-- Converted from rest-api/security/grant-api-keys.asciidoc (AsciiDoc). Includes are inlined. -->

### Grant API key API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Creates an API key on behalf of another user.

#### Request

`POST /_security/api_key/grant`

#### Prerequisites

* To use this API, you must have the `grant_api_key` or the `manage_api_key` cluster privilege.

#### Description

This API is similar to security-api-create-api-key, however it creates the
API key for a user that is different than the user that runs the API.

The caller must have authentication credentials for the user on whose behalf
the API key will be created. It is not possible to use this API to create an
API key without that user's credentials.
The supported user authentication credentials types are:
 * username and password
 * Elasticsearch access tokens
 * JWTs

The user, for whom the authentication credentials is provided,
can optionally "run as" (impersonate) another user.
In this case, the API key will be created on behalf of the impersonated user.

This API is intended be used by applications that need to create and manage
API keys for end users, but cannot guarantee that those users have permission
to create API keys on their own behalf (see security-api-create-api-key-prereqs).
The API keys are created by the Elasticsearch API key service, which is automatically
enabled.

A successful grant API key API call returns a JSON structure that contains the
API key, its unique id, and its name. If applicable, it also returns expiration
information for the API key in milliseconds.

**Note:** By default, API keys never expire. You can specify expiration information
when you create the API keys.

See api-key-service-settings for configuration settings related to API key
service.

#### Request body

The following parameters can be specified in the body of a POST request:

`access_token`::
(Required*, string)
The user's Elasticsearch access token, or JWT. Both access and
id JWT token types are supported, and they depend on the underlying JWT realm configuration.
The created API key will have a point in time snapshot of permissions of the user authenticated with this token
(or even more restricted permissions, see the `role_descriptors` parameter).
If you specify the `access_token` grant type, this parameter is required. It is not valid with other grant types.

`api_key`::
(Required, object)
Defines the API key.

`expiration`:::
(Optional, string) Expiration time for the API key. By default, API keys never
expire.

`name`:::
(Required, string) Specifies the name for this API key.

`role_descriptors`:::
(Optional, object) The role descriptors for this API
key. This parameter is optional. When it is not specified or is an empty array,
the API key has a point in time snapshot of permissions of the specified user or
access token. If you supply role descriptors, the resultant permissions are an
intersection of API keys permissions and the permissions of the user or access
token. The structure of a role descriptor is the same as the request for create API keys API.

`metadata`:::
(Optional, object) Arbitrary metadata that you want to associate with the API key.
It supports nested data structure.
Within the `metadata` object, keys beginning with `_` are reserved for
system usage.

`client_authentication`::
(Optional, object) When using the `access_token` grant type, and when supplying a
JWT, this specifies the client authentication for JWTs that
need it (i.e. what's normally specified by the `ES-Client-Authentication` request header).

`scheme`:::
(Required, string) The scheme (case-sensitive) as it's supplied in the
`ES-Client-Authentication` request header. Currently, the only supported
value is `SharedSecret`.

`value`:::
(Required, string) The value that follows the scheme for the client credentials
as it's supplied in the `ES-Client-Authentication` request header. For example,
if the request header would be `ES-Client-Authentication: SharedSecret myShar3dS3cret`
if the client were to authenticate directly with a JWT, then `value` here should
be `myShar3dS3cret`.
`grant_type`::
(Required, string)
The type of grant. Supported grant types are: `access_token`,`password`.

`access_token`:::
In this type of grant, you must supply either an access token, that was created by the
Elasticsearch token service (see security-api-get-token and encrypt-http-communication),
or a JWT (either a JWT `access_token` or a JWT `id_token`).

`password`:::
In this type of grant, you must supply the user ID and password for which you
want to create the API key.

`password`::
(Required*, string)
The user's password. If you specify the `password` grant type, this parameter is
required. It is not valid with other grant types.

`username`::
(Required*, string)
The user name that identifies the user. If you specify the `password` grant type,
this parameter is required. It is not valid with other grant types.

`run_as`::
(Optional, string)
The name of the user to be impersonated.

*Indicates that the setting is required in some, but not all situations.

#### Examples

```console
POST /_security/api_key/grant
{
  "grant_type": "password",
  "username" : "test_admin",
  "password" : "x-pack-test-password",
  "api_key" : {
    "name": "my-api-key",
    "expiration": "1d",
    "role_descriptors": {
      "role-a": {
        "cluster": ["all"],
        "indices": [
          {
          "names": ["index-a*"],
          "privileges": ["read"]
          }
        ]
      },
      "role-b": {
        "cluster": ["all"],
        "indices": [
          {
          "names": ["index-b*"],
          "privileges": ["all"]
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
}
```

The user (`test_admin`) whose credentials are provided can "run as" another user (`test_user`).
The API key will be granted to the impersonated user (`test_user`).

```console
POST /_security/api_key/grant
{
  "grant_type": "password",
  "username" : "test_admin",  <1>
  "password" : "x-pack-test-password",  <2>
  "run_as": "test_user",  <3>
  "api_key" : {
    "name": "another-api-key"
  }
}
```
<1> The user for which the credential is provided and performs "run as".
<2> Credential for the above user
<3> The impersonated user for whom the API key will be created for.
