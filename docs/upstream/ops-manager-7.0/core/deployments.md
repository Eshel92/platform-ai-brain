<!-- Converted from core/deployments.txt (reStructuredText). Includes are inlined. -->

# Example Deployment Architectures

The following examples illustrate some possible MongoDB and Ops Manager
deployments.

## Considerations

On FCV 4.0 and earlier, for best performance on any of these installs, 
configure each backup host with two disk partitions: one for the snapshot 
store or File System Store and one for the head databases.

On FCV `4.2` and later, backups no longer require 
`head databases`. For more information, see 
backup-daemon.

## Test Install on a Single Host

For a test deployment, you can deploy all of the Ops Manager components to
a single host, as described in
/tutorial/install-simple-test-deployment.

(Figure: /images/ops-manager-test.png)

**Note:**

If you would like to test backup services, use the Ops Manager Application to
configure them. When
configuring Ops Manager,
you can specify the backup settings. 

For FCV 4.0 and earlier, the Backup Daemon service creates the 
`head databases` dynamically in that 
directory. The Backup Daemon service then manages these head
databases.

For FCV `4.2` and later, the application database stores 
snapshots of deployment state in 
backup cursors.

## Production Installs

### Redundant Metadata and Snapshots

This deployment provides redundancy for the
mms-application-database and backup-database in the
event of host failure. The deployment runs the database in a MongoDB
replica set with three data-bearing members with copies of the
data.

**Important:**

This deployment provides high availability for the Ops Manager Application.
Ops Manager uses a `w:2`
write concern, and can
tolerate the loss of one data-bearing node from the
mms-application-database. To make the deployment more
durable, enable journaling.

(Figure: /images/ops-manager-ha-single-database.png)

**Note:**

All hosts must satisfy the combined
hardware and software requirements for
both the systems specified in the **System Requirements** column.

* - Host
  - System Requirements
  - Purpose

* - 1

  -
    - Ops Manager Application

    - Ops Manager Application database

  - Serves the Ops Manager Application database primary and the snapshot
    store secondary.

* - 2

  -
    - Ops Manager Application

    - snapshot store

  - Serves the snapshot store primary and the Ops Manager Application
    database secondary.

* - 3

  -
    - Ops Manager Application database

    - snapshot store

  - Hosts the Ops Manager Application Database and snapshot store secondary
    replica set members.

    Replica sets provide data redundancy and are
    strongly recommended, but are not required for Ops Manager.

For an example tutorial on installing the minimally viable Ops Manager
installation, see Install a Simple Test Deployment on RHEL.

### Highly Available Ops Manager Application and Multiple snapshot stores

This Ops Manager deployment runs multiple instances behind a load
balancer to provide high availability for Ops Manager.
This deployment scales out to add an additional snapshot store.

(Figure: /images/ops-manager-ha-multiple-databases.png)

The deployment includes:

- two hosts that serve the Ops Manager Application and the Ops Manager Application
  Database

- four hosts that serve Ops Manager Application with Backup enabled and Backup
  Databases

- additional hosts to serve the remaining members of each replica set

Deploy an HTTP (Hypertext Transfer Protocol) Load Balancer to balance the HTTP (Hypertext Transfer Protocol) traffic for the
Ops Manager Application. Ops Manager does not supply an HTTP (Hypertext Transfer Protocol) Load Balancer. You
must provision, deploy, and configure it yourself. A load balancer
placed before of the Ops Manager Application hosts must not return cached
content.

All of the software services need to be able to communicate with
the Ops Manager Application Databases and the snapshot stores.
Configure your firewalls to allow traffic between these hosts
on the appropriate ports.

**Note:**

All hosts must satisfy the combined
hardware and software requirements for
both the systems specified in the **System Requirements** column.

* - Host
  - System Requirements
  - Purpose

* - **1 & 2**

  -
    - Ops Manager Application

    - Ops Manager Application Database

  - Serves the primary and secondary for the Ops Manager Application database.

* - **3**, **4**, **5** & **6**

  -
    - Ops Manager Application

    - snapshot store

  - Serves the primary and secondary for the two snapshot stores.

    Only the Backup Daemon needs to communicate with the head
    databases. As such, their `net.bindIp` value is
    `127.0.0.1` to prevent external communication.
    `net.bindIp` specifies the IP address that
    mongod and mongos listens to for
    connections coming from applications.

* - **7** & **8**

  -

    - Ops Manager Application database

    - snapshot store

  - Serve the remaining replica set members for the Ops Manager Application
    Database and the two snapshot stores.

To learn how to install Ops Manager with high availability, see
/tutorial/configure-application-high-availability.
