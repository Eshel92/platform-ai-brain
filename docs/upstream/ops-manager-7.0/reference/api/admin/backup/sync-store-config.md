<!-- Converted from reference/api/admin/backup/sync-store-config.txt (reStructuredText). Includes are inlined. -->

# Sync Store Configurations

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Endpoints

The following lists the endpoints available for Sync Store
configurations.

| Method | Endpoint | Description |
|---|---|---|
| GET | /sync/mongoConfigs/{SYNCSTORE-ID} | Get One Sync Store Configuration by ID |
| GET | /sync/mongoConfigs | Get All Sync Store Configurations |
| POST | /sync/mongoConfigs | Create One Sync Store Configuration |
| PUT | /sync/mongoConfigs/{SYNCSTORE-ID} | Update One Sync Store Configuration |
| DELETE | /sync/mongoConfigs/{SYNCSTORE-ID} | Delete One Sync Store Configuration |
