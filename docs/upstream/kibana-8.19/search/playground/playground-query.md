<!-- Converted from search/playground/playground-query.asciidoc (AsciiDoc). Includes are inlined. -->

### View and modify queries

preview::[]

Once you've set up your chat interface, you can start chatting with the model.
Playground will automatically generate Elasticsearch queries based on your questions, and retrieve the most relevant documents from your Elasticsearch indices.
The Playground UI enables you to view and modify these queries.

* Click *View query* to open the visual query editor.
* Modify the query by selecting fields to query per index.

**Tip:**
The `{query}` variable represents the user's question, rewritten as an Elasticsearch query.

The following screenshot shows the query editor in the Playground UI.
In this simple example, the `books` index has two fields: `author` and `name`.
Selecting a field adds it to the `fields` array in the query.

(Figure: images/query-interface.png)

Certain fields in your documents may be hidden.
Learn more about hidden fields.

#### Improving relevance

The fields you select in the query editor determine the relevance of the retrieved documents.

Remember that the next step in the workflow is to send the retrieved documents to the LLM to answer the question.
Context length is an important factor in ensuring the model has enough information to generate a relevant answer.
Refer to Optimize context for more information.

Troubleshooting provides tips on how to diagnose and fix relevance issues.

**Note:**
Playground uses the [`retriever`](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/retriever.html) syntax for Elasticsearch queries.
Retrievers make it easier to compose and test different retrieval strategies in your search pipelines.
Refer to [documentation](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/retrievers-overview.html) for a high level overview of retrievers.

#### Hidden fields

The query editor shows fields which make sense for the user to search on, but not all fields in your documents are visible from the editor.

Available field types:

- Semantic fields like `sparse_vector` or `dense_vector` fields where the embeddings have been created from a inference processor
- `text` fields

Hidden Field Types:

- non `text` fields like `keyword` fields
- fields that are not indexed
- semantic fields where the embeddings have not been created from a inference processor
- nested fields
