<!-- Converted from connect-to-cluster.txt (reStructuredText). Includes are inlined. -->

:orphan:

# Connect to a Cluster

Learn how to connect to MongoDB clusters whether they are hosted on
MongoDB Atlas or self-managed.

## Connection String Formats

To connect to your deployment, you need a connection string. The
connection string format depends on whether you connect to a replica
set, sharded cluster, or standalone deployment.

**Replica Set:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**Sharded Cluster:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**Standalone:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

If the username or password includes the following characters, those
characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1):

```none
$ : / ? # [ ] @
```

For detailed information about connection string formats and options,
see find-connection-string.

## Get Your Connection String

How you obtain your connection string depends on whether your
deployment is hosted on MongoDB Atlas or self-managed.

### MongoDB Atlas Deployments

To connect to a cluster hosted on MongoDB Atlas, see
atlas-connect-to-deployment, which covers how to:

- Get your connection string via the Atlas CLI or Atlas UI.
- Configure your IP access list.
- Create database users.
- Use various connection methods including drivers, Compass, `mongosh`, and more.

### Self-Managed Deployments

Before you connect to a self-managed deployment:

- Ensure your MongoDB deployment is running and accessible.
- Create a database user with the appropriate privileges.
- Verify network connectivity between your client and the MongoDB deployment.

To construct your connection string, use the appropriate
connection string format for your
deployment topology.

### Connection Methods

After you have your connection string, you can connect using the following
methods:

- connect-via-driver - MongoDB drivers for various programming languages
- atlas-connect-via-compass - MongoDB Compass GUI
- connect-mongo-shell - `mongosh`
- mongodb-for-vscode - MongoDB for VS Code
- Command Line Tools - mongodump, mongorestore, and other tools

## Learn More

- Connection String Formats
- Connection String Options
- test-failover
- connection-limits
