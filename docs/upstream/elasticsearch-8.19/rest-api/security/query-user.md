<!-- Converted from rest-api/security/query-user.asciidoc (AsciiDoc). Includes are inlined. -->

### Query User API

Retrieves native users with Query DSL in a paginated fashion.

**Note:** As opposed to the get user api, built-in users are excluded from the
result. This API is only for native users.

#### Request

`GET /_security/_query/user`

`POST /_security/_query/user`

#### Prerequisites

* To use this API, you must have at least the  `read_security` cluster privilege.

#### Description

Use this API to retrieve users managed by the
native realm in a paginated manner.
You can optionally filter the results with a query.

#### Request body

You can specify the following parameters in the request body:

`query`::
(Optional, string) A query to filter which users to return.
The query supports a subset of query types, including
`match_all`, `bool`,
`term`, `terms`,
`match`, `ids`,
`prefix`, `wildcard`,
`exists`, `range`,
and `simple query string`.
You can query the following public values associated with a user.
**Valid values for `query`**
`username`::
An identifier for the user.

`roles`::
An array of the role names of the roles that are assigned to the user.

`full_name`::
Full name of the user.

`email`::
The email of the user.

`enabled`::
Specifies whether the user is enabled.

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

#### Query parameters

`with_profile_uid`::
(Optional, boolean) Determines whether to retrieve the user profile `uid`,
if exists, for the users. Defaults to `false`.

#### Response body

This API returns the following top level fields:

`total`::
The total number of users found.

`count`::
The number of users returned in the response.

`users`::
A list of users that match the query.

#### Examples

The following request lists all users, assuming you have the
`read_security` privilege:

```console
GET /_security/_query/user
```

A successful call returns a JSON structure that contains the information
retrieved from one or more users:

```console-result
{
    "total": 2,
    "count": 2,
    "users": [ <1>
        {
            "username": "jacknich",
            "roles": [
                "admin",
                "other_role1"
            ],
            "full_name": "Jack Nicholson",
            "email": "jacknich@example.com",
            "metadata": {
                "intelligence": 7
            },
            "enabled": true
        },
        {
            "username": "sandrakn",
            "roles": [
                "admin",
                "other_role1"
            ],
            "full_name": "Sandra Knight",
            "email": "sandrakn@example.com",
            "metadata": {
                "intelligence": 7
            },
            "enabled": true
        }
    ]
}
```

<1> The list of users that were retrieved for this request

If you create a user with the following details:

```console
POST /_security/user/jacknich
{
  "password" : "l0ng-r4nd0m-p@ssw0rd",
  "roles" : [ "admin", "other_role1" ],
  "full_name" : "Jack Nicholson",
  "email" : "jacknich@example.com",
  "metadata" : {
    "intelligence" : 7
  }
}
```

A successful call returns a JSON structure:

```console-result
{
  "created": true
}
```

Use the user information retrieve the user with a query:

```console
POST /_security/_query/user
{
    "query": {
        "prefix": {
            "roles": "other"
        }
    }
}
```
A successful call returns a JSON structure for a user:

```console-result
{
    "total": 1,
    "count": 1,
    "users": [
        {
            "username": "jacknich",
            "roles": [
                "admin",
                "other_role1"
            ],
            "full_name": "Jack Nicholson",
            "email": "jacknich@example.com",
            "metadata": {
                "intelligence": 7
            },
            "enabled": true
        }
    ]
}
```

To retrieve the user `profile_uid` as part of the response:

```console
POST /_security/_query/user?with_profile_uid=true
{
    "query": {
        "prefix": {
            "roles": "other"
        }
    }
}
```

```console-result
{
    "total": 1,
    "count": 1,
    "users": [
        {
            "username": "jacknich",
            "roles": [
                "admin",
                "other_role1"
            ],
            "full_name": "Jack Nicholson",
            "email": "jacknich@example.com",
            "metadata": {
                "intelligence": 7
            },
            "enabled": true,
            "profile_uid": "u_79HkWkwmnBH5gqFKwoxggWPjEBOur1zLPXQPEl1VBW0_0"
        }
    ]
}
```

Use a `bool` query to issue complex logical conditions and use
`from`, `size`, `sort` to help paginate the result:

```js
POST /_security/_query/user
{
  "query": {
    "bool": {
      "must": [
        {
          "wildcard": {
            "email": "*example.com" <1>
          }
        },
        {
          "term": {
            "enabled": true <2>
          }
        }
      ],
      "filter": [
        {
          "wildcard": {
            "roles": "*other*" <3>
          }
        }
      ]
    }
  },
  "from": 1, <4>
  "size": 2, <5>
  "sort": [
    { "username": { "order": "desc"} } <6>
  ]
}
```

<1> The email must end with `example.com`
<2> The user must be enabled
<3> The result will be filtered to only contain users with at least one role that contains the substring `other`
<4> The offset to begin the search result is the 2nd (zero-based index) user
<5> The page size of the response is 2 users
<6> The result is sorted by `username` in descending order

The response contains a list of matched users along with their sort values:

```js
{
    "total": 5,
    "count": 2,
    "users": [
        {
            "username": "ray",
            "roles": [
                "other_role3"
            ],
            "full_name": "Ray Nicholson",
            "email": "rayn@example.com",
            "metadata": {
                "intelligence": 7
            },
            "enabled": true,
            "_sort": [
                "ray" <1>
            ]
        },
        {
            "username": "lorraine",
            "roles": [
                "other_role3"
            ],
            "full_name": "Lorraine Nicholson",
            "email": "lorraine@example.com",
            "metadata": {
                "intelligence": 7
            },
            "enabled": true,
            "_sort": [
                "lorraine"
            ]
        }
    ]
}
```

<1> The sort value is `username`
