<!-- Converted from reference/method/rs.stepDown.txt (reStructuredText). Includes are inlined. -->

# rs.stepDown() (mongosh method)

## Description

**`rs.stepDown(stepDownSecs, secondaryCatchUpPeriodSecs)`**

Instructs the primary of the replica set to become a
secondary. After the primary steps down, eligible secondaries
hold an election for primary.

The method does not immediately step down the primary. If no
`electable` secondaries
are up to date with the primary, the primary waits up to
`secondaryCatchUpPeriodSecs` (by default 10 seconds) for a
secondary to catch up. Once an electable secondary is
available, the method steps down the primary.

Once stepped down, the original primary becomes a secondary and is
ineligible from becoming primary again for the remainder of time
specified by `stepDownSecs`.

For a detailed explanation of the method 's execution,
see rs.stepDown-behavior.

**Note:**

The method is only valid against the primary and throws an
error if run on a non-primary member.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `replSetStepDown` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `rs.stepDown()` method has the following parameters:

| Parameter | Type | Description |
|---|---|---|
| `stepDownSecs` | number | The number of seconds to step down the primary, during which time the stepdown member is ineligible for becoming primary. If you specify a non-numeric value, the command uses `60` seconds. The stepdown period starts from the time that the `mongod` receives the command. The stepdown period must be greater than the `secondaryCatchUpPeriodSecs`. |
| `secondaryCatchUpPeriodSecs` | number | Optional. The number of seconds that `mongod` will wait for an electable secondary to catch up to the primary. When specified, `secondaryCatchUpPeriodSecs` overrides the default wait time of `10` seconds. |

## Compatibility

This method is available in deployments hosted in the following environments:

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

### Concurrent Operations

The `rs.stepDown()` method attempts to
terminate long running user operations that block the primary
from stepping down, such as an index build, a write operation or a
map-reduce job.

### Availability of Eligible Secondaries

The method then initiates a catchup period where it waits up to
`secondaryCatchUpPeriodSeconds`, by default 10 seconds, for a
secondary to become up-to-date with the primary. The primary only steps
down if a secondary is up-to-date with the primary during the
catchup period to prevent rollbacks.

If no electable secondary meets this criterion by the end of the waiting
period, the primary does not step down and the method errors.
\

Once the primary steps down successfully, that node cannot become the
primary for the remainder of the `stepDownSecs` period,
which began when the node received the method.

### Client Connections

`rs.stepDown()` method doesn't close all client 
connections. 

### Writes During Stepdown

**Note:**

All writes to the primary fail during the period starting when the
`rs.stepDown()` method is received until either a new
primary is elected, or if there are no electable secondaries, the
original primary resumes normal operation. 

Writes that were in progress when `rs.stepDown()` is run
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
