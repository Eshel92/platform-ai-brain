<!-- Converted from rest-api/security/delete-service-token.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete service account tokens API

**New API reference**
For the most up-to-date API details, refer to [Security APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-security).

Deletes  service account tokens for a `service` in a
specified `namespace`.

#### Request

`DELETE /_security/service/<namespace>/<service>/credential/token/<token_name>`

#### Prerequisites

* To use this API, you must have at least the `manage_service_account`
cluster privilege.

#### Description

The API response indicates whether the specified service account token is found
and deleted or it is not found.

#### Path parameters

`namespace`::
(Required, string) Name of the namespace.

`service`::
(Required, string) Name of the service name.

`token_name`::
(Required, string) Name of the service account token.

#### Examples

The following request deletes the `token1` service account token from the
`elastic/fleet-server` service account:

```console
DELETE /_security/service/elastic/fleet-server/credential/token/token42
```

If the service account token is successfully deleted, the request returns
`{"found": true}`. Otherwise, the response will have status code `404` and
found` will be set to `false`.

```console-result
{
  "found" : true
}
```
