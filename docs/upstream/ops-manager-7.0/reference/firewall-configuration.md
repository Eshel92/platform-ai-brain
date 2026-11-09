<!-- Converted from reference/firewall-configuration.txt (reStructuredText). Includes are inlined. -->

# Firewall Configuration

## Accessible Ports

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

## Open Ports to Access Ops Manager

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

## Open Ports to Access Ops Manager and MongoDB Hosts

(Figure: /images/open-ports-ops-manager-hosts.png)

Most Ops Manager administration can be performed through the user
interface. Some procedures require access to the operating system.
To permit your administrators to access your Ops Manager as well as
MongoDB hosts, open the following ports to those hosts.

| Service | Default Port | Transport | Direction | Purpose | Uses TLS (Transport Layer Security)? |
|---|---|---|---|---|---|
| ssh (Secure Shell) | 22 | TCP (Transmission Control Protocol) | Inbound | Linux System administration. | Yes |
| RDP (Remote Desktop Protocol) | 3389 | TCP (Transmission Control Protocol) | Inbound | Windows System administration. | No |

## Open Ports to Back Up, Restore, and Query MongoDB Instances using Ops Manager

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

## Open Ports to Authenticate Ops Manager Users using LDAP (Lightweight Directory Access Protocol)

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

## Open Ports to Authenticate with MongoDB

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

## Open Ports to Manage Encryption Keys using KMIP (Key Management Interoperability)

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

### Internet Site Access

If Ops Manager is not configured for
Local Mode,
it requires access to the following Internet sites over HTTPS (Hypertext Transfer Protocol Secure):

| Site | Purpose |
|---|---|
| downloads.mongodb.com, downloads.mongodb.org | To download MongoDB Enterprise Builds. |
| opsmanager.mongodb.com | To download the MongoDB `version manifest`. |
| fastdl.mongodb.org | To download MongoDB Community Builds. |
