<!-- Converted from tutorial/connect-to-mongodb.txt (reStructuredText). Includes are inlined. -->

# Connect to a MongoDB Process

## Overview

To connect to a MongoDB, retrieve the hostname and port information
from Ops Manager and then use a MongoDB client, such as `mongosh` or a
MongoDB client library, to connect. To
connect to a cluster, retrieve the hostname
and port for the mongos process. To connect to a
replica set or standalone process, retrieve 
the hostname and port for the mongod processes.

## Firewall Rules

Firewall rules and user authentication affect your access to MongoDB.
You must have access to the server and port of the MongoDB process.
For information on firewalls on servers running MongoDB, see
the firewall information in the Network Security document in the MongoDB manual.

If your MongoDB instance runs on Amazon Web Services (AWS), then the
security group associated with the AWS servers also affects access. AWS
security groups control inbound and outbound traffic to their
associated servers.

## Procedures

You can retrieve a shell command for connecting to your MongoDB
instance, or you can retrieve the host and port number of a specific
MongoDB process and create your own command for connecting using either
shell or
MongoDB client library.

### Get a Shell Command to Connect to a MongoDB Instance

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: On the line listing the cluster, replica set, or process, click the ellipsis icon and select Connect to this instance.**

Ops Manager provides a `mongo` command that you can use 
to connect to the MongoDB process.

### Get the Host and Port for a MongoDB Process

**Step 1: Navigate to the Clusters view for your deployment.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. If it is not already displayed, click Deployment in 
   the sidebar.

#. Click the Clusters view.

**Step 2: (Optional) For sharded clusters, filter which process type is listed.**

The four buttons are listed in the following order, left to right:
Shards, Configs, Mongos, and
BIs. 

| Process | Displays |
|---|---|
| Shards | mongod processes that host your data. |
| Configs | mongod processes that run as config servers to store a sharded cluster's metadata. |
| Mongos | mongos processes that route data in a sharded cluster. |
| BIs | BI (Business Intelligence) processes that access data in a sharded cluster. |

**Step 3: On the line listing the process, click Metrics.**

Ops Manager displays the hostname and port of the process at the top of the
charts page.

### Connect to a Deployment Using `mongosh`

Get the host and port using the previous procedure. From a shell, run `mongosh` and specify the
host and port. For example:

```sh
mongosh --username <user> --password <pass> --host <host> --port <port>
```

### Connect to a Deployment Using a MongoDB Client Library

Get the host and port using the above procedure.
See your client library's instructions for
creating a connection string that
specifies the hostname and port. 

For sharded clusters, you specify the hostname and port of the
mongos instance. For a replica set, you specify a seed list of
all hosts in the replica set. Your client library will automatically connect to
the primary. For example:

```javascript
mongodb://[<username>:<password>@]hostname0<:port>[,hostname1:<port1>][,hostname2:<port2>][...][,hostnameN:<portN>]
```

**See also:**

/data-explorer
