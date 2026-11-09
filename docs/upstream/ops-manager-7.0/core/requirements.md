<!-- Converted from core/requirements.txt (reStructuredText). Includes are inlined. -->

# Ops Manager System Requirements

This section describes the hardware, software, and networking
requirements for the hosts that run the
Ops Manager components.

**Important:**

Before deploying hosts, use the /core/installation-checklist
to plan your configuration.

For requirements for the MongoDB instances running as the Ops Manager
Application Database and the Backup Database, see
/tutorial/prepare-backing-mongodb-instances.

## Hardware Requirements

**Note:**

When using the term *hardware* on this page, it should be
understood as the specifications per host using one of the
following architectures:

- physical hardware,
- hardware components allocated to a virtual host,
- hardware components allocated to a virtual container, or
- hardware components allocated to a Kubernetes Worker Node.

Each host must meet the total *RAM* and *disk capacity* requirements
for all Ops Manager components that it serves:

- Ops Manager application
- Ops Manager application databases
- Head databases for the active Backup Daemon(s)
- Backup blockstore databases

**Example:**

You want to serve both the Ops Manager application and a
`Backup Daemon` on one host. 
This Ops Manager configuration will manage and monitor 300 MongoDB hosts,
back up 200 hosts, and run FCV (Feature Compatibility Version) 4.2 or later. The
total disk capacity of all databases being backed up is 4 TB. 
The total requirements would be:

- Ops Manager application needs 15 GB of RAM.
- The Backup Daemon also needs at least 100 GB 
  of available disk capacity.

This example host would require a minimum of 15 GB of RAM and 100 GB
of disk capacity.

**Warning:** Potential for Production Failure

Your Ops Manager instance can fail in production if you fail to configure the following:

- Ops Manager hosts per the /core/requirements.

- MongoDB hosts per the
  Production Notes in
  the MongoDB manual. MongoDB instances in Ops Manager include:

  - The Ops Manager Application Database,
  - Each blockstore.
  - Each Ops Manager Backup Daemon `head database`. This only
    applies to FCV 4.0 and earlier. FCV 4.2 and later do not use
    `head databases` for backups.

### Ops Manager Hardware Requirements

Every host that serves the Ops Manager application must meet the
following hardware requirements. Note that connecting too many hosts 
to a single project may cause performance issues.

| Number of Monitored Hosts | CPU Cores | Physical Memory [1]_ | Disk |
|---|---|---|---|
| Up to 400 monitored hosts | 4+ | 15 GB | 10 GB for Ops Manager Application in `/opt` plus storage for logs [2]_ |
| Up to 2,000 monitored hosts | 8+ | 15 GB | 10 GB for Ops Manager Application in `/opt` plus storage for logs [2]_ |
| More than 2,000 hosts | Contact MongoDB Account Manager | Contact MongoDB Account Manager | Contact MongoDB Account Manager |

### Ops Manager Application Database Hardware Requirements

The Ops Manager Application Database
runs as a three-member replica set that runs on dedicated
hosts.

Every host that serves the Ops Manager Application Database must meet the
following hardware (physical or virtual) requirements. Note that connecting 
too many hosts to a single project may cause performance issues.

| Number of Monitored Hosts | RAM | Disk Capacity | CPU Cores |
|---|---|---|---|
| Up to 400 | 8 GB RAM plus the RAM required for the `mongod` application | 200 GB | 4 × 2 GHz+ |
| Up to 2,000 | 15 GB RAM plus the RAM required for the `mongod` application | 500 GB | 4 × 2 GHz+ |
| More than 2,000 | Contact your MongoDB Account Manager | Contact your MongoDB Account Manager | Contact your MongoDB Account Manager |

For the best performance, use:

- SSDs to store your Ops Manager
  Application Databases.

- The WiredTiger storage engine. For the differences between the
  WiredTiger and MMAPv1 storage engines, see
  the types of storage engines in
  the MongoDB manual.

Disk capacity estimates are *approximate*. The needed disk capacity can
increase *or* decrease due to the number of databases being monitored.

### Backup Daemon Hardware Requirements

