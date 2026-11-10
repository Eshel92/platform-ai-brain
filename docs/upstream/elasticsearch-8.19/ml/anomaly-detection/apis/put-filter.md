<!-- Converted from ml/anomaly-detection/apis/put-filter.asciidoc (AsciiDoc). Includes are inlined. -->

# Create filters API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Instantiates a filter.

## Request

`PUT _ml/filters/<filter_id>`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

A filter contains a list of strings. It can be used by one or more jobs.
Specifically, filters are referenced in the `custom_rules` property of detector
configuration objects. For more information, see
{ml-docs}/ml-ad-run-jobs.html#ml-ad-rules[Custom rules].

## Path parameters

`<filter_id>`::
(Required, string)
A string that uniquely identifies a filter.

## Request body

`description`::
  (Optional, string) A description of the filter.
  
`items`::
  (Required, array of strings) The items of the filter. A wildcard `*` can be
  used at the beginning or the end of an item. Up to 10000 items are allowed in
  each filter.

## Examples

```console
PUT _ml/filters/safe_domains
{
  "description": "A list of safe domains",
  "items": ["*.google.com", "wikipedia.org"]
}
```

When the filter is created, you receive the following response:

```console-result
{
  "filter_id": "safe_domains",
  "description": "A list of safe domains",
  "items": ["*.google.com", "wikipedia.org"]
}
```
