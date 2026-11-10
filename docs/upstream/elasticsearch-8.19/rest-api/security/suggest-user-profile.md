<!-- Converted from rest-api/security/suggest-user-profile.asciidoc (AsciiDoc). Includes are inlined. -->

### Suggest user profile API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

**Note:** The user profile feature is designed only for use by Kibana and
Elastic’s Observability, {ents}, and Elastic Security solutions. Individual
users and external applications should not call this API directly. Elastic reserves
the right to change or remove this feature in future releases without prior notice.

Get suggestions for user profiles that match specified search criteria.

#### Request

`GET /_security/profile/_suggest`

`POST /_security/profile/_suggest`

#### Prerequisites

To use this API, you must have _at least_ the `read_security`
cluster privilege (or a greater privilege
such as `manage_user_profile` or `manage_security`).

#### Query parameters

`data`::
(Optional, string) Comma-separated list of filters for the `data` field of
the profile document. To return all content, use `data=*`. To return a
subset of content, use `data=<key>` to retrieve the content nested under the
specified `<key>`. Defaults to returning no content.

#### Request body

`name`::
(Optional, string)
Query string used to match name-related fields in user profile documents. Name-related fields are the user's `username`, `full_name` and `email`.

`size`::
(Optional, integer)
Number of profiles to return. Defaults to `10`.

`data`::
(Optional, string)
Comma-separated list of filters for the `data` field of
the profile document. It works the same way as the `data` query parameter.

**Note:** It is an error to specify `data` as both the query parameter and the request body field.

`hint`::
(Optional, object)
Extra search criteria to improve relevance of the suggestion result.
A profile matching the specified hint is ranked higher in the response.
But not-matching the hint does not exclude a profile from the response
as long as it matches the `name` field query.
**Properties of `hint`:**
`uids`::
(Optional, list of strings)
A list of Profile UIDs to match against.

`labels`::
(Optional, object)
A single key-value pair to match against the `labels` section of a profile.
The key must be a string and the value must be either a string or a list of strings.
A profile is considered matching if it matches at least one of the strings.

#### Response body

`total`::
(object)
Metadata about the number of matching profiles.

`took`::
(integer)
Milliseconds it took Elasticsearch to execute the request.

`profiles`::
(array of objects)
List of profile documents, ordered by relevance, that match the search criteria.

#### Examples

The following request get suggestions for profile documents with name-related fields
matching `jack`. It specifies both `uids` and `labels` hints for better relevance:

```console
POST /_security/profile/_suggest
{
  "name": "jack",  <1>
  "hint": {
    "uids": [  <2>
      "u_8RKO7AKfEbSiIHZkZZ2LJy2MUSDPWDr3tMI_CkIGApU_0",
      "u_79HkWkwmnBH5gqFKwoxggWPjEBOur1zLPXQPEl1VBW0_0"
    ],
    "labels": {
      "direction": ["north", "east"]  <3>
    }
  }
}
```
<1> A profile's name-related fields must match `jack` for it to be included in the response.
<2> The `uids` hint include profile UIDs for both user `jackspa` and `jacknich`.
<3> The `labels` hint ranks profiles higher if their `direction` label matches either `north` or `east`.

The API returns:

```console-result
{
  "took": 30,
  "total": {
    "value": 3,
    "relation": "eq"
  },
  "profiles": [
    {
      "uid": "u_79HkWkwmnBH5gqFKwoxggWPjEBOur1zLPXQPEl1VBW0_0",
      "user": {
        "username": "jacknich",    <1>
        "roles": [ "admin", "other_role1" ],
        "realm_name": "native",
        "email" : "jacknich@example.com",
        "full_name": "Jack Nicholson"
      },
      "labels": {
        "direction": "north"
      },
      "data": {}
    },
    {
      "uid": "u_8RKO7AKfEbSiIHZkZZ2LJy2MUSDPWDr3tMI_CkIGApU_0",
      "user": {
        "username": "jackspa",    <2>
        "roles": [ "user" ],
        "realm_name": "native",
        "email" : "jackspa@example.com",
        "full_name": "Jack Sparrow"
      },
      "labels": {
        "direction": "south"
      },
      "data": {}
    },
    {
      "uid": "u_P_0BMHgaOK3p7k-PFWUCbw9dQ-UFjt01oWJ_Dp2PmPc_0",
      "user": {
        "username": "jackrea",    <3>
        "roles": [ "admin" ],
        "realm_name": "native",
        "email" : "jackrea@example.com",
        "full_name": "Jack Reacher"
      },
      "labels": {
        "direction": "west"
      },
      "data": {}
    }
  ]
}
```
<1> User `jacknich` is ranked highest because the profile matches both the `uids` and `labels` hints
<2> User `jackspa` is ranked second because the profile matches only the `uids` hint
<3> User `jackrea` is ranked lowest because the profile does not match any hints. However, it is *not*
    excluded from the response because it matches the `name` query.
