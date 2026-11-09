<!-- Converted from admin/backup/jobs-page.txt (reStructuredText). Includes are inlined. -->

# Jobs

This page lets you manage Backup jobs and Backup resources for
each project. The top part of the page displays Active Jobs
and the bottom part displays Stopped Jobs. The following
fields on the page have a yellow background if delayed:

- Last Agent Conf, if older than 1 hour.

- Last Oplog, if older than 1 hour before the
  Last Agent Conf.

- Head Time, if older than 1 hour before
  Last Oplog.

- Last Snapshot, if older than the snapshot interval
  multiplied by 1.5.

## Manage Backup Jobs

From the Jobs page, you can do the following:

| Task | Procedure |
|---|---|
| Assign a project to particular set of `Backup Daemons` or `blockstores`. | Click the project, select the Daemons or blockstores, and select Save Changes. |
| View a job's log. | Click the name of the job and then click the Logs link. Contact MongoDB Support if you need help interpreting the error message. |
| View information about a job. | Click the job. From the job's page you can access logs, conf calls, and other information, and you can download diagnostics. |
| Move a job to a new Backup Daemon. | Click the job. On the job's page, click the Move head link, select the new `head`, and click the Move Head button. FCV `4.2` and later use backup cursors instead of `head databases`. For more information, see backup-daemon. |
| Filter the page to display the jobs assigned to a particular Daemon or blockstore. | Click the name of the Daemon or blockstore. |
| Toggle whether a job journals its `head database`. | Select or clear Journal Head to turn on or off journaling for your head database. Changing this setting at the job level overrides the deployment-wide setting. See `mms.backup.journal.heads` for how to enable or disable journaling for all head databases in your project. |

## Manage Backup Resources

From the Jobs page, you can assign Backup resources to a
particular `project`.

You can make these changes for existing Backups, but only new
backup jobs will follow the new rules. Making
these changes does not affect existing deployments. For additional
procedural information, see
/tutorial/move-jobs-to-new-backup-daemon.

* - Task
  - Procedure

* - Assign a project to particular `Daemons`,
    `blockstores`
    or `oplog stores`.

  - Click the project to open the project's assignment page; make the
    assignments; select Save Changes.

* - Assign a project to a labelled set of resources.

  - Assign the desired label on the Admin page for each resource. For more information, see
    daemons-interface, blockstores,
    and oplog-stores-page.

    Then, on the Jobs page:

    1. Click the project name to open the project's assignment page.

    2. In the Assignment Labels list box, click
       Select Labels.

    3. Select the label. Each selected label must exist on at least
       one Daemon, one blockstore, and one oplog store. If you
       select multiple labels, the resource must meet all selected
       labels.

       Keep in mind that the resource must also meet any other
       selected criteria on this page.

       For example: for a Daemon to match, it must also meet any
       selections you have made in the Backup Daemon
       field.

    4. Click Save Changes.

    Some label changes do not require stopping and restarting backups: 

    - Changes that only affect Oplogs only require stopping and restarting running jobs.
    - Changes that only affect Daemons only need a move head to move the existing data.
    - Changes that only affect blockstores only need an inter groom job.

    WARNING: After you change the labels applied to this backup job,
    stop and then restart backups for this
    deployment. Once Backup restarts, Ops Manager changes the
    `oplog store` assigned to this
    Backup job. The oplog store matches the job's assigned
    labels to an oplog store with the same
    assigned labels. This change halts
    new and removes existing
    `point-in-time restores` until
    Ops Manager takes the next snapshot after reassigning the oplog
    store.

* - Configure a project to use KMIP.
  - Specify the KMIP (Key Management Interoperability) fields and click Save Changes.
