<!-- Converted from reference/api/users.txt (reStructuredText). Includes are inlined. -->

# Users

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

The `users` resource allows you to create and update users and
retrieve user information. This resource also provides an endpoint 
for creating the first user in a system and retrieving a 
`public API key` for use in future API calls. The endpoint for
creating the first user is the only endpoint you can use without 
first having an API key.

## Endpoints

The following endpoints are available for `users`.

| Method | Endpoint | Description |
|---|---|---|
| GET | /users/{USER-ID} | Retrieve one user by their user ID. |
| GET | /users/byName/{USER-NAME} | Retrieve one user by their name. |
| POST | /users | Create one new user. |

|  |  |  |
|---|---|---|
| POST | /unauth/users | Create the first Ops Manager user. |
| PATCH | /users/{USER-ID} | Update one existing user. |
| DELETE | /users/{USER-ID} | Delete one Ops Manager user. |

**See also:**

/reference/api/organizations/organization-get-all-users
