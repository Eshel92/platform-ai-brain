<!-- Converted from ml/trained-models/apis/infer-trained-model.asciidoc (AsciiDoc). Includes are inlined. -->

# Infer trained model API

**New API reference**
For the most up-to-date API details, refer to [Machine learning trained model APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-trained-model).

Evaluates a trained model. The model may be any supervised model either trained
by {dfanalytics} or imported.

**Note:** For model deployments with caching enabled, results may be returned
directly from the inference cache.

## Request

`POST _ml/trained_models/<model_id>/_infer`
`POST _ml/trained_models/<deployment_id>/_infer`

## Path parameters

`<model_id>`::
(Optional, string)
The unique identifier of the trained model or a model alias.
If you specify the `model_id` in the API call, and the model has multiple 
deployments, a random deployment will be used. If the `model_id` matches the ID 
of one of the deployments, that deployment will be used.

`<deployment_id>`::
(Optional, string)
A unique identifier for the deployment of the model.

## Query parameters

`timeout`::
(Optional, time)
Controls the amount of time to wait for inference results. Defaults to 10 seconds.

## Request body

`docs`::
(Required, array)
An array of objects to pass to the model for inference. The objects should
contain the fields matching your configured trained model input. Typically for
NLP models, the field name is `text_field`. Each inference input field specified 
in this property must be single strings not arrays of strings.

`inference_config`::
(Optional, object)
The default configuration for inference. This can be: `regression`,
`classification`, `fill_mask`, `ner`, `question_answering`,
`text_classification`, `text_embedding` or `zero_shot_classification`.
If `regression` or `classification`, it must match the `target_type` of the
underlying `definition.trained_model`. If `fill_mask`, `ner`,
`question_answering`, `text_classification`, or `text_embedding`; the
`model_type` must be `pytorch`. If not specified, the `inference_config`
from when the model was created is used.
**Properties of `inference_config`**
`classification`:::
(Optional, object)
Classification configuration for inference.
**Properties of classification inference**
=====
`num_top_classes`::::
(Optional, integer)
Specifies the number of top class predictions to return. Defaults to 0.
`num_top_feature_importance_values`::::
(Optional, integer)
Specifies the maximum number of
{ml-docs}/ml-feature-importance.html[{feat-imp}] values per document. Defaults
to 0 which means no {feat-imp} calculation occurs.
`prediction_field_type`::::
(Optional, string)
Specifies the type of the predicted field to write.
Valid values are: `string`, `number`, `boolean`. When `boolean` is provided
`1.0` is transformed to `true` and `0.0` to `false`.
`results_field`::::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to `predicted_value`.
`top_classes_results_field`::::
(Optional, string)
Specifies the field to which the top classes are written. Defaults to
`top_classes`.
=====

`fill_mask`:::
(Optional, object)
Configuration for a fill_mask natural language processing (NLP) task. The
fill_mask task works with models optimized for a fill mask action. For example,
for BERT models, the following text may be provided: "The capital of France is
[MASK].". The response indicates the value most likely to replace `[MASK]`. In
this instance, the most probable token is `paris`.
**Properties of fill_mask inference**
=====
`num_top_classes`::::
(Optional, integer)
Number of top predicted tokens to return for replacing the mask token. Defaults
to `0`.

`results_field`::::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to `predicted_value`.
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
**Properties of tokenization**
======
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
`xlm_roberta`::::
(Optional, object)
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of xlm_roberta**
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
`bert_ja`::::
(Optional, object)
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
**Properties of bert_ja**
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
======
=====

`ner`:::
(Optional, object)
Configures a named entity recognition (NER) task. NER is a special case of token
classification. Each token in the sequence is classified according to the
provided classification labels. Currently, the NER task requires the
`classification_labels` Inside-Outside-Beginning (IOB) formatted labels. Only
person, organization, location, and miscellaneous are supported.
**Properties of ner inference**
=====
`results_field`::::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to `predicted_value`.
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
**Properties of tokenization**
======
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
`xlm_roberta`::::
(Optional, object)
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of xlm_roberta**
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
`bert_ja`::::
(Optional, object)
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
**Properties of bert_ja**
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
======
=====

