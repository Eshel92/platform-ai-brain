<!-- Converted from tab-widgets/inference-api/infer-api-ingest-pipeline.asciidoc (AsciiDoc). Includes are inlined. -->

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
