<!-- Converted from reference/command/replSetStepDown.txt (reStructuredText). Includes are inlined. -->

# replSetStepDown

## Description

**`replSetStepDown`**

Instructs the primary of the replica set to become a
secondary. After the primary steps down, eligible secondaries
hold an election for primary.

The command does not immediately step down the primary. If no
`electable` secondaries
are up to date with the primary, the primary waits up to
`secondaryCatchUpPeriodSecs` (by default 10 seconds) for a
secondary to catch up. Once an electable secondary is
available, the command steps down the primary.

Once stepped down, the original primary becomes a secondary and is
ineligible from becoming primary again for the remainder of time
specified by `replSetStepDown: <seconds>`.

For a detailed explanation of the command 's execution,
see replSetStepDown-behavior.

**Note:**

The command is only valid against the primary and throws an
error if run on a non-primary member.

**Tip:**

In `mongosh`, this command can also be run through the `rs.stepDown` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

The `replSetStepDown` can only run on the `admin` database.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, M10+, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     replSetStepDown: <seconds>,
     secondaryCatchUpPeriodSecs: <seconds>,
     force: <true|false>
   } 
)
```

## Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| `replSetStepDown` | number | The number of seconds to step down the primary, during which time the stepdown member is ineligible for becoming primary. If you specify a non-numeric value, the command uses `60` seconds. The stepdown period starts from the time that the `mongod` receives the command. The stepdown period must be greater than the `secondaryCatchUpPeriodSecs`. |
| `secondaryCatchUpPeriodSecs` | number | Optional. The number of seconds that the `mongod` will wait for an electable secondary to catch up to the primary. When specified, `secondaryCatchUpPeriodSecs` overrides the default wait time of either `10` seconds or if `force: true`, `0` seconds. |
| `force` | boolean | Optional. A boolean that determines whether the primary steps down if no electable and up-to-date secondary exists within the wait period. If `true`, the primary steps down even if no suitable secondary member exists; this could lead to rollbacks if a secondary with replication lag becomes the new primary. If `false`, the primary does not step down if no suitable secondary member exists and the command returns an error. Defaults to `false`. |

       

## Behavior

### Concurrent Operations

The `replSetStepDown` command attempts to
terminate long running user operations that block the primary
from stepping down, such as an index build, a write operation or a
map-reduce job.

### Availability of Eligible Secondaries

The command then initiates a catchup period where it waits up to
`secondaryCatchUpPeriodSeconds`, by default 10 seconds, for a
secondary to become up-to-date with the primary. The primary only steps
down if a secondary is up-to-date with the primary during the
catchup period to prevent rollbacks.

If no electable secondary meets this criterion by the end of the waiting
period, the primary does not step down and the command errors.
You can override this behavior and issue with command with the `force: true` option to immediately step down the primary.

Once the primary steps down successfully, that node cannot become the
primary for the remainder of the `replSetStepDown: <seconds>` period,
which began when the node received the command.

### Client Connections

`replSetStepDown` command doesn't close all client 
connections. 

### Writes During Stepdown

**Note:**

All writes to the primary fail during the period starting when the
`replSetStepDown` command is received until either a new
primary is elected, or if there are no electable secondaries, the
original primary resumes normal operation. 

Writes that were in progress when `replSetStepDown` is run
are killed. In-progress transactions
also fail with transient-transaction-error and can be
retried as a whole.

The time period where writes fail is at maximum:

`secondaryCatchUpPeriodSecs` (10s by default) +
`electionTimeoutMillis` (10s by default).

### Election Handoff

When you step down a primary using `rs.stepDown` or
`replSetStepDown` without setting the `force` field to
`true`, the stepped-down primary nominates an eligible secondary
to call an election immediately. 

## Examples

### Step Down with Default Options

The following example, run on the current primary, attempts to step
down the member for `120` seconds.

The operation waits up to the default `10` seconds for a
secondary to catch up. If no suitable secondary exists, the primary
does not step down and the command errors.

**Note:**

All writes to the primary fail during the period starting when the
`replSetStepDown` command is received until either a new
primary is elected, or if there are no electable secondaries, the
original primary resumes normal operation. 

Writes that were in progress when `replSetStepDown` is run
are killed. In-progress transactions
also fail with transient-transaction-error and can be
retried as a whole.

The time period where writes fail is at maximum:

`secondaryCatchUpPeriodSecs` (10s by default) +
`electionTimeoutMillis` (10s by default).

```javascript
db.adminCommand( { replSetStepDown: 120 } )
```

### Specify Wait Time for Secondary Catch Up

The following example, run on the current primary, attempts to step
down the member for `120` seconds, waiting up to `15` seconds for
an electable secondary to catch up. If no suitable secondary exists,
the primary does not step down and the command errors.

**Note:**

All writes to the primary fail during the period starting when the
`replSetStepDown` command is received until either a new
primary is elected, or if there are no electable secondaries, the
original primary resumes normal operation. 

Writes that were in progress when `replSetStepDown` is run
are killed. In-progress transactions
also fail with transient-transaction-error and can be
retried as a whole.

The time period where writes fail is at maximum:

`secondaryCatchUpPeriodSecs` (10s by default) +
`electionTimeoutMillis` (10s by default).

```javascript
db.adminCommand( { replSetStepDown: 120, secondaryCatchUpPeriodSecs: 15 } )
```

### Specify Secondary Catch Up with Force Step Down

The following example, run on the current primary, attempts to step
down the member for `120` seconds, waiting up to `15` seconds for
an electable secondary to catch up. Because of the `force: true`
option, the primary steps down even if no suitable secondary exists.

**Note:**

All writes to the primary fail during the period starting when the
`replSetStepDown` command is received until either a new
primary is elected, or if there are no electable secondaries, the
original primary resumes normal operation. 

Writes that were in progress when `replSetStepDown` is run
are killed. In-progress transactions
also fail with transient-transaction-error and can be
retried as a whole.

The time period where writes fail is at maximum:

`secondaryCatchUpPeriodSecs` (10s by default) +
`electionTimeoutMillis` (10s by default).

```javascript
db.adminCommand( { replSetStepDown: 120, secondaryCatchUpPeriodSecs: 15, force: true } )
```

**See also:**

`rs.stepDown()`
