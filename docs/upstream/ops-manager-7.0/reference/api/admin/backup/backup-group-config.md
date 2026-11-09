<!-- Converted from reference/api/admin/backup/backup-group-config.txt (reStructuredText). Includes are inlined. -->

# Project Backup Job Configurations

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Endpoints

The following lists the endpoints available for project backup job
configurations.

| Method | Endpoint | Description |
|---|---|---|
| GET | /groups/{PROJECT-ID} | Get One Project Backup Jobs Configuration by ID |
| GET | /groups | Get All Project Backup Jobs Configurations |
| PUT | /groups/{PROJECT-ID} | Update One Project Backup Jobs Configuration |
