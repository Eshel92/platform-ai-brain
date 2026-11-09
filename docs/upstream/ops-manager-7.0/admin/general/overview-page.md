<!-- Converted from admin/general/overview-page.txt (reStructuredText). Includes are inlined. -->

# Overview Page

This page starts with the System Overview, a dashboard that
lists the following statistics about this Ops Manager instance:

|  |  |
|---|---|
| Active Projects | Number of projects that have active MongoDB Agents. |
| Total Projects | Number of projects that have been created. |
| Total Users | Number of users that have been created. |
| Enabled Hosts | Number of `mongod` and `mongos` processes being actively monitored. |
| Total Page Views | Number of page views served over time. |
| Diagnostic Archive | Link to download the Diagnostic Archive for the Ops Manager instance in `.tar` or `.zip` format. |

Following the dashboard, three tabs contain the following data:

|  |  |
|---|---|
| Servers | Hosts that serve the `mongod`, `mongos`, and MongoDB Agents for the Ops Manager instance and the MongoDB databases that it manages and monitors. Each replica set has a unique color across hosts. |
| MongoDB Processes | List of MongoDB databases that this Ops Manager instance manages and monitors. |
| System Warnings | Global Alerts that monitored MongoDB databases return to the Ops Manager instance. |
