<!-- Converted from reference/method/rs.add.txt (reStructuredText). Includes are inlined. -->

# rs.add() (mongosh method)

## Definition

**`rs.add(host, arbiterOnly)`**

Adds a member to a replica set. To run the method, you must
connect to the primary of the replica set.

* - Parameter

  - Type

  - Description

* - `host`

  - string or document

  - The new member to add to the replica set. Specify either as a string
    or a configuration document:

    - If a document, specify a replica set member configuration document
      as found in the `members` array. You must specify the
      `host` field in the member configuration
      document.

      ```javascript
       {
         _id: <int>,
         host: <string>,        // required
         arbiterOnly: <boolean>,
         buildIndexes: <boolean>,
         hidden: <boolean>,
         priority: <number>,
         tags: <document>,
         secondaryDelaySecs: <int>,
         votes: <number>
      }
      ```

      For a description of the configuration field, refer to
      `members`.

    - If a string, specify the hostname and optionally the port number
      for the new member.

* - `arbiterOnly`

  - boolean

  - Optional. Applies only if the `<host>` value is a string. If `true`, the
    added host is an arbiter.

`rs.add()` provides a wrapper around some of the
functionality of the `replSetReconfig` database
command and the corresponding `mongosh` helper
`rs.reconfig()`. See the
/reference/replica-configuration document for full
documentation of all replica set configuration options.

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

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

## Behavior

`rs.add()` can, in some cases, trigger an election for primary
which will disconnect the shell (such as adding a new member with
a higher priority than the current primary). In such cases,
`mongosh` may display an error even if the operation
succeeds.

**Warning:**

Before MongoDB 5.0, a newly added secondary still counts as a voting
member even though it can neither serve reads nor become primary until
its data is consistent. If you are running a MongoDB version earlier
than 5.0 and add a secondary with its `votes`
and `priority` settings greater than zero, this can
lead to a case where a majority of the voting members are
online but no primary can be elected. To avoid such situations,
consider adding the new secondary initially with
`priority :0` and `votes :0`. Then, run `rs.status()` to ensure the
member has transitioned into `SECONDARY` state. Finally, use
`rs.reconfig()` to update its priority and votes.

## Example

### Add a Secondary to a New Replica Set

To add a new secondary member with default vote and priority settings
to a new replica set, you can call the `rs.add()` method with:

- Member Configuration Document

  ```javascript
  rs.add( { host: "mongodbd4.example.net:27017" } )
  ```

- Host name

  ```javascript
  rs.add( "mongodbd4.example.net:27017" )
  ```

### Add a Secondary to an Existing Replica Set

Add a new secondary member with default vote and priority settings
to an existing replica set:

```javascript
rs.add( { host: "mongodbd4.example.net:27017" } )
```

**Warning:**

Before MongoDB 5.0, a newly added secondary still counts as a voting
member even though it can neither serve reads nor become primary until
its data is consistent. If you are running a MongoDB version earlier
than 5.0 and add a secondary with its `votes`
and `priority` settings greater than zero, this can
lead to a case where a majority of the voting members are
online but no primary can be elected. To avoid such situations,
consider adding the new secondary initially with
`priority :0` and `votes :0`. Then, run `rs.status()` to ensure the
member has transitioned into `SECONDARY` state. Finally, use
`rs.reconfig()` to update its priority and votes.

### Add a Priority 0 Member to a Replica Set

The following operation adds a `mongod` instance, running on
the host `mongodb4.example.net` and accessible on the default port
`27017`, as a priority 0
secondary member:

```javascript
rs.add( { host: "mongodbd4.example.net:27017", priority: 0 } )
```

You must specify the `members[n].host` field in the member
configuration document.

See the `members` for the available replica set member
configuration settings.

### Add an Arbiter to a Replica Set

The following operation adds a `mongod` instance, running on
the host `mongodb3.example.net` and accessible on the default port
`27017` as an arbiter:

- Member Configuration Document

  ```javascript
  rs.add( { host: "mongodb3.example.net:27017", arbiterOnly: true } )
  ```

- Host name

  ```javascript
  rs.add("mongodb3.example.net:27017", true)
  ```

See also:

- /tutorial/expand-replica-set
- /tutorial/add-replica-set-arbiter
- /tutorial/replace-replica-set-member
- /tutorial/remove-replica-set-member
