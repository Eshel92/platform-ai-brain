<!-- Converted from reference/api/admin/backup/oplog-store-config.txt (reStructuredText). Includes are inlined. -->

# Oplog Store Configurations

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Endpoints

The following lists the endpoints available for Oplog Store configurations.

| Method | Endpoint | Description |
|---|---|---|
| GET | /oplog/mongoConfigs/{OPLOG-ID} | Get One Oplog Configuration by ID |
| GET | /oplog/mongoConfigs | Get All Oplog Configurations |
| POST | /oplog/mongoConfigs | Create One Oplog Configuration |
| PUT | /oplog/mongoConfigs/{OPLOG-ID} | Update One Oplog Configuration |
| DELETE | /oplog/mongoConfigs/{OPLOG-ID} | Delete One Oplog Configuration |
