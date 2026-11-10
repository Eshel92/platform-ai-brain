<!-- Converted from rest-api/security/create-service-token.asciidoc (AsciiDoc). Includes are inlined. -->

### Create service account token API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Creates a  service accounts token for access without requiring basic
authentication.

#### Request

`POST /_security/service/<namespace>/<service>/credential/token/<token_name>`

`PUT /_security/service/<namespace>/<service>/credential/token/<token_name>`

`POST /_security/service/<namespace>/<service>/credential/token`

#### Prerequisites

* To use this API, you must have at least the `manage_service_account`
cluster privilege.

#### Description

A successful create service account token API call returns a JSON structure
that contains the service account token, its name, and its secret value.

**Note:** Service account tokens never expire. You must actively delete them if they are no longer needed.

#### Path parameters

`namespace`::
  (Required, string) Name of the namespace.

`service`::
  (Required, string) Name of the service name.

`token_name`::
  (Optional, string) Name for the service account token. If omitted, a random name will be generated.
Token names must be at least 1 and no more than 256 characters. They can contain
alphanumeric characters (`a-z`, `A-Z`, `0-9`), dashes (`-`), and underscores
(`_`), but cannot begin with an underscore.

**Note:** Token names must be unique in the context of the associated service
account. They must also be globally unique with their fully qualified names,
which are comprised of the service account principal and token name, such as
`<namespace>/<service>/<token-name>`.

#### Examples

The following request creates a service account token:

```console
POST /_security/service/elastic/fleet-server/credential/token/token1
```

The response includes the service account token, its name, and its secret value:

```console-result
{
  "created": true,
  "token": {
    "name": "token1",
    "value": "AAEAAWVsYXN0aWM...vZmxlZXQtc2VydmVyL3Rva2VuMTo3TFdaSDZ" <1>
  }
}
```
<1> The secret value to use as a bearer token

To use the service account token, include the generated token value in a
request with an `Authorization: Bearer` header:

```shell
curl -H "Authorization: Bearer AAEAAWVsYXN0aWM...vZmxlZXQtc2VydmVyL3Rva2VuMTo3TFdaSDZ" http://localhost:9200/_cluster/health
```

**Note:** If your node has `xpack.security.http.ssl.enabled` set to `true`, then
you must specify `https` in the request URL.

The following request creates a service token with an auto-generated token name:

```console
POST /_security/service/elastic/fleet-server/credential/token
```

The response includes the service account token, its auto-generated name, and
its secret value:

```console-result
{
  "created": true,
  "token": {
    "name": "Jk5J1HgBuyBK5TpDrdo4",
    "value": "AAEAAWVsYXN0aWM...vZmxlZXQtc2VydmVyL3Rva2VuMTo3TFdaSDZ"
  }
}
```
