<!-- Converted from ml/anomaly-detection/apis/delete-calendar-job.asciidoc (AsciiDoc). Includes are inlined. -->

# Delete anomaly detection jobs from calendar API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Deletes anomaly detection jobs from a calendar.

## Request

`DELETE _ml/calendars/<calendar_id>/jobs/<job_id>`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Path parameters

`<calendar_id>`::
(Required, string)
A string that uniquely identifies a calendar.
`<job_id>`::
(Required, string)
An identifier for the anomaly detection jobs. It can be a job
identifier, a group name, or a comma-separated list of jobs or groups.

## Examples

```console
DELETE _ml/calendars/planned-outages/jobs/total-requests
```

When the job is removed from the calendar, you receive the following
results:

```console-result
{
   "calendar_id": "planned-outages",
   "job_ids": []
}
```
