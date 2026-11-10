<!-- Converted from ilm/error-handling.asciidoc (AsciiDoc). Includes are inlined. -->

## Troubleshooting index lifecycle management errors

When ILM executes a lifecycle policy, it's possible for errors to occur
while performing the necessary index operations for a step. 
When this happens, ILM moves the index to an `ERROR` step. 
If ILM cannot resolve the error automatically, execution is halted  
until you resolve the underlying issues with the policy, index, or cluster.

See [this video](https://www.youtube.com/watch?v=VCIqkji3IwY) 
for a walkthrough of troubleshooting current ILM health issues, and [this video](https://www.youtube.com/watch?v=onrnnwjYWSQ)
for a walkthrough of troubleshooting historical ILM issues.

For example, you might have a `shrink-index` policy that shrinks an index to four shards once it
is at least five days old: 

```console
PUT _ilm/policy/shrink-index
{
  "policy": {
    "phases": {
      "warm": {
        "min_age": "5d",
        "actions": {
          "shrink": {
            "number_of_shards": 4
          }
        }
      }
    }
  }
}
```

There is nothing that prevents you from applying the `shrink-index` policy to a new
index that has only two shards:

```console
PUT /my-index-000001
{
  "settings": {
    "index.number_of_shards": 2,
    "index.lifecycle.name": "shrink-index"
  }
}
```

After five days, ILM attempts to shrink `my-index-000001` from two shards to four shards.
Because the shrink action cannot _increase_ the number of shards, this operation fails 
and ILM moves `my-index-000001` to the `ERROR` step. 

You can use the ILM Explain API to get information about
what went wrong: 

```console
GET /my-index-000001/_ilm/explain
```

Which returns the following information:

```console-result
{
  "indices" : {
    "my-index-000001" : {
      "index" : "my-index-000001",
      "managed" : true,                         
      "index_creation_date_millis" : 1541717265865,
      "time_since_index_creation": "5.1d",
      "policy" : "shrink-index",                <1>
      "lifecycle_date_millis" : 1541717265865,
      "age": "5.1d",                            <2>
      "phase" : "warm",                         <3>
      "phase_time_millis" : 1541717272601,
      "action" : "shrink",                      <4>
      "action_time_millis" : 1541717272601,
      "step" : "ERROR",                         <5>
      "step_time_millis" : 1541717272688,
      "failed_step" : "shrink",                 <6>
      "step_info" : {
        "type" : "illegal_argument_exception",  <7>
        "reason" : "the number of target shards [4] must be less that the number of source shards [2]"
      },
      "phase_execution" : {
        "policy" : "shrink-index",
        "phase_definition" : {                  <8>
          "min_age" : "5d",
          "actions" : {
            "shrink" : {
              "number_of_shards" : 4
            }
          }
        },
        "version" : 1,
        "modified_date_in_millis" : 1541717264230
      }
    }
  }
}
```

<1> The policy being used to manage the index: `shrink-index`
<2> The index age: 5.1 days
<3> The phase the index is currently in: `warm`
<4> The current action: `shrink`
<5> The step the index is currently in: `ERROR`
<6> The step that failed to execute: `shrink`
<7> The type of error and a description of that error.
<8> The definition of the current phase from the `shrink-index` policy

To resolve this, you could update the policy to shrink the index to a single shard after 5 days:

```console
PUT _ilm/policy/shrink-index
{
  "policy": {
    "phases": {
      "warm": {
        "min_age": "5d",
        "actions": {
          "shrink": {
            "number_of_shards": 1
          }
        }
      }
    }
  }
}
```

### Retrying failed lifecycle policy steps

Once you fix the problem that put an index in the `ERROR` step, 
you might need to explicitly tell ILM to retry the step:

```console
POST /my-index-000001/_ilm/retry
```

ILM subsequently attempts to re-run the step that failed. 
You can use the ILM Explain API to monitor the progress.

### Common ILM setting issues

#### How `min_age` is calculated

When setting up an ILM policy or automating rollover with ILM, be aware that `min_age` can be relative to either the rollover time or the index creation time.

If you use ILM rollover, `min_age` is calculated relative to the time the index was rolled over. This is because the rollover API generates a new index and updates the `age` of the previous index to reflect the rollover time. If the index hasn't been rolled over, then the `age` is the same as the `creation_date` for the index.

You can override how `min_age` is calculated using the `index.lifecycle.origination_date` and `index.lifecycle.parse_origination_date` ILM settings.

### Common ILM errors

Here's how to resolve the most common errors reported in the `ERROR` step.

**Tip:** Problems with rollover aliases are a common cause of errors.
Consider using data streams instead of managing rollover with aliases.

#### Rollover alias [x] can point to multiple indices, found duplicated alias [x] in index template [z]

The target rollover alias is specified in an index template's `index.lifecycle.rollover_alias` setting.
You need to explicitly configure this alias _one time_ when you
bootstrap the initial index.
The rollover action then manages setting and updating the alias to
roll over to each subsequent index.

Do not explicitly configure this same alias in the aliases section of an index template.

See this [resolving `duplicate alias` video](https://www.youtube.com/watch?v=Ww5POq4zZtY) for an example troubleshooting walkthrough.

#### index.lifecycle.rollover_alias [x] does not point to index [y]

Either the index is using the wrong alias or the alias does not exist.

Check the `index.lifecycle.rollover_alias` index setting.
To see what aliases are configured, use _cat/aliases.

See this [resolving `not point to index` video](https://www.youtube.com/watch?v=NKSe67x7aw8) for an example troubleshooting walkthrough.

#### Setting [index.lifecycle.rollover_alias] for index [y] is empty or not defined

The `index.lifecycle.rollover_alias` setting must be configured for the rollover action to work.

Update the index settings to set `index.lifecycle.rollover_alias`.

See this [resolving `empty or not defined` video](https://www.youtube.com/watch?v=LRpMC2GS_FQ) for an example troubleshooting walkthrough.

#### Alias [x] has more than one write index [y,z]

Only one index can be designated as the write index for a particular alias.

Use the aliases API to set `is_write_index:false` for all but one index.

See this [resolving `more than one write index` video](https://www.youtube.com/watch?v=jCUvZCT5Hm4) for an example troubleshooting walkthrough.

#### index name [x] does not match pattern ^.*-\d+

The index name must match the regex pattern `^.*-\d+` for the rollover action to work.
The most common problem is that the index name does not contain trailing digits.
For example, `my-index` does not match the pattern requirement.

Append a numeric value to the index name, for example `my-index-000001`.

See this [resolving `does not match pattern` video](https://www.youtube.com/watch?v=9sp1zF6iL00) for an example troubleshooting walkthrough.

#### CircuitBreakingException: [x] data too large, data for [y]

This indicates that the cluster is hitting resource limits.

Before continuing to set up ILM, you'll need to take steps to alleviate the resource issues.
For more information, see circuit-breaker-errors.

#### High disk watermark [x] exceeded on [y]

This indicates that the cluster is running out of disk space.
This can happen when you don't have index lifecycle management set up to roll over from hot to warm nodes.
For more information, see Fix watermark errors.

#### security_exception: action [<action-name>] is unauthorized for user [<user-name>] with roles [<role-name>], this action is granted by the index privileges [manage_follow_index,manage,all]

This indicates the ILM action cannot be executed because the user that ILM uses to perform the action doesn’t have the correct privileges.
ILM actions are run as though they are performed by the last user who modified the policy with the privileges that user had at that time.
The account used to create or modify the policy must have permissions to perform all operations that are part of that policy.
