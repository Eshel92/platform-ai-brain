<!-- Converted from organizations-projects.txt (reStructuredText). Includes are inlined. -->

# Organizations and Projects

**Important:** New

Ops Manager provides a new organizations and projects hierarchy to
help you manage your Ops Manager deployments. Groups are now
known as projects. You can create many projects in an
organization.

## Organizations

In the organizations and projects hierarchy, an organization can
contain many projects (previously referred to as groups). Under
this structure, you can:

- View all projects within an organization, create teams of users,
  and assign teams to projects. See /tutorial/manage-organizations.

- Connect to Atlas as part of live migration
  to Atlas. See Connect to Atlas.

## Projects

Groups are now projects. Previously, users managed
deployments by groups, where each group was managed separately even if
a user belonged to multiple groups.

### Existing Groups

If you have existing groups, organizations have been automatically
created for your groups (now projects), and your groups have been
placed under these organizations.

If your groups share the same billing settings, they have been placed
in the same organization.

### Deployments

Deployments are now associated with projects. As before, deployments
must have unique names within projects. See
/tutorial/manage-projects
and /tutorial/manage-project-settings.

## Teams

You can create teams of users and then assign teams of users to
projects. See /tutorial/manage-users.

## Invitations to Organizations and Projects

You can view and accept invitations to organizations
and projects. See /invitations.
