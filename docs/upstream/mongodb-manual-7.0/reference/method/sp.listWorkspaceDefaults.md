<!-- Converted from reference/method/sp.listWorkspaceDefaults.txt (reStructuredText). Includes are inlined. -->

# sp.listWorkspaceDefaults() (mongosh method)

## Definition

**`sp.listWorkspaceDefaults()`**

Returns a document containing the default and maximum tier
configuration for the current Stream Processing Workspace.
This information describes the tier sizing capabilities of your workspace.

## Compatibility

This method is supported in Atlas Stream Processing Workspaces.

## Syntax

   
The `sp.listWorkspaceDefaults()` method has the following syntax:

```javascript
sp.listWorkspaceDefaults()
```

## Return Value

`sp.listWorkspaceDefaults()` returns a document containing the following fields:

| Field | Type | Description |
|---|---|---|
| `defaultTierSize` | string | The default tier size assigned to stream processors in this workspace. Stream processors inherit this tier unless you explicitly specify a different tier when creating or starting them. |
| `maxTierSize` | string | The maximum tier size available for stream processors in this workspace. This represents the largest tier you can assign to any stream processor. |

## Behavior

`sp.listWorkspaceDefaults()` returns a single document describing
the default and maximum tier configuration for the current stream
processing workspace to `STDOUT`.

## Access Control

Running `sp.listWorkspaceDefaults()` requires the `atlasAdmin`
role.

## Example

The following example shows an expected response from
`sp.listWorkspaceDefaults()`:

```sh
sp.listWorkspaceDefaults()
```

Output:

```json
{
  defaultTierSize: "T2",
  maxTierSize: "T8"
}
```

## Learn More

- Manage Stream Processors
- `sp.listStreamProcessors()`
- `sp.createStreamProcessor()`
