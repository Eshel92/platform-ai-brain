<!-- Converted from reference/connection-string.txt (reStructuredText). Includes are inlined. -->

# Connection Strings

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the following examples.

----------

You can use connection strings to define connections between
MongoDB instances and the following destinations:

- Your applications when you connect using `drivers`.
- Tools such as `MongoDB Compass` and 
  `the MongoDB Shell (mongosh)`.

## Compatibility

You can use connection strings to connect to deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

Complete these steps to find your connection string.

## Find Your MongoDB Atlas Connection String

**atlas-cli:**

To find your MongoDB Atlas connection string using the
`Atlas CLI`, `install` and `connect` from the Atlas CLI, then run the following
command. Replace `<clusterName>` with the name of the MongoDB Atlas
cluster and replace `<projectId>` with the project ID.

```
atlas clusters connectionStrings describe <clusterName> --projectId <projectId>
```

To learn more, see `atlas clusters connectionStrings describe`.

**atlas-ui:**

To find your MongoDB Atlas connection string in the Atlas UI,
follow these steps:

**Step 1: In the MongoDB Atlas UI, go to the Clusters page for your project.**

**Warning:** Navigation Improvements In Progress

We're currently rolling out a new and improved navigation 
experience. If the following steps don't match your view in the 
Atlas UI, see `the preview Atlas documentation`.

a. If it's not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it's not already displayed, select your project
   from the Projects menu in the navigation bar.

#. If it's not already displayed, click Clusters in the 
   sidebar.

   The [Clusters](https://cloud.mongodb.com/go?l=https%3A%2F%2Fcloud.mongodb.com%2Fv2%2F%3Cproject%3E%23%2Fclusters) page displays.

**Step 2: Open the Connection Method dialog.**

a. Click Connect for the cluster to which
   you want to connect.
#. Click Choose a Connection Method. MongoDB Atlas
   selects Standard Connection by default. To
   connect using a private endpoint, select 
   Private Endpoint.

**Step 3: Choose a connection method.**

To connect to your application, click Drivers. To
connect using tools, click the tool you want to use to access your
data.

**Step 4: Follow instructions for the connection method you selected.**

a. If you selected Drivers, select your driver and
   version. If you selected a tool, download the tool.
b. Select Connect To Cluster. 
c. Copy the connection string. Replace `<password>` and
   `<username>` in the connection string with the database
   user's credentials.

Your MongoDB Atlas connection string resembles the following 
example:

**shell:**

```bash
mongosh "mongodb+srv://cluster0.example.mongodb.net myFirstDatabase" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
```

**java-sync:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
```

**java-async:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
```

**nodejs:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
```

**php:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
```

**perl:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
```

**ruby:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
```

**scala:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/?retryWrites=true&w=majority
```

**compass:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/
```

**csharp:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/
```

**go:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/
```

**motor:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/
```

**rust:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@cluster0.example.mongodb.net/
```

## Find Your Self-Hosted Deployment's Connection String

If you are connected to your self-hosted MongoDB Enterprise or
MongoDB Community deployment, run `db.getMongo()` method to
return the connection string.

If you are not connected to your deployment, you can
determine your connection string based on the connection type you
want to use. See connections-dns-seedlist to learn the SRV
connection string syntax or
connections-standard-connection-string-format to learn the
standard connection string syntax.

Your self-hosted connection string resembles the following
examples:

**srv:**

**repl:**

The following replica set connection string includes these
elements:

- The `replicaSet` option
- The hostname(s) of the `mongod` instance(s) as
  listed in the replica set configuration
- It authenticates as user `myDatabaseUser` with the password
  `D1fficultP%40ssw0rd` to enforce access control

**shell:**

```bash
mongosh "mongodb+srv://mongodb0.example.com/?authSource=admin&replicaSet=myRepl" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**java-sync:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**java-async:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**nodejs:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**php:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**perl:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**ruby:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**scala:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**compass:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**csharp:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**go:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

**motor:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**rust:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin&replicaSet=myRepl
```

If the username or password includes the following characters, those
characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1):

```none
$ : / ? # [ ] @
```

**sharded:**

The following sharded cluster connection string includes the
these elements:

- The `mongos` hosts in the connection string
- It authenticates as user `myDatabaseUser` with the password
  `D1fficultP%40ssw0rd` to enforce access control

**shell:**

```bash
mongosh "mongodb+srv://mongos0.example.com/?authSource=admin" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**java-sync:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**java-async:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**nodejs:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**php:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**perl:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**ruby:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**scala:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**compass:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**csharp:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**go:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

**motor:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**rust:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com/?authSource=admin
```