**Important:**

Before getting started with Backup, *contact your MongoDB Account
Manager* to help estimate the storage requirements for your Backup
Daemon host.

Each host on which you activate the `Backup Daemon` must meet
the following requirements plus
those for Ops Manager.

Each host that serves an active Backup Daemon has the following
hardware requirements:

**fcv42:**

The Backup Daemon should have at least 100 GB of available disk
capacity.

**fcv40:**

| Number of hosts | CPU Cores | RAM |
|---|---|---|
| Up to 200 | 4+ × 2 GHz+ | 15 GB additional RAM |

The Backup Daemon creates `head databases`
that replicate data for each replica set assigned to the Daemon.
Typically, each host on which you activate the Backup Daemon
needs to store 2.0 to 2.5 times the sum of the size on disk of
all the backed-up replica sets.

Specifically, each host must have:

- The disk capacity and write capacity to maintain each head
  database, **plus**

- The disk capacity to store an additional copy of the data for
  each head database to support
  `point-in-time restores`.

Contact your MongoDB Account Manager to determine disk capacity and
throughput requirements.

### Backup Database Hardware Requirements

If you use Ops Manager Backup, you must provision hosts for the Backup
Database.

Host requirements for the Backup Database vary, depending on whether
you use a blockstore database or file system storage to store your
snapshots. The Backup Database always holds
oplog data.

If you store snapshots in the Backup Database, its hosts typically
must have enough capacity to store 2 to 3 times the total backed-up
production data size. Snapshots are compressed and de-duplicated at
the block level in the blockstore.

Your specific requirements depend on your data compressibility and
change rate. *Contact your MongoDB Account Manager* to help estimate
the use case and workload-dependent storage requirements for your
Backup Database hosts.

If you store snapshots in the Backup Database, each data-bearing member
must meet the following requirements:

