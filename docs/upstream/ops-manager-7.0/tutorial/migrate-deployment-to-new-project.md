<!-- Converted from tutorial/migrate-deployment-to-new-project.txt (reStructuredText). Includes are inlined. -->

# Migrate a MongoDB Deployment to a New Project

You can migrate a MongoDB deployment from one Ops Manager project to 
another project.

## Considerations

Historic metrics for the MongoDB deployment don't migrate to the new 
project.

## Procedure

**Step 1: Download snapshots.**

If you have backup enabled and want to retain snapshots:

a. Download any snapshots that you want to keep:

   - Download the snapshots for a replica set.
   - Download the snapshots for a sharded cluster.

#. Stop all backups.

   **Important:**

   All existing snapshots remain available for download until they 
   expire, but Ops Manager captures no new snapshots.

**Step 2: Prepare backup components.**

If you want backup enabled for your MongoDB deployment in the new 
project, prepare your backup components.

**Step 3: Prepare the old project.**

a. Deactivate the backup and monitoring MongoDB Agent functions in the old project.

#. Unmanage the MongoDB deployment in the old project, but continue to monitor it.

**Step 4: Prepare the new project.**

a. Create a new project to use as the 
   destination project.

#. Click Settings in the left navigation.

#. Note the Project ID value on the 
   Project Settings tab.

#. Create a new Agent API key.

**Step 5: Prepare the MongoDB Agent.**

**Note:**

If you have multiple deployments in your project and a 
MongoDB Agent installed only on the hosts that you plan to move, 
you must install new agents on servers that you will not move to 
the new project.

a. Stop the MongoDB Agent.

#. Edit the MongoDB Agent configuration file to update the 
   `mmsGroupId` and `mmsApiKey` settings with the 
   values from for the new project.

#. (Optional) If the new project is a new Ops Manager, update the 
   mmsbaseurl setting.

#. Start the MongoDB Agent.

   The MongoDB deployment servers should appear on the 
   Servers and Agents tabs.

**Step 6: Migrate the MongoDB deployment.**

a. Activate the backup and monitoring MongoDB Agent functions in the new project.

#. Add the MongoDB deployment to your new project.

#. (Optional) Start backups.

**Step 7: Remove the old project.**

**Warning:**

This step permanetly deletes your old project and its related 
artifacts.

a. Terminate all backups in the old project.

   **Important:**

   If you don't terminate all backups in the old project, all 
   existing snapshots remain available for download until they 
   expire and occupy disk space. You can't remove the MongoDB 
   deployment and delete the old project unless your terminate all 
   backups.

#. Completely remove the MongoDB deployment from the old project.

#. Delete the old project.
