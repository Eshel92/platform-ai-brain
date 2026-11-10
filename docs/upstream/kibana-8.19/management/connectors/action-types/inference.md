<!-- Converted from management/connectors/action-types/inference.asciidoc (AsciiDoc). Includes are inlined. -->

## AI connector and action

coming::[]

The inference connector uses the Elasticsearch client to send requests to an inference service.
The connector uses the run connector API to send the request.

### Create connectors in Kibana

You can create connectors in *{stack-manage-app} > {connectors-ui}*. For example:

(Figure: management/connectors/images/inference-connector.png)

#### Connector configuration

{infer-cap} connectors have the following configuration properties:

Name::      The name of the connector.
Service::   The supported inference service provider.
Task type:: The inference task type, it depends on the selected service.
Inference ID:: The unique identifier of the inference endpoint.
Provider configuration:: Settings for service configuration.
Provider secrets:: Configuration for authentication.
Task type configuration:: Settings for task type configuration.

### Test connectors

You can test connectors using the run connector API or
while creating or editing the connector in Kibana. For example:

(Figure: management/connectors/images/inference-completion-params.png)

### {infer-cap} connector actions

The inference actions have the following configuration properties. Properties depend on the selected task type.

#### Completion

The following example performs a completion task on the example question.

Input::
The text on which you want to perform the inference task. For example:
```text
{
  input: 'What is Elastic?'
}
```

#### Text embedding

The following example performs a text embedding task.

Input::
The text on which you want to perform the inference task. For example:
```text
{
  input: 'The sky above the port was the color of television tuned to a dead channel.',
  task_settings: {
    input_type: 'ingest'
  }
}
```

Input type::
An optional string that overwrites the connector's default model.

#### Reranking

The following example performs a reranking task on the example input.

Input::
The text on which you want to perform the inference task. Should be a string array. For example:
```text
{
  input: ['luke', 'like', 'leia', 'chewy', 'r2d2', 'star', 'wars'],
  query: 'star wars main character'
}
```

Query::
The search query text.

#### Sparse embedding

The following example performs a sparse embedding task on the example sentence.

Input::
The text on which you want to perform the inference task. For example:
```text
{
  input: 'The sky above the port was the color of television tuned to a dead channel.'
}
```

### Connector networking configuration

Use the Action configuration settings to customize connector networking configurations, such as proxies, certificates, or TLS settings. You can apply these settings to all your connectors or use `xpack.actions.customHostSettings` to set per-host configurations.
