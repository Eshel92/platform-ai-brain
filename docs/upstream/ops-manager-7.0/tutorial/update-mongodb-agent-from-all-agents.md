<!-- Converted from tutorial/update-mongodb-agent-from-all-agents.txt (reStructuredText). Includes are inlined. -->

# Update from all legacy Agents

You have a project with automated MongoDB deployments with Monitoring, Backup, or both and want to update to the MongoDB Agent.

**Note:** Review the Prerequisites First

If you want to start or continue using Automation to manage your
MongoDB deployments, please review the
/tutorial/install-mongodb-agent-prereq before updating to the
MongoDB Agent.

## Procedure

**Step 1: Log in to the Ops Manager Application.**

**Step 2: Unmanage Any Unique Indexes.**

If you upgrade from Ops Manager 4.0 to 4.2 or later, edit each
deployment to remove any
unique indexes from management.

Ops Manager 4.2 and later differs from 4.0 in how it manages index. To
view, create, or delete indexes after this upgrade, use Data
Explorer.

**Warning:**

Don't drop your unique indexes.
You need only remove them from management.

**Step 3: From the notification banner, click Update All Agents.**

The Update to MongoDB Agent page opens to start the
update process. The Introducing the MongoDB Agent step
displays. When you have finished reading this step, click
Next.

**Step 4: Add any existing configuration options for your legacy Agents that Automation did not manage.**

If Automation did not manage your Backup or Monitoring Agents, you
can add any Backup or Monitoring settings you had before at the
Add Custom Configuration Options for your MongoDB Agent
(Optional) step.

**Important:** Deployments using Kerberos Authentication

Don't add either of the following settings from the legacy Agents:

- `krb5Principal`
- `krb5Keytab`

Your legacy Agents authenticated with Kerberos as separate database
users. Because the MongoDB Agent combines the functions of the
legacy Agents, it employs a *single* database user. To upgrade to 
the MongoDB Agent and continue using Kerberos, you must:

1. Create a new Kerberos User Principal and database user for the
   MongoDB Agent.
#. Update the Agent authentication configuration in the Ops Manager Authentication &
   TLS settings with the new MongoDB Agent Principal and Keytab 
   files.

You can remove the legacy Monitoring and Backup Agent users after
updating to the MongoDB Agent. 

To add options that you had for your
Backup Agent and
Monitoring Agent:

a. Under the Backup Configurations section:

   i. Type the desired setting
      in the Setting box and its corresponding value in
      the Value box.

   #. To add more than one Setting, click the
      + Add Setting link. Another row appears.

   #. Repeat until all settings have been added.

b. Under the Monitoring Configurations section:

   i. Type the desired setting in the Setting
      box and the corresponding value in the
      Value box.

   #. To add more than one Setting, click the
      + Add Setting link. Another row appears.

   #. Repeat until all settings have been added.

c. Once you have added all the settings necessary for your deployment, click Next.

You can click the trash-alt to remove any settings that
you have added.

**Important:**

Ops Manager does not validate any of these settings. Make sure that the
settings and values are correct.

**Step 5: Update automated hosts to MongoDB Agent.**

If your project has hosts that use Automation, you can
update the Agents on those hosts to the MongoDB Agent.

a. Click Update All.

b. Wait until all hosts show Updated.

c. Click Next.

**Important:**

All authentication SCRAM, LDAP (Lightweight Directory Access Protocol), and Kerberos credentials from
legacy Agents are retained after the update. All `.pem` key
files are retained as well.

All credentials for the legacy Agents are migrated to the
MongoDB Agent.

The legacy Automation Agent credentials become the MongoDB Agent
credentials used for Automation. These credentials should not need
modification. However, if you need to modify them, navigate to
Deployment
arrow-right Security
arrow-right Settings
arrow-right Edit Settings.

The legacy Monitoring Agent credentials can be
modified from Deployment
arrow-right Processes
arrow-right `ellipsis`
arrow-right Monitoring Settings
arrow-right Credentials.

The legacy Backup Agent credentials can be
modified from Continuous Backup
arrow-right Overview
arrow-right Deployment to Backup
arrow-right `ellipsis` under Options column
arrow-right Edit Credentials.

**Step 6: Finish the installation of the MongoDB Agent.**

At the Final Steps modal, the legacy Backup and
Monitoring Agents are put into standby mode. Click
Finish.

## Next Steps

After the MongoDB Agent update completes:

- Stop and
  remove the legacy
  Monitoring Agent.

- Stop and
  remove the legacy Backup
  Agent.
