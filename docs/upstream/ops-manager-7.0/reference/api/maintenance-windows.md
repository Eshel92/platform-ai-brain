<!-- Converted from reference/api/maintenance-windows.txt (reStructuredText). Includes are inlined. -->

# Maintenance Windows

The `maintenanceWindows` resource turns off alert notifications for
specified alert types for a period of time to allow maintenance to 
occur.

## Endpoints

The following endpoints are available for `maintenanceWindows`.

| Method | Endpoint | Description |
|---|---|---|
| GET | /groups/{PROJECT-ID}/maintenanceWindows/ | Retrieve all maintenance windows with end dates in the future. |
| GET | /groups/{PROJECT-ID}/maintenanceWindows/{MW-ID} | Retrieve one maintenance window with an end date in the future. |
| POST | /groups/{PROJECT-ID}/maintenanceWindows | Create one maintenance window. |
| PATCH | /groups/{PROJECT-ID}/maintenanceWindows/{MW-ID} | Update one maintenance window with an end date in the future. |
| DELETE | /groups/{PROJECT-ID}/maintenanceWindows/{MW-ID} | Delete one maintenance window with an end date in the future. |
