<!-- Converted from tutorial/configure-auditing.txt (reStructuredText). Includes are inlined. -->

# Configure Auditing

**Note:** Auditing in MongoDB Atlas

MongoDB Atlas supports auditing for all `M10` and larger
clusters. Atlas supports specifying a JSON-formatted audit
filter as documented in /tutorial/configure-audit-filters 
and using the Atlas audit filter builder for simplified auditing 
configuration. To learn more, see the Atlas documentation for 
Set Up Database Auditing
and
Configure a Custom Auditing Filter.

MongoDB Enterprise
supports auditing of various operations. A complete
auditing solution must involve **all** `mongod` server and
`mongos` router processes.

The audit facility can write audit events to the console, the
syslog (option is unavailable on Windows), a JSON file, or a
BSON file. For details on the audited operations and the audit log
messages, see /reference/audit-message.

## Enable and Configure Audit Output

To enable auditing in MongoDB Enterprise, set an audit output
destination with `--auditDestination`.

**Warning:**

For sharded clusters, if you enable auditing on
`mongos` instances you must also enable auditing on the
cluster's `mongod` instances. Configure auditing for
`mongod` on all of the shards and config servers.

### Output to Syslog

To enable auditing and print audit events to the syslog (option
is unavailable on Windows) in JSON format, specify `syslog` for the
`--auditDestination` setting. For
example:

```bash
mongod --dbpath data/db --auditDestination syslog
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

**Important:**

Before you bind to other ip addresses, consider enabling
access control and other security measures listed
in /administration/security-checklist to prevent unauthorized
access.

**Warning:**

The syslog message limit can result in the truncation of the audit
messages. The auditing system will neither detect the truncation nor
error upon its occurrence. 

In a Linux system, messages are subject to the rules defined in the Linux
configuration file `/etc/systemd/journald.conf`. By default, log message 
bursts are limited to 1000 messages within a 30 second period. To see more 
messages, increase the `RateLimitBurst` parameter in 
`/etc/systemd/journald.conf`.

You may also specify these options in the configuration file:

```yaml
storage:
   dbPath: data/db
auditLog:
   destination: syslog
```

### Output to Console

To enable auditing and print the audit events to standard
output (i.e. `stdout`), specify `console` for the
`--auditDestination` setting. For
example:

```bash
mongod --dbpath data/db --auditDestination console
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

**Important:**

Before you bind to other ip addresses, consider enabling
access control and other security measures listed
in /administration/security-checklist to prevent unauthorized
access.

You may also specify these options in the configuration file:

```yaml
storage:
   dbPath: data/db
auditLog:
   destination: console
```

### Output to JSON File

To enable auditing and print audit events to a file in JSON
format, specify the following options:

| Option | Value |
|---|---|
| `--auditDestination` | `file` |
| `--auditFormat` | `JSON` |
| `--auditPath` | The output filename. Accepts either the full path name or relative path name. |

  
For example, the following enables auditing and records audit events to
a file with the relative path name of `data/db/auditLog.json`:

```bash
mongod --dbpath data/db --auditDestination file --auditFormat JSON --auditPath data/db/auditLog.json
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

**Important:**

Before you bind to other ip addresses, consider enabling
access control and other security measures listed
in /administration/security-checklist to prevent unauthorized
access.

The audit file may be rotated with the `logRotate` command,
either alongside  the server log or independently. Rotation specifics
may be configured with the `systemLog.logRotate` configuration
file option or the `--logRotate`
command-line option.

You may also specify these options in the configuration file:

```yaml
storage:
   dbPath: data/db
auditLog:
   destination: file
   format: JSON
   path: data/db/auditLog.json
```

**Note:** Printing audit events to a file in JSON format degrades

server performance more than printing to a file in BSON format.

### Output to BSON File

To enable auditing and print audit events to a file in BSON binary
format, specify the following options:

| Option | Value |
|---|---|
| `--auditDestination` | `file` |
| `--auditFormat` | `BSON` |
| `--auditPath` | The output filename. Accepts either the full path name or relative path name. |

For example, the following enables auditing and records audit events to
a BSON file with the relative path name of `data/db/auditLog.bson`:

```bash
mongod --dbpath data/db --auditDestination file --auditFormat BSON --auditPath data/db/auditLog.bson
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

**Important:**

Before you bind to other ip addresses, consider enabling
access control and other security measures listed
in /administration/security-checklist to prevent unauthorized
access.

The audit file is `rotated` at the same time as
the server log file. Rotation specifics may be configured with the
`systemLog.logRotate` configuration file option or the
`--logRotate` command-line option.

You may also specify these options in the configuration file:

```yaml
storage:
   dbPath: data/db
auditLog:
   destination: file
   format: BSON
   path: data/db/auditLog.bson
```

The following example converts the audit log into readable form using
`bsondump` and outputs the result:

```bash
bsondump data/db/auditLog.bson
```

## Runtime Audit Filter Management

Starting in MongoDB 5.0, audit filters can be configured at runtime.
Runtime Audit Filter Management provides three benefits compared to
audit filter configurations that are specified in a local
`mongod` or `mongos` configuration file:

- rafm-separation
- rafm-configurability
- rafm-consistency

### Separation of Concerns

Prior to MongoDB 5.0, anyone auditing a MongoDB `mongod`
or `mongos` instance had to have write access to the host
server's file system in order to update audit filters. Runtime Audit
Filter Management improves security by separating audit access from
administrative access.

Using Runtime Audit Filter Management instead of editing configuration
files directly means: 

- File system access is not required so an auditor does not need access
  to the `mongod` or `mongos` host server.

- There is no direct access to the `mongod` or
  `mongos` instance's configuration file.

- Runtime Audit Filter Management only exposes audit filters and the `auditAuthorizationSuccess`
  parameter.

### Runtime Configurability

Starting in MongoDB 5.0, when Runtime Audit Filter Management is
enabled, auditing can be reconfigured at runtime without restarting the
`mongod` or `mongos` instance. A statically
configured instance has to be restarted to update its audit settings.

Audit filter modifications made at runtime persist when an instance is
shutdown and restarted.

### Consistency

Within a cluster, if all participating `mongod` and
`mongos` nodes are configured to use Runtime Audit Filter
Management, then every node will use the same audit filters. In
contrast, if each node has its own locally configured audit filters,
there is no guarantee of audit filter consistency across nodes.

### Enable Runtime Audit Filter Management

Starting in MongoDB 5.0, audit configurations for `mongod`
and `mongos` nodes can be configured at runtime. A group
of these nodes can take part in a distributed audit configuration. 

To include a node in a distributed audit configuration, update the
node's configuration file as follows and restart the server.

| Parameter | Value |
|---|---|
| `auditLog.runtimeConfiguration` | `true` |
| `auditLog.filter` | Unset |
| `auditAuthorizationSuccess` | Unset |

The server logs an error and fails to start if:

-  `runtimeConfiguration` is `true` and
-  either `auditLog.filter` or `auditAuthorizationSuccess` is set.

To modify audit filters and the `auditAuthorizationSuccess` parameter at
runtime, see `setAuditConfig`.

**See also:**

- /tutorial/configure-audit-filters
- /core/auditing
- /reference/audit-message
- `setAuditConfig`
- `getAuditConfig`
