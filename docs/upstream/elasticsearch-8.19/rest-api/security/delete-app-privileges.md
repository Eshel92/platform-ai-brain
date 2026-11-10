<!-- Converted from rest-api/security/delete-app-privileges.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete application privileges API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Removes application privileges.

#### Request

`DELETE /_security/privilege/<application>/<privilege>`

#### Prerequisites

To use this API, you must have either:

- the `manage_security` cluster privilege (or a greater privilege such as `all`); _or_
- the _"Manage Application Privileges"_ global privilege for the application being referenced
  in the request

#### Path parameters

`application`::
  (Required, string) The name of the application. Application privileges are
  always associated with exactly one application.

`privilege`::
  (Required, string) The name of the privilege.

#### Examples

The following example deletes the `read` application privilege from the
`myapp` application:

```console
DELETE /_security/privilege/myapp/read
```

If the privilege is successfully deleted, the request returns `{"found": true}`.
Otherwise, `found` is set to false.

```console-result
{
  "myapp": {
    "read": {
      "found" : true
    }
  }
}
```
