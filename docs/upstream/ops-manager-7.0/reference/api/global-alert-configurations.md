<!-- Converted from reference/api/global-alert-configurations.txt (reStructuredText). Includes are inlined. -->

# Global Alert Configurations

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

The `globalAlertConfigs` resource retrieves and updates alert
configurations for global
alerts.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following endpoints are available for `globalAlertConfigs`.

| Method | Endpoint | Description |
|---|---|---|
| GET | /globalAlertConfigs | Retrieve all global alert configurations. |
| GET | /globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}/alerts | Retrieve all open alerts triggered by one alert configuration. |
| GET | /globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID} | Retrieve one alert configuration. |
| POST | /globalAlertConfigs | Create one alert configuration. |
| PUT | /globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID} | Update one global alert configuration. |
| PUT | /globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID} | Enable or disable one global alert configuration. |
| DELETE | /globalAlertConfigs | Delete one global alert configuration. |
| POST | /globalAlertConfigs/{GLOBAL-ALERT-CONFIG-ID}/{NOTIFICATION-ID}/test | Test a notification method in a global alert configuration. |
