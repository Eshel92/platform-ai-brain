<!-- Converted from reference/telemetry-overview.txt (reStructuredText). Includes are inlined. -->

# Telemetry

Telemetry collection gathers usage information about your Ops Manager
installation and sends it to MongoDB. Ops Manager enables collecting and
sending telemetry data by default.

**Important:**

This feature is available starting in Ops Manager 8.0.17 and 7.0.20.

Ops Manager performs the initial telemetry data collection seven days 
after you install or upgrade to Ops Manager 8.0.17 or later in the 8.0 
series, or 7.0.20 or later in the 7.0 series. You can 
disable telemetry from the Ops Manager UI or by using the telemetry API.

## About Telemetry

Telemetry is an automated, anonymous usage report that Ops Manager
generates and sends to MongoDB once a week.

Telemetry describes:

- How you configure and run your Ops Manager installation.
- The MongoDB deployments that Ops Manager manages.

Telemetry does not include data that Ops Manager can use to uniquely
identify you or your organization.

## Telemetry Purpose and Usage

MongoDB uses telemetry data to understand how customers configure and
use Ops Manager and the MongoDB deployments that it manages. This
information helps MongoDB:

- Identify the most common deployment patterns.
- Understand the size and topology of managed deployments.
- See which backup mechanisms and infrastructures are most common.

MongoDB uses these insights to prioritize product improvements that
benefit the most customers.

## Telemetry Data Collected

Telemetry data describes your Ops Manager installation and each MongoDB
deployment that Ops Manager manages.

### Installation-Level Data

Telemetry includes information about your Ops Manager installation, such
as:

- A static, unique identifier for the Ops Manager installation.
- The Ops Manager version.
- The operating systems that run on the Ops Manager hosts.
- The number of Ops Manager instances in this installation.
- The number of AppDB nodes.
- The number of backup daemons running.
- The authentication method that Ops Manager uses.
- The infrastructure type that hosts Ops Manager.
- CPU cores and memory provisioned for each Ops Manager host.
- The number of projects and organizations that exist in this installation.

### Deployment-Level Data

Telemetry also includes information about each MongoDB deployment that
Ops Manager manages, such as:

- A static, unique identifier for the deployment.
- The MongoDB version or versions that the deployment uses.
- The deployment type.
- The number of nodes and, for sharded clusters, the number of shards.
- The total data size for the deployment, not including local metadata.
- The MongoDB edition used by the deployment.
- Whether TLS (Transport Layer Security) is enabled.
- The authentication method that the deployment uses.

For the complete field list and types, see the telemetry response
schema in Retrieve Telemetry Data.

## When Telemetry Runs

If telemetry is enabled, Ops Manager schedules a recurring job that
collects and sends telemetry data once every seven days.

When you install or upgrade to Ops Manager 8.0.17 or later in the 8.0 
series, or 7.0.20 or later in the 7.0 series, Ops Manager enables 
telemetry by default and waits seven days before it sends the first telemetry 
snapshot. This grace period gives you time to review and, if needed, disable
telemetry before any data is sent.

Ops Manager uses persisting identifiers for telemetry across
restarts and upgrades. If you reinstall Ops Manager, it generates new
identifiers.

## View Telemetry Data

You can view the telemetry data that Ops Manager plans to send before it is sent.

### Use the Diagnostics Output

Ops Manager includes telemetry data in its diagnostics output. The
diagnostics output contains internal diagnostic information about
your Ops Manager installation, including the telemetry payload.

To review telemetry data:

**Step 1: Open the Ops Manager Config page**

From the Ops Manager UI, go to Admin > 
General > Ops Manager Config.

**Step 2: Download the diagnostics output**

On the Permissions tab, in the Details section, 
click Download next to Current Collected Data. 

**Step 3: Review the telemetry data**

Extract the diagnostics output and locate the telemetry data in 
the archive.

Only a subset of the diagnostics data is sent as telemetry. Review the
telemetry subset in the archive to see the data values that Ops Manager
plans to send in the next telemetry snapshot.

### Use the Telemetry API

You can also use the telemetry API to view the telemetry status and
payload that Ops Manager plans to send.

The Retrieve Telemetry Data 
endpoint returns:

- A flag that indicates if telemetry is enabled.
- The date and time when Ops Manager last sent telemetry successfully.
- The date and time when Ops Manager schedules the next telemetry job.
- The telemetry data object for the next snapshot.

## Control Telemetry Collection

You can enable or disable telemetry collection for your Ops Manager
installation at any time. 

**Important:**

Telemetry is either fully enabled or fully disabled. You cannot enable 
or disable individual telemetry fields.

### Use the UI

Administrators can configure telemetry from the Ops Manager UI. 

**Step 1: Open the Ops Manager Config page**

From the Ops Manager UI, go to Admin > 
General > Ops Manager Config.

**Step 2: Open the Permissions tab**

Click the Permissions tab to view the 
Usage Information Collection setting.

**Step 3: Enable or disable telemetry**

Use the Usage Information Collection control to enable or  
disable telemetry.

If you disable telemetry, Ops Manager stops sending telemetry snapshots
starting with the next scheduled run.

### Use the API

You can also control telemetry collection by using the telemetry API.

The Toggle Telemetry Status
endpoint lets you:

- Enable telemetry by setting the `enabled` field to `true`.
- Disable telemetry by setting the `enabled` field to `false`.

## Network and Connectivity

Telemetry requires that your Ops Manager hosts can reach the MongoDB
telemetry ingestion endpoint.

**Note:**

Ops Manager installations that run in air-gapped environments or
behind restrictive firewalls might be unable to send telemetry
data, even if telemetry is enabled.

MongoDB stores ingested telemetry in an internal system and uses it in
aggregate form to improve Ops Manager and related products.
