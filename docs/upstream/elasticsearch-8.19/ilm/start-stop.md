<!-- Converted from ilm/start-stop.asciidoc (AsciiDoc). Includes are inlined. -->

## Start and stop index lifecycle management

By default, the ILM service is in the `RUNNING` state and manages 
all indices that have lifecycle policies. 

You can stop index lifecycle management to suspend management operations for all indices.
For example, you might stop index lifecycle management when performing scheduled maintenance or making
changes to the cluster that could impact the execution of ILM actions.

**Important:** When you stop ILM, SLM 
operations are also suspended. 
No snapshots will be taken as scheduled until you restart ILM.
In-progress snapshots are not affected.

### Get ILM status

To see the current status of the ILM service, use the Get Status API:

```console
GET _ilm/status
```

Under normal operation, the response shows ILM is `RUNNING`:

```console-result
{
  "operation_mode": "RUNNING"
}
```

### Stop ILM

To stop the ILM service and pause execution of all lifecycle policies, 
use the Stop API:

```console
POST _ilm/stop
```

ILM service runs all policies to a point where it is safe to stop. 
While the ILM service is shutting down, 
the status API shows ILM is in the `STOPPING` mode:

```console-result
{
  "operation_mode": "STOPPING"
}
```

Once all policies are at a safe stopping point, ILM moves into the `STOPPED` mode:

```console-result
{
  "operation_mode": "STOPPED"
}
```

### Start ILM

To restart ILM and resume executing policies, use the Start API.
This puts the  ILM service in the `RUNNING` state and 
ILM begins executing policies from where it left off.

```console
POST _ilm/start
```
