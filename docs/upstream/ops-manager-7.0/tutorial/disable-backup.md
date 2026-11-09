<!-- Converted from tutorial/disable-backup.txt (reStructuredText). Includes are inlined. -->

# Disable the Backup Service

## Overview

Disabling Ops Manager Backup immediately deletes all snapshots. Later, if you
want re-enable Backup, Ops Manager behaves as if your deployments had never been
backed up and requires an `initial sync`.

## Procedure

**Step 1: Stop and then terminate each deployment enrolled in Backup.**

In Ops Manager, click Continuous Backup. For each deployment enrolled in Backup:

a. Click the backup's ellipsis icon and click Stop.

b. Click the Stop button. If prompted for an authentication code, enter the code.

a. Once the backup has stopped, click the backup's ellipsis icon and click Terminate.

b. Click the Terminate button.

**Step 2: Stop all Backups.**

See /tutorial/start-or-stop-backup-agent.
