<!-- Converted from reference/method/sp.process.txt (reStructuredText). Includes are inlined. -->

# sp.process() (mongosh method)

## Definition

**`sp.process()`**

Creates an ephemeral Stream Processor on the
current Stream Processing Workspace.

You can only invoke this command while connected to a stream
processing workspace.

This command requires `mongosh` version ≥ 2.0.

## Compatibility

This method is supported in Atlas Stream Processing Workspaces.

## Syntax

The `sp.process()` method has the following
syntax:

```json
sp.process(
  [
    <pipeline>
  ],
  {
    <options>
  }
)
```

## Command Fields

`sp.process()` takes these fields:

* - Field
  - Type
  - Necessity
  - Description

* - `pipeline`
  - array
  - Required
  - Stream aggregation pipeline the
    stream processor applies to your streaming data.

* - `options`
  - object
  - Optional
  - Object that defines optional settings for your stream
    processor.

* - `options.limit`
  - integer
  - Optional
  - Maximum number of documents to return to your terminal.
    `sp.process()` ends the session after it returns this number
    of documents.

* - `options.tier`
  - string
  - Optional
  - Tier to assign to the stream processor. Tier names are
    case-insensitive. If you omit this field, the stream processor
    uses the default tier for your Stream Processing Workspace. Must be one of the
    following values:

    - `SP2`
    - `SP5`
    - `SP10`
    - `SP30`
    - `SP50`

    To learn more, see Tiers.

## Behavior

`sp.process()` creates an ephemeral, unnamed stream
processor on the current stream processing workspace and immediately
initializes it. This stream processor persists only while it
runs. If you terminate an ephemeral stream processor, you must create
it again to use it.

An ephemeral stream processor stops when any of the following occurs:

- The processor returns the number of documents set by
  `options.limit`.
- 10 minutes elapse.
- You stop the processor.

## Access Control

The user running `sp.process()` must have the
`atlasAdmin` role.

## Example

The following example creates an ephemeral stream processor that
ingests data from the `sample_stream_solar` connection. The
processor excludes all documents where the value of the `device_id`
field is `device_8`, passing the rest to a tumbling window with a 10-second duration. Each window groups the
documents it receives, then returns various statistics of each group.
The stream processor then merges these records to
`solar_db.solar_coll` over the `mongodb1` connection.

```json
sp.process(
  [
    {
      $source: {
        connectionName: 'sample_stream_solar',
        timeField: {
          $dateFromString: {
            dateString: '$timestamp'
          }
        }
      }
    },
    {
      $match: {
        $expr: {
          $ne: [
            "$device_id",
            "device_8"
          ]
        }
      }
    },
    {
      $tumblingWindow: {
        interval: {
          size: Int32(10),
          unit: "second"
        },
        "pipeline": [
          {
            $group: {
              "_id": { "device_id": "$device_id" },
              "max_temp": { $max: "$obs.temp" },
              "max_watts": { $max: "$obs.watts" },
              "min_watts": { $min: "$obs.watts" },
              "avg_watts": { $avg: "$obs.watts" },
              "median_watts": {
                $median: {
                  input: "$obs.watts",
                  method: "approximate"
                }
              }
            }
          }
        ]
      }
    },
    {
      $merge: {
        into: {
          connectionName: "mongodb1",
          db: "solar_db",
          coll: "solar_coll"
        },
        on: ["_id"]
      }
    }
  ]
)
```

## Learn More

- atlas-sp-aggregation
- atlas-sp-manage-processor
