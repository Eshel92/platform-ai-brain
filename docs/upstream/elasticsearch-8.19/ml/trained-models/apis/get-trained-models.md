<!-- Converted from ml/trained-models/apis/get-trained-models.asciidoc (AsciiDoc). Includes are inlined. -->

# Get trained models API

**New API reference**
For the most up-to-date API details, refer to [Machine learning trained model APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-trained-model).

Retrieves configuration information for a trained model.

## Request

`GET _ml/trained_models/` +

`GET _ml/trained_models/<model_id>` +

`GET _ml/trained_models/_all` +

`GET _ml/trained_models/<model_id1>,<model_id2>` +

`GET _ml/trained_models/<model_id_pattern*>`

## Prerequisites

Requires the `monitor_ml` cluster privilege. This privilege is included in the
`machine_learning_user` built-in role.

## Path parameters

`<model_id>`::
(Optional, string)
The unique identifier of the trained model or a model alias.
You can get information for multiple trained models in a single API request by
using a comma-separated list of model IDs or a wildcard expression.

## Query parameters

`allow_no_match`::
(Optional, Boolean)
Specifies what to do when the request:
* Contains wildcard expressions and there are no models that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty array when there are no
matches and the subset of results when there are partial matches. If this
parameter is `false`, the request returns a `404` status code when there are no
matches or only partial matches.
`decompress_definition`::
(Optional, Boolean)
Specifies whether the included model definition should be returned as a JSON map
(`true`) or in a custom compressed format (`false`). Defaults to `true`.

`exclude_generated`::
(Optional, Boolean)
Indicates if certain fields should be removed from the configuration on
retrieval. This allows the configuration to be in an acceptable format to be retrieved
and then added to another cluster. Default is false.
`from`::
(Optional, integer)
Skips the specified number of models. The default value is `0`.
`include`::
(Optional, string)
A comma delimited string of optional fields to include in the response body. The
default value is empty, indicating no optional fields are included. Valid
options are:
 - `definition`: Includes the model definition.
 - `feature_importance_baseline`: Includes the baseline for {feat-imp} values.
 - `hyperparameters`: Includes the information about hyperparameters used to
    train the model. This information consists of the value, the absolute and
    relative importance of the hyperparameter as well as an indicator of whether
    it was specified by the user or tuned during hyperparameter optimization.
 - `total_feature_importance`: Includes the total {feat-imp} for the training
   data set.
 - `definition_status`: Includes the field `fully_defined` indicating if the
full model definition is present.
The baseline and total {feat-imp} values are returned in the `metadata` field
in the response body.

`size`::
(Optional, integer)
Specifies the maximum number of models to obtain. The default value
is `100`.
`tags`::
(Optional, string)
A comma delimited string of tags. A trained model can have many tags, or none.
When supplied, only trained models that contain all the supplied tags are
returned.

## Response body

`trained_model_configs`::
(array)
An array of trained model resources, which are sorted by the `model_id` value in
ascending order.
**Properties of trained model resources**
`created_by`:::
(string)
The creator of the trained model.

`create_time`:::
(time units)
The time when the trained model was created.

`default_field_map` :::
(object)
A string object that contains the default field map to use when inferring
against the model. For example, {dfanalytics} may train the model on a specific
multi-field `foo.keyword`. The analytics job would then supply a default field
map entry for `"foo" : "foo.keyword"`.
Any field map described in the inference configuration takes precedence.

`description`:::
(string)
The free-text description of the trained model.

`model_size_bytes`:::
(integer)
The estimated model size in bytes to keep the trained model in memory.
This parameter applies only to {dfanalytics} trained models.

`estimated_operations`:::
(integer)
The estimated number of operations to use the trained model.

