<!-- Converted from reference/method/sp.listConnections.txt (reStructuredText). Includes are inlined. -->

# sp.listConnections() (mongosh method)

## Definition

**`sp.listConnections()`**

Returns documents for each connection in the connection registry of
the current stream processing workspace. Each document provides
descriptive information including the name and type of each
connection.

You can only invoke this command while connected to a stream
processing workspace.

This command requires `mongosh` version ≥ 2.0.

## Syntax

   
The `sp.listConnections()` method has the following syntax:

```json
sp.listConnections()
```

## Command Fields

`sp.listConnections()` takes no fields.

## Behavior

`sp.listConnections()` returns documents describing all of the
connections in the connection registry of the current stream
processing workspace to the shell.

## Access Control

The user running `sp.listConnections()` must have the
`atlasAdmin` role.

## Example

The following example shows an expected response from
`sp.listConnections()`:

```sh
sp.listStreamProcessors()
```

Output:

```json
{
```

	ok: 1,
	connections: [
	  { name: 'vt', type: 'atlas', cluster: 'versiontest' },
	  { name: 'testkafka', type: 'kafka' },
	  { name: 'sample_stream_solar', type: 'inmemory' },
	  { name: 'jsncluster0', type: 'atlas', cluster: 'jsncluster0' }
	]
      } 

## Learn More

- Manage Stream Processors
