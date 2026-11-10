<!-- Converted from rest-api/security/bulk-delete-roles.asciidoc (AsciiDoc). Includes are inlined. -->

### Bulk delete roles API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Bulk deletes roles in the native realm.

#### Request

`DELETE /_security/role/`

#### Prerequisites

* To use this API, you must have at least the `manage_security` cluster
privilege.

#### Description

The role management APIs are generally the preferred way to manage roles, rather than using
file-based role management. The bulk delete roles API cannot delete
roles that are defined in roles files.

#### Path parameters

`refresh`::
Optional setting of the [refresh policy](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-refresh.html) for the write request. Defaults to Immediate.

#### Request body

The following parameters can be specified in the body of a DELETE request
and pertain to deleting a set of roles:

`names`::
(list) A list of role names to delete.

#### Examples

The following example deletes a `my_admin_role` and `my_user_role` roles:

```console
DELETE /_security/role
{
    "names": ["my_admin_role", "my_user_role"]
}
```

If the roles are successfully deleted, the request returns:

```console-result
{
    "deleted": [
        "my_admin_role",
        "my_user_role"
    ]
}
```

If a role cannot be found, the not found roles are grouped under `not_found`:

```console
DELETE /_security/role
{
    "names": ["my_admin_role", "not_an_existing_role"]
}
```

```console-result
{
    "deleted": [
        "my_admin_role"
    ],
    "not_found": [
        "not_an_existing_role"
    ]
}
```

If a request fails or is invalid, the errors are grouped under `errors`:

```console
DELETE /_security/role
{
    "names": ["my_admin_role", "superuser"]
}
```

```console-result
{
    "deleted": [
        "my_admin_role"
    ],
    "errors": {
        "count": 1,
        "details": {
            "superuser": {
                "type": "illegal_argument_exception",
                "reason": "role [superuser] is reserved and cannot be deleted"
            }
        }
    }
}
```