`inference_config`:::
(object)
The default configuration for inference. This can be either a `regression`
or `classification` configuration. It must match the `target_type` of the
underlying `definition.trained_model`.
**Properties of `inference_config`**
=====
`classification`::::
(object)
Classification configuration for inference.
**Properties of classification inference**
======
`num_top_classes`:::
(integer)
Specifies the number of top class predictions to return. Defaults to 0.
`num_top_feature_importance_values`:::
(integer)
Specifies the maximum number of
{ml-docs}/ml-feature-importance.html[{feat-imp}] values per document. Defaults
to 0 which means no {feat-imp} calculation occurs.
`prediction_field_type`:::
(string)
Specifies the type of the predicted field to write.
Valid values are: `string`, `number`, `boolean`. When `boolean` is provided
`1.0` is transformed to `true` and `0.0` to `false`.
`results_field`:::
(string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to `predicted_value`.
`top_classes_results_field`:::
(string)
Specifies the field to which the top classes are written. Defaults to
`top_classes`.
======
`fill_mask`::::
(Optional, object)
Configuration for a fill_mask natural language processing (NLP) task. The
fill_mask task works with models optimized for a fill mask action. For example,
for BERT models, the following text may be provided: "The capital of France is
[MASK].". The response indicates the value most likely to replace `[MASK]`. In
this instance, the most probable token is `paris`.
**Properties of fill_mask inference**
======
`mask_token`::::
(Optional, string)
The string/token which will be removed from incoming documents and replaced with the inference prediction(s). In a response, this field contains the mask token for the specified model/tokenizer. Each model and tokenizer has a predefined mask token which cannot be changed. Thus, it is recommended not to set this value in requests. However, if this field is present in a request, its value must match the predefined value for that model/tokenizer, otherwise the request will fail.
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
=======
`bert`::::
(Optional, object)
BERT-style tokenization is to be performed with the enclosed settings.
**Properties of bert**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in BERT-style tokenization are:
* `[CLS]`: The first token of the sequence being classified.
* `[SEP]`: Indicates sequence separation.
========
`roberta`::::
(Optional, object)
RoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of roberta**
========
`add_prefix_space`::::
(Optional, boolean)
Specifies if the tokenization should prefix a space to the tokenized input to the model.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`mpnet`::::
(Optional, object)
MPNet-style tokenization is to be performed with the enclosed settings.
**Properties of mpnet**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in MPNet-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`xlm_roberta`::::
(Optional, object)
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of xlm_roberta**
========
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`bert_ja`::::
(Optional, object)
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
**Properties of bert_ja**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens if `true`.
========
=======
`vocabulary`::::
(Optional, object)
The configuration for retrieving the vocabulary of the model. The vocabulary is
then used at inference time. This information is usually provided automatically
by storing vocabulary in a known, internally managed index.
**Properties of vocabulary**
=======
`index`::::
(Required, string)
The index where the vocabulary is stored.
=======
======

`ner`::::
(Optional, object)
Configures a named entity recognition (NER) task. NER is a special case of token
classification. Each token in the sequence is classified according to the
provided classification labels. Currently, the NER task requires the
`classification_labels` Inside-Outside-Beginning (IOB) formatted labels. Only
person, organization, location, and miscellaneous are supported.
**Properties of ner inference**
======
`classification_labels`::::
(Optional, string)
An array of classification labels. NER supports only
Inside-Outside-Beginning labels (IOB) and only persons, organizations, locations,
and miscellaneous. For example:
`["O", "B-PER", "I-PER", "B-ORG", "I-ORG", "B-LOC", "I-LOC", "B-MISC", "I-MISC"]`.

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
=======
`bert`::::
(Optional, object)
BERT-style tokenization is to be performed with the enclosed settings.
**Properties of bert**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in BERT-style tokenization are:
* `[CLS]`: The first token of the sequence being classified.
* `[SEP]`: Indicates sequence separation.
========
`roberta`::::
(Optional, object)
RoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of roberta**
========
`add_prefix_space`::::
(Optional, boolean)
Specifies if the tokenization should prefix a space to the tokenized input to the model.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`mpnet`::::
(Optional, object)
MPNet-style tokenization is to be performed with the enclosed settings.
**Properties of mpnet**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in MPNet-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`xlm_roberta`::::
(Optional, object)
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of xlm_roberta**
========
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`bert_ja`::::
(Optional, object)
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
**Properties of bert_ja**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens if `true`.
========
=======
`vocabulary`::::
(Optional, object)
The configuration for retrieving the vocabulary of the model. The vocabulary is
then used at inference time. This information is usually provided automatically
by storing vocabulary in a known, internally managed index.
**Properties of vocabulary**
=======
`index`::::
(Required, string)
The index where the vocabulary is stored
=======
======

`pass_through`::::
(Optional, object)
Configures a `pass_through` task. This task is useful for debugging as no
post-processing is done to the inference output and the raw pooling layer
results are returned to the caller.
**Properties of pass_through inference**
======
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
=======
`bert`::::
(Optional, object)
BERT-style tokenization is to be performed with the enclosed settings.
**Properties of bert**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in BERT-style tokenization are:
* `[CLS]`: The first token of the sequence being classified.
* `[SEP]`: Indicates sequence separation.
========
`roberta`::::
(Optional, object)
RoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of roberta**
========
`add_prefix_space`::::
(Optional, boolean)
Specifies if the tokenization should prefix a space to the tokenized input to the model.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`mpnet`::::
(Optional, object)
MPNet-style tokenization is to be performed with the enclosed settings.
**Properties of mpnet**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in MPNet-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`xlm_roberta`::::
(Optional, object)
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of xlm_roberta**
========
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`bert_ja`::::
(Optional, object)
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
**Properties of bert_ja**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens if `true`.
========
=======
`vocabulary`::::
(Optional, object)
The configuration for retrieving the vocabulary of the model. The vocabulary is
then used at inference time. This information is usually provided automatically
by storing vocabulary in a known, internally managed index.
**Properties of vocabulary**
=======
`index`::::
(Required, string)
The index where the vocabulary is stored.
=======
======

`regression`::::
(object)
Regression configuration for inference.
**Properties of regression inference**
======
`num_top_feature_importance_values`:::
(integer)
Specifies the maximum number of
{ml-docs}/ml-feature-importance.html[{feat-imp}] values per document.
By default, it is zero and no {feat-imp} calculation occurs.
`results_field`:::
(string)
The field that is added to incoming documents to contain the inference
prediction. Defaults to `predicted_value`.
======
`text_classification`::::
(Optional, object)
A text classification task. Text classification classifies a provided text
sequence into previously known target classes. A specific example of this is
sentiment analysis, which returns the likely target classes indicating text
sentiment, such as "sad", "happy", or "angry".
**Properties of text_classification inference**
======
`classification_labels`::::
(Optional, string)
An array of classification labels.

`num_top_classes`::::
(Optional, integer)
Specifies the number of top class predictions to return. Defaults to all classes (-1).

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
=======
`bert`::::
(Optional, object)
BERT-style tokenization is to be performed with the enclosed settings.
**Properties of bert**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in BERT-style tokenization are:
* `[CLS]`: The first token of the sequence being classified.
* `[SEP]`: Indicates sequence separation.
========
`roberta`::::
(Optional, object)
RoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of roberta**
========
`add_prefix_space`::::
(Optional, boolean)
Specifies if the tokenization should prefix a space to the tokenized input to the model.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`mpnet`::::
(Optional, object)
MPNet-style tokenization is to be performed with the enclosed settings.
**Properties of mpnet**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in MPNet-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`xlm_roberta`::::
(Optional, object)
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of xlm_roberta**
========
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`bert_ja`::::
(Optional, object)
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
**Properties of bert_ja**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens if `true`.
========
=======

`vocabulary`::::
(Optional, object)
The configuration for retrieving the vocabulary of the model. The vocabulary is
then used at inference time. This information is usually provided automatically
by storing vocabulary in a known, internally managed index.
**Properties of vocabulary**
=======
`index`::::
(Required, string)
The index where the vocabulary is stored.
=======
======
`text_embedding`::::
(Object, optional)
Text embedding takes an input sequence and transforms it into a vector of
numbers. These embeddings capture not simply tokens, but semantic meanings and
context. These embeddings can be used in a dense vector field
for powerful insights.
**Properties of text_embedding inference**
======
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
**Properties of tokenization**
=======
`bert`::::
(Optional, object)
BERT-style tokenization is to be performed with the enclosed settings.
**Properties of bert**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in BERT-style tokenization are:
* `[CLS]`: The first token of the sequence being classified.
* `[SEP]`: Indicates sequence separation.
========
`roberta`::::
(Optional, object)
RoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of roberta**
========
`add_prefix_space`::::
(Optional, boolean)
Specifies if the tokenization should prefix a space to the tokenized input to the model.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`mpnet`::::
(Optional, object)
MPNet-style tokenization is to be performed with the enclosed settings.
**Properties of mpnet**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in MPNet-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`xlm_roberta`::::
(Optional, object)
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of xlm_roberta**
========
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`bert_ja`::::
(Optional, object)
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
**Properties of bert_ja**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens if `true`.
========
=======
`vocabulary`::::
(Optional, object)
The configuration for retrieving the vocabulary of the model. The vocabulary is
then used at inference time. This information is usually provided automatically
by storing vocabulary in a known, internally managed index.
**Properties of vocabulary**
=======
`index`::::
(Required, string)
The index where the vocabulary is stored.
=======
======
`text_similarity`::::
(Object, optional)
Text similarity takes an input sequence and compares it with another input sequence. This is commonly referred to
as cross-encoding. This task is useful for ranking document text when comparing it to another provided text input.
**Properties of text_similarity inference**
======
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
**Properties of tokenization**
=======
`bert`::::
(Optional, object)
BERT-style tokenization is to be performed with the enclosed settings.
**Properties of bert**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in BERT-style tokenization are:
* `[CLS]`: The first token of the sequence being classified.
* `[SEP]`: Indicates sequence separation.
========
`roberta`::::
(Optional, object)
RoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of roberta**
========
`add_prefix_space`::::
(Optional, boolean)
Specifies if the tokenization should prefix a space to the tokenized input to the model.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`mpnet`::::
(Optional, object)
MPNet-style tokenization is to be performed with the enclosed settings.
**Properties of mpnet**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in MPNet-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`xlm_roberta`::::
(Optional, object)
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of xlm_roberta**
========
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`bert_ja`::::
(Optional, object)
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
**Properties of bert_ja**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens if `true`.
========
=======
`vocabulary`::::
(Optional, object)
The configuration for retrieving the vocabulary of the model. The vocabulary is
then used at inference time. This information is usually provided automatically
by storing vocabulary in a known, internally managed index.
**Properties of vocabulary**
=======
`index`::::
(Required, string)
The index where the vocabulary is stored.
=======
======
`zero_shot_classification`::::
(Object, optional)
Configures a zero-shot classification task. Zero-shot classification allows for
text classification to occur without pre-determined labels. At inference time,
it is possible to adjust the labels to classify. This makes this type of model
and task exceptionally flexible.
If consistently classifying the same labels, it may be better to use a
fine-tuned text classification model.
**Properties of zero_shot_classification inference**
======
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
=======
`bert`::::
(Optional, object)
BERT-style tokenization is to be performed with the enclosed settings.
**Properties of bert**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in BERT-style tokenization are:
* `[CLS]`: The first token of the sequence being classified.
* `[SEP]`: Indicates sequence separation.
========
`roberta`::::
(Optional, object)
RoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of roberta**
========
`add_prefix_space`::::
(Optional, boolean)
Specifies if the tokenization should prefix a space to the tokenized input to the model.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`mpnet`::::
(Optional, object)
MPNet-style tokenization is to be performed with the enclosed settings.
**Properties of mpnet**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in MPNet-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`xlm_roberta`::::
(Optional, object)
experimental:[] XLMRoBERTa-style tokenization is to be performed with the enclosed settings.
**Properties of xlm_roberta**
========
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens. The tokens typically included in RoBERTa-style tokenization are:
* `<s>`: The first token of the sequence being classified.
* `</s>`: Indicates sequence separation.
========
`bert_ja`::::
(Optional, object)
experimental:[] BERT-style tokenization for Japanese text is to be performed
with the enclosed settings.
**Properties of bert_ja**
========
`do_lower_case`::::
(Optional, boolean)
Specifies if the tokenization lower case the text sequence when building the
tokens.
`max_sequence_length`::::
(Optional, integer)
Specifies the maximum number of tokens allowed to be output by the tokenizer.
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

`with_special_tokens`::::
(Optional, boolean)
Tokenize with special tokens if `true`.
========
=======
`vocabulary`::::
(Optional, object)
The configuration for retrieving the vocabulary of the model. The vocabulary is
then used at inference time. This information is usually provided automatically
by storing vocabulary in a known, internally managed index.
**Properties of vocabulary**
=======
`index`::::
(Required, string)
The index where the vocabulary is stored.
=======
======
=====

`input`:::
(object)
The input field names for the model definition.
**Properties of `input`**
=====
`field_names`::::
(string)
An array of input field names for the model.
=====

`fully_defined`::
(boolean)
True if the full model definition is present.
This field is only present if `include=definition_status` was specified in the request.

`location`::
(Optional, object)
The model definition location. Must be provided if the `definition` or `compressed_definition` are not
provided.
**Properties of `location`**
=====
`index`:::
(Required, object)
Indicates that the model definition is stored in an index. It is required to be empty as
the index for storing model definitions is configured automatically.
=====

`license_level`::
(string)
The license level of the trained model.

`metadata`::
(object)
An object containing metadata about the trained model. For example, models
created by {dfanalytics} contain `analysis_config` and `input` objects.
**Properties of metadata**
=====
`feature_importance_baseline`:::
(object)
An object that contains the baseline for {feat-imp} values. For {reganalysis},
it is a single value. For {classanalysis}, there is a value for each class.

`hyperparameters`:::
(array)
List of the available hyperparameters optimized during the
`fine_parameter_tuning` phase as well as specified by the user.
**Properties of hyperparameters**
======
`absolute_importance`::::
(double)
A positive number showing how much the parameter influences the variation of the
{ml-docs}/dfa-regression-lossfunction.html[loss function]. For
hyperparameters with values that are not specified by the user but tuned during
hyperparameter optimization.

`max_trees`::::
(integer)
The maximum number of decision trees in the forest. The maximum value is 2000.
By default, this value is calculated during hyperparameter optimization.
`name`::::
(string)
Name of the hyperparameter.

`relative_importance`::::
(double)
A number between 0 and 1 showing the proportion of influence on the variation of
the loss function among all tuned hyperparameters. For hyperparameters with
values that are not specified by the user but tuned during hyperparameter
optimization.

`supplied`::::
(Boolean)
Indicates if the hyperparameter is specified by the user (`true`) or optimized
(`false`).

`value`::::
(double)
The value of the hyperparameter, either optimized or specified by the user.

======

`total_feature_importance`:::
(array)
An array of the total {feat-imp} for each feature used from
the training data set. This array of objects is returned if {dfanalytics} trained
the model and the request includes `total_feature_importance` in the `include`
request parameter.
**Properties of total {feat-imp}**
======

`feature_name`:::
(string)
The feature for which this importance was calculated.
`importance`:::
(object)
A collection of {feat-imp} statistics related to the training data set for this particular feature.
**Properties of {feat-imp}**
=======
`mean_magnitude`:::
(double)
The average magnitude of this feature across all the training data.
This value is the average of the absolute values of the importance
for this feature.
`max`:::
(integer)
The maximum importance value across all the training data for this
feature.
`min`:::
(integer)
The minimum importance value across all the training data for this
feature.
=======

`classes`:::
(array)
If the trained model is a classification model, {feat-imp} statistics are gathered
per target class value.
**Properties of class {feat-imp}**

=======

`class_name`:::
(string)
The target class value. Could be a string, boolean, or number.

`importance`:::
(object)
A collection of {feat-imp} statistics related to the training data set for this particular feature.
**Properties of {feat-imp}**
========
`mean_magnitude`:::
(double)
The average magnitude of this feature across all the training data.
This value is the average of the absolute values of the importance
for this feature.
`max`:::
(int)
The maximum importance value across all the training data for this
feature.
`min`:::
(int)
The minimum importance value across all the training data for this
feature.
========

=======

======
=====

`model_id`::
(string)
Identifier for the trained model.

`model_type`::
(Optional, string)
The created model type. By default the model type is `tree_ensemble`.
Appropriate types are:
* `tree_ensemble`: The model definition is an ensemble model of decision trees.
* `lang_ident`: A special type reserved for language identification models.
* `pytorch`: The stored definition is a PyTorch (specifically a TorchScript) model. Currently only
NLP models are supported.

`tags`::
(string)
A comma delimited string of tags. A trained model can have many tags, or none.

`version`::
(string)
The machine learning configuration version number at which the trained model was created.

**Note:** From Elasticsearch 8.10.0,  a new version number is used to
track the configuration and state changes in the machine learning plugin. This new
version number is decoupled from the product version and will increment
independently. The `version` value represents the new version number.

## Response codes

`400`::
  If `include_model_definition` is `true`, this code indicates that more than
  one models match the ID pattern.

`404` (Missing resources)::
  If `allow_no_match` is `false`, this code indicates that there are no
  resources that match the request or only partial matches for the request.

## Examples

The following example gets configuration information for all the trained models:

```console
GET _ml/trained_models/
```
