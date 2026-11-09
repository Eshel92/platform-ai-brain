<!-- Converted from reference/api/third-party-integration-settings.txt (reStructuredText). Includes are inlined. -->

# Third-Party Integration Settings

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

## Ops Manager Endpoints

**Important:**

Each project can have only one configuration per
`{INTEGRATION-TYPE}`.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

The following endpoints are available for managing
third-party service integrations.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /groups/{GROUP-ID}/integrations | Get all third-party integration configurations for the project associated with `{GROUP-ID}`. |
| `GET` | /groups/{GROUP-ID}/integrations/{INTEGRATION-TYPE} | Get a specific third-party integration configuration for `{INTEGRATION-TYPE}` for the project associated with `{GROUP-ID}`. |
| `POST` | /groups/{GROUP-ID}/integrations/{INTEGRATION-TYPE} | Add a new third-party integration configuration for `{INTEGRATION-TYPE}` to the project associated with `{GROUP-ID}`. |
| `PUT` | /groups/{GROUP-ID}/integrations/{INTEGRATION-TYPE} | Replace the third-party integration configuration for `{INTEGRATION-TYPE}` with a new configuration, or add a new configuration if there is no configuration for `{INTEGRATION-TYPE}`, to the project associated with `{GROUP-ID}`. |
| `DELETE` | /groups/{GROUP-ID}/integrations/{INTEGRATION-TYPE} | Remove the third-party integration configuration for `{INTEGRATION-TYPE}` from the project associated with `{GROUP-ID}`. |

## Prometheus Endpoints

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/prometheus/v1.0/`

The following endpoints are available for managing the
Prometheus integration.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /groups/{GROUP-ID}/discovery | Returns the latest targets for the project associated with `{GROUP-ID}`. |
