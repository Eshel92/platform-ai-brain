<!-- Converted from reference/server-sessions.txt (reStructuredText). Includes are inlined. -->

# Server Sessions

## Overview

MongoDB's server sessions, or logical sessions, are the underlying
framework used by client sessions to support causal-consistency and 
retryable writes.

**Important:**

This page documents server sessions. Applications interact with
server sessions through client sessions. The methods you can call on
a client session object, such as `Session.getDatabase()`, are
documented in the `Session` reference.

Server sessions are available for replica sets and sharded clusters only.

## Command Options

Starting in 3.6, MongoDB drivers associate all operations with a server
session, with the exception of unacknowledged writes. The following
options are available for all commands to support association with a
server session:

**Important:**

`mongosh` and the drivers assign these options
to the commands in the session.

| Option | Type | Description |
|---|---|---|
| `lsid` | Document | The document that specifies the unique ID of the session associated with the command. If the `txnNumber` is specified, the `lsid` is required. |
| `txnNumber` | 64-bit integer | A strictly increasing non-negative number that uniquely identifies the command in the command's session. If specified, the command must also include the `lsid` option. |

For the `delete`, `insert`, and `update`
commands that take an array of statements, the following option is also
available:

**Important:**

Do not manually set `stmtIds`. MongoDB sets the `stmtIds`
to be strictly increasing non-negative numbers.

| Option | Type | Description |
|---|---|---|
| `stmtIds` | Array of 32-bit integers | Array of numbers that uniquely identify their respective write operations within the write command. |

## Sessions Commands

The following commands can be used to list, manage, and kill server
sessions throughout MongoDB clusters:

| Commands | Descriptions |
|---|---|
| `endSessions` | Expires specified server sessions. |
| `killAllSessions` | Kills all server sessions. |
| `killAllSessionsByPattern` | Kills all server sessions that match the specified pattern. |
| `killSessions` | Kills specified server sessions. |
| `refreshSessions` | Refreshes idle server sessions. |
| `startSession` | Starts a new server session. |

## Sessions and Access Control

If the deployment enforces authentication/authorization, the user must
be authenticated to start a session, and only that user can use the
session.

To use sessions with `$external` authentication users
(Kerberos, LDAP, or X.509 users), usernames cannot be greater
than 10k bytes.

If the deployment does not enforce authentication/authorization, a
created session has no owner and can be used by any user on any
connection. If a user authenticates and creates a session for a
deployment that does not enforce authentication/authorization, that user
owns the session. However, any user on any connection may use the
session.

If the deployment transitions to authentication without any downtime, any
sessions without an owner cannot be used.

**See also:**

`maxSessions`
