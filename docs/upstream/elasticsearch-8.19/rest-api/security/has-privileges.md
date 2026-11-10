<!-- Converted from rest-api/security/has-privileges.asciidoc (AsciiDoc). Includes are inlined. -->

### Has privileges API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Determines whether the logged in user has a specified list of privileges.

#### Request

`GET /_security/user/_has_privileges`

`POST /_security/user/_has_privileges`

#### Prerequisites

* All users can use this API, but only to determine their own privileges.
To check the privileges of other users, you must use the run as feature. For
more information, see
run-as-privilege.

#### Description

For a list of the privileges that you can specify in this API,
see security-privileges.

A successful call returns a JSON structure that shows whether each specified
privilege is assigned to the user.

#### Request body

`cluster`:: (list) A list of the cluster privileges that you want to check.

`index`::
`names`::: (list) A list of indices.
`allow_restricted_indices`::: (Boolean) This needs to be set to `true` (default
is `false`) if using wildcards or regexps for patterns that cover restricted
indices. Implicitly, restricted indices do not match index patterns because
restricted indices usually have limited privileges and including them in
pattern tests would render most such tests `false`. If restricted indices are
explicitly included in the `names` list, privileges will be checked against
them regardless of the value of `allow_restricted_indices`.
`privileges`::: (list) A list of the privileges that you want to check for the
specified indices.

`application`::
`application`::: (string) The name of the application.
`privileges`::: (list) A list of the privileges that you want to check for the
specified resources. May be either application privilege names, or the names of
actions that are granted by those privileges
`resources`::: (list) A list of resource names against which the privileges
should be checked

#### Examples

The following example checks whether the current user has a specific set of
cluster, index, and application privileges:

```console
GET /_security/user/_has_privileges
{
  "cluster": [ "monitor", "manage" ],
  "index" : [
    {
      "names": [ "suppliers", "products" ],
      "privileges": [ "read" ]
    },
    {
      "names": [ "inventory" ],
      "privileges" : [ "read", "write" ]
    }
  ],
  "application": [
    {
      "application": "inventory_manager",
      "privileges" : [ "read", "data:write/inventory" ],
      "resources" : [ "product/1852563" ]
    }
  ]
}
```

The following example output indicates which privileges the "rdeniro" user has:

```console-result
{
  "username": "rdeniro",
  "has_all_requested" : false,
  "cluster" : {
    "monitor" : true,
    "manage" : false
  },
  "index" : {
    "suppliers" : {
      "read" : true
    },
    "products" : {
      "read" : true
    },
    "inventory" : {
      "read" : true,
      "write" : false
    }
  },
  "application" : {
    "inventory_manager" : {
      "product/1852563" : {
        "read": false,
        "data:write/inventory": false
      }
    }
  }
}
```
