<!-- Converted from ingest/processors/inference.asciidoc (AsciiDoc). Includes are inlined. -->

### {infer-cap} processor

Uses a pre-trained {dfanalytics} model or a model deployed for natural
language processing tasks to infer against the data that is being
ingested in the pipeline.

.{infer-cap} Options
|======
| Name                                  | Required  | Default                                    | Description
| `model_id` .                          | yes       | -                                          | (String) An inference ID, a model deployment ID, a trained model ID or an alias.
| `input_output`                        | no        | -                                          | (List) Input fields for inference and output (destination) fields for the inference results. This option is incompatible with the `target_field` and `field_map` options.
| `target_field`                        | no        | `ml.inference.<processor_tag>`             | (String) Field added to incoming documents to contain results objects.
| `field_map`                           | no        | If defined the model's default field map   | (Object) Maps the document field names to the known field names of the model. This mapping takes precedence over any default mappings provided in the model configuration.
| `inference_config`                    | no        | The default settings defined in the model  | (Object) Contains the inference type and its options.
| `ignore_missing`                      | no        | `false`                                    | (Boolean) If `true` and any of the input fields defined in `input_ouput` are missing then those missing fields are quietly ignored, otherwise a missing field causes a failure. Only applies when using `input_output` configurations to explicitly list the input fields.
| `description`     | no      | -        | Description of the processor. Useful for describing the purpose of the processor or its configuration.
| `if`             | no       | -        | Conditionally execute the processor. See conditionally-run-processor.
| `ignore_failure` | no       | `false`  | Ignore failures for the processor. See handling-pipeline-failures.
| `on_failure`     | no       | -        | Handle failures for the processor. See handling-pipeline-failures.
| `tag`            | no       | -        | Identifier for the processor. Useful for debugging and metrics.
|======

==================================================
* You cannot use the `input_output` field with the `target_field` and 
`field_map` fields. For NLP models, use the `input_output` option. For 
{dfanalytics} models, use the `target_field` and `field_map` option.
* Each inference input field must be single strings, not arrays of strings.
* The `input_field` is processed as is and ignores any index mapping's analyzers at time of inference run.
==================================================

#### Configuring input and output fields

Select the `content` field for inference and write the result to 
`content_embedding`.

**Important:** If the specified `output_field` already exists in the ingest document, it won't be overwritten.
The inference results will be appended to the existing fields within `output_field`, which could lead to duplicate fields and potential errors.
To avoid this, use an unique `output_field` field name that does not clash with any existing fields.

```js
{
  "inference": {
    "model_id": "model_deployment_for_inference",
    "input_output": [
        {
            "input_field": "content",
            "output_field": "content_embedding"
        }
    ]
  }
}
```

#### Configuring multiple inputs

The `content` and `title` fields will be read from the incoming document and 
sent to the model for the inference. The inference output is written to 
`content_embedding` and `title_embedding` respectively.

```js
{
  "inference": {
    "model_id": "model_deployment_for_inference",
    "input_output": [
        {
            "input_field": "content",
            "output_field": "content_embedding"
        },
        {
            "input_field": "title",
            "output_field": "title_embedding"
        }
    ]
  }
}
```

Selecting the input fields with `input_output` is incompatible with
the `target_field` and `field_map` options.

{dfanalytics-cap} models must use the `target_field` to specify the root 
location results are written to and optionally a `field_map` to map field names 
in the input document to the model input fields.

```js
{
  "inference": {
    "model_id": "model_deployment_for_inference",
    "target_field": "FlightDelayMin_prediction_infer",
    "field_map": {
      "your_field": "my_field"
    },
    "inference_config": { "regression": {} }
  }
}
```

#### {classification-cap} configuration options

Classification configuration for inference.

`num_top_classes`::
(Optional, integer)
Specifies the number of top class predictions to return. Defaults to 0.
`num_top_feature_importance_values`::
(Optional, integer)
Specifies the maximum number of
{ml-docs}/ml-feature-importance.html[{feat-imp}] values per document. Defaults
to 0 which means no {feat-imp} calculation occurs.
`results_field`::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to the `results_field` value of the {dfanalytics-job} that was
used to train the model, which defaults to `<dependent_variable>_prediction`.
`top_classes_results_field`::
(Optional, string)
Specifies the field to which the top classes are written. Defaults to
`top_classes`.
`prediction_field_type`::
(Optional, string)
Specifies the type of the predicted field to write.
Valid values are: `string`, `number`, `boolean`. When `boolean` is provided
`1.0` is transformed to `true` and `0.0` to `false`.

