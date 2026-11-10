<!-- Converted from autoscaling/deciders/fixed-decider.asciidoc (AsciiDoc). Includes are inlined. -->

### Fixed decider

experimental[]
The fixed decider is intended for testing only. Do not use this decider in production.

The {cloud}/ec-autoscaling.html[autoscaling] `fixed` decider responds with a fixed required capacity. It is not enabled
by default but can be enabled for any policy by explicitly configuring it.

#### Configuration settings

`storage`::
(Optional, byte value)
Required amount of node-level storage. Defaults to `-1` (disabled).

`memory`::
(Optional, byte value)
Required amount of node-level memory. Defaults to `-1` (disabled).

`processors`::
(Optional, float)
Required number of processors. Defaults to disabled.

`nodes`::
(Optional, integer)
Number of nodes to use when calculating capacity. Defaults to `1`.

#### Examples

This example puts an autoscaling policy named `my_autoscaling_policy`, enabling
and configuring the fixed decider.

```console
PUT /_autoscaling/policy/my_autoscaling_policy
{
  "roles" : [ "data_hot" ],
  "deciders": {
    "fixed": {
      "storage": "1tb",
      "memory": "32gb",
      "processors": 2.3,
      "nodes": 8
    }
  }
}
```

The API returns the following result:

```console-result
{
  "acknowledged": true
}
```

```console
DELETE /_autoscaling/policy/my_autoscaling_policy
```
