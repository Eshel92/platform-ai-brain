<!-- Converted from rest-api/security/delete-role-mappings.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete role mappings API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Removes role mappings.

#### Request

`DELETE /_security/role_mapping/<name>` 

#### Prerequisites

* To use this API, you must have at least the `manage_security` cluster privilege.

#### Description

Role mappings define which roles are assigned to each user. For more information, 
see mapping-roles.

The role mapping APIs are generally the preferred way to manage role mappings
rather than using role mapping files.
The delete role mappings API cannot remove role mappings that are defined
in role mapping files.

#### Path parameters

`name`::
 (string) The distinct name that identifies the role mapping. The name is
  used solely as an identifier to facilitate interaction via the API; it does
  not affect the behavior of the mapping in any way.

#### Examples

The following example delete a role mapping:

```console
DELETE /_security/role_mapping/mapping1
```

If the mapping is successfully deleted, the request returns `{"found": true}`.
Otherwise, `found` is set to false.

```console-result
{
  "found" : true
}
```
