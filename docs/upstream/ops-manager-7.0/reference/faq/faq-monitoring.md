<!-- Converted from reference/faq/faq-monitoring.txt (reStructuredText). Includes are inlined. -->

# FAQ: Monitoring and Alerts

This addresses common questions about Ops Manager and how it monitors
MongoDB instances and alerts you of issues with those deployments.

## Host Configuration

### How do I add a new host or server?

See /tutorial/add-existing-mongodb-processes.

#### Can Ops Manager monitor itself?

Yes. You can use Ops Manager to monitor the backing MongoDB
instances
that hold data for Ops Manager and the Backup Daemon. Create a
separate project for the backing
instances.

You **cannot**, however, use Ops Manager to backup or automate the backing
instances.

Ops Manager also provides built-in basic monitoring of all backing
databases through system alerts.

### Can I monitor Kerberos-enabled instances?

Yes. Ops Manager does support monitoring for Kerberos-enabled MongoDB
instances. To learn how this works, see
/tutorial/configure-mongodb-agent-for-kerberos.

### Monitoring

#### Do I need an agent for every MongoDB instance?

No. In your Ops Manager project, a single agent connects to all
MongoDB databases. Configure firewalls to allow the
agent to connect across data centers and servers.

Beginning with agent version 5.0.0, you can activate Monitoring with multiple agents
to distribute monitoring assignments and provide failover.
Ops Manager distributes monitoring assignments among up to 100 running
agents. If you run more than 100 agents, the
additional agents behave as "standby" agents.
For details, see Manage Monitoring Function.

#### Where should I run the agent?

The amount of resources the agent requires varies depending
on infrastructure size, the number of servers and the databases it is
monitoring. Run the agent on an existing machine with additional
capacity that *does not* run a `mongod` instance. You may
also run the agent on a smaller dedicated instance.

The agent load scales with the number of monitored `mongod`
plus `mongos` processes and the number of databases in your MongoDB
environment.

For production environments, it is recommended to install the
agent on a dedicated server, and not on the
the same host as a data bearing `mongod` instance. This
allows you to perform maintenance on the `mongod` and its
host without affecting the monitoring for your deployment.
Additionally, an agent may contend for resources with the
`mongod`.

You can install the agent on the same system as an
arbiter, a `mongos`, or an application server depending on the
requirements of these services and available resources.

#### Can I run the agent on an AWS micro server?

If you monitor five or fewer `mongod` instances, you can use an AWS (Amazon Web Services)
micro server.

#### Why can't the agent connect to my host?

The most common problem is that the agent is unable to resolve the
hostname of the host. Check DNS and the `/etc/hosts` file.

The second most common problem is that there are firewall rules in
place that prohibit access to the host from the agent.

To test the connection, login to the host running the agent and try
to connect using `mongosh`:

```sh
mongosh <hostname>:<port>/test
```

**Note:**

Ops Manager does not support port forwarding.

#### Why does the agent connect with hostnames instead of IP addresses?

By default, the agent resolves hostnames to connect. If
the agent cannot connect by resolving a hostname, you can force the
agent to prefer an IP address over its corresponding
hostname for a specific IP address. Preferred hostnames also allow you
to specify the hostname to use for servers with multiple aliases. This
prevents servers from appearing multiple times under different names
in the Ops Manager interface.

To create a preferred hostname, go to
Project Settings and add a
Preferred Hostnames entry. For details, see
/tutorial/manage-project-settings

#### How do I setup and configure the agent?

See the `README` file included in the agent download.

#### How do I disable Monitoring in Ops Manager?

See Deactivate Monitoring.

## Data Presentation

### What are all those vertical bars in my charts?

A *red bar* indicates a server restart.

A *orange bar* indicates the server is now a primary.

A *brown bar* indicates the server is now a secondary.

## Data Retention

### What is the data retention policy for Ops Manager?

Ops Manager retains two distinct types of data: metrics, which describe 
usage; and snapshots, which back up your data.

Ops Manager preserves:

- .. include:: /includes/extracts/metric-data-retention-retention.rst

- Snapshots according to their retention policy.

## Alerts

### What do the alert conditions mean?

For a reference on the alert conditions, see /reference/alerts/.

### What alerts are configured by default?

See /tutorial/manage-alert-configurations for the default alert
configurations as well as steps to add new alerts or modify existing
alerts, including modifying the alert frequency.
