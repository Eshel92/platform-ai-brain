<!-- Converted from rest-api/security/get-users.asciidoc (AsciiDoc). Includes are inlined. -->

### Get users API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Retrieves information about users in the native realm and built-in users.

#### Request

`GET /_security/user` +

`GET /_security/user/<username>`

#### Prerequisites

* To use this API, you must have at least the `read_security` cluster privilege.

#### Description

For more information about the native realm, see
realms and native-realm.

#### Path parameters

`username`::
  (Optional, string) An identifier for the user. You can specify multiple
  usernames as a comma-separated list. If you omit this parameter, the API
  retrieves information about all users.

#### Query parameters

`with_profile_uid`::
(Optional, boolean) Determines whether to retrieve the user profile `uid`,
if exists, for the users. Defaults to `false`.

#### Response body

A successful call returns an array of users with the JSON representation of the
users. Note that user passwords are not included.

#### Response codes

If the user is not defined in the `native` realm, the request 404s.

#### Examples

To retrieve a native user, submit a GET request to the `/_security/user/<username>`
endpoint:

```console
GET /_security/user/jacknich
```

```console-result
{
  "jacknich": {
    "username": "jacknich",
    "roles": [
      "admin", "other_role1"
    ],
    "full_name": "Jack Nicholson",
    "email": "jacknich@example.com",
    "metadata": { "intelligence" : 7 },
    "enabled": true
  }
}
```

To retrieve the user `profile_uid` as part of the response:

```console
GET /_security/user/jacknich?with_profile_uid=true
```

```console-result
{
  "jacknich": {
    "username": "jacknich",
    "roles": [
      "admin", "other_role1"
    ],
    "full_name": "Jack Nicholson",
    "email": "jacknich@example.com",
    "metadata": { "intelligence" : 7 },
    "enabled": true,
    "profile_uid": "u_79HkWkwmnBH5gqFKwoxggWPjEBOur1zLPXQPEl1VBW0_0"
  }
}
```

Omit the username to retrieve all users:

```console
GET /_security/user
```
