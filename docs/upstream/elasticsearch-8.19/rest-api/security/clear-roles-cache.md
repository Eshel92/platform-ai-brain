<!-- Converted from rest-api/security/clear-roles-cache.asciidoc (AsciiDoc). Includes are inlined. -->

### Clear roles cache API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Evicts roles from the native role cache. 

#### Request

`POST /_security/role/<roles>/_clear_cache` 

#### Prerequisites

* To use this API, you must have at least the `manage_security` cluster
privilege.

#### Description

For more information about the native realm, see 
realms and native-realm. 

#### Path parameters

`<roles>`::
(Required, string)
Comma-separated list of roles to evict from the role cache. To evict all
roles, use `*`. Does not support other wildcard patterns.

#### Examples

The clear roles cache API evicts roles from the native role cache. For example, 
to clear the cache for `my_admin_role`:

```console
POST /_security/role/my_admin_role/_clear_cache
```

Specify multiple roles as a comma-separated list.

```console
POST /_security/role/my_admin_role,my_test_role/_clear_cache
```

To clear all roles from the cache, use `*`.

```console
POST /_security/role/*/_clear_cache
```
