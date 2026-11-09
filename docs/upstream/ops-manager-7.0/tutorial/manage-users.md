<!-- Converted from tutorial/manage-users.txt (reStructuredText). Includes are inlined. -->

# Ops Manager Access

To access an Ops Manager organization or the project within that organization,
an Ops Manager user must be a member of that organization. Depending on the
user's role in the organization, the Ops Manager
user may also need to be a member of the project to access a project.

An Ops Manager user can be a member of multiple projects and multiple
organizations. If an Ops Manager user is a member of a project, the user's
access to the project is determined their
role in the project.

Within an organization, you can group users into teams. Users can
belong to multiple teams. Teams can be assigned to multiple projects.
The team's project role sets the team members'
access to the project.

**Note:**

Ops Manager users are separate from MongoDB users.

## Considerations

You can register with and login using your Google account or using your
email account.

## Add Users to Ops Manager

**Note:** Invitations Can Be Disabled

When configuring your Ops Manager installation, you can disable
`Invitation Only Mode`. This allows users to create
accounts at the Ops Manager account registration page.

Unless you have disabled invitation mode, you must invite users to
Ops Manager projects and organizations. The following procedures result in
an email invitation being sent to the users you want to add. The
users must accept your invitation to join a project or organization.

- To invite a new user to a project, see add-users-to-project.
- To invite a new user to an organization, see
  add-users-to-org.

## Manage User Access to an Organization

**Note:** Required Permissions

To perform any of the following actions, you must have the
`Organization Owner` role.

### Add Users to an Organization

**Step 1: Navigate to the Users tab for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Access Manager in the sidebar, or click
   Access Manager in the navigation bar, then click
   your organization.

#. If it is not already displayed, click the Users tab.

**Step 2: Specify User.**

a. Select Invite Users from the Manage
   button menu.

b. From the Add Users page, enter the new user's
   email address in the combo box.

   After typing in the email address, either press
   Enter or click on the email address beneath the
   New User header under the combo box.

c. Repeat for any additional users.

**Step 3: Choose the roles for the new Users.**

By default, each user is given the `Organization Member`
role. To change or add additional roles for each user, click the
role dropdown menu, then select the checkboxes for each role you want the user to have in the organization.

**Step 4: Invite the Users.**

Click Add Users to Organization.

Ops Manager sends an e-mail to the selected users inviting them to join
the project. Invited users do not have access to the project until
they accept the invitation. Invitations expire after 30 days.

### View Active Users and Pending Invitations in an Organization

To view users in an organization:

**Step 1: Navigate to the Users tab for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Access Manager in the sidebar, or click
   Access Manager in the navigation bar, then click
   your organization.

This page lists:

- Users who are members of your Ops Manager organization.
- Pending users who have not accepted to the invitation to join the
  organization or project within the organization.

**Step 2: To cancel an invitation, click trash-alt to the right of the pending user.**

### Edit User's Role in an Organization

To edit roles through Ops Manager for the organization:

**Step 1: Navigate to the Users tab for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Access Manager in the sidebar, or click
   Access Manager in the navigation bar, then click
   your organization.

#. If it is not already displayed, click the Users tab.

**Step 2: Click Edit Permissions next to the organization you want to modify.**

**Step 3: Select the new role or roles for the user from the menu.**

**Step 4: Click the checkmark to save.**

### Remove Users from an Organization

 

**Note:**

You cannot remove the last `Organization Owner` from an
organization.

**Step 1: Navigate to the Users tab for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Access Manager in the sidebar, or click
   Access Manager in the navigation bar, then click
   your organization.

#. If it is not already displayed, click the Users tab.

**Step 2: Click trash-alt to the right of the user.**

**Step 3: Click Remove User from Organization.**

## Manage Team Access to an Organization

In an organization, you can group its users into teams to facilitate
adding and granting roles to multiple users to projects. You assign
project access at the team level. All users in the team share the same
project access.

Organization users can belong to multiple teams.

**Note:** Required Permissions

To perform any of the following actions, you must have the
`Organization Owner` role.

### Create a Team

**Note:**

There is an upper limit of 250 teams per organization.

