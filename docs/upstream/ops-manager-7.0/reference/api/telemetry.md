<!-- Converted from reference/api/telemetry.txt (reStructuredText). Includes are inlined. -->

# Telemetry

Telemetry collection gathers usage information about your Ops Manager
installation and sends it to MongoDB. Ops Manager
enables collecting and sending telemetry data by default.

**Important:**

This feature is available starting in Ops Manager 8.0.17 and 7.0.20.

To learn more about telemetry behavior and the data that Ops Manager 
collects, see Telemetry Overview.

## Endpoints

The following lists the endpoints available for telemetry.

| Endpoint | Method | Description |
|---|---|---|
| Retrieve Telemetry Data | GET | Retrieve telemetry collection status and configuration details. |
| Toggle Telemetry Status | PATCH | Enable or disable telemetry collection for your Ops Manager installation. |

## Required Roles

All telemetry endpoints require the `Global Owner` role.
