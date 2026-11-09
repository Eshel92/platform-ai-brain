<!-- Converted from reference/api/admin/backup/blockstore-config.txt (reStructuredText). Includes are inlined. -->

# Blockstore Configurations

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0/admin/backup`

## Endpoints

The following lists the endpoints available for blockstore
configurations.

| Method | Endpoint | Description |
|---|---|---|
| GET | /snapshot/mongoConfigs/{BLOCKSTORE-ID} | Get One Blockstore Configuration by ID |
| GET | /snapshot/mongoConfigs | Get All Blockstore Configurations |
| POST | /snapshot/mongoConfigs | Create One Blockstore Configuration |
| PUT | /snapshot/mongoConfigs/{BLOCKSTORE-ID} | Update One Blockstore Configuration |
| DELETE | /snapshot/mongoConfigs/{BLOCKSTORE-ID} | Delete One Blockstore Configuration |
