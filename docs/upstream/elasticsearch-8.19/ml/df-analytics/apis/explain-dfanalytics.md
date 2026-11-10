<!-- Converted from ml/df-analytics/apis/explain-dfanalytics.asciidoc (AsciiDoc). Includes are inlined. -->

# Explain {dfanalytics} API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  {dfanalytics} APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-data-frame).

Explains a {dataframe-analytics-config}.

## Request

`GET _ml/data_frame/analytics/_explain` +

`POST _ml/data_frame/analytics/_explain` +

`GET _ml/data_frame/analytics/<data_frame_analytics_id>/_explain` +

`POST _ml/data_frame/analytics/<data_frame_analytics_id>/_explain`

## Prerequisites

Requires the following privileges:

* cluster: `monitor_ml` (the `machine_learning_user` built-in role grants this 
  privilege)
* source indices: `read`, `view_index_metadata`

## Description

This API provides explanations for a {dataframe-analytics-config} that either 
exists already or one that has not been created yet.
The following explanations are provided:

* which fields are included or not in the analysis and why,
* how much memory is estimated to be required. The estimate can be used when 
  deciding the appropriate value for `model_memory_limit` setting later on.

If you have object fields or fields that are excluded via source filtering,
they are not included in the explanation.

## Path parameters

`<data_frame_analytics_id>`::
(Optional, string)
Identifier for the {dfanalytics-job}.

## Request body

A {dataframe-analytics-config} as described in put-dfanalytics.
Note that `id` and `dest` don't need to be provided in the context of this API.

## Response body

The API returns a response that contains the following:

`field_selection`::
(array)
An array of objects that explain selection for each field, sorted by 
the field names.
**Properties of `field_selection` objects**
`is_included`:::
(Boolean) Whether the field is selected to be included in the analysis.

`is_required`:::
(Boolean) Whether the field is required.

`feature_type`:::
(string) The feature type of this field for the analysis. May be `categorical` 
or `numerical`.

`mapping_types`:::
(string) The mapping types of the field.

`name`:::
(string) The field name.

`reason`:::
(string) The reason a field is not selected to be included in the analysis.

`memory_estimation`::
(object) 
An object containing the memory estimates.
**Properties of `memory_estimation`**
`expected_memory_with_disk`:::
(string) Estimated memory usage under the assumption that overflowing to disk is 
allowed during {dfanalytics}. `expected_memory_with_disk` is usually smaller 
than `expected_memory_without_disk` as using disk allows to limit the main 
memory needed to perform {dfanalytics}.

`expected_memory_without_disk`:::
(string) Estimated memory usage under the assumption that the whole 
{dfanalytics} should happen in memory (i.e. without overflowing to disk).

## Examples

```console
POST _ml/data_frame/analytics/_explain
{
  "source": {
    "index": "houses_sold_last_10_yrs"
  },
  "analysis": {
    "regression": {
      "dependent_variable": "price"
    }
  }
}
```

The API returns the following results:

```console-result
{
  "field_selection": [
    {
      "field": "number_of_bedrooms",
      "mappings_types": ["integer"],
      "is_included": true,
      "is_required": false,
      "feature_type": "numerical"
    },
    {
      "field": "postcode",
      "mappings_types": ["text"],
      "is_included": false,
      "is_required": false,
      "reason": "[postcode.keyword] is preferred because it is aggregatable"
    },
    {
      "field": "postcode.keyword",
      "mappings_types": ["keyword"],
      "is_included": true,
      "is_required": false,
      "feature_type": "categorical"
    },
    {
      "field": "price",
      "mappings_types": ["float"],
      "is_included": true,
      "is_required": true,
      "feature_type": "numerical"
    }
  ],
  "memory_estimation": {
    "expected_memory_without_disk": "128MB",
    "expected_memory_with_disk": "32MB"
  }
}
```
