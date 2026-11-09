<!-- Converted from tutorial/manage-users-and-roles.txt (reStructuredText). Includes are inlined. -->

# Manage Users and Roles on Self-Managed Deployments

The following examples cover user and role management under
the MongoDB authorization model for self-managed deployments. To
create a user, see create-users.

## Prerequisites

If you have enabled access control 
for your deployment, you must authenticate as a user with the required 
privileges specified in each section. To perform the operations listed 
in this tutorial, user administrators require the 
`userAdminAnyDatabase` role, or `userAdmin` role 
in the specific databases. For details on adding a user administrator 
as the first user, see enable-access-control 
   

## Create a User-Defined Role

**Note:**

To create user-defined roles in MongoDB Atlas, see 
add-mongodb-roles in the MongoDB Atlas documentation.

MongoDB provides built-in roles for common
access patterns. If built-in roles don't cover your required
privileges, create a user-defined role.

Except for roles created in the `admin` database, a role can only
include privileges that apply to its database and can only inherit from
other roles in its database.

A role created in the `admin` database can include privileges that
apply to the `admin` database, other databases or to the
cluster resource, and can inherit from roles
in other databases as well as the `admin` database.

To create a new role, use the `db.createRole()` method,
specifying the privileges in the `privileges` array and the 
inherited roles in the `roles` array.

MongoDB uses the combination of the database name and the role 
name to uniquely define a role. Each role is scoped to the 
database in which you create the role, but MongoDB stores all 
role information in the `admin.system.roles` collection in 
the `admin` database.

## Prerequisites

To create a role in a database, you must have:

- the `createRole` action on
  that database resource.

- the `grantRole` action on
  that database to specify privileges for the new role as well as to
  specify roles to inherit from.

Built-in roles `userAdmin` and
`userAdminAnyDatabase` provide `createRole` and
`grantRole` actions on their respective resources.

To create a role with `authenticationRestrictions` specified, you
must have the `setAuthenticationRestriction`
action on the
database resource which the role is
created.

To add custom user-defined roles with `mongosh`, see the 
following examples:

- create-role-to-manage-ops.
- create-role-for-mongostat.
- create-role-for-system-views.

## Create a Role to Manage Current Operations

