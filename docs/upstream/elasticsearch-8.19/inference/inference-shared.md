<!-- Converted from inference/inference-shared.asciidoc (AsciiDoc). Includes are inlined. -->

tag::api-key-admonition[]
**Important:** You need to provide the API key only once, during the inference model creation.
The get-inference-api does not retrieve your API key.
After creating the inference model, you cannot change the associated API key.
If you want to use a different API key, delete the inference model and recreate it with the same name and the updated API key.
end::api-key-admonition[]

tag::inference-id[]
The unique identifier of the inference endpoint.
end::inference-id[]

tag::request-per-minute-example[]
```text
"rate_limit": {
    "requests_per_minute": <<number_of_requests>>
}
```
end::request-per-minute-example[]

tag::service-settings[]
Settings used to install the inference model.
end::service-settings[]

tag::task-settings[]
Settings to configure the inference task.
These settings are specific to the `<task_type>` you specified.
end::task-settings[]

tag::task-type[]
The type of the inference task that the model will perform.
end::task-type[]

tag::chunking-settings[]
Chunking configuration object.
Refer to infer-chunking-config to learn more about chunking.
end::chunking-settings[]

tag::chunking-settings-max-chunking-size[]
Specifies the maximum size of a chunk in words.
Defaults to `250`.
This value cannot be higher than `300` or lower than `20` (for `sentence` strategy) or `10` (for `word` strategy).
end::chunking-settings-max-chunking-size[]

tag::chunking-settings-overlap[]
Only for `word` chunking strategy.
Specifies the number of overlapping words for chunks.
Defaults to `100`.
This value cannot be higher than the half of `max_chunk_size`.
end::chunking-settings-overlap[]

tag::chunking-settings-sentence-overlap[]
Only for `sentence` chunking strategy.
Specifies the numnber of overlapping sentences for chunks.
It can be either `1` or `0`.
Defaults to `1`.
end::chunking-settings-sentence-overlap[]

tag::chunking-settings-strategy[]
Specifies the chunking strategy.
It could be either `sentence` or `word`.
end::chunking-settings-strategy[]

tag::chat-completion-schema-content-with-examples[]
**Examples**
======
String example
```js
{
    "content": "Some string"
}
```

Object example
```js
{
    "content": [
        {
            "text": "Some text",
            "type": "text"
        }
    ]
}
```
======

String representation:::
(Required, string)
The text content.
Object representation:::
`text`::::
(Required, string)
The text content.
`type`::::
(Required, string)
This must be set to the value `text`.
end::chat-completion-schema-content-with-examples[]

tag::chat-completion-docs[]
For more information on how to use the `chat_completion` task type, please refer to the chat completion documentation.
end::chat-completion-docs[]
