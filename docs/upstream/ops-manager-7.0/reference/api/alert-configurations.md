<!-- Converted from reference/api/alert-configurations.txt (reStructuredText). Includes are inlined. -->

# Alert Configurations

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following lists the endpoints available for alert
configuration. An alert
configuration defines the
conditions that trigger an alert and the methods of notification.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /api/atlas/v1.0/alertConfigs/matchers/fieldNames | Get all field names that the `matchers.fieldName` parameter accepts when you create or update an Alert Configuration. |
| GET | /groups/{PROJECT-ID}/alertConfigs | Get all alert configurations for a project. |
| POST | /groups/{PROJECT-ID}/alertConfigs | Create an alert configuration |
| GET | /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID} | Get an alert configuration. |
| PUT | /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID} | Update an alert configuration. |
| PATCH | /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID} | Enable/disable an alert configuration. |
| DELETE | /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID} | Delete an alert configuration. |
| GET | /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}/alerts | Get all open alerts for an alert configuration. |
| POST | /groups/{PROJECT-ID}/alertConfigs/{ALERT-CONFIG-ID}/{NOTIFICATION-ID}/test | Test a notification method in an alert configuration. |