#### Fill mask configuration options

`num_top_classes`::
(Optional, integer)
Specifies the number of top class predictions to return. Defaults to 0.
`results_field`::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to the `results_field` value of the {dfanalytics-job} that was
used to train the model, which defaults to `<dependent_variable>_prediction`.
`tokenization`::
(Optional, object)
Indicates the tokenization to perform and the desired settings.
The default tokenization configuration is `bert`. Valid tokenization
values are
* `bert`: Use for BERT-style models
* `deberta_v2`: Use for DeBERTa v2 and v3-style models
* `mpnet`: Use for MPNet-style models
* `roberta`: Use for RoBERTa-style and BART-style models
* experimental:[] `xlm_roberta`: Use for XLMRoBERTa-style models
* experimental:[] `bert_ja`: Use for BERT-style models trained for the Japanese
language.
**Properties of tokenization**
=====
`bert`::::
(Optional, object)
BERT-style tokenization is to be performed with the enclosed settings.
**Properties of bert**
=======

`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======

`deberta_v2`::::
(Optional, object)
DeBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of deberta_v2**
=======
`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `balanced`: One or both of the first and second sequences may be truncated so as to balance the tokens included from both sequences.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence, that sequence is truncated.

=======

`roberta`::::
(Optional, object)
RoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of roberta**
=======

`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======

`mpnet`::::
(Optional, object)
MPNet-style tokenization is to be performed with the enclosed settings.
**Properties of mpnet**
=======

`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======
=====

#### NER configuration options

`results_field`::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to the `results_field` value of the {dfanalytics-job} that was
used to train the model, which defaults to `<dependent_variable>_prediction`.
`tokenization`::
(Optional, object)
Indicates the tokenization to perform and the desired settings.
The default tokenization configuration is `bert`. Valid tokenization
values are
* `bert`: Use for BERT-style models
* `deberta_v2`: Use for DeBERTa v2 and v3-style models
* `mpnet`: Use for MPNet-style models
* `roberta`: Use for RoBERTa-style and BART-style models
* experimental:[] `xlm_roberta`: Use for XLMRoBERTa-style models
* experimental:[] `bert_ja`: Use for BERT-style models trained for the Japanese
language.
**Properties of tokenization**
=====
`bert`::::
(Optional, object)
BERT-style tokenization is to be performed with the enclosed settings.
**Properties of bert**
=======

`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======

`deberta_v2`::::
(Optional, object)
DeBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of deberta_v2**
=======
`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `balanced`: One or both of the first and second sequences may be truncated so as to balance the tokens included from both sequences.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence, that sequence is truncated.

=======

`roberta`::::
(Optional, object)
RoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of roberta**
=======

`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======

`mpnet`::::
(Optional, object)
MPNet-style tokenization is to be performed with the enclosed settings.
**Properties of mpnet**
=======

`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======
=====

#### {regression-cap} configuration options

Regression configuration for inference.

`results_field`::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to the `results_field` value of the {dfanalytics-job} that was
used to train the model, which defaults to `<dependent_variable>_prediction`.
`num_top_feature_importance_values`::
(Optional, integer)
Specifies the maximum number of
{ml-docs}/ml-feature-importance.html[{feat-imp}] values per document.
By default, it is zero and no {feat-imp} calculation occurs.

#### Text classification configuration options

`classification_labels`::
(Optional, string) An array of classification labels.

`num_top_classes`::
(Optional, integer)
Specifies the number of top class predictions to return. Defaults to 0.
`results_field`::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to the `results_field` value of the {dfanalytics-job} that was
used to train the model, which defaults to `<dependent_variable>_prediction`.
`tokenization`::
(Optional, object)
Indicates the tokenization to perform and the desired settings.
The default tokenization configuration is `bert`. Valid tokenization
values are
* `bert`: Use for BERT-style models
* `deberta_v2`: Use for DeBERTa v2 and v3-style models
* `mpnet`: Use for MPNet-style models
* `roberta`: Use for RoBERTa-style and BART-style models
* experimental:[] `xlm_roberta`: Use for XLMRoBERTa-style models
* experimental:[] `bert_ja`: Use for BERT-style models trained for the Japanese
language.
**Properties of tokenization**
=====
`bert`::::
(Optional, object)
BERT-style tokenization is to be performed with the enclosed settings.
**Properties of bert**
=======

