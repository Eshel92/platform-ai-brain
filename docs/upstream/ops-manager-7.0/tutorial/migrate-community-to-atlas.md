<!-- Converted from tutorial/migrate-community-to-atlas.txt (reStructuredText). Includes are inlined. -->

# Migrate a MongoDB Community Deployment to Atlas

## Overview

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

If you use MongoDB Community Edition
but can't use general Atlas Live Migration 
due to network restrictions, you can migrate your MongoDB deployments to 
Atlas via Cloud Manager. To live migrate data from 
your MongoDB deployments to clusters in Atlas using Cloud Manager:

1. Add your deployments to Cloud Manager or Ops Manager.
#. Add credentials for Monitoring.
#. Follow the live migration process to Atlas.

For detailed steps, see cc-to-atlas-procedure.

## Prerequisites

Before you begin the live migration process from MongoDB Community 
to Atlas, you must:

- Have an existing deployment in 
  MongoDB Community Edition.

- Start a free trial of
  `Cloud Manager`.

## Considerations

### Credentials for Monitoring

When you add your MongoDB Community deployment to Cloud Manager 
or Ops Manager, you need to add credentials for Monitoring only, 
not for Automation or Backup. Adding your deployment for Monitoring 
imports your deployment's metadata into Cloud Manager or Ops Manager
to help with the Live Migration process. It does not import your 
deployment's actual data.

To learn more about authentication 
credentials, see add-existing-mongodb-processes-auth.

### Setup Considerations

You can use Cloud Manager to migrate your MongoDB deployments.

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

For deployments running MongoDB 6.0.5 or later, you can only use Cloud Manager,
not Ops Manager, to monitor them if you want to live migrate (push) them
to Atlas. You can migrate such deployments to Atlas
using live migration (pull). For a detailed overview of live migration
options, see Migrate to Atlas.

## Procedure

Perform this procedure for each of your MongoDB deployments.

**Step 1: Add your deployment to Cloud Manager or Ops Manager.**

Follow the procedure to add-existing-mongodb-hosts. 

**Step 2: Add credentials for Monitoring.**

To add credentials for Monitoring:

a. Create the credentials to the deployment. See 
   Required Access for Monitoring.
#. Add the credentials based on your project's authentication mechanism. 
   See add-auth-credentials-imported-deployment. 

**Note:**

If you're adding your MongoDB deployment 
to monitoring so that you can live migrate it 
to Atlas, you don't need to add credentials for 
Automation and Backup.
To learn more, see add-existing-mongodb-processes-auth.

**Step 3: Follow the Live Migration Process to Atlas.**

To migrate your deployment to Atlas once you've added it
to Cloud Manager or Ops Manager, follow the workflow in 
Migrate a Deployment to Atlas.
