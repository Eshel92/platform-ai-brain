<!-- Converted from admin/general/projects-page.txt (reStructuredText). Includes are inlined. -->

# Projects Page

The Projects page in the Admin interface lists
`projects`, their creation dates, and their last pings
from agents.

## View a Project's Details

To view a project's details:

1. Click Admin, General, and 
   Projects.

#. Click the project's name.

## View a Project's Organization Details

To view a project's organization details:

1. Click Admin, General, and 
   Projects.

#. Click the organization's name next to the project name.

## Download a Diagnostic Archive

You can download a diagnostic archive for debugging and
troubleshooting. To learn more, see download-diagnostic-archives.

## Edit a Project's Backup Configuration

From the Jobs page, you can assign Backup resources to a
particular `project`. To learn more, see 
admin-manage-backup-resources.

1. Click Admin, General, and 
   Projects.

#. In the Actions column for a project, click 
   `ellipsis`, then click Backup Configuration.

#. Edit the backup configuration and click Save Changes.

## Edit a Project's Tags

A project can have up to 10 tags. Tags follow these rules:

- Are case-sensitive

- Can contain these characters:

  - `A` through `Z`
  - `0` through `9`
  - `.` (period)
  - `_` (underscore)
  - `-` (dash)

- Are limited to 32 characters

To edit a project's tags:

1. Click Admin, General, and 
   Projects.

#. In the Actions column for a project, click 
   `ellipsis`, then click Edit Tags.

## Edit a Project's  Metric Data Retention Policy

To edit a project's metric data retention policy:

1. Click Admin, General, and 
   Projects.

#. In the Actions column for a project, click
   `ellipsis`, then click
   Monitoring Data Retention.

#. Change the retention levels as desired. Increasing the
   retention period for a granularity level requires more
   storage on the Ops Manager Application Database. To learn more about monitoring
   data retention, see the default monitoring data retention
   values per
   `day`,
   `hour`,
   and
   `minute`.

## Edit a Project's LDAP (Lightweight Directory Access Protocol) Groups

To edit the LDAP groups that correspond to a project's roles:

To learn how to associate LDAP groups with project roles, see
the Associate LDAP groups with project roles
step.

**Note:**

You can perform this procedure only if you enabled LDAP (Lightweight Directory Access Protocol)
authentication for Ops Manager.
