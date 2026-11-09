<!-- Converted from tutorial/monitor-with-snmp.txt (reStructuredText). Includes are inlined. -->

# Monitor MongoDB With SNMP on Linux

**Note:** Enterprise Feature (Deprecated)

Starting in MongoDB 6.0, SNMP is deprecated and will be removed in the
next release. To monitor your deployment, use [MongoDB Ops Manager](https://www.mongodb.com/docs/ops-manager/current/). 

SNMP is only available in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server).

## Overview

MongoDB Enterprise can provide database metrics via SNMP, in
support of centralized data collection and aggregation. This procedure
explains the setup and configuration of a `mongod` instance
as an SNMP subagent, as well as initializing and testing of SNMP
support with MongoDB Enterprise.

**See also:**

/tutorial/troubleshoot-snmp and
/tutorial/monitor-with-snmp-on-windows for
complete instructions on using MongoDB with SNMP on Windows
systems.

## Considerations

- SNMP support is only available in `mongod`.
  Other MongoDB tools such as `mongos` do not support SNMP.
- `mongod` does not support the use of SNMP traps.

## Configuration Files

MongoDB Enterprise includes the following SNMP configuration files:

- `MONGOD-MIB.txt`:

  The management information base (MIB) file that defines MongoDB's
  SNMP output. On Ubuntu and Debian platforms, this file is shipped
  compressed as `MONGOD-MIB.txt.gz` and must be decompressed with
  `gunzip`.

- `mongod.conf.subagent`:

  The configuration file to run `mongod` as the SNMP
  subagent. This file sets SNMP run-time configuration options,
  including the `agentXSocket` to connect to the SNMP master.

- `mongod.conf.master`:

  The configuration file to run `mongod` as the SNMP
  master. This file sets SNMP run-time configuration options,
  including the `agentaddress` to run on.

The MongoDB SNMP configuration files are provided with your MongoDB
Enterprise installation, as follows:

- If you installed MongoDB Enterprise via a package manager, these files
  are installed to the following directory as part of the package
  installation process:

  | Platform | Path |
  |---|---|
  | RHEL / CentOS | `/usr/share/doc/mongodb-enterprise-server-6.0.21` |
  | Ubuntu / Debian | `/usr/share/doc/mongodb-enterprise-server` |
  | SUSE | `/usr/share/doc/packages/mongodb-enterprise-server` |

- If you installed MongoDB Enterprise from a `.tgz` tarball, these
  files were included in the tarball.

## Procedure

**Step 1: Copy configuration files.**

Copy the MongoDB SNMP configuration files from their installation
location to their target directories, according to your platform:

**rhel-centos:**

#. Navigate to the location where the SNMP files were installed.
   For example, if you installed the latest version of MongoDB via
   the `yum` package manager:

   ```bash
   cd /usr/share/doc/mongodb-enterprise-server-6.0.21
   ```

#. Copy the two MongoDB SNMP files to their target directories:

   ```bash
   sudo cp MONGOD-MIB.txt /usr/share/snmp/mibs/
   sudo cp mongod.conf.subagent /etc/snmp/mongod.conf
   ```

**ubuntu-debian:**

#. Navigate to the location where the SNMP files were installed.
   For example, if you installed MongoDB via the `apt` package
   manager:

   ```bash
   cd /usr/share/doc/mongodb-enterprise-server
   ```

#. Copy the `MONGOD-MIB.txt.gz` file to its target directory,
   and unzip it:

   ```bash
   sudo cp MONGOD-MIB.txt.gz /usr/share/snmp/mibs/
   sudo gunzip /usr/share/snmp/mibs/MONGOD-MIB.txt.gz
   ```

#. Copy the `mongod.conf.subagent` file to its target directory:

   ```bash
   sudo cp mongod.conf.subagent /etc/snmp/mongod.conf
   ```

**suse-linux:**

#. Navigate to the location where the SNMP files were installed.
   For example, if you installed the latest version of MongoDB via
   the `zypper` package manager:

   ```bash
   cd /usr/share/doc/packages/mongodb-enterprise-server
   ```

#. Copy the two MongoDB SNMP files to their target directories:

   ```bash
   sudo cp MONGOD-MIB.txt /usr/share/snmp/mibs/
   sudo cp mongod.conf.subagent /etc/snmp/mongod.conf
   ```

**Step 2: Configure SNMP.**

**rhel-centos:**

Edit the `/etc/snmp/snmpd.conf` file, and add the following:

```bash
# sec.name          source         community
  com2sec local     localhost       mongodb
# group.name        sec.model  sec.name
  group MyRWGroup   any        local
# incl/excl   subtree            mask
  view all    included  .1       80
# context               sec.model sec.level prefix read   write  notif
  access MyRWGroup ""   any       noauth    0      all    all    all

master agentx
AgentXSocket /tmp/agentx/master
AgentXPerms 0777 0777 mongod mongod
```

**ubuntu-debian:**

#. Install `snmpd` if it is not already installed:

   ```bash
   sudo apt-get install snmpd
   ```

