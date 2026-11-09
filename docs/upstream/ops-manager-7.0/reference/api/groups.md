<!-- Converted from reference/api/groups.txt (reStructuredText). Includes are inlined. -->

# Groups: API Endpoints for Projects

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

## Endpoints

### Manage Project Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /groups | Get All Projects for the Current User |
| `GET` | /groups/{PROJECT-ID} | Get One Project by Its ID |
| `GET` | /groups/byName/{GROUP-NAME} | Get One Project by Its Name |
| `GET` | /groups/byAgentApiKey/{AGENT-API-KEY} | Get One Project by Its Agent API Key |
| `POST` | /groups | Create One Project |
| `PATCH` | /groups/{PROJECT-ID}/ | Update One Project |
| `DELETE` | /groups/{PROJECT-ID} | Delete One Project |

### Manage Users in One Project Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /groups/{PROJECT-ID}/users | Get All Users in One Project |
| `POST` | /groups/{PROJECT-ID}/users | Add Users to One Project |
| `DELETE` | /groups/{PROJECT-ID}/users/{USER-ID} | Remove One User from One Project |

### Manage Invitations to One Project Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | /groups/{GROUP-ID}/invites/{INVITATION-ID} | Create One Invitation |
| `DELETE` | /groups/{GROUP-ID}/invites/{INVITATION-ID} | Delete One Invitation |
| `GET` | /groups/{GROUP-ID}/invites | Get All Invitations |
| `GET` | /groups/{GROUP-ID}/invites/{INVITATION-ID} | Get One Invitation |
| `PATCH` | /groups/{GROUP-ID}/invites/{INVITATION-ID} | Update One Invitation by ID |
| `PATCH` | /groups/{GROUP-ID}/invites | Update One Invitation |

### Manage Teams in One Project Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /groups/{PROJECT-ID}/teams | Get All Teams in One Project |
| `POST` | /groups/{PROJECT-ID}/teams | Add a Team or Teams to One Project |
| `DELETE` | /groups/{PROJECT-ID}/teams/{TEAM-ID} | Remove the specified team from the specified group. |

|  |  |  |
|---|---|---|
| `GET` | /groups?tag={TAG1}&tag={TAG2} | Get All Projects with Specific Tags for the Current User |