If the username or password includes the following characters, those
characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1):

```none
$ : / ? # [ ] @
```

**standalone:**

The following standalone connection string authenticates as user `myDatabaseUser` with the password `D1fficultP%40ssw0rd` to enforce access control:

**shell:**

```bash
mongosh "mongodb+srv://mongodb0.example.com/?authSource=admin" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**java-sync:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**java-async:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**nodejs:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**php:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**perl:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**ruby:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**scala:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**compass:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**csharp:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**go:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

**motor:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**rust:**

```bash
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com/?authSource=admin
```

If the username or password includes the following characters, those
characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1):

```none
$ : / ? # [ ] @
```

**standard:**

**repl:**

The following replica set connection string includes these
elements:

- The `replicaSet` option
- The hostname(s) of the `mongod` instance(s) as
  listed in the replica set configuration
- A username and password to enforce access control:

**shell:**

```bash
mongosh "mongodb://mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**java-sync:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**java-async:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**nodejs:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**php:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**perl:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**ruby:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**scala:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**compass:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**csharp:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**go:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**motor:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

**rust:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?authSource=admin&replicaSet=myRepl
```

If the username or password includes the following characters, those
characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1):

```none
$ : / ? # [ ] @
```

**sharded:**

The following sharded cluster connection string includes the
these elements:

- The `mongos` hosts in the connection string
- A username and password to enforce access control

**shell:**

```bash
mongosh "mongodb://mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**java-sync:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**java-async:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**nodejs:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**php:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**perl:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**ruby:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**scala:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**compass:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**csharp:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**go:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**motor:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

**rust:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos0.example.com:27017,mongos1.example.com:27017,mongos2.example.com:27017/?authSource=admin
```

If the username or password includes the following characters, those
characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1):

```none
$ : / ? # [ ] @
```

**standalone:**

The following standalone connection string enforces access
control:

**shell:**

```bash
mongosh "mongodb://@mongodb0.example.com:27017/?authSource=admin" --apiVersion 1 --username myDatabaseUser
```

**python:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**java-sync:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**java-async:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**nodejs:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**php:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**perl:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**ruby:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**scala:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**compass:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**csharp:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**go:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**motor:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

**rust:**

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
```

If the username or password includes the following characters, those
characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1):

```none
$ : / ? # [ ] @
```

For a full list of connection string options, see connections-dns-seedlist or
connections-standard-connection-string-format. For more
examples, see connections-connection-examples.

## Connection String Formats

You can specify the MongoDB connection string by using one
of the following formats:

- connections-dns-seedlist: A connection string with a hostname
  that corresponds to a DNS SRV record. Your driver or
  `mongosh` queries the record to determine which hosts
  are running the `mongod` or `mongos`
  instances.

- connections-standard-connection-string-format: A connection
  string that specifies all hosts that are running the 
  `mongod` or `mongos` instances.

MongoDB Atlas clusters use SRV connection format unless you connect to an 
online archive.

To connect directly to a host and port specified in a connection string,
set the `directConnection` option to `true`. For full
details about `directConnection` and the other connection string
options, see connections-connection-options. 

### SRV Connection Format

MongoDB supports a
DNS (Domain Name Service)-constructed seed list. Using 
DNS to construct the available servers list allows more flexibility of
deployment and the ability to change the servers in rotation without
reconfiguring clients.

The SRV URI connection scheme has the following form:

```none
mongodb+srv://[username:password@]host[/[defaultauthdb][?options]]
```

For more examples, see connections-connection-examples.

#### Connection String Components

A connection string includes the following components:

* - Component
  - Description

* - `mongodb://` or `mongodb+srv://`

  - A required prefix to identify that this is a string in the
    standard connection format (`mongodb://`) or SRV connection
    format (`mongodb+srv://`). To learn more about each format,
    see connections-standard-connection-string-format
    and connections-dns-seedlist.

* - `username:password@`

  - Optional. Authentication credentials. 

    If specified, the client will attempt to authenticate the
    user to the `authSource`. If
    `authSource` is unspecified, the client will
    attempt to authenticate the user to the `defaultauthdb`.
    And if the `defaultauthdb` is unspecified, to the `admin`
    database.

    If the username or password includes the following characters, those
    characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1):

    ```none
    $ : / ? # [ ] @
    ```

    See also `authSource`.

