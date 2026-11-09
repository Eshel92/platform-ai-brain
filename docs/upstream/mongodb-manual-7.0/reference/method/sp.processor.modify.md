<!-- Converted from reference/method/sp.processor.modify.txt (reStructuredText). Includes are inlined. -->

# sp.processor.modify() (mongosh method)

## Definition

**`sp.processor.modify()`**

Modifies a named Stream Processor on the
current Stream Processing Workspace.

## Compatibility

This method is supported in Atlas Stream Processing Workspaces.

## Syntax

The `sp.processor.modify()` method has the following syntax: 

```javascript
sp.processor.modify({
  pipeline: [
    <pipeline>
  ],
  name: <name>,
  dlq: {
    connectionName: <connectionName>,
    db: <db>,
    coll: <coll>
  },
  resumeFromCheckpoint: <resumeFromCheckpoint>,
  tier: <tier>
})
```

## Command Fields

`sp.processor.modify()` takes the following fields:

* - Field
  - Type
  - Necessity
  - Description

* - `pipeline`
  - array
  - Optional
  - Array of aggregation stages to apply to
    your streaming data where the last stage must be a sink
    stage. To learn more, see
    Stream Processing Aggregation.

* - `name`
  - string
  - Optional
  - New name for the stream processor.

* - `dlq`
  - object
  - Optional
  - Object that sets a dead letter
    queue for your stream processor. To remove an existing dead
    letter queue, pass an empty object (`{}`).

* - `dlq.connectionName`
  - string
  - Conditional
  - Label that identifies a connection in your connection
    registry. This connection must reference a Atlas cluster.
    Required when you set a dead letter queue.

* - `dlq.db`
  - string
  - Conditional
  - Name of a Atlas database on the cluster specified
    in `dlq.connectionName`. Required when you set a
    dead letter queue.

* - `dlq.coll`
  - string
  - Conditional
  - Name of a collection in the database specified in
    `dlq.db`. Required when you set a dead letter queue.

* - `resumeFromCheckpoint`
  - boolean
  - Optional
  - Flag that specifies whether the modified stream processor
    resumes from its last checkpoint. By default, this field is
    `true`. When set to `false`, the processor retains only
    summary statistics.

* - `tier`
  - string
  - Optional
  - The tier to assign to the stream processor. If you
    don't declare this option, the processor retains its
    current tier. Must be one of the following values:

    - `SP2`
    - `SP5`
    - `SP10`
    - `SP30`
    - `SP50`

    To learn more, see Tiers.

## Behavior

The stream processor must be in a `STOPPED` state before you invoke
this method. The `pipeline` argument replaces the processor's entire
existing pipeline, including stages that you do not change.

By default, the modified processor resumes from its last checkpoint. If
you set `resumeFromCheckpoint` to `false`, the modified
processor retains only summary statistics. When you modify a processor
with open windows, Atlas Stream Processing recomputes those windows on the updated
pipeline.

For limitations that apply when you modify stream processors, see
Modify a Stream Processor.

## Access Control

To run `sp.processor.modify()`, you must have the
`atlasAdmin` role.

## Example

The example changes a stopped stream processor named `solarDemo`
to add a `$match` stage, rename it, update its tier, and configure
a dead letter queue:

```javascript
sp.solarDemo.modify({
  pipeline: [
    { $source: { connectionName: "sample_stream_solar" }},
    { $match: { device_id: "device_0" }},
    { $merge: { into: {
        connectionName: "cluster0",
        db: "testout",
        coll: "testout2"
    }}}
  ],
  name: "solarDemoRenamed",
  dlq: {
    connectionName: "cluster0",
    db: "testout",
    coll: "dlq"
  },
  resumeFromCheckpoint: true,
  tier: "SP10"
})
```

Output:

```javascript
{ ok: 1 }
```

Start the renamed processor, then run `sp.listStreamProcessors()`
to verify the name, tier, and dead letter queue changes:

```javascript
sp.solarDemoRenamed.start()
sp.listStreamProcessors()
```

Output:

```javascript
[
  {
    id: '6a39b08e6d9040e1cef8e31f',
    name: 'solarDemoRenamed',
    lastModified: ISODate('2026-06-22T22:00:46.858Z'),
    state: 'STARTED',
    tier: 'SP10',
    errorMsg: '',
    workers: [ 'worker-5f4c5bbc9d-7hg2q' ],
    pipeline: [
      { '$source': { connectionName: 'sample_stream_solar' } },
      { '$match': { device_id: 'device_0' } },
      {
        '$merge': {
          into: {
            connectionName: 'cluster0',
            db: 'testout',
            coll: 'testout2'
          }
        }
      }
    ],
    lastStateChange: ISODate('2026-06-22T22:01:16.835Z'),
    dlq: {
      connectionName: 'cluster0',
      db: 'testout',
      coll: 'dlq'
    }
  }
]
```

Run `sp.processor.sample()` to verify the pipeline
change:

```javascript
sp.solarDemoRenamed.sample()
```

Output:

```javascript
{
  device_id: 'device_0',
  group_id: 9,
  timestamp: '2026-06-22T22:01:25.828+00:00',
  max_watts: 450,
  event_type: 0,
  obs: {
    watts: 122,
    temp: 18
  }
}
{
  device_id: 'device_0',
  group_id: 3,
  timestamp: '2026-06-22T22:01:26.828+00:00',
  max_watts: 450,
  event_type: 0,
  obs: {
    watts: 377,
    temp: 7
  }
}
```

## Learn More

- Manage Stream Processors
