<!-- Converted from rest-api/security/clear-api-key-cache.asciidoc (AsciiDoc). Includes are inlined. -->

### Clear API key cache API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Evicts a subset of all entries from the API key cache.
The cache is also automatically cleared on state changes of the security index.

#### Request

`POST /_security/api_key/<ids>/_clear_cache`

#### Prerequisites

* To use this API, you must have at least the `manage_security` cluster
privilege.

#### Description

For more information about API keys, see security-api-create-api-key,
security-api-get-api-key, and security-api-invalidate-api-key.

#### Path parameters

`<ids>`::
(Required, string)
Comma-separated list of API key IDs to evict from the API key cache. To evict
all API keys, use `*`. Does not support other wildcard patterns.

#### Examples

The clear API key cache API evicts entries from the API key cache.
For example, to clear the entry of API key with ID `yVGMr3QByxdh1MSaicYx`.

```console
POST /_security/api_key/yVGMr3QByxdh1MSaicYx/_clear_cache
```

Specify multiple API keys as a comma-separated list.

```console
POST /_security/api_key/yVGMr3QByxdh1MSaicYx,YoiMaqREw0YVpjn40iMg/_clear_cache
```

To clear all entries from the API key cache, use `*`.

```console
POST /_security/api_key/*/_clear_cache
```
