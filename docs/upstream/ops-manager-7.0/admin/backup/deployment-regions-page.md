<!-- Converted from admin/backup/deployment-regions-page.txt (reStructuredText). Includes are inlined. -->

# Deployment Regions

Ops Manager supports backup regionalization, which allows each cluster or
shard to read from and write to snapshot stores in a region you
choose. To enable regionalized backup, you must configure deployment
regions. You then bind backup resources such as snapshot stores or `backup daemons` to these deployment
regions.

**Note:**

You can't delete deployment regions that are currently bound to
backup resources. 

The deployment region page lists all available deployment regions, and
allows you to define new deployment regions.

**Important:**

Regional backups ensure storage isolation of cluster data
backup. Backup metadata, monitoring, and other Ops Manager data not
related to the specific cluster backup data can still move across
regions depending on your Ops Manager deployment configuration.

To ensure data isolation during restore procedures, you must
execute restores only against endpoints in that deployment's
configured deployment region. This requirement applies when you
restore replica sets and sharded clusters, as well as queryable
restores.

To fulfill backup data sovereignty requirements, you must ensure
that you configure all backup and restore endpoints correctly and a
user doesn't request an operation that causes backup data to move
across regions.

To further protect against unintentional cross-region backup or
restore, consider configuring network restrictions for your data
centers.

## Add New Deployment Regions

To define a new deployment region:

**Step 1: Click Add New Deployment Region.**

**Step 2: Configure the deployment region.**

In the Set up a Deployment Region
window, provide values for the following fields:

| Field | Value |
|---|---|
| Deployment ID | Unique identifier that references this deployment region in configurations. The ID can contain up to 64 alphanumeric characters and the dash (`-), underscore (`), and dot (`.`) characters. You can't modify the deployment ID of a region once it's created. |
| Ingestion Endpoint | Ops Manager instance to which the `Backup Agent` writes snapshot or oplog data. Value must be a valid URL (Uniform Resource Locator) such as `http://www.mongodb.com`. Supports both HTTP and HTTPS protocols. |
| Restore Endpoint | Ops Manager instance that serves restore requests. |
| Queryable Proxy Server Endpoint | Ops Manager instance that serves `Queryable Backup` requests. Value must be in the following format: `domain:port`. For example, `localhost:8080`. |
| Deployment Description | String that describes the purpose of the deployment region. |
| Assignment Enabled | Flag that specifies whether you an assign the region to new resources. If you disable this field, you can't assign the region to any new resource. |

**Step 3: Click Confirm.**

## Edit a Deployment Region

To make changes to a deployment region, perform the following steps: 

**Step 1: Open the modal to edit a deployment region.**

For the deployment region that you want to modify: 

a. Click the ellipsis-h in the Actions column.
#. Select Edit from the dropdown.

   The Set up a Deployment Region modal displays.

**Step 2: Modify the deployment region.**

In the Set up a Deployment Region
modal, make changes to any of the following fields:

| Field | Value |
|---|---|
| Ingestion Endpoint | Ops Manager instance to which the `Backup Agent` writes snapshot or oplog data. Value must be a valid URL (Uniform Resource Locator) such as `http://www.mongodb.com`. Supports both HTTP and HTTPS protocols. |
| Restore Endpoint | Ops Manager instance that serves restore requests. |
| Queryable Proxy Server Endpoint | Ops Manager instance that serves `Queryable Backup` requests. Value must be in the following format: `domain:port`. For example, `localhost:8080`. |
| Deployment Description | String that describes the purpose of the deployment region. |
| Assignment Enabled | Flag that specifies whether you can assign the region to new resources. If you disable this field, you can't assign the region to any new resource. |

**Step 3: Click Confirm.**

## Assign a Deployment Region for a Shard

To assign a deployment region to a new shard, perform the following
steps:

**Step 1: Click the Assign button.**

You can find the Assign button in the
Continuous Backup dashboard the following ways: 

- Hover over the cluster status Misconfigured.
- Click the ellipsis-h in the Options column. 

The Start Backup modal displays.

**Step 2: Configure the deployment region.**

Select a deployment region from the Select region
dropdown. You can't modify deployment regions configured for
existing members. 

**Note:**

To change the deployment region for a member, you must first
stop and terminate the current backup job, and then start a new
backup job in the new region.

Ensure that the deployment region that you select has snapshot,
oplog, and sync stores configured for that region. Ops Manager displays
an error if there are no daemons bound to any of the selected
deployment regions. 

**Step 3: Click Start.**

When you assign a deployment region to a shard, Ops Manager does the
following: 

- Assigns snapshot, oplog, and sync stores and daemons to the
  backup jobs.
- Resumes oplog tailing and takes snapshots
- Resolves project alarms.
