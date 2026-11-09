<!-- Converted from reference/method/rs.initiate.txt (reStructuredText). Includes are inlined. -->

# rs.initiate() (mongosh method)

## Description

**`rs.initiate(configuration)`**

Initiates a replica set. Optionally, the method can take an
argument in the form of a document that holds the
configuration of a replica set.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `replSetInitiate` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `rs.initiate()` method has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `configuration` | document | Optional. A document that specifies configuration for the new replica set. If a configuration is not specified, MongoDB uses a default replica set configuration. |

## Compatibility

This method is available in deployments hosted in the following environments:

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## IP Binding

**Warning:**

Before you bind your instance to a publicly-accessible IP address,
you must secure your cluster from unauthorized access. For a complete
list of security recommendations, see
security-checklist. At minimum, consider
enabling authentication and hardening
network infrastructure.

MongoDB binaries, `mongod` and `mongos`, bind
to localhost by default. If the `net.ipv6` configuration file
setting or the `--ipv6` command line option is set for the binary,
the binary additionally binds to the localhost IPv6 address.

By default `mongod` and `mongos` that are
bound to localhost only accept connections from clients that are
running on the same computer. This binding behavior includes
`mongosh` and other members of your replica set or sharded
cluster. Remote clients cannot connect to binaries that are bound only
to localhost.

To override the default binding and bind to other IP addresses, use the
`net.bindIp` configuration file setting or the `--bind_ip`
command-line option to specify a list of hostnames or IP addresses.

**Warning:**

Starting in MongDB 5.0, [split horizon DNS](https://en.wikipedia.org/wiki/Split-horizon_DNS) nodes that are
only configured with an IP address fail startup validation and
report an error. See `disableSplitHorizonIPCheck`.

For example, the following `mongod` instance binds to both
the localhost and the hostname `My-Example-Associated-Hostname`, which is
associated with the IP address `198.51.100.1`:

```none
mongod --bind_ip localhost,My-Example-Associated-Hostname
```

In order to connect to this instance, remote clients must specify
the hostname  or its associated IP address `198.51.100.1`:

```none
mongosh --host My-Example-Associated-Hostname

mongosh --host 198.51.100.1
```

## Replica Set Configuration

See replica-set-configuration-document for details of the
replica set configuration document.

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

## Example

The following example initiates a new replica set with three members.

The three `mongod` instances must have started with the
`--replSet` command line option (or
`replication.replSetName` if using a configuration file) set
to `myReplSet` and the `--bind_ip` (or `net.bindIp`
if using a configuration file) set appropriately such that other
members of the replica set and clients can connect.

**Warning:**

Before you bind your instance to a publicly-accessible IP address,
you must secure your cluster from unauthorized access. For a complete
list of security recommendations, see
security-checklist. At minimum, consider
enabling authentication and hardening
network infrastructure.

Connect `mongosh` to one of the `mongod`
instances and run `rs.initiate()`.

**Note:**

Run `rs.initiate()` on *just one and only one*
`mongod` instance for the replica set.

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

```javascript
rs.initiate(
   {
      _id: "myReplSet",
      version: 1,
      members: [
         { _id: 0, host : "mongodb0.example.net:27017" },
         { _id: 1, host : "mongodb1.example.net:27017" },
         { _id: 2, host : "mongodb2.example.net:27017" }
      ]
   }
)
```

For details on replica set configuration, see
replSetGetConfig-output.

For details on deploying a replica set, see
/tutorial/deploy-replica-set.

**See also:**

/administration/replica-set-member-configuration
