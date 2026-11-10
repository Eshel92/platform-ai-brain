<!-- Converted from licensing/get-license.asciidoc (AsciiDoc). Includes are inlined. -->

### Get license API

**New API reference**
For the most up-to-date API details, refer to [Licensing APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-license).

This API enables you to retrieve licensing information.

#### Request

`GET /_license`

#### Description

This API returns information about the type of license, when it was issued, and
when it expires, for example.

For more information about the different types of licenses, see
https://www.elastic.co/subscriptions.

**Note:** If the master node is generating a new cluster state, the get license API
may return a `404 Not Found` response. If you receive an unexpected `404`
response after cluster startup, wait a short period and retry the request. 

#### Query Parameters

`local`::
  (Boolean) Specifies whether to retrieve local information. The default value
  is `false`, which means the information is retrieved from the master node.
  
 `accept_enterprise`::
(Boolean) If `true`, this parameter returns `enterprise` for Enterprise
license types. If `false`, this parameter returns `platinum` for both
`platinum` and `enterprise` license types. This behavior is maintained for
backwards compatibility.
   
deprecated::[7.6.0,"This parameter is deprecated and will always be set to `true` in 8.x."]

#### Authorization

You must have `monitor` cluster privileges to use this API.
For more information, see security-privileges.

#### Examples

The following example provides information about a trial license:

```console
GET /_license
```

```console-result
{
  "license" : {
    "status" : "active",
    "uid" : "cbff45e7-c553-41f7-ae4f-9205eabd80xx",
    "type" : "trial",
    "issue_date" : "2018-10-20T22:05:12.332Z",
    "issue_date_in_millis" : 1540073112332,
    "expiry_date" : "2018-11-19T22:05:12.332Z",
    "expiry_date_in_millis" : 1542665112332,
    "max_nodes" : 1000,
    "max_resource_units" : null,
    "issued_to" : "test",
    "issuer" : "elasticsearch",
    "start_date_in_millis" : -1
  }
}
```