**Step 1: Navigate to the Teams tab for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Access Manager in the sidebar, or click
   Access Manager in the navigation bar, then click
   your organization.

#. Click the Teams tab.

**Step 2: Create a new team.**

#. Click Create Team.

#. From the Create a Team page, enter the your team name
   in the Name Your Team box. The name must be unique
   within an organization.

#. To add existing organization users to the team, click in the
   Add Members box and either start typing their Ops Manager
   username or click on the name of a user that appears in 
   the combo box.

#. Click Create Team to confirm.

### Manage Team Members

**Step 1: Navigate to the Teams tab for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Access Manager in the sidebar, or click
   Access Manager in the navigation bar, then click
   your organization.

#. Click the Teams tab.

**Step 2: Add or remove users from a team.**

Click the name of the team you wish to modify.

a. Click Add Members.

b. Type the name or email of the user from the combo box. 

   You can only add users who are part of the organization. 

   Users who have not accepted an invitation to join the
   organization cannot be added as team members.

c. Click Add Members.

d. Repeat for additional team members.

Click trash-alt to the right of the member.

Removing a user from the team removes the user's project
assignments granted by the team membership.

If a user is assigned to a project through both a team and
individual assignment, removing the user from a team does not
remove the user's assignment to that project. 

### Rename a Team

**Step 1: Navigate to the Teams tab for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Access Manager in the sidebar, or click
   Access Manager in the navigation bar, then click
   your organization.

#. Click the Teams tab.

**Step 2: Rename the team.**

For the team you wish to rename:

a. Click `ellipsis` in the Actions column.

#. Click Rename Team.

#. Enter a new name for the team. 

   The team name must be unique within the organization.

#. Click Rename Team.

### Delete a Team

**Step 1: Navigate to the Teams tab for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Access Manager in the sidebar, or click
   Access Manager in the navigation bar, then click
   your organization.

#. Click the Teams tab.

**Step 2: Delete the team.**

For the team you wish to delete:

a. Click trash-alt next to the team that you want to delete.

#. Confirm that you wish to proceed with team deletion.

   For users belonging the team, deleting a team removes the
   users' project assignments granted by that team membership.

## Manage Application Access to an Organization

**Note:** Required Permissions

To manage API (Application Programming Interface) Keys for an Organization, you must have the
`Organization Owner` role.

To learn how to manage an Application's Access to an Organization
using API (Application Programming Interface) Keys, see:

- Create an API Key in an Organization
- View the Details of an API Key in an Organization
- Change an API Key in an Organization
- Delete an API Key from an Organization

## Manage Access to a Project

**Note:** Required Permissions

To perform any of the following actions, you must have either the
`Project Owner` or `Project User Admin` role.

### View Who Can Access a Project

To view which users, teams, or API (Application Programming Interface) Keys can access a project:

**Step 1: Navigate to the Users tab for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Access Manager in the sidebar, or click
   Access Manager in the navigation bar, then click
   your organization.

#. If it is not already displayed, click the Users tab.

**Step 2: Click the tab for Users, Teams, or API Keys to see the appropriate access.**

Each tab lists the project's users, teams, or API (Application Programming Interface) Keys along with
their project roles and corresponding
actions.

### View Active Users and Pending Invitations to Project

**Step 1: Navigate to the Users tab for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Project menu in the navigation bar.

#. Click Access Manager in the navigation bar, then click
   your project.

The Users tab also lists any outstanding invitations to
users to join the project and any requests from users who want to join
the project. A user can request to join a project when they first
register for Ops Manager.

Individual users are ordered by status. They appear in the following
sequence:

a. Users currently in your project.
#. Users with pending invitations to join your project.
#. Users requesting to join your project.

Ops Manager displays the Name of users who have not accepted
their invitation as Pending User and their role as
--invite sent--.

**Step 2: To cancel an invitation, click trash-alt to the right of the pending user.**

### Add Users or Teams to a Project

**Note:**

There is an upper limit of 250 users per team.

**Step 1: Navigate to the Users tab for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Project menu in the navigation bar.

#. Click Access Manager in the navigation bar, then click
   your project.

#. If it is not already displayed, click the Users tab.

**Step 2: Specify User or Team.**