#. Edit the `/etc/snmp/snmpd.conf` file, and add the following:

   ```bash
   # sec.name          source         community
     com2sec local     localhost       mongodb
   # group.name        sec.model  sec.name
     group MyRWGroup   any        local
   # incl/excl   subtree            mask
     view all    included  .1       80
   # context               sec.model sec.level prefix read   write  notif
     access MyRWGroup ""   any       noauth    0      all    all    all

   AgentXSocket /tmp/agentx/master
   AgentXPerms 0777 0777 mongodb mongodb
   ```

**suse-linux:**

Edit the `/etc/snmp/snmpd.conf` file, and add the following:

```bash
# sec.name          source         community
  com2sec local     localhost       mongodb
# group.name        sec.model  sec.name
  group MyRWGroup   any        local
# incl/excl   subtree            mask
  view all    included  .1       80
# context               sec.model sec.level prefix read   write  notif
  access MyRWGroup ""   any       noauth    0      all    all    all

master agentx
AgentXSocket /tmp/agentx/master
AgentXPerms 0777 0777 mongod mongod
```

This configuration defines a UNIX domain socket for communication
between the *master* (`snmpd`) and *sub-agent* (MongoDB), and
defines basic SNMP permissions for access to the relevant MongoDB
SNMP fields.

**Note:**

To bind your master to a non-localhost IP address, add that IP
address to the `agentaddress` field in the
`/etc/snmp/snmpd.conf` file, and update the appropriate network
security ACLs to permit a valid address range. An address range of
10.0.0.0/8 with a security name of "mynetwork" has been provided in
the `mongod.conf.master` configuration file as an example.

The above configuration is given as an example only; you may wish to
customize permissions based on your site security requirements. While
MongoDB support can provide guidance on configuring MongoDB for SNMP,
configuring SNMP on operating systems is out of scope.

**Step 3: Start SNMP.**

Start SNMP on your system using the initialization system appropriate
for your version of Linux:

- For Linux systems using **systemd** (`systemctl` command):

  ```bash
  sudo systemctl start snmpd
  ```

- For Linux systems using **System V init** (`service` command):

  ```bash
  sudo service snmpd start
  ```

**Step 4: Start MongoDB.**

Start `mongod` with the
`snmp-subagent` to send data to the
SNMP master.

```sh
mongod --snmp-subagent
```

**Step 5: Confirm SNMP data retrieval.**

Verify that MongoDB is accessible for SNMP queries with the
`snmpwalk` testing command.

**rhel-centos:**

#. Install `snmpwalk` on your system:

   ```bash
   sudo yum install net-snmp-utils
   ```

#. Run `snmpwalk` with the following parameters to verify the
   ability to collect data from `mongod`: 

   ```bash
   snmpwalk -m /usr/share/snmp/mibs/MONGOD-MIB.txt -v 2c -c mongodb 127.0.0.1:161 1.3.6.1.4.1.34601
   ```

**ubuntu-debian:**

#. **DEBIAN ONLY**: If necessary, add the `non-free`
   repository to your `/etc/apt/sources.list` file to access
   the `snmp-mibs-downloader` package. For example, on Debian 9
   "Stretch", the primary repo entries might look like this:

   ```bash
   deb http://deb.debian.org/debian stretch main non-free
   deb-src http://deb.debian.org/debian stretch main non-free
   ```

#. **DEBIAN / UBUNTU**: Install the `snmp-mibs-downloader`
   package to supply necessary MIB files, then restart the
   `snmpd` service to reload the new MIB files:

   ```bash
   sudo apt-get update
   sudo apt-get -y install snmp-mibs-downloader
   sudo service snmpd restart          
   ```

#. **DEBIAN / UBUNTU**: Run `snmpwalk` with the following
   parameters to verify the ability to collect data from
   `mongod`: 

   ```bash
   snmpwalk -m /usr/share/snmp/mibs/MONGOD-MIB.txt -v 2c -c mongodb 127.0.0.1:161 1.3.6.1.4.1.34601
   ```

**suse-linux:**

```bash
snmpwalk -m /usr/share/snmp/mibs/MONGOD-MIB.txt -v 2c -c mongodb 127.0.0.1:161 1.3.6.1.4.1.34601
```

The `snmpwalk` command should display current values for SNMP fields
such as `sysUpTime`, and `memoryResident`, among others.

**Note:**

The port used in the above `snmpwalk` testing command, port 161,
is the default port for the `snmpd` service, *not* the primary
`port` for the `mongod`. If you have
configured a different port for your `snmpd` service, supply that
here instead.

## Optional: Run MongoDB as SNMP Master

You can run `mongod` with the
`snmp-master` option for testing
purposes. To do this, use the SNMP master configuration file instead of
the subagent configuration file. From the directory containing the
unpacked MongoDB installation files:

```bash
cp mongod.conf.master /etc/snmp/mongod.conf
```

**Note:**

To bind your master to a non-localhost IP address, add that IP
address to the `agentaddress` field in the
`/etc/snmp/mongod.conf` file, and update the appropriate network
security ACLs to permit a valid address range. An address
range of 10.0.0.0/8 with a security name of "mynetwork" has been
provided in the master configuration file as an example.

Then, start `mongod` with the
`snmp-master` option:

```bash
mongod --snmp-master
```
