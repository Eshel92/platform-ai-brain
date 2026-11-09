<!-- Converted from reference/api/measurements.txt (reStructuredText). Includes are inlined. -->

# Measurements

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Retrieves measurements the Monitoring and Automations have
collected for your MongoDB processes, databases, and disks.
Monitorings collect process and database measurements using
MongoDB diagnostic commands, including
serverStatus and
dbStats. Automations
collect measurements for hosts that run managed mongod
and mongos processes.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following lists the endpoints available for measurements.

| Method | Endpoint | Description |
|---|---|---|
| GET | /groups/{PROJECT-ID}/hosts/{HOST-ID}/measurements | Get Host, Process, and System Measurements |
| GET | /groups/{PROJECT-ID}/hosts/{HOST-ID}/disks/{PARTITION-NAME}/measurements | Get Disk Partition Measurements |
| GET | /groups/{PROJECT-ID}/hosts/{HOST-ID}/databases/{DATABASE-NAME}/measurements | Get Database Measurements |
| GET | /groups/{PROJECT-ID}/hosts/{HOST-ID}/measurements | Get a List of Measurement Types |

**Note:**

All of the given endpoints return specific measurement types.
To learn about what Ops Manager measures, see /reference/api/measures/measurement-types.