- To add an individual user:

  a. Select Invite Users from the Manage
     button menu.

  b. From the Add Users page, enter the new user's
     email address in the combo box.

     After typing in the email address, you must either press
     Enter or click on the email address beneath the
     New User header under the combo box.

  c. Repeat for any additional users.

- To add a team:

  a. Select Create Team from the Manage
     button menu.

  b. Enter the team's name in the Name Your Team box.

  c. Enter the new team member's email address or [Jira](https://jira.mongodb.org) username
     in the Add Members combo box.

     After typing in the email address, either press
     Enter or click on the email address in the combo
     box.

  d. Repeat for any additional team members.

**Step 3: Choose the new roles for the User or Team.**

By default, each user and team is given the ``Project
Member`` role. To change or add additional roles for each user or
team, click on the role dropdown menu, then select the checkboxes for
each role you want the user or team to
have in the project.

All team members share the roles assigned to the team on this
project.

**Step 4: Invite the Users or Create the Teams.**

- For a new user, click Add Users to Project.

  Ops Manager sends an e-mail to the selected users inviting them to join
  the project. Invited users do not have access to the project until
  they accept the invitation. Invitations expire after 30 days.

- For a new team, click Create Team.

**Note:**

If the added user does not belong to the project's organization,
Ops Manager adds the user to the organization.

### Remove Users or Teams from a Project

**Note:**

You cannot remove the last `Project Owner` from an
organization.

**Step 1: Navigate to the Users tab for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Project menu in the navigation bar.

#. Click Access Manager in the navigation bar, then click
   your project.

#. If it is not already displayed, click the Users tab.

**Step 2: Navigate to the appropriate tab for the resource you want to remove:**

- If it is not already displayed and you want to remove a user, click
  the Users tab.

- If you want to remove a team, click the Teams tab.

**Step 3: Click trash-alt to the right of the user or team to remove.**

**Step 4: Confirm the removal.**

- To confirm a user removal, click
  Remove User from Organization.

- To confirm a team removal, click
  Delete Team."

### Edit a User's or Team's Role in a Project

To assign roles to any user in any group, you must have either the
Global User Admin role or Global
Owner role.

You can assign roles either through Ops Manager, as described here, or
through an LDAP server after you have
set up LDAP integration and created LDAP groups
for your Ops Manager roles.

To edit roles through Ops Manager, for the project:

**Step 1: Navigate to the Users tab for your organization.**

a. If it is not already displayed, select your desired organization
   from the `office` Organizations menu in the
   navigation bar.

#. Click Access Manager in the sidebar, or click
   Access Manager in the navigation bar, then click
   your organization.

#. If it is not already displayed, click the Users tab.

**Step 2: Click Edit Permissions next to the organization you want to modify.**

**Step 3: Select the new role or roles for the user from the menu.**

**Step 4: Click the checkmark to save.**

#### Assign Ops Manager Roles with LDAP

To assign roles through an LDAP server, you must set up LDAP
integration and create LDAP
groups for your Ops Manager roles. You must also have the permissions described in
assign-roles-to-users.

For LDAP authentication, the welcome form includes the ability to assign
LDAP groups to the Ops Manager group-level and global roles.

1. Configure LDAP authentication.

2. Create groups on your LDAP server for each of the available Ops Manager
   group-level and global roles.

To assign LDAP groups to Ops Manager roles:

1. Click the Admin link at the top right of the Ops Manager page.

2. Click General and then click Projects.

3. Click the pencil icon at the far right of a group name. Edit the
   Roles interface by adding the appropriate LDAP group name to its
   corresponding Ops Manager group name.

Because Ops Manager does not update role assignments stored in your LDAP server,
assign roles by assigning users to groups in your LDAP server.

Configure global roles in the `conf-mms.properties` configuration
file.

## Manage Application Access to a Project

**Note:** Required Permissions

To manage API (Application Programming Interface) Keys for an Organization, you must have the
`Project User Admin` role.

To learn how to manage a Application's Access to an Project using API (Application Programming Interface)
Keys, see:

- Create an API Key for a Project
- View the Details of an API Key in a Project
- Change an API Key's Roles in a Project
- Delete an API Key from a Project