* - `host[:port]`

  - The host (and optional port number) where the
    `mongod` instance (or `mongos`
    instance for a sharded cluster) is running. You can specify a
    hostname, IP address, or UNIX domain socket. Specify as many
    hosts as appropriate for your deployment topology:

    - For a standalone, specify the hostname of the standalone
      `mongod` instance.

    - .. include:: /includes/fact-uri-rs-hostnames.rst

    - For a sharded cluster, specify the hostname(s) of the
      `mongos` instance(s).

    If the port number is not specified, the default port `27017`
    is used.

    If you use the SRV URI connection format, you can specify only one 
    host and no port. Otherwise, the driver or `mongosh` 
    raises a parse error and does not perform DNS resolution.

* - `/defaultauthdb`

  - Optional. The authentication database to use if the
    connection string includes `username:password@`
    authentication credentials but the `authSource` option
    is unspecified.

    If both `authSource` and `defaultauthdb` are
    unspecified, the client will attempt to authenticate the
    specified user to the `admin` database. For more information, 
    see `authSource`.

    IMPORTANT: For Atlas deployments using the connections-dns-seedlist, 
    `authSource` is automatically set to `admin` in the `TXT` DNS  
    record. For more information about connecting to Atlas deployments, 
    see atlas-connect-to-deployment.

* - `?<options>`

  - Optional. A query string that specifies connection specific
    options as `<name>=<value>` pairs. See
    connections-connection-options for a full description of
    these options.

    If the connection string does not specify a database/ you must
    specify a slash (`/`) between the last `host` and the
    question mark (`?`) that begins the string of options.

In order to leverage the DNS seed list, use the same syntax as a standard connection string with a prefix of
`mongodb+srv` rather than the standard `mongodb`. The `+srv`
indicates to the client that the hostname that follows corresponds to a
DNS SRV record. The driver or `mongosh` will then
query the DNS for the record to determine which hosts are running the
`mongod` or `mongos` instances.

**Note:**

Use of the `+srv` connection string modifier
automatically sets the `tls` (or the equivalent
`ssl`) option to `true` for the connection. You can
override this behavior by explicitly setting the `tls`
(or the equivalent `ssl`) option to `false` with
`tls=false` (or `ssl=false`) in the query string.

When using the `+srv` format, you must specify the `hostname`, 
`domain`, and `top-level domain (TLD)` in the following format: 
`<hostname>.<domain>.<TLD>.` This table shows how the placeholders
correspond to example values:

| Placeholder | Example |
|---|---|
| `<hostname>` | `server` |
| `<domain>` | `example` |
| `<TLD>` | `com` |
| `<hostname>.<domain>.<TLD>` | `server.example.com` |

This example shows a DNS seed list connection string that 
correctly uses the `<hostname>.<domain>.<TLD>` format. It
authenticates as user `myDatabaseUser` with the password
`D1fficultP%40ssw0rd`:

```none
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@server.example.com/
```

The corresponding DNS configuration resembles:

```none
Record                            TTL   Class    Priority Weight Port  Target
_mongodb._tcp.server.example.com. 86400 IN SRV   0        5      27317 mongodb1.example.com.
_mongodb._tcp.server.example.com. 86400 IN SRV   0        5      27017 mongodb2.example.com.
```

Individual SRV records must be in 
`_mongodb._tcp.<hostname>.<domain>.<TLD>` format.

When a client connects to a member of the seed list, the client 
retrieves a list of replica set members it can connect to. Clients 
often use DNS aliases in their seed lists which means the host may
return a server list that differs from the original seed list. If this
happens, clients will use the hostnames provided by the replica set 
rather than the hostnames listed in the seed list to ensure that 
replica set members can be reached via the hostnames in the resulting
replica set config. 

**Important:**

The hostnames returned in SRV records must share the same parent
domain (in this example, `example.com`) as the given hostname. If
the parent domains and hostname do not match, you will not be able to
connect.

This example shows a DNS seed list connection string that is missing
the `<hostname>`. This is incorrect and raises an error. 

```none
# This connection string is missing the <hostname> and raises a connection error

mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@example.com/       
```

Like the standard connection string, the DNS seed list connection string
supports specifying options as a query string. With a DNS seed list
connection string, you can *also* specify the following options via a
TXT record:

- `replicaSet`
- `authSource`

You may only specify one TXT record per `mongod` instance.
If multiple TXT records appear in the DNS and/or if the TXT
record contains an option other than `replicaSet` or `authSource`,
the client will return an error.

The TXT record for the `server.example.com` DNS entry would resemble:

```none
Record              TTL   Class    Text
server.example.com. 86400 IN TXT   "replicaSet=mySet&authSource=authDB"
```

Taken together, the DNS SRV records and the options specified in the TXT
record resolve to the following standard format connection string:

