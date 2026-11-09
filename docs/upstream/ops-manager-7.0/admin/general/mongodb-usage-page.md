<!-- Converted from admin/general/mongodb-usage-page.txt (reStructuredText). Includes are inlined. -->

# MongoDB Usage Page

**Important:** Enable MongoDB Usage UI and MongoDB Usage Data Collection

If `MongoDB Usage UI` is set to `true`, this page
displays information about the MongoDB Usage collected via daily
snapshots.

If this page contains no data, you can populate it with data with one of two methods:

- Set `MongoDB Usage Data Collection` to `true` and wait
  for the daily usage snapshot to generate within 24 hours.

- Request the
  Daily Usage Snapshot API resource.

## Sections of the Page

This page has two parts: a usage summary and a table of MongoDB deployments.

### Usage Summary

This card contains a section for each server type that your Ops Manager deployment between the dates selected.

Each server type section contains three headings:

| Heading | Description |
|---|---|
| RAM Used | Greatest amount of RAM used on the date with the greatest use. |
| Total Nodes | Count of nodes used on the date with the greatest use. |
| Date | When this server type had its greatest use. |

The *date of greatest use* depends on the server type:

| Server Type | Date of Greatest Use Measured |
|---|---|
| RAM Pool | When the greatest amount of RAM was used for all hosts running that server type. |
| All other server types | When the greatest number of all hosts of that server type were running. |

### Deployments Table

This table contains each server and describes the server type
associated, as well as important information about the server's
processes and their deployments.

To build this report, Ops Manager:

1. Takes daily snapshots of all running MongoDB processes.
2. Merges all snapshots for the selected range of dates.

If you stop or terminate a server before creating the report, that
server remains part of the report in the date range you selected.

**Example:**

1. You start Process A on Host A on 20 April.
#. On 4 May, Ops Manager takes a snapshot of Process A.
#. On 5 May, you shut down Process A.
#. On 6 May, Ops Manager takes a new snapshot.
#. On 10 May, you create report for the range of 1 to 6 May.
#. This report includes Process A.

To exclude the shutdown process, create a report that doesn't include
dates when that process ran.

## Actions

From this page, you can:

### Determine Server Type Usage over Time

To review which server types were in use for your MongoDB Enterprise
installations during a given time period:

1. Select a start date from the From box.

2. Select an end date from the To box.

The Usage Summary updates automatically with the applicable values.
This usage summary covers all hosts, organizations, and projects.

### Apply New Server Type to Multiple Hosts

To change the server type of multiple hosts at once:

1. Check the box at the left the columns containing the hosts to which
   you wish to apply the new server type.

2. Select the desired server type from the
   Apply a Server Type dropdown.

This action updates these hosts to have that server type for all
*existing* and *future* usage snapshots. The new server type does not
apply to the timeframe you specified using the date selectors.

### Apply New Server Type to Specific Host

To change the server type of one host, use the dropdown in its row
under the Server Type column.

This action updates this host to have that server type for all
*existing* and *future* usage snapshots. The new server type does not
apply to the timeframe you specified using the date selectors.

### Download a Usage Report

To report on your MongoDB Enterprise usage:

1. (Optional) Clear Redact sensitive information if you
   want include all IP addresses, hostnames, organization names, and
   project names in the report.

#. Click Download Report to create a usage report.

#. Attach this report to the MongoDB email displayed on the
   MongoDB Usage page.

## Procedures

### Create One Virtual Machine Group

**Step 1: Navigate to the MongoDB Usage page.**

a. Click the Admin link in the upper right corner of the
   console.

b. Click the General tab.

c. Click the MongoDB Usage page.

**Step 2: Create a Virtual Machine Group.**

a. Click checkboxes to the left of the hostnames representing the
   physical host you want to combine into a single license.

b. Click Add to Virtual Machine Group.

   If you don't have a Virtual Machine Group, Ops Manager displays a notice that you
   need to create one.

c. Click Create Virtual Machine Group.

   Ops Manager displays the Create Virtual Machine Group.

d. Type a name for the VMG (Virtual Machine Group) in the Group name box.

e. Select the Server Type from the Select a server type
   menu.

f. Click Create.

   Ops Manager displays the MongoDB Usage page with a banner
   that explains that it has created the VMG (Virtual Machine Group).

### Rename One Virtual Machine Group

**Step 1: Navigate to the MongoDB Usage page.**

a. Click the Admin link in the upper right corner of the
   console.

b. Click the General tab.

c. Click the MongoDB Usage page.

**Step 2: Rename the Virtual Machine Group.**

a. To the right of the Virtual Machine Group that you want to modify, click
   Modify Group.

   Ops Manager displays the Modify Virtual Machine Group modal.

b. Type a new name for the VMG (Virtual Machine Group) in the Rename the group
   box.

c. Click Update or click Cancel to leave the
   host as it is.

   If you renamed the host, Ops Manager displays the MongoDB
   Usage page with the renamed VMG (Virtual Machine Group).

### Delete One Virtual Machine Group

**Step 1: Navigate to the MongoDB Usage page.**

a. Click the Admin link in the upper right corner of the
   console.

b. Click the General tab.

c. Click the MongoDB Usage page.

**Step 2: Delete one Virtual Machine Group.**

a. To the right of the Virtual Machine Group that you want to modify, click
   Modify Group.

   Ops Manager displays the Modify Virtual Machine Group modal.

b. Click Delete.

   Ops Manager displays the Delete Virtual Machine Group.

c. Click Delete to confirm the removal or click
   Cancel to leave the host.

   If you deleted the host, Ops Manager displays the MongoDB
   Usage page without the deleted VMG (Virtual Machine Group).

### Remove One Host from One Virtual Machine Group

**Step 1: Navigate to the MongoDB Usage page.**

a. Click the Admin link in the upper right corner of the
   console.

b. Click the General tab.

c. Click the MongoDB Usage page.

**Step 2: Remove a host from the Virtual Machine Group.**

a. If you can't find the VM (Virtual Machine) that you want to remove from the VMG (Virtual Machine Group),
   type part of its name in the Search box.

b. Click Remove Host to the left of the VM (Virtual Machine) you want to
   remove from the Virtual Machine Group.

   Ops Manager displays the Remove from group modal.

c. Click Remove to confirm the removal or click
   Cancel to leave the VM (Virtual Machine) in the VMG (Virtual Machine Group).

   If you removed the host, Ops Manager displays the
   MongoDB Usage page with:

   - the remaining VM (Virtual Machine)\s in the original VMG (Virtual Machine Group) and
   - the removed VM (Virtual Machine) as separate entry in the deployments table.

### Add More VMs to One Virtual Machine Group

**Step 1: Navigate to the MongoDB Usage page.**

a. Click the Admin link in the upper right corner of the
   console.

b. Click the General tab.

c. Click the MongoDB Usage page.

**Step 2: Add a host to a Virtual Machine Group.**

a. Click checkboxes to the left of the hostnames representing the
   virtual hosts you want to combine into a single license. These
   hostnames can't belong to any existing VMG (Virtual Machine Group).

b. Click Add to Virtual Machine Group.

c. Click the name of the VMG (Virtual Machine Group) to which you want to add the selected
   VM (Virtual Machine).

   Ops Manager adds the VM (Virtual Machine) to the VMG (Virtual Machine Group) immediately without further
   confirmation.
