<!-- Converted from reference/faq/faq-mongodb-agent.txt (reStructuredText). Includes are inlined. -->

# FAQ: MongoDB Agent

This addresses common questions about the MongoDB Agent.

## General

### What is the MongoDB Agent?

The MongoDB Agent helps you manage, monitor, and back up your MongoDB 
instances.

### When was the MongoDB Agent in Ops Manager launched?

The MongoDB Agent was released for Ops Manager 4.1 on 29 May 2019. 
MongoDB requires you to update as soon as possible to the MongoDB Agent because the legacy Agents are now EOL. 

### When must I switch to the MongoDB Agent?

Now. Any legacy agent update requires switching to the MongoDB Agent.
You must update all clusters in the project. Once updated, the
Ops Manager console renders the new interface for the MongoDB Agent.

### Can I update per cluster or per node?

No. Updates to MongoDB Agent must be done for all clusters in a project
simultaneously.

### Did the Ops Manager UI change?

Yes. The Agent(s) and Servers tabs were updated to reflect this change.

### Does the Ops Manager API support the MongoDB Agent?

Yes.

### Can I programmatically upgrade to MongoDB Agent via the API?

Yes.

### Does the new installer use a different filename?

No. The name for the installer is `mms-automation` to make the update
easier.

### I have a PEM Key File and Password(s) set for my legacy Automation, Monitoring or Backup Agents? What should I know when I switch to the MongoDB Agent?

When you switch to using the MongoDB Agent, these settings are preserved.
If you previously set a PEM (Privacy-Enhanced Mail) Key File and Password in the Security >
Settings section of Ops Manager, Ops Manager uses the current Automation
Agent's PEM (Privacy-Enhanced Mail) key file and Password as the MongoDB Agent PEM (Privacy-Enhanced Mail) Key File
and Password.

Any existing Monitoring and Backup PEM (Privacy-Enhanced Mail) Key File and password(s) are
exported into the new custom configuration section for Monitoring and
Backup on the MongoDB Agent UI page. A warning displays in the
Configure Cloud Manager Agents section
(Security > Settings)
that the values from the custom configuration section override these values.

## I only use the legacy Monitoring Agent, what does this mean for me?

The MongoDB Agent provides support in this case. The process of switching
to using the MongoDB Agent proceeds as follows:

#. When the MongoDB Agent is available, you see the banner
   notification that your Monitoring Agent is out of date.

#. When you are ready to switch, click Update in the
   banner. A workflow that guides you through the update process
   starts.

   a. Read a MongoDB Agent description with a link to documentation.

   #. Specify custom Monitoring configuration options that you use for
      your Ops Manager project.

   #. Download and install the MongoDB Agent. Ops Manager verifies that the
      MongoDB Agent is installed correctly on the list of specified servers.

      **Note:**

      Previously configured  authentication methods continue to work.
      You provide the MongoDB authentication information in
      Monitoring Settings uder the ellipsis-h menu.

#. Once you install the MongoDB Agent on a server, the MongoDB Agent enables
   the Monitoring for projects where Monitoring  existed as a
   standalone Agent before switching to theMongoDB Agent.

#. The MongoDB Agent puts the previously used  Monitoring Agents into
   standby mode and no longer shows them in the UI.

#. The previously used standalone Monitoring Agents can no longer monitor
   instances. You can stop and remove them when ready.

From this point forward, the MongoDB Agent updates itself after you
choose the Confirm and Deploy option for the new version.
You no longer need to download the MongoDB Agent each time a new version
becomes available!

## I only use the legacy Monitoring and Backup Agents, what does this mean for me?

The MongoDB Agent supports this use case. The flow for switching to the
MongoDB Agent proceeds as follows:

#. When the MongoDB Agent is available, you see the banner
   notification that your Monitoring and Backup Agents are out of date.

#. When you are ready to update, click Update in the
   banner. A workflow that guides you through the update process
   starts.

   a. Read MongoDB Agent description with a link to documentation.

   #. Specify custom Monitoring and Backup configuration options that you
      use for your Ops Manager project.

   #. Download and install the MongoDB Agent. Ops Manager
      verifies that the MongoDB Agent been installed correctly on the
      list of known servers.

      **Note:**

      Previous authentication methods continue to work. You provide
      MongoDB authentication information in Monitoring Settings
      under the ellipsis-h menu. To specify Backup user
      settings, go to Backup under Options >
      ellipsis-h > Edit Credentials.

#. Once the MongoDB Agent is installed on a server, it enables the
   Monitoring and Backup in projects where the Agents were previously
   configured.

#. The MongoDB Agent puts the previously used  Monitoring and Backup Agents
   into standby mode and no longer shows them in the UI. The previously
   used standalone Monitoring Agents can no longer monitor instances.
   You can stop and remove them when ready.

From this point forward, the MongoDB Agent updates itself if you choose
to use the Confirm and Deploy option for a new version. You
no longer need to download the MongoDB Agent each time a new version
becomes available!

## My clusters are already managed using all 3 legacy Agents, what will happen?

The update flow proceeds as follows:

#. When the MongoDB Agent is available, you see the banner
   notification that your legacy Agents are out of date.

#. When you are ready to update, click Update in the
   banner. A workflow that guides you through the update process
   starts.

   #. Read the MongoDB Agent description with link to documentation.

   #. Review  a list of your current servers and update them to the
      MongoDB Agent. As a part of this update process the MongoDB Agent:

      - Stops any legacy Monitoring and Backup Agents.

      - Enables Monitoring and Backup on the servers where Monitoring
        and  Backup were running as Agents.

      - Removes the binaries for the stopped Monitoring and Backup Agents.

      - Unlocks the `mms-monitoring-agent` or `mms-backup-agent`
        users in your MongoDB instances so you can delete them, if
        desired. The MongoDB Agent uses the `mms-automation` user to
        connect to your instances.

From this point forward, the MongoDB Agent works as a single process for
Automation, Monitoring, and Backup.

### What about the three MongoDB Agent Users?

MongoDB consolidated the three MongoDB users that the legacy Automation
Agent used (`mms-automation`, `mms-monitoring-agent`,
`mms-backup-agent`) into one user. This user, `mms-automation`, can 
automate, monitor, and back up instances. MongoDB didn't remove the previous
MongoDB users in case you use those users in other projects. However, 
Ops Manager unlocked these users in its interface as part of the update so that 
you may delete them.

I mostly manage my clusters with the Automation Agent but I have a

## Standalone legacy Backup and Monitoring Agents, what does this mean for me?

You get both update flows: one for any standalone Agent, as described in
the previous sections:

I only use the legacy Monitoring Agent, what does this mean for me? or

I only use the legacy Monitoring and Backup Agents, what does this mean for me?

For those servers where Automation manages legacy Monitoring and Backup Agents,
see 
My clusters are already managed using all 3 Agents, what will happen?.
