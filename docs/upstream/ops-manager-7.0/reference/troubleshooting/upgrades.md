<!-- Converted from reference/troubleshooting/upgrades.txt (reStructuredText). Includes are inlined. -->

# Upgrade Issues

## Failed Rolling Upgrade

To recover from a failed rolling upgrade follow these steps in the
following order:

1. Restart your Ops Manager instances.

#. Check to see if you have upgraded *all* Ops Manager hosts that support
   your Ops Manager instance.

   If Ops Manager detects two running versions, it remains in **Upgrade
   Mode**. Stop the Ops Manager Application on the host running an earlier
   version, upgrade that host, then restart that host.

#. Restore the Application Database to a previous state after the
   upgrade process had started, but before it has completed.

   a. Copy of all the Ops Manager log files.
   b. Stop all Ops Manager instances including backup daemons.
   c. Restore the Application Database to a backup taken before the
      upgrade was started.
   d. Reinstall the previous version of Ops Manager.
   e. Restart all Ops Manager instances.
   f. Contact MongoDB Support and provide all details.

#. Leave Ops Manager in **Upgrade Mode** and
   contact MongoDB Support.

   - If migrations cannot be applied, Ops Manager remains in Upgrade Mode.
   - If you can accept your Ops Manager instance in this state within the
     bounds of your SLA (Service Level Agreement), contact MongoDB Support and provide details of the problem
