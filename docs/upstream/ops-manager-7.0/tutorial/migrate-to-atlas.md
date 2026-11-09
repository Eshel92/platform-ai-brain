<!-- Converted from tutorial/migrate-to-atlas.txt (reStructuredText). Includes are inlined. -->

# Migrate from Ops Manager to Atlas

**Important:** Live Migration (push) Deprecated or Not Supported for Source Deployments Managed or Monitored by Ops Manager

- For source deployments running any MongoDB 6.0.+ versions, where the
  deployments are managed or monitored by Ops Manager, live migration (push)
  is not supported.
- For source deployments running any MongoDB 5.0 and earlier versions,
  where the deployments are managed or monitored by Ops Manager, live
  migration (push) is deprecated.
- For source deployments running MongoDB 6.0.+, where the deployments
  are monitored by Cloud Manager, live migration (push) is supported.
  To learn more, see Live Migrate Your MongoDB Cluster Monitored by Cloud Manager to Atlas.

## Overview

To live migrate data from the Ops Manager-monitored deployments to
clusters in Atlas, you:

1. Add your deployment to Ops Manager if you haven't already done so.
#. Add credentials to Monitoring.
#. Prepare a cluster in MongoDB Atlas.
#. Provision a migration host in Ops Manager and connect Ops Manager to Atlas.
#. Start the live migration process in Atlas.

You begin the process in Atlas, by running the live migration wizard.
Depending on the stage in the process, you perform the live migration steps either
in Atlas or in Ops Manager. See lm-workflow. 

To live migrate your MongoDB Community deployments to 
Atlas using Ops Manager, see migrate-community-to-atlas.

## Restrictions

You can't select an `M0` free cluster or `M2/M5` shared cluster
as the source or target for Live Migration. To migrate data from an
`M0` free cluster or `M2/M5` shared cluster to a paid cluster,
see Modify a Cluster.

## Supported Platforms

The list of supported platforms depends on which type of live migration
you are using:

- For live migrations of MongoDB 6.0.17+ or 7.0.13+
  clusters monitored by Cloud Manager to Atlas,
  see [mongosync platforms](https://www.mongodb.com/docs/cluster-to-cluster-sync/current/installation) to review
  the list of supported platforms for the migration host.

- For live migrations of source clusters running MongoDB earlier than
  6.0.17, the live migration to Atlas
  is supported for all
  platforms on which you can provision a migration host.

  Provisioning of the migration host is not supported on Windows or macOS.
  You can still live migrate your data from a Windows-based deployment
  to Atlas if you provision your migration host on one of its
  supported platforms. You can't live migrate your data from a macOS-based
  deployment to Atlas.

## Prerequisites

Before you begin the live migration process, follow these prerequisites.

### Add Your Deployment to Ops Manager

Follow the procedure to add-existing-mongodb-hosts. 

### Add Credentials for Monitoring

When you add your  deployment to Ops Manager, you need to add credentials for Monitoring only,  not for Automation or Backup. Adding your deployment for
Monitoring  imports your deployment's metadata into Ops Manager to help with the live migration process. It doesn't import your deployment's actual data. To
learn more about authentication credentials, see add-existing-mongodb-processes-auth.

To add credentials for Monitoring:

1. Create the credentials to the deployment. See 
   Required Access for Monitoring.
#. Add the credentials based on your project's authentication mechanism. 
   See add-auth-credentials-imported-deployment. 

**Note:**

If you're adding your MongoDB deployment to monitoring so that you can live migrate it to Atlas, you don't need to add credentials for 
Automation and Backup. To learn more, see add-existing-mongodb-processes-auth.

### Request an External IP Address

Request an external IP address for Ops Manager from your network administrator.
When you are ready to live migrate data, Atlas
uses this address for a link-token it generates.
When you run live migration, you push the data from a live deployment
in Ops Manager to a provisioned cluster in Atlas using the
link-token. You generate this link-token in
Atlas in Stage 1 of the live migration process.
To learn more, see
Live Migrate Your Data from Ops Manager or Cloud Manager.

### Consider Configuring a VPC Peering Connection or Private Endpoints

For information about support for VPC peering connections and private endpoints,
see the MongoDB Atlas documentation for your type of live migration:

- Live Migrate Your MongoDB 6.0.17 or Later Cluster Monitored by Cloud Manager to Atlas
- Live Migrate Your Data from Ops Manager or Cloud Manager

**Important:**

Sharded clusters, multi-region clusters, and multi-cloud
clusters don't support live migration through private endpoints.
Private endpoints are supported ONLY for live migration of replica sets
deployed within a single cloud provider and single region.

### Create a Cluster in Atlas

Perform these tasks in Atlas:

- Create an Atlas account.
- Create an Atlas organization.
- Create a project
  in this organization.
- Create a new cluster
  in your project.

## Workflow for Live Migration

The following diagram describes the stages in the live migration workflow.

(Figure: /images/live-migration-stages.png)
      provision a migration host, and start live migration."
:width: 700px
:align: center

The stages in the live migration workflow are:

- **Stage 1: Link with Atlas**. Perform this step in Atlas,
  after provisioning a cluster.

  a. In the left-side panel of your organization's page, click 
     Live Migration.
  #. Select Migrate from Ops Manager or Cloud Manager and start
     the live migration wizard.
  #. If you are migrating from MongoDB Community using Ops Manager, read and
     accept the Ops Manager Migration Agreement.
  #. In the Generate Link-Token step of the wizard, specify
     the external IP address for Ops Manager that you obtained from your
     service administrator. See Prerequisites.

- **Stage 2: Provision Migration Host**.
  
  - In Ops Manager, provision a Migration Host.
    A migration host is a dedicated MongoDB Agent that orchestrates the
    live migration process from Ops Manager to Atlas.

  - In the Live Migration: Connect to Atlas section of your
    Ops Manager organization's Settings page, select
    Connect to Atlas and enter the
    the link-token that you created in Atlas.

- **Stage 3: Start the Migration**. In Atlas, follow the
  steps in the wizard to start the live migration process.

To learn more, see Live Migrate Your Data from Ops Manager or
Cloud Manager.
