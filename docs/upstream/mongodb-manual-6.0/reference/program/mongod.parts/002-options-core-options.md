<!-- Part 2 of 6 of reference/program/mongod.md (split because the page is big). -->

### Core Options

**`--help, -h`**

Returns information on the options and use of `mongod`.

**`--version`**

Returns the `mongod` release number.

**`--config <filename>, -f <filename>`**

Specifies a configuration file for runtime configuration options. The
configuration file is the preferred method for runtime configuration of
`mongod`. The options are equivalent to the command-line
configuration options. See /reference/configuration-options for
more information.

Ensure the configuration file uses ASCII encoding. The `mongod`
instance does not support configuration files with non-ASCII encoding,
including UTF-8.

**`--configExpand <none|rest|exec>`**

*Default*: none

Enables using Expansion Directives
in configuration files. Expansion directives allow you to set
externally sourced values for configuration file options. 

`--configExpand` supports the following expansion directives:

| Value | Description |
|---|---|
| `none` | Default. `mongod` does not expand expansion directives. `mongod` fails to start if any configuration file settings use expansion directives. |
| `rest` | `mongod` expands `__rest` expansion directives when parsing the configuration file. |
| `exec` | `mongod` expands `__exec` expansion directives when parsing the configuration file. |

You can specify multiple expansion directives as a comma-separated
list, for example: `rest, exec`. If the configuration file contains
expansion directives not specified to `--configExpand`, the `mongod`
returns an error and terminates.

See externally-sourced-values for configuration files
for more information on expansion directives.

**`--verbose, -v`**

Increases the amount of internal reporting returned on standard output
or in log files. Increase the verbosity with the `-v` form by
including the option multiple times, for example: `-vvvvv`.

**Note:**

Starting in version 4.2, MongoDB includes the Debug verbosity level
(1-5) in the log messages. For example,
if the verbosity level is 2, MongoDB logs `D2`. In previous
versions, MongoDB log messages only specified `D` for Debug level.

   

**`--quiet`**

Runs `mongod` in a quiet mode that attempts to limit the amount
of output.

This option suppresses:

- output from database commands

- replication activity

- connection accepted events

- connection closed events

**`--port <port>`**

*Default*:

- 27017 if `mongod` is not a shard member or a config server member
- 27018 if `mongod` is a `shard member`
- 27019 if `mongod` is a `config server member`

The TCP port on which the MongoDB instance listens for
client connections.

**Changed in version:** 6.0.12

The `--port` option accepts a range of values between `0` and `65535`.
Setting the port to `0` configures `mongod` to use an arbitrary
port assigned by the operating system.

   

**`--bind_ip <hostnames|ipaddresses|Unix domain socket paths>`**

*Default*: localhost

The hostnames and/or IP addresses and/or full Unix domain socket
paths on which `mongod` should listen for client connections. You
may attach `mongod` to any interface. To bind to multiple
addresses, enter a list of comma-separated values.

**Example:** `localhost,/tmp/mongod.sock`

You can specify both IPv4 and IPv6 addresses, or hostnames that
resolve to an IPv4 or IPv6 address.

**Example:** `localhost, 2001:0DB8:e132:ba26:0d5c:2774:e7f9:d513`

**Note:**

If specifying an IPv6 address *or* a hostname that resolves to an
IPv6 address to `--bind_ip`, you must start `mongod` with 
`--ipv6` to enable IPv6 support. Specifying an IPv6 address
to `--bind_ip` does not enable IPv6 support.

