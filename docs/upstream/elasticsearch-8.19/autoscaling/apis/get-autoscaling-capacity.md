<!-- Converted from autoscaling/apis/get-autoscaling-capacity.asciidoc (AsciiDoc). Includes are inlined. -->

### Get autoscaling capacity API

**Note:** {cloud-only}

**New API reference**
For the most up-to-date API details, refer to [Autoscaling APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-autoscaling).

Get {cloud}/ec-autoscaling.html[autoscaling] capacity.

#### Request

```console
GET /_autoscaling/capacity/
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have
`manage_autoscaling` cluster privileges. For more information, see
security-privileges.

#### Description

This API gets the current autoscaling capacity based on the configured
autoscaling policy. This API will return information to size the cluster
appropriately to the current workload.

The `required_capacity` is calculated as the max of the `required_capacity`
result of all individual deciders that are enabled for the policy.

The operator should verify that the `current_nodes` match
the operator's knowledge of the cluster to avoid making autoscaling decisions
based on stale or incomplete information.

The response contains decider-specific information you can use to diagnose how
and why autoscaling determined a certain capacity was required. This information
is provided for diagnosis only. Do not use this information to make autoscaling
decisions.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Response body

`policies`::
(object)
Contains the map of policy name to capacity result
**Properties of `policies`**
`<policy_name>`::
(object)
Contains capacity information for the policy
**Properties of `<policy_name>`**
=====
`required_capacity`::
(object)
Contains the required capacity for the policy.
**Properties of `required_capacity`**
======
`node`::
(object)
Contains the minimum node sizes required per node, ensuring that individual
shards or ML jobs can fit into a single node.
**Properties of `node`**
=======
`storage`::
(integer)
Bytes of storage required per node.

`memory`::
(integer)
Bytes of memory required per node.

`processors`::
(float)
Number of processors (vCPUs) required per node.

=======
`total`::
(object)
Contains the total size required for the policy.
**Properties of `total`**
=======
`storage`::
(integer)
Total bytes of storage required for the policy.

`memory`::
(integer)
Total bytes of memory required for the policy.

`processors`::
(float)
Total number of processors (vCPUs) required for the policy.

=======
======
`current_capacity`::
(object)
Contains the current capacity for nodes governed by the policy, i.e. the nodes
that Elasticsearch bases its calculation on.
**Properties of `current_capacity`**
======
`node`::
(object)
Contains the maximum sizes of nodes governed by the policy.
**Properties of `node`**
=======
`storage`::
(integer)
Maximum bytes of storage of a node.

`memory`::
(integer)
Maximum bytes of memory of a node.

`processors`::
(float)
Maximum number of processors (vCPUs) of a node.

=======
`total`::
(object)
Contains the current total storage and memory sizes for nodes governed by the policy.
**Properties of `total`**
=======
`storage`::
(integer)
Current bytes of storage available for the policy.

`memory`::
(integer)
Current bytes of memory available for the policy.

`processors`::
Current number of processors (vCPUs) available for the policy.

=======
======
`current_nodes`::
(array of objects)
List of nodes used for capacity calculation.
**Properties of elements in `current_nodes`**
======
`name`::
(string)
Name of the node.
======
`deciders`::
(object)
The capacity results from individual deciders, allowing insight into how the
outer level `required_capacity` was calculated.
**Properties of `deciders`**
=======
`<decider_name>`::
(object)
The capacity result for a specific decider enabled for the policy.
**Properties of `<decider_name>`**
========
`required_capacity`::
(object)
Required capacity determined by the decider.
**Properties of `required_capacity`**
=========
`node`::
(object)
Contains the minimum node sizes required per node, ensuring that individual
shards or machine learning jobs can fit into a single node.
**Properties of `node`**
==========
`storage`::
(integer)
Bytes of storage required per node.

`memory`::
(integer)
Bytes of memory required per node.

`processors`::
(float)
Number of processors (vCPUs) required per node.

==========
`total`::
(object)
Contains the total size required for the policy.
**Properties of `total`**
==========
`storage`::
(integer)
Total bytes of storage required for the policy.

`memory`::
(integer)
Total bytes of memory required for the policy.

`processors`::
(float)
Total number of processors (vCPUs) required for the policy.

==========
=========
`reason_summary`::
(string)
Description of the basis for the decider's result.

`reason_details`::
(object)
A per-decider structure containing details about the basis for the deciders' result.
The contents should not be relied on for application purposes and are not subject
to backwards compatibility guarantees.
========
=======
=====

#### Examples

This example retrieves the current autoscaling capacity.

```console
GET /_autoscaling/capacity
```

The API returns the following result:

```console-result
{
  policies: {}
}
```
