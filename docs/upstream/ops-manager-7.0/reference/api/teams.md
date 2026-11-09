<!-- Converted from reference/api/teams.txt (reStructuredText). Includes are inlined. -->

# Teams

The `teams` resource provides access to retrieve MongoDB Ops Manager
teams.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /orgs/{ORG-ID}/teams | Retrieves all teams to which the authorized user has access. |
| `GET` | /orgs/{ORG-ID}/teams/{TEAM-ID} | Get the team with ID `{TEAM-ID}` in the organization associated with `{ORG-ID}`. |
| `GET` | /orgs/{ORG-ID}/teams/byName/{TEAM-NAME} | Get the team with name `{TEAM-NAME}` in the organization associated with `{ORG-ID}`. |
| `GET` | /orgs/{ORG-ID}/teams/{TEAM-ID}/users | Get all users in the team associated with `{TEAM-ID}` in the organization associated with `{ORG-ID}`. |
| `POST` | /orgs/{ORG-ID}/teams | Create a single team in the organization associated with `{ORG-ID}}`. |
| `PATCH` | /orgs/{ORG-ID}/teams/{TEAM-ID} | Rename a team in an organization. |
| `PATCH` | /groups/{PROJECT-ID}/teams/{TEAM-ID} | Update roles for a team in a project. |
| `POST` | /orgs/{ORG-ID}/teams/{TEAM-ID}/users | Add a user from the organization associated with `{ORG-ID}` to the team with ID `{TEAM-ID}`. |
| `DELETE` | /orgs/{ORG-ID}/teams/{TEAM-ID}/users/{USER-ID} | Remove the specified user from the specified team. |
| `DELETE` | /orgs/{ORG-ID}/teams/{TEAM-ID} | Delete the team with ID `{TEAM-ID}` from the organization specified to `{ORG-ID}`. |
| `DELETE` | /groups/{PROJECT-ID}/teams/{TEAM-ID} | Remove the specified team from the specified group. |
