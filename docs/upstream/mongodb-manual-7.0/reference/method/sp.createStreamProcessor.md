<!-- Converted from reference/method/sp.createStreamProcessor.txt (reStructuredText). Includes are inlined. -->

# sp.createStreamProcessor() (mongosh method)

## Definition

**`sp.createStreamProcessor()`**

Creates a Stream Processor on
the current Stream Processing Workspace.

You can only invoke this command while connected to a stream
processing workspace.

This command requires `mongosh` version ≥ 2.0.

## Compatibility

This method is supported in Atlas Stream Processing Workspaces.

## Syntax

   
The `sp.createStreamProcessor()` method has the following
syntax:

```json
sp.createStreamProcessor(
  <name>,
  [
    <pipeline>
  ],
  {
    <options>
  }
)
```

## Command Fields

`sp.createStreamProcessor()` takes these fields:

* - Field
  - Type
  - Necessity	  
  - Description

* - `name`
  - string
  - Required
  - Logical name for the stream processor. This must be unique
    within the stream processing workspace.

* - `pipeline`
  - array
  - Required
  - Stream aggregation pipeline you
    want to apply to your streaming data.

* - `options`
  - object
  - Optional
  - Object defining various optional settings for your stream
    processor.

* - `options.dlq`
  - object
  - Conditional
  - Object assigning a 
    dead letter queue for your stream processing workspace.
    This field is necessary if you define the `options` field.

* - `options.dlq.connectionName`
  - string
  - Conditional
  - Label that identifies a connection in your 
    connection registry. This connection must reference an 
    Atlas cluster. This field is necessary if you define the
    `options.dlq` field.

* - `options.dlq.db`
  - string
  - Conditional
  - Name of an Atlas database on the cluster specified 
    in `options.dlq.connectionName`. This field is necessary if 
    you define the `options.dlq` field.

* - `options.dlq.coll`
  - string
  - Conditional
  - Name of a collection in the database specified in
    `options.dlq.db`. This field is necessary if you 
    define the `options.dlq` field.

* - `options.tier`
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

## Behavior

`sp.createStreamProcessor()` creates a persistent, named stream
processor on the current stream processing workspace. You can
initialize this stream processor with
`sp.processor.start()`. If you try to create a stream
processor with the same name as an existing stream processor,
`mongosh` will return an error.

## Access Control

The user running `sp.createStreamProcessor()` must have the
`atlasAdmin` role.

## Example

The following example creates a stream processor named `solarDemo`
which ingests data from the `sample_stream_solar` connection. The
processor excludes all documents where the value of the `device_id`
field is `device_8`, passing the rest to a tumbling window with a 10-second
duration. Each window groups the documents it receives, then returns
various useful statistics of each group. The stream processor then
merges these records to `solar_db.solar_coll` over the `mongodb1`
connection.

```json
sp.createStreamProcessor(
  'solarDemo',
  [
    {
      $source: {
```

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
	         "_id": {  "device_id": "$device_id" },
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

## Learn More

- Stream Aggregation
- Manage Stream Processors
