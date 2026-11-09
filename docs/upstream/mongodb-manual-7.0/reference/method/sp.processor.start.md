<!-- Converted from reference/method/sp.processor.start.txt (reStructuredText). Includes are inlined. -->

# sp.processor.start() (mongosh method)

## Definition

**`sp.processor.start()`**

Starts a named
Stream Processor on
the current Stream Processing Workspace.

You can only invoke this command while connected to a stream
processing workspace.

This command requires `mongosh` version ≥ 2.0.

## Compatibility

This method is supported in Atlas Stream Processing Workspaces.

## Syntax

   
The `sp.processor.start()` method has the following syntax:

```json
sp.processor.start(
  {
    <options>
  }
)
```

## Command Fields

`sp.processor.start()` takes these fields:

* - Field
  - Type
  - Necessity	  
  - Description

* - `startAfter`
  - token
  - Conditional
  - See atlas-sp-agg-source-syntax-coll

* - `startAtOperationTime`
  - timestamp
  - Conditional
  - See atlas-sp-agg-source-syntax-coll

* - `tier`
  - string
  - Optional
  - The tier to which Atlas Stream Processing assigns the
    processor. If you do not declare this option,
    Atlas Stream Processing assigns the processor to the
    Stream Processing Workspace's tier. Must be one of the following:

    - `SP2`
    - `SP5`
    - `SP10`
    - `SP30`
    - `SP50`

    To learn more, see Tiers.

* - `autoscaling`
  - object
  - Optional
  - Object that enables and configures vertical autoscaling for
    the processor. To learn more, see Enable and
    Configure Autoscaling.

* - `autoscaling.enabled`
  - boolean
  - Conditional
  - Turns autoscaling on or off. Required when you set
    `autoscaling`.

* - `autoscaling.minTier`
  - string
  - Optional
  - The lowest tier the processor can scale down to. If you
    don't specify this field, Atlas Stream Processing uses the lower of the
    Stream Processing Workspace default tier and the tier that you start the
    processor on.

* - `autoscaling.maxTier`
  - string
  - Optional
  - The highest tier the processor can scale up to. If you
    don't specify this field, Atlas Stream Processing uses the Stream Processing Workspace
    maximum tier size.

* - `clearCheckpoints`
  - boolean
  - Optional
  - Specifies whether this start request skips checkpoint recovery.
    When set to `true`, the processor starts without recovering a
    checkpoint. By default, this field is `false`.

* - `resumeFromCheckpoint`
  - boolean
  - Optional
  - Specifies if the processor resumes from its most recent
    checkpoint when it starts. By default, this field is `true`,
    and the processor resumes from its most recent checkpoint. 

## Behavior

`sp.processor.start()` starts a named stream processor on the
current stream processing workspace. The stream processor must be in a
`STOPPED` state. If you invoke `sp.processor.start()` for a
stream processor that is not `STOPPED`, `mongosh` will return an error.

## Access Control

The user running `sp.processor.start()` must have the
`atlasAdmin` role.

## Example

The following example starts a stream processor named `solarDemo`.

```sh
sp.solarDemo.start()
```

## Learn More

- Manage Stream Processors