The following example creates a role named `manageOpRole` which
provides only the privileges to run both `db.currentOp()` 
and `db.killOp()`. [#built-in-roles1]_

**Note:**

Users do not need any specific privileges to view or kill their own 
operations on `mongod` instances. See `db.currentOp()` 
and `db.killOp()` for details.

**Step 1: Connect to MongoDB with the appropriate privileges.**

Connect to `mongod` or `mongos` with the privileges
specified in the define-roles-prereq section.

The following procedure uses the `myUserAdmin` created in
/tutorial/enable-authentication.

```javascript
mongosh --port 27017 -u myUserAdmin -p 'abc123' --authenticationDatabase 'admin'
```

The `myUserAdmin` has privileges to create roles in the `admin`
as well as other databases.

**Step 2: Create a new role to manage current operations.**

`manageOpRole` has privileges that act on multiple databases as well
as the cluster resource. As such, you must
create the role in the `admin` database.

```javascript
use admin
db.createRole(
   {
     role: "manageOpRole", 
     privileges: [
       { resource: { cluster: true }, actions: [ "killop", "inprog" ] },
       { resource: { db: "", collection: "" }, actions: [ "killCursors" ] }
     ],
     roles: []
   }
)
```

The new role grants permissions to kill any operations.

**Warning:**

Terminate running operations with extreme caution. Only use
the `db.killOp()` method or `killOp` command to terminate operations initiated by clients
and *do not* terminate internal database operations.

## Create a Role to Run `mongostat`

The following example creates a role named `mongostatRole` that 
provides only the privileges to run `mongostat`.
[#built-in-roles2]_

**Step 1: Connect to MongoDB with the appropriate privileges.**

Connect to `mongod` or `mongos` with the privileges
specified in the define-roles-prereq section.

The following procedure uses the `myUserAdmin` created in
/tutorial/enable-authentication.

```javascript
mongosh --port 27017 -u myUserAdmin -p 'abc123' --authenticationDatabase 'admin'
```

The `myUserAdmin` has privileges to create roles in the `admin`
as well as other databases.

**Step 2: Create a new role to manage current operations.**

`mongostatRole` has privileges that act on the cluster
resource. As such, you must create the role in
the `admin` database.

```javascript
use admin
db.createRole(
   {
     role: "mongostatRole", 
     privileges: [
       { resource: { cluster: true }, actions: [ "serverStatus" ] }
     ],
     roles: []
   }
)
```

## Create a Role to Drop `system.views` Collection across Databases

The following example creates a role named
`dropSystemViewsAnyDatabase` that provides the privileges to 
drop the `system.views` collection in any database.

**Step 1: Connect to MongoDB with the appropriate privileges.**

Connect to `mongod` or `mongos` with the privileges
specified in the define-roles-prereq section.

The following procedure uses the `myUserAdmin` created in
/tutorial/enable-authentication.

```javascript
mongosh --port 27017 -u myUserAdmin -p 'abc123' --authenticationDatabase 'admin'
```

The `myUserAdmin` has privileges to create roles in the `admin`
as well as other databases.

**Step 2: Create a new role to drop the `system.views` collection in any database.**

For the role, specify a privilege that consists
of:

- an `actions` array that contains the
  `dropCollection` action, and

- a resource document that
  specifies an empty string (`""`) for the database and the string
  `"system.views"` for the collection. See
  resource-specific-collection for more information.

```javascript
use admin
db.createRole(
   {
     role: "dropSystemViewsAnyDatabase", 
     privileges: [
       {
         actions: [ "dropCollection" ],
         resource: { db: "", collection: "system.views" }
       }
     ],
     roles: []
   }
)
```

## Modify Access for an Existing User

**Note:**

To modify an existing database user's roles in MongoDB Atlas, 
see modify-mongodb-users in the MongoDB Atlas documentation.

### Prerequisites

- .. include:: /includes/access-grant-roles.rst

- .. include:: /includes/access-revoke-roles.rst

- .. include:: /includes/access-roles-info.rst

### Procedure

**Step 1: Connect to MongoDB with the appropriate privileges.**

Connect to `mongod` or `mongos` as a user with
the privileges specified in the prerequisite section.

The following procedure uses the `myUserAdmin` created in
/tutorial/enable-authentication.

```javascript
mongosh --port 27017 -u myUserAdmin -p 'abc123' --authenticationDatabase 'admin'
```

**Step 2: Identify the user's roles and privileges.**

To display the roles and privileges of the user to be modified, use the
`db.getUser()` and `db.getRole()` methods.

For example, to view roles for `reportsUser` created in
add-new-user, issue:

```javascript
use reporting
db.getUser("reportsUser")
```

To display the privileges granted to the user by the
`readWrite` role on the `"accounts"` database, issue:

```javascript
use accounts
db.getRole( "readWrite", { showPrivileges: true } )
```

**Step 3: Identify the privileges to grant or revoke.**

If the user requires additional privileges, grant to the user the
role, or roles, with the required set of privileges. If such a role
does not exist, create a new role
with the appropriate set of privileges.

To revoke a subset of privileges provided by an existing role: revoke
the original role and grant a role that contains only the required
privileges. You may need to create a new role if a role does not exist.

**Step 4: Modify the user's access.**

Revoke a role with the `db.revokeRolesFromUser()` method.
The following example operation removes the `readWrite`
role on the `accounts` database from the `reportsUser`:

```javascript
use reporting
db.revokeRolesFromUser(
    "reportsUser",
    [
      { role: "readWrite", db: "accounts" }
    ]
)
```

Grant a role using the `db.grantRolesToUser()`
method. For example, the following operation grants the
`reportsUser` user the `read` role on the
`accounts` database:

```javascript
use reporting
db.grantRolesToUser(
    "reportsUser",
    [
      { role: "read", db: "accounts" }
    ]
)
```

For sharded clusters, the changes to the user are instant on the
`mongos` on which the command runs. However, for other
`mongos` instances in the cluster, the user cache may wait
up to 10 minutes to refresh. See
`userCacheInvalidationIntervalSecs`.

## Modify the Password for an Existing User

**Note:**

To modify an existing MongoDB Atlas user's password, see 
modify-mongodb-users in the MongoDB Atlas documentation.

### Prerequisites

To modify the password of another user on a database, you must have the
`changePassword` action
on that database.

### Procedure

**Step 1: Connect to MongoDB with the appropriate privileges.**

Connect to the `mongod` or `mongos` with the privileges
specified in the change-password-prereq section.

The following procedure uses the `myUserAdmin` created in
/tutorial/enable-authentication.

```javascript
mongosh --port 27017 -u myUserAdmin -p 'abc123' --authenticationDatabase 'admin'
```

**Step 2: Change the password.**

Pass the user's username and the new password to the
`db.changeUserPassword()` method.

The following operation changes the `reporting` user's password to
`SOh3TbYhxuLiW8ypJPxmt1oOfL`:

```javascript
db.changeUserPassword("reporting", "SOh3TbYhxuLiW8ypJPxmt1oOfL")
```

**See also:**

change-password-custom-data

## View a User's Roles

**Note:**

To view a user's roles in MongoDB Atlas, see 
view-mongodb-users in the MongoDB Atlas
documentation.

### Prerequisites

To view another user's information, you must have the
`viewUser` action on the
other user's database.

Users can view their own information.

### Procedure

**Step 1: Connect to MongoDB with the appropriate privileges.**

Connect to `mongod` or `mongos` as a user with
the privileges specified in the prerequisite section.

The following procedure uses the `myUserAdmin` created in
/tutorial/enable-authentication.

```javascript
mongosh --port 27017 -u myUserAdmin -p 'abc123' --authenticationDatabase 'admin'
```

**Step 2: Identify the user's roles.**

Use the `usersInfo` command or `db.getUser()` method to
display user information.

For example, to view roles for `reportsUser` created in
add-new-user, issue:

```javascript
use reporting
db.getUser("reportsUser")
```

In the returned document, the `roles`
field displays all roles for `reportsUser`:

```javascript
...
"roles" : [
   { "role" : "readWrite", "db" : "accounts" },
   { "role" : "read", "db" : "reporting" },
   { "role" : "read", "db" : "products" },
   { "role" : "read", "db" : "sales" }
]
```

## View a Role's Privileges

**Note:**

To view a role's privileges in MongoDB Atlas, see 
view-mongodb-roles in the MongoDB Atlas documentation.

### Prerequisites

To view a role's information, you must be either explicitly granted the
role or must have the `viewRole` action on the role's database.

### Procedure

**Step 1: Connect to MongoDB with the appropriate privileges.**

Connect to `mongod` or `mongos` as a user with
the privileges specified in the prerequisite section.

The following procedure uses the `myUserAdmin` created in
/tutorial/enable-authentication.

```javascript
mongosh --port 27017 -u myUserAdmin -p 'abc123' --authenticationDatabase 'admin'
```

**Step 2: Identify the privileges granted by a role.**

For a given role, use the `db.getRole()` method, or the
`rolesInfo` command, with the `showPrivileges` option:

For example, to view the privileges granted by `read` role on
the `products` database, use the following operation, issue:

```javascript
use products
db.getRole( "read", { showPrivileges: true } )
```

In the returned document, the `privileges` and
`inheritedPrivileges` arrays. The
`privileges` lists the privileges directly
specified by the role and excludes those privileges inherited
from other roles. The `inheritedPrivileges`
lists all privileges granted by this role, both directly
specified and inherited. If the role does not inherit from other
roles, the two fields are the same.

```javascript
...
"privileges" : [
  {
    "resource": { "db" : "products", "collection" : "" },
    "actions": [ "collStats","dbHash","dbStats","find","killCursors","planCacheRead" ]
  },
  {
    "resource" : { "db" : "products", "collection" : "system.js" },
    "actions": [ "collStats","dbHash","dbStats","find","killCursors","planCacheRead" ]
  }
],
"inheritedPrivileges" : [
  {
    "resource": { "db" : "products", "collection" : "" },
    "actions": [ "collStats","dbHash","dbStats","find","killCursors","planCacheRead" ]
  },
  {
    "resource" : { "db" : "products", "collection" : "system.js" },
    "actions": [ "collStats","dbHash","dbStats","find","killCursors","planCacheRead" ]
  }
]
```
