<!-- Converted from reference/database-users.txt (reStructuredText). Includes are inlined. -->

# Database Users

MongoDB uses database users to authenticate clients and grant
access to your deployment. Assign roles to
database users based on the level of access and tasks they need to
perform.

## Use Cases

Create database users to:

- Allow reads and writes to the database but restrict
  administrative access.

- Assign administrative privileges to manage the database, perform
  backups, and configure settings.

- Grant read-only access for reporting and analytics.

## Behavior

Roles govern database user permissions. Use MongoDB's
built-in roles or create custom roles.

### Database Users in Self-Managed Deployments

Grant database users in self-managed deployments one or more roles.
Roles grant users privileges to
perform actions on specified resources.

Users can perform actions on the following resources:

- Collections
- Databases
- Clusters

To create and manage users in your self-managed deployment, use the
`createUser` command or the `db.createUser()`
method.

### Database Users in MongoDB Atlas

Database users in MongoDB Atlas have different built-in roles than
self-managed deployments. When you create a database user in
MongoDB Atlas, Atlas built-in roles apply to all databases in your
project.

**Note:**

Database users are separate from Atlas users. Database users
access MongoDB databases. Atlas users access the Atlas
application.

Create database users, assign built-in roles, and create custom
roles in the `Atlas CLI`,
atlas-admin-api-overview, or the Atlas UI.
To learn more, see Add Database Users.

## Get Started

To create and manage database users, see:  

- manage-users-and-roles.
- Configure Database Users on Atlas.

## Details

### Authentication

Specify the authentication mechanism when you create a user. MongoDB
supports the following authentication mechanisms:

|  | SCRAM | X.509 | Kerberos | LDAP | OIDC | AWS-IAM |
|---|---|---|---|---|---|---|
| MongoDB Community | ✓ | ✓ |  |  |  |  |
| MongoDB Enterprise | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| MongoDB Atlas (M10 and above) | ✓ | ✓ |  | ✓ | ✓ | ✓ |
| MongoDB Atlas (Free and Flex Tiers) | ✓ | ✓ |  |  |  | ✓ |
| MongoDB Atlas (Flex) | ✓ | ✓ |  |  |  | ✓ |

To learn more, see:

- authentication
- Configure Cluster Authentication and Authorization on
  Atlas

### Authorization

MongoDB uses Role-Based Access Control to verify user access to
resources and operations. Database users in MongoDB Atlas have different
built-in roles than self-hosted deployments. However, MongoDB builds
all built-in roles from the same set of privilege actions.

To learn more, see:

- authorization
- Built-In Roles and Privileges on Atlas
