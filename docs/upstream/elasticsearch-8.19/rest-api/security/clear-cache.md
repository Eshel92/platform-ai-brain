<!-- Converted from rest-api/security/clear-cache.asciidoc (AsciiDoc). Includes are inlined. -->

### Clear cache API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Evicts users from the user cache. You can completely clear
the cache or evict specific users.

#### Request

`POST /_security/realm/<realms>/_clear_cache` +

`POST /_security/realm/<realms>/_clear_cache?usernames=<usernames>`

#### Description

User credentials are cached in memory on each node to avoid connecting to a
remote authentication service or hitting the disk for every incoming request.
There are realm settings that you can use to configure the user cache. For more
information, see
controlling-user-cache.

To evict roles from the role cache, see the
Clear roles cache API.
To evict privileges from the privilege cache, see the
Clear privileges cache API.
To evict API keys from the API key cache, see the
Clear API key cache API.

#### Path parameters

`<realms>`::
(Required, string)
Comma-separated list of realms to clear. To clear all realms, use `*`. Does not
support other wildcard patterns.

`usernames`::
  (Optional, list) A comma-separated list of the users to clear from the cache.
  If you do not specify this parameter, the API evicts all users from the user
  cache.

#### Examples

For example, to evict all users cached by the `file` realm:

```console
POST /_security/realm/default_file/_clear_cache
```

To evict selected users, specify the `usernames` parameter:

```console
POST /_security/realm/default_file/_clear_cache?usernames=rdeniro,alpacino
```

To clear the caches for multiple realms, specify the realms as a comma-delimited
list:

```console
POST /_security/realm/default_file,ldap1/_clear_cache
```

To clear the caches for all realms, use `*`.

```console
POST /_security/realm/*/_clear_cache
```
