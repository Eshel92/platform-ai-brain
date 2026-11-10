<!-- Converted from ilm/set-up-lifecycle-policy.asciidoc (AsciiDoc). Includes are inlined. -->

## Configure a lifecycle policy

For ILM to manage an index, a valid policy 
must be specified in the `index.lifecycle.name` index setting. 

To configure a lifecycle policy for rolling indices, 
you create the policy and add it to the index template.

To use a policy to manage an index that doesn't roll over,
you can specify a lifecycle policy when you create the index,
or apply a policy directly to an existing index.

ILM policies are stored in the global cluster state and can be included in snapshots
by setting `include_global_state` to `true` when you take the snapshot. 
When the snapshot is restored, all of the policies in the global state are restored and 
any local policies with the same names are overwritten.

**Important:** When you enable index lifecycle management for Beats or the Logstash Elasticsearch output plugin, 
the necessary policies and configuration changes are applied automatically. 
You can modify the default policies, but you do not need to explicitly configure a policy or
bootstrap an initial index.

### Create lifecycle policy

To create a lifecycle policy from Kibana, open the menu and go to *Stack
Management > Index Lifecycle Policies*. Click *Create policy*.

image:images/ilm/create-policy.png[Create policy page]

You specify the lifecycle phases for the policy and the actions to perform in each phase.

The create or update policy API is invoked to add the
policy to the Elasticsearch cluster.

**API example**
```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "hot": {
        "actions": {
          "rollover": {
            "max_primary_shard_size": "25GB" <1>
          }
        }
      },
      "delete": {
        "min_age": "30d",
        "actions": {
          "delete": {} <2>
        }
      }
    }
  }
}
```

<1> Roll over the index when it reaches 25GB in size
<2> Delete the index 30 days after rollover

**Important:** The rollover action implicitly always rolls over a data stream or alias if one or more shards contain
200000000 or more documents. Normally a shard will reach 25GB long before it reaches 200M documents,
but this isn't the case for space efficient data sets. Search performance will very likely suffer
if a shard contains more than 200M documents. This is the reason of the builtin limit.

### Apply lifecycle policy with an index template

To use a policy that triggers the rollover action, 
you need to configure the policy in the index template used to create each new index.
You specify the name of the policy and the alias used to reference the rolling indices.

**Tip:** An `index.lifecycle.rollover_alias` setting is only required if using index lifecycle management with an alias. It is unnecessary when using Data Streams.

You can use the Kibana Create template wizard to create a template. To access the
wizard, open the menu and go to *Stack Management > Index Management*. In the
*Index Templates* tab, click *Create template*.

image:images/ilm/create-template-wizard-my_template.png[Create template page]

The wizard invokes the <<indices-put-template,create or update index template
API>> to add templates to a cluster.

**API example**
```console
PUT _index_template/my_template
{
  "index_patterns": ["test-*"], <1>
  "template": {
    "settings": {
      "number_of_shards": 1,
      "number_of_replicas": 1,
      "index.lifecycle.name": "my_policy", <2>
      "index.lifecycle.rollover_alias": "test-alias" <3>
    }
  }
}
```

<1> Use this template for all new indices whose names begin with `test-`
<2> Apply `my_policy` to new indices created with this template
<3> Define an index alias for referencing indices managed by `my_policy`

```console
DELETE _index_template/my_template
```

#### Create an initial managed index

When you set up policies for your own rolling indices, if you are not using the recommended
data streams, you need to manually create the first index managed by a policy and
designate it as the write index.

**Important:** When you enable index lifecycle management for Beats or the Logstash Elasticsearch output plugin, 
the necessary policies and configuration changes are applied automatically. 
You can modify the default policies, but you do not need to explicitly configure a policy or
bootstrap an initial index.

The name of the index must match the pattern defined in the index template and end with a number.
This number is incremented to generate the name of indices created by the rollover action.

For example, the following request creates the `test-00001` index. 
Because it matches the index pattern specified in `my_template`, 
Elasticsearch automatically applies the settings from that template.

```console
PUT test-000001
{
  "aliases": {
    "test-alias":{
      "is_write_index": true <1>
    }
  }
}
```

<1> Set this initial index to be the write index for this alias.

Now you can start indexing data to the rollover alias specified in the lifecycle policy. 
With the sample `my_policy` policy, the rollover action is triggered once the initial
index exceeds 25GB. 
ILM then creates a new index that becomes the write index for the `test-alias`.

### Apply lifecycle policy manually

You can specify a policy when you create an index or
apply a policy to an existing index through Kibana Management or
the update settings API. 
When you apply a policy, ILM immediately starts managing the index.

**Important:** Do not manually apply a policy that uses the rollover action.
Policies that use rollover must be applied by the index template. 
Otherwise, the policy is not carried forward when the rollover action creates a new index.

The `index.lifecycle.name` setting specifies an index's policy.

**API example**
```console
PUT test-index
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1,
    "index.lifecycle.name": "my_policy" <1>
  }
}
```
<1> Sets the lifecycle policy for the index.

#### Apply a policy to multiple indices

You can apply the same policy to multiple indices by using wildcards in the index name 
when you call the update settings API.

**Warning:** Be careful that you don't inadvertently match indices that you don't want to modify.

```console
PUT _index_template/mylogs_template
{
  "index_patterns": [
    "mylogs-*"
  ],
  "template": {
    "settings": {
      "number_of_shards": 1,
      "number_of_replicas": 1
    },
    "mappings": {
      "properties": {
        "message": {
          "type": "text"
        },
        "@timestamp": {
          "type": "date"
        }
      }
    }
  }
}
```

```console
POST mylogs-pre-ilm-2019.06.24/_doc
{
  "@timestamp": "2019-06-24T10:34:00",
  "message": "this is one log message"
}
```

```console
POST mylogs-pre-ilm-2019.06.25/_doc
{
  "@timestamp": "2019-06-25T17:42:00",
  "message": "this is another log message"
}
```

```console
DELETE _index_template/mylogs_template
```

```console
PUT mylogs-pre-ilm*/_settings <1>
{
  "index": {
    "lifecycle": {
      "name": "mylogs_policy_existing"
    }
  }
}
```

<1> Updates all indices with names that start with `mylogs-pre-ilm`

#### Switch lifecycle policies

To switch an index's lifecycle policy, follow these steps:

. Remove the existing policy using the remove policy API.
Target a data stream or alias to remove the policies of all its indices.
```console
POST logs-my_app-default/_ilm/remove
```

. The remove policy API removes all ILM metadata from the index and
doesn't consider the index's lifecycle status. This can leave indices in an
undesired state.
For example, the `forcemerge` action temporarily closes an
index before reopening it. Removing an index's ILM policy during a
`forcemerge` can leave the index closed indefinitely.

After policy removal, use the get index API to check an
index's state . Target a data stream or alias to get the state of all its
indices.

```console
GET logs-my_app-default
```

You can then change the index as needed. For example, you can re-open any
closed indices using the open index API.

```console
POST logs-my_app-default/_open
```

. Assign a new policy using the update settings API.
Target a data stream or alias to assign a policy to all its indices.
**Warning:** Don't assign a new policy without first removing the existing policy.
This can cause phase execution to silently fail.

```console
PUT logs-my_app-default/_settings
{
  "index": {
    "lifecycle": {
      "name": "new-lifecycle-policy"
    }
  }
}
```
