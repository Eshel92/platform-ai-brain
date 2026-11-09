<!-- Converted from tutorial/configure-audit-filters.txt (reStructuredText). Includes are inlined. -->

# Configure Audit Filters

**Note:** Auditing in MongoDB Atlas

MongoDB Atlas supports auditing for all `M10` and larger
clusters. Atlas supports specifying a JSON-formatted audit
filter as documented below and using the Atlas audit filter
builder for simplified auditing configuration. To learn more, see
the Atlas documentation for
Set Up Database Auditing
and Configure a Custom Auditing Filter.

MongoDB Enterprise
supports auditing of various operations. When
enabled, the audit facility, by
default, records all auditable operations as detailed in
audit-action-details-results. You can specify event filters to
limit which events are recorded.

You can configure audit filters at startup or you can configure MongoDB to
allow filter configuration at runtime.

## Audit Filter Syntax

Audit filters have the same form as query predicate documents specified
to `find` commands. To see example audit filters, see
audit-filter-examples.

## Filter Configuration at Runtime

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

## Filter Configuration at System Startup

Audit filters can be specified on the command line or else in the
configuration file used to start the
`mongod` or `mongos` instance.

### Configuration File Usage

Filters can be specified in YAML under the `auditLog` session of the
configuration file. See the examples
below for sample configurations.

**Note:**

If `runtimeConfiguration` is enabled, then the
configuration file cannot be used to
specify audit filters.

## Examples

### Record All Auditable Events

To record all auditable events, do not specify an audit filter. By
default, the audit facility records all auditable operations.

### Filter for Multiple Operation Types

The following example audits only the `createCollection`
and `dropCollection` actions by using the filter:

```bash
{ atype: { $in: [ "createCollection", "dropCollection" ] } }
```

To specify an audit filter, enclose the filter document in single
quotes to pass the document as a string.

```javascript
mongod --dbpath data/db --auditDestination file --auditFilter '{ atype: { $in: [ "createCollection", "dropCollection" ] } }' --auditFormat BSON --auditPath data/db/auditLog.bson
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

To specify the audit filter in a 
configuration file, you must use the YAML format 
of the configuration file.

```yaml
storage:
   dbPath: data/db
auditLog:
   destination: file
   format: BSON
   path: data/db/auditLog.bson
   filter: '{ atype: { $in: [ "createCollection", "dropCollection" ] } }'
```

### Filter on Authentication Operations on a Single Database

The `<field>` can include any field in the audit message. For authentication operations (i.e.
`atype: "authenticate"`), the audit messages include a `db` field
in the `param` document.

The following example audits only the `authenticate` operations
that occur against the `test` database by using the filter:

```bash
{ atype: "authenticate", "param.db": "test" }
```

To specify an audit filter, enclose the filter document in single
quotes to pass the document as a string.

```javascript
mongod --dbpath data/db --auth --auditDestination file --auditFilter '{ atype: "authenticate", "param.db": "test" }' --auditFormat BSON --auditPath data/db/auditLog.bson
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

To specify the audit filter in a 
configuration file, you must use the YAML format 
of the configuration file.

```yaml
storage:
   dbPath: data/db
security:
   authorization: enabled
auditLog:
   destination: file
   format: BSON
   path: data/db/auditLog.bson
   filter: '{ atype: "authenticate", "param.db": "test" }'
```

To filter on all `authenticate` operations across databases, omit
`"param.db": "test"` and use the filter `{ atype: "authenticate" }`.

### Filter on Collection Creation and Drop Operations for a Single Database

