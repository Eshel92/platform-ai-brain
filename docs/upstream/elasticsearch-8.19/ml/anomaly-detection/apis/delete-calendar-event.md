<!-- Converted from ml/anomaly-detection/apis/delete-calendar-event.asciidoc (AsciiDoc). Includes are inlined. -->

# Delete events from calendar API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Deletes scheduled events from a calendar.

## Request

`DELETE _ml/calendars/<calendar_id>/events/<event_id>`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

This API removes individual events from a calendar. To remove all scheduled
events and delete the calendar, see the
delete calendar API.

## Path parameters

`<calendar_id>`::
(Required, string)
A string that uniquely identifies a calendar.
`<event_id>`::
  (Required, string) Identifier for the scheduled event. You can obtain this
  identifier by using the get calendar events API.

## Examples

```console
DELETE _ml/calendars/planned-outages/events/LS8LJGEBMTCMA-qz49st
```

When the event is removed, you receive the following results:
```js
{
  "acknowledged": true
}
```
