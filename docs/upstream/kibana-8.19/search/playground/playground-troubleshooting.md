<!-- Converted from search/playground/playground-troubleshooting.asciidoc (AsciiDoc). Includes are inlined. -->

### Troubleshooting

preview::[]

Dense vectors are not searchable::
Embeddings must be generated using the [inference processor](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/inference-processor.html) with an ML node.

Context length error::
You'll need to adjust the size of the context you're sending to the model.
Refer to playground-context.

LLM credentials not working::
Under *Model settings*, use the wrench button (🔧) to edit your GenAI connector settings.

Poor answer quality::
Check the retrieved documents to see if they are valid.
Adjust your Elasticsearch queries to improve the relevance of the documents retrieved. Refer to playground-query.
You can update the initial instructions to be more detailed. This is called 'prompt engineering'. Refer to this [OpenAI guide](https://platform.openai.com/docs/guides/prompt-engineering) for more information.
You might need to click *⟳ Clear chat* to clear chat history and start a new conversation.
If you mix topics, the model will find it harder to generate relevant responses.
