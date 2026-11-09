<!-- Converted from reference/method/rs.remove.txt (reStructuredText). Includes are inlined. -->

# rs.remove()

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
