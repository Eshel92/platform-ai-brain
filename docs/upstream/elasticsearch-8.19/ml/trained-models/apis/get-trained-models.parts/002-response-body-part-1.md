<!-- Part 2 of 4 of ml/trained-models/apis/get-trained-models.md (split because the page is big). -->

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