`span`::::
(Optional, integer)
When `truncate` is `none`, you can partition longer text sequences
for inference. The value indicates how many tokens overlap between each
subsequence.
The default value is `-1`, indicating no windowing or spanning occurs.
**Note:** When your typical input is just slightly larger than `max_sequence_length`, it may be best to simply truncate;
there will be very little information in the second subsequence.
`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======

`deberta_v2`::::
(Optional, object)
DeBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of deberta_v2**
=======
`span`::::
(Optional, integer)
When `truncate` is `none`, you can partition longer text sequences
for inference. The value indicates how many tokens overlap between each
subsequence.
The default value is `-1`, indicating no windowing or spanning occurs.
**Note:** When your typical input is just slightly larger than `max_sequence_length`, it may be best to simply truncate;
there will be very little information in the second subsequence.
`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `balanced`: One or both of the first and second sequences may be truncated so as to balance the tokens included from both sequences.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence, that sequence is truncated.

=======

`roberta`::::
(Optional, object)
RoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of roberta**
=======

`span`::::
(Optional, integer)
When `truncate` is `none`, you can partition longer text sequences
for inference. The value indicates how many tokens overlap between each
subsequence.
The default value is `-1`, indicating no windowing or spanning occurs.
**Note:** When your typical input is just slightly larger than `max_sequence_length`, it may be best to simply truncate;
there will be very little information in the second subsequence.
`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======

`mpnet`::::
(Optional, object)
MPNet-style tokenization is to be performed with the enclosed settings.
**Properties of mpnet**
=======

`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======
=====

#### Text embedding configuration options

`results_field`::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to the `results_field` value of the {dfanalytics-job} that was
used to train the model, which defaults to `<dependent_variable>_prediction`.
`tokenization`::
(Optional, object)
Indicates the tokenization to perform and the desired settings.
The default tokenization configuration is `bert`. Valid tokenization
values are
* `bert`: Use for BERT-style models
* `deberta_v2`: Use for DeBERTa v2 and v3-style models
* `mpnet`: Use for MPNet-style models
* `roberta`: Use for RoBERTa-style and BART-style models
* experimental:[] `xlm_roberta`: Use for XLMRoBERTa-style models
* experimental:[] `bert_ja`: Use for BERT-style models trained for the Japanese
language.
**Properties of tokenization**
=====
`bert`::::
(Optional, object)
BERT-style tokenization is to be performed with the enclosed settings.
**Properties of bert**
=======

`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======

`deberta_v2`::::
(Optional, object)
DeBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of deberta_v2**
=======
`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `balanced`: One or both of the first and second sequences may be truncated so as to balance the tokens included from both sequences.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence, that sequence is truncated.

=======

`roberta`::::
(Optional, object)
RoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of roberta**
=======

`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======

`mpnet`::::
(Optional, object)
MPNet-style tokenization is to be performed with the enclosed settings.
**Properties of mpnet**
=======

`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======
=====

#### Text expansion configuration options

`results_field`::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to the `results_field` value of the {dfanalytics-job} that was
used to train the model, which defaults to `<dependent_variable>_prediction`.
`tokenization`::
(Optional, object)
Indicates the tokenization to perform and the desired settings.
The default tokenization configuration is `bert`. Valid tokenization
values are
* `bert`: Use for BERT-style models
* `deberta_v2`: Use for DeBERTa v2 and v3-style models
* `mpnet`: Use for MPNet-style models
* `roberta`: Use for RoBERTa-style and BART-style models
* experimental:[] `xlm_roberta`: Use for XLMRoBERTa-style models
* experimental:[] `bert_ja`: Use for BERT-style models trained for the Japanese
language.
**Properties of tokenization**
=====
`bert`::::
(Optional, object)
BERT-style tokenization is to be performed with the enclosed settings.
**Properties of bert**
=======

