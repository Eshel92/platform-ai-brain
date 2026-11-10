<!-- Converted from licensing/delete-license.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete license API

**New API reference**
For the most up-to-date API details, refer to [Licensing APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-license).

This API enables you to delete licensing information.

#### Request

`DELETE /_license`

#### Description

When your license expires, X-Pack operates in a degraded mode. For more
information, see
[License expiration](https://www.elastic.co/guide/en/kibana/8.19/managing-licenses.html#license-expiration).

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

* If the {operator-feature} is enabled, only operator
users can use this API.

#### Examples

The following example queries the info API:

```console
DELETE /_license
```

When the license is successfully deleted, the API returns the following response:
```js
{
  "acknowledged": true
}
```
