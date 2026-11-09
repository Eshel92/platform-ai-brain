<!-- Converted from reference/api/admin/backup/s3-oplog-store-config.txt (reStructuredText). Includes are inlined. -->

# S3 Oplog Configurations

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Endpoints

The following lists the endpoints available for S3 Oplog configurations.

| Method | Endpoint | Description |
|---|---|---|
| GET | /oplog/s3Configs/{S3-OPLOG-ID} | Get One S3 Oplog Configuration by ID |
| GET | /oplog/s3Configs | Get All S3 Oplog Configurations |
| POST | /oplog/s3Configs | Create One S3 Oplog Configuration |
| PUT | /oplog/s3Configs/{S3-OPLOG-ID} | Update One S3 Oplog Configuration |
| DELETE | /oplog/s3Configs/{S3-OPLOG-ID} | Delete One S3 Oplog Configuration |
