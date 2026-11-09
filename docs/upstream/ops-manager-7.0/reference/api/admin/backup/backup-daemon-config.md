<!-- Converted from reference/api/admin/backup/backup-daemon-config.txt (reStructuredText). Includes are inlined. -->

# Backup Daemon Configurations

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Endpoints

The following lists the endpoints available for Backup Daemon
configurations.

| Method | Endpoint | Description |
|---|---|---|
| GET | /daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY} | Get One Backup Daemon Configuration by Host |
| GET | /daemon/configs | Get All Backup Daemon Configurations |
| PUT | /daemon/configs/{MACHINE} | Create One Backup Daemon Configuration |
| PUT | /daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY} | Update One Backup Daemon Configuration |
| DELETE | /daemon/configs/{MACHINE}/{HEAD-ROOT-DIRECTORY} | Delete One Backup Daemon Configuration |
