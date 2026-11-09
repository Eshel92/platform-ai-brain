<!-- Converted from tutorial/troubleshoot-snmp.txt (reStructuredText). Includes are inlined. -->

# Troubleshoot SNMP

**Note:** Enterprise Feature (Deprecated)

Starting in MongoDB 6.0, SNMP is deprecated and will be removed in the
next release. To monitor your deployment, use [MongoDB Ops Manager](https://www.mongodb.com/docs/ops-manager/current/). 

SNMP is only available in MongoDB Enterprise.

MongoDB Enterprise on macOS does *not* include support for SNMP due
to SERVER-29352.

## Overview

MongoDB Enterprise can provide database metrics via SNMP, in
support of centralized data collection and aggregation. This document
identifies common problems you may encounter when deploying MongoDB
Enterprise with SNMP as well as possible solutions for these issues.

See /tutorial/monitor-with-snmp
and /tutorial/monitor-with-snmp-on-windows for
complete installation instructions.

## Issues

### Failed Global Initialization

If you receive the following error message when trying to monitor with
SNMP:

```none
<Timestamp> F CONTROL [main] Failed global initialization: Bad Value: snmp.subagent is not allowed when snmp.disabled is specified
```

Ensure that you have not `disabled SNMP access` to `mongod`.

By default, SNMP access to `mongod` instances is enabled.
Starting in MongoDB 4.0.6, you can disable SNMP access using either
command-line option `--snmp-disabled`
or the configuration file option `snmp.disabled`.

### Failed to Connect

The following in the `mongod` logfile:

```none
Warning: Failed to connect to the agentx master agent
```

AgentX is the SNMP agent extensibility protocol defined in Internet
[RFC 2741](http://www.ietf.org/rfc/rfc2741.txt). It explains how
to define additional data to monitor over SNMP. When MongoDB fails
to connect to the agentx master agent, use the following procedure to
ensure that the SNMP subagent can connect properly to the SNMP master.

#. Make sure the master agent is running.

#. Compare the SNMP master's configuration file with the subagent
   configuration file. Ensure that the agentx socket definition is
   the same between the two.

#. Check the SNMP configuration files to see if they specify using UNIX
   Domain Sockets. If so, confirm that the `mongod` has
   appropriate permissions to open a UNIX domain socket.

### Error Parsing Command Line

One of the following errors at the command line:

```none
Error parsing command line: unknown option snmp-master
try 'mongod --help' for more information
```

```none
Error parsing command line: unknown option snmp-subagent
try 'mongod --help' for more information
```

`mongod` binaries that are not part of the Enterprise
Edition produce this error. Install the Enterprise Edition and attempt to start
`mongod` again.

Other MongoDB binaries, including `mongos` will produce
this error if you attempt to start them with
`snmp-master` or
`snmp-subagent`. Only
`mongod` supports SNMP.

MongoDB Enterprise on macOS does *not* include support for SNMP due
to SERVER-29352.

### Error Starting `SNMPAgent`

The following line in the log file indicates
that `mongod` cannot read the `mongod.conf` file:

```none
[SNMPAgent] warning: error starting SNMPAgent as master err:1
```

If running on Linux, ensure `mongod.conf` exists in the `/etc/snmp`
directory, and ensure that the `mongod` UNIX user has
permission to read the `mongod.conf` file.

If running on Windows, ensure `mongod.conf` exists in
`C:\snmp\etc\config`.
