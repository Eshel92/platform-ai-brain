<!-- Converted from reference/api/admin/backup/s3-blockstore-config.txt (reStructuredText). Includes are inlined. -->

# S3-Compatible Blockstore Configurations

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Endpoints

The following lists the endpoints available for S3 blockstore configurations.

| Method | Endpoint | Description |
|---|---|---|
| GET | /snapshot/s3Configs/{S3-BLOCKSTORE-ID} | Get One S3-Compatible Blockstore Configuration by ID |
| GET | /snapshot/s3Configs | Get All S3-Compatible Blockstore Configurations |
| POST | /snapshot/s3Configs | Create One S3-Compatible Blockstore Configuration |
| PUT | /snapshot/s3Configs/{S3-BLOCKSTORE-ID} | Update One S3-Compatible Blockstore Configuration |
| DELETE | /snapshot/s3Configs/{S3-BLOCKSTORE-ID} | Delete One S3-Compatible Blockstore Configuration |
