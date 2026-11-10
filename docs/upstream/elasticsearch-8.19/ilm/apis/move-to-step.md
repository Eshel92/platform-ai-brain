<!-- Converted from ilm/apis/move-to-step.asciidoc (AsciiDoc). Includes are inlined. -->

### Move to lifecycle step API

**New API reference**
For the most up-to-date API details, refer to [Index lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ilm).

Triggers execution of a specific step in the lifecycle policy.

#### Request

`POST _ilm/move/<index>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage_ilm`
privileges on the indices being managed to use this API. For more information,
see security-privileges.

#### Description

**Warning:** This operation can result in the loss of data. Manually moving an index
into a specific step executes that step even if it has already been performed.
This is a potentially destructive action and this should be considered an expert
level API.

Manually moves an index into the specified step and executes that step.
You must specify both the current step and the step to be executed in the
body of the request.

The request will fail if the current step does not match the step currently
being executed for the index. This is to prevent the index from being moved from
an unexpected step into the next step.

When specifying the target (`next_step`) to which the index will be moved, either the `name` or both
the `action` and `name` fields are optional. If only the phase is specified, the index will move to
the first step of the first action in the target phase. If the phase and action are specified, the index will move to
the first step of the specified action in the specified phase. Only actions specified in the ILM
policy are considered valid, an index cannot move to a step that is not part of its policy.

#### Path parameters

`<index>`::
  (Required, string) Identifier for the index.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

`timeout`::
(Optional, time units) Period to wait for a response from all relevant nodes in the cluster after updating the cluster metadata.
If no response is received before the timeout expires, the cluster metadata update still applies but the response will indicate that it was not completely acknowledged.
Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Request body

`current_step`::
(Required, object)
**Properties of `current_step`**
`phase`::
(Required, string)
The name of the current phase.
Must match the phase as returned by the explain API.

`action`::
(Required, string)
The name of the current action. 
Must match the action as returned by the explain API.

`name`::
(Required, string)
The name of the current step. 
Must match the step as returned by the explain API.
If ILM encounters a problem while performing an action, 
it halts execution of the policy and transitions to the `ERROR` step.
If you are trying to advance a policy after troubleshooting a failure, 
you specify this `ERROR` step as the current step. 
For more information, see ILM error handling.

`next_step`::
(Required, object)
**Properties of `next_step`**
`phase`::
(Required, string)
The name of the phase that contains the action you want to perform or resume.

`action`::
(Optional, string)
The name action you want to perform or resume. Required if `name` used.

`name`::
(Optional, string)
The name of the step to move to and execute. Required if `action` used.

#### Examples

The following example moves `my-index-000001` from the initial step to the
`forcemerge` step:

```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "warm": {
        "min_age": "10d",
        "actions": {
          "forcemerge": {
            "max_num_segments": 1
          }
        }
      },
      "delete": {
        "min_age": "30d",
        "actions": {
          "delete": {}
        }
      }
    }
  }
}

PUT my-index-000001
{
  "settings": {
    "index.lifecycle.name": "my_policy"
  }
}
```

```console
POST _ilm/move/my-index-000001
{
  "current_step": { <1>
    "phase": "new",
    "action": "complete",
    "name": "complete"
  },
  "next_step": { <2>
    "phase": "warm",
    "action": "forcemerge", <3>
    "name": "forcemerge" <4>
  }
}
```
<1> The step that the index is expected to be in
<2> The step that you want to execute
<3> The optional action to which the index will be moved
<4> The optional step name to which the index will be moved

If the request succeeds, you receive the following result:

```console-result
{
  "acknowledged": true
}
```

The request will fail if the index is not in the `new` phase as specified
by the `current_step`.

The following example pushes `my-index-000001` from the end of hot phase into
the start of warm:

```console
POST _ilm/move/my-index-000001
{
  "current_step": {
    "phase": "hot",
    "action": "complete",
    "name": "complete"
  },
  "next_step": {
    "phase": "warm"
  }
}
```
