<!-- Converted from licensing/get-basic-status.asciidoc (AsciiDoc). Includes are inlined. -->

### Get basic status API

**New API reference**
For the most up-to-date API details, refer to [Licensing APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-license).

This API enables you to check the status of your basic license.

#### Request

`GET /_license/basic_status`

#### Description

In order to initiate a basic license, you must not currently have a basic
license.

For more information about the different types of licenses, see
https://www.elastic.co/subscriptions.

#### Authorization

You must have `monitor` cluster privileges to use this API.
For more information, see security-privileges.

#### Examples

The following example checks whether you are eligible to start a basic:

```console
GET /_license/basic_status
```

Example response:

```console-result
{
  "eligible_to_start_basic": true
}
```
