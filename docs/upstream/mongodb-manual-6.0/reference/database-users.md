<!-- Converted from reference/database-users.txt (reStructuredText). Includes are inlined. -->

# Database Users

MongoDB uses database users to authenticate clients and grant varying levels of 
access to your deployment. You can assign roles to 
database users based on the required level of access and specific tasks they 
need to perform. 

## Use Cases

For example, you can create database users to: 

- Allow reads and writes to the database but restrict administrative access. 

- Assign administrative privileges to manage the database, perform 
  backups, and configure settings. 

- Grant read-only access for reporting and analytics purposes.

## Behavior

Database users and their permissions are governed by the roles that are 
assigned to them. You can use MongoDB's built-in roles or create custom 
roles.

### Database Users in Self-Managed Deployments

You can grant database users in self-managed deployments one or more roles. 
Roles grant users privileges to perform actions 
on specified resources. Users can perform actions on 
the following resources:

- Collections
- Databases
- Clusters

For more information, see built-in-roles.

To create and manage users in your self-managed deployment, use the 
`createUser` command or the `db.createUser()` method.

### Database Users in MongoDB Atlas

Database users in MongoDB Atlas have different built-in roles than self-managed
deployments. When you create a database user in MongoDB Atlas, Atlas built-in roles 
apply to all databases in your project. To learn more, see 
Altas Built-In Roles and Privileges.

**Note:**

Database users are separate from Atlas users. Database users have access to 
MongoDB databases, while Atlas users have access to the Atlas application 
itself. 

You can create database users, assign built-in roles, and create custom roles in 
the atlas-cli, atlas-admin-api-overview, or the Atlas UI. To learn more, see 
Add Database Users.

## Get Started

To create and manage database users, see:  

- manage-users-and-roles.
- Configure Database Users on Atlas.

## Details

### Authentication

When you create a user, you can specify the authentication mechanism that the
user uses to authenticate to the database. MongoDB supports the following 
authentication mechanisms:

|  | SCRAM | X.509 | Kerberos | LDAP | OIDC | AWS-IAM |
|---|---|---|---|---|---|---|
| MongoDB Community | ✓ | ✓ |  |  |  |  |
| MongoDB Enterprise | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| MongoDB Atlas (M10 and above) | ✓ | ✓ |  | ✓ | ✓ | ✓ |
| MongoDB Atlas (Shared Tier) | ✓ | ✓ |  |  |  | ✓ |
| MongoDB Atlas (Flex) | ✓ | ✓ |  |  |  | ✓ |

To learn more, see: 

- authentication.
- Configure Cluster Authentication and Authorization on Atlas.

### Authorization

MongoDB uses Role-Based Access Control (RBAC) to verify a user's access to 
resources and operations in the database. Although database users in MongoDB Atlas 
have different built-in roles than self-hosted deployments, the built-in roles 
for each type of deployment are built from the same set of 
privilege actions. 

To learn more, see: 

- authorization.
- Built-In Roles and Privileges on Atlas.
