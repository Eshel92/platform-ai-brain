<!-- Converted from reference/troubleshooting/automation.txt (reStructuredText). Includes are inlined. -->

# Automation

Ops Manager Automation allows you to deploy, configure, and manage MongoDB
deployments with the Ops Manager UI. Ops Manager Automation relies on an
MongoDB Agent, which must be installed on every server in the
deployment. The MongoDB Agents periodically poll the Ops Manager service
to determine the current goal, and continually report their status to
Ops Manager.

## Automation Runs Only on 64-bit Architectures

Ops Manager provides only 64-bit downloads of the MongoDB Agent.

## Using Own Hardware

- If you deploy Automation manually, ensure that you have one
  MongoDB Agent on every server.

- If you deploy the agent manually, you must create MongoDB's
  `dbPath` and the directory for the MongoDB binaries and
  ensure that the user running the agent owns these
  directories.

  If you install using the `rpm` package, the agent runs as the
  `mongod` user; if using the `deb` package, the agent runs as the
  `mongodb` user. If you install using the `tar.gz` archive file,
  you can run the agent as any user.

## Networking

### Connectivity to MongoDB Ports

All hosts must be able to allow communication between MongoDB
ports. The default is `27017`, but you can configure alternate port
ranges in the Ops Manager interface.

The MongoDB Agent *must* be able to connect to
Ops Manager on port `8080` (HTTP (Hypertext Transfer Protocol)) or port `8443` (HTTPS (Hypertext Transfer Protocol Secure)).
For more information on access to ports and IP addresses, see
/core/security.

### Intra-cluster Connectivity Issue

When performing a rolling update, the MongoDB Agent tries to avoid
downtime. It needs to collect state from other members of the cluster.
A connectivity issue (between `mongod`\s and `mongos`\es), such as
hostname resolution or misconfigured firewall, may prevent the
MongoDB Agent from determining the remote processes state and
completing the change. 

To ensure all members of the cluster can communicate with each other:

1. For a non-sharded cluster:

   a. Log into each `mongod`.
   b. From that `mongod` host, log into all the other members of the
      replica set.

2. For a sharded cluster:

   a. Log into each `mongod`.
   b. From that `mongod` host, log into all the other members of the
      shard.
   c. Log into each `mongos`. 
   d. From that the `mongos` host:

      i.  Log into the other `mongos` hosts.
      ii. Log into all the other members of each shard.

### Frequent Automation Connections

MongoDB Agent gathers the state from each member of the cluster every 10
seconds to ensure that the environment is in the expected state. As
part of this assessment, MongoDB Agent creates a connection, checks
certain files to determine state, and then closes the connection. These
frequent, short-lived connections are part of MongoDB Agent's routine
activity and should not impact performance.

## Automation Configuration

After completing the automation configuration, ensure that the
deployment plan satisfies the needs of your deployment. Check
hostnames and ports before confirming the deployment.

## Sizing

- Ensure that you provision hosts with enough space to run MongoDB
  and support the requirements of your data set.

- Ensure that you provision a sufficient number of hosts to run your
  deployment. Each `mongod` should run on its own host.

## Frequent Connection Timeouts

The MongoDB Agent may frequently time out of connections for one or
more of the following reasons:

- Connection timeouts

- High network latency

- High server load

- Large SSL keys

- Insufficient CPU speed

By default, connections time out after 40 seconds. MongoDB recommends
gradually increasing the value of the `dialTimeoutSeconds`
MongoDB Agent configuration setting to prevent frequent premature
connection timeouts. However, increasing this value also increases the
time required to deploy future configuration changes. Experiment with
small, incremental increases until you determine the optimum value for
your deployment.

To learn more, see `dialTimeoutSeconds` in MongoDB Agent
Connection Settings.

## Deployments

A banner that displays
We have detected a potential problem while deploying...
appears when certain conditions apply. These are some examples.

### Deployment Change Unable to Complete / Not Proceeding

If you have added or restarted a deployment and the deployment remains
in the `In Progress` state for several minutes, the banner displays.

At this point, you have four options:

1. Click View Diagnostics.

   The View Diagnostics modal displays any errors that may
   have happened during deployment.

2. Click View Status.

   The Automation Status modal displays the deployment
   processes, when they last reported their deployment status, what
   task they are trying to complete, and the deployment status. You can
   filter the results in the following ways:
   
   - Type a hostname in the Filter processes search bar.
   - Select one or more process types from the Process Type
     dropdown.
   - Select one or more automation states from the
     Automation State dropdown.

   To learn more about the status of any of the individual processes,
   you can click the ellipsis icon and select either
   View Details or View Agent Logs.

   - View Details shows what the deployment plan for the
     process is and which stage of that plan the MongoDB Agent
     currently is.

   - View Agent Logs opens a new browser window with the
     Deployment > Agents >
     Agent Logs screen shown and the contents of the
     MongoDB Agent log displayed by default. Click the
     View menu to select a different agent log.

