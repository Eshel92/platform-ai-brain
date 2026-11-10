<!-- Converted from tab-widgets/inference-api/infer-api-mapping-widget.asciidoc (AsciiDoc). Includes are inlined. -->

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
