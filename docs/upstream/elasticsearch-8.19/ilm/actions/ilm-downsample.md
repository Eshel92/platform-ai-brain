<!-- Converted from ilm/actions/ilm-downsample.asciidoc (AsciiDoc). Includes are inlined. -->

### Downsample

Phases allowed: hot, warm, cold.

Aggregates a time series (TSDS) index and stores
pre-computed statistical summaries (`min`, `max`, `sum`, `value_count` and
`avg`) for each metric field grouped by a configured time interval. For example,
a TSDS index that contains metrics sampled every 10 seconds can be downsampled
to an hourly index. All documents within an hour interval are summarized and
stored as a single document and stored in the downsample index.

This action corresponds to the  downsample API.

The name of the resulting downsample index is
`downsample-<original-index-name>-<random-uuid>`. If ILM performs the
`downsample` action on a backing index for a data stream, the downsample index
becomes a backing index for the same stream and the source index is deleted.

To use the `downsample` action in the `hot` phase, the `rollover` action *must*
be present. If no rollover action is configured, ILM will reject the
policy.

#### Options

`fixed_interval`:: (Required, string) The
fixed time interval into which the data
will be downsampled.

#### Example 

```console
PUT _ilm/policy/datastream_policy   
{
  "policy": {                       
    "phases": {
      "hot": {                      
        "actions": {
          "rollover": {             
            "max_docs": 1
          },
          "downsample": {
  	          "fixed_interval": "1h"
  	      }
        }
      }
    }
  }
}
```
