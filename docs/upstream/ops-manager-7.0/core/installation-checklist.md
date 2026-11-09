<!-- Converted from core/installation-checklist.txt (reStructuredText). Includes are inlined. -->

# Installation Checklist

You must make several decisions based on the content of this page
before you install Ops Manager. During the installation process, you will
make choices based on these decisions.

To install Ops Manager:

1. Read the /application.

#. Plan your installation according to the questions on this page.

#. Provision servers that meet the /core/requirements.

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

#. Install the Application Database and optional Backup Database.

#. Install Ops Manager with one of the following methods:

   - om-install-rpm
   - om-install-deb
   - om-install-archive

   **Note:**

   To install a simple evaluation deployment on a single server, see
   /tutorial/install-simple-test-deployment.

## Topology Decisions

### Do you require redundancy and/or high availability?

The topology you choose for your deployment
affects the redundancy and availability of both your metadata and
snapshots, and the availability of the Ops Manager Application.

Ops Manager stores application metadata and snapshots in the Ops Manager Application
Database and Backup Database respectively. To provide data redundancy,
run each database as a three-member replica set on multiple
servers.

To provide high availability for write operations to the databases, set
up each replica set so that all three members hold data. This way, if a
member is unreachable the replica set can still write data. Ops Manager
uses `w:2` write concern, which
requires acknowledgement from the primary and one secondary for each
write operation.

To provide high availability for the Ops Manager Application, run at least two
instances of the application and use a load balancer. A load balancer
placed in front of the Ops Manager Application must not return cached content.
For more information, see
/tutorial/configure-application-high-availability.

The following tables describe the pros and cons for different
topologies.

#### Test Install

This deployment runs on one server and has no data-redundancy. If you
lose the server, you must start over from scratch.

|  |  |
|---|---|
| Pro | Needs only needs one server. |
| Con | If you lose the server, you lose everything: users and projects, metadata, backups, automation configurations, stored monitoring metrics, etc. |

#### Production Install with Highly Available Metadata and Snapshots

This install requires at least three servers. The replica sets for the
Ops Manager Application Database and the Backup Database each comprise at least
three *data-bearing* members. This requires sufficient storage and
memory.

|  |  |
|---|---|
| Pro | You can lose a member of the Ops Manager Application Database or Backup Database and still maintain Ops Manager availability. No Ops Manager functionality is lost while the member is down. |
| Con | Loss of the Ops Manager instance requires you to manually start a new Ops Manager instance. No Ops Manager functionality is available while the application is down. |

#### Production Install with a Highly Available Ops Manager Application

This runs multiple Ops Manager Applications behind a load balancer and
requires infrastructure outside of what Ops Manager offers. For details,
see /tutorial/configure-application-high-availability.

|  |  |
|---|---|
| Pro | Ops Manager continues to be available even when any individual server is lost. |
| Con | Requires a larger number of servers, and requires a load balancer capable of routing traffic to available application servers. |

### Will you deploy managed MongoDB instances on servers that have no internet access?

If the servers where you deploy MongoDB don't have internet access and if
you use Automation, then before you create the first managed MongoDB deployment
from Ops Manager, you must configure local mode and store the binaries.
MongoDB Agents can then download the binaries directly from Ops Manager.
To learn more, see /tutorial/configure-local-mode.

### Will you use a proxy for the Ops Manager application's outbound network connections?

If Ops Manager will use a proxy server to access external services, you
must configure the proxy settings in Ops Manager's `conf-mms.properties`
configuration file. If you have already started Ops Manager, you must
restart after configuring the proxy settings.

## Security Decisions

### Will you use authentication, TLS (Transport Layer Security), or both for the connections to the backing databases?

If you will use authentication or TLS (Transport Layer Security) for connections to the
Ops Manager Application Database and Backup Database, you must configure those
options on each database when
deploying the database
and then you must configure Ops Manager with the necessary certificate
information for accessing the databases. For details, see
/tutorial/configure-ssl-connection-to-backing-mongodb

### Will you use LDAP (Lightweight Directory Access Protocol) for user authenticate to Ops Manager?

If you want to use LDAP (Lightweight Directory Access Protocol) for user management, you can configure LDAP (Lightweight Directory Access Protocol)
authentication before or after creating your first project. There are
different prerequisites for implementing a new LDAP (Lightweight Directory Access Protocol) authentication
scheme or for converting an existing authentication scheme to LDAP (Lightweight Directory Access Protocol). To
learn more about these differences, see ldap-new-vs-convert.

For details on LDAP (Lightweight Directory Access Protocol) authentication, see
/tutorial/configure-for-ldap-authentication.

### Will you use TLS (Transport Layer Security) for connections to the Ops Manager application?

If you will use TLS (Transport Layer Security) for connections to Ops Manager from MongoDB Agents,
users, and the API (Application Programming Interface), then you must configure Ops Manager to use TLS (Transport Layer Security).
The procedure to install Ops Manager includes the option to configure
TLS (Transport Layer Security) access.

## Backup Decisions

### Will the servers that run your Backup Daemons have internet access?

If the servers that run your Backup Daemons have no internet access,
you must configure offline binary access for the Backup Daemon before
running the Daemon. The /tutorial/configure-local-mode page
covers the option to configure offline binary access.

### Are certain backups required to be in certain data centers?

If you need to assign backups of particular MongoDB deployments to
particular data centers, then each data center requires its own
Ops Manager instance, Backup Daemon, and MongoDB Agent. The separate
Ops Manager instances must share a single dedicated Ops Manager Application
Database. The MongoDB Agent in each data center must use the URL (Uniform Resource Locator) for
its local Ops Manager instance, which you can configure through either
different hostnames or split-horizon DNS (Domain Name System). For detailed requirements,
see /tutorial/assign-snapshot-stores-to-data-center.