3. Click View Agent Logs.

   A new browser window opens with the Deployment >
   Agents > Agent Logs screen shown and the
   contents of the MongoDB Agent log displayed by default. Click
   the View menu to select a different agent log.

4. Click Allow Override & Edit Configuration.

   If you diagnose an error and need to correct the deployment
   configuration, follow the procedure to
   edit the deployment.

If you shut down the deployment and still cannot find a solution,
remove the deployment from 
Ops Manager.

### MongoDB Agents Are Down or Not Communicating

If Automation Module of MongoDB Agent can't communicate with the
Ops Manager Application `API endpoint` or the MongoDB
Server processes, Ops Manager displays a warning banner in the Project. You
can resolve this in one of two ways depending upon whether or not you
expect the MongoDB Agents to be communicating:

#### MongoDB Agents need to communicate

If the MongoDB Agent(s) should be communicating with the Ops Manager
host or MongoDB instances, confirm the following for each MongoDB Agent:

a. The Agent is up and running on each host.

#. The Agent and the Ops Manager Application API endpoint
   can communicate.

#### MongoDB Agents Do Not Need to Communicate

If Automation Module of MongoDB Agent(s) should be communicating with
the Ops Manager Application `API endpoint` or MongoDB
Server processes, confirm the following for each automated MongoDB
Server deployment:

a. Click the Allow Editing & Override Current Configuration
   link in the warning banner.

#. Remove all processes
   (`mongod` *and* `mongos`) running on the hosts that serve the
   unneeded MongoDB Agents.

## MongoDB Agent Permissions

A permissions issue may prevent automation from completing a change. If
View Status or View Diagnostics report an
permissions-related error (such as ``open /data/db/mongod.lock:
permission denied``), ensure that the MongoDB Agent user owns and has
read and write permissions to the `dbpath` and `logpath` files.

## Remove Problematic MongoDB Hosts

You can use the console or the API (Application Programming Interface) to remove stale, broken, or
problematic hosts from automation. This may include the circumstance
when the MongoDB Agent can't be reached.

To remove a problematic host using the console:

1. Navigate to your project.

2. Click Servers.

3. Find your problematic host.

4. Click `ellipsis`, then Remove Server.

   Ops Manager displays the
   Are you sure you want to remove this server> modal.

5. Enter the provided hostname into the
   Enter the host name field an click Remove
   if you want to remove this server.

   **Warning:**

   Ops Manager removes all monitoring data for this host when you click
   Remove. Ops Manager provides no confirmation or
   cancellation for this action.

   If you don't want to remove the server, click Cancel.

6. Click Review & Deploy to review your changes.

   Ops Manager displays your proposed changes.

   - If you are satisfied, click Confirm & Deploy.

     Ops Manager removes all processes and agents at this time.

   - If you want to make further configuration changes,
     click Cancel.

To remove a problematic host using the API (Application Programming Interface):

1. Get the current automation config.

2. Edit the automation configuration JSON (Javascript Object Notation) file.

3. Remove the stale node from
   processes and
   replica sets.

4. Update the automation config file.

5. Wait for a few minutes.

6. Check the Agents view.

7. Confirm the host no longer appears on the list of Agents.

## Ensure TLS Certificates Contain a Subject Alternative Name

 

**Warning:**

The MongoDB Agent from version 11.12.0.7384 requires TLS (Transport Layer Security)
certificates include a value in the Subject Alternative Name
field. Before upgrading to 11.12.0.7384, ensure that all TLS (Transport Layer Security)
certificates used in your MongoDB deployment contain a SAN (Subject Alternative Name).
[#cnchange]_

## Store Configuration Files in Memory for Existing Clusters

If you use Ops Manager version 4.2 or versions 4.4.0 - 4.4.6, you may encounter
errors when setting `enableLocalConfigurationServer` to `true`
and restarting your MongoDB Agent. 

This issue only affects existing clusters where 
`enableLocalConfigurationServer` is set to `true` after the cluster 
is created. Setting this value before creating the cluster does not trigger 
this issue.

To safely change this setting for existing clusters:

#. At the end of your MongoDB Agent 
   configuration file, add:

   ```ini
   enableLocalConfigurationServer=true
   ```

#. Shut down each process managed 
   by the MongoDB Agent.

#. Restart the MongoDB Agent by running the following command:

   ```ini
   service mongodb-mms-automation-agent restart
   ```

#. Restart the MongoDB processes that you 
   shut down.

#. Verify that the `automation-mongod.conf` file has the
   `__rest` expansion directive.

For more information on storing configuration files in memory, 
see /reference/mongodb-agent-external-configuration.
