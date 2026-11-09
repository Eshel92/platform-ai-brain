<!-- Converted from tutorial/manage-mongodb-users.txt (reStructuredText). Includes are inlined. -->

# Manage MongoDB Users

 

When you select an Authentication Mechanism for your Ops Manager project, 
this enables access control for all managed deployments in your Ops Manager
project.

With access control enabled, clients must authenticate to the MongoDB
process as MongoDB users. Once authenticated, these users only have
privileges granted by their assigned roles. You can assign MongoDB's
built-in roles to a user as well
as custom roles.

You can create MongoDB users before or after enabling accessing
control, but your MongoDB instances do not require user credentials if
access control is not enabled.

**Important:**

MongoDB users are separate from Ops Manager users. MongoDB users have access to MongoDB
databases, while Ops Manager users access the Ops Manager application itself.

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

## Add One MongoDB User

**Note:** Ops Manager Uses Default Hashing Iterations for User Credentials

When you create a MongoDB user via Ops Manager, it uses the default
number of iterations for 
`SCRAM-SHA-1`
(10,000) and `SCRAM-SHA-256`
(15,000) to hash user credentials. If you want to use different
values, create the user in MongoDB directly.

**Step 1: Navigate to the MongoDB Users tab for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Security tab.
#. Click MongoDB Users.

**Step 2: Click the Add New User button.**

**Step 3: Complete the user account fields.**

* - Field

  - Description

* - Identifier

  - 
    - In the first field, enter the database on which the user
      authenticates.

    - In the second field, enter a username on that database.

    Together, the database and username uniquely identify the
    user. Though the user has just one authentication database,
    the user can have privileges on other databases. You grant
    those privileges when assigning the user roles.

    If you are authenticating with an external system, like
    Kerberos or an LDAP server, add users to the
    `$external` database.

* - Roles

  - Enter any available user-defined roles and built-in
    roles into this box. The combo 
    box provides a list of existing roles when you click in it.

* - Password

  - Enter the user's password.

    **Important:**

    If you specified `$external` as the database in the
    Identifier, you do not need to specify a
    password for the new user.

* - Authentication Restrictions

  - 
    a. Click Add Entry.

    b. Add one or more IP (Internet Protocol) addresses and/or CIDR (Classless Inter-Domain Routing) blocks in 
       either the Client Source or Server 
       Address boxes. Separate multiple addresses or blocks with 
       commas.

       - Client Source restricts which addresses this 
         user can authenticate and use the given roles.

       - Server Address restricts the addresses this 
         user can authenticate and has the given roles.

    c. Click Save.

    d. To add another entry, click Add Entry.

**Step 4: Click Add User.**

**Step 5: Click Review & Deploy to review your changes.**

**Step 6: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

## Edit One MongoDB User Details

**Note:** Ops Manager Uses Default Hashing Iterations for User Credentials

When you edit a MongoDB user via Ops Manager, it uses the default
number of iterations for 
`SCRAM-SHA-1`
(10,000) and `SCRAM-SHA-256`
(15,000) to hash user credentials. If you want to use different
values, update the user in MongoDB directly.

**Step 1: Navigate to the MongoDB Users tab for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Security tab.
#. Click MongoDB Users.

**Step 2: Click Edit next to the user you want to modify.**

**Step 3: Edit the user's information.**

* - Field

  - Description

* - Identifier

  - These values cannot be edited.

* - Roles

  - Enter any available user-defined roles and built-in
    roles into this box. The combo 
    box provides a list of existing roles when you click in it.

    To remove a role, click the `x` to the left of that role.

* - Password

  - Enter the user's password.

    **Important:**

    If you specified `$external` as the database in the
    Identifier, you do not need to change this 
    value.

* - Authentication Restrictions

  - To add an authentication restriction:

    a. Click Add Entry.

    b. Add one or more IP (Internet Protocol) addresses or CIDR (Classless Inter-Domain Routing) blocks in 
       either the Client Source or Server 
       Address boxes. Separate multiple addresses or blocks with 
       commas.

       - Client Source restricts which addresses this 
         user can authenticate and use the given roles.

       - Server Address restricts the addresses this 
         user can authenticate and has the given roles.

    c. Click Save.

    d. To add another entry, click Add Entry.

    To remove an authentication restriction:

    a. Click the `x` to the right of the authentication 
       restriction.

**Step 4: Click Save Changes.**

**Step 5: Click Review & Deploy to review your changes.**

**Step 6: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

## Manage or Unmanage MongoDB Users

**Step 1: Navigate to the MongoDB Users tab for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Security tab.
#. Click MongoDB Users.

**Step 2: Click Refresh to discover any unmanaged users in your deployments.**

This shows all MongoDB users
present in all managed deployments for the Ops Manager project and any potential
conflicts.

**Step 3: Select users to manage or unmanage.**

Set the Sync switch to `Yes` for each MongoDB user you
want Ops Manager to manage. To manage all MongoDB users for the Ops Manager project, click the
Sync All link.

Set the Sync switch to `No` to unmanage the MongoDB
user.

| Current Sync State | New Sync State | What Changes |
|---|---|---|
| `NO` | `YES` | Ops Manager now manages the user. If there are any potential conflicts with other discovered users, Ops Manager presents you with the option to resolve conflicts. |
| `YES` | `NO` | Ops Manager no longer manages the user. WARNING: If Enforce Consistent Set is `YES`, Ops Manager deletes the user from all MongoDB databases that Ops Manager currently manages for this project. If Enforce Consistent Set is `NO`, Ops Manager no longer manages the users in that MongoDB database, but you can manage these users through a direct connection to that database. |

**Step 4: Click Review & Deploy to review your changes.**

**Step 5: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

**Step 6: Click Refresh to verify the desired users have been removed from your deployments.**

## Remove a MongoDB User

The following procedure deletes the MongoDB user from all the project's
managed MongoDB deployments. See also
manage-unmanage-mongodb-users.

**Step 1: Navigate to the MongoDB Users tab for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Security tab.
#. Click MongoDB Users.

**Step 2: Set the Enforce Consistent Set toggle to `YES`.**

**Step 3: Set the Sync setting for the users to be deleted to `OFF`.**

**Step 4: Click Delete next to the user to delete.**

**Step 5: Click Review & Deploy to review your changes.**

**Step 6: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

**Step 7: Click Refresh to verify the desired users have been removed from your deployments.**
