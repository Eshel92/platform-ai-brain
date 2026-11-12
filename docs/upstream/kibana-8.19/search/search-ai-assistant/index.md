<!-- Converted from search/search-ai-assistant/index.asciidoc (AsciiDoc). Includes are inlined. -->

## AI Assistant

**Tip:**
Don't confuse AI Assistant with Playground! Use Playground to chat with your data, test and tweak different Elasticsearch queries in the Playground UI, and download the code to integrate into your own RAG application.

Use AI Assistant to get help with Elasticsearch and Kibana tasks directly in the UI.

**Observability use cases**
****
Refer to the {observability-guide}/obs-ai-assistant.html[Observability documentation] for more information on how to use AI Assistant in Observability contexts.
****

*AI Assistant for Observability and Search* uses generative AI to help you with a variety of tasks related to Elasticsearch and Kibana, including:

1. *Constructing Queries*: Assists you in building queries to search and analyze your data.
2. *Indexing Data*: Guides you on how to index data into Elasticsearch.
3. *Searching Data*: Helps you search for specific data within your Elasticsearch indices.
4. *Using Elasticsearch APIs*: Calls Elasticsearch APIs on your behalf if you need specific operations performed.
5. *Generating Sample Data*: Helps you create sample data for testing and development purposes.
6. *Visualizing and Analyzing Data*: Assists you in creating visualizations and analyzing your data using Kibana.
7. *Explaining ES|QL*: Explains how ES|QL works and help you convert queries from other languages to [ES|QL.](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/esql.html)

### Requirements

To use AI Assistant in *Search* contexts, you must have the following:

* Elastic Stack version 8.16.0, or an Elasticsearch Serverless project.
* A generative AI connector to connect to a LLM provider, or a local model.
** You need an account with a third-party generative AI provider, which AI Assistant uses to generate responses, or else you need to host your own local model.
** To set up AI Assistant, you need the `Actions and Connectors : All` privilege.
* To use AI Assistant, you need at least the `Elastic AI Assistant : All` and `Actions and Connectors : Read` privilege.
* AI Assistant requires {ml-docs}/ml-nlp-elser.html[ELSER], Elastic's proprietary semantic search model.

### Your data and AI Assistant

Elastic does not use customer data for model training. This includes anything you send the model, such as alert or event data, detection rule configurations, queries, and prompts. However, any data you provide to AI Assistant will be processed by the third-party provider you chose when setting up the generative AI connector as part of the assistant setup.

Elastic does not control third-party tools, and assumes no responsibility or liability for their content, operation, or use, nor for any loss or damage that may arise from your using such tools. Please exercise caution when using AI tools with personal, sensitive, or confidential information. Any data you submit may be used by the provider for AI training or other purposes. There is no guarantee that the provider will keep any information you provide secure or confidential. You should familiarize yourself with the privacy practices and terms of use of any generative AI tools prior to use.

### Using AI Assistant

To open AI Assistant, select the **AI Assistant** button in the top toolbar in the UI.
You can also use the global search field in the UI to find AI Assistant.

(Figure: images/ai-assistant-button.png)

This opens the AI Assistant chat interface flyout.

(Figure: images/ai-assistant-welcome-chat.png)

You can get started by selecting *✨ Suggest* to get some example prompts, or by typing into the chat field.

### Add data to the AI Assistant knowledge base

**Note:**
This functionality is not available on Elastic Cloud Serverless projects.

You can improve the relevance of AI Assistant’s responses by indexing your own data into AI Assistant's knowledge base.
AI Assistant uses {ml-docs}/ml-nlp-elser.html[ELSER], Elastic's proprietary semantic search model, to power its search capabilities.

#### Use the UI

To add external data to the knowledge base in UI:

. In the AI Assistant UI, select the **Settings** icon: `⋮`.
. Under *Actions*, click **Manage knowledge base**.
. Click the **New entry** button, and choose either:
** **Single entry**: Write content for a single entry in the UI.
** **Bulk import**: Upload a newline delimited JSON (`ndjson`) file containing a list of entries to add to the knowledge base.
Each object should conform to the following format:
```json
{
  "id": "a_unique_human_readable_id",
  "text": "Contents of item",
}
```

#### Use Search connectors

**Note:**
This functionality is not available on Elastic Cloud Serverless projects.

You can ingest external data (GitHub issues, Markdown files, Jira tickets, text files, etc.) into Elasticsearch using [Search Connectors](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/es-connectors.html). Connectors sync third party data sources to Elasticsearch. 

Supported service types include [GitHub](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/es-connectors-github.html), [Slack](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/es-connectors-slack.html), [Jira](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/es-connectors-jira.html), and more. These can be Elastic managed or self-managed on your own infrastructure.

To create a connector and make its content available to the AI Assistant knowledge base, follow these steps:

. *In Kibana UI, go to _Search -> Content -> Connectors_ and follow the instructions to create a new connector.*
For example, if you create a [GitHub connector](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/es-connectors-github.html) you must set a `name`, attach it to a new or existing `index`, add your `personal access token` and include the `list of repositories` to synchronize.
**Tip:** Learn more about configuring and [using connectors](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/es-connectors-usage.html) in the Elasticsearch documentation.
. *Create a pipeline and process the data with ELSER.*
To process connector data using {ml-docs}/ml-nlp-elser.html[ELSER], you must create an *ML Inference Pipeline*:
.. Open the previously created connector and select the *Pipelines* tab.
.. Select *Copy and customize* button at the `Unlock your custom pipelines` box.
.. Select *Add Inference Pipeline* button at the `Machine Learning Inference Pipelines` box.
.. Select *ELSER (Elastic Learned Sparse EncodeR)* ML model to add the necessary embeddings to the data.
.. Select the fields that need to be evaluated as part of the inference pipeline.
.. Test and save the inference pipeline and the overall pipeline.
. *Sync data.*
Once the pipeline is set up, perform a *Full Content Sync* of the connector. The inference pipeline will process the data as follows:
* As data comes in, the ELSER model processes the data, creating sparse embeddings for each document.
* If you inspect the ingested documents, you can see how the weights and tokens are added to the `predicted_value` field.
. *Confirm AI Assistant can access the index.*
Ask the AI Assistant a specific question to confirm that the data is available for the AI Assistant knowledge base.
