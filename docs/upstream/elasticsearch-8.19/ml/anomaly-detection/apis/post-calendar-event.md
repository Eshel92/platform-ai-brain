<!-- Converted from ml/anomaly-detection/apis/post-calendar-event.asciidoc (AsciiDoc). Includes are inlined. -->

# Add events to calendar API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Posts scheduled events in a calendar.

## Request

`POST _ml/calendars/<calendar_id>/events`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

This API accepts a list of
{ml-docs}/ml-ad-run-jobs.html#ml-ad-calendars[scheduled events], each
of which must have a start time, end time, and description.

## Path parameters

`<calendar_id>`::
(Required, string)
A string that uniquely identifies a calendar.

## Request body

`events`::
(Required, array) A list of one of more scheduled events. The event's start and
end times may be specified as integer milliseconds since the epoch or as a
string in ISO 8601 format.
**Properties of events**
`description`:::
(Optional, string) A description of the scheduled event.

`end_time`:::
(Required, date) The timestamp for the end of the scheduled event in
milliseconds since the epoch or ISO 8601 format.

`start_time`:::
(Required, date) The timestamp for the beginning of the scheduled event in
milliseconds since the epoch or ISO 8601 format.

## Examples

```console
POST _ml/calendars/planned-outages/events
{
  "events" : [
    {"description": "event 1", "start_time": 1513641600000, "end_time": 1513728000000},
    {"description": "event 2", "start_time": 1513814400000, "end_time": 1513900800000},
    {"description": "event 3", "start_time": 1514160000000, "end_time": 1514246400000}
  ]
}
```

The API returns the following results:

```console-result
{
  "events": [
    {
      "description": "event 1",
      "start_time": 1513641600000,
      "end_time": 1513728000000,
      "calendar_id": "planned-outages"
    },
    {
      "description": "event 2",
      "start_time": 1513814400000,
      "end_time": 1513900800000,
      "calendar_id": "planned-outages"
    },
    {
      "description": "event 3",
      "start_time": 1514160000000,
      "end_time": 1514246400000,
      "calendar_id": "planned-outages"
    }
  ]
}
```
