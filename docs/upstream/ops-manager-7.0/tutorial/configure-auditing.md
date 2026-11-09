<!-- Converted from tutorial/configure-auditing.txt (reStructuredText). Includes are inlined. -->

# Configure and Deploy Auditing

MongoDB Enterprise provides the capability to audit mongod
and mongos instances. The auditing facility allows
administrators and users to track system activity for deployments
with multiple users and applications. Administrators can configure
auditing to write to the console, syslog, a JSON
file or a BSON file. You can also use filters to restrict which events
are logged.

**Important:**

If you're running MongoDB Enterprise version 5.0 or later and 
MongoDB Agent 11.0.13.7055 or later, you can:

- Set separate rules for rotating server logs and audit logs.
- Compress and delete audit logs using Ops Manager. For security reasons, we recommend managing
  your audit log compression and deletion outside of Ops Manager.

If you're running earlier versions of MongoDB Enterprise or the
MongoDB Agent, Ops Manager: 

- Uses your System Log Rotation settings to rotate both the
  server logs and the audit logs. 
- Doesn't compress or delete audit logs. If you configure compression and
  deletion, Ops Manager applies these settings to the server logs only.

MongoDB Community users can rotate, compress, and delete the server logs
only.

**Note:**

For more general information about auditing, including the audit
guarantee, see Auditing. For details about
audited events, see audit-action-details-results. For
information about setting up filters, see Configure Audit
Filters.

## Prerequisites

Your Ops Manager cluster must run MongoDB Enterprise, version 2.6 or later,
to configure and deploy auditing.

## Procedure

**Step 1: Click Deployment, then Processes.**

**Step 2: Click Modify next to the MongoDB process for which you want to configure auditing.**

**Step 3: Click Advanced Configuration Options.**

**Step 4: Click + Add Option.**

**Step 5: Select auditLogDestination from the Startup Option menu.**

**Step 6: Select the desired destination for audit events from the Value menu.**

**Step 7: (Optional) If you selected `file` as the audit log destination, repeat step 4 and specify the following additional properties:**

- `auditLogFormat`: `JSON` or `BSON`

- `auditLogPath`: the desired location of the audit log file

**Step 8: (Optional) To filter which events are audited, repeat steps 1-4 and add the `auditLogFilter` property.**

For information about how to create filters, see 
Configure Audit Filters.

**Step 9: Click Apply to deploy your auditing configuration.**
