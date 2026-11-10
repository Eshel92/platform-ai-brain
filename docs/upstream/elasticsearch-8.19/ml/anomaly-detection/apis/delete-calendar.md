<!-- Converted from ml/anomaly-detection/apis/delete-calendar.asciidoc (AsciiDoc). Includes are inlined. -->

# Delete calendars API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Deletes a calendar.

## Request

`DELETE _ml/calendars/<calendar_id>`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

This API removes all scheduled events from the calendar then deletes the
calendar.

## Path parameters

`<calendar_id>`::
(Required, string)
A string that uniquely identifies a calendar.

## Examples

```console
DELETE _ml/calendars/planned-outages
```

When the calendar is deleted, you receive the following results:

```console-result
{
  "acknowledged": true
}
```
