<!-- Converted from reference/api/feature-control-policies.txt (reStructuredText). Includes are inlined. -->

# Feature Control Policies

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

Feature Control Policies allow you to enable or disable certain MongoDB
features based on your site-specific needs. Use these resources to view
and update Feature Control Policies via the API.

## Required Roles

To use these endpoints, grant the following roles to an Project
API Key:

| Role | Possible Action |
|---|---|
| `Project Owner` | Retrieve or update a feature control policy. |
| Any authenticated user | Retrieve the list of available policies for a project. |

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /groups/{PROJECT-ID}/controlledFeature | Retrieve the Feature Control Policies for one Project. |
| `PUT` | /groups/{PROJECT-ID}/controlledFeature | Update the Feature Control Policies for one Project. |
| `GET` | /groups/availablePolicies | Retrieve the available Feature Control Policies. |
