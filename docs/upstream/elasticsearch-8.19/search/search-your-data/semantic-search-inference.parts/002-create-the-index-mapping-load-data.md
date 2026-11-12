<!-- Part 2 of 5 of search/search-your-data/semantic-search-inference.md (split because the page is big). -->

#### Create the index mapping

The mapping of the destination index - the index that contains the embeddings that the model will create based on your input text - must be created.
The destination index must have a field with the `dense_vector` field type for most models and the `sparse_vector` field type for the sparse vector models like in the case of the `elasticsearch` service to index the output of the used model.

```console
PUT cohere-embeddings
{
  "mappings": {
    "properties": {
      "content_embedding": { <1>
        "type": "dense_vector", <2>
        "dims": 1024, <3>
        "element_type": "byte"
      },
      "content": { <4>
        "type": "text" <5>
      }
    }
  }
}
```
<1> The name of the field to contain the generated tokens. It must be refrenced
in the inference pipeline configuration in the next step.
<2> The field to contain the tokens is a `dense_vector` field.
<3> The output dimensions of the model. Find this value in the
[Cohere documentation](https://docs.cohere.com/reference/embed) of the model you
use.
<4> The name of the field from which to create the dense vector representation.
In this example, the name of the field is `content`. It must be referenced in
the inference pipeline configuration in the next step.
<5> The field type which is text in this example.

```console
PUT elser-embeddings
{
  "mappings": {
    "properties": {
      "content_embedding": { <1>
        "type": "sparse_vector" <2>
      },
      "content": { <3>
        "type": "text" <4>
      }
    }
  }
}
```
<1> The name of the field to contain the generated tokens. It must be refrenced
in the inference pipeline configuration in the next step.
<2> The field to contain the tokens is a `sparse_vector` field for ELSER.
<3> The name of the field from which to create the dense vector representation.
In this example, the name of the field is `content`. It must be referenced in
the inference pipeline configuration in the next step.
<4> The field type which is text in this example.

```console
PUT hugging-face-embeddings
{
  "mappings": {
    "properties": {
      "content_embedding": { <1>
        "type": "dense_vector", <2>
        "dims": 768, <3>
        "element_type": "float"
      },
      "content": { <4>
        "type": "text" <5>
      }
    }
  }
}
```
<1> The name of the field to contain the generated tokens. It must be referenced
in the inference pipeline configuration in the next step.
<2> The field to contain the tokens is a `dense_vector` field.
<3> The output dimensions of the model. Find this value in the
[HuggingFace model documentation](https://huggingface.co/sentence-transformers/all-mpnet-base-v2).
<4> The name of the field from which to create the dense vector representation.
In this example, the name of the field is `content`. It must be referenced in
the inference pipeline configuration in the next step.
<5> The field type which is text in this example.

```console
PUT openai-embeddings
{
  "mappings": {
    "properties": {
      "content_embedding": { <1>
        "type": "dense_vector", <2>
        "dims": 1536, <3>
        "element_type": "float",
        "similarity": "dot_product" <4>
      },
      "content": { <5>
        "type": "text" <6>
      }
    }
  }
}
```
<1> The name of the field to contain the generated tokens. It must be referenced
in the inference pipeline configuration in the next step.
<2> The field to contain the tokens is a `dense_vector` field.
<3> The output dimensions of the model. Find this value in the
[OpenAI documentation](https://platform.openai.com/docs/guides/embeddings/embedding-models)
of the model you use.
<4> The faster` dot_product` function can be used to calculate similarity
because OpenAI embeddings are normalised to unit length. You can check the
[OpenAI docs](https://platform.openai.com/docs/guides/embeddings/which-distance-function-should-i-use)
about which similarity function to use.
<5> The name of the field from which to create the dense vector representation.
In this example, the name of the field is `content`. It must be referenced in
the inference pipeline configuration in the next step.
<6> The field type which is text in this example.

```console
PUT azure-openai-embeddings
{
  "mappings": {
    "properties": {
      "content_embedding": { <1>
        "type": "dense_vector", <2>
        "dims": 1536, <3>
        "element_type": "float",
        "similarity": "dot_product" <4>
      },
      "content": { <5>
        "type": "text" <6>
      }
    }
  }
}
```
<1> The name of the field to contain the generated tokens. It must be referenced
in the inference pipeline configuration in the next step.
<2> The field to contain the tokens is a `dense_vector` field.
<3> The output dimensions of the model. Find this value in the
[Azure OpenAI documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#embeddings-models)
of the model you use.
<4> For Azure OpenAI embeddings, the `dot_product` function should be used to
calculate similarity as Azure OpenAI embeddings are normalised to unit length.
See the
[Azure OpenAI embeddings](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/understand-embeddings)
documentation for more information on the model specifications.
<5> The name of the field from which to create the dense vector representation.
In this example, the name of the field is `content`. It must be referenced in
the inference pipeline configuration in the next step.
<6> The field type which is text in this example.

```console
PUT azure-ai-studio-embeddings
{
  "mappings": {
    "properties": {
      "content_embedding": { <1>
        "type": "dense_vector", <2>
        "dims": 1536, <3>
        "element_type": "float",
        "similarity": "dot_product" <4>
      },
      "content": { <5>
        "type": "text" <6>
      }
    }
  }
}
```
<1> The name of the field to contain the generated tokens. It must be referenced
in the inference pipeline configuration in the next step.
<2> The field to contain the tokens is a `dense_vector` field.
<3> The output dimensions of the model. This value may be found on the model card in your Azure AI Studio deployment.
<4> For Azure AI Studio embeddings, the `dot_product` function should be used to
calculate similarity.
<5> The name of the field from which to create the dense vector representation.
In this example, the name of the field is `content`. It must be referenced in
the inference pipeline configuration in the next step.
<6> The field type which is text in this example.

```console
PUT google-vertex-ai-embeddings
{
  "mappings": {
    "properties": {
      "content_embedding": { <1>
        "type": "dense_vector", <2>
        "dims": 768, <3>
        "element_type": "float",
        "similarity": "dot_product" <4>
      },
      "content": { <5>
        "type": "text" <6>
      }
    }
  }
}
```
<1> The name of the field to contain the generated embeddings. It must be referenced in the inference pipeline configuration in the next step.
<2> The field to contain the embeddings is a `dense_vector` field.
<3> The output dimensions of the model. This value may be found on the [Google Vertex AI model reference](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api).
The inference API attempts to calculate the output dimensions automatically if `dims` are not specified.
<4> For Google Vertex AI embeddings, the `dot_product` function should be used to calculate similarity.
<5> The name of the field from which to create the dense vector representation.
In this example, the name of the field is `content`. It must be referenced in
the inference pipeline configuration in the next step.
<6> The field type which is `text` in this example.

```console
PUT mistral-embeddings
{
  "mappings": {
    "properties": {
      "content_embedding": { <1>
        "type": "dense_vector", <2>
        "dims": 1024, <3>
        "element_type": "float",
        "similarity": "dot_product" <4>
      },
      "content": { <5>
        "type": "text" <6>
      }
    }
  }
}
```
<1> The name of the field to contain the generated tokens. It must be referenced
in the inference pipeline configuration in the next step.
<2> The field to contain the tokens is a `dense_vector` field.
<3> The output dimensions of the model. This value may be found on the [Mistral model reference](https://docs.mistral.ai/getting-started/models/).
<4> For Mistral embeddings, the `dot_product` function should be used to
calculate similarity.
<5> The name of the field from which to create the dense vector representation.
In this example, the name of the field is `content`. It must be referenced in
the inference pipeline configuration in the next step.
<6> The field type which is text in this example.

```console
PUT amazon-bedrock-embeddings
{
  "mappings": {
    "properties": {
      "content_embedding": { <1>
        "type": "dense_vector", <2>
        "dims": 1024, <3>
        "element_type": "float",
        "similarity": "dot_product" <4>
      },
      "content": { <5>
        "type": "text" <6>
      }
    }
  }
}
```
<1> The name of the field to contain the generated tokens. It must be referenced
in the inference pipeline configuration in the next step.
<2> The field to contain the tokens is a `dense_vector` field.
<3> The output dimensions of the model. This value may be different depending on the underlying model used.
See the [Amazon Titan model](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-multiemb-models.html) or the [Cohere Embeddings model](https://docs.cohere.com/reference/embed) documentation.
<4> For Amazon Bedrock embeddings, the `dot_product` function should be used to
calculate similarity for Amazon titan models, or `cosine` for Cohere models.
<5> The name of the field from which to create the dense vector representation.
In this example, the name of the field is `content`. It must be referenced in
the inference pipeline configuration in the next step.
<6> The field type which is text in this example.

```console
PUT alibabacloud-ai-search-embeddings
{
  "mappings": {
    "properties": {
      "content_embedding": { <1>
        "type": "dense_vector", <2>
        "dims": 1024, <3>
        "element_type": "float"
      },
      "content": { <4>
        "type": "text" <5>
      }
    }
  }
}
```
<1> The name of the field to contain the generated tokens. It must be referenced
in the inference pipeline configuration in the next step.
<2> The field to contain the tokens is a `dense_vector` field.
<3> The output dimensions of the model. This value may be different depending on the underlying model used.
See the [AlibabaCloud AI Search embedding model](https://help.aliyun.com/zh/open-search/search-platform/developer-reference/text-embedding-api-details) documentation.
<4> The name of the field from which to create the dense vector representation.
In this example, the name of the field is `content`. It must be referenced in
the inference pipeline configuration in the next step.
<5> The field type which is text in this example.


#### Create an ingest pipeline with an inference processor

Create an ingest pipeline with an inference processor and use the model you created above to infer against the data that is being ingested in the pipeline.

```console
PUT _ingest/pipeline/cohere_embeddings_pipeline
{
  "processors": [
    {
      "inference": {
        "model_id": "cohere_embeddings", <1>
        "input_output": { <2>
          "input_field": "content",
          "output_field": "content_embedding"
        }
      }
    }
  ]
}
```
<1> The name of the inference endpoint you created by using the
put-inference-api, it's referred to as `inference_id` in that step.
<2> Configuration object that defines the `input_field` for the inference process
and the `output_field` that will contain the inference results.

```console
PUT _ingest/pipeline/elser_embeddings_pipeline
{
  "processors": [
    {
      "inference": {
        "model_id": "elser_embeddings", <1>
        "input_output": { <2>
          "input_field": "content",
          "output_field": "content_embedding"
        }
      }
    }
  ]
}
```
<1> The name of the inference endpoint you created by using the
put-inference-api, it's referred to as `inference_id` in that step.
<2> Configuration object that defines the `input_field` for the inference process
and the `output_field` that will contain the inference results.

```console
PUT _ingest/pipeline/hugging_face_embeddings_pipeline
{
  "processors": [
    {
      "inference": {
        "model_id": "hugging_face_embeddings", <1>
        "input_output": { <2>
          "input_field": "content",
          "output_field": "content_embedding"
        }
      }
    }
  ]
}
```
<1> The name of the inference endpoint you created by using the
put-inference-api, it's referred to as `inference_id` in that step.
<2> Configuration object that defines the `input_field` for the inference process
and the `output_field` that will contain the inference results.

```console
PUT _ingest/pipeline/openai_embeddings_pipeline
{
  "processors": [
    {
      "inference": {
        "model_id": "openai_embeddings", <1>
        "input_output": { <2>
          "input_field": "content",
          "output_field": "content_embedding"
        }
      }
    }
  ]
}
```
<1> The name of the inference endpoint you created by using the
put-inference-api, it's referred to as `inference_id` in that step.
<2> Configuration object that defines the `input_field` for the inference process
and the `output_field` that will contain the inference results.

```console
PUT _ingest/pipeline/azure_openai_embeddings_pipeline
{
  "processors": [
    {
      "inference": {
        "model_id": "azure_openai_embeddings", <1>
        "input_output": { <2>
          "input_field": "content",
          "output_field": "content_embedding"
        }
      }
    }
  ]
}
```
<1> The name of the inference endpoint you created by using the
put-inference-api, it's referred to as `inference_id` in that step.
<2> Configuration object that defines the `input_field` for the inference process
and the `output_field` that will contain the inference results.

```console
PUT _ingest/pipeline/azure_ai_studio_embeddings_pipeline
{
  "processors": [
    {
      "inference": {
        "model_id": "azure_ai_studio_embeddings", <1>
        "input_output": { <2>
          "input_field": "content",
          "output_field": "content_embedding"
        }
      }
    }
  ]
}
```
<1> The name of the inference endpoint you created by using the
put-inference-api, it's referred to as `inference_id` in that step.
<2> Configuration object that defines the `input_field` for the inference process
and the `output_field` that will contain the inference results.

```console
PUT _ingest/pipeline/google_vertex_ai_embeddings_pipeline
{
  "processors": [
    {
      "inference": {
        "model_id": "google_vertex_ai_embeddings", <1>
        "input_output": { <2>
          "input_field": "content",
          "output_field": "content_embedding"
        }
      }
    }
  ]
}
```
<1> The name of the inference endpoint you created by using the
put-inference-api, it's referred to as `inference_id` in that step.
<2> Configuration object that defines the `input_field` for the inference process
and the `output_field` that will contain the inference results.

```console
PUT _ingest/pipeline/mistral_embeddings_pipeline
{
  "processors": [
    {
      "inference": {
        "model_id": "mistral_embeddings", <1>
        "input_output": { <2>
          "input_field": "content",
          "output_field": "content_embedding"
        }
      }
    }
  ]
}
```
<1> The name of the inference endpoint you created by using the
put-inference-api, it's referred to as `inference_id` in that step.
<2> Configuration object that defines the `input_field` for the inference process
and the `output_field` that will contain the inference results.

```console
PUT _ingest/pipeline/amazon_bedrock_embeddings_pipeline
{
  "processors": [
    {
      "inference": {
        "model_id": "amazon_bedrock_embeddings", <1>
        "input_output": { <2>
          "input_field": "content",
          "output_field": "content_embedding"
        }
      }
    }
  ]
}
```
<1> The name of the inference endpoint you created by using the
put-inference-api, it's referred to as `inference_id` in that step.
<2> Configuration object that defines the `input_field` for the inference process
and the `output_field` that will contain the inference results.

```console
PUT _ingest/pipeline/alibabacloud_ai_search_embeddings_pipeline
{
  "processors": [
    {
      "inference": {
        "model_id": "alibabacloud_ai_search_embeddings", <1>
        "input_output": { <2>
          "input_field": "content",
          "output_field": "content_embedding"
        }
      }
    }
  ]
}
```
<1> The name of the inference endpoint you created by using the
put-inference-api, it's referred to as `inference_id` in that step.
<2> Configuration object that defines the `input_field` for the inference process
and the `output_field` that will contain the inference results.


#### Load data

In this step, you load the data that you later use in the inference ingest pipeline to create embeddings from it.

Use the `msmarco-passagetest2019-top1000` data set, which is a subset of the MS MARCO Passage Ranking data set.
It consists of 200 queries, each accompanied by a list of relevant text passages.
All unique passages, along with their IDs, have been extracted from that data set and compiled into a
[tsv file](https://github.com/elastic/stack-docs/blob/main/docs/en/stack/ml/nlp/data/msmarco-passagetest2019-unique.tsv).

Download the file and upload it to your cluster using the [Data Visualizer](https://www.elastic.co/guide/en/kibana/8.19/connect-to-elasticsearch.html#upload-data-kibana) in the {ml-app} UI.
After your data is analyzed, click **Override settings**.
Under **Edit field names**, assign `id` to the first column and `content` to the second.
Click **Apply**, then **Import**.
Name the index `test-data`, and click **Import**.
After the upload is complete, you will see an index named `test-data` with 182,469 documents.
