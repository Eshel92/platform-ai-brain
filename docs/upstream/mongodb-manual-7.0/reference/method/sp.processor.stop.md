<!-- Converted from reference/method/sp.processor.stop.txt (reStructuredText). Includes are inlined. -->

# sp.processor.stop() (mongosh method)

## Definition

**`sp.processor.stop()`**

Stops a named
Stream Processor on
the current Stream Processing Workspace.

You can only invoke this command while connected to a stream
processing workspace.

This command requires `mongosh` version ≥ 2.0.

## Compatibility

This method is supported in Atlas Stream Processing Workspaces.

## Syntax

   
The `sp.processor.stop()` method has the following syntax:

```sh
sp.processor.stop()
```

## Command Fields

`sp.processor.stop()` takes no fields.

## Behavior

`sp.processor.stop()` stops a named stream processor on the
current stream processing workspace. The stream processor must be in a
`running` state. If you invoke `sp.processor.stop()` for a
stream processor that is not `running`, `mongosh` will return an error. 

## Access Control

The user running `sp.processor.stop()` must have the
`atlasAdmin` role.

## Example

The following example stops a stream processor named `solarDemo`.

```
sp.solarDemo.stop()
```

## Learn More

- Manage Stream Processors
