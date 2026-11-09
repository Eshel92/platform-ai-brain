<!-- Converted from tutorial/provision-migration-host.txt (reStructuredText). Includes are inlined. -->

# Provision a Migration Host for MongoDB Agent

**Important:** Live Migration (push) Deprecated or Not Supported for Source Deployments Managed or Monitored by Ops Manager

- For source deployments running any MongoDB 6.0.+ versions, where the
  deployments are managed or monitored by Ops Manager, live migration (push)
  is not supported.
- For source deployments running any MongoDB 5.0 and earlier versions,
  where the deployments are managed or monitored by Ops Manager, live
  migration (push) is deprecated.
- For source deployments running MongoDB 6.0.+, where the deployments
  are monitored by Cloud Manager, live migration (push) is supported.
  To learn more, see Live Migrate Your MongoDB Cluster Monitored by Cloud Manager to Atlas.

   
To live migrate your source MongoDB deployment monitored in Ops Manager to
Atlas, provision a server for the migration host.

## Overview

The migration host is a server on which you install a dedicated MongoDB Agent.
This MongoDB Agent automates live migration operations. It requires that
you set its configuration option `agentFeatureCloudMigrationEnabled` to `true`.

You use the migration host to manage the live migration process of your
deployment from Ops Manager to Atlas. You can't use the migration host
for any other purposes.

After you provision the migration host, its server appears under the
Servers tab. A MongoDB Agent on the migration host runs a
one-time migration of data from Ops Manager to Atlas and reports the
live migration status back to Ops Manager.

To learn about starting a live migration from Ops Manager, see
Migrate a Deployment to Atlas and review the
workflow for live migration to Atlas.

## Considerations

If you plan to migrate more than one deployment at a time, create a
dedicated migration host for each of the deployments that you want
to migrate to Atlas.

**Note:**

Using an HTTP proxy, which intercepts and replaces TLS certificates
for the relayed HTTPS requests is not supported by Ops Manager when you
use it in hybrid mode.

## Prerequisites

The migration host must use a 64-bit CPU architecture and one of the
following supported platforms. The platforms depend on the migration tool
that the migration host will be running to facilitate the migration.

- Migration host for live migrations (push) of source deployments of MongoDB
  earlier than 6.0.17 that you add to monitoring in Cloud Manager,
  where the migration host runs `mongomirror`:

  | Architecture | Distro/OS | 5.0 |
  |---|---|---|
  | x86_64 | RHEL/Centos 7 | check-circle |
  |  | RHEL/Centos 8 | check-circle |
  |  | Amazon Linux 2 | check-circle |
  |  | SUSE12 | check-circle |
  |  | SUSE15 | check-circle |
  |  | Debian 9 | check-circle |
  |  | Debian 10 | check-circle |
  |  | Debian 11 | check-circle |
  |  | Ubuntu 18.x | check-circle |
  |  | Ubuntu 20.x | check-circle |
  | ARM | RHEL/Centos 8 | check-circle |
  |  | Amazon Linux 2 | check-circle |
  | PowerPC/ ppc64le | RHEL/ Centos 7 | check-circle |
  |  | RHEL/ Centos 8 | check-circle |
  | zSeries/ 390x | RHEL 7 | check-circle |
  |  | RHEL 8 | check-circle |
  |  | Windows | check-circle |

  **Note:**

  The configuration of a migration host for live migration is not
  supported on Windows or macOS. You can still live migrate (push) your data
  from a Windows-based deployment to Atlas if you
  provision your migration host on one of the platforms it supports. 
  You can't live migrate your data from a macOS-based deployment to 
  Atlas.

  If Ops Manager is running in local mode, you must have outgoing 
  access to the following server to download mongomirror.

  ```none
  translators-connectors-releases.s3.amazonaws.com
  ```

- Migration host for live migrations (push) of MongoDB 6.0.17+ or
  7.0.13+ source
  deployments monitored in Cloud Manager, where the migration host runs [mongosync](https://www.mongodb.com/docs/cluster-to-cluster-sync/current/reference/mongosync/):
  
  The migration host must use a 64-bit CPU architecture and one of the
  [mongosync platforms](https://www.mongodb.com/docs/cluster-to-cluster-sync/current/installation).

## Migration Host Resource Requirements

The live migration process is CPU-intensive and requires sufficient
network bandwidth. Use a cloud instance with enough resources to help
ensure a successful migration.

Avoid host environments that have been characterized as having
low network bandwidth.

You may also need to provision additional storage for the
`cloudMigrationOplogPath` option described in the following
procedure.

- MongoDB 6.0.17+ or 7.0.13+. For the migration host that runs `mongosync` to
  facilitate push live migrations, use an instance
  with a minimum of 8 CPUs and 24 GB of RAM.

- MongoDB versions earlier than 6.0.17. For the migration host that runs
  `mongomirror` to facilitate push live migrations, use a host
  with 2-4 CPU cores and 4-8 GB of RAM to migrate a replica set.
  Use an instance with 2-4 CPU cores per shard to migrate a sharded cluster.

## Procedure

**Step 1: Click Deployment, select the Agents tab, and then select Downloads & Settings.**

**Step 2: Under Automation, select your operating system and follow the instructions to install and run the agent on the migration host.**

To learn more, see /tutorial/install-mongodb-agent-to-monitor.

**Step 3: Edit the MongoDB Agent configuration file to enable Live Migration.**

a. If you don't already have the  automation-agent.config file open from the
   previous step, open it in your preferred text editor:

   ```sh
   sudo vi /etc/mongodb-mms/automation-agent.config
   ```

#. Add or update the following live migration configuration options:

   | Key | Value |
   |---|---|
   | `agentFeatureCloudMigrationEnabled` | `true` |
   | `cloudMigrationOplogPath` | Path to the oplog files for the live migration process. This key is optional and if set, requires provisioning enough storage in the specified directory for the oplog buffering. Contact MongoDB Support if you need assistance determining whether you need to set this key for your deployment. |

#. Ensure that the resulting changes to the  automation-agent.config file
   contain the following necessary configuration options for live
   migration:

   ```ini
   mmsGroupId=<The ID of your project>
   mmsApiKey=<The Agent API key of your project>
   mmsBaseUrl=<The URL of your Ops Manager application>
   agentFeatureCloudMigrationEnabled=true
   cloudMigrationOplogPath=<The path to the oplog files>
   ```

   To learn more, see mongodb-agent-settings.

**Step 4: Restart the MongoDB Agent to incorporate the updated settings.**

An additional server appears under the Servers tab, and
an additional MongoDB Agent appears under the Agents tab.

## Next Steps

Once you have provisioned the migration host, you can switch to
Atlas and follow the steps in the wizard to
start the live migration process.
