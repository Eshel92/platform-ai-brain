<!-- Converted from reference/method/sp.listStreamProcessors.txt (reStructuredText). Includes are inlined. -->

# sp.listStreamProcessors() (mongosh method)

## Definition

**`sp.listStreamProcessors()`**

Returns documents for each named
Stream Processor on
the current Stream Processing Workspace. Each
document provides descriptive information including the name,
current state, and pipeline of a stream processor.

You can only invoke this command while connected to a stream
processing workspace.

This command requires `mongosh` version ≥ 2.0.

## Compatibility

This method is supported in Atlas Stream Processing Workspaces.

## Syntax

   
The `sp.listStreamProcessors()` method has the following syntax:

```json
sp.listStreamProcessors(
  {
   <filter>
  }
)
```

## Command Fields

`sp.listStreamProcessors()` takes these fields:

| Field | Type | Necessity | Description |
|---|---|---|---|
| `filter` | document | Optional | Document specifying which fields to filter stream processors on. If you provide a filter, the command will only return those processors which match the values for all the fields you specify. |

## Behavior

`sp.listStreamProcessors()` returns documents describing all of
the named stream processors on the current stream processing workspace
to `STDOUT`. 

## Access Control

The user running `sp.listStreamProcessors()` must have the
`atlasAdmin` role.

## Example

The following example shows an expected response from
`sp.listStreamProcessors()` when the command is called without any
filter:

```sh
sp.listStreamProcessors()
```

Output:

```json
{
```

	id: '0135',
	name: "proc01",
	last_modified: ISODate("2023-03-20T20:15:54.601Z"),
	state: "RUNNING",
	error_msg: '',
	pipeline: [
	  {
	    $source: {
	      connectionName: "myKafka", 
	      topic: "stuff"
	    }
	  },
	  {
	    $match: { 
	      temperature: 46 
	    }
	  },
	  {
	    $emit: {
	      connectionName: "mySink",
	      topic: "output",
	    }  
	  }
	],
	lastStateChange: ISODate("2023-03-20T20:15:59.442Z")
      },
      {   
	id: '0218',
	name: "proc02",
	last_modified: ISODate("2023-03-21T20:17:33.601Z"),
	state: "STOPPED",
	error_msg: '',
	pipeline: [
	  {
	    $source: {
	      connectionName: "myKafka", 
	      topic: "things"
	    }
	  },
	  {
	    $match: { 
	      temperature: 41 
	    }
	  },
	  {
	    $emit: {
	      connectionName: "mySink",
	      topic: "results",
	    }  
	  }
	],
	lastStateChange: ISODate("2023-03-21T20:18:26.139Z")
      }

The following example shows an expected response if you invoke
`sp.listStreamProcessors()` filtering for only those stream
processors with a `state` of `running`.

```sh
sp.listStreamProcessors({"state": "running"})
```

Output:

```json
{
```

	id: '0135',
	name: "proc01",
	last_modified: ISODate("2023-03-20T20:15:54.601Z"),
	state: "RUNNING",
	error_msg: '',
	pipeline: [
	  {
	    $source: {
	      connectionName: "myKafka", 
	      topic: "stuff"
	    }
	  },
	  {
	    $match: { 
	      temperature: 46 
	    }
	  },
	  {
	    $emit: {
	      connectionName: "mySink",
	      topic: "output",
	    }  
	  }
	],
	lastStateChange: ISODate("2023-03-20T20:15:59.442Z")
      }

## Learn More

- Manage Stream Processors
