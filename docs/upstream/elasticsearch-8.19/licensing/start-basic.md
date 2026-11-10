<!-- Converted from licensing/start-basic.asciidoc (AsciiDoc). Includes are inlined. -->

### Start basic API

**New API reference**
For the most up-to-date API details, refer to [Licensing APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-license).

This API starts an indefinite basic license.

#### Request

`POST /_license/start_basic`

#### Description

The `start basic` API enables you to initiate an indefinite basic license, which
gives access to all the basic features. If the basic license does not support
all of the features that are available with your current license, however, you are
notified in the response. You must then re-submit the API request with the
`acknowledge` parameter set to `true`.

To check the status of your basic license, use the following API:
get-basic-status.

For more information about the different types of licenses, see
https://www.elastic.co/subscriptions.

#### Authorization

You must have `manage` cluster privileges to use this API.
For more information, see
security-privileges.

#### Examples

The following example starts a basic license if you do not currently have a license:

```console
POST /_license/start_basic
```

Example response:
```js
{
  "basic_was_started": true,
  "acknowledged": true
}
```

The following example starts a basic license if you currently have a license with more
features than a basic license. As you are losing features, you must pass the acknowledge
parameter:

```console
POST /_license/start_basic?acknowledge=true
```

Example response:
```js
{
  "basic_was_started": true,
  "acknowledged": true
}
```
