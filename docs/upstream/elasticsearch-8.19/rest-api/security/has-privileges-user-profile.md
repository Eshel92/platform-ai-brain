<!-- Converted from rest-api/security/has-privileges-user-profile.asciidoc (AsciiDoc). Includes are inlined. -->

### Has privileges user profile API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

**Note:** The user profile feature is designed only for use by Kibana and
Elastic’s Observability, {ents}, and Elastic Security solutions. Individual
users and external applications should not call this API directly. Elastic reserves
the right to change or remove this feature in future releases without prior notice.

Determines whether the users associated with the specified user profile IDs
have all the requested privileges.

#### Request

`GET /_security/profile/_has_privileges`

`POST /_security/profile/_has_privileges`

#### Prerequisites

To use this API, you must have _at least_ the `read_security`
cluster privilege (or a greater privilege
such as `manage_user_profile` or `manage_security`).

#### Description

This API uses the profile IDs, as returned by security-api-activate-user-profile,
to identify the users for which to check the privileges of.
It is similar to the security-api-has-privileges API, but unlike it, this API
checks the privileges of other users, not of the user that's calling it.

See security-privileges for the list of privileges that can be specified in this API.

A successful call returns the subset list of profile IDs that have **all** the requested privileges.

#### Request body

`uids`:: (list) A list of profile IDs. The privileges are checked for associated users of the profiles.

`privileges`:: The object containing all the privileges to be checked.
`cluster`::: (list) A list of the cluster privileges that you want to check.
`index`:::
`names`:::: (list) A list of indices.
`allow_restricted_indices`:::: (Boolean) This needs to be set to `true` (default
is `false`) if using wildcards or regexps for patterns that cover restricted
indices. Implicitly, restricted indices do not match index patterns because
restricted indices usually have limited privileges and including them in
pattern tests would render most such tests `false`. If restricted indices are
explicitly included in the `names` list, privileges will be checked against
them regardless of the value of `allow_restricted_indices`.
`privileges`:::: (list) A list of the privileges that you want to check for the
specified indices.
`application`:::
`application`:::: (string) The name of the application.
`privileges`:::: (list) A list of the privileges that you want to check for the
specified resources. May be either application privilege names, or the names of
actions that are granted by those privileges.
`resources`:::: (list) A list of resource names against which the privileges
should be checked.

Note that the `privileges` section above is identical to the
request body of the other Has Privileges API.

#### Response body

A successful has privileges user profile API call returns a JSON structure that contains
two fields:

`has_privilege_uids`:: (list) The subset of the requested profile IDs of the users that have
**all** the requested privileges.

`errors`:: (object) Errors encountered while fulfilling the request. This field is absent if there is no error.
It does **not** include the profile IDs of the users that do not have all the requested privileges.
**Properties of objects in `errors`**
`count`:: (number) Total number of errors

`details`:: (object) The detailed error report with keys being profile IDs and values being the exact errors.

#### Examples

The following example checks whether the two users associated with the specified profiles have all the
requested set of cluster, index, and application privileges:

```console
POST /_security/profile/_has_privileges
{
  "uids": [
    "u_LQPnxDxEjIH0GOUoFkZr5Y57YUwSkL9Joiq-g4OCbPc_0",
    "u_rzRnxDgEHIH0GOUoFkZr5Y27YUwSk19Joiq=g4OCxxB_1",
    "u_does-not-exist_0"
  ],
  "privileges": {
    "cluster": [ "monitor", "create_snapshot", "manage_ml" ],
    "index" : [
      {
        "names": [ "suppliers", "products" ],
        "privileges": [ "create_doc"]
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
}
```

The following example output indicates that only one of the three users has all the privileges
and one of them is not found:

```js
{
  "has_privilege_uids": ["u_rzRnxDgEHIH0GOUoFkZr5Y27YUwSk19Joiq=g4OCxxB_1"],
  "errors": {
    "count": 1,
    "details": {
      "u_does-not-exist_0": {
        "type": "resource_not_found_exception",
        "reason": "profile document not found"
      }
    }
  }
}
```
