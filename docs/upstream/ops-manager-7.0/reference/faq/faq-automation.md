<!-- Converted from reference/faq/faq-automation.txt (reStructuredText). Includes are inlined. -->

# FAQ: Automation

This addresses common questions about Ops Manager and its Automation
features.

Ops Manager can automate management operations for your monitored MongoDB
processes, allowing you to reconfigure, stop, and restart MongoDB
through the Ops Manager interface.

Ops Manager Automation can run only on 64-bit architectures.

## What versions of MongoDB does Ops Manager manage?

For specific Ops Manager functions and supported MongoDB versions, see
/reference/mongodb-compatibility.

## What are the upgrade paths for Ops Manager versions 1.8.x and 2.0.x?

For upgrade paths, see Upgrade Ops Manager.

## How does Ops Manager manage MongoDB deployments?

After you deploy the agent in the environment of the
MongoDB deployment, each agent periodically communicates with Ops Manager
and performs any required work.

Agents constantly reassess their environment to adapt their work as
necessary. As part of this routine activity, the agent establishes
frequent short-lived connections to the cluster members. If an agent
encounters an issue, such as network connectivity problems or Ops Manager
failure, the agents adjust their work to compensate and safely arrive at
their goal state.

Agents create plans to move from their current state to a goal state.
Plans execute in steps, where each step is autonomous and independent
of other steps.

**Example:**

For an installation, the plan involves downloading MongoDB, starting
the process with the appropriate command line options, initializing
the replica set, waiting for a healthy majority. The configuration
reaches goal state when the replica set is active and has a healthy
majority.

## How does Ops Manager perform maintenance on cluster nodes?

Ops Manager performs a `rolling restart` when you perform maintenance
on nodes in a cluster. The agent updates nodes in a cluster one-by-one,
always maintaining a primary node, until all nodes are updated to 
maintain cluster availability during a maintenance period.

For each secondary node in the cluster, the agent:

1. Restarts the `mongod` process running on the node in `standalone` 
   mode.
#. Performs the maintenance task.
#. Restarts the `mongod` process running on the node in `replSet` 
   mode.

After the secondary nodes are updated, the agent:

1. Steps the primary down using the rs.stepDown() command.
#. Triggers an election for a new primary node.
#. Performs the maintenance task on the former primary node.
#. Restarts the `mongod` process running on the former primary node in   
   `replSet` mode to join the cluster as a secondary node.

In Ops Manager, the agent performs rolling restarts on cluster nodes for 
maintenance tasks, including the following:

- Rotating KMIP (Key Management Interoperability) keys.
- Rotating keyfiles.
- Changing `mongod` configuration arguments.
- Upgrading or downgrading TLS (Transport Layer Security), `auth`, or `clusterAuth` mode.
- Changing the MongoDB version.
- Changing the oplog size.
- Removing a process from a replica set.
- Cancelling a restore from backup.
- Enabling the Profiler

**See also:**

/tutorial/prepare-for-maintenance/

   

## How many Automations do I need?

To use Automation, you must have an agent running on every host where
a managed MongoDB instance runs.

## Is any MongoDB data transferred by the agent?

Agents do *not* transmit any data records from a MongoDB deployment.
The agents only communicate deployment configuration information and
MongoDB logs.

## Will Ops Manager handle failures during an upgrade?

Generally speaking, yes. The design of the management and automation
components of Ops Manager do not account for *all* possible failures; however
the architecture of the system can work around many types of failures.

## What types of deployment can I create in Ops Manager?

Using Ops Manager, you can configure all MongoDB deployment types: sharded
clusters, replica sets, and standalones.

The shards in a sharded cluster **must** be replica sets. That is, a
shard cannot be a standalone mongod. If you must run a shard
as a single mongod (which provides **no** redundancy or
failover), run the shard as a single-member replica set.

**Note:**

You may not upgrade a sharded MongoDB deployment to version 3.4 if 
the deployment uses mirrored mongod instances as config 
servers. To allow the sharded deployment to be upgraded, see 
/tutorial/convert-config-servers-to-replica-set. The 
conversion requires that the sharded deployment run MongoDB version
3.2.4 or later. Deployments running previous versions must upgrade
to version 3.2.4 before an upgrade to version 3.4.
