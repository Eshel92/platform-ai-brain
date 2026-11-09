<!-- Converted from tutorial/manage-mongodb-roles.txt (reStructuredText). Includes are inlined. -->

# Manage Custom Roles

Roles grant users access to MongoDB resources. By default, MongoDB
provides some built-in roles,
but if these roles cannot describe a desired privilege set, you can
create custom roles.

When you create a role, you specify the database to which it applies.
Ops Manager stores your custom roles on all MongoDB instances in your Ops Manager
project but uniquely identifies a role by the combination of the
database name and role name. If a database with that name exists on
multiple deployments within your Ops Manager project, the role applies to
each of those databases. If you create a role on the `admin`
database, the role applies to all `admin` databases in the
deployment.

Roles consist of privileges that grant access to specific actions on
specific resources. On most databases, a resource is the database or a
collection, but on the `admin` database a resource can be all
databases, all collections with a given name across databases, or all
deployments.

A role can inherit privileges from other roles in its database. A role
on the `admin` database can inherit privileges from roles in other
databases.

MongoDB roles are separate from Ops Manager roles.

## Considerations

### Managed Users and Roles

Any users or roles you choose to manage in an Ops Manager project have their
Synced value set to `Yes` and are synced to all
deployments in the project.

Any users or roles you do not choose to manage in an Ops Manager project have
their Synced value set to `No` and exist only in their
respective MongoDB deployments.

**Note:**

If you toggle Synced to `OFF` after import, any users
or roles you create are deleted.

### Consistent Users and Roles

If you enforce a consistent set of users and roles in your project,
Ops Manager synchronizes these users and roles across all deployments in that
project. Toggle Enforce Consistent Set to choose whether or
not to manage one set of users and roles:

### Enforce Consistent Set is `YES`

In a managed project, Ops Manager grants all of the users and roles access to
all deployments. All deployments that the Ops Manager project manages have
the same set of MongoDB users and roles.

Ops Manager limits the access to users and roles where you set
Synced to `Yes`. Ops Manager deletes all users and roles that Ops Manager project doesn't manage from the deployments in your project.

### Enforce Consistent Set is `NO`

In a managed project, Ops Manager allows each deployment to use its own set of MongoDB users and roles. Ops Manager doesn't need to manage these MongoDB users and roles. To manage these
users and roles, you must connect direct to the MongoDB
deployment.

Ops Manager grants managed MongoDB users and roles where you set
Synced to `Yes` access to all managed deployments.

Ops Manager limits access of unmanaged MongoDB users and roles, where you set
Synced to `No`, to those users' and roles' specific
deployments.

**Note:**

Enforce Consistent Set defaults to `NO`.

To learn how importing MongoDB deployments can affect managing users
and roles, see automation-updated-security-settings.

## Prerequisite

MongoDB access control
must be enabled
to apply roles. You can create roles before enabling accessing control
or after, but they don't go into effect until you enable access
control.

## Create a Custom MongoDB Role

**Step 1: Navigate to the MongoDB Roles tab for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Security tab.
#. Click MongoDB Roles.

**Step 2: Click Add New Role.**

**Step 3: In the Identifier field, enter the database on which to define the role and enter a name for the role.**

A role applies to the database on which it is defined and can grant
access down to the collection level. The combination of the role name
and its database uniquely identify that role. Complete the
Identifier fields to meet the authentication and
authorization methods you use:

* If you use neither LDAP authentication nor authorization, type the
  database name in the database
  Identifier field and the name you want for the role in the
  name Identifier field.

* If you use LDAP authentication, but not LDAP authorization, type
  `$external` in the database Identifier field and
  the name you want for the role in the name
  Identifier field.

* If you use any authentication method with LDAP Authorization, type
  `admin` in the database Identifier field and the
  LDAP Group DN in the name Identifier field.

  **Example:**

  In your LDAP server, you created an LDAP Group with a Distinguished
  Name of `CN=DBA,CN=Users,DC=example,DC=com`. If you want to create a
  DBA role in Ops Manager linked to this LDAP Group, type `admin` in the
  database Identifier field and
  `CN=DBA,CN=Users,DC=example,DC=com` in the name
  Identifier field.

**Step 4: Select the privileges to grant the new role.**

You can grant privileges in two ways:

To grant a new role all the privileges of one or more existing roles,
select the roles in the Inherits From field. The field
provides a drop-down list that includes both MongoDB
built-in roles and any custom roles you
have already created.

To grant specific privileges to the role, click ADD
PRIVILEGES FOR A RESOURCE.

In the Resource field, specify the resource to which to
apply the role. Select the database from the drop-down menu.
To specify the whole database, leave the field
blank. To specify a collection, enter the collection name. If the
resource is on the `admin` database, you can click
ADMIN and apply the role outside the `admin` database.

In the Available Privileges section, select the actions
to apply. For a description of each action, see Privilege
Actions in the MongoDB manual.

**Step 5: Click Add Privileges.**

**Step 6: Click Add Role.**

**Step 7: Click Review & Deploy to review your changes.**

**Step 8: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

## Edit a Custom Role

You can change a custom role's privileges. You cannot change its name
or database.

**Step 1: Navigate to the MongoDB Roles tab for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Security tab.
#. Click MongoDB Roles.

**Step 2: Click Edit next to the role you want to modify.**

**Step 3: Add or Remove privileges for that role.**

You can grant privileges in two ways:

To grant a new role all the privileges of one or more existing roles,
select the roles in the Inherits From field. The field
provides a drop-down list that includes both MongoDB
built-in roles and any custom roles you
have already created.

To grant specific privileges to the role, click ADD
PRIVILEGES FOR A RESOURCE.

In the Resource field, specify the resource to which to
apply the role. Select the database from the drop-down menu.
To specify the whole database, leave the field
blank. To specify a collection, enter the collection name. If the
resource is on the `admin` database, you can click
ADMIN and apply the role outside the `admin` database.

In the Available Privileges section, select the actions
to apply. For a description of each action, see Privilege
Actions in the MongoDB manual.

To remove an inherited role, click the x next to the role.
To remove a privilege, click the trash icon next to the privilege.

**Step 4: Click Save Changes.**

**Step 5: Click Review & Deploy to review your changes.**

**Step 6: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

## View Privileges for a Role

To view a role's privileges, click Deployment, then
the Security tab, then Roles,
then view privileges next to the role.

Each privilege pairs a resource with a set of
Privilege Actions. All roles
are assigned a database. Each
built-in role is assigned to
either `admin` database or every database.

## Remove a Custom Role

**Step 1: Navigate to the MongoDB Roles tab for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Security tab.
#. Click MongoDB Roles.

**Step 2: Set the Synced value to `No` next to the role that you want to delete.**

**Step 3: Click Unsync to verify.**

**Step 4: Click Review & Deploy to review your changes.**

**Step 5: Click Confirm & Deploy to deploy your changes.**

**Note:**

If Enforce Consistent Set is set to `Yes`, the
custom role is also removed from managed MongoDB processes. If
Enforce Consistent Set is set to `No`, you must
manually remove the role with the
dropRole command.
