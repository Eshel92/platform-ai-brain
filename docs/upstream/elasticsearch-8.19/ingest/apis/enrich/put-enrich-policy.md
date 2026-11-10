<!-- Converted from ingest/apis/enrich/put-enrich-policy.asciidoc (AsciiDoc). Includes are inlined. -->

### Create enrich policy API

For the most up-to-date API details, refer to [Enrich APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-enrich).

Creates an enrich policy.

```console
PUT /_enrich/policy/my-policy
{
  "match": {
    "indices": "users",
    "match_field": "email",
    "enrich_fields": ["first_name", "last_name", "city", "zip", "state"]
  }
}
```

#### Request

`PUT /_enrich/policy/<enrich-policy>`

#### Prerequisites

To use enrich policies, you must have:

* `read` index privileges for any indices used
* The `enrich_user` built-in role

#### Description

Use the create enrich policy API to create a enrich policy.

**Warning:**
Once created, you can't update or change an enrich policy.
Instead, you can:

. Create and execute a new enrich policy.

. Replace the previous enrich policy
    with the new enrich policy
    in any in-use enrich processors or ES|QL queries.

. Use the delete enrich policy API or
Index Management in Kibana
    to delete the previous enrich policy.

#### Path parameters

`<enrich-policy>`::
(Required, string)
Name of the enrich policy to create or update.

#### Request body

`<policy-type>`::
(Required, object)
Configures the enrich policy. The field key is the enrich policy type. Valid key
values are:
`geo_match`:::
Matches enrich data to incoming documents based on a
`geo_shape` query. For an example, see
geo-match-enrich-policy-type.

`match`:::
Matches enrich data to incoming documents based on a
`term` query. For an example, see
match-enrich-policy-type.

`range`:::
Matches a number, date, or IP address in incoming documents to a range in the
enrich index based on a `term` query. For an example,
see range-enrich-policy-type.
**Properties of `<policy-type>`**
`indices`::
(Required, String or array of strings)
One or more source indices used to create the enrich index.
If multiple indices are specified, they must share a common `match_field`.

`match_field`::
(Required, string)
Field in source indices used to match incoming documents.

`enrich_fields`::
(Required, Array of strings)
Fields to add to matching incoming documents. These fields must be present in
the source indices.

`query`::
(Optional, Query DSL query object)
Query used to filter documents in the enrich index. The policy only uses
documents matching this query to enrich incoming documents. Defaults to a
`match_all` query.
