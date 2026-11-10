<!-- Converted from ml/trained-models/apis/put-trained-models.asciidoc (AsciiDoc). Includes are inlined. -->

# Create trained models API

**New API reference**
For the most up-to-date API details, refer to [Machine learning trained model APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-trained-model).

Creates a trained model.

**Warning:** Models created in version 7.8.0 are not backwards compatible
         with older node versions. If in a mixed cluster environment,
         all nodes must be at least 7.8.0 to use a model stored by
         a 7.8.0 node.

## Request

`PUT _ml/trained_models/<model_id>`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the
`machine_learning_admin` built-in role.

## Description

The create trained model API enables you to supply a trained model that is not
created by {dfanalytics}.

## Path parameters

`<model_id>`::
(Required, string)
The unique identifier of the trained model.

## Query parameters

`defer_definition_decompression`::
(Optional, boolean)
If set to `true` and a `compressed_definition` is provided, the request defers
definition decompression and skips relevant validations.
This deferral is useful for systems or users that know a good byte size estimate for their
model and know that their model is valid and likely won't fail during inference.

`wait_for_completion`::
(Optional, boolean)
Whether to wait for all child operations such as model download
to complete, before returning or not. Defaults to `false`.

## Request body

`compressed_definition`::
(Required, string)
The compressed (GZipped and Base64 encoded) inference definition of the model.
If `compressed_definition` is specified, then `definition` cannot be specified.

`definition`::
(Required, object)
The inference definition for the model. If `definition` is specified, then
`compressed_definition` cannot be specified.
**Properties of `definition`**
`preprocessors`::
(Optional, object)
Collection of preprocessors. See ml-put-trained-models-preprocessor-example.
**Properties of `preprocessors`**
=====
`frequency_encoding`::
(Required, object)
Defines a frequency encoding for a field.
**Properties of `frequency_encoding`**
======
`feature_name`::
(Required, string)
The name of the resulting feature.

`field`::
(Required, string)
The field name to encode.

`frequency_map`::
(Required, object map of string:double)
Object that maps the field value to the frequency encoded value.

`custom`::
(Optional, Boolean)
Boolean value indicating if the analytics job created the preprocessor
or if a user provided it. This adjusts the feature importance calculation.
When `true`, the feature importance calculation returns importance for the
processed feature. When `false`, the total importance of the original field
is returned. Default is `false`.
======

`one_hot_encoding`::
(Required, object)
Defines a one hot encoding map for a field.
**Properties of `one_hot_encoding`**
======
`field`::
(Required, string)
The field name to encode.

`hot_map`::
(Required, object map of strings)
String map of "field_value: one_hot_column_name".

`custom`::
(Optional, Boolean)
Boolean value indicating if the analytics job created the preprocessor
or if a user provided it. This adjusts the feature importance calculation.
When `true`, the feature importance calculation returns importance for the
processed feature. When `false`, the total importance of the original field
is returned. Default is `false`.
======

`target_mean_encoding`::
(Required, object)
Defines a target mean encoding for a field.
**Properties of `target_mean_encoding`**
======
`default_value`:::
(Required, double)
The feature value if the field value is not in the `target_map`.

`feature_name`:::
(Required, string)
The name of the resulting feature.

`field`:::
(Required, string)
The field name to encode.

`target_map`:::
(Required, object map of string:double)
Object that maps the field value to the target mean value.

`custom`::
(Optional, Boolean)
Boolean value indicating if the analytics job created the preprocessor
or if a user provided it. This adjusts the feature importance calculation.
When `true`, the feature importance calculation returns importance for the
processed feature. When `false`, the total importance of the original field
is returned. Default is `false`.
======
=====

`trained_model`::
(Required, object)
The definition of the trained model.
**Properties of `trained_model`**
=====
`tree`::
(Required, object)
The definition for a binary decision tree.
**Properties of `tree`**
======
`classification_labels`:::
(Optional, string) An array of classification labels (used for
`classification`).

`feature_names`:::
(Required, string)
Features expected by the tree, in their expected order.

`target_type`:::
(Required, string)
String indicating the model target type; `regression` or `classification`.

`tree_structure`:::
(Required, object)
An array of `tree_node` objects. The nodes must be in ordinal order by their
`tree_node.node_index` value.
======

`tree_node`::
(Required, object)
The definition of a node in a tree.
There are two major types of nodes: leaf nodes and not-leaf nodes.

