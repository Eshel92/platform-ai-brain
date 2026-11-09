<!-- Converted from reference/api/usage.txt (reStructuredText). Includes are inlined. -->

# MongoDB Server Usage

This section describes how to manage your server types. You can group
virtual hosts into physical hosts and discover your current server
usage.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Required Roles

The API Key requires the `Global Owner` role to manage server
usage.

## Endpoints

The following lists the endpoints available for the server usage
resource.

| Method | Endpoint | Description |
|---|---|---|
| `POST` | /usage/dailyCapture | Generates snapshot of usage for the processes Ops Manager manages. |
| `GET` | /usage/report | Generates a compressed report of server usage in a given timeframe. |
| `GET` | /usage/assignments | Retrieves all host assignments. |
| `GET` | /usage/groups/{groupId}/hosts | Retrieves all host assignments for one project. |
| `GET` | /usage/groups/{groupId}/defaultServerType | Retrieve one default server type for one project. |
| `PUT` | /usage/groups/{groupId}/defaultServerType | Update one default server type for one project. |
| `PUT` | /usage/hosts/{hostId} | Update one default server type for one host. |
| `GET` | /usage/organizations/{orgId}/hosts | Retrieves all host assignments for one organization. |
| `GET` | /usage/organizations/{orgId}/defaultServerType | Retrieve one default server type for one organization. |
| `PUT` | /usage/organizations/{orgId}/defaultServerType | Update one default server type for one organization. |
| `GET` | /usage/groups | Retrieves a list of all physical and virtual hosts that Ops Manager manages. This list includes each physical hosts' server type. |
| `GET` | /usage/groups/{physicalHostId} | Retrieves a list of all physical and virtual hosts that Ops Manager manages identified with the physical host's ID. This list includes each physical host's server type. |
| `POST` | /usage/groups | Create one new physical host and bind one or more virtual hosts to that physical host. |
| `PUT` | /usage/groups/{physicalHostId} | Replace one physical host and its bindings to one or more virtual hosts. |
| `DELETE` | /usage/groups/{physicalHostId} | Remove one physical host from Ops Manager |