| CPU Cores | Disk Capacity | RAM |
|---|---|---|
| 4 × 2 GHz+ | The minimum disk capacity required for the Ops Manager blockstore uses the following formula: (2 to 3 times the total size of the `dbPath`) * 2 (to allow groom jobs) Contact [MongoDB Support](https://support.mongodb.com/welcome) to accurately determine your minimum disk capacity. | 8 GB of RAM per TB of blockstore disk to provide good snapshot and restore speed. Ops Manager defines 1 TB of blockstore as 1024`4` bytes. |

Contact your MongoDB Account Manager to determine disk capacity and
throughput requirements.

If you will *not* store snapshots in the Backup Database, each
data-bearing member must meet the following requirements:

| CPU Cores | Disk Capacity |
|---|---|
| 4 × 2 GHz+ | The size of your oplogs compressed for the configured point in time window. The default is 24 hours. |

## Network Requirements

### Internet Site Access

If you configured Ops Manager to download binaries direct from the
Internet, Ops Manager requires access to the following Internet sites over
HTTPS (Hypertext Transfer Protocol Secure) using both IPv4 (Internet Protocol version 4) and IPv6 (Internet Protocol version 6) requests to the Internet:

| Site | Purpose |
|---|---|
| downloads.mongodb.com, downloads.mongodb.org | To download MongoDB Enterprise Builds. |
| opsmanager.mongodb.com | To download the MongoDB `version manifest`. |
| fastdl.mongodb.org | To download MongoDB Community Builds. |

### Latency between Ops Manager and Backing Database Hosts

Connections between the Ops Manager Application host and its Application
Database, Oplog, and blockstore replica sets must have the lowest
possible network latency. With deployments exceeding 200 MongoDB hosts,
latency between your Ops Manager Application components should be under 1 ms.
Please contact MongoDB Support
if you anticipate that your network environment cannot meet this
requirement.

### TCP Keepalive Setting

Many Ops Manager components connect to a running `mongod` process. These
include:

- the application database,
- any backup databases, and
- any MongoDB databases that the MongoDB Agent manages.

The systems that host these components send data traffic to each other
to verify an active connection. The TCP (Transmission Control Protocol) keepalive setting determines
how often to run this check. Most systems use the default value of
**7200** seconds (two hours).

The network connection may drop within that timeframe. Without an
existing connection, Ops Manager must create a new connection to that
`mongod` process. This can delay communication or result in network
timeouts or socket errors. To prevent this issue, reduce the keepalive
value to increase the verification checks. All Ops Manager components must
use the same keepalive value.

To learn how to set this to the recommended value, see
faq-keepalive in the MongoDB Server Manual.

### MongoDB and MongoDB Agent Host Access

Each MongoDB and MongoDB Agent host should self-identify as its FQDN (fully qualified domain name)
to ensure reliable connectivity.

tabs:
  - id: linux
    name: Linux
    content: |

      Use the following command to find the host FQDN (fully qualified domain name):

      ```shell
      > hostname -f
      ```

      Your result should look like this:

      ```shell
      mongodb.example.com
      ```

  - id: windows
    name: Windows
    content: |

      Windows hosts host must be connected to the internet and
      attached to a Active Directory domain. 

      Use the following command to find the host FQDN (fully qualified domain name):

      ```powershell
      PS C:\> systeminfo | findstr /B /C:"Host" /C:"Domain"
      ```

      Your result should look like this:

      ```powershell
      Host Name:                 mongodb
      Domain:                    example.com
      ```

      Combine the `Host Name` and `Domain` with a `.` to get
      the FQDN (fully qualified domain name). With the previous example, the FQDN (fully qualified domain name) is
      `mongoodb.example.com`.

### Accessible Ports

The Ops Manager Application must be able to connect to users and MongoDB
Agents over HTTP (Hypertext Transfer Protocol) or HTTPS (Hypertext Transfer Protocol Secure). MongoDB Agents must be able to
connect to MongoDB client MongoDB databases.

Though Ops Manager only requires open HTTP (Hypertext Transfer Protocol) (or HTTPS (Hypertext Transfer Protocol Secure)) and MongoDB
network ports to connect with users and to databases, what ports are
opened on a firewall depend upon what capabilities are enabled:
encryption, authentication and monitoring.

This page defines which systems need to connect to which ports on
other systems.

Ops Manager connects with a number of services. This page explains the
ports that must be opened to deploy the various components used with
an Ops Manager deployment.

The specific ports that must be open on any intermediate firewalls
depend upon what capabilities are enabled, such as encryption,
authentication, and monitoring.

(Figure: /images/network-ports.png)

**Tip:**

All ports listed in the following sections are either the port
specified in the documentation for MongoDB installations or the
[known ports](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt)
for the specific service assigned by the IANA (Internet Assigned Numbers Authority). If the port
number can be changed, it is noted after the table in each
section.

To run Ops Manager without an Internet connection, see
/tutorial/configure-local-mode/ to ensure you have all of
the necessary binaries to run Ops Manager without an Internet
connection.

### Open Ports to Access Ops Manager

Ops Manager requires the following minimum network port requirements:

* Both Ops Manager users and MongoDB Agents must be able to connect to
  the Ops Manager application over HTTP (Hypertext Transfer Protocol) or HTTPS (Hypertext Transfer Protocol Secure).

* Ops Manager must be able to connect to the mongod running
  the Ops Manager application MongoDB databases.

* For each Ops Manager project, MongoDB Agents must be able to connect
  to all client MongoDB processes (`mongod` or `mongos`).

* The Ops Manager application must also be able to send email to
  Ops Manager users.

To use Ops Manager, open the following ports to the specified hosts.

* - Service
  - Default Port
  - Transport
  - Direction
  - Purpose
  - Uses TLS (Transport Layer Security)?

* - HTTP (Hypertext Transfer Protocol)
  - 8080
  - TCP (Transmission Control Protocol)
  - Inbound
  - Provides a web connection to Ops Manager from users and MongoDB
    Agents.
  - No

* - HTTPS (Hypertext Transfer Protocol Secure)
  - 8443
  - TCP (Transmission Control Protocol)
  - Inbound
  - Provides a secure web connection to Ops Manager from users and
    MongoDB Agents.
  - Yes

* - HTTP (Hypertext Transfer Protocol) or HTTPS (Hypertext Transfer Protocol Secure)
  - 8090
  - TCP (Transmission Control Protocol)
  - Inbound
  - Provides a health-check endpoint for monitoring Ops Manager
    through a monitoring service like Zabbix or Nagios. It is
    only available through `localhost` and is disabled by
    default.

    To enable it, see enable-debug-endpoints. When enabled,
    you can access the endpoint at:

    ```http
    http://127.0.0.1:8090/health
    ```

    IMPORTANT: This port is only accessible from `localhost`
    (or `127.0.0.1`). The port number *can* be changed from
    `8090` to another value.

    The API (Application Programming Interface) endpoint provides the ability to check connections
    from the HTTP (Hypertext Transfer Protocol) Service to the
    Ops Manager Application Database
    and the Backup Snapshot Storage.

    A successful response returns the following:

    ```json
    {
      "mms_db": "OK",
      "backup_db": "OK"
    }
    ```

  - Optional

* - MongoDB
  - 27017
  - TCP (Transmission Control Protocol)
  - Outbound
  - Connects to MongoDB application, backup and client databases.
  - Optional

* - SMTP (Simple Mail Transport Protocol)
  - 587
  - TCP (Transmission Control Protocol)
  - Outbound
  - Sends emails from Ops Manager to an SMTP (Simple Mail Transport Protocol) host or to
    [AWS SES](https://aws.amazon.com/ses/).
  - Optional

**Note:**

- To set a non-default port for Ops Manager, see /tutorial/manage-ports/.

- To configure a different port for the application database, see
  `mongo.mongoUri`.

- To configure a different port for a client database, see
  /tutorial/deploy-standalone, /tutorial/deploy-replica-set,
  or /tutorial/deploy-sharded-cluster for a new deployment
  or /tutorial/add-existing-mongodb-processes for an
  existing deployment.

### Open Ports to Access Ops Manager and MongoDB Hosts

(Figure: /images/open-ports-ops-manager-hosts.png)

Most Ops Manager administration can be performed through the user
interface. Some procedures require access to the operating system.
To permit your administrators to access your Ops Manager as well as
MongoDB hosts, open the following ports to those hosts.

| Service | Default Port | Transport | Direction | Purpose | Uses TLS (Transport Layer Security)? |
|---|---|---|---|---|---|
| ssh (Secure Shell) | 22 | TCP (Transmission Control Protocol) | Inbound | Linux System administration. | Yes |
| RDP (Remote Desktop Protocol) | 3389 | TCP (Transmission Control Protocol) | Inbound | Windows System administration. | No |

### Open Ports to Back Up, Restore, and Query MongoDB Instances using Ops Manager

(Figure: /images/open-ports-backup-restore-query-ops-manager.png)

Ops Manager can back up MongoDB databases to one or more storage
systems:

- A MongoDB database (`blockstore`)
- An S3-compatible storage bucket (S3-compatible storage blockstore)
- A file system (`file system store`).

To back up MongoDB hosts, open the following ports to the preferred
backup hosts (blockstore, S3-compatible storage snapshot store and/or file system
snapshot store):

| Service | Default Port | Transport | Direction | Purpose | Uses TLS (Transport Layer Security)? |
|---|---|---|---|---|---|
| MongoDB | 27017 | TCP (Transmission Control Protocol) | Outbound | Back up snapshots of entire database to blockstore or snapshot metadata to S3-compatible storage blockstore metadata database. | Optional |
| HTTPS (Hypertext Transfer Protocol Secure) | 443 | TCP (Transmission Control Protocol) | Outbound | Back up database snapshot data to S3-compatible storage bucket. | Yes |
| NFS (Network File System) | 2049 | TCP (Transmission Control Protocol) | Outbound | Back up database snapshots to UNIX-/Linux-based file system. | No |
| CIFS (Common Internet File System) | 3020 | TCP (Transmission Control Protocol) | Outbound | Back up database snapshots to Windows-based file system. | No |
| Proxy Server | 25999 | TCP (Transmission Control Protocol) | Outbound | Query the snapshot backup host. | No |

Snapshots can also be restored using the link displayed in the
Ops Manager application. The same ports needed to use Ops Manager would
need to be open for the user to download the snapshot.

To find the download link, click Continuous Backup, then the
Restore History tab, then click the download
link next to the snapshot.

**Note:**

- To configure a different port for the blockstore, see
  /tutorial/manage-blockstore-storage.

- To configure a different port for the S3-compatible storage Snapshot Store metadata
  database, see /tutorial/manage-s3-blockstore-storage.

MongoDB 3.4.2 Enterprise and later provides the ability to query
backup snapshots. Ops Manager provisions these queryable snapshots as
read-only MongoDB instances, as described in
Query a Backup.
To query a backup snapshot, open the following ports:

| Service | Default Port | Transport | Direction | Purpose | Uses TLS (Transport Layer Security)? |
|---|---|---|---|---|---|
| MongoDB | 27700-27719 | TCP (Transmission Control Protocol) | Inbound | Enable communication between the app host and a queryable backup snapshot. | Optional |

### Open Ports to Authenticate Ops Manager Users using LDAP (Lightweight Directory Access Protocol)

(Figure: /images/open-ports-ops-manager-ldap.png)

MongoDB Enterprise users can authenticate Ops Manager users using LDAP (Lightweight Directory Access Protocol). To
authenticate using LDAP (Lightweight Directory Access Protocol), open the following ports on Ops Manager and
your LDAP (Lightweight Directory Access Protocol) host.

| Service | Default Port | Transport | Direction | Purpose | Uses TLS (Transport Layer Security)? |
|---|---|---|---|---|---|
| LDAP (Lightweight Directory Access Protocol) | 389 | UDP (User Datagram Protocol) | Both | Authenticate and/or authorize Ops Manager users against LDAP (Lightweight Directory Access Protocol) host. | No |
| LDAPS (Secure Lightweight Directory Access Protocol) | 636 | UDP (User Datagram Protocol) | Both | Authenticate and/or authorize Ops Manager users against LDAP (Lightweight Directory Access Protocol) host. | Yes |

To configure the Ops Manager LDAP (Lightweight Directory Access Protocol) URI (Uniform Resource Identifier) strings, including
configuring a non-standard port, see ldap-settings.

### Open Ports to Authenticate with MongoDB

(Figure: /images/open-ports-ops-manager-mongo-auth.png)

MongoDB Enterprise users can use Kerberos or LDAP (Lightweight Directory Access Protocol) to authenticate
MongoDB users. To authenticate using LDAP (Lightweight Directory Access Protocol) or Kerberos, open the
following ports between the MongoDB client databases, Ops Manager, and
the Kerberos or LDAP (Lightweight Directory Access Protocol) host(s).

| Service | Default Port | Transport | Direction | Purpose | Uses TLS (Transport Layer Security)? |
|---|---|---|---|---|---|
| Kerberos | 88 | TCP (Transmission Control Protocol) / UDP (User Datagram Protocol) | Outbound | Request authentication for MongoDB users against Kerberos host. | No |
| Kerberos | 88 | UDP (User Datagram Protocol) | Inbound | Receive authentication for MongoDB users against Kerberos host. | No |
| LDAP (Lightweight Directory Access Protocol) | 389 | UDP (User Datagram Protocol) | Both | Authenticate and/or authorize MongoDB users against LDAP (Lightweight Directory Access Protocol) host. | No |
| LDAPS (Secure Lightweight Directory Access Protocol) | 636 | UDP (User Datagram Protocol) | Both | Authenticate and/or authorize MongoDB users against LDAP (Lightweight Directory Access Protocol) host. | Yes |

To configure Kerberos for authentication to the Ops Manager application
database, see configuration-kerberos-settings.

### Open Ports to Manage Encryption Keys using KMIP (Key Management Interoperability)

(Figure: /images/open-ports-ops-manager-kmip.png)

MongoDB Enterprise deployments using the WiredTiger storage engine
supports a native encryption option. You can use a KMIP (Key Management Interoperability) service to
manage the master encryption key. To support the encrypted storage
engine via KMIP (Key Management Interoperability), open the following ports between the Backup Daemon
hosts, the MongoDB hosts, and the KMIP (Key Management Interoperability) hosts.

| Service | Default Ports | Transport | Direction | Purpose | Uses TLS (Transport Layer Security)? |
|---|---|---|---|---|---|
| KMIP (Key Management Interoperability) | 5696 | TCP (Transmission Control Protocol) | Outbound | Send messages between MongoDB databases and KMIP (Key Management Interoperability) host. | Yes |

**Note:**

If you change the port for the KMIP (Key Management Interoperability) host, see
/tutorial/encrypt-snapshots to configure Ops Manager to use
that new port.

## Internet Site Access

If Ops Manager is not configured for
Local Mode,
it requires access to the following Internet sites over HTTPS (Hypertext Transfer Protocol Secure):

| Site | Purpose |
|---|---|
| downloads.mongodb.com, downloads.mongodb.org | To download MongoDB Enterprise Builds. |
| opsmanager.mongodb.com | To download the MongoDB `version manifest`. |
| fastdl.mongodb.org | To download MongoDB Community Builds. |

### Use resolvable hostnames

Each MongoDB Agent and Ops Manager instance must be able to resolve the
hostname for each host hosting a MongoDB instance or MongoDB Agent.

On each host, set their hostnames to fully qualified domain names
(FQDN (fully qualified domain name)) whenever possible. Consult the documentation for your
operating system as to how to find and set the hostname as an FQDN (fully qualified domain name).

Setting the FQDN (fully qualified domain name) on each host helps you know which host you are
using when logged into that host. To enable other hosts to know
what the other hosts' hostnames are, you need to provide a way for
those hosts to resolve hostnames.

There are two ways to configure hostname resolution.

#### Use a Domain Name Service

To make the hosts' hostnames resolvable, run a host with a domain name
service (DNS (Domain Name System)). DNS (Domain Name System) maps IP addresses to hostnames with a given
domain (such as `example.com`). This DNS (Domain Name System) host should have an entry
for each host in the deployment: Ops Manager, MongoDB Agent and MongoDB.
Entries for LDAP (Lightweight Directory Access Protocol), Kerberos, and email hosts as well as load
balancers would be recommended.

#### Edit Host Files

If a DNS (Domain Name System) setup is not possible, add entries for each host in the
`hosts` file of each system.

* - Operating System
  - `hosts` Location

* - Linux
  -

   ```sh
   /etc/hosts
   ```

* - Mac OS X
  -

   ```sh
   /private/etc/hosts
   ```

* - Windows
  -

   ```powershell
   %SystemRoot%\System32\drivers\etc\hosts
   ```

   This normally resolves to:

   ```powershell
   C:\Windows\System32\drivers\etc\hosts
   ```

The `hosts` file is a root-readable plain text and must be edited
with `root` or `Administrator` permissions. The entry format is
written as:

```ini
127.0.0.1   localhost
10.15.0.5   opsmgr.example.dev
10.15.10.15 rs1.example.dev
10.15.10.16 rs2.example.dev
10.15.10.17 rs3.example.dev
```

## Software Requirements

Hosts that run Ops Manager components must meet the following software
requirements:

**Important:**

Ops Manager 5.0 and later requires Bash 4.2 or later.

### Operating System Compatibility Matrices

#### Operating Systems Compatible with Ops Manager

Hosts that run Ops Manager must run on a 64-bit version of one of the
following operating systems:

##### Intel/AMD (`x86_64`) Hardware Architectures

| Operating System | Ops Manager 6.0 | Ops Manager 7.0 |
|---|---|---|
| Amazon Linux | 2 | 2, 2023 |
| Debian | 10, 11 | 11, 12 |
| RHEL (Red Hat Enterprise Linux) | 7, 8, 9 | 7 *(deprecated)*, 8, 9 |
| SUSE Linux Enterprise Server | 12, 15 | 12 *(deprecated)*, 15 |
| Ubuntu | 18.04, 20.04, 22.04 | 20.04 *(deprecated)*, 22.04 |

**Note:**

Though the MongoDB Agent can be installed on `s390x` and on
PowerPC (`ppc64le`) architectures, the Ops Manager Application *cannot* be
installed on these platforms. You must install the Ops Manager Application on one
of the platforms listed in the previous table.

Though support for Microsoft Windows Server platforms is discontinued in Ops Manager 5.0 and any later versions, you 
can use one of the 5.0 and later Ops Manager versions from the list of 
supported platforms in the 
previous table, or `deploy Ops Manager in a container with the 
Kubernetes Operator`.

#### Operating Systems Compatible with the MongoDB Agent

Hosts that run MongoDB Agents must run on a 64-bit version of one of
the following hardware architectures and operating systems. The 
following table lists the MongoDB Server versions that you can deploy 
with the MongoDB Agent on the associated platforms:

| Architecture | Distro/OS | 7.0 | 6.0 | 5.0 |
|---|---|---|---|---|
| x86_64 | RHEL/Oracle Linux 7 `1` | check-circle | check-circle | check-circle |
|  | RHEL/Rocky/Alma Linux/Oracle Linux 8 `1` | check-circle | check-circle | check-circle |
|  | RHEL/Rocky/Alma Linux/Oracle Linux 9 `1` | check-circle | check-circle | check-circle |
|  | Amazon Linux 2 | check-circle | check-circle | check-circle |
|  | Amazon Linux 2023 | check-circle |  |  |
|  | SUSE12 | check-circle | check-circle | check-circle |
|  | SUSE15 | check-circle | check-circle | check-circle |
|  | Debian 9 |  |  | check-circle |
|  | Debian 10 |  | check-circle | check-circle |
|  | Debian 11 | check-circle | check-circle | check-circle |
|  | Debian 12 | check-circle |  |  |
|  | Ubuntu 18.x |  | check-circle | check-circle |
|  | Ubuntu 20.x | check-circle | check-circle | check-circle |
|  | Ubuntu 22.x `2` | check-circle | check-circle |  |
|  | Windows | check-circle | check-circle | check-circle |
| ARM | RHEL 8 | check-circle | check-circle | check-circle |
|  | RHEL 9 | check-circle | check-circle |  |
|  | Amazon Linux 2 | check-circle | check-circle | check-circle |
|  | Amazon Linux 2023 | check-circle |  |  |
|  | Ubuntu 20.x | check-circle |  |  |
| PowerPC/ ppc64le | RHEL 7 | check-circle | check-circle | check-circle |
|  | RHEL 8 | check-circle | check-circle | check-circle |
| zSeries/ 390x | RHEL 7 | check-circle | check-circle | check-circle |
|  | RHEL 8 | check-circle | check-circle | check-circle |
|  | RHEL 9 | check-circle |  |  |

`1` MongoDB supports Oracle Linux running
RHCK (Red Hat Compatible Kernel) only. 
MongoDB doesn't support Oracle Linux running
UEK (Unbreakable Enterprise Kernel).

`2` `MongoDB Connector for BI` isn't supported on Ubuntu 22.04.

##### Intel/AMD (`x86_64`) Hardware Architectures

Support for running MongoDB Agent on Windows 2008 or
Windows Server 2008R2 ends beginning with Ops Manager 5.0. 

MongoDB Agent still supports managing MongoDB deployments
that run on Windows 2016, 2019, 2020.

**Note:**

As of Ops Manager Server 4.0.11, Windows architectures require
the [Visual C++ Redistributable Packages for Visual Studio 2013](https://www.microsoft.com/en-us/download/details.aspx?id=40784).

### Exec Options for `/var` Mount

Ops Manager requires the default `exec` option defined in 
`/etc/fstab` on the underlying host machine in order to run the required 
binaries stored in the volume backing the `/var` directory.

### Ulimits Requirements for Ops Manager Application

The Ops Manager package automatically raises the following `ulimits`:

- Open files

- Maximum user processes

- Virtual memory

RHEL (Red Hat Enterprise Linux) limits the maximum
number of user processes to `1024`. This overrides the general
user process limit (`ulimit -u`) setting.

For the userid that runs Ops Manager (`mongodb-mms` by default), 
add `soft` and `hard` `nproc` (number of processes) entries to the `/etc/security/limits.d/99-mongodb-nproc.conf` user process
configuration file. Use values that are larger than the RHEL (Red Hat Enterprise Linux) `1024` user process limit.

```apache
mongodb-mms soft nproc 200000
mongodb-mms hard nproc 500000
```

If `/etc/security/limits.d/99-mongodb-nproc.conf` does not exist, create it. Use the contents of the
`/etc/security/limits.d/90-nproc.conf` file as a template.

### MongoDB Version for Ops Manager Application Database and Backup Database

For the following Ops Manager release series, you may run its
backing databases on any of the following MongoDB versions:

| Ops Manager Release | MongoDB 4.2 | MongoDB 4.4 | MongoDB 5.0 | MongoDB 6.0 | MongoDB 7.0 |
|---|---|---|---|---|---|
| Ops Manager 7.0 | EOL | EOL | Deprecated | Supported | Supported |
| Ops Manager 6.0 | EOL | Deprecated | Supported | Supported | N/A |
| Ops Manager 5.0 | Deprecated | Supported | Supported | N/A | N/A |
| Ops Manager 4.4 | Supported | Supported | N/A | N/A | N/A |
| Ops Manager 4.2 | Supported | N/A | N/A | N/A | N/A |

**Note:**

A deprecated version still works with the corresponding Ops Manager
release, but we will remove the support for this version in the
next release. [MongoDB Support](https://support.mongodb.com) recommends migrating to a supported
version to avoid potential incompatibility issues.

To learn more, see [MongoDB Legacy Support Policy](https://www.mongodb.com/legal/support-policy/legacy) and 
[MongoDB Software Lifecycle Schedules for Ops Manager](https://www.mongodb.com/legal/support-policy/lifecycles).

Version support covers the full release series from the first to the
last release.

To learn more about MongoDB versioning, see
release-version-numbers in the MongoDB Manual.

**Important:**

Only the MongoDB Ops Manager backing databases must meet this
requirement. The MongoDB deployments that Ops Manager manages do not.
For the minimum versions required for managed MongoDB deployments,
see /reference/mongodb-compatibility/.

#### Ulimits Requirements for Backup Daemon and Backing Databases

Refer to the following pages in the MongoDB manual for `ulimit`
requirements for the hosts that run MongoDB (Backup Daemon and
Ops Manager Backing Databases hosts):

- MongoDB Production Notes

- MongoDB Ulimit Settings

### Email Service

Install and verify an Email Server. Ops Manager needs an email server to
send alerts and recover
user accounts. You may use an SMTP Server or an
AWS (Amazon Web Services) SES (Simple Email Service) server. To configure your Email Server, see
`Email Delivery Method Configuration`.

Many Linux host-oriented distributions include a local SMTP (Simple Mail Transport Protocol) server by
default. These include, but are not limited to:

- [Postfix](http://www.postfix.org)
- [Exim](https://www.exim.org)
- [Sendmail](https://www.proofpoint.com/us/open-source-email-solution)

Windows Server includes an SMTP (Simple Mail Transport Protocol) relay with Internet Information
Server.

You also may configure Ops Manager to send mail via third party
providers. These include, but are not limited to:

- [Gmail](https://www.google.com/gmail/)
- [Sendgrid](https://sendgrid.com)

### Install fontconfig on Linux Hosts

When installing Ops Manager version 4.0.13 or later on Linux hosts,
install the **fontconfig** package to enable data export from the
Status tab to PDF or PNG format.

### Client Web Browsers

To use Ops Manager, you must use one of the following supported browsers with
Javascript enabled:

| Supported Web Browser | Supported Version(s) |
|---|---|
| [Google Chrome](https://www.google.com/chrome/) | latest stable |
| [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/) | latest stable |
| [Microsoft Edge](https://www.microsoft.com/en-us/windows/microsoft-edge) | latest stable |
| [Apple Safari](https://www.apple.com/safari/) | latest stable |

Ops Manager displays a warning on non-supported browsers.