If specifying a 
[link-local IPv6 address](https://en.wikipedia.org/wiki/Link-local_address#IPv6)
(`fe80::/10`), you must append the 
[zone index](https://en.wikipedia.org/wiki/IPv6_address#Scoped_literal_IPv6_addresses_(with_zone_index))
to that address (i.e. `fe80::<address>%<adapter-name>`). 

**Example:** `localhost,fe80::a00:27ff:fee0:1fcf%enp0s3`

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

**Warning:**

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

For more information about IP Binding, refer to the
/core/security-mongodb-configuration documentation.

To bind to all IPv4 addresses, enter `0.0.0.0`.

To bind to all IPv4 and IPv6 addresses, enter `::,0.0.0.0` or
an asterisk `"*"` (enclose the asterisk in quotes to avoid filename 
pattern expansion). Alternatively, use the `net.bindIpAll` setting.

**Note:**

- `--bind_ip` and `--bind_ip_all` are mutually exclusive.
  Specifying both options causes `mongod` to throw an error and
  terminate.

- The command-line option `--bind` overrides the configuration
  file setting `net.bindIp`.

**`--bind_ip_all`**

If specified, the `mongod` instance binds to all IPv4
addresses (i.e. `0.0.0.0`). If `mongod` starts with
`--ipv6`, `--bind_ip_all` also binds to all IPv6 addresses
(i.e. `::`). 

`mongod` only supports IPv6 if started with `--ipv6`. Specifying
`--bind_ip_all` alone does not enable IPv6 support.

**Warning:**

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

For more information about IP Binding, refer to the
/core/security-mongodb-configuration documentation.

Alternatively, you can set the `--bind_ip` option to `::,0.0.0.0`
or to an asterisk `"*"` (enclose the asterisk in quotes to avoid filename
pattern expansion).

**Note:**

`--bind_ip` and `--bind_ip_all` are mutually exclusive. That
is, you can specify one or the other, but not both.

      

**`--clusterIpSourceAllowlist <string>`**

**New in version:** 5.0

A list of IP addresses/CIDR ([Classless Inter-Domain Routing](https://tools.ietf.org/html/rfc4632)) ranges against which the
`mongod` validates authentication requests from other members of
the replica set and, if part of a sharded cluster, the `mongos`
instances. The `mongod` verifies that the originating IP is
either explicitly in the list or belongs to a CIDR range in the list. If the
IP address is not present, the server does not authenticate the
`mongod` or `mongos`.

`--clusterIpSourceAllowlist` has no effect on a `mongod` started without
authentication.

`--clusterIpSourceAllowlist` accepts multiple comma-separated IPv4/6 addresses or Classless
Inter-Domain Routing ([CIDR](https://tools.ietf.org/html/rfc4632)) ranges:

```bash
mongod --clusterIpSourceAllowlist 192.0.2.0/24,127.0.0.1,::1
```

**Important:**

Ensure `--clusterIpSourceAllowlist` includes the IP address *or* CIDR ranges that include the
IP address of each replica set member or `mongos` in the
deployment to ensure healthy communication between cluster components.

**`--ipv6`**

Enables IPv6 support. `mongod` disables IPv6 support by default.

Setting `--ipv6` does *not* direct the `mongod` to listen on any
local IPv6 addresses or interfaces. To configure the `mongod` to
listen on an IPv6 interface, you must either:

- Configure `--bind_ip` with one or more IPv6 addresses or
  hostnames that resolve to IPv6 addresses, **or**
- Set `--bind_ip_all` to `true`.

**`--listenBacklog <number>`**

*Default*: Target system `SOMAXCONN` constant

The maximum number of connections that can exist in the listen
queue.

**Important:**

To prevent undefined behavior, specify a value for this
parameter between `1` and the local system `SOMAXCONN`
constant.

The default value for the `listenBacklog` parameter is set at
compile time to the target system `SOMAXCONN` constant.
`SOMAXCONN` is the maximum valid value that is documented for
the *backlog* parameter to the *listen* system call.

Some systems may interpret `SOMAXCONN` symbolically, and others
numerically. The actual *listen backlog* applied in practice may
differ from any numeric interpretation of the `SOMAXCONN` constant
or argument to `--listenBacklog`, and may also be constrained by
system settings like `net.core.somaxconn` on Linux.

Passing a value for the `listenBacklog` parameter that exceeds the
`SOMAXCONN` constant for the local system is, by the letter of the
standards, undefined behavior. Higher values may be silently integer
truncated, may be ignored, may cause unexpected resource
consumption, or have other adverse consequences.

On systems with workloads that exhibit connection spikes, for which
it is empirically known that the local system can honor higher
values for the *backlog* parameter than the `SOMAXCONN` constant,
setting the `listenBacklog` parameter to a higher value may reduce
operation latency as observed by the client by reducing the number
of connections which are forced into a backoff state.

**`--maxConns <number>`**

The maximum number of simultaneous connections that `mongod`
accepts. This setting has no effect if it is higher than your operating
system's configured maximum connection tracking threshold.

Do not assign too low of a value to this option, or you will
encounter errors during normal application operation.

**`--logpath <path>`**

Sends all diagnostic logging information to a log file instead of to
standard output or to the host's syslog system. MongoDB creates
the log file at the path you specify.

By default, MongoDB moves any existing log file rather than overwriting
it. To instead append to the log file, set the `--logappend` option.
   

**`--syslog`**

Sends all logging output to the host's syslog system rather
than to standard output or to a log file (`--logpath`).

The `--syslog` option is not supported on Windows.

**Warning:**

The `syslog` daemon generates timestamps when it logs a message, not
when MongoDB issues the message. This can lead to misleading timestamps
for log entries, especially when the system is under heavy load. We
recommend using the `--logpath` option for production systems to
ensure accurate timestamps.

MongoDB includes the component in its log 
messages to `syslog`.

```none
...  ACCESS   [repl writer worker 5] Unsupported modification to roles collection ...
```

**`--syslogFacility <string>`**

*Default*: user

Specifies the facility level used when logging messages to syslog.
The value you specify must be supported by your
operating system's implementation of syslog. To use this option, you
must  enable the `--syslog` option.

**`--logappend`**

Appends new entries to the end of the existing log file when the `mongod`
instance restarts. Without this option, `mongod` backs up the
existing log and create a new file.

**`--logRotate <string>`**

*Default*: rename

Determines the behavior for the `logRotate` command when
rotating the server log and/or the audit log. Specify either
`rename` or `reopen`:

- `rename` renames the log file.

- `reopen` closes and reopens the log file following the typical
  Linux/Unix log rotate behavior. Use `reopen` when using the
  Linux/Unix logrotate utility to avoid log loss.

  If you specify `reopen`, you must also use `--logappend`.

**`--timeStampFormat <string>`**

*Default*: iso8601-local

The time format for timestamps in log messages. Specify one of the
following values:

| Value | Description |
|---|---|
| `iso8601-utc` | Displays timestamps in Coordinated Universal Time (UTC) in the ISO-8601 format. For example, for New York at the start of the Epoch: `1970-01-01T00:00:00.000Z` |
| `iso8601-local` | Displays timestamps in local time in the ISO-8601 format. For example, for New York at the start of the Epoch: `1969-12-31T19:00:00.000-05:00` |

**Note:**

`--timeStampFormat` no longer supports `ctime`. An example of `ctime` 
formatted date is: `Wed Dec 31 18:17:54.811`.

**`--traceExceptions`**

For internal diagnostic use only.

   

**`--pidfilepath <path>`**

Specifies a file location to store the process ID (PID) of the `mongod`
process. The user running the `mongod` or `mongos`
process must be able to write to this path. If the `--pidfilepath` option is not
specified, the process does not create a PID file. This option is generally
only useful in combination with the `--fork` option.

**Note:** Linux

On Linux, PID file management is generally the responsibility of
your distro's init system: usually a service file in the `/etc/init.d`
directory, or a systemd unit file registered with `systemctl`. Only
use the `--pidfilepath` option if you are not using one of these init
systems. For more information, please see the respective
Installation Guide for your operating system.

**Note:** macOS

On macOS, PID file management is generally handled by `brew`. Only use
the `--pidfilepath` option if you are not using `brew` on your macOS system. 
For more information, please see the respective
Installation Guide for your operating system.

**`--keyFile <file>`**

Specifies the path to a key file that stores the shared secret
that MongoDB instances use to authenticate to each other in a
sharded cluster or replica set. `--keyFile` implies
`--auth`. See inter-process-auth for more
information.

Keyfiles for internal membership authentication use YAML format to allow for multiple keys in a 
keyfile. The YAML format accepts either:

- A single key string (same as in earlier versions)

- A sequence of key strings

The YAML format is compatible with the existing single-key
keyfiles that use the text file format.

**`--setParameter <options>`**

Specifies one of the MongoDB parameters described in
/reference/parameters. You can specify multiple `setParameter`
fields.
   

**`--nounixsocket`**

Disables listening on the UNIX domain socket. `--nounixsocket` applies only
to Unix-based systems.

The `mongod` process
always listens on the UNIX socket unless one of the following is true:

- `--nounixsocket` is set

- `net.bindIp` is not set

- `net.bindIp` does not specify `localhost` or its associated IP address

`mongod` installed from official install-mdb-community-debian 
and install-mdb-community-redhat-centos packages
have the `bind_ip` configuration set to `127.0.0.1` by
default.

**`--unixSocketPrefix <path>`**

*Default*: /tmp

The path for the UNIX socket. `--unixSocketPrefix` applies only
to Unix-based systems.

If this option has no value, the
`mongod` process creates a socket with `/tmp` as a prefix. MongoDB
creates and listens on a UNIX socket unless one of the following is true:

- `net.unixDomainSocket.enabled` is `false`

- `--nounixsocket` is set

- `net.bindIp` is not set

- `net.bindIp` does not specify `localhost` or its associated IP address

**`--filePermissions <path>`**

*Default*: `0700`

Sets the permission for the UNIX domain socket file.

`--filePermissions` applies only to Unix-based systems.

**`--fork`**

Enables a daemon mode that runs the `mongod` process in the
background. The `--fork` option is not supported on Windows.

By default `mongod` does not run as a daemon. You run `mongod` as
a daemon by using either `--fork` or a controlling process
that handles daemonization, such as `upstart` or `systemd`.

To use `--fork`, configure log output for the `mongod` with one of the following:

- `--logpath`
- `--syslog`

**`--auth`**

Enables authorization to control user's access to database resources
and operations. When authorization is enabled, MongoDB requires all
clients to authenticate themselves first in order to determine the
access for the client.

To configure users, use the `mongosh` client. If no users 
exist, the localhost interface has access to the 
database until you create the first user.

See Security for more information.
   

**`--noauth`**

Disables authentication. Currently the default. Exists for future
compatibility and clarity.
   

**`--transitionToAuth`**

Allows the `mongod` to accept and create authenticated and
non-authenticated connections to and from other `mongod`
and `mongos` instances in the deployment. Used for
performing rolling transition of replica sets or sharded clusters
from a no-auth configuration to internal authentication. Requires specifying a internal
authentication mechanism such as
`--keyFile`.

For example, if using keyfiles for
internal authentication, the `mongod` creates
an authenticated connection with any `mongod` or `mongos`
in the deployment using a matching keyfile. If the security mechanisms do
not match, the `mongod` utilizes a non-authenticated connection instead.

A `mongod` running with `--transitionToAuth` does not enforce user access
controls. Users may connect to your deployment without any
access control checks and perform read, write, and administrative operations.

**Note:**

A `mongod` running with internal authentication and *without* `--transitionToAuth` requires clients to connect
using user access controls. Update clients to
connect to the `mongod` using the appropriate user
prior to restarting `mongod` without `--transitionToAuth`.

**`--sysinfo`**

Returns diagnostic system information and then exits. The
information provides the page size, the number of physical pages,
and the number of available physical pages.
   

**`--noscripting`**

Disables the scripting engine.
   

**`--notablescan`**

Forbids operations that require a collection scan. See `notablescan` for additional information.
   

**`--shutdown`**

The `--shutdown` option cleanly and safely terminates the `mongod`
process. When invoking `mongod` with this option you must set the
`--dbpath` option either directly or by way of the
configuration file and the
`--config` option.

The `--shutdown` option is available only on Linux systems.

For additional ways to shut down, see also terminate-mongod-processes.
   

**`--redactClientLogData`**

*Available in MongoDB Enterprise only.*

A `mongod` running with `--redactClientLogData` redacts any message accompanying a given
log event before logging. This prevents the `mongod` from writing
potentially sensitive data stored on the database to the diagnostic log.
Metadata such as error or operation codes, line numbers, and source file
names are still visible in the logs.

Use `--redactClientLogData` in conjunction with
/core/security-encryption-at-rest and
/core/security-transport-encryption to assist compliance with
regulatory requirements.

For example, a MongoDB deployment might store Personally Identifiable
Information (PII) in one or more collections. The `mongod` logs events
such as those related to CRUD operations, sharding metadata, etc. It is
possible that the `mongod` may expose PII as a part of these logging
operations. A `mongod` running with `--redactClientLogData` removes any message
accompanying these events before being output to the log, effectively
removing the PII.

Diagnostics on a `mongod` running with `--redactClientLogData` may be more difficult
due to the lack of data related to a log event. See the
process logging manual page for an
example of the effect of `--redactClientLogData` on log output.

On a running `mongod`, use `setParameter` with the
`redactClientLogData` parameter to configure this setting.

**`--networkMessageCompressors <string>`**

*Default*: snappy,zstd,zlib

Specifies the default compressor(s) to use for
communication between this `mongod` instance and:

- other members of the deployment if the instance is part of a replica set or a sharded cluster

- `mongosh`

- drivers that support the `OP_COMPRESSED` message format.

MongoDB supports the following compressors:

- snappy

- zlib

- zstd

**Note:**

Both `mongod` and `mongos` instances default to 
`snappy,zstd,zlib` compressors, in that order.

To disable network compression, set the value to `disabled`.

**Important:**

Messages are compressed when both parties enable network
compression. Otherwise, messages between the parties are
uncompressed.

If you specify multiple compressors, then the order in which you list
the compressors matter as well as the communication initiator. For
example, if `mongosh` specifies the following network
compressors `zlib,snappy` and the `mongod` specifies
`snappy,zlib`, messages between `mongosh` and
`mongod` uses `zlib`.

If the parties do not share at least one common compressor, messages
between the parties are uncompressed. For example, if
`mongosh` specifies the network compressor
`zlib` and `mongod` specifies `snappy`, messages
between `mongosh` and `mongod` are not
compressed.

**`--timeZoneInfo <path>`**

The full path from which to load the time zone database. If this option
is not provided, then MongoDB uses its built-in time zone database.

The configuration file included with Linux and macOS packages sets the
time zone database path to `/usr/share/zoneinfo` by default.

The built-in time zone database is a copy of the [Olson/IANA time zone database](https://www.iana.org/time-zones). It is updated along with
MongoDB releases, but the time zone database release cycle
differs from the MongoDB release cycle. The most recent release of
the time zone database is available on our [download site](https://downloads.mongodb.org/olson_tz_db/timezonedb-latest.zip).

```bash
wget https://downloads.mongodb.org/olson_tz_db/timezonedb-latest.zip
unzip timezonedb-latest.zip
mongod --timeZoneInfo timezonedb-2017b/
```

**Warning:**

MongoDB uses the third party [timelib](https://github.com/derickr/timelib) library to provide accurate
conversions between timezones. Due to a recent update, `timelib`
could create inaccurate time zone conversions in older versions of
MongoDB.

To explicitly link to the time zone database in versions of MongoDB
prior to 5.0, download the [time zone database](https://downloads.mongodb.org/olson_tz_db/timezonedb-latest.zip).
and use the `timeZoneInfo` parameter.

**See also:**

`processManagement.timeZoneInfo`.

   

**`--outputConfig`**

Outputs the `mongod` instance's configuration options, formatted
in YAML, to `stdout` and exits the `mongod` instance. For
configuration options that uses externally-sourced-values,
`--outputConfig` returns the resolved value for those options.

**Warning:**

This may include any configured passwords or secrets previously
obfuscated through the external source.

For usage examples, see:

- expansion-directive-output

- /tutorial/convert-command-line-options-to-yaml
