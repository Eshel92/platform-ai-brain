<!-- Converted from core/auditing.txt (reStructuredText). Includes are inlined. -->

# Auditing

**Note:** Auditing in MongoDB Atlas

MongoDB Atlas supports auditing for `M10` and larger clusters.
To learn more, see set-up-database-auditing in the MongoDB Atlas 
documentation.

MongoDB Enterprise includes an auditing capability for
`mongod` and `mongos` instances. The auditing
facility allows administrators and users to track system activity for
deployments with multiple users and applications.

## Enable and Configure Audit Output

The auditing facility can write audit events to the console, the
syslog, a JSON file, or a BSON file. To enable auditing in
MongoDB Enterprise, set an audit output destination with
`--auditDestination`. For details,
see /tutorial/configure-auditing.

For information on the audit log messages, see /reference/audit-message.

## Audit Events and Filter

Once enabled, the auditing system can record the following operations
[#transactions]_:

- schema (DDL),
- replica set and sharded cluster,
- authentication and authorization, and
- CRUD operations (requires `auditAuthorizationSuccess` set to `true`).

**Note:**

Starting in MongoDB 5.0, secondaries do not log
DDL audit events for replicated changes. DDL audit events are still
logged for DDL operations that modify the local database and the `system.profile
<` collection.

For details on audited actions, see audit-action-details-results.

With the auditing system, you can set up filters to restrict the
events captured. To set up filters, see /tutorial/configure-audit-filters.

## Audit Guarantee

The auditing system writes every audit event [#filter]_ to an
in-memory buffer of audit events. MongoDB writes this buffer to disk
periodically. For events collected from any single connection, the
events have a total order: if MongoDB writes one event to disk, the
system guarantees that it has written all prior events for that
connection to disk.

If an audit event entry corresponds to an operation that affects the
durable state of the database, such as a modification to data, MongoDB
will always write the audit event to disk *before* writing to the
journal for that entry.

That is, before adding an operation to the journal, MongoDB writes all
audit events on the connection that triggered the operation, up to and
including the entry for the operation.

These auditing guarantees require that MongoDB run with
`journaling` enabled.

**Warning:**

MongoDB may lose events **if** the server terminates before it
commits the events to the audit log. The client may receive
confirmation of the event before MongoDB commits to the audit log.
For example, while auditing an aggregation operation, the server
might terminate after returning the result but before the audit log
flushes.

In addition, if the server cannot write to the audit log at the
`audit destination`, the server
will terminate.
