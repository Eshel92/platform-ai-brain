<!-- Converted from rest-api/security/disable-users.asciidoc (AsciiDoc). Includes are inlined. -->

### Disable users API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Disables users in the native realm. 

#### Request

`PUT /_security/user/<username>/_disable` 

#### Prerequisites

* To use this API, you must have at least the `manage_security` cluster privilege.

#### Description

By default, when you create users, they are enabled. You can use this API to 
revoke a user's access to Elasticsearch. To re-enable a user, there is an 
enable users API. 

For more information about the native realm, see 
realms and native-realm. 

#### Path parameters

`username`::
  (Required, string) An identifier for the user.

#### Examples

The following example disables the user `jacknich`:

```console
PUT /_security/user/jacknich/_disable
```
