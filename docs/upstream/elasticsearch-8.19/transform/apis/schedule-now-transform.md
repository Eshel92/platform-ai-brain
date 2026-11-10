<!-- Converted from transform/apis/schedule-now-transform.asciidoc (AsciiDoc). Includes are inlined. -->

# Schedule now transform API

**New API reference**
For the most up-to-date API details, refer to [Transform APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-transform).

Instantly runs a transform to process data.

## Request

`POST _transform/<transform_id>/_schedule_now`

## Prerequisites

* Requires the `manage_transform` cluster privilege. This privilege is included
in the `transform_admin` built-in role.

## Description

When you run this API, processing for the next checkpoint is started immediately 
without waiting for the configured `frequency` interval. The API returns 
immediately, data processing happens in the background. Subsequently, the 
transform will be processed again at `now + frequency` unless the API is 
called again in the meantime.

## Path parameters

`<transform_id>`::
(Required, string)
Identifier for the transform.

## Query parameters

`timeout`::
(Optional, time)
Period to wait for a response. If no response is received before the timeout
expires, the request fails and returns an error. Defaults to `30s`.

## Examples

```console
POST _transform/ecommerce_transform/_schedule_now
```

When the transform is scheduled now, you receive the following results:

```console-result
{
  "acknowledged" : true
}
```
