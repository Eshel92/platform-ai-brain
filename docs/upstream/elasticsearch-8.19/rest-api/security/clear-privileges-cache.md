<!-- Converted from rest-api/security/clear-privileges-cache.asciidoc (AsciiDoc). Includes are inlined. -->

### Clear privileges cache API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Evicts privileges from the native application privilege cache.
The cache is also automatically cleared for applications that have their privileges updated.

#### Request

`POST /_security/privilege/<applications>/_clear_cache`

#### Prerequisites

* To use this API, you must have at least the `manage_security` cluster
privilege.

#### Description

For more information about the native realm, see
realms and native-realm.

#### Path parameters

`<applications>`::
(Required, string)
Comma-separated list of applications to clear. To clear all applications, use
`*`. Does not support other wildcard patterns.

#### Examples

The clear privileges cache API evicts privileges from the native application privilege cache.
For example, to clear the cache for `myapp`:

```console
POST /_security/privilege/myapp/_clear_cache
```

Specify multiple applications as a comma-separated list.

```console
POST /_security/privilege/myapp,my-other-app/_clear_cache
```

To clear the cache for all applications, use `*`.

```console
POST /_security/privilege/*/_clear_cache
```
