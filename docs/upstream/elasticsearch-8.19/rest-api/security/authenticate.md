<!-- Converted from rest-api/security/authenticate.asciidoc (AsciiDoc). Includes are inlined. -->

### Authenticate API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Enables you to submit a request with a basic auth header to
authenticate a user and retrieve information about the authenticated user.

#### Request

`GET /_security/_authenticate`

#### Description

A successful call returns a JSON structure that shows user information such as their username, the roles that are
assigned to the user, any assigned metadata, and information about the realms that authenticated and authorized the user.

#### Response codes

If the user cannot be authenticated, this API returns a 401 status code.

#### Examples

To authenticate a user, submit a GET request to the
`/_security/_authenticate` endpoint:

```console
GET /_security/_authenticate
```

The following example output provides information about the "rdeniro" user:

```console-result
{
  "username": "rdeniro",
  "roles": [
    "admin"
  ],
  "full_name": null,
  "email":  null,
  "metadata": { },
  "enabled": true,
  "authentication_realm": {
    "name" : "file",
    "type" : "file"
  },
  "lookup_realm": {
    "name" : "file",
    "type" : "file"
  },
  "authentication_type": "realm"
}
```
