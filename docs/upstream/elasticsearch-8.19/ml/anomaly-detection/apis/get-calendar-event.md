<!-- Converted from ml/anomaly-detection/apis/get-calendar-event.asciidoc (AsciiDoc). Includes are inlined. -->

# Get scheduled events API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Retrieves information about the scheduled events in calendars.

## Request

`GET _ml/calendars/<calendar_id>/events` +

`GET _ml/calendars/_all/events`

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
You can get scheduled event information for multiple calendars in a single
API request by using a comma-separated list of ids or a wildcard expression.
You can get scheduled event information for all calendars by using `_all` or `*`
as the calendar identifier.

## Query parameters

`end`::
  (Optional, string) Specifies to get events with timestamps earlier than this
  time.

`from`::
  (Optional, integer) Skips the specified number of events. Defaults to `0`.

`job_id`::
  (Optional, string) Specifies to get events for a specific anomaly detection job
  identifier or job group. It must be used with a calendar identifier of `_all`
  or `*`.

`size`::
  (Optional, integer) Specifies the maximum number of events to obtain. Defaults
  to `100`.

`start`::
  (Optional, string) Specifies to get events with timestamps after this time.

## Request body

You can also specify the query parameters in the request body; the exception are
`from` and `size`, use `page` instead:

`page`::
**Properties of `page`**

`from`:::
(Optional, integer) Skips the specified number of events. Defaults to `0`.

`size`:::
(Optional, integer) Specifies the maximum number of events to obtain. Defaults
to `100`.

## Response body

The API returns an array of scheduled event resources, which have the
following properties:

`calendar_id`::
(string)
A string that uniquely identifies a calendar.
`description`::
(string) A description of the scheduled event.

`end_time`::
(date) The timestamp for the end of the scheduled event in milliseconds since
the epoch or ISO 8601 format.

`event_id`::
(string) An automatically-generated identifier for the scheduled event.

`start_time`::
(date) The timestamp for the beginning of the scheduled event in milliseconds
since the epoch or ISO 8601 format.

## Examples

```console
GET _ml/calendars/planned-outages/events
```

The API returns the following results:

```console-result
{
  "count": 3,
  "events": [
    {
      "description": "event 1",
      "start_time": 1513641600000,
      "end_time": 1513728000000,
      "calendar_id": "planned-outages",
      "event_id": "LS8LJGEBMTCMA-qz49st"
    },
    {
      "description": "event 2",
      "start_time": 1513814400000,
      "end_time": 1513900800000,
      "calendar_id": "planned-outages",
      "event_id": "Li8LJGEBMTCMA-qz49st"
    },
    {
      "description": "event 3",
      "start_time": 1514160000000,
      "end_time": 1514246400000,
      "calendar_id": "planned-outages",
      "event_id": "Ly8LJGEBMTCMA-qz49st"
    }
  ]
}
```

The following example retrieves scheduled events that occur within a specific
period of time:

```console
GET _ml/calendars/planned-outages/events?start=1635638400000&end=1635724800000
```
