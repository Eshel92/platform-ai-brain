<!-- Converted from tutorial/clear-security-settings.txt (reStructuredText). Includes are inlined. -->

# Clear Security Settings

## Overview

Ops Manager enables you to configure the security settings that your deployments
use through the Ops Manager user interface. If you wish to reset the security
settings for your deployment, you may do so using the Clear
Settings button. Clear Settings clears all
authentication-related settings so you can start over from a blank
configuration.

Clear Settings removes all authentication-related settings,
including the authentication mechanisms for the deployment,
automation users and roles, and defined users for the
Monitoring and Backups.
   
You **cannot** reset the security settings for a deployment if your
deployment includes any managed processes.

## Procedure

You may only reset the authentication settings if there are no managed
processes associated with your deployment. As such, if you wish to reset
the security settings, you must unmanage all processes, and then use the
Clear Settings button to reset the security settings.

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: Select Remove from Ops Manager.**

**Step 3: Select whether to also stop monitoring the process.**

Select Unmanage this item but continue to monitor
and click Remove. If prompted for an authentication code,
enter the code.

You do not need to stop monitoring a process in order to reset the
security settings.

**Step 4: Navigate to the Settings tab.**

#. Click the Security tab.

#. Click the Settings tab.

**Step 5: Click Clear Settings.**

The Clear Settings button resets the security settings
for your Ops Manager deployment. 

**Important:**

If you still have managed processes, the Clear Settings
button is grayed out.

**Step 6: To confirm that you wish to clear the security settings, click Clear Settings.**

**Step 7: Click Review & Deploy to review your changes.**

**Step 8: Click Confirm & Deploy to deploy your changes.**

Otherwise, click Cancel and you can make
additional changes.

Ops Manager will reset all security settings. You can now edit the security
settings if you wish to. To resume management of any processes,
see: /tutorial/nav/mongodb-agent.
