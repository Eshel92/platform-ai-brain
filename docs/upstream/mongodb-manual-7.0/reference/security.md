<!-- Converted from reference/security.txt (reStructuredText). Includes are inlined. -->

# Security Reference for Self-Managed Deployments

The following lists the security related methods available in
`mongosh` as well as additional
security reference material.

## Security Methods in `mongosh`

### User Management and Authentication Methods

| Name | Description |
|---|---|
| `db.auth()` | Authenticates a user to a database. |
| `db.changeUserPassword()` | Changes an existing user's password. |
| `db.createUser()` | Creates a new user. |
| `db.dropUser()` | Removes a single user. |
| `db.dropAllUsers()` | Deletes all users associated with a database. |
| `db.getUser()` | Returns information about the specified user. |
| `db.getUsers()` | Returns information about all users associated with a database. |
| `db.grantRolesToUser()` | Grants a role and its privileges to a user. |
| `db.removeUser()` | Deprecated. Removes a user from a database. |
| `db.revokeRolesFromUser()` | Removes a role from a user. |
| `db.updateUser()` | Updates user data. |
| `passwordPrompt()` | Prompts for the password as an alternative to specifying passwords directly in various `mongosh` user authentication/management methods. |

   

### Role Management Methods

| Name | Description |
|---|---|
| `db.createRole()` | Creates a role and specifies its privileges. |
| `db.dropRole()` | Deletes a user-defined role. |
| `db.dropAllRoles()` | Deletes all user-defined roles associated with a database. |
| `db.getRole()` | Returns information for the specified role. |
| `db.getRoles()` | Returns information for all the user-defined roles in a database. |
| `db.grantPrivilegesToRole()` | Assigns privileges to a user-defined role. |
| `db.revokePrivilegesFromRole()` | Removes the specified privileges from a user-defined role. |
| `db.grantRolesToRole()` | Specifies roles from which a user-defined role inherits privileges. |
| `db.revokeRolesFromRole()` | Removes inherited roles from a role. |
| `db.updateRole()` | Updates a user-defined role. |

   

## Security Reference Documentation

/reference/system-roles-collection
   Describes the content of the collection that stores user-defined
   roles.

/reference/system-users-collection
   Describes the content of the collection that stores users'
   credentials and role assignments.

/reference/resource-document
   Describes the resource document for roles.

/reference/privilege-actions
   List of the actions available for privileges.