`span`::::
(Optional, integer)
When `truncate` is `none`, you can partition longer text sequences
for inference. The value indicates how many tokens overlap between each
subsequence.
The default value is `-1`, indicating no windowing or spanning occurs.
**Note:** When your typical input is just slightly larger than `max_sequence_length`, it may be best to simply truncate;
there will be very little information in the second subsequence.
`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======

`deberta_v2`::::
(Optional, object)
DeBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of deberta_v2**
=======
`span`::::
(Optional, integer)
When `truncate` is `none`, you can partition longer text sequences
for inference. The value indicates how many tokens overlap between each
subsequence.
The default value is `-1`, indicating no windowing or spanning occurs.
**Note:** When your typical input is just slightly larger than `max_sequence_length`, it may be best to simply truncate;
there will be very little information in the second subsequence.
`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `balanced`: One or both of the first and second sequences may be truncated so as to balance the tokens included from both sequences.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence, that sequence is truncated.

=======

`roberta`::::
(Optional, object)
RoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of roberta**
=======

`span`::::
(Optional, integer)
When `truncate` is `none`, you can partition longer text sequences
for inference. The value indicates how many tokens overlap between each
subsequence.
The default value is `-1`, indicating no windowing or spanning occurs.
**Note:** When your typical input is just slightly larger than `max_sequence_length`, it may be best to simply truncate;
there will be very little information in the second subsequence.
`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======

`mpnet`::::
(Optional, object)
MPNet-style tokenization is to be performed with the enclosed settings.
**Properties of mpnet**
=======

`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======
=====

#### Text similarity configuration options

`text_similarity`:::
(Object, optional)
Text similarity takes an input sequence and compares it with another input sequence. This is commonly referred to
as cross-encoding. This task is useful for ranking document text when comparing it to another provided text input.
**Properties of text_similarity inference**
=====
`span_score_combination_function`::::
(Optional, string)
Identifies how to combine the resulting similarity score when a provided text passage is longer than `max_sequence_length` and must be
automatically separated for multiple calls. This only is applicable when `truncate` is `none` and `span` is a non-negative
number. The default value is `max`. Available options are:
* `max`: The maximum score from all the spans is returned.
* `mean`: The mean score over all the spans is returned.
`tokenization`::::
(Optional, object)
Indicates the tokenization to perform and the desired settings.
The default tokenization configuration is `bert`. Valid tokenization
values are
* `bert`: Use for BERT-style models
* `deberta_v2`: Use for DeBERTa v2 and v3-style models
* `mpnet`: Use for MPNet-style models
* `roberta`: Use for RoBERTa-style and BART-style models
* experimental:[] `xlm_roberta`: Use for XLMRoBERTa-style models
* experimental:[] `bert_ja`: Use for BERT-style models trained for the Japanese
language.
Refer to tokenization-properties to review the properties of the
`tokenization` object.
=====

#### Zero shot classification configuration options

`labels`::
(Optional, array)
The labels to classify. Can be set at creation for default labels, and
then updated during inference.
`multi_label`::
(Optional, boolean)
Indicates if more than one `true` label is possible given the input.
This is useful when labeling text that could pertain to more than one of the
input labels. Defaults to `false`.
`results_field`::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to the `results_field` value of the {dfanalytics-job} that was
used to train the model, which defaults to `<dependent_variable>_prediction`.
`tokenization`::
(Optional, object)
Indicates the tokenization to perform and the desired settings.
The default tokenization configuration is `bert`. Valid tokenization
values are
* `bert`: Use for BERT-style models
* `deberta_v2`: Use for DeBERTa v2 and v3-style models
* `mpnet`: Use for MPNet-style models
* `roberta`: Use for RoBERTa-style and BART-style models
* experimental:[] `xlm_roberta`: Use for XLMRoBERTa-style models
* experimental:[] `bert_ja`: Use for BERT-style models trained for the Japanese
language.
**Properties of tokenization**
=====
`bert`::::
(Optional, object)
BERT-style tokenization is to be performed with the enclosed settings.
**Properties of bert**
=======

`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======

`deberta_v2`::::
(Optional, object)
DeBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of deberta_v2**
=======
`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `balanced`: One or both of the first and second sequences may be truncated so as to balance the tokens included from both sequences.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence, that sequence is truncated.

=======

`roberta`::::
(Optional, object)
RoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of roberta**
=======