The `<field>` can include any field in the audit message. For collection creation and drop
operations (i.e. `atype: "createCollection"` and ``atype:
"dropCollection"`), the audit messages include a namespace `ns``
field in the `param` document.

The following example audits only the `createCollection` and
`dropCollection` operations that occur against the `test` database
by using the filter:

**Note:**

The regular expression requires two backslashes (`\\`) to escape
the dot (`.`).

```bash
{ atype: { $in: [ "createCollection", "dropCollection" ] }, "param.ns": /^test\\./ } }
```

To specify an audit filter, enclose the filter document in single
quotes to pass the document as a string.

```javascript
mongod --dbpath data/db --auth --auditDestination file --auditFilter '{ atype: { $in: [ "createCollection", "dropCollection" ] }, "param.ns": /^test\\./ } }' --auditFormat BSON --auditPath data/db/auditLog.bson
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

To specify the audit filter in a 
configuration file, you must use the YAML format 
of the configuration file.

```yaml
storage:
   dbPath: data/db
security:
   authorization: enabled
auditLog:
   destination: file
   format: BSON
   path: data/db/auditLog.bson
   filter: '{ atype: { $in: [ "createCollection", "dropCollection" ] }, "param.ns": /^test\\./ } }'
```

### Filter by Authorization Role

The following example audits operations by users with
`readWrite` role on the `test` database, including users
with roles that inherit from `readWrite`, by using the filter:

```bash
{ roles: { role: "readWrite", db: "test" } }
```

To specify an audit filter, enclose the filter document in single
quotes to pass the document as a string.

```javascript
mongod --dbpath data/db --auth --auditDestination file --auditFilter '{ roles: { role: "readWrite", db: "test" } }' --auditFormat BSON --auditPath data/db/auditLog.bson
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

To specify the audit filter in a 
configuration file, you must use the YAML format 
of the configuration file.

```yaml
storage:
   dbPath: data/db
security:
   authorization: enabled
auditLog:
   destination: file
   format: BSON
   path: data/db/auditLog.bson
   filter: '{ roles: { role: "readWrite", db: "test" } }'
```

### Filter on Read and Write Operations

To capture read and write operations in the audit, you must also
enable the audit system to log authorization successes using the
`auditAuthorizationSuccess` parameter.
[#authorization-agnostic]_

**Note:**

Enabling `auditAuthorizationSuccess` degrades performance
more than logging only the authorization failures.

This filter audits multiple read and write operations:

```bash
{
   atype: "authCheck",
   "param.command": { $in: [ "find", "insert", "delete", "update", "findAndModify" ] }
}
```

The audited operations include:

- `find()`
- `insertOne()`
- `insertMany()`
- `remove()`
- `updateOne()`
- `updateMany()`
- `findAndModify()`

To specify an audit filter, enclose the filter document in single
quotes to pass the document as a string.

```javascript
mongod --dbpath data/db --auth --setParameter auditAuthorizationSuccess=true --auditDestination file --auditFilter '{ atype: "authCheck", "param.command": { $in: [ "find", "insert", "delete", "update", "findAndModify" ] } }' --auditFormat BSON --auditPath data/db/auditLog.bson
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

To specify the audit filter in a 
configuration file, you must use the YAML format 
of the configuration file.

```yaml
storage:
   dbPath: data/db
security:
   authorization: enabled
auditLog:
   destination: file
   format: BSON
   path: data/db/auditLog.bson
   filter: '{ atype: "authCheck", "param.command": { $in: [ "find", "insert", "delete", "update", "findAndModify" ] } }'
setParameter: { auditAuthorizationSuccess: true }
```

### Filter on Read and Write Operations for a Collection

To capture read and write operations in the audit, you must also
enable the audit system to log authorization successes using the
`auditAuthorizationSuccess` parameter.
[#authorization-agnostic]_

**Note:**

Enabling `auditAuthorizationSuccess` degrades performance
more than logging only the authorization failures.

This filter audits multiple read and write operations on the `orders`
collection in the `test` database:

```bash
{
    atype: "authCheck",
    "param.ns": "test.orders",
    "param.command": { $in: [ "find", "insert", "delete", "update", "findAndModify" ] }
}
```

The audited operations include: 

- `find()`
- `insertOne()`
- `insertMany()`
- `remove()`
- `updateOne()`
- `updateMany()`
- `findAndModify()`

To specify an audit filter, enclose the filter document in single
quotes to pass the document as a string.

```javascript
mongod --dbpath data/db --auth --setParameter auditAuthorizationSuccess=true --auditDestination file --auditFilter '{ atype: "authCheck", "param.ns": "test.orders", "param.command": { $in: [ "find", "insert", "delete", "update", "findAndModify" ] } }' --auditFormat BSON --auditPath data/db/auditLog.bson
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

To specify the audit filter in a 
configuration file, you must use the YAML format 
of the configuration file.

```yaml
storage:
   dbPath: data/db
security:
   authorization: enabled
auditLog:
   destination: file
   format: BSON
   path: data/db/auditLog.bson
   filter: '{ atype: "authCheck", "param.ns": "test.orders", "param.command": { $in: [ "find", "insert", "delete", "update", "findAndModify" ] } }'
setParameter: { auditAuthorizationSuccess: true }
```

### Specify Top-Level Query Operators ($or)

To filter on multiple audit message fields, you can specify a top-level
query operator like `$or`. For example, the following filter
captures operations where either `atype` is `authenticate` or the
operation was performed by a user with the `readWrite` role:

```javascript
{
   $or: [
      { atype: "authenticate" },
      { "roles.role": "readWrite" }
   ]
}
```

To specify an audit filter, enclose the filter document in single
quotes to pass the document as a string.

```javascript
mongod --dbpath data/db --auth --setParameter auditAuthorizationSuccess=true --auditDestination file --auditFilter '{ $or: [ { atype: "authenticate" }, { "roles.role": "readWrite" } ] }' --auditFormat BSON --auditPath data/db/auditLog.bson
```

Include additional options as required for your configuration. For
instance, if you wish remote clients to connect to your deployment
or your deployment members are run on different hosts, specify the
`--bind_ip`. 

To specify the audit filter in a 
configuration file, you must use the YAML format 
of the configuration file.

```yaml
storage:
   dbPath: data/db
security:
   authorization: enabled
auditLog:
   destination: file
   format: BSON
   path: data/db/auditLog.bson
   filter: '{ $or: [ { atype: "authenticate" }, { "roles.role": "readWrite" } ] }'
```

## Learn More

- /tutorial/configure-auditing
- /core/auditing
- /reference/audit-message
- `getAuditConfig`
- `setAuditConfig`
