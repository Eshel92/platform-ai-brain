<!-- Converted from ml/df-analytics/apis/preview-dfanalytics.asciidoc (AsciiDoc). Includes are inlined. -->

# Preview {dfanalytics} API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  {dfanalytics} APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-data-frame).

Previews the features used by a {dataframe-analytics-config}.

## Request

`GET _ml/data_frame/analytics/_preview` +

`POST _ml/data_frame/analytics/_preview` +

`GET _ml/data_frame/analytics/<data_frame_analytics_id>/_preview` +

`POST _ml/data_frame/analytics/<data_frame_analytics_id>/_preview`

## Prerequisites

Requires the `monitor_ml` cluster privilege. This privilege is included in the 
`machine_learning_user` built-in role.

## Description

This API provides preview of the extracted features for a {dataframe-analytics-config}
that either exists already or one that has not been created yet.

## Path parameters

`<data_frame_analytics_id>`::
(Optional, string)
Identifier for the {dfanalytics-job}.

## Request body

`config`::
(Optional, object)
A {dataframe-analytics-config} as described in put-dfanalytics.
Note that `id` and `dest` don't need to be provided in the context of this API.

## Response body

The API returns a response that contains the following:

`feature_values`::
(array)
An array of objects that contain feature name and value pairs. The features have
been processed and indicate what will be sent to the model for training.

## Examples

```console
POST _ml/data_frame/analytics/_preview
{
  "config": {
    "source": {
      "index": "houses_sold_last_10_yrs"
    },
    "analysis": {
      "regression": {
        "dependent_variable": "price"
      }
    }
  }
}
```

The API returns the following results:

```console-result
{
  "feature_values": [
    {
      "number_of_bedrooms": "1",
      "postcode": "29655",
      "price": "140.4"
    },
    ...
  ]
}
```