`pass_through`:::
(Optional, object)
Configures a `pass_through` task. This task is useful for debugging as no
post-processing is done to the inference output and the raw pooling layer
results are returned to the caller.
**Properties of pass_through inference**
=====
`results_field`::::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to `predicted_value`.
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
**Properties of tokenization**
======
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
`xlm_roberta`::::
(Optional, object)
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of xlm_roberta**
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
`bert_ja`::::
(Optional, object)
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
**Properties of bert_ja**
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
======
=====

`question_answering`:::
(Optional, object)
Configures a question answering natural language processing (NLP) task. Question
answering is useful for extracting answers for certain questions from a large
corpus of text.
**Properties of question_answering inference**
=====
`max_answer_length`::::
(Optional, integer)
The maximum amount of words in the answer. Defaults to `15`.

`num_top_classes`::::
(Optional, integer)
The number the top found answers to return. Defaults to `0`, meaning only the
best found answer is returned.

`question`::::
(Required, string)
The question to use when extracting an answer

`results_field`::::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to `predicted_value`.
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
Recommended to set `max_sequence_length` to `386` with `128` of `span` and set
`truncate` to `none`.
**Properties of tokenization**
======
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
`xlm_roberta`::::
(Optional, object)
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of xlm_roberta**
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
`bert_ja`::::
(Optional, object)
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
**Properties of bert_ja**
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
======
=====

`regression`:::
(Optional, object)
Regression configuration for inference.
**Properties of regression inference**
=====
`num_top_feature_importance_values`::::
(Optional, integer)
Specifies the maximum number of
{ml-docs}/ml-feature-importance.html[{feat-imp}] values per document.
By default, it is zero and no {feat-imp} calculation occurs.
`results_field`::::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to `predicted_value`.
=====

`text_classification`:::
(Optional, object)
A text classification task. Text classification classifies a provided text
sequence into previously known target classes. A specific example of this is
sentiment analysis, which returns the likely target classes indicating text
sentiment, such as "sad", "happy", or "angry".
**Properties of text_classification inference**
=====
`classification_labels`::::
(Optional, string) An array of classification labels.

`num_top_classes`::::
(Optional, integer)
Specifies the number of top class predictions to return. Defaults to all classes
(-1).

