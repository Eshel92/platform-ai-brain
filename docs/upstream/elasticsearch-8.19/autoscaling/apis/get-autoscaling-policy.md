<!-- Converted from autoscaling/apis/get-autoscaling-policy.asciidoc (AsciiDoc). Includes are inlined. -->

### Get autoscaling policy API

**Note:** {cloud-only}

**New API reference**
For the most up-to-date API details, refer to [Autoscaling APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-autoscaling).

Get {cloud}/ec-autoscaling.html[autoscaling] policy.

#### Request

```console
PUT /_autoscaling/policy/my_autoscaling_policy
{
  "roles" : [],
  "deciders": {
    "fixed": {
    }
  }
}
```

```console
DELETE /_autoscaling/policy/my_autoscaling_policy
```

```console
GET /_autoscaling/policy/<name>
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have
`manage_autoscaling` cluster privileges. For more information, see
security-privileges.

#### Description

This API gets an autoscaling policy with the provided name.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Examples

This example gets an autoscaling policy named `my_autoscaling_policy`.

```console
GET /_autoscaling/policy/my_autoscaling_policy
```

The API returns the following result:

```console-result
{
   "roles": <roles>,
   "deciders": <deciders>
}
```
