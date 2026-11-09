<!-- Converted from reference/api/alerts.txt (reStructuredText). Includes are inlined. -->

# Alerts

The `alerts` resource allows you to retrieve and acknowledge
alerts.

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following lists the endpoints available for alerts.

| Method | Endpoint | Description |
|---|---|---|
| GET | /groups/{PROJECT-ID}/alerts | Get all alerts for a project. |
| GET | /groups/{PROJECT-ID}/alerts/{ALERT-ID} | Get the specified alert for a project. |
| PATCH | /groups/{PROJECT-ID}/alerts/{ALERT-ID} | Acknowledge or unacknowledge an alert. |