`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======

`mpnet`::::
(Optional, object)
MPNet-style tokenization is to be performed with the enclosed settings.
**Properties of mpnet**
=======

`truncate`::::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

=======
=====

#### {infer-cap} processor examples

```js
"inference":{
  "model_id": "my_model_id",
  "field_map": {
    "original_fieldname": "expected_fieldname"
  },
  "inference_config": {
    "regression": {
      "results_field": "my_regression"
    }
  }
}
```

This configuration specifies a `regression` inference and the results are
written to the `my_regression` field contained in the `target_field` results
object. The `field_map` configuration maps the field `original_fieldname` from
the source document to the field expected by the model.

```js
"inference":{
  "model_id":"my_model_id"
  "inference_config": {
    "classification": {
      "num_top_classes": 2,
      "results_field": "prediction",
      "top_classes_results_field": "probabilities"
    }
  }
}
```

This configuration specifies a `classification` inference. The number of
categories for which the predicted probabilities are reported is 2
(`num_top_classes`). The result is written to the `prediction` field and the top
classes to the `probabilities` field. Both fields are contained in the
`target_field` results object.

For an example that uses {nlp} trained models, refer to
{ml-docs}/ml-nlp-inference.html[Add NLP inference to ingest pipelines].

#### {feat-imp-cap} object mapping

To get the full benefit of aggregating and searching for
{ml-docs}/ml-feature-importance.html[{feat-imp}], update your index mapping of
the {feat-imp} result field as you can see below:

```js
"ml.inference.feature_importance": {
  "type": "nested",
  "dynamic": true,
  "properties": {
    "feature_name": {
      "type": "keyword"
    },
    "importance": {
      "type": "double"
    }
  }
}
```

The mapping field name for {feat-imp} (in the example above, it is
`ml.inference.feature_importance`) is compounded as follows:

`<ml.inference.target_field>`.`<inference.tag>`.`feature_importance`

* `<ml.inference.target_field>`: defaults to `ml.inference`.
* `<inference.tag>`: if is not provided in the processor definition, then it is
not part of the field path.

For example, if you provide a tag `foo` in the definition as you can see below:

```js
{
  "tag": "foo",
  ...
}
```

Then, the {feat-imp} value is written to the
`ml.inference.foo.feature_importance` field.

You can also specify the target field as follows:

```js
{
  "tag": "foo",
  "target_field": "my_field"
}
```

In this case, {feat-imp} is exposed in the
`my_field.foo.feature_importance` field.

#### {infer-cap} processor examples

The following example uses an inference endpoint in an inference processor named `query_helper_pipeline` to perform a chat completion task.
The processor generates an Elasticsearch query from natural language input using a prompt designed for a completion task type.
Refer to this list for the inference service you use and check the corresponding examples of setting up an endpoint with the chat completion task type.

```console
PUT _ingest/pipeline/query_helper_pipeline
{
  "processors": [
    {
      "script": {
        "source": "ctx.prompt = 'Please generate an elasticsearch search query on index `articles_index` for the following natural language query. Dates are in the field `@timestamp`, document types are in the field `type` (options are `news`, `publication`), categories in the field `category` and can be multiple (options are `medicine`, `pharmaceuticals`, `technology`), and document names are in the field `title` which should use a fuzzy match. Ignore fields which cannot be determined from the natural language query context: ' + ctx.content" <1>
      }
    },
    {
      "inference": {
        "model_id": "openai_chat_completions", <2>
        "input_output": {
          "input_field": "prompt",
          "output_field": "query"
        }
      }
    },
    {
      "remove": {
        "field": "prompt"
      }
    }
  ]
}
```
<1> The `prompt` field contains the prompt used for the completion task, created with Painless.
`+ ctx.content` appends the natural language input to the prompt.
<2> The ID of the pre-configured inference endpoint, which utilizes the `openai` service with the `completion` task type.

The following API request will simulate running a document through the ingest pipeline created previously:

```console
POST _ingest/pipeline/query_helper_pipeline/_simulate
{
  "docs": [
    {
      "_source": {
        "content": "artificial intelligence in medicine articles published in the last 12 months" <1>
      }
    }
  ]
}
```
<1> The natural language query used to generate an Elasticsearch query within the prompt created by the inference processor.

#### Further readings

* [Which job is the best for you? Using LLMs and semantic_text to match resumes to jobs](https://www.elastic.co/search-labs/blog/openwebcrawler-llms-semantic-text-resume-job-search)
