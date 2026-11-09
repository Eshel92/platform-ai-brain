<!-- Converted from reference/api/restore-jobs.txt (reStructuredText). Includes are inlined. -->

# Restore Jobs

The `restoreJobs` resource allows you to manage restore jobs. A
restore job is essentially one request to retrieve one of your existing
snapshots to restore one `mongod` to one previous state. To initiate
one restore job, you must issue the request from an IP address on your
user account's access list.

**Important:**

Restore delivery via SCP (secure copy) was removed in
Ops Manager 4.0.

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following lists the endpoints available for restore jobs.

| Method | Endpoint | Description |
|---|---|---|
| GET | /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs | Get All Restore Jobs for One Cluster |
| GET | /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs?batchid={BATCH-ID} | Get All Restore Jobs for One Batch for One Cluster |
| GET | /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs/{JOB-ID} | Get One Restore Job for One Cluster |
| POST | /groups/{PROJECT-ID}/clusters/{CLUSTER-ID}/restoreJobs | Create One Restore Job for One Cluster |

**Important:** Deprecated when using MongoDB 3.4

As of MongoDB 3.4, mirrored config server deployments (also known as
SCCC (Sync Cluster Connection Config)) are no longer
supported. The following API methods work with SCCC (Sync
Cluster Connection Config) config servers only. Config servers must be
deployed as replica sets (also known as CSRS (Config Server
Replica Set)). For more information, see
replset-config-servers in the MongoDB Server Manual.

| Method | Endpoint | Description |
|---|---|---|
| GET | /groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs | Get All Restore Jobs for One Legacy Mirrored Config Server |
| GET | /groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs/{JOB-ID} | Get One Restore Job for One Legacy Mirrored Config Server |
| POST | /groups/{PROJECT-ID}/hosts/{HOST-ID}/restoreJobs | Create One Restore Job for One Legacy Mirrored Config Server |
