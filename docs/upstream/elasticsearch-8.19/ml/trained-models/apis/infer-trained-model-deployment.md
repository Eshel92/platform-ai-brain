<!-- Converted from ml/trained-models/apis/infer-trained-model-deployment.asciidoc (AsciiDoc). Includes are inlined. -->

# Infer trained model deployment API

**New API reference**
For the most up-to-date API details, refer to [Machine learning trained model APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-trained-model).

Evaluates a trained model.

deprecated::[8.3.0,Replaced by infer-trained-model.]

## Request

`POST _ml/trained_models/<model_id>/deployment/_infer`

## Path parameters

`<model_id>`::
(Required, string)
The unique identifier of the trained model or a model alias.

## Query parameters

`timeout`::
(Optional, time)
Controls the amount of time to wait for inference results. Defaults to 10 seconds.

## Request body

`docs`::
(Required, array)
An array of objects to pass to the model for inference. The objects should
contain a field matching your configured trained model input. Typically, the
field name is `text_field`.

## Examples

The response depends on the task the model is trained for. If it is a text
classification task, the response is the score. For example:

```console
POST _ml/trained_models/model2/deployment/_infer
{
	"docs": [{"text_field": "The movie was awesome!!"}]
}
```

The API returns the predicted label and the confidence.

```console-result
{
  "predicted_value" : "POSITIVE",
  "prediction_probability" : 0.9998667964092964
}
```

For named entity recognition (NER) tasks, the response contains the annotated
text output and the recognized entities.

```console
POST _ml/trained_models/model2/deployment/_infer
{
	"docs": [{"text_field": "Hi my name is Josh and I live in Berlin"}]
}
```

The API returns in this case:

```console-result
{
  "predicted_value" : "Hi my name is [Josh](PER&Josh) and I live in [Berlin](LOC&Berlin)",
  "entities" : [
    {
      "entity" : "Josh",
      "class_name" : "PER",
      "class_probability" : 0.9977303419824,
      "start_pos" : 14,
      "end_pos" : 18
    },
    {
      "entity" : "Berlin",
      "class_name" : "LOC",
      "class_probability" : 0.9992474323902818,
      "start_pos" : 33,
      "end_pos" : 39
    }
  ]
}
```

Zero-shot classification tasks require extra configuration defining the class
labels. These labels are passed in the zero-shot inference config.

```console
POST _ml/trained_models/model2/deployment/_infer
{
  "docs": [
    {
      "text_field": "This is a very happy person"
    }
  ],
  "inference_config": {
    "zero_shot_classification": {
      "labels": [
        "glad",
        "sad",
        "bad",
        "rad"
      ],
      "multi_label": false
    }
  }
}
```

The API returns the predicted label and the confidence, as well as the top
classes:

```console-result
{
  "predicted_value" : "glad",
  "top_classes" : [
    {
      "class_name" : "glad",
      "class_probability" : 0.8061155063386439,
      "class_score" : 0.8061155063386439
    },
    {
      "class_name" : "rad",
      "class_probability" : 0.18218006158387956,
      "class_score" : 0.18218006158387956
    },
    {
      "class_name" : "bad",
      "class_probability" : 0.006325615787634201,
      "class_score" : 0.006325615787634201
    },
    {
      "class_name" : "sad",
      "class_probability" : 0.0053788162898424545,
      "class_score" : 0.0053788162898424545
    }
  ],
  "prediction_probability" : 0.8061155063386439
}
```

The tokenization truncate option can be overridden when calling the API:

```console
POST _ml/trained_models/model2/deployment/_infer
{
  "docs": [{"text_field": "The Amazon rainforest covers most of the Amazon basin in South America"}],
  "inference_config": {
    "ner": {
      "tokenization": {
        "bert": {
          "truncate": "first"
        }
      }
    }
  }
}
```

When the input has been truncated due to the limit imposed by the model's
`max_sequence_length` the `is_truncated` field appears in the response.

```console-result
{
  "predicted_value" : "The [Amazon](LOC&Amazon) rainforest covers most of the [Amazon](LOC&Amazon) basin in [South America](LOC&South+America)",
  "entities" : [
    {
      "entity" : "Amazon",
      "class_name" : "LOC",
      "class_probability" : 0.9505460915724254,
      "start_pos" : 4,
      "end_pos" : 10
    },
    {
      "entity" : "Amazon",
      "class_name" : "LOC",
      "class_probability" : 0.9969992804311777,
      "start_pos" : 41,
      "end_pos" : 47
    }
  ],
  "is_truncated" : true
}
```
