<!-- Converted from reference/method/rs.remove.txt (reStructuredText). Includes are inlined. -->

# rs.remove() (mongosh method)

## Definition

**`rs.remove(hostname)`**

Removes the member described by the `hostname` parameter from the
current replica set. This function will disconnect the
shell briefly and forces a reconnection as the replica set
renegotiates which member will be primary. As a
result, the shell will display an error even if this command
succeeds.

The `rs.remove()` method has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `hostname` | string | The hostname of a system in the replica set. |

**Note:**

Before running the `rs.remove()` operation, it is good
practice to *shut down* the replica set member that you are
removing.

## Compatibility

This method is available in deployments hosted in the following environments:

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

### Global Write Concern

Removing a member changes the number of voting members in the replica
set, which can change the implicit default write concern. 

You must explicitly set the global default write concern before attempting to reconfigure a replica set with a configuration that would change the implicit
default write concern. To set the global default write concern, use the
`setDefaultRWConcern` command.

### Removal Waits Until a Majority of Members Install the Replica Configuration

`rs.remove()` runs the `replSetReconfig` command
with a configuration that omits the removed member. The method waits
until a majority of voting replica set members install the new replica
configuration before it returns success. A voting member is any replica
set member where `members[n].votes` is `1`, including
arbiters. To learn how replica set members install a new configuration,
see replSetReconfig-cmd-majority-install.

`rs.remove()` does not accept a maxTimeMS limit. If a majority of voting members
never install the new configuration, the operation waits indefinitely.

### Connections to the Removed Member

..
  This behavior will change once SERVER-36417 closes. 

By default, replica set members wait for 5 minutes before dropping
connections to the removed member. In sharded replica sets, you can
modify this timeout using the
`ShardingTaskExecutorPoolHostTimeoutMS` server parameter.

To immediately drop all outgoing connections from the replica set to
the removed member, run the `dropConnections`
administrative command  on each remaining member on the replica set:

```javascript
db.adminCommand( 
  {
    "dropConnections" : 1,
    "hostAndPort" : [
      "<hostname>:<port>"
    ] 
  } 
)
```

Replace `<hostname>` with the hostname of the removed member and
`<port>` with the port the `mongod` listened on.
