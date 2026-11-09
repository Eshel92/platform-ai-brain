<!-- Converted from reference/api/snapshots.txt (reStructuredText). Includes are inlined. -->

# Snapshots

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

This resource allows you to view metadata of, change the expiration date
for, and remove existing snapshots. A snapshot is a complete copy of the
data in a `mongod` instance at a point in time.

You can retrieve snapshot metadata for the whole cluster or replica set, or for a single config server in
a cluster.

To restore the snapshot data, you must create a
restore job.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following lists the endpoints available for snapshots.

| Method | Endpoint | Description |
|---|---|---|
| GET | /groups/{groupId}/clusters/{clusterId}/snapshots | Get All Snapshots for a Cluster |
| GET | /groups/{groupId}/clusters/{clusterId}/snapshots/{snapshotId} | Get one snapshot for a cluster. |
| PATCH | /groups/{groupId}/clusters/{clusterId}/snapshots/{snapshotId} | Change expiration date for one snapshot. |
| DELETE | /groups/{groupId}/clusters/{clusterId}/snapshots/{snapshotId} | Remove one snapshot. IMPORTANT: To delete a snapshot, you must issue the request from an IP address on your user account's access list. |
| POST | /groups/{groupId}/clusters/{clusterId}/snapshots/onDemandSnapshot | Create one on-demand snapshot for a cluster. |

**Important:** Deprecated when using MongoDB 3.4

As of MongoDB 3.4, mirrored config server deployments (also known
as SCCC (Sync Cluster Connection Config)) are no longer
supported. The following API methods work with
SCCC (Sync Cluster Connection Config) config servers only.
Config servers must be deployed as replica sets (also known as
CSRS (Config Server Replica Set)). For more information, see
replset-config-servers
in the MongoDB Server Manual.

| Method | Endpoint | Description |
|---|---|---|
| GET | /groups/{groupId}/hosts/{hostId}/snapshots | Get all snapshots for a config server. |
| GET | /groups/{groupId}/hosts/{hostId}/snapshots/{snapshotId} | Get one snapshot for a config server. |
