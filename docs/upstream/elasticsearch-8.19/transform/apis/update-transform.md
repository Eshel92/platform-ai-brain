<!-- Converted from transform/apis/update-transform.asciidoc (AsciiDoc). Includes are inlined. -->

# Update transform API

**New API reference**
For the most up-to-date API details, refer to [Transform APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-transform).

Updates certain properties of a transform.

## Request

`POST _transform/<transform_id>/_update`

## Prerequisites

Requires the following privileges:

* cluster: `manage_transform` (the `transform_admin` built-in role grants this
  privilege)
* source indices: `read`, `view_index_metadata`
* destination index: `read`, `index`. If a `retention_policy` is configured, `delete` index privilege is
also required.

## Description

This API updates an existing transform. The list of properties that you can
update is a subset of the list that you can define when you create a transform.

When the transform is updated, a series of validations occur to ensure its
success. You can use the `defer_validation` parameter to skip these checks.

All updated properties except description do not take effect until after the
transform starts the next checkpoint. This is so there is data consistency in
each checkpoint.

**Important:**

* Your transform remembers which roles the user who updated it had at the time
of update and runs with those privileges. If you provide
secondary authorization headers, those
credentials are used instead.
* You must use Kibana or this API to update a transform. Directly updating any
transform internal, system, or hidden indices is not supported and may cause
permanent failure.

## Path parameters

`<transform_id>`::
(Required, string)
Identifier for the transform.

## Query parameters

`defer_validation`::
(Optional, Boolean) When `true`, deferrable validations are not run. This
behavior may be desired if the source index does not exist until after the
transform is updated.

`timeout`::
(Optional, time)
Period to wait for a response. If no response is received before the timeout
expires, the request fails and returns an error. Defaults to `30s`.

## Request body

`description`::
  (Optional, string) Free text description of the transform.

`dest`::
(Optional, object)
The destination for the transform.
**Properties of `dest`**

`index`:::
(Required, string)
The _destination index_ for the transform.

In the case of a `pivot` transform, the mappings of the destination
index are deduced based on the source fields when possible. If alternate
mappings are required, use the Create index API
prior to starting the transform.

In the case of a `latest` transform, the mappings are never deduced. If dynamic
mappings for the destination index are undesirable, use the
Create index API prior to starting the transform.
`aliases`:::
(Optional, array of objects)
The aliases that the destination index for the transform should have.
Aliases are manipulated using the stored credentials of the transform, which means the secondary credentials supplied
at creation time (if both primary and secondary credentials are specified).

The destination index is added to the aliases regardless whether the destination
index was created by the transform or pre-created by the user.
**Properties of `aliases`**
=====

`alias`::::
(Required, string)
The name of the alias.
`move_on_creation`::::
(Optional, boolean)
Whether or not the destination index should be the **only** index in this alias.
If `true`, all the other indices will be removed from this alias before adding the destination index to this alias.
Defaults to `false`.
=====

`pipeline`:::
(Optional, string)
The unique identifier for an ingest pipeline.

`frequency`::
(Optional, time units)
The interval between checks for changes in the source indices when the
transform is running continuously. The minimum value is `1s` and the maximum
is `1h`. The default value is `1m`.
`_meta`::
(Optional, object)
Defines optional transform metadata.

`retention_policy`::
(Optional, object)
Defines a retention policy for the transform. Data that meets the defined
criteria is deleted from the destination index.
**Properties of `retention_policy`**
`time`:::
(Required, object)
Specifies that the transform uses a time field to set the retention policy.
Data is deleted if `time.field` for the retention policy exists and contains
data older than `max.age`.
**Properties of `time`**
=====
`field`:::
(Required, string)
The date field that is used to calculate the age of the document. Set
`time.field` to an existing date field.
`max_age`:::
(Required, time units)
Specifies the maximum age of a document in the destination index. Documents that
are older than the configured value are removed from the destination index.
=====

