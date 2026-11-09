<!-- Converted from reference/api/backup-configurations.txt (reStructuredText). Includes are inlined. -->

# Backup Configurations

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

## Overview

A backup configuration determines the settings used to back up a sharded
cluster or replica set. The `backupConfigs` resource lets you view and
update backup configurations. In certain cases, you can also create 
backup configurations, as described in 
/reference/api/backup/update-backup-config. The 
`backupConfigs` resource supports only the `GET` and `PATCH`
methods.

To update or create a backup configuration, you must issue the request 
from an IP address on your user account's access list. The `backupConfigs` resource accepts
`PATCH` requests only from IP addresses in the access list.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following lists the endpoints available for 
Backup Configuration.

| Method | Endpoint | Description |
|---|---|---|
| GET | /groups/{PROJECT-ID}/backupConfigs | Get all backup configurations for a project. |
| GET | /groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID} | Get a single backup configuration by cluster ID. |
| PATCH | /groups/{PROJECT-ID}/backupConfigs/{CLUSTER-ID} | Update a backup configuration. |
