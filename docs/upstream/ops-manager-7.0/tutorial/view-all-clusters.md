<!-- Converted from tutorial/view-all-clusters.txt (reStructuredText). Includes are inlined. -->

# View All Clusters

The All Clusters view displays all deployments to which
the user belongs.

**Note:**

For an Ops Manager administrator, the view displays all deployments
to which the administrator has access, not just those to which
the administrator belongs. To change this behavior, see the
`mms.allclusters.onlyMembership` setting.

## Access All Clusters View

Click the All Clusters link at the top left corner of
Ops Manager Application to view all deployments that Ops Manager manages.

To find an organization, a
project, or a deployment, you can enter part of its
name in the search box.

Select the options within the dropdown menus to filter the displayed
deployment list.

The dropdown menus and their options include:

* - Menu
  - Options

* - Availability
  - 
    - All (*Default*)
    - Nodes Available
    - Some Nodes Available
    - No Primary
    - Has Warnings & Alerts

* - deployment Type
  - 
    - All (*Default*)
    - Standalones
    - Replica Sets
    - Sharded Clusters

* - MongoDB Version
  - 
    - All (*Default*)
    - <MongoDB Versions>
    - Inconsistent

* - Configuration settings
  - 
    - All (*Default*)
    - Auth OFF
    - Backup OFF
    - SSL (Secure Sockets Layer) OFF

If no Projects within an Organization match the filter criteria, then
that Organization will not appear in the results as well.

**Note:**

By default, deployment\s without any contact with a Monitoring for the last 6 months are not displayed. To display these
deployments, click Show Inactive Clusters.

## Deployment Details

The All Clusters view displays the deployments by
Organization/Projects.

The view displays the following information for each deployment:

| Field | Description |
|---|---|
| Name | The name of the deployment. |
| Version | MongoDB Version of the deployment. |
| Data Size | Size of the deployment data. |
| Nodes | Number of nodes in the deployment. |
| Backup | Backup enabled status. |
| SSL | TLS (Transport Layer Security)/SSL (Secure Sockets Layer) enabled status. |
| Auth | Authentication required status. |
| Alerts | Number of open alerts. |
