<!-- Converted from autoscaling/autoscaling-deciders.asciidoc (AsciiDoc). Includes are inlined. -->

## Autoscaling deciders

Reactive storage decider::
Estimates required storage capacity of current data set. Available for policies
governing data nodes.

Proactive storage decider::
Estimates required storage capacity based on current ingestion into hot nodes.
Available for policies governing hot data nodes.

Frozen shards decider::
Estimates required memory capacity based on the number of partially mounted shards.
Available for policies governing frozen data nodes.

Frozen storage decider::
Estimates required storage capacity as a percentage of the total data set of
partially mounted indices.
Available for policies governing frozen data nodes.

Frozen existence decider::
Estimates a minimum require frozen memory and storage capacity when any index is
in the frozen ILM phase.

Machine learning decider::
Estimates required memory capacity based on machine learning jobs.
Available for policies governing machine learning nodes.

Fixed decider::
Responds with a fixed required capacity. This decider is intended for testing only.

(See `autoscaling/deciders/reactive-storage-decider.md`)
(See `autoscaling/deciders/proactive-storage-decider.md`)
(See `autoscaling/deciders/frozen-shards-decider.md`)
(See `autoscaling/deciders/frozen-storage-decider.md`)
(See `autoscaling/deciders/frozen-existence-decider.md`)
(See `autoscaling/deciders/machine-learning-decider.md`)
(See `autoscaling/deciders/fixed-decider.md`)
