<!-- Converted from tutorial/change-mongodb-version.txt (reStructuredText). Includes are inlined. -->

# Change the Version of MongoDB

You can upgrade or downgrade MongoDB versions within the same Feature
Compatibility Version (FCV) in Ops Manager sharded clusters,
replica sets, and standalone MongoDB instances
while maximizing the availability of your deployments.

You can add custom-built versions of MongoDB
for Ops Manager to download.

If Ops Manager doesn't manage your deployment, change the version of MongoDB manually.
To learn more, see upgrade tutorials for each MongoDB release.

**Note:** Ops Manager support for End of Life MongoDB versions

Ops Manager doesn't support Backup,
Monitoring, or Automation for versions earlier than MongoDB 3.6.

Ops Manager continues to support Automation, Backup, and Monitoring
using the MongoDB Agent for clusters running MongoDB 3.6 or later.

## Considerations

- Check the following documents for any considerations or 
  compatibility issues before changing a deployment's MongoDB version:

  - The MongoDB Release Notes

    **Warning:** Upgrades from MongoDB 5.0 to 6.0

    When you upgrade a sharded cluster from MongoDB 5.0 to 6.0, you
    must use the procedure on the
    Upgrade a Sharded Cluster to 6.0 page of the MongoDB
    Manual to refresh the cached routing table for each `mongos`.

  - The documentation for your driver.

  - /reference/mongodb-compatibility

- Plan the version change during a predefined maintenance window.

- Change the MongoDB version on a staging environment before changing a
  production environment. Your staging environment should mirror your
  production environment. This can help avoid compatibility issues 
  that may result in downtime for your production deployment.

- Follow the MongoDB release notes when 
  performing manual upgrades of replica sets and
  sharded clusters.

**Note:** Downgrading Limitations

You cannot downgrade a MongoDB deployment:

- From version 5.0 to any version before 4.4.0
- From version 4.4 to any version before 4.2.6

## Prerequisites

### Remove Incompatible MongoDB Features when Downgrading

If the MongoDB deployment has its Feature Compatibility Version
set to the same release series as its Version, you must first
manually downgrade the instance's featureCompatibilityVersion.

**seven-oh-to-six-oh:**

**Step 1: Unmanage, but continue to monitor, the deployment.**

**Step 2: Downgrade the Feature Compatibility Version.**

To downgrade your deployment from version 7.0 to 6.0, you 
must contact [support](https://support.mongodb.com/) for assistance. For 
more information, see [Downgrade 7.0 to 6.0](https://www.mongodb.com/docs/v7.0/release-notes/7.0-downgrade/).

**Note:**

This sets the `featureCompatibilityVersion` to `6.0`.

**Step 3: Import the deployment.**

1. Import the deployment back into 
   Ops Manager.

#. Edit the deployment in Ops Manager and select
   the downgraded version under the Version column.

**six-oh-to-five-oh:**

**Step 1: Unmanage, but continue to monitor, the deployment.**

**Step 2: **

Read the downgrade considerations
and take appropriate action for unsupported features.

**Step 3: Downgrade the Feature Compatibility Version.**

- `Downgrade the 6.0 Standalone Feature Compatibility Version to 5.0`
- `Downgrade the 6.0 Replica Set Feature Compatibility Version to 5.0`
- `Downgrade the 6.0 Sharded Cluster Feature Compatibility Version to 5.0`

**Note:**

This sets the `featureCompatibilityVersion` to `5.0`.

**Step 4: Import the deployment.**

1. Import the deployment back into 
   Ops Manager.

#. Edit the deployment in Ops Manager and select
   the downgraded version under the Version column.

**five-oh-to-four-four:**

**Step 1: Unmanage, but continue to monitor, the deployment.**

**Step 2: Downgrade the Feature Compatibility Version.**

- `Downgrade the 5.0 Standalone Feature Compatibility Version to 4.4`
- `Downgrade the 5.0 Replica Set Feature Compatibility Version to 4.4`
- `Downgrade the 5.0 Sharded Cluster Feature Compatibility Version to 4.4`

**Note:**

This removes any 5.0 incompatible features and sets the
`featureCompatibilityVersion` to `4.4`.

**Step 3: Import the deployment.**

1. Import the deployment back into 
   Ops Manager.

#. Edit the deployment in Ops Manager and select
   the downgraded version under the Version column.

**four-four-to-four-two:**

**Step 1: Unmanage, but continue to monitor, the deployment.**

**Step 2: Downgrade the Feature Compatibility Version.**

- `Downgrade the 4.4 Standalone Feature Compatibility Version to 4.2`
- `Downgrade the 4.4 Replica Set Feature Compatibility Version to 4.2`
- `Downgrade the 4.4 Sharded Cluster Feature Compatibility Version to 4.2`

**Note:**

This removes any 4.4 incompatible features
and sets the
`featureCompatibilityVersion` to `4.2`.

**Step 3: Import the deployment.**

1. Import the deployment back into 
   Ops Manager.

#. Edit the deployment in Ops Manager and select
   the downgraded version under the Version column.

## Procedure

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: On the line listing the deployment item, click Modify.**

**Step 3: Verify the desired version number is in the version list.**

In the Cluster Configuration section, the
Cluster Settings heading lists the processes with their
names, MongoDB versions, data directories and log files.

a. Scroll to the Cluster Settings heading.

b. Click the Version arrow for the first MongoDB process
   in the list. 

**Note:**

If you're running in local mode and don't see your desired version, you
can  Update the Version Manifest Manually.

To learn more, see Local Mode Configuration.

**Step 4: Change the version of MongoDB for the deployment.**

For each MongoDB process that you want to change:

a. Click the current version number for the process.
b. Click the desired version number.

**Step 5: (Optional) Update the `featureCompatibilityVersion`.**

If you are upgrading to a new major version, and wish to enable
features offered in the new major version, you must also update the
`featureCompatibilityVersion`.

For each MongoDB deployment that you want to change:

a. Click the current `featureCompatibilityVersion` for the
   deployment.
b. Click the value that matches the desired version number.

**Step 6: Click Save.**

**Step 7: Click Review & Deploy to review your changes.**

**Step 8: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.
