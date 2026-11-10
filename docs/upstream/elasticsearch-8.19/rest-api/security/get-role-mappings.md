<!-- Converted from rest-api/security/get-role-mappings.asciidoc (AsciiDoc). Includes are inlined. -->

### Get role mappings API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Retrieves role mappings.

#### Request

`GET /_security/role_mapping` +

`GET /_security/role_mapping/<name>`

#### Prerequisites

* To use this API, you must have at least the `read_security` cluster privilege.

#### Description

Role mappings define which roles are assigned to each user. For more information,
see mapping-roles.

The role mapping APIs are generally the preferred way to manage role mappings
rather than using role mapping files.
The get role mappings API cannot retrieve role mappings that are defined
in role mapping files.

#### Path parameters

`name`::
  (Optional, string) The distinct name that identifies the role mapping. The name
  is used solely as an identifier to facilitate interaction via the API; it does
  not affect the behavior of the mapping in any way. You can specify multiple
  mapping names as a comma-separated list. If you do not specify this
  parameter, the API returns information about all role mappings.

#### Response body

A successful call retrieves an object, where the keys are the
names of the request mappings, and the values are the JSON representation of
those mappings. For more information, see
role-mapping-resources.

#### Response codes

If there is no mapping with the requested name, the
response will have status code `404`.

#### Examples

The following example retrieves information about the `mapping1` role mapping:

```console
GET /_security/role_mapping/mapping1
```

```console-result
{
  "mapping1": {
    "enabled": true,
    "roles": [
      "user"
    ],
    "rules": {
      "field": {
        "username": "*"
      }
    },
    "metadata": {}
  }
}
```
