<!-- Converted from admin/backup/job-timeline-page.txt (reStructuredText). Includes are inlined. -->

# Job Timeline

This page displays a graphical representation of information found on
other Admin pages, in particular the Jobs
page. The Job Timeline page displays critical timestamps
(`head`, last snapshot, next snapshot) and
offers a way to assign a `daemon` to a given job.

**Note:**

FCV `4.2` and later use 
backup cursors instead of
`head databases`. For
more information, see backup-daemon.

Click the Auto refresh checkbox to update the list
automatically every 10 seconds. Click the Refresh button
to refresh data manually.

To view the backup job JSON (Javascript Object Notation), click the Show JSON link
under the Project heading for any backup job. When the
JSON (Javascript Object Notation) displays, click the View raw runtime data link
under the code to view the raw data. To hide the daemon JSON (Javascript Object Notation), click
the Hide JSON link.

For detailed information about snapshot metadata fields available in the
JSON data, see om-snapshots.

To move the job to a new Backup Daemon, click the Move head
link under the Machine heading for a backup job. Select the
location and click the Move head button to move the job to
a new Backup Daemon. Ops Manager does not automatically move jobs between
daemons.
