<!-- Converted from reference/api/admin/backup/file-system-store-config.txt (reStructuredText). Includes are inlined. -->

# File System Store Configurations

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Endpoints

The following lists the endpoints available for File System Store
configurations.

| Method | Endpoint | Description |
|---|---|---|
| GET | /snapshot/fileSystemConfigs/{FILESYSTEM-ID} | Get One File System Store Configuration by ID |
| GET | /snapshot/fileSystemConfigs | Get All File System Store Configurations |
| POST | /snapshot/fileSystemConfigs | Create One File System Store Configuration |
| PUT | /snapshot/fileSystemConfigs/{FILESYSTEM-ID} | Update One File System Store Configuration |
| DELETE | /snapshot/fileSystemConfigs/{FILESYSTEM-ID} | Delete One File System Store Configuration |