* Leaf nodes only need `node_index` and `leaf_value` defined.
* All other nodes need `split_feature`, `left_child`, `right_child`,
  `threshold`, `decision_type`, and `default_left` defined.
**Properties of `tree_node`**
======
`decision_type`::
(Optional, string)
Indicates the positive value (in other words, when to choose the left node)
decision type. Supported `lt`, `lte`, `gt`, `gte`. Defaults to `lte`.

`default_left`::
(Optional, Boolean)
Indicates whether to default to the left when the feature is missing. Defaults
to `true`.

`leaf_value`::
(Optional, double)
The leaf value of the of the node, if the value is a leaf (in other words, no
children).

`left_child`::
(Optional, integer)
The index of the left child.

`node_index`::
(Integer)
The index of the current node.

`right_child`::
(Optional, integer)
The index of the right child.

`split_feature`::
(Optional, integer)
The index of the feature value in the feature array.

`split_gain`::
(Optional, double) The information gain from the split.

`threshold`::
(Optional, double)
The decision threshold with which to compare the feature value.
======

`ensemble`::
(Optional, object)
The definition for an ensemble model. See ml-put-trained-models-model-example.
**Properties of `ensemble`**
======
`aggregate_output`::
(Required, object)
An aggregated output object that defines how to aggregate the outputs of the
`trained_models`. Supported objects are `weighted_mode`, `weighted_sum`, and
`logistic_regression`. See ml-put-trained-models-aggregated-output-example.
**Properties of `aggregate_output`**
=======
`logistic_regression`::
(Optional, object)
This `aggregated_output` type works with binary classification (classification
for values [0, 1]). It multiplies the outputs (in the case of the `ensemble`
model, the inference model values) by the supplied `weights`. The resulting
vector is summed and passed to a
[`sigmoid` function](https://en.wikipedia.org/wiki/Sigmoid_function). The result
of the `sigmoid` function is considered the probability of class 1 (`P_1`),
consequently, the probability of class 0 is `1 - P_1`. The class with the
highest probability (either 0 or 1) is then returned. For more information about
logistic regression, see
[this wiki article](https://en.wikipedia.org/wiki/Logistic_regression).
**Properties of `logistic_regression`**
========
`weights`:::
(Required, double)
The weights to multiply by the input values (the inference values of the trained
models).
========

`weighted_sum`::
(Optional, object)
This `aggregated_output` type works with regression. The weighted sum of the
input values.
**Properties of `weighted_sum`**
========
`weights`:::
(Required, double)
The weights to multiply by the input values (the inference values of the trained
models).
========

`weighted_mode`::
(Optional, object)
This `aggregated_output` type works with regression or classification. It takes
a weighted vote of the input values. The most common input value (taking the
weights into account) is returned.
**Properties of `weighted_mode`**
========
`weights`:::
(Required, double)
The weights to multiply by the input values (the inference values of the trained
models).
========

`exponent`::
(Optional, object)
This `aggregated_output` type works with regression. It takes a weighted sum of
the input values and passes the result to an exponent function
(`e^x` where `x` is the sum of the weighted values).
**Properties of `exponent`**
========
`weights`:::
(Required, double)
The weights to multiply by the input values (the inference values of the trained
models).
========
=======

`classification_labels`::
(Optional, string)
An array of classification labels.

`feature_names`::
(Optional, string)
Features expected by the ensemble, in their expected order.

`target_type`::
(Required, string)
String indicating the model target type; `regression` or `classification.`

`trained_models`::
(Required, object)
An array of `trained_model` objects. Supported trained models are `tree` and
`ensemble`.
======

=====

`description`::
(Optional, string)
A human-readable description of the inference trained model.

`estimated_heap_memory_usage_bytes`::
(Optional, integer) deprecated:[7.16.0,Replaced by `model_size_bytes`]

`estimated_operations`::
(Optional, integer)
The estimated number of operations to use the trained model during inference.
This property is supported only if `defer_definition_decompression` is `true` or
the model definition is not supplied.

`inference_config`::
(Required, object)
The default configuration for inference. This can be: `regression`,
`classification`, `fill_mask`, `ner`, `question_answering`,
`text_classification`, `text_embedding`, `text_expansion` or `zero_shot_classification`.
If `regression` or `classification`, it must match the `target_type` of the
underlying `definition.trained_model`. If `fill_mask`, `ner`,
`question_answering`, `text_classification`, `text_embedding` or `text_expansion`; the
`model_type` must be `pytorch`.
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
Number of top predicted tokens to return for replacing the mask token. Defaults to `0`.

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
Refer to tokenization-properties to review the properties of the
`tokenization` object.
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
`classification_labels`::::
(Optional, string)
An array of classification labels. NER only supports Inside-Outside-Beginning
labels (IOB) and only persons, organizations, locations, and miscellaneous.
Example: ["O", "B-PER", "I-PER", "B-ORG", "I-ORG", "B-LOC", "I-LOC", "B-MISC",
"I-MISC"]

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
Refer to tokenization-properties to review the
properties of the `tokenization` object.
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
Refer to tokenization-properties to review the properties of the
`tokenization` object.
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
Recommended to set `max_sentence_length` to `386` with `128` of `span` and set
`truncate` to `none`.
Refer to tokenization-properties to review the properties of the
`tokenization` object.
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
Refer to tokenization-properties to review the properties of the
`tokenization` object.
=====

`text_embedding`:::
(Object, optional)
Text embedding takes an input sequence and transforms it into a vector of
numbers. These embeddings capture not simply tokens, but semantic meanings and
context. These embeddings can be used in a dense vector field
for powerful insights.
**Properties of text_embedding inference**
=====
`embedding_size`::::
(Optional, integer)
The number of dimensions in the embedding vector produced by the model.
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
Refer to tokenization-properties to review the properties of the
`tokenization` object.
=====

`text_expansion`:::
(Object, optional)
The text expansion task works with sparse embedding models to transform an input sequence
into a vector of weighted tokens. These embeddings capture semantic meanings and
context and can be used in a sparse vector field for powerful insights.
**Properties of text_expansion inference**
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
Refer to tokenization-properties to review the properties of the
`tokenization` object.
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
`classification_labels`::::
(Required, array)
The classification labels used during the zero-shot classification. Classification
labels must not be empty or null and only set at model creation. They must be all three
of ["entailment", "neutral", "contradiction"].

**Note:** This is NOT the same as `labels` which are the values that zero-shot is attempting to
      classify.
`hypothesis_template`::::
(Optional, string)
This is the template used when tokenizing the sequences for classification.
The labels replace the `{}` value in the text. The default value is:
`This example is {}.`
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
Refer to tokenization-properties to review the properties of the
`tokenization` object.
=====

`input`::
(Required, object)
The input field names for the model definition.
**Properties of `input`**
`field_names`:::
(Required, string)
An array of input field names for the model.

`location`::
(Optional, object)
The model definition location. If the `definition` or `compressed_definition`
are not specified, the `location` is required.
**Properties of `location`**
`index`:::
(Required, object)
Indicates that the model definition is stored in an index. This object must be
empty as the index for storing model definitions is configured automatically.

`metadata`::
(Optional, object)
An object map that contains metadata about the model.

`model_size_bytes`::
(Optional, integer)
The estimated memory usage in bytes to keep the trained model in memory. This
property is supported only if `defer_definition_decompression` is `true` or the
model definition is not supplied.

`model_type`::
(Optional, string)
The created model type. By default the model type is `tree_ensemble`.
Appropriate types are:
* `tree_ensemble`: The model definition is an ensemble model of decision trees.
* `lang_ident`: A special type reserved for language identification models.
* `pytorch`: The stored definition is a PyTorch (specifically a TorchScript) model. Currently only
NLP models are supported. For more information, refer to {ml-docs}/ml-nlp.html[{nlp-cap}].
`platform_architecture`::
(Optional, string)
If the model only works on one platform, because it is heavily
optimized for a particular processor architecture and OS combination,
then this field specifies which. The format of the string must match
the platform identifiers used by Elasticsearch, so one of, `linux-x86_64`,
`linux-aarch64`, `darwin-x86_64`, `darwin-aarch64`, or `windows-x86_64`.
For portable models (those that work independent of processor architecture or
OS features), leave this field unset.

`prefix_strings`::
(Optional, object)
Certain NLP models are trained in such a way that a prefix string should
be applied to the input text before the input is evaluated. The prefix
may be different depending on the intention. For asymmetric tasks such
as infromation retrieval the prefix applied to a passage as it is indexed
can be different to the prefix applied when searching those passages.
`prefix_strings` has 2 options, a prefix string that is always applied
in the search context and one that is always applied when ingesting the
docs. Both are optional.
**Properties of `prefix_strings`**
`search`:::
(Optional, string)
The prefix string to prepend to the input text for requests
originating from a search query.

`ingest`:::
(Optional, string)
The prefix string to prepend to the input text for requests
at ingest where the inference ingest processor is used.

`tags`::
(Optional, string)
An array of tags to organize the model.

### Properties of `tokenizaton`

The `tokenization` object has the following properties.

`bert`::
(Optional, object)
BERT-style tokenization is to be performed with the enclosed settings.
**Properties of bert**
`do_lower_case`:::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`:::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
`span`:::
(Optional, integer)
When `truncate` is `none`, you can partition longer text sequences
for inference. The value indicates how many tokens overlap between each
subsequence.
The default value is `-1`, indicating no windowing or spanning occurs.
**Note:** When your typical input is just slightly larger than `max_sequence_length`, it may be best to simply truncate;
there will be very little information in the second subsequence.
`truncate`:::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

`with_special_tokens`:::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in BERT-style tokenization are:
* `[CLS]`: The first token of the sequence being classified.
* `[SEP]`: Indicates sequence separation.
`deberta_v2`::
(Optional, object)
DeBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of deberta_v2**
`do_lower_case`:::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
Defaults to `false`.

`max_sequence_length`:::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
`span`:::
(Optional, integer)
When `truncate` is `none`, you can partition longer text sequences
for inference. The value indicates how many tokens overlap between each
subsequence.
The default value is `-1`, indicating no windowing or spanning occurs.
**Note:** When your typical input is just slightly larger than `max_sequence_length`, it may be best to simply truncate;
there will be very little information in the second subsequence.
`truncate`:::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `balanced`: One or both of the first and second sequences may be truncated so as to balance the tokens included from both sequences.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence, that sequence is truncated.

`with_special_tokens`:::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in DeBERTa-style tokenization are:
* `[CLS]`: The first token of the sequence being classified.
* `[SEP]`: Indicates sequence separation and sequence end.
`roberta`::
(Optional, object)
RoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of roberta**
`add_prefix_space`:::
(Optional, boolean)
Specifies if the tokenization should prefix a space to the tokenized input to the model.
`max_sequence_length`:::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
`span`:::
(Optional, integer)
When `truncate` is `none`, you can partition longer text sequences
for inference. The value indicates how many tokens overlap between each
subsequence.
The default value is `-1`, indicating no windowing or spanning occurs.
**Note:** When your typical input is just slightly larger than `max_sequence_length`, it may be best to simply truncate;
there will be very little information in the second subsequence.
`truncate`:::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

`with_special_tokens`:::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
`mpnet`::
(Optional, object)
MPNet-style tokenization is to be performed with the enclosed settings.
**Properties of mpnet**
`do_lower_case`:::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`:::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
`span`:::
(Optional, integer)
When `truncate` is `none`, you can partition longer text sequences
for inference. The value indicates how many tokens overlap between each
subsequence.
The default value is `-1`, indicating no windowing or spanning occurs.
**Note:** When your typical input is just slightly larger than `max_sequence_length`, it may be best to simply truncate;
there will be very little information in the second subsequence.
`truncate`:::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

`with_special_tokens`:::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in MPNet-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
`xlm_roberta`::
(Optional, object)
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of xlm_roberta**
`max_sequence_length`:::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
`span`:::
(Optional, integer)
When `truncate` is `none`, you can partition longer text sequences
for inference. The value indicates how many tokens overlap between each
subsequence.
The default value is `-1`, indicating no windowing or spanning occurs.
**Note:** When your typical input is just slightly larger than `max_sequence_length`, it may be best to simply truncate;
there will be very little information in the second subsequence.
`truncate`:::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

`with_special_tokens`:::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
`bert_ja`::
(Optional, object)
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
**Properties of bert_ja**
`do_lower_case`:::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`:::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
`span`:::
(Optional, integer)
When `truncate` is `none`, you can partition longer text sequences
for inference. The value indicates how many tokens overlap between each
subsequence.
The default value is `-1`, indicating no windowing or spanning occurs.
**Note:** When your typical input is just slightly larger than `max_sequence_length`, it may be best to simply truncate;
there will be very little information in the second subsequence.
`truncate`:::
(Optional, string)
Indicates how tokens are truncated when they exceed `max_sequence_length`.
The default value is `first`.
* `none`: No truncation occurs; the inference request receives an error.
* `first`: Only the first sequence is truncated.
* `second`: Only the second sequence is truncated. If there is just one sequence,
					 that sequence is truncated.

**Note:** For `zero_shot_classification`, the hypothesis sequence is always the second
sequence. Therefore, do not use `second` in this case.

`with_special_tokens`:::
(Optional, boolean)
Tokenize with special tokens if `true`.

## Examples

### Preprocessor examples

The example below shows a `frequency_encoding` preprocessor object:

```js
{
   "frequency_encoding":{
      "field":"FlightDelayType",
      "feature_name":"FlightDelayType_frequency",
      "frequency_map":{
         "Carrier Delay":0.6007414737092798,
         "NAS Delay":0.6007414737092798,
         "Weather Delay":0.024573576178086153,
         "Security Delay":0.02476631010889467,
         "No Delay":0.6007414737092798,
         "Late Aircraft Delay":0.6007414737092798
      }
   }
}
```

The next example shows a `one_hot_encoding` preprocessor object:

```js
{
   "one_hot_encoding":{
      "field":"FlightDelayType",
      "hot_map":{
         "Carrier Delay":"FlightDelayType_Carrier Delay",
         "NAS Delay":"FlightDelayType_NAS Delay",
         "No Delay":"FlightDelayType_No Delay",
         "Late Aircraft Delay":"FlightDelayType_Late Aircraft Delay"
      }
   }
}
```

This example shows a `target_mean_encoding` preprocessor object:

```js
{
   "target_mean_encoding":{
      "field":"FlightDelayType",
      "feature_name":"FlightDelayType_targetmean",
      "target_map":{
         "Carrier Delay":39.97465788139886,
         "NAS Delay":39.97465788139886,
         "Security Delay":203.171206225681,
         "Weather Delay":187.64705882352948,
         "No Delay":39.97465788139886,
         "Late Aircraft Delay":39.97465788139886
      },
      "default_value":158.17995752420433
   }
}
```

### Model examples

The first example shows a `trained_model` object:

```js
{
   "tree":{
      "feature_names":[
         "DistanceKilometers",
         "FlightTimeMin",
         "FlightDelayType_NAS Delay",
         "Origin_targetmean",
         "DestRegion_targetmean",
         "DestCityName_targetmean",
         "OriginAirportID_targetmean",
         "OriginCityName_frequency",
         "DistanceMiles",
         "FlightDelayType_Late Aircraft Delay"
      ],
      "tree_structure":[
         {
            "decision_type":"lt",
            "threshold":9069.33437193022,
            "split_feature":0,
            "split_gain":4112.094574306927,
            "node_index":0,
            "default_left":true,
            "left_child":1,
            "right_child":2
         },
         ...
         {
            "node_index":9,
            "leaf_value":-27.68987349695448
         },
         ...
      ],
      "target_type":"regression"
   }
}
```

The following example shows an `ensemble` model object:

```js
"ensemble":{
   "feature_names":[
      ...
   ],
   "trained_models":[
      {
         "tree":{
            "feature_names":[],
            "tree_structure":[
               {
                  "decision_type":"lte",
                  "node_index":0,
                  "leaf_value":47.64069875778043,
                  "default_left":false
               }
            ],
            "target_type":"regression"
         }
      },
      ...
   ],
   "aggregate_output":{
      "weighted_sum":{
         "weights":[
            ...
         ]
      }
   },
   "target_type":"regression"
}
```

### Aggregated output example

Example of a `logistic_regression` object:

```js
"aggregate_output" : {
  "logistic_regression" : {
    "weights" : [2.0, 1.0, .5, -1.0, 5.0, 1.0, 1.0]
  }
}
```

Example of a `weighted_sum` object:

```js
"aggregate_output" : {
  "weighted_sum" : {
    "weights" : [1.0, -1.0, .5, 1.0, 5.0]
  }
}
```

Example of a `weighted_mode` object:

```js
"aggregate_output" : {
  "weighted_mode" : {
    "weights" : [1.0, 1.0, 1.0, 1.0, 1.0]
  }
}
```

Example of an `exponent` object:

```js
"aggregate_output" : {
  "exponent" : {
    "weights" : [1.0, 1.0, 1.0, 1.0, 1.0]
  }
}
```

### Trained models JSON schema

For the full JSON schema of trained models,
[click here](https://github.com/elastic/ml-json-schemas).
