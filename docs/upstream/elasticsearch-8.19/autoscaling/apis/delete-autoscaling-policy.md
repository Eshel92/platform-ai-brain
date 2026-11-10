<!-- Converted from autoscaling/apis/delete-autoscaling-policy.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete autoscaling policy API

**Note:** {cloud-only}

**New API reference**
For the most up-to-date API details, refer to [Autoscaling APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-autoscaling).

Delete {cloud}/ec-autoscaling.html[autoscaling] policy.

#### Request

```console
PUT /_autoscaling/policy/my_autoscaling_policy
{
  "roles": [],
  "deciders": {
    "fixed": {
    }
  }
}
```

```console
DELETE /_autoscaling/policy/<name>
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`manage_autoscaling` cluster privilege to use this
API.

* If the {operator-feature} is enabled, only operator
users can use this API.

#### Description

This API deletes an autoscaling policy with the provided name.

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

#### Examples

This example deletes an autoscaling policy named `my_autoscaling_policy`.

```console
DELETE /_autoscaling/policy/my_autoscaling_policy
```

The API returns the following result:

```console-result
{
  "acknowledged": true
}
```

This example deletes all autoscaling policies.

```console
DELETE /_autoscaling/policy/*
```

The API returns the following result:

```console-result
{
  "acknowledged": true
}
```
