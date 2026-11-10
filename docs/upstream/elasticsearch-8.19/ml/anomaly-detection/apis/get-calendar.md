<!-- Converted from ml/anomaly-detection/apis/get-calendar.asciidoc (AsciiDoc). Includes are inlined. -->

# Get calendars API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Retrieves configuration information for calendars.

## Request

`GET _ml/calendars/<calendar_id>` +

`GET _ml/calendars/_all`

## Prerequisites

Requires the `monitor_ml` cluster privilege. This privilege is included in the 
`machine_learning_user` built-in role.

## Description

For more information, see
{ml-docs}/ml-ad-run-jobs.html#ml-ad-calendars[Calendars and scheduled events].

## Path parameters

`<calendar_id>`::
(Required, string)
A string that uniquely identifies a calendar.
You can get information for multiple calendars in a single API request by using
a comma-separated list of ids or a wildcard expression. You can get information
for all calendars by using `_all`, by specifying `*` as the calendar identifier,
or by omitting the identifier.

## Query parameters

`from`::
    (Optional, integer) Skips the specified number of calendars. This parameter
    is supported only when you omit the `<calendar_id>`. Defaults to `0`.

`size`::
    (Optional, integer) Specifies the maximum number of calendars to obtain.
    This parameter is supported only when you omit the `<calendar_id>`. Defaults
    to `100`.

## Request body

`page`::
**Properties of `page`**

`from`:::
(Optional, integer) Skips the specified number of calendars. This object is 
supported only when you omit the `<calendar_id>`. Defaults to `0`.

`size`:::
(Optional, integer) Specifies the maximum number of calendars to obtain. This
object is  supported only when you omit the `<calendar_id>`. Defaults to `100`.

## Response body

The API returns an array of calendar resources, which have the following
properties:

`calendar_id`::
(string)
A string that uniquely identifies a calendar.
`job_ids`::
(array) An array of anomaly detection job identifiers. For example:
`["total-requests"]`.

## Examples

```console
GET _ml/calendars/planned-outages
```

The API returns the following results:

```console-result
{
  "count": 1,
  "calendars": [
    {
      "calendar_id": "planned-outages",
      "job_ids": [
        "total-requests"
      ]
    }
  ]
}
```
