<!-- Converted from api/dashboard/export-dashboard.asciidoc (AsciiDoc). Includes are inlined. -->

### Export dashboard API

deprecated::[7.15.0,Use the [saved objects API](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-saved-objects) instead.]

Export dashboards and corresponding saved objects.

#### Request

`GET <kibana host>:<port>/api/kibana/dashboards/export`

`GET <kibana host>:<port>/s/<space-id>/api/kibana/dashboards/export`

#### Query parameters

`dashboard`::
  (Required, array|string) The IDs of the dashboards that you want to export.
  To export multiple dashboards, repeat the query parameter.

#### Response body

`objects`::
  (array) A top level property that includes the saved objects. The order of the objects is not guaranteed. Use the exact response body as the request body for the corresponding Import dashboard API.

#### Response code

`200`::
  Indicates a successful call.

#### Example

```sh
$ curl -X GET api/kibana/dashboards/export?dashboard=942dcef0-b2cd-11e8-ad8e-85441f0c2e5c <1>
```

<1> The dashboard ID is `942dcef0-b2cd-11e8-ad8e-85441f0c2e5c`.
