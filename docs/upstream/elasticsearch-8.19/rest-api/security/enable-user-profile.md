<!-- Converted from rest-api/security/enable-user-profile.asciidoc (AsciiDoc). Includes are inlined. -->

### Enable user profile API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

**Note:** The user profile feature is designed only for use by Kibana and
Elastic’s Observability, {ents}, and Elastic Security solutions. Individual
users and external applications should not call this API directly. Elastic reserves
the right to change or remove this feature in future releases without prior notice.

Enables a user profile so it's visible in
user profile searches.

#### Request

`POST /_security/profile/<uid>/_enable`

`PUT /_security/profile/<uid>/_enable`

#### Prerequisites

To use this API, you must have the `manage_user_profile` cluster privilege.

#### Description

When you activate a user profile, it's
automatically enabled and visible in user profile searches. If you later
disable the user profile, you can use the
enable user profile API to make the profile visible in these searches again.

#### Path parameters

`<uid>`::
(Required, string) Unique identifier for the user profile.

#### Query parameters

`refresh`::
(Optional, enum) If `true`, Elasticsearch refreshes the affected shards to make this
operation visible to search, if `wait_for` then wait for a refresh to make
this operation visible to search, if `false` do nothing with refreshes.
Valid values: `true`, `false`, `wait_for`. Default: `false`.

#### Examples

The following request enables the user profile for a `uid` matching
`u_79HkWkwmnBH5gqFKwoxggWPjEBOur1zLPXQPEl1VBW0_0`:

```console
POST /_security/profile/u_79HkWkwmnBH5gqFKwoxggWPjEBOur1zLPXQPEl1VBW0_0/_enable
```
