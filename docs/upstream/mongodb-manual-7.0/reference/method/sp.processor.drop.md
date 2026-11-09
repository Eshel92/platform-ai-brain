<!-- Converted from reference/method/sp.processor.drop.txt (reStructuredText). Includes are inlined. -->

# sp.processor.drop() (mongosh method)

## Definition

**`sp.processor.drop()`**

Deletes a named
Stream Processor from
the current Stream Processing Workspace.

You can only invoke this command while connected to a stream
processing workspace.

This command requires `mongosh` version ≥ 2.0.

## Compatibility

This method is supported in Atlas Stream Processing Workspaces.

## Syntax

   
The `sp.processor.drop()` method has the following
syntax:

```json
sp.processor.drop()
```

   

## Command Fields

`sp.processor.drop()` takes no fields.

## Behavior

`sp.processor.drop()` deletes the given named stream processor
from the current stream processing workspace. If you invoke this
command on a currently running stream processor, it stops that
processor before deleting it.

## Access Control

The user running `sp.processor.drop()` must have the
`atlasAdmin` role.

## Example

The following example stops a stream processor named `solarDemo`

```
sp.solarDemo.drop()
```

## Learn More

- Manage Stream Processors
