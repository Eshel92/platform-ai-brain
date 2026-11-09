<!-- Converted from tutorial/add-servers-automation.txt (reStructuredText). Includes are inlined. -->

# Provision Servers for Automation

## Overview

Ops Manager can automate operations for the MongoDB processes running on your
hosts. Ops Manager can both discover existing processes and deploy new ones.

Ops Manager Automation relies on an Automation Agent, which must be installed on
every server that runs a monitored MongoDB deployment. The Automation
Agents periodically poll Ops Manager to determine the goal configuration, deploy
changes as needed, and report deployment status back to Ops Manager.

## Procedure

Install the MongoDB Agent on each host that you want Ops Manager to manage.
The following procedure applies to all operating systems.

Instructions for a specific operating system can be read on
/tutorial/nav/install-mongodb-agent.

On Linux hosts, if you installed MongoDB with a package manager, use
the same package manager to install the MongoDB Agent. If you installed
MongoDB without a package manager, use an archive to install the
MongoDB Agent.

## Next Steps

Once you have installed the MongoDB Agent to all your hosts, you can
deploy your first replica set,
cluster, or standalone.
