<!-- Converted from rest-api/security/update-user-profile-data.asciidoc (AsciiDoc). Includes are inlined. -->

### Update user profile data API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

**Note:** The user profile feature is designed only for use by Kibana and
Elastic’s Observability, {ents}, and Elastic Security solutions. Individual
users and external applications should not call this API directly. Elastic reserves
the right to change or remove this feature in future releases without prior notice.

Updates specific data for the user profile that's associated with the specified
unique ID.

#### Request

`POST /_security/profile/<uid>/_data`

#### Prerequisites

To use this API, you must have one of the following privileges:

* The `manage_user_profile` cluster privilege.
* The `update_profile_data` global privilege for the namespaces that are
referenced in the request.

#### Description

The update user profile API updates the `labels` and `data` fields of an
existing user profile document with JSON objects. New keys and their values are
added to the profile document, and conflicting keys are replaced by data that's
included in the request.

For both `labels` and `data`, content is namespaced by the top-level fields.
The `update_profile_data` global privilege grants privileges for updating only
the allowed namespaces.

#### Path parameters

`uid`::
(Required, string) A unique identifier for the user profile.

#### Query parameters

`if_seq_no`::
(Optional, integer) Only perform the operation if the document has this
sequence number. See optimistic-concurrency-control-index.
`if_primary_term`::
(Optional, integer) Only perform the operation if the document has
this primary term. See optimistic-concurrency-control-index.
`refresh`::
(Optional, enum) If `true`, Elasticsearch refreshes the affected shards to make this
operation visible to search, if `wait_for` then wait for a refresh to make
this operation visible to search, if `false` do nothing with refreshes.
Valid values: `true`, `false`, `wait_for`. Default: `false`.
`uid`::
(Required, string) A unique identifier for the user profile.

#### Request body

`labels`::
(Required*, object)
Searchable data that you want to associate with the user profile.
This field supports a nested data structure. Within the `labels` object,
top-level keys cannot begin with an underscore (`_`) or contain a period (`.`).

`data`::
(Required*, object)
Non-searchable data that you want to associate with the user profile.
This field supports a nested data structure. Within the `data` object, top-level
keys cannot begin with an underscore (`_`) or contain a period (`.`)
The `data` object is not searchable, but can be retrieved with the
Get user profile API.

*Indicates that the setting is required in some, but not all situations.

#### Response body

A successful update user profile data API call returns a JSON structure
indicating that the request is acknowledged:

```js
{
  "acknowledged": true
}
```

#### Examples

The following request updates a profile document for a `uid` matching
`u_P_0BMHgaOK3p7k-PFWUCbw9dQ-UFjt01oWJ_Dp2PmPc_0`:

```console
POST /_security/profile/u_P_0BMHgaOK3p7k-PFWUCbw9dQ-UFjt01oWJ_Dp2PmPc_0/_data
{
  "labels": {
    "direction": "east"
  },
  "data": {
    "app1": {
      "theme": "default"
    }
  }
}
```

You can update the profile data to replace some keys and add new keys:

```console
POST /_security/profile/u_P_0BMHgaOK3p7k-PFWUCbw9dQ-UFjt01oWJ_Dp2PmPc_0/_data
{
  "labels": {
    "direction": "west"
  },
  "data": {
    "app1": {
      "font": "large"
    }
  }
}
```

If you get the profile now, the consolidated profile data is returned:
```console
GET /_security/profile/u_P_0BMHgaOK3p7k-PFWUCbw9dQ-UFjt01oWJ_Dp2PmPc_0?data=*
```

```console-result
{
  "profiles": [
    {
      "uid": "u_P_0BMHgaOK3p7k-PFWUCbw9dQ-UFjt01oWJ_Dp2PmPc_0",
      "enabled": true,
      "last_synchronized": 1642650651037,
      "user": {
        "username": "jackrea",
        "roles": [
          "admin"
        ],
        "realm_name": "native",
        "full_name": "Jack Reacher",
        "email": "jackrea@example.com"
      },
      "labels": {
        "direction": "west"
      },
      "data": {
        "app1": {
          "theme": "default",
          "font": "large"
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
