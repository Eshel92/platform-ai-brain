<!-- Converted from ml/anomaly-detection/apis/delete-filter.asciidoc (AsciiDoc). Includes are inlined. -->

# Delete filters API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Deletes a filter.

## Request

`DELETE _ml/filters/<filter_id>`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

This API deletes a filter. If an anomaly detection job references the filter, you cannot
delete the filter. You must update or delete the job before you can delete the
filter. For more information, see
{ml-docs}/ml-ad-run-jobs.html#ml-ad-rules[Custom rules].

## Path parameters

`<filter_id>`::
(Required, string)
A string that uniquely identifies a filter.

## Examples

```console
DELETE _ml/filters/safe_domains
```

When the filter is deleted, you receive the following results:

```console-result
{
  "acknowledged": true
}
```
