<!-- Converted from ml/anomaly-detection/apis/put-calendar.asciidoc (AsciiDoc). Includes are inlined. -->

# Create calendars API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Instantiates a calendar.

## Request

`PUT _ml/calendars/<calendar_id>`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

For more information, see
{ml-docs}/ml-ad-run-jobs.html#ml-ad-calendars[Calendars and scheduled events].

## Path parameters

`<calendar_id>`::
(Required, string)
A string that uniquely identifies a calendar.

## Request body

`description`::
(Optional, string) A description of the calendar.

## Examples

```console
PUT _ml/calendars/planned-outages
```

When the calendar is created, you receive the following results:

```console-result
{
  "calendar_id": "planned-outages",
  "job_ids": []
}
```
