<!-- Converted from ml/trained-models/apis/put-trained-model-vocabulary.asciidoc (AsciiDoc). Includes are inlined. -->

# Create trained model vocabulary API

**New API reference**
For the most up-to-date API details, refer to [Machine learning trained model APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-trained-model).

Creates a trained model vocabulary.
This is supported only for natural language processing (NLP) models.

## Request

`PUT _ml/trained_models/<model_id>/vocabulary/`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the
`machine_learning_admin` built-in role.

## Description

The vocabulary is stored in the index as described in
`inference_config.*.vocabulary` of the trained model definition.

## Path parameters

`<model_id>`::
(Required, string)
The unique identifier of the trained model.

## Request body

`vocabulary`::
(array)
The model vocabulary. Must not be empty.

`merges`::
(Optional, array)
The model merges used in byte-pair encoding. The merges must be sub-token pairs, space delimited, and in order of
preference. Example: ["f o", "fo o"]. Must be provided for RoBERTa and BART style models.

`scores`::
(Optional, array)
Vocabulary value scores used by sentence-piece tokenization. Must have the same length as `vocabulary`.
Required for unigram sentence-piece tokenized models like XLMRoberta and T5.

## Examples

The following example shows how to create a model vocabulary for a
previously stored trained model configuration.

```console
PUT _ml/trained_models/elastic__distilbert-base-uncased-finetuned-conll03-english/vocabulary
{
  "vocabulary": [
    "[PAD]",
    "[unused0]",
    ...
  ]
}
```

The API returns the following results:

```console-result
{
    "acknowledged": true
}
```
