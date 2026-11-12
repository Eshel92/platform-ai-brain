<!-- Part 3 of 5 of search/search-your-data/semantic-search-inference.md (split because the page is big). -->

#### Ingest the data through the inference ingest pipeline

Create embeddings from the text by reindexing the data through the inference pipeline that uses your chosen model.
This step uses the [reindex API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-reindex.html) to simulate data ingestion through a pipeline.

```console
POST _reindex?wait_for_completion=false
{
  "source": {
    "index": "test-data",
    "size": 50 <1>
  },
  "dest": {
    "index": "cohere-embeddings",
    "pipeline": "cohere_embeddings_pipeline"
  }
}
```
<1> The default batch size for reindexing is 1000. Reducing `size` to a smaller
number makes the update of the reindexing process quicker which enables you to
follow the progress closely and detect errors early.

**Note:** The
[rate limit of your Cohere account](https://dashboard.cohere.com/billing)
may affect the throughput of the reindexing process.

```console
POST _reindex?wait_for_completion=false
{
  "source": {
    "index": "test-data",
    "size": 50 <1>
  },
  "dest": {
    "index": "elser-embeddings",
    "pipeline": "elser_embeddings_pipeline"
  }
}
```
<1> The default batch size for reindexing is 1000. Reducing `size` to a smaller
number makes the update of the reindexing process quicker which enables you to
follow the progress closely and detect errors early.

```console
POST _reindex?wait_for_completion=false
{
  "source": {
    "index": "test-data",
    "size": 50 <1>
  },
  "dest": {
    "index": "hugging-face-embeddings",
    "pipeline": "hugging_face_embeddings_pipeline"
  }
}
```
<1> The default batch size for reindexing is 1000. Reducing `size` to a smaller
number makes the update of the reindexing process quicker which enables you to
follow the progress closely and detect errors early.

```console
POST _reindex?wait_for_completion=false
{
  "source": {
    "index": "test-data",
    "size": 50 <1>
  },
  "dest": {
    "index": "openai-embeddings",
    "pipeline": "openai_embeddings_pipeline"
  }
}
```
<1> The default batch size for reindexing is 1000. Reducing `size` to a smaller
number makes the update of the reindexing process quicker which enables you to
follow the progress closely and detect errors early.

**Note:** The
[rate limit of your OpenAI account](https://platform.openai.com/account/limits)
may affect the throughput of the reindexing process. If this happens, change
`size` to `3` or a similar value in magnitude.

```console
POST _reindex?wait_for_completion=false
{
  "source": {
    "index": "test-data",
    "size": 50 <1>
  },
  "dest": {
    "index": "azure-openai-embeddings",
    "pipeline": "azure_openai_embeddings_pipeline"
  }
}
```
<1> The default batch size for reindexing is 1000. Reducing `size` to a smaller
number makes the update of the reindexing process quicker which enables you to
follow the progress closely and detect errors early.

**Note:** The
[rate limit of your Azure OpenAI account](https://learn.microsoft.com/en-us/azure/ai-services/openai/quotas-limits#quotas-and-limits-reference)
may affect the throughput of the reindexing process. If this happens, change
`size` to `3` or a similar value in magnitude.

```console
POST _reindex?wait_for_completion=false
{
  "source": {
    "index": "test-data",
    "size": 50 <1>
  },
  "dest": {
    "index": "azure-ai-studio-embeddings",
    "pipeline": "azure_ai_studio_embeddings_pipeline"
  }
}
```
<1> The default batch size for reindexing is 1000. Reducing `size` to a smaller
number makes the update of the reindexing process quicker which enables you to
follow the progress closely and detect errors early.

**Note:** Your Azure AI Studio model deployment may have rate limits in place that
might affect the throughput of the reindexing process. If this happens, change
`size` to `3` or a similar value in magnitude.

```console
POST _reindex?wait_for_completion=false
{
  "source": {
    "index": "test-data",
    "size": 50 <1>
  },
  "dest": {
    "index": "google-vertex-ai-embeddings",
    "pipeline": "google_vertex_ai_embeddings_pipeline"
  }
}
```
<1> The default batch size for reindexing is 1000. Reducing `size` will make updates to the reindexing process faster. This enables you to
follow the progress closely and detect errors early.

```console
POST _reindex?wait_for_completion=false
{
  "source": {
    "index": "test-data",
    "size": 50 <1>
  },
  "dest": {
    "index": "mistral-embeddings",
    "pipeline": "mistral_embeddings_pipeline"
  }
}
```
<1> The default batch size for reindexing is 1000. Reducing `size` to a smaller
number makes the update of the reindexing process quicker which enables you to
follow the progress closely and detect errors early.

```console
POST _reindex?wait_for_completion=false
{
  "source": {
    "index": "test-data",
    "size": 50 <1>
  },
  "dest": {
    "index": "amazon-bedrock-embeddings",
    "pipeline": "amazon_bedrock_embeddings_pipeline"
  }
}
```
<1> The default batch size for reindexing is 1000. Reducing `size` to a smaller
number makes the update of the reindexing process quicker which enables you to
follow the progress closely and detect errors early.

```console
POST _reindex?wait_for_completion=false
{
  "source": {
    "index": "test-data",
    "size": 50 <1>
  },
  "dest": {
    "index": "alibabacloud-ai-search-embeddings",
    "pipeline": "alibabacloud_ai_search_embeddings_pipeline"
  }
}
```
<1> The default batch size for reindexing is 1000. Reducing `size` to a smaller
number makes the update of the reindexing process quicker which enables you to
follow the progress closely and detect errors early.

The call returns a task ID to monitor the progress:

```console
GET _tasks/<task_id>
```

Reindexing large datasets can take a long time.
You can test this workflow using only a subset of the dataset.
Do this by cancelling the reindexing process, and only generating embeddings for the subset that was reindexed.
The following API request will cancel the reindexing task:

```console
POST _tasks/<task_id>/_cancel
```
