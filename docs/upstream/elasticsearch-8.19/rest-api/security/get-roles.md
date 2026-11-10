<!-- Converted from rest-api/security/get-roles.asciidoc (AsciiDoc). Includes are inlined. -->

### Get roles API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Retrieves roles in the native realm.

#### Request

`GET /_security/role` +

`GET /_security/role/<name>` +

#### Prerequisites

* To use this API, you must have at least the `read_security` cluster privilege.

#### Description

The role management APIs are generally the preferred way to manage roles, rather than using
file-based role management. The get roles
API cannot retrieve roles that are defined in roles files.

#### Path parameters

`name`::
  (Optional, string) The name of the role. You can specify multiple roles as a
  comma-separated list. If you do not specify this parameter, the API
  returns information about all roles.

#### Response body

A successful call returns an array of roles with the JSON representation of the
role. The returned role format is a simple extension of the role definition format,
only adding an extra field `transient_metadata.enabled`.
This field is `false` in case the role is automatically disabled, for example when the license
level does not allow some permissions that the role grants.

#### Response codes

If the role is not defined in the native realm, the request returns 404.

#### Examples

The following example retrieves information about the `my_admin_role` role in
the native realm:

```console
GET /_security/role/my_admin_role
```

```console-result
{
  "my_admin_role": {
    "description": "Grants full access to all management features within the cluster.",
    "cluster" : [ "all" ],
    "indices" : [
      {
        "names" : [ "index1", "index2" ],
        "privileges" : [ "all" ],
        "allow_restricted_indices" : false,
        "field_security" : {
          "grant" : [ "title", "body" ]}
      }
    ],
    "applications" : [ ],
    "run_as" : [ "other_user" ],
    "metadata" : {
      "version" : 1
    },
    "transient_metadata": {
      "enabled": true
    }
  }
}
```

To retrieve all roles, omit the role name:

```console
GET /_security/role
```
