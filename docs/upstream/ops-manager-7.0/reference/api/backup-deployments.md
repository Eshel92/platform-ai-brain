<!-- Converted from reference/api/backup-deployments.txt (reStructuredText). Includes are inlined. -->

# Deployment Regions

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

## Overview

Ops Manager supports backup regionalization, which allows each cluster or
shard to read from and write to snapshot stores in single or multiple
regions of your choice. The `backupDeployments` resource lets you view
and update deployment regions. 

To update or create a deployment region, you must issue the request 
from an IP address on your user account's access list. The `backupDeployments` resource
accepts all requests only from IP addresses in the access list.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following lists the endpoints available for 
Backup Configuration.

| Method | Endpoint | Description |
|---|---|---|
| GET | /admin/backup/backupDeployments | Get all deployment regions for a project. |
| GET | /admin/backup/backupDeployments/{DEPLOYMENT-ID} | Get one deployment region by its ID. |
| POST | /admin/backup/backupDeployments/ | Create a new deployment region. |
| PUT | /admin/backup/backupDeployments/ | Create one new deployment region by ID. |
| PATCH | /admin/backup/backupDeployments/{CLUSTER-ID} | Assign a deployment region to a cluster specified by the cluster ID. |
| DELETE | /admin/backup/backupDeployments/{DEPLOYMENT-ID} | Remove one deployment region by its ID. |