`results_field`::::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to `predicted_value`.
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
**Properties of tokenization**
======
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
`xlm_roberta`::::
(Optional, object)
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of xlm_roberta**
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
`bert_ja`::::
(Optional, object)
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
**Properties of bert_ja**
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
======
=====
`text_embedding`:::
(Object, optional)
Text embedding takes an input sequence and transforms it into a vector of
numbers. These embeddings capture not simply tokens, but semantic meanings and
context. These embeddings can be used in a dense vector field
for powerful insights.
**Properties of text_embedding inference**
=====
`results_field`::::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to `predicted_value`.
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
**Properties of tokenization**
======
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
`xlm_roberta`::::
(Optional, object)
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of xlm_roberta**
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
`bert_ja`::::
(Optional, object)
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
**Properties of bert_ja**
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
======
=====
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
`text`::::
(Required, string)
This is the text with which to compare all document provided text inputs.
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
**Properties of tokenization**
======
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
`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in BERT-style tokenization are:
* `[CLS]`: The first token of the sequence being classified.
* `[SEP]`: Indicates sequence separation.
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
`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in BERT-style tokenization are:
* `[CLS]`: The first token of the sequence being classified.
* `[SEP]`: Indicates sequence separation.
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
`xlm_roberta`::::
(Optional, object)
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of xlm_roberta**
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
`bert_ja`::::
(Optional, object)
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
**Properties of bert_ja**
=======
`span`::::
(Optional, integer)
When `truncate` is `none`, you can partition longer text sequences
for inference. The value indicates how many tokens overlap between each
subsequence.
The default value is `-1`, indicating no windowing or spanning occurs.
**Note:** When your typical input is just slightly larger than `max_sequence_length`, it may be best to simply truncate;
there will be very little information in the second subsequence.
`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens if `true`.
=======
======
=====
`zero_shot_classification`:::
(Object, optional)
Configures a zero-shot classification task. Zero-shot classification allows for
text classification to occur without pre-determined labels. At inference time,
it is possible to adjust the labels to classify. This makes this type of model
and task exceptionally flexible.
If consistently classifying the same labels, it may be better to use a
fine-tuned text classification model.
**Properties of zero_shot_classification inference**
=====
`labels`::::
(Optional, array)
The labels to classify. Can be set at creation for default labels, and
then updated during inference.
`multi_label`::::
(Optional, boolean)
Indicates if more than one `true` label is possible given the input.
This is useful when labeling text that could pertain to more than one of the
input labels. Defaults to `false`.
`results_field`::::
(Optional, string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to `predicted_value`.
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
**Properties of tokenization**
======
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
`xlm_roberta`::::
(Optional, object)
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of xlm_roberta**
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
`bert_ja`::::
(Optional, object)
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
**Properties of bert_ja**
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
======
=====

## Examples

The response depends on the kind of model.

For example, for {lang-ident} the response is the predicted language and the
score:

```console
POST _ml/trained_models/lang_ident_model_1/_infer
{
  "docs":[{"text": "The fool doth think he is wise, but the wise man knows himself to be a fool."}]
}
```

Here are the results predicting english with a high probability.

```console-result
{
  "inference_results": [
    {
      "predicted_value": "en",
      "prediction_probability": 0.9999658805366392,
      "prediction_score": 0.9999658805366392
    }
  ]
}
```

When it is a text classification model, the response is the score and predicted
classification.

For example:

```console
POST _ml/trained_models/model2/_infer
{
	"docs": [{"text_field": "The movie was awesome!!"}]
}
```

The API returns the predicted label and the confidence.

```console-result
{
  "inference_results": [{
    "predicted_value" : "POSITIVE",
    "prediction_probability" : 0.9998667964092964
  }]
}
```

For named entity recognition (NER) models, the response contains the annotated
text output and the recognized entities.

```console
POST _ml/trained_models/model2/_infer
{
	"docs": [{"text_field": "Hi my name is Josh and I live in Berlin"}]
}
```

The API returns in this case:

```console-result
{
  "inference_results": [{
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
  }]
}
```

Zero-shot classification models require extra configuration defining the class
labels. These labels are passed in the zero-shot inference config.

```console
POST _ml/trained_models/model2/_infer
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
  "inference_results": [{
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
  }]
}
```

Question answering models require extra configuration defining the question to
answer.

```console
POST _ml/trained_models/model2/_infer
{
  "docs": [
    {
      "text_field": "<long text to extract answer>"
    }
  ],
  "inference_config": {
    "question_answering": {
      "question": "<question to be answered>"
    }
  }
}
```

The API returns a response similar to the following:

```console-result
{
    "predicted_value": <string subsection of the text that is the answer>,
    "start_offset": <character offset in document to start>,
    "end_offset": <character offset end of the answer,
    "prediction_probability": <prediction score>
}
```

Text similarity models require at least two sequences of text to compare. It's
possible to provide multiple strings of text to compare to another text
sequence:

```console
POST _ml/trained_models/cross-encoder__ms-marco-tinybert-l-2-v2/_infer
{
  "docs":[{ "text_field": "Berlin has a population of 3,520,031 registered inhabitants in an area of 891.82 square kilometers."}, {"text_field": "New York City is famous for the Metropolitan Museum of Art."}],
  "inference_config": {
    "text_similarity": {
      "text": "How many people live in Berlin?"
    }
  }
}
```

The response contains the prediction for every string that is compared to the
text provided in the `text_similarity`.`text` field:

```console-result
{
  "inference_results": [
    {
      "predicted_value": 7.235751628875732
    },
    {
      "predicted_value": -11.562295913696289
    }
  ]
}
```

The tokenization truncate option can be overridden when calling the API:

```console
POST _ml/trained_models/model2/_infer
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
  "inference_results": [{
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
  }]
}
```
