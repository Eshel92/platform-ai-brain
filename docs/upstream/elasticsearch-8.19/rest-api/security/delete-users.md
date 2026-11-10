<!-- Converted from rest-api/security/delete-users.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete users API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Deletes users from the native realm. 

#### Request

`DELETE /_security/user/<username>` 

#### Prerequisites

* To use this API, you must have at least the `manage_security` cluster privilege.

#### Description

For more information about the native realm, see 
realms and native-realm. 

#### Path parameters

`username`::
  (Required, string) An identifier for the user. 

#### Examples

The following example deletes the user `jacknich`:

```console
DELETE /_security/user/jacknich
```

If the user is successfully deleted, the request returns `{"found": true}`.
Otherwise, `found` is set to false.

```console-result
{
  "found" : true
}
```
