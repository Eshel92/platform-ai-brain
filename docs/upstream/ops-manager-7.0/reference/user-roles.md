<!-- Converted from reference/user-roles.txt (reStructuredText). Includes are inlined. -->

# Ops Manager Roles

Ops Manager roles allow you to grant users different levels of access to
Ops Manager. You can grant a user the privileges needed to perform a specific
set of tasks and no more.

If you use LDAP (Lightweight Directory Access Protocol) authentication for Ops Manager, you must:

1. Create LDAP (Lightweight Directory Access Protocol) groups for each available role that follows.
2. Assign users to these LDAP (Lightweight Directory Access Protocol) groups.

Neither the LDAP (Lightweight Directory Access Protocol) server nor Ops Manager synchronizes the groups and
roles without user intervention.

To assign user roles, see assign-roles-to-users. You can't
assign your own roles.

## Organization Roles

* - Organization Role
  - Privileges

* - .. authrole:: Organization Owner
  - An Ops Manager user with this organization role can:

    - Grants root access to the organization.

    - Grants `Project Owner` access to all projects in
      the organization, even if added to a project with a
      non-Owner role.

    - Use any privilege granted to any organization role.

    - Administer organization settings.

    - Add, edit, or delete users to the organization.

    - Delete the organization.

* - .. authrole:: Organization Project Creator
  - An Ops Manager user with this organization role can:

    - Create projects in the organization.

    - Use any privilege granted to the
      `Organization Member` role.

* - .. authrole:: Organization Read Only
  - An Ops Manager user with this organization role can grant read-only
    access to everything in the organization, including all projects
    in the organization.

* - .. authrole:: Organization Member
  - An Ops Manager user with this organization role can grant read-only
    access to the organization (settings, users, and billing) and
    the projects to which they belong.

    Within a project, an  `Organization Member`'s project
    role sets their project privileges.

    A `Project User Admin` or
    `Owner` can add a new Ops Manager user to a
    project. This also adds this new Ops Manager user to that project's
    organization.

## Project Roles

The following roles grant privileges within a project.

* - Project Role
  - Privileges

* - .. authrole:: Project Read Only
  - An Ops Manager user with this project role can view most project
    components, including all:

    - Activity
    - Operational data
    - Ops Manager Users
    - Ops Manager User roles.

    This user can't modify or delete anything.

* - .. authrole:: Project User Admin
  - An Ops Manager user with this project role can:

    - Add an existing Ops Manager user to a project. If the added user
      does not currently belong to the organization, the user will
      be added to the organization as well.

    - Invite a new Ops Manager user to a project. After the Ops Manager user
      accepts the invite, Ops Manager also adds this user to the
      organization.

    - Remove an existing project invitation.

    - Deny a user's request to join a project. This can deny
      the user access to the project depending on the user's role in
      the organization.

    - Remove a user from a project.

    - Modify a user's role within a project.

* - .. authrole:: Project Data Access Admin
  - An Ops Manager user with this project role can:

    - Use the Data Explorer.

      With the Data Explorer, the Ops Manager user
      with this role can:

      - View, create, and drop databases, collections, and indexes.

      - View, modify, and delete documents.

    - Use any privilege granted to the `Project Read Only`
      role.

    - Kill an operation in the
      Real Time Performance Panel.

    - View the sample query field values in the
      /tutorial/performance-advisor.

* - .. authrole:: Project Data Access Read/Write
  - An Ops Manager user with this project role can:

    - Use the Data Explorer. With the
      Data Explorer, the Ops Manager user with
      this role can:

      - View and create databases and collections.

      - View, modify, and delete documents.

      - View indexes.

    - View the sample query field values in the
      /tutorial/performance-advisor.

* - .. authrole:: Project Data Access Read Only
  - An Ops Manager user with this project role can:

    - View databases, collections, and indexes in the
      Data Explorer

    - View the sample query field values in the
      /tutorial/performance-advisor.

* - .. authrole:: Project Monitoring Admin
  - An Ops Manager user with this project role can:

    - Use any privilege granted to the `Project Read Only`
      role.

    - Administer alerts (create, modify, delete, enable/disable,
      acknowledge/unacknowledge).

    - Manage hosts (add, edit, delete).

    - Download Monitoring.

* - .. authrole:: Project Backup Admin
  - An Ops Manager user with this project role can:

    - Use any privilege granted to the `Project Read Only`
      role.

    - Manage backups,
      including:

      - Starting, stopping, and terminating backups.

      - Requesting restores.

      - Viewing and editing the namespaces filter.

      - Viewing and editing host passwords.

      - Modifying backup settings.

      - Generating SSH keys.

      - Downloading the MongoDB Agent.

* - .. authrole:: Project Automation Admin
  - An Ops Manager user with this project role can:

    - Use any privilege granted to the `Project Read Only`
      role.

    - View deployments.

    - Provision machines.

    - Edit configuration files.

    - Download the MongoDB Agent.

* - .. authrole:: Project Owner
  - An Ops Manager user with this project role can:

    - Use any privilege granted to any of the other project roles.

    - Configure the Backup
      service.

      A user with `Organization Owner` role has
      `Project Owner` access for all projects in the
      organization, even if added to a project with a non-Owner
      role.

## Global Roles

Global roles have all the same privileges as the equivalent
Organization and Project roles, except that they have these
privileges for all projects and organizations. They also have some
additional privileges as noted in the following table.

The following roles grant privileges for all projects and organizations.

* - Global Role
  - Description

* - .. authrole:: Global Read Only

  - Grants `Project Read Only` access to all projects
    and `Organization Read Only` for all organizations.
    The role additionally grants access to do the following:

    - View backups and other
      statistics through the admin console.

    - Global user search.

* - .. authrole:: Global User Admin

  - Grants `Project User Admin` access to all projects
    and all organizations. The role additionally grants access to
    do the following:

    - Manage console messages.

    - Send test emails, SMS messages, and voice calls.

    - Edit user accounts.

    - Manage LDAP group mappings for organization and project
      roles.

* - .. authrole:: Global Monitoring Admin

  - Grants `Project Monitoring Admin` access
    to all projects. The role additionally grants access to do
    the following:

    - View system statistics through the admin
      console.

* - .. authrole:: Global Backup Admin

  - Grants `Project Backup Admin` access to all
    projects. The role additionally grants access to do the
    following:

    - View system statistics through the admin
      console.

    - Manage blockstore, daemon, and oplog store configurations.

    - Move jobs between daemons.

    - Approve backups in awaiting provisioning state.

* - .. authrole:: Global Automation Admin

  - Grants `Project Automation Admin` access
    to all projects. The role additionally grants access to view
    system statistics through the admin console.

* - .. authrole:: Global Owner

  - Grants privileges from all roles combined except those
    required to access Data Explorer:

    - `Project Data Access Admin`
    - `Project Data Access Read/Write`
    - `Project Data Access Read Only`
