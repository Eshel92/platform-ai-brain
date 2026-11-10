<!-- Converted from rest-api/security/clear-service-token-caches.asciidoc (AsciiDoc). Includes are inlined. -->

### Clear service account token caches API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Evicts a subset of all entries from the  service account
token caches.

#### Request

`POST /_security/service/{namespace}/{service}/credential/token/{token_name}/_clear_cache`

#### Prerequisites

* To use this API, you must have at least the `manage_security`
cluster privilege.

#### Description

Two, separate caches exist for service account tokens: one cache for tokens
backed by the `service_tokens` file, and another for tokens backed by the
`.security` index. This API clears matching entries from both caches.

The cache for service account tokens backed by the `.security` index is cleared
automatically on state changes of the security index. The cache for tokens
backed by the `service_tokens` file is cleared automatically on file changes.

See Service accounts for more information.

#### Path parameters

`namespace`::
(Required, string) Name of the namespace.

`service`::
(Required, string) Name of the service name.

`token_name`::
(Required, string) Comma-separated list of token names to evict from the
service account token caches. Use a wildcard (`*`) to evict all tokens that
belong to a service account. Does not support other wildcard patterns.

#### Examples

The following request clears the service account token cache for the `token1`
token:

```console
POST /_security/service/elastic/fleet-server/credential/token/token1/_clear_cache
```

Specify multiple token names as a comma-separated list:

```console
POST /_security/service/elastic/fleet-server/credential/token/token1,token2/_clear_cache
```

To clear all entries from the service account token caches, use a wildcard
(`*`) in place of token names:

```console
POST /_security/service/elastic/fleet-server/credential/token/*/_clear_cache
```
