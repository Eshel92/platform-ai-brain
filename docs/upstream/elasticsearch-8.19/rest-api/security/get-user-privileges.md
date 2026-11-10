<!-- Converted from rest-api/security/get-user-privileges.asciidoc (AsciiDoc). Includes are inlined. -->

### Get user privileges API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Retrieves the security privileges for the logged in 
user.

#### Request

`GET /_security/user/_privileges`

#### Prerequisites

* All users can use this API, but only to determine their own privileges. To 
check the privileges of other users, you must use the run as feature. For
more information, see run-as-privilege.

#### Description

To check whether a user has a specific list of privileges, use the
has privileges API.

#### Examples

```console
GET /_security/user/_privileges
```

```console-result
{
  "cluster" : [
    "all"
  ],
  "global" : [ ],
  "indices" : [
    {
      "names" : [
        "*"
      ],
      "privileges" : [
        "all"
      ],
      "allow_restricted_indices" : true
    }
  ],
  "applications" : [
    {
      "application" : "*",
      "privileges" : [
        "*"
      ],
      "resources" : [
        "*"
      ]
    }
  ],
  "run_as" : [
    "*"
  ]
}
```
