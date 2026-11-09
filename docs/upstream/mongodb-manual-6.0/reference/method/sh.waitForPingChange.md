<!-- Converted from reference/method/sh.waitForPingChange.txt (reStructuredText). Includes are inlined. -->

# sh.waitForPingChange()

## Definition

**`sh.waitForPingChange(activePings, timeout, interval)`**

`sh.waitForPingChange()` waits for a change in ping state
of one of the `activepings`, and only returns when the specified
ping changes state.

| Parameter | Type | Description |
|---|---|---|
| `activePings` | array | An array of active pings from the `mongos` collection. |
| `timeout` | integer | Number of milliseconds to wait for a change in ping state. |
| `interval` | integer | Number of milliseconds to sleep in each waiting cycle. |

          

## Compatibility

This method is available in deployments hosted in the following environments: 

**Important:**

This command is not supported in MongoDB Atlas clusters.
For information on Atlas support for all commands, 
see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB
