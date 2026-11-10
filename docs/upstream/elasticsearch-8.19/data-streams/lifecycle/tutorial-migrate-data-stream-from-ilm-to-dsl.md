<!-- Converted from data-streams/lifecycle/tutorial-migrate-data-stream-from-ilm-to-dsl.asciidoc (AsciiDoc). Includes are inlined. -->

### Tutorial: Migrate ILM managed data stream to data stream lifecycle

In this tutorial we'll look at migrating an existing data stream from Index Lifecycle Management (ILM) to
data stream lifecycle. The existing ILM managed backing indices will continue
to be managed by ILM until they age out and get deleted by ILM; however,
the new backing indices will be managed by data stream lifecycle.
This way, a data stream is gradually migrated away from being managed by ILM to
being managed by data stream lifecycle. As we'll see, ILM and data stream lifecycle
can co-manage a data stream; however, an index can only be managed by one system at
a time.

```console
DELETE _data_stream/dsl-data-stream
DELETE _index_template/dsl-data-stream-template
DELETE _ilm/policy/pre-dsl-ilm-policy
```

#### TL;DR

To migrate a data stream from ILM to data stream lifecycle we'll have to execute
two steps:

1. Update the index template that's backing the data stream to set prefer_ilm
to `false`, and to configure data stream lifecycle.
2. Configure the data stream lifecycle for the _existing_ data stream using
the lifecycle API.

For more details see the migrate to data stream lifecycle section.

#### Setup ILM managed data stream

Let's first create a data stream with two backing indices managed by ILM.
We first create an ILM policy:

```console
PUT _ilm/policy/pre-dsl-ilm-policy
{
  "policy": {
    "phases": {
      "hot": {
        "actions": {
          "rollover": {
            "max_primary_shard_size": "50gb"
          }
        }
      },
      "delete": {
        "min_age": "7d",
        "actions": {
          "delete": {}
        }
      }
    }
  }
}
```

And let's create an index template that'll back the data stream and configures ILM:

```console
PUT _index_template/dsl-data-stream-template
{
  "index_patterns": ["dsl-data-stream*"],
  "data_stream": { },
  "priority": 500,
  "template": {
    "settings": {
      "index.lifecycle.name": "pre-dsl-ilm-policy"
    }
  }
}
```

We'll now index a document targeting `dsl-data-stream` to create the data stream
and we'll also manually rollover the data stream to have another generation index created:

```console
POST dsl-data-stream/_doc?
{
  "@timestamp": "2023-10-18T16:21:15.000Z",
  "message": "192.0.2.42 - - [06/May/2099:16:21:15 +0000] \"GET /images/bg.jpg HTTP/1.0\" 200 24736"
}
```

```console
POST dsl-data-stream/_rollover
```

We'll use the GET _data_stream API to inspect the state of
the data stream:

```console
GET _data_stream/dsl-data-stream
```

Inspecting the response we'll see that both backing indices are managed by ILM
and that the next generation index will also be managed by ILM:

```console-result
{
  "data_streams": [
    {
      "name": "dsl-data-stream",
      "timestamp_field": {
        "name": "@timestamp"
      },
      "indices": [
        {
          "index_name": ".ds-dsl-data-stream-2023.10.19-000001",    <1>
          "index_uuid": "xCEhwsp8Tey0-FLNFYVwSg",
          "prefer_ilm": true,                                       <2>
          "ilm_policy": "pre-dsl-ilm-policy",                       <3>
          "managed_by": "Index Lifecycle Management",               <4>
          "index_mode": "standard"
        },
        {
          "index_name": ".ds-dsl-data-stream-2023.10.19-000002",
          "index_uuid": "PA_JquKGSiKcAKBA8DJ5gw",
          "prefer_ilm": true,
          "ilm_policy": "pre-dsl-ilm-policy",
          "managed_by": "Index Lifecycle Management",
          "index_mode": "standard"
        }
      ],
      "generation": 2,
      "status": "GREEN",
      "template": "dsl-data-stream-template",
      "next_generation_managed_by": "Index Lifecycle Management",   <5>
      "prefer_ilm": true,                                           <6>
      "ilm_policy": "pre-dsl-ilm-policy",                           <7>
      "hidden": false,
      "system": false,
      "allow_custom_routing": false,
      "replicated": false,
      "index_mode": "standard",
      "rollover_on_write": false,
      "settings": {}
    }
  ]
}
```

<1> The name of the backing index.
<2> For each backing index we display the value of the prefer_ilm
configuration which will indicate if ILM takes precedence over data stream lifecycle in case
both systems are configured for an index.
<3> The ILM policy configured for this index.
<4> The system that manages this index (possible values are "Index Lifecycle Management",
"Data stream lifecycle", or "Unmanaged")
<5> The system that will manage the next generation index (the new write index of this
data stream, once the data stream is rolled over). The possible values are
"Index Lifecycle Management", "Data stream lifecycle", or "Unmanaged".
<6> The prefer_ilm value configured in the index template
that's backing the data stream. This value will be configured for all the new backing indices.
If it's not configured in the index template the backing indices will receive the `true`
default value (ILM takes precedence over data stream lifecycle by default as it's
currently richer in features).
<7> The ILM policy configured in the index template that's backing this data
stream (which will be configured on all the new backing indices, as long as it exists
in the index template).

#### Migrate data stream to data stream lifecycle

To migrate the `dsl-data-stream` to data stream lifecycle we'll have to execute
two steps:

1. Update the index template that's backing the data stream to set prefer_ilm
to `false`, and to configure data stream lifecycle.
2. Configure the data stream lifecycle for the _existing_ `dsl-data-stream` using
the lifecycle API.

**Important:** The data stream lifecycle configuration that's added to the index template,
being a data stream configuration, will only apply to **new** data streams.
Our data stream exists already, so even though we added a data stream lifecycle
configuration in the index template it will not be applied to `dsl-data-stream`.

Let's update the index template:

```console
PUT _index_template/dsl-data-stream-template
{
  "index_patterns": ["dsl-data-stream*"],
  "data_stream": { },
  "priority": 500,
  "template": {
    "settings": {
      "index.lifecycle.name": "pre-dsl-ilm-policy",
      "index.lifecycle.prefer_ilm": false             <1>
    },
    "lifecycle": {
      "data_retention": "7d"                          <2>
    }
  }
}
```

<1> The `prefer_ilm` setting will now be configured on the **new** backing indices
(created by rolling over the data stream) such that ILM does _not_ take
precedence over data stream lifecycle.
<2> We're configuring the data stream lifecycle so _new_ data streams will be
managed by data stream lifecycle.

We've now made sure that new data streams will be managed by data stream lifecycle.

Let's update our existing `dsl-data-stream` and configure data stream lifecycle:

```console
PUT _data_stream/dsl-data-stream/_lifecycle
{
    "data_retention": "7d"
}
```

We can inspect the data stream to check that the next generation will indeed be
managed by data stream lifecycle:

```console
GET _data_stream/dsl-data-stream
```

```console-result
{
  "data_streams": [
    {
      "name": "dsl-data-stream",
      "timestamp_field": {
        "name": "@timestamp"
      },
      "indices": [
        {
          "index_name": ".ds-dsl-data-stream-2023.10.19-000001",
          "index_uuid": "xCEhwsp8Tey0-FLNFYVwSg",
          "prefer_ilm": true,
          "ilm_policy": "pre-dsl-ilm-policy",
          "managed_by": "Index Lifecycle Management",               <1>
          "index_mode": "standard"
        },
        {
          "index_name": ".ds-dsl-data-stream-2023.10.19-000002",
          "index_uuid": "PA_JquKGSiKcAKBA8DJ5gw",
          "prefer_ilm": true,
          "ilm_policy": "pre-dsl-ilm-policy",
          "managed_by": "Index Lifecycle Management",               <2>
          "index_mode": "standard"
        }
      ],
      "generation": 2,
      "status": "GREEN",
      "template": "dsl-data-stream-template",
      "lifecycle": {
        "enabled": true,
        "data_retention": "7d",
        "effective_retention": "7d",
        "retention_determined_by": "data_stream_configuration"
      },
      "ilm_policy": "pre-dsl-ilm-policy",
      "next_generation_managed_by": "Data stream lifecycle",         <3>
      "prefer_ilm": false,                                           <4>
      "hidden": false,
      "system": false,
      "allow_custom_routing": false,
      "replicated": false,
      "index_mode": "standard",
      "rollover_on_write": false,
      "settings": {}
    }
  ]
}
```

<1> The existing backing index will continue to be managed by ILM
<2> The existing backing index will continue to be managed by ILM
<3> The next generation index will be managed by Data stream lifecycle
<4> The `prefer_ilm` setting value we configured in the index template is reflected
and will be configured accordingly for new backing indices.

We'll now rollover the data stream to see the new generation index being managed by
data stream lifecycle:

```console
POST dsl-data-stream/_rollover
```

```console
GET _data_stream/dsl-data-stream
```

