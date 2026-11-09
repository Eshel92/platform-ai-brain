<!-- Converted from reference/api/cloud-migration.txt (reStructuredText). Includes are inlined. -->

# Live Data Migration from Ops Manager to MongoDB Atlas

Connects an Ops Manager organization to an MongoDB Atlas organization. This
connection allows you to migrate your data from an Ops Manager deployment to
an MongoDB Atlas cluster.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following endpoints are available to connect organizations between
Ops Manager and MongoDB Atlas.

| Method | Endpoint | Description |
|---|---|---|
| `POST` | /orgs/{orgId}/liveExport/migrationLink | Connect the source Ops Manager organization with a target MongoDB Atlas organization. |
| `DELETE` | /orgs/{orgId}/liveExport/migrationLink | Remove the connection between the source Ops Manager organization and the target MongoDB Atlas organization. This stops the source organization from synchronizing data with the target organization. |
| `GET` | /orgs/{orgId}/liveExport/migrationLink/status | Return the status of the connection between the specified source Ops Manager organization and the target MongoDB Atlas organization. |
