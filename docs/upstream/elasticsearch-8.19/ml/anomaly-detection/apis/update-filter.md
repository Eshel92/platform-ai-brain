<!-- Converted from ml/anomaly-detection/apis/update-filter.asciidoc (AsciiDoc). Includes are inlined. -->

# Update filters API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Updates the description of a filter, adds items, or removes items. 

## Request

`POST _ml/filters/<filter_id>/_update`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Path parameters

`<filter_id>`::
(Required, string)
A string that uniquely identifies a filter.

## Request body

`add_items`::
  (Optional, array of strings) The items to add to the filter.

`description`::
  (Optional, string) A description for the filter.
	
`remove_items`::
  (Optional, array of strings) The items to remove from the filter.

## Examples

```console
POST _ml/filters/safe_domains/_update
{
  "description": "Updated list of domains",
  "add_items": ["*.myorg.com"],
  "remove_items": ["wikipedia.org"]
}
```

The API returns the following results:

```console-result
{
  "filter_id": "safe_domains",
  "description": "Updated list of domains",
  "items": ["*.google.com", "*.myorg.com"]
}
```
