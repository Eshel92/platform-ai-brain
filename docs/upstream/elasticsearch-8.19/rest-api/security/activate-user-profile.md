<!-- Converted from rest-api/security/activate-user-profile.asciidoc (AsciiDoc). Includes are inlined. -->

### Activate user profile API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

**Note:** The user profile feature is designed only for use by Kibana and
Elastic’s Observability, {ents}, and Elastic Security solutions. Individual
users and external applications should not call this API directly. Elastic reserves
the right to change or remove this feature in future releases without prior notice.

Creates or updates a user profile on behalf of another user.

#### Request

`POST /_security/profile/_activate`

#### Prerequisites

* To use this API, you must have the `manage_user_profile` cluster privilege.

#### Description

The activate user profile API creates or updates a profile document for end
users with information that is extracted from the user's authentication object,
including `username`, `full_name`, `roles`, and the authentication realm.
For example, in the JWT `access_token` case, the profile user's `username` is
extracted from the JWT token claim pointed to by the `claims.principal`
setting of the JWT realm that authenticated the token.

When updating a profile document, the API enables the document if it was
disabled. Any updates do not change existing content for either the `labels` or
`data` fields.

This API is intended only for use by applications (such as Kibana) that need to
create or update profiles for end users.

**Important:** The calling application must have either an `access_token`, or a
combination of `username` and `password` for the user that the profile document
is intended for.

#### Request body

`access_token`::
(Required*, string)
The user's Elasticsearch access token, or JWT. Both access and
id JWT token types are supported, and they depend on the underlying JWT realm configuration.
If you specify the `access_token` grant type, this parameter is required. It is not valid with other grant types.

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
The type of grant.
**Valid values for `grant_type`**
`access_token`::
In this type of grant, you must supply either an access token, that was created by the
Elasticsearch token service (see security-api-get-token and encrypt-http-communication),
or a JWT (either a JWT `access_token` or a JWT `id_token`).

`password`::
In this type of grant, you must supply the `username` and `password` for the
user that you want to create the API key for.

`password`::
(Required*, string)
The user's password. If you specify the `password` grant type, this parameter is
required. It is not valid with other grant types.

`username`::
(Required*, string)
The username that identifies the user. If you specify the `password` grant type,
this parameter is required. It is not valid with other grant types.

*Indicates that the setting is required in some, but not all situations.

#### Response body

A successful activate user profile API call returns a JSON structure that contains
the profile unique ID, user information, timestamp for the operation and version
control numbers.

#### Examples

```console
POST /_security/profile/_activate
{
  "grant_type": "password",
  "username" : "jacknich",
  "password" : "l0ng-r4nd0m-p@ssw0rd"
}
```

The API returns the following response:

```console-result
{
  "uid": "u_79HkWkwmnBH5gqFKwoxggWPjEBOur1zLPXQPEl1VBW0_0",
  "enabled": true,
  "last_synchronized": 1642650651037,
  "user": {
    "username": "jacknich",
    "roles": [
      "admin", "other_role1"
    ],
    "realm_name": "native",
    "full_name": "Jack Nicholson",
    "email": "jacknich@example.com"
  },
  "labels": {},
  "data": {},
  "_doc": {
    "_primary_term": 88,
    "_seq_no": 66
  }
}
```
