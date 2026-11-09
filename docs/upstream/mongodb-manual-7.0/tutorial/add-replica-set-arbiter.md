<!-- Converted from tutorial/add-replica-set-arbiter.txt (reStructuredText). Includes are inlined. -->

# Add an Arbiter to a Self-Managed Replica Set

In some circumstances (such as you have a primary and a secondary but
cost constraints prohibit adding another secondary), you may choose to
add a `mongod` instance to a replica set as an
arbiter to vote in elections.

Arbiters are `mongod` instances that are part of a
replica set but do not hold data (i.e. do not provide data
redundancy). They can, however, participate in elections.

Arbiters have minimal resource requirements and do not require
dedicated hardware. You can deploy an arbiter on an application
server or a monitoring host.

**Important:**

Do not run an arbiter on systems that also host the
primary or the secondary members of the replica set.

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

## Considerations

Arbiters are not supported with
quarterly rapid releases. If
your deployment includes arbiters, only use
LTS (Long Term Support) releases.

## Primary-Secondary-Arbiter Replica Sets

If you are using a three-member primary-secondary-arbiter (PSA) 
architecture, consider the following:

- The write concern `"majority"` can cause
  performance issues if a secondary is unavailable or lagging. For 
  advice on how to mitigate these issues, see 
  performance-issues-psa.

- If you are using a global default `"majority"` 
  and the write concern is less than the size of the majority,
  your queries may return stale (not fully replicated) data.

### Arbiter

An arbiter does not store data, but until the arbiter's `mongod`
process is added to the replica set, the arbiter will act like any other
`mongod` process and start up with a set of data files and with a
full-sized journal.

### IP Binding

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

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

## Add an Arbiter

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

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

#. Create a data directory (e.g. `storage.dbPath`) for the
   arbiter. The `mongod` instance uses the directory for
   configuration data. The directory *will not* hold the data set. For
   example, create the `/var/lib/mongodb/arb` directory:

   ```bash
   mkdir /var/lib/mongodb/arb
   ```

#. Start the arbiter, specifying the data directory and the name of the replica set
   to join. The following starts an arbiter using the `/var/lib/mongodb/arb`
   as the `dbPath` and  `rs` for the replica set name:

   **Warning:**

   Before you bind your instance to a publicly-accessible IP address,
   you must secure your cluster from unauthorized access. For a complete
   list of security recommendations, see
   security-checklist. At minimum, consider
   enabling authentication and hardening
   network infrastructure.

   ```bash
   mongod --port 27017 --dbpath /var/lib/mongodb/arb --replSet rs --bind_ip localhost,<hostname(s)|ip address(es)>
   ```

#. Connect to the primary and add the arbiter to the replica set. Use
   the `rs.addArb()` method, as in the following example which
   assumes that `m1.example.net` is the hostname associated with the
   specified ip address for the arbiter:

   ```javascript
   rs.addArb("m1.example.net:27017")
   ```

   This operation adds the arbiter running on port `27017` on the
   `m1.example.net` host.
