<!-- Converted from tutorial/configure-windows-netsh-firewall.txt (reStructuredText). Includes are inlined. -->

# Configure Windows `netsh` Firewall for Self-Managed Deployments

On Windows Server systems, the `netsh` program provides
methods for managing the Windows Firewall. These firewall rules make it possible
for administrators to control what hosts can connect to the system,
and limit risk exposure by limiting the hosts that can connect to a
system.

This document outlines basic Windows Firewall configurations.
Use these approaches as a starting point for your
larger networking organization.
For a detailed over view of security
practices and risk management for MongoDB, see
/security.

**See also:**

[Windows Firewall](http://technet.microsoft.com/en-us/network/bb545423.aspx)
documentation from Microsoft.

## Overview

Windows Firewall processes rules in an ordered determined
by rule type, and parsed in the following order:

#. `Windows Service Hardening`
#. `Connection security rules`
#. `Authenticated Bypass Rules`
#. `Block Rules`
#. `Allow Rules`
#. `Default Rules`

By default, the policy in Windows Firewall allows all outbound connections
and blocks all incoming connections.

Given the default ports of all
MongoDB processes, you must configure networking rules that permit *only*
required communication between your application and the appropriate
`mongod.exe` and `mongos.exe` instances.

The configuration changes outlined in this document will create rules
which explicitly allow traffic from specific addresses and on specific
ports, using a default policy that drops all traffic that is not
explicitly allowed.

You can configure the Windows Firewall with using the `netsh` command line
tool or through a windows application.  On Windows Server 2008 this
application is Windows Firewall With Advanced Security in Administrative Tools.
On previous versions of Windows Server, access the
Windows Firewall application in the System and Security control panel.

The procedures in this document use the `netsh` command line tool.

## Patterns

This section contains a number of patterns and examples for
configuring Windows Firewall for use with MongoDB deployments.
If you have configured different ports using the `port` configuration
setting, you will need to modify the rules accordingly.

### Traffic to and from `mongod.exe` Instances

This pattern is applicable to all `mongod.exe` instances running
as standalone instances or as part of a replica set.
The goal of this pattern is to explicitly allow traffic to the
`mongod.exe` instance from the application server.

```bat
netsh advfirewall firewall add rule name="Open mongod port 27017" dir=in action=allow protocol=TCP localport=27017
```

This rule allows all incoming traffic to port `27017`, which
allows the application server to connect to the
`mongod.exe` instance.

Windows Firewall also allows enabling network access for
an entire application rather than to a specific port, as in the
following example:

```bat
netsh advfirewall firewall add rule name="Allowing mongod" dir=in action=allow program=" C:\Program Files\MongoDB\Server\3.4\bin\mongod.exe"
```

You can allow all access for a `mongos.exe` server, with the
following invocation:

```bat
netsh advfirewall firewall add rule name="Allowing mongos" dir=in action=allow program=" C:\Program Files\MongoDB\Server\3.4\bin\mongos.exe"
```

### Traffic to and from `mongos.exe` Instances

`mongos.exe` instances provide query routing for
sharded clusters. Clients connect to `mongos.exe`
instances, which behave from the client's perspective as
`mongod.exe` instances. In turn, the `mongos.exe`
connects to all `mongod.exe` instances that are components of
the sharded cluster.

Use the same Windows Firewall command to allow traffic to
and from these instances as you would from the `mongod.exe`
instances that are members of the replica set.

```bat
netsh advfirewall firewall add rule name="Open mongod shard port 27018" dir=in action=allow protocol=TCP localport=27018
```

### Traffic to and from a MongoDB Config Server

Configuration servers, host the config database that stores metadata
for sharded clusters. Each production cluster has three configuration
servers, initiated using the `mongod --configsvr`
option. [#config-option]_ Configuration servers listen for connections on port
`27019`. As a result, add the following Windows Firewall rules to the
config server to allow incoming and outgoing connection on port
`27019`, for connection to the other config servers.

```bat
netsh advfirewall firewall add rule name="Open mongod config svr port 27019" dir=in action=allow protocol=TCP localport=27019
```

Additionally, config servers need to allow incoming connections from
all of the `mongos.exe` instances in the cluster *and* all
`mongod.exe` instances in the cluster. Add rules that
resemble the following:

```bat
netsh advfirewall firewall add rule name="Open mongod config svr inbound" dir=in action=allow protocol=TCP remoteip=<ip-address> localport=27019
```

Replace `<ip-address>` with the addresses of the
`mongos.exe` instances and the shard `mongod.exe`
instances.

### Traffic to and from a MongoDB Shard Server

For shard servers, running as `mongod --shardsvr`
[#shard-option]_ Because the default port number is `27018` when running 
with the `shardsvr` value for the `clusterRole` setting, 
you must configure the following Windows Firewall rules to allow 
traffic to and from each shard:

```bat
netsh advfirewall firewall add rule name="Open mongod shardsvr inbound" dir=in action=allow protocol=TCP remoteip=<ip-address> localport=27018
netsh advfirewall firewall add rule name="Open mongod shardsvr outbound" dir=out action=allow protocol=TCP remoteip=<ip-address> localport=27018
```

Replace the `<ip-address>` specification with the IP address of all
`mongod.exe` instances. This allows you to permit incoming
and outgoing traffic between all shards including constituent replica
set members to:

- all `mongod.exe` instances in the shard's replica sets.

- all `mongod.exe` instances in other shards. [#migrations]_

Furthermore, shards need to be able make outgoing connections to:

- all `mongos.exe` instances.

- all `mongod.exe` instances in the config servers.

Create a rule that resembles the following, and replace the
`<ip-address>` with the address of the config servers and the
`mongos.exe` instances:

```bat
netsh advfirewall firewall add rule name="Open mongod config svr outbound" dir=out action=allow protocol=TCP remoteip=<ip-address> localport=27018
```

### Provide Access For Monitoring Systems

The `mongostat` diagnostic tool, when running with the
`--discover` needs to be able to reach
all components of a cluster, including the config servers, the shard
servers, and the `mongos.exe` instances.

## Manage Windows Firewall Configurations

This section contains a number of basic operations for managing and
using `netsh`. While you can use the GUI front ends to manage the
Windows Firewall, all core functionality is accessible is
accessible from `netsh`.

### Delete Windows Firewall Rules for Default MongoDB Ports

To delete the firewall rule allowing `mongod.exe` traffic:

```bat
netsh advfirewall firewall delete rule name="Open mongod port 27017" protocol=tcp localport=27017

netsh advfirewall firewall delete rule name="Open mongod shard port 27018" protocol=tcp localport=27018
```

### List All Windows Firewall Rules

To return a list of all Windows Firewall rules:

```bat
netsh advfirewall firewall show rule name=all
```

### Reset Windows Firewall

To reset the Windows Firewall rules:

```bat
netsh advfirewall reset
```

### Backup and Restore Windows Firewall Rules

To simplify administration of larger systems, you can export or import
Windows Firewall rules.

- To export all Windows Firewall rules, run the following command:

  ```bat
  netsh advfirewall export "C:\temp\MongoDBfw.wfw"
  ```

  Replace `"C:\temp\MongoDBfw.wfw"` with a path of your choosing.

- To import Windows Firewall rules, run the following command:

  ```bat
  netsh advfirewall import "C:\temp\MongoDBfw.wfw"
  ```

  Replace `"C:\temp\MongoDBfw.wfw"` with the path to the file that
  contains your Windows Firewall rules.
