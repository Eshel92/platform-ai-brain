<!-- Converted from search/playground/index.asciidoc (AsciiDoc). Includes are inlined. -->

## Playground

preview::[]

Use Playground  to combine your Elasticsearch data with the power of large language models (LLMs) for retrieval augmented generation (RAG).
The chat interface translates your natural language questions into Elasticsearch queries, retrieves the most relevant results from your Elasticsearch documents, and passes those documents to the LLM to generate tailored responses.

Once you start chatting, use the UI to view and modify the Elasticsearch queries that search your data.
You can also view the underlying Python code that powers the chat interface, and download this code to integrate into your own application.

Learn how to get started on this page.
Refer to the following for more advanced topics:

* playground-context
* playground-query
* playground-troubleshooting

.🍿 Getting started videos
***********************
Watch these video tutorials to help you get started:

* [Getting Started](https://www.youtube.com/watch?v=zTHgJ3rhe10)
* [Using Playground with local LLMs](https://www.youtube.com/watch?v=ZtxoASFvkno)
***********************

### How Playground  works

Here's a simpified overview of how Playground  works:

* User *creates a connection* to LLM provider
* User *selects a model* to use for generating responses
* User *define the model's behavior and tone* with initial instructions
** *Example*: "_You are a friendly assistant for question-answering tasks. Keep responses as clear and concise as possible._"
* User *selects Elasticsearch indices* to search
* User *enters a question* in the chat interface
* Playground  *autogenerates an Elasticsearch query* to retrieve relevant documents
** User can *view and modify underlying Elasticsearch query* in the UI
* Playground  *auto-selects relevant fields* from retrieved documents to pass to the LLM
** User can *edit fields targeted*
* Playground  passes *filtered documents* to the LLM
** The LLM generates a response based on the original query, initial instructions, chat history, and Elasticsearch context
* User can *view the Python code* that powers the chat interface
** User can also *Download the code* to integrate into application

### Availability and prerequisites

For Elastic Cloud and self-managed deployments Playground  is available in the *Search* space in Kibana, under *Content* > *Playground *.

For Elastic Serverless, Playground  is available in your Elasticsearch project UI.

To use Playground , you'll need the following:

1. An Elastic *v8.14.0+* deployment or Elasticsearch *Serverless* project. (Start a [free trial](https://cloud.elastic.co/registration)).
2. At least one *Elasticsearch index* with documents to search.
** See ingest data if you'd like to ingest sample data.
3. An account with a *supported LLM provider*. Playground  supports the following:
|===
| Provider | Models | Notes

| *Amazon Bedrock*
a|
* Anthropic: Claude 3.5 Sonnet
* Anthropic: Claude 3 Haiku
a|

| *OpenAI*
a|
* GPT-3 turbo
* GPT-4 turbo
* GPT-4 omni
a|

| *Azure OpenAI*
a|
* GPT-3 turbo
* GPT-4 turbo
a|
Buffers responses in large chunks

| *Google*
a|
* Google Gemini 1.5 Pro
* Google Gemini 1.5 Flash
a|

|===

**Tip:**
You can also use locally hosted LLMs that are compatible with the OpenAI SDK.
Once you've set up your LLM, you can connect to it using the OpenAI connector.
Refer to the following for examples:

* {security-guide}/connect-to-byo-llm.html[Using LM Studio]
* [LocalAI with `docker-compose`](https://www.elastic.co/search-labs/blog/localai-for-text-embeddings)

### Getting started

(Figure: get-started.png)

#### Connect to LLM provider

To get started with Playground , you need to create a connector for your LLM provider.
You can also connect to locally hosted LLMs which are compatible with the OpenAI API, by using the OpenAI connector.

To connect to an LLM provider, follow these steps on the Playground  landing page:

. Under *Connect to an LLM*, click *Create connector*.
. Select your *LLM provider*.
. *Name* your connector.
. Select a *URL endpoint* (or use the default).
. Enter *access credentials* for your LLM provider. (If you're running a locally hosted LLM using the OpenAI connector, you must input a value in the API key form, but the specific value doesn't matter.)

**Tip:**
If you need to update a connector, or add a new one, click the 🔧 *Manage* button beside *Model settings*.

#### Ingest data (optional)

_You can skip this step if you already have data in one or more Elasticsearch indices._

There are many options for ingesting data into Elasticsearch, including:

* The {enterprise-search-ref}/crawler.html[Elastic crawler] for web content (*NOTE*: Not yet available in _Serverless_)
* [Elastic connectors](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/es-connectors.html) for data synced from third-party sources
* The Elasticsearch [Bulk API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docs-bulk.html) for JSON documents
.*Expand* for example
==============
To add a few documents to an index called `books` run the following in Dev Tools Console:

```console
POST /_bulk
{ "index" : { "_index" : "books" } }
{"name": "Snow Crash", "author": "Neal Stephenson", "release_date": "1992-06-01", "page_count": 470}
{ "index" : { "_index" : "books" } }
{"name": "Revelation Space", "author": "Alastair Reynolds", "release_date": "2000-03-15", "page_count": 585}
{ "index" : { "_index" : "books" } }
{"name": "1984", "author": "George Orwell", "release_date": "1985-06-01", "page_count": 328}
{ "index" : { "_index" : "books" } }
{"name": "Fahrenheit 451", "author": "Ray Bradbury", "release_date": "1953-10-15", "page_count": 227}
{ "index" : { "_index" : "books" } }
{"name": "Brave New World", "author": "Aldous Huxley", "release_date": "1932-06-01", "page_count": 268}
{ "index" : { "_index" : "books" } }
{"name": "The Handmaids Tale", "author": "Margaret Atwood", "release_date": "1985-06-01", "page_count": 311}
```
==============

We've also provided some Jupyter notebooks to easily ingest sample data into Elasticsearch. 
Find these in the [elasticsearch-labs](https://github.com/elastic/elasticsearch-labs/blob/main/notebooks/ingestion-and-chunking) repository.
These notebooks use the official Elasticsearch Python client.

#### Select Elasticsearch indices

Once you've connected to your LLM provider, it's time to choose the data you want to search.

. Click *Add data sources*.
. Select one or more Elasticsearch indices.
. Click *Save and continue* to launch the chat interface.

**Tip:**
You can always add or remove indices later by selecting the *Data* button from the main Playground  UI.

(Figure: images/data-button.png)

#### Chat and query modes

Since 8.15.0 (and earlier for Elasticsearch Serverless), the main Playground  UI has two modes:

* *Chat mode*: The default mode, where you can chat with your data via the LLM.
* *Query mode*: View and modify the Elasticsearch query generated by the chat interface.

The *chat mode* is selected when you first set up your Playground  instance.

(Figure: images/chat-interface.png)

To switch to *query mode*, select *Query* from the main UI.

(Figure: images/query-interface.png)

**Tip:**
Learn more about the underlying Elasticsearch queries used to search your data in playground-query

#### Set up the chat interface

You can start chatting with your data immediately, but you might want to tweak some defaults first.

You can adjust the following under *Model settings*:

* *Model*. The model used for generating responses.
* *Instructions*. Also known as the _system prompt_, these initial instructions and guidelines define the behavior of the model throughout the conversation. Be *clear and specific* for best results.
* *Include citations*. A toggle to include citations from the relevant Elasticsearch documents in responses.

Playground  also uses another LLM under the hood, to encode all previous questions and responses, and make them available to the main model.
This ensures the model has "conversational memory".

Under *Indices*, you can edit which Elasticsearch indices will be searched.
This will affect the underlying Elasticsearch query.

**Tip:**
Click *✨ Regenerate* to resend the last query to the model for a fresh response.

Click *⟳ Clear chat* to clear chat history and start a new conversation.

#### View and download Python code

Use the *View code* button to see the Python code that powers the chat interface.
You can integrate it into your own application, modifying as needed.
We currently support two implementation options:

* Elasticsearch Python Client + LLM provider
* LangChain + LLM provider

(Figure: images/view-code-button.png)

#### Next steps

Once you've got Playground  up and running, and you've tested out the chat interface, you might want to explore some more advanced topics:

* playground-context
* playground-query
* playground-troubleshooting

(See `search/playground/playground-context.md`)
(See `search/playground/playground-query.md`)
(See `search/playground/playground-troubleshooting.md`)
