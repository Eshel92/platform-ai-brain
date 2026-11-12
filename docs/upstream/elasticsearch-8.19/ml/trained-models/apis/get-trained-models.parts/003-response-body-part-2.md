<!-- Part 3 of 4 of ml/trained-models/apis/get-trained-models.md (split because the page is big). -->

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
