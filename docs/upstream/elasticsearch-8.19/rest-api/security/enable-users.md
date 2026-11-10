<!-- Converted from rest-api/security/enable-users.asciidoc (AsciiDoc). Includes are inlined. -->

### Enable users API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Enables users in the native realm. 

#### Request

`PUT /_security/user/<username>/_enable` 

#### Prerequisites

* To use this API, you must have at least the `manage_security` cluster privilege.

#### Description

By default, when you create users, they are enabled. You can use this enable 
users API and the disable users API to change that attribute. 

For more information about the native realm, see 
realms and native-realm. 

#### Path parameters

`username`::
  (Required, string) An identifier for the user.

#### Examples

The following example enables the user `jacknich`:

```console
PUT /_security/user/jacknich/_enable
```