`settings`::
(Optional, object)
Defines optional transform settings.
**Properties of `settings`**
`align_checkpoints`:::
(Optional, boolean)
Specifies whether the transform checkpoint ranges should be optimized for performance.
Such optimization can align checkpoint ranges with date histogram interval when date histogram
is specified as a group source in the transform config. As an effect, less document updates in the
destination index will be performed thus improving overall performance.
The default value is `true`, which means the checkpoint ranges will be optimized if possible.
`dates_as_epoch_millis`:::
(Optional, boolean)
Defines if dates in the output should be written as ISO formatted string (default)
or as millis since epoch. `epoch_millis` has been the default for transforms created
before version `7.11`. For compatible output set this to `true`.
The default value is `false`.
`deduce_mappings`:::
(Optional, boolean)
Specifies whether the transform should deduce the destination index mappings from the transform config.
The default value is `true`, which means the destination index mappings will be deduced if possible.
`docs_per_second`:::
(Optional, float)
Specifies a limit on the number of input documents per second. This setting
throttles the transform by adding a wait time between search requests. The
default value is `null`, which disables throttling.
`max_page_search_size`:::
(Optional, integer)
Defines the initial page size to use for the composite aggregation for each
checkpoint. If circuit breaker exceptions occur, the page size is dynamically
adjusted to a lower value. The minimum value is `10` and the maximum is `65,536`.
The default value is `500`.
`num_failure_retries`:::
(Optional, integer)
Defines the number of retries on a recoverable failure before the transform task is marked as `failed`.
The minimum value is `0` and the maximum is `100`.
`-1` can be used to denote infinity. In this case, the transform never gives up on retrying a recoverable failure.
The default value is the cluster-level setting `num_transform_failure_retries`.
`unattended`:::
(Optional, boolean)
If `true`, the transform runs in unattended mode. In unattended mode, the
transform retries indefinitely in case of an error which means the transform
never fails. Setting the number of retries other than infinite fails in
validation. Defaults to `false`.

`source`::
(Optional, object)
The source of the data for the transform.
**Properties of `source`**

`index`:::
(Required, string or array)
The _source indices_ for the transform. It can be a single index, an index
pattern (for example, `"my-index-*"`), an array of indices (for example,
`["my-index-000001", "my-index-000002"]`), or an array of index patterns (for
example, `["my-index-*", "my-other-index-*"]`. For remote indices use the syntax
`"remote_name:index_name"`.
**Note:** If any indices are in remote clusters then the master node and at least
one transform node must have the `remote_cluster_client` node role.
`query`:::
(Optional, object)
A query clause that retrieves a subset of data from the source index. See
query-dsl.

`sync`::
(Optional, object)
Defines the properties transforms require to run continuously.
**Note:** You can update these properties only if it is a continuous transform. You
cannot change a batch transform into a continuous transform or vice versa.
Instead, clone the transform in Kibana and add or remove the `sync` property.

**Properties of `sync`**

`time`:::
(Required, object)
Specifies that the transform uses a time field to synchronize the source and
destination indices.
**Properties of `time`**
=====

`delay`::::
(Optional, time units)
The time delay between the current time and the latest input data time. The
default value is `60s`.
`field`::::
(Required, string)
The date field that is used to identify new documents in the source.
**Tip:** In general, it’s a good idea to use a field that contains the
ingest timestamp. If you use a different field,
you might need to set the `delay` such that it accounts for data transmission
delays.

=====

## Examples

```console
POST _transform/simple-kibana-ecomm-pivot/_update
{
  "source": {
    "index": "kibana_sample_data_ecommerce",
    "query": {
      "term": {
        "geoip.continent_name": {
          "value": "Asia"
        }
      }
    }
  },
  "description": "Maximum priced ecommerce data by customer_id in Asia",
  "dest": {
    "index": "kibana_sample_data_ecommerce_transform_v2",
    "pipeline": "add_timestamp_pipeline"
  },
  "frequency": "15m",
  "sync": {
    "time": {
      "field": "order_date",
      "delay": "120s"
    }
  }
}
```

When the transform is updated, you receive the updated configuration:

```console-result
{
  "id" : "simple-kibana-ecomm-pivot",
  "authorization" : {
    "roles" : [
      "superuser"
    ]
  },
  "version" : "8.4.0",
  "create_time" : 1656113450613,
  "source" : {
    "index" : [
      "kibana_sample_data_ecommerce"
    ],
    "query" : {
      "term" : {
        "geoip.continent_name" : {
          "value" : "Asia"
        }
      }
    }
  },
  "dest" : {
    "index" : "kibana_sample_data_ecommerce_transform_v2",
    "pipeline" : "add_timestamp_pipeline"
  },
  "frequency" : "15m",
  "sync" : {
    "time" : {
      "field" : "order_date",
      "delay" : "120s"
    }
  },
  "pivot" : {
    "group_by" : {
      "customer_id" : {
        "terms" : {
          "field" : "customer_id"
        }
      }
    },
    "aggregations" : {
      "max_price" : {
        "max" : {
          "field" : "taxful_total_price"
        }
      }
    }
  },
  "description" : "Maximum priced ecommerce data by customer_id in Asia",
  "settings" : { }
}
```