```console-result
{
  "data_streams": [
    {
      "name": "dsl-data-stream",
      "timestamp_field": {
        "name": "@timestamp"
      },
      "indices": [
        {
          "index_name": ".ds-dsl-data-stream-2023.10.19-000001",
          "index_uuid": "xCEhwsp8Tey0-FLNFYVwSg",
          "prefer_ilm": true,
          "ilm_policy": "pre-dsl-ilm-policy",
          "index_mode": "standard",
          "managed_by": "Index Lifecycle Management"                <1>
        },
        {
          "index_name": ".ds-dsl-data-stream-2023.10.19-000002",
          "index_uuid": "PA_JquKGSiKcAKBA8DJ5gw",
          "prefer_ilm": true,
          "ilm_policy": "pre-dsl-ilm-policy",
          "index_mode": "standard",
          "managed_by": "Index Lifecycle Management"                <2>
        },
        {
          "index_name": ".ds-dsl-data-stream-2023.10.19-000003",
          "index_uuid": "PA_JquKGSiKcAKBA8abcd1",
          "prefer_ilm": false,                                      <3>
          "ilm_policy": "pre-dsl-ilm-policy",
          "index_mode": "standard",
          "managed_by": "Data stream lifecycle"                     <4>
        }
      ],
      "generation": 3,
      "status": "GREEN",
      "template": "dsl-data-stream-template",
      "lifecycle": {
        "enabled": true,
        "data_retention": "7d",
        "effective_retention": "7d",
        "retention_determined_by": "data_stream_configuration"
      },
      "ilm_policy": "pre-dsl-ilm-policy",
      "next_generation_managed_by": "Data stream lifecycle",
      "prefer_ilm": false,
      "hidden": false,
      "system": false,
      "allow_custom_routing": false,
      "replicated": false,
      "index_mode": "standard",
      "rollover_on_write": false,
      "settings": {}
    }
  ]
}
```

<1> The backing indices that existed before rollover will continue to be managed by ILM
<2> The backing indices that existed before rollover will continue to be managed by ILM
<3> The new write index received the `false` value for the `prefer_ilm` setting, as we configured
in the index template
<4> The new write index is managed by `Data stream lifecycle`

#### Migrate data stream back to ILM

We can easily change this data stream to be managed by ILM because we didn't remove
the ILM policy when we <<update-index-template-for-dsl, updated
the index template>>.

We can achieve this in two ways:

1. Delete the lifecycle from the data streams
2. Disable data stream lifecycle by configuring the `enabled` flag to `false`.

Let's implement option 2 and disable the data stream lifecycle:

```console
PUT _data_stream/dsl-data-stream/_lifecycle
{
    "data_retention": "7d",
    "enabled": false <1>
}
```
<1> The `enabled` flag can be ommitted and defaults to `true` however, here we
explicitly configure it to `false`
Let's check the state of the data stream:

```console
GET _data_stream/dsl-data-stream
```

```console-result
{
  "data_streams": [
    {
      "name": "dsl-data-stream",
      "timestamp_field": {
        "name": "@timestamp"
      },
      "indices": [
        {
          "index_name": ".ds-dsl-data-stream-2023.10.19-000001",
          "index_uuid": "xCEhwsp8Tey0-FLNFYVwSg",
          "prefer_ilm": true,
          "ilm_policy": "pre-dsl-ilm-policy",
          "index_mode": "standard",
          "managed_by": "Index Lifecycle Management"
        },
        {
          "index_name": ".ds-dsl-data-stream-2023.10.19-000002",
          "index_uuid": "PA_JquKGSiKcAKBA8DJ5gw",
          "prefer_ilm": true,
          "ilm_policy": "pre-dsl-ilm-policy",
          "index_mode": "standard",
          "managed_by": "Index Lifecycle Management"
        },
        {
          "index_name": ".ds-dsl-data-stream-2023.10.19-000003",
          "index_uuid": "PA_JquKGSiKcAKBA8abcd1",
          "prefer_ilm": false,
          "ilm_policy": "pre-dsl-ilm-policy",
          "index_mode": "standard",
          "managed_by": "Index Lifecycle Management"                <1>
        }
      ],
      "generation": 3,
      "status": "GREEN",
      "template": "dsl-data-stream-template",
      "lifecycle": {
        "enabled": false,                                          <2>
        "data_retention": "7d"
      },
      "ilm_policy": "pre-dsl-ilm-policy",
      "next_generation_managed_by": "Index Lifecycle Management",  <3>
      "prefer_ilm": false,
      "hidden": false,
      "system": false,
      "allow_custom_routing": false,
      "replicated": false,
      "index_mode": "standard",
      "rollover_on_write": false,
      "settings": {}
    }
  ]
}
```
<1> The write index is now managed by ILM
<2> The `lifecycle` configured on the data stream is now disabled.
<3> The next write index will be managed by ILM

Had we removed the ILM policy from the index template when we updated
it, the write index of the data stream will now be `Unmanaged` because the index
wouldn't have the ILM policy configured to fallback onto.
