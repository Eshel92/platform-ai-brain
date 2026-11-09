<!-- Converted from reference/troubleshooting/getting-started.txt (reStructuredText). Includes are inlined. -->

# Getting Started

To begin troubleshooting, complete these tasks to check for common, 
easily fixed problems:

## Authentication Errors

If your MongoDB instances run with authentication enabled, ensure Ops Manager
has the MongoDB credentials. To learn more, see
/tutorial/edit-host-authentication-credentials.

## Check Agent Output or Log

If you continue to encounter problems, check the agent's output for 
errors. To learn more, see
Agent Logs for more information.

## Ensure Connectivity Between Agent and Monitored Hosts

Ensure the system running the agent can resolve and connect to the
`mongod` processes. If you install multiple Monitorings, ensure that **each** Monitoring can reach every
`mongod` process in the deployment.

To confirm, log into the system where the agent is running and issue a
command in the following form:

```sh
mongosh <hostname>:<port>
```

Replace `<hostname>` with the hostname and `<port>` with the
port that the database is listening on.

Ops Manager does not support port forwarding.

## Ensure Connectivity Between Agent and Ops Manager Server

Verify that the Monitoring can connect on TCP port 8443
(outbound) to the Ops Manager server (i.e. `api-agents.mongodb.com`.)

## Allow Agent to Discover Hosts and Collect Initial Data

Allow the agent to run for 5 to 10 minutes to allow host discovery and
initial data collection.
