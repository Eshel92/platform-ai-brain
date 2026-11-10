<!-- Converted from rest-api/security/query-role.asciidoc (AsciiDoc). Includes are inlined. -->

### Query Role API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Retrieves roles with Query DSL in a paginated fashion.

#### Request

`GET /_security/_query/role`

`POST /_security/_query/role`

#### Prerequisites

* To use this API, you must have at least the  `read_security` cluster privilege.

#### Description

The role management APIs are generally the preferred way to manage roles, rather than using
file-based role management.
The query roles API does not retrieve roles that are defined in `roles.yml` files.
You can optionally filter the results with a query. Also, the results can be paginated and sorted.

**Note:** This API automatically returns built-in roles as well.
The built-in roles can be filtered out by using the `metadata._reserved` field in the query.
See example below.

#### Request body

You can specify the following parameters in the request body:

`query`::
(Optional, string) A query to filter which roles to return.
The query supports a subset of query types, including
`match_all`, `bool`,
`term`, `terms`,
`match`, `ids`,
`prefix`, `wildcard`,
`exists`, `range`,
and `simple query string`.
You can query the following values associated with a role.
**Valid values for `query`**
`name`::
(keyword) The name of the role.

`description`::
(text) The description of the role.

`metadata`::
(flattened) Metadata field associated with the role, such as `metadata.app_tag`.
Note that metadata is internally indexed as a flattened field type.
This means that all sub-fields act like `keyword` fields when querying and sorting.
It also implies that it is not possible to refer to a subset of metadata fields using wildcard patterns,
e.g. `metadata.field*`, even for query types that support field name patterns.
Lastly, all the metadata fields can be searched together when simply mentioning the
`metadata` field (i.e. not followed by any dot and sub-field name).

`applications`::
The list of application privileges that the role grants.

`application`:::
(keyword) The name of the application associated to the privileges and resources.

`privileges`:::
(keyword) The names of the privileges that the role grants.

`resources`:::
(keyword) The resources to which the privileges apply.

`from`::
(Optional, integer) Starting document offset. Needs to be non-negative and defaults to `0`.
By default, you cannot page through more than 10,000 hits using the `from` and
`size` parameters. To page through more hits, use the
`search_after` parameter.

`size`::
(Optional, integer) The number of hits to return. Must not be negative and defaults to `10`.
By default, you cannot page through more than 10,000 hits using the `from` and
`size` parameters. To page through more hits, use the
`search_after` parameter.

`sort`::
(Optional, object) Sort definition. You can sort on `username`, `roles` or `enabled`.
In addition, sort can also be applied to the `_doc` field to sort by index order.

`search_after`::
(Optional, array) Search after definition.

#### Response body

This API returns the following top level fields:

`total`::
The total number of roles found.

`count`::
The number of roles returned in the response.

`roles`::
A list of roles that match the query.
The returned role format is an extension of the role definition format.
It adds the `transient_metadata.enabled` and the `_sort` fields.
`transient_metadata.enabled` is set to `false` in case the role is automatically disabled,
for example when the role grants privileges that are not allowed by the installed license.
`_sort` is present when the search query sorts on some field.
It contains the array of values that have been used for sorting.

#### Examples

The following request lists all roles (except built-in ones), sorted by the role name:

```console
POST /_security/_query/role
{
    "query": {
      "bool": {
        "must_not": {
          "term": {
            "metadata._reserved": true
          }
        }
      }
    },
    "sort": ["name"]
}
```

A successful call returns a JSON structure that contains the information
retrieved for one or more roles:

```console-result
{
    "total": 2,
    "count": 2,
    "roles": [ <1>
        {
          "name" : "my_admin_role",
          "cluster" : [
            "all"
          ],
          "indices" : [
            {
              "names" : [
                "index1",
                "index2"
              ],
              "privileges" : [
                "all"
              ],
              "field_security" : {
                "grant" : [
                  "title",
                  "body"
                ]
              },
              "allow_restricted_indices" : false
            }
          ],
          "applications" : [ ],
          "run_as" : [
            "other_user"
          ],
          "metadata" : {
            "version" : 1
          },
          "transient_metadata" : {
            "enabled" : true
          },
          "description" : "Grants full access to all management features within the cluster.",
          "_sort" : [
            "my_admin_role"
          ]
        },
        {
          "name" : "my_user_role",
          "cluster" : [ ],
          "indices" : [
            {
              "names" : [
                "index1",
                "index2"
              ],
              "privileges" : [
                "all"
              ],
              "field_security" : {
                "grant" : [
                  "title",
                  "body"
                ]
              },
              "allow_restricted_indices" : false
            }
          ],
          "applications" : [ ],
          "run_as" : [ ],
          "metadata" : {
            "version" : 1
          },
          "transient_metadata" : {
            "enabled" : true
          },
          "description" : "Grants user access to some indicies.",
          "_sort" : [
            "my_user_role"
          ]
        }
    ]
}
```

<1> The list of roles that were retrieved for this request

Similarly, the following request can be used to query only the user access role,
given its description:

```console
POST /_security/_query/role
{
  "query": {
    "match": {
      "description": {
        "query": "user access"
      }
    }
  },
  "size": 1 <1>
}
```

<1> Return only the best matching role

```console-result
{
    "total": 2,
    "count": 1,
    "roles": [
        {
          "name" : "my_user_role",
          "cluster" : [ ],
          "indices" : [
            {
              "names" : [
                "index1",
                "index2"
              ],
              "privileges" : [
                "all"
              ],
              "field_security" : {
                "grant" : [
                  "title",
                  "body"
                ]
              },
              "allow_restricted_indices" : false
            }
          ],
          "applications" : [ ],
          "run_as" : [ ],
          "metadata" : {
            "version" : 1
          },
          "transient_metadata" : {
            "enabled" : true
          },
          "description" : "Grants user access to some indicies."
        }
    ]
}
```
