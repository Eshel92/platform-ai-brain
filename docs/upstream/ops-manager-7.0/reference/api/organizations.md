<!-- Converted from reference/api/organizations.txt (reStructuredText). Includes are inlined. -->

# Organizations

The `orgs` resource provides access to return, create, update, or
remove MongoDB Ops Manager organizations.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /orgs | Return the list of all organizations to which the authenticated user belongs. |
| GET | /orgs/{ORG-ID} | Return information about the organization associated with `{ORG-ID}`. |
| GET | /orgs/{ORG-ID}/groups | Return all projects in the organization associated with `{ORG-ID}`. |
| GET | /orgs/{ORG-ID}/users | Return all users in the specified organization. |
| POST | /orgs | Create one organization. |
| PATCH | /orgs/{ORG-ID} | Update one organization. |
| DELETE | /orgs/{ORG-ID} | Remove the organization associated with `{ORG-ID}`. |
| POST | /orgs/{ORG-ID}/invites/{INVITATION-ID} | Create one invitation. |
| DELETE | /orgs/{ORG-ID}/invites/{INVITATION-ID} | Remove one invitation. |
| GET | /orgs/{ORG-ID}/invites | Return the list of all invitations. |
| GET | /orgs/{ORG-ID}/invites/{INVITATION-ID} | Return one invitation. |
| PATCH | /orgs/{ORG-ID}/invites/{INVITATION-ID} | Update one invitation by ID. |
| PATCH | /orgs/{ORG-ID}/invites | Update one invitation. |
