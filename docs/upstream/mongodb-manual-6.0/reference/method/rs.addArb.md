<!-- Converted from reference/method/rs.addArb.txt (reStructuredText). Includes are inlined. -->

# rs.addArb()

## Description

**`rs.addArb(host)`**

Adds a new arbiter to an existing replica set.

`rs.add(<host>, true)` is functionally the same as 
`rs.addArb(<host>)`. You can use these commands interchangeably.

**Warning:**

Avoid deploying more than one arbiter in a replica
set. See rollbacks-multi-arbiters.

To add an arbiter to an existing replica set:

- Typically, if there are two or fewer data-bearing members in the
  replica set, you might need to first set the cluster wide write
  concern for the replica set.

- See cluster wide write concern for more information on why you
  might need to set the cluster wide write concern.

You do not need to change the cluster wide write concern before starting
a new replica set with an arbiter.

**See also:**

Default write concern formula

The `rs.addArb()` method takes the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `host` | string | Specifies the hostname and optionally the port number of the arbiter member to add to replica set. |

## Compatibility

This method is available in deployments hosted in the following environments:

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## IP Binding

**Warning:**

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

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

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.
