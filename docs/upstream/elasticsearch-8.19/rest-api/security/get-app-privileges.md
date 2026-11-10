<!-- Converted from rest-api/security/get-app-privileges.asciidoc (AsciiDoc). Includes are inlined. -->

### Get application privileges API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Retrieves application privileges.

#### Request

`GET /_security/privilege` +

`GET /_security/privilege/<application>` +

`GET /_security/privilege/<application>/<privilege>`

#### Prerequisites

To use this API, you must have either:

- the `read_security` cluster privilege (or a greater privilege such as `manage_security` or `all`); _or_
- the _"Manage Application Privileges"_ global privilege for the application being referenced
  in the request

#### Description

To check a user's application privileges, use the
has privileges API.

#### Path parameters

`application`::
  (Optional, string) The name of the application. Application privileges are
  always associated with exactly one application. If you do not specify this
  parameter, the API returns information about all privileges for all
  applications.

`privilege`::
  (Optional, string) The name of the privilege. If you do not specify this
  parameter, the API returns information about all privileges for the requested
  application.

#### Examples

The following example retrieves information about the `read` privilege for the
`app01` application:

```console
GET /_security/privilege/myapp/read
```

A successful call returns an object keyed by application name and privilege
name. If the privilege is not defined, the request responds with a 404 status.

```console-result
{
  "myapp": {
    "read": {
      "application": "myapp",
      "name": "read",
      "actions": [
        "data:read/*",
        "action:login"
      ],
      "metadata": {
        "description": "Read access to myapp"
      }
    }
  }
}
```

To retrieve all privileges for an application, omit the privilege name:

```console
GET /_security/privilege/myapp/
```

To retrieve every privilege, omit both the application and privilege names:

```console
GET /_security/privilege/
```
