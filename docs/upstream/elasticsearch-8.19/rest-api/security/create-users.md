<!-- Converted from rest-api/security/create-users.asciidoc (AsciiDoc). Includes are inlined. -->

### Create or update users API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Adds and updates users in the native realm. These users are commonly referred
to as _native users_.

#### Request

`POST /_security/user/<username>` +

`PUT /_security/user/<username>`

#### Prerequisites

* To use this API, you must have at least the `manage_security` cluster privilege.

#### Description

A `password` is required for adding a new user but is optional when updating an
existing user. To change a user's password without updating any other fields,
use the change password API.

For more information about the native realm, see
realms and native-realm.

#### Path parameters

`username`::
  (Required, string) An identifier for the user.
**Note:** Usernames must be at least 1 and no more than 507 characters. They can
contain alphanumeric characters (`a-z`, `A-Z`, `0-9`), spaces, punctuation, and
printable symbols in the [Basic Latin (ASCII) block](https://en.wikipedia.org/wiki/Basic_Latin_(Unicode_block)). Leading or trailing whitespace is not allowed.

#### Query parameters

`refresh`::
    (string) One of `true`, `false`, or `wait_for`.
    These values have the same meaning as in the Index API,
    but the default value for this API (Put User) is `true`.

#### Request body

The following parameters can be specified in the body of a POST or PUT request:

`enabled`::
(Boolean) Specifies whether the user is enabled. The default value is `true`.

`email`::
(string) The email of the user.

`full_name`::
(string) The full name of the user.

`metadata`::
(object) Arbitrary metadata that you want to associate with the user.

`password`::
(Required*, string) The user's password. Passwords must be at least 6 characters long.
When adding a user, one of `password` or `password_hash` is required.
When updating an existing user, the password is optional, so that other
fields on the user (such as their roles) may be updated without modifying
the user's password.

`password_hash`::
(string) A _hash_ of the user's password. This must be produced using the
same hashing algorithm as has been configured for password storage. For more
details, see the explanation of the
`xpack.security.authc.password_hashing.algorithm` setting in
hashing-settings.
Using this parameter allows the client to pre-hash the password for
performance and/or confidentiality reasons.
The `password` parameter and the `password_hash` parameter cannot be
used in the same request.

`roles`::
(Required, list) A set of roles the user has. The roles determine the user's
access permissions. To create a user without any roles, specify an empty list:
`[]`.

*Indicates that the setting is required in some, but not all situations.

#### Examples

The following example creates a user `jacknich`:

```console
POST /_security/user/jacknich
{
  "password" : "l0ng-r4nd0m-p@ssw0rd",
  "roles" : [ "admin", "other_role1" ],
  "full_name" : "Jack Nicholson",
  "email" : "jacknich@example.com",
  "metadata" : {
    "intelligence" : 7
  }
}
```

A successful call returns a JSON structure that shows whether the user has been
created or updated.

```console-result
{
  "created": true <1>
}
```

<1> When an existing user is updated, `created` is set to false.

After you add a user, requests from that user can be authenticated. For example:

```shell
curl -u jacknich:l0ng-r4nd0m-p@ssw0rd http://localhost:9200/_cluster/health
```
