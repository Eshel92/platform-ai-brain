<!-- Converted from rest-api/security/change-password.asciidoc (AsciiDoc). Includes are inlined. -->

### Change passwords API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Changes the passwords of users in the native realm and built-in users.

#### Request

`POST /_security/user/_password` +

`POST /_security/user/<username>/_password`

#### Prerequisites

* Every user can change their own password. Users with the `manage_security`
privilege can change passwords of other users.

#### Description

You can use the create user API to update everything
but a user's `username` and `password`. This API changes a user's password.

For more information about the native realm, see
realms and native-realm.

#### Path parameters

`username`::
  (Optional, string) The user whose password you want to change. If you do not specify
  this parameter, the password is changed for the current user.

#### Request body

`password` ::
(string) The new password value. Passwords must be at least 6 characters long.
One of `password` or `password_hash` is required.

`password_hash` ::
(string) A _hash_ of the new password value. This must be produced using the
same hashing algorithm as has been configured for password storage. For more
details, see the explanation of the
`xpack.security.authc.password_hashing.algorithm` setting in
hashing-settings.
Using this parameter allows the client to pre-hash the password for
performance and/or confidentiality reasons.
The `password` parameter and the `password_hash` parameter cannot be
used in the same request.

#### Examples

The following example updates the password for the `jacknich` user:

```console
POST /_security/user/jacknich/_password
{
  "password" : "new-test-password"
}
```

A successful call returns an empty JSON structure.

```console-result
{}
```