```none
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb1.example.com:27317,mongodb2.example.com:27017/?replicaSet=mySet&authSource=authDB
```

You can override the options specified in a TXT record by passing the option
in the query string. In the following example, the query string has provided
an override for the `authSource` option configured in the TXT record
of the DNS entry above.

```none
mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@server.example.com/?connectTimeoutMS=300000&authSource=aDifferentAuthDB
```

Given the override for the `authSource`, the equivalent connection
string in the standard format would be:

```none
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb1.example.com:27317,mongodb2.example.com:27017/?connectTimeoutMS=300000&replicaSet=mySet&authSource=aDifferentAuthDB
```

**Note:**

The `mongodb+srv` option fails if there is no available DNS
with records that correspond to the hostname identified in the
connection string. If you use the `+srv` connection string modifier,
the `tls` (or the equivalent `ssl`) option is 
set to `true` for the connection. You can override this behavior by 
explicitly setting the `tls` 
(or the equivalent `ssl`) option to `false` with
`tls=false` (or `ssl=false`) in the query string.

For an example that connects `mongosh` to a replica set using 
the DNS seed list connection format, see mongosh Connection Options.

### Standard Connection String Format

This section describes the standard format of the MongoDB connection
URI used to connect to a self-hosted MongoDB standalone deployment,
replica set, or sharded cluster.

The standard URI connection scheme has the form:

```none
mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]
```

For more examples, see connections-connection-examples.

#### Connection String Database Options

You can specify a default database in the `[/defaultauthdb]` field of the 
connection string. The client uses the specified `[/defaultauthdb]` database 
as the default database. If unspecified by the connection string, the 
default database is the `test` database.

You can specify the authentication database in your connection string
using the `authSource` connection option. If specified, the
client uses this database to verify your user identity and credentials.
If `authSource` is unspecified, it defaults to the 
`[/defaultauthdb]` database. If both `authSource` and 
`[/defaultauthdb]` are unspecified, `authSource` 
defaults to the `admin` database.

The following connection string sets the default database to `myDefaultDB`
and the authentication database to `admin`:

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017/myDefaultDB?authSource=admin
```

#### Connection String Components

A connection string includes the following components:

* - Component
  - Description

* - `mongodb://` or `mongodb+srv://`

  - A required prefix to identify that this is a string in the
    standard connection format (`mongodb://`) or SRV connection
    format (`mongodb+srv://`). To learn more about each format,
    see connections-standard-connection-string-format
    and connections-dns-seedlist.

* - `username:password@`

  - Optional. Authentication credentials. 

    If specified, the client will attempt to authenticate the
    user to the `authSource`. If
    `authSource` is unspecified, the client will
    attempt to authenticate the user to the `defaultauthdb`.
    And if the `defaultauthdb` is unspecified, to the `admin`
    database.

    If the username or password includes the following characters, those
    characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1):

    ```none
    $ : / ? # [ ] @
    ```

    See also `authSource`.

* - `host[:port]`

  - The host (and optional port number) where the
    `mongod` instance (or `mongos`
    instance for a sharded cluster) is running. You can specify a
    hostname, IP address, or UNIX domain socket. Specify as many
    hosts as appropriate for your deployment topology:

    - For a standalone, specify the hostname of the standalone
      `mongod` instance.

    - .. include:: /includes/fact-uri-rs-hostnames.rst

    - For a sharded cluster, specify the hostname(s) of the
      `mongos` instance(s).

    If the port number is not specified, the default port `27017`
    is used.

    If you use the SRV URI connection format, you can specify only one 
    host and no port. Otherwise, the driver or `mongosh` 
    raises a parse error and does not perform DNS resolution.

* - `/defaultauthdb`

  - Optional. The authentication database to use if the
    connection string includes `username:password@`
    authentication credentials but the `authSource` option
    is unspecified.

    If both `authSource` and `defaultauthdb` are
    unspecified, the client will attempt to authenticate the
    specified user to the `admin` database. For more information, 
    see `authSource`.

    IMPORTANT: For Atlas deployments using the connections-dns-seedlist, 
    `authSource` is automatically set to `admin` in the `TXT` DNS  
    record. For more information about connecting to Atlas deployments, 
    see atlas-connect-to-deployment.

* - `?<options>`

  - Optional. A query string that specifies connection specific
    options as `<name>=<value>` pairs. See
    connections-connection-options for a full description of
    these options.

    If the connection string does not specify a database/ you must
    specify a slash (`/`) between the last `host` and the
    question mark (`?`) that begins the string of options.
