<!-- Converted from ml/anomaly-detection/apis/put-calendar-job.asciidoc (AsciiDoc). Includes are inlined. -->

# Add anomaly detection jobs to calendar API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Adds an anomaly detection job to a calendar.

## Request

`PUT _ml/calendars/<calendar_id>/jobs/<job_id>`

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
PUT _ml/calendars/planned-outages/jobs/total-requests
```

The API returns the following results:

```console-result
{
  "calendar_id": "planned-outages",
  "job_ids": [
    "total-requests"
  ]
}
```
