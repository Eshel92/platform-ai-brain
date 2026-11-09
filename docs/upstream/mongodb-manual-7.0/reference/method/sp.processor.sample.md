<!-- Converted from reference/method/sp.processor.sample.txt (reStructuredText). Includes are inlined. -->

# sp.processor.sample() (mongosh method)

## Definition

**`sp.processor.sample()`**

Returns arrays of sampled results from a currently running
Stream Processor on
the current Stream Processing Workspace.

You can only invoke this command while connected to a stream
processing workspace.

This command requires `mongosh` version ≥ 2.0.

## Compatibility

This method is supported in Atlas Stream Processing Workspaces.

## Syntax

   
The `sp.processor.sample()` method has the following syntax:

```json
sp.processor.sample()
```

## Command Fields

`sp.processor.sample()` takes no fields.

## Behavior

`sp.processor.sample()` returns arrays of sampled results
from the named, currently running stream processor to `STDOUT`. This
command runs continuously until you cancel it using `CTRL-C`, or until
the returned samples cumulatively reach `40 MB`.

## Access Control

The user running `sp.processor.sample()` must have the
`atlasAdmin` role.

## Example

The following example shows an expected response from calling `sp.solarDemo.sample()`
to sample from a stream processor called `solarDemo`:

```sh
sp.solarDemo.sample()
```

Output:

```json
{
```

	_id: {
	  device_id: 'device_5'
	},
	max_temp: 8,
	max_watts: 66,
	min_watts: 66,
	avg_watts: 66,
	median_watts: 66
      }
      {
	_id: {
	  device_id: 'device_0'
	},
	max_temp: 18,
	max_watts: 210,
	min_watts: 68,
	avg_watts: 157,
	median_watts: 193
      }
      {
	_id: {
	  device_id: 'device_10'
	},
	max_temp: 21,
	max_watts: 128,
	min_watts: 4,
	avg_watts: 66,
	median_watts: 4
      }
      {
	_id: {
	  device_id: 'device_9'
	},
	max_temp: 10,
	max_watts: 227,
	min_watts: 66,
	avg_watts: 131.4,
	median_watts: 108
      }

## Learn More

- Manage Stream Processors
