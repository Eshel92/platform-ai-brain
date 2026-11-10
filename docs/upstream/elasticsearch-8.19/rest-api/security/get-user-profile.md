<!-- Converted from rest-api/security/get-user-profile.asciidoc (AsciiDoc). Includes are inlined. -->

### Get user profiles API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

**Note:** The user profile feature is designed only for use by Kibana and
Elastic’s Observability, {ents}, and Elastic Security solutions. Individual
users and external applications should not call this API directly. Elastic reserves
the right to change or remove this feature in future releases without prior notice.

Retrieves user profiles using a list of unique profile ID.

#### Request

`GET /_security/profile/<uid>`

#### Prerequisites

To use this API, you must have _at least_ the `read_security`
cluster privilege (or a greater privilege
such as `manage_user_profile` or `manage_security`).

#### Description

The get user profile API returns the user profile document matching a specified
`uid`, which is generated when
activating a user profile.

#### Path parameters

`uid`::
(Required, string) The unique identifier for the user profile. You can specify multiple IDs as
a comma-separated list.

#### Query parameters

`data`::
(Optional, string) Comma-separated list of filters for the `data` field of
the profile document. To return all content, use `data=*`. To return a
subset of content, use `data=<key>` to retrieve the content nested under the
specified `<key>`. Defaults to returning no content.

#### Response body

A successful call returns the JSON representation of the user profile
and its internal versioning numbers. The API returns an empty object
if no profile document is found for the provided `uid`.
The content of the `data` field is not returned by default to avoid deserializing
a potential large payload.

#### Examples

```console
GET /_security/profile/u_79HkWkwmnBH5gqFKwoxggWPjEBOur1zLPXQPEl1VBW0_0
```

The API returns the following response for a `uid` matching `u_79HkWkwmnBH5gqFKwoxggWPjEBOur1zLPXQPEl1VBW0_0`:

```console-result
{
  "profiles": [
    {
      "uid": "u_79HkWkwmnBH5gqFKwoxggWPjEBOur1zLPXQPEl1VBW0_0",
      "enabled": true,
      "last_synchronized": 1642650651037,
      "user": {
        "username": "jacknich",
        "roles": [
          "admin", "other_role1"
        ],
        "realm_name": "native",
        "full_name": "Jack Nicholson",
        "email": "jacknich@example.com"
      },
      "labels": {
        "direction": "north"
      },
      "data": {}, <1>
      "_doc": {
        "_primary_term": 88,
        "_seq_no": 66
      }
    }
  ]
}
```

<1> No content is returned in the `data` field by default.

The following request retrieves a subset of `data` that's nested under the
key `app1`, along with the user's profile:

```console
GET /_security/profile/u_79HkWkwmnBH5gqFKwoxggWPjEBOur1zLPXQPEl1VBW0_0?data=app1.key1
```

```console-result
{
  "profiles": [
    {
      "uid": "u_79HkWkwmnBH5gqFKwoxggWPjEBOur1zLPXQPEl1VBW0_0",
      "enabled": true,
      "last_synchronized": 1642650651037,
      "user": {
        "username": "jacknich",
        "roles": [
          "admin", "other_role1"
        ],
        "realm_name": "native",
        "full_name": "Jack Nicholson",
        "email": "jacknich@example.com"
      },
      "labels": {
        "direction": "north"
      },
      "data": {
        "app1": {
          "key1": "value1"
        }
      },
      "_doc": {
        "_primary_term": 88,
        "_seq_no": 66
      }
    }
  ]
}
```

If there has been any errors when retrieving the user profiles, they are returned in the `errors` field:

```js
{
  "profiles": [],
  "errors": {
    "count": 1,
    "details": {
       "u_FmxQt3gr1BBH5wpnz9HkouPj3Q710XkOgg1PWkwLPBW_5": {
         "type": "resource_not_found_exception",
         "reason": "profile document not found"
       }
    }
  }
}
```
