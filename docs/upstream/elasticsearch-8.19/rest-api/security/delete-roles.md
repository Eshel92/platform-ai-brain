<!-- Converted from rest-api/security/delete-roles.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete roles API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Removes roles in the native realm.

#### Request

`DELETE /_security/role/<name>` 

#### Prerequisites

* To use this API, you must have at least the `manage_security` cluster privilege.

#### Description

The role management APIs are generally the preferred way to manage roles, rather than using
file-based role management. The delete roles API cannot remove roles that are defined in roles files.

#### Path parameters

`name`::
  (string) The name of the role. 

#### Examples

The following example deletes a `my_admin_role` role:

```console
DELETE /_security/role/my_admin_role
```

If the role is successfully deleted, the request returns `{"found": true}`.
Otherwise, `found` is set to false.

```console-result
{
  "found" : true
}
```
