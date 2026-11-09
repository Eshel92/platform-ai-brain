<!-- Converted from admin/backup/restores-page.txt (reStructuredText). Includes are inlined. -->

# Restores

This page displays a table of the last 300 requested restores and their
progress. This table includes:

* - Column
  - Purpose

* - Project
  - Project from which this snapshot was restored.

* - Replica Set
  - Cluster of which this snapshot was restored.

* - App User
  - Ops Manager user account that requested the restore.

* - Cancelled / Broken
  - Indicator that the restore was interrupted.

* - Point in Time
  - Date and time to which the data should be restored and the
    method used to determine that timestamp. Ops Manager expresses this
    timestamp as `mm/dd/yyyy - hh:mm:ss AM|PM`.

* - Uncompressed Size
  - Total file size of your snapshot.

* - Estimated Transfer Size
  - Estimated file size for the compressed file (`*.tar.gz`) to be
    transferred via HTTP (Hypertext Transfer Protocol).

* - Machine (tries)
  - List of Backup Daemons used for the restore as well as

    - their head DB paths
    - the number of times a Backup Daemon tried if the restore
      requires a Backup Daemon

    **Important:** Legacy Value

    No current restore delivery method retries a restore if it
    fails. This column applies to obsolete restore methods.

* - Bytes Transferred
  - Total number of bytes that transferred while the restore job was
    valid.

* - Last Heartbeat
  - Last date and time activity was detected on the transfer.
    Ops Manager expresses this timestamp as ``mm/dd/yyyy - hh:mm:ss
    AM|PM``.

* - Transfer Started
  - Date and time when the HTTP (Hypertext Transfer Protocol) transfer was started. Ops Manager
    expresses this timestamp as `mm/dd/yyyy - hh:mm:ss AM|PM`.

* - Transfer Finished
  - Date and time when the HTTP (Hypertext Transfer Protocol) transfer was finished. Ops Manager
    expresses this timestamp as `mm/dd/yyyy - hh:mm:ss AM|PM`.

* - Transfer Status
  - Status of the download when the Admin page loads.

* - Transfer Rate
  - Speed of the HTTP (Hypertext Transfer Protocol) download in MBps.

* - Delivery
  - Information regarding type of delivery. Types include:

    | Delivery Type | Restore Type |
    |---|---|
    | `pull` | Typical snapshot download |
    | `query` | Queryable snapshot download |
    | `client_pit_pull` | Point-in-time snapshot download |

* - Request Origin
  - Unique identifier of the project that requested the restore and
    which method was used to make the request. The method is either
    API (`automationApi`) or the Console (`automationUi`).

* - Submitted
  - Date and time when the restore was requested. Ops Manager
    expresses this timestamp as `mm/dd/yyyy - hh:mm:ss AM|PM`.

* - Current Phase
  - Indicator of the progress of the restore. Phases include:

    - `transfer`
    - `inProgress`
    - `done`
    - `completed`

To show all restores ever requested, click Show All.
