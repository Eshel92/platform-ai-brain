<!-- Converted from tutorial/assign-snapshot-stores-to-data-center.txt (reStructuredText). Includes are inlined. -->

# Assign Snapshot Stores to Specific Data Centers

## Overview

Additional Snapshot Stores can be added to meet storage requirements.
These additional stores can be deployed in the same data center as the
first store. There are times where these stores need to be deployed to
other data centers due to either network performance issues or
regulatory requirements.

You can bind specific Ops Manager `projects` to specific
snapshot stores and particular data centers. This assigns the backups
of particular MongoDB deployments to specific data centers.

**Note:**

You can bind only projects to specific snapshot stores or 
data centers. You cannot bind shards to a specific location.

(Figure: /images/dual-data-center-backup.bakedsvg.svg)

This tutorial sets up two snapshot stores, one in each of two separate
data centers, and attaches a separate project to each.

## Prerequisites

* Configure the two Ops Manager Application instances to share a single dedicated
  mms-application-database.

  * The members of the Ops Manager Application Database replica set can be put in
    each data center.

* Configure each Backup to use the URL for its local
  Ops Manager Application.

  * Each Ops Manager Application can use a different hostname or a split-horizon
    DNS to point each agent to its local Ops Manager Application.

**Note:**

The Ops Manager Application Database and the backup blockstore databases are
MongoDB databases and can run as standalones or
replica sets.

For production deployments, use replica sets to provide database
high availability.

## Procedures

### Provision Servers in Each Data Center

Each data center must host its own backup blockstore database
or File System Store, application and
MongoDB Agent with Backup.

Each server must meet the cumulative hardware and software requirements
for the components it runs. See /core/requirements.

All servers running Backup and Ops Manager Application Databases use MongoDB.
They must meet the configuration requirements in the MongoDB
Production Notes.

### Install MongoDB

Install MongoDB on the servers that host the:

- Ops Manager Application database
- Blockstore databases

See Install MongoDB in the MongoDB manual to
find the correct install procedure for your operating system.

To run replica sets for the Ops Manager Application database and blockstore
databases, see Deploy a Replica Set in the MongoDB manual.

### Install and Start the Ops Manager Application

Install the Ops Manager Application in each data center.

**Note:**

See /tutorial/nav/install-application for instructions for
your operating system.

**Important:**

Each set of installation instructions for each operating system
covers how to create a multiple instances of an Ops Manager Application. These
activities need to be completed before binding projects to the backup
resources.

### Bind Projects to Backup Resources

**Step 1: In a web browser, open Ops Manager.**

**Step 2: Create a new Ops Manager project for Data Center #1.**

a. Click on your user name in the upper-right hand corner and select My Projects.

#. Click Add Project.

#. Enter the project name.

#. Click Create Project.

**Step 3: Create a second Ops Manager project for the Data Center #2.**

**Step 4: Click the Admin link at the upper right of the page to open the Admin interface.**

**Step 5: Configure backup resources.**

a. Click the Backup tab.

b. Click the Daemons page and check that there are two
   daemons listed.

c. Click the Snapshot Storage page.

d. Create a
   file system store
   or a
   blockstore
   using network storage or a MongoDB database in Data Center #2.

e. Click Save.

f. Click the Oplog Storage page.

g. Add an oplog store using a MongoDB database in Data Center #2.

h. Click Save.

**Step 6: Assign resources to the data centers.**

a. Click the General tab.

b. Click the Projects page.

c. Select the name of the project assigned to Data Center 1.

d. Click the View link to the right of
   Backup Configuration.

e. Select the local options for Project 1 / Data Center 1.

   | Menu | Option |
   |---|---|
   | Backup Daemons | Choose Select Backup Daemons then check the daemon that is in Data Center 1. |
   | Oplog Stores | Choose Select Oplog Stores then check the oplog store that is in Data Center 1. |
   | Snapshot Stores | Choose Select Snapshot Stores then check the snapshot store that is in Data Center 1. |

f. Repeat steps a to e for Project 2.

**Step 7: Install agents.**

a. /tutorial/nav/install-mongodb-agent to the project
   assigned to Data Center 1.

#. As needed for the MongoDB Agent used with the Data Center 1
   project, activate:

   - Backup,
   - Monitoring,
   - Automation, or
   - any combination of these functions.

#. /tutorial/nav/install-mongodb-agent to the project
   assigned to Data Center 2.

#. As needed for the MongoDB Agent used with the Data Center 2
   project, activate:

   - Backup,
   - Monitoring,
   - Automation, or
   - any combination of these functions.
