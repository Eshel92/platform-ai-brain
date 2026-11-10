<!-- Converted from management/connectors/action-types/obs-ai-assistant.asciidoc (AsciiDoc). Includes are inlined. -->

## Observability AI Assistant connector and action

preview::[]

The Observability AI Assistant connector adds AI-driven insights and custom actions to your workflow.

To learn how to interact with the assistant through this connector, refer to the {observability-guide}/obs-ai-assistant.html[Observability AI Assistant] documentation.

### Create connectors in Kibana

To use this connector, you must have been granted access to use the Observability AI Assistant feature.
You cannot manage this connector in *{stack-manage-app} > {connectors-ui}* or by using APIs.
You also cannot create an Observability AI Assistant preconfigured connector.
It is available only when you're creating a rule in Kibana.
For example:

(Figure: management/connectors/images/obs-ai-assistant-action.png)

**Note:** You can have only one Observability AI Assistant action in each rule.

#### Connector configuration

Observability AI Assistant connectors have the following configuration properties:

Connector::
The name of the connector to use to send requests to your AI provider.
For more information, refer to openai-action-type or bedrock-action-type.

Message::
A message containing the prompt to send to the Observability AI Assistant.
The message can specify a set of tasks for the assistant to perform, such as creating a graph or report,
and it can call an available connector to send messages to an external system, such as Slack.

**Note:** Currently you can only send messages to a Slack webhook.
Support for additional connectors will be added in the future.

For example, you can create a rule that sends the following prompt to the AI Assistant when an error count threshold is breached:

```text
High error count alert has triggered. Execute the following steps:
  - create a graph of the error count for the service impacted by the alert
  for the last 24h
  - to help troubleshoot, recall past occurrences of this alert, plus any
  other active alerts. Generate a report with all the found information
  and send it to the Slack connector as a single message. Also include
  the link to this conversation in the report.
```

### Test connectors

You cannot test or edit these connectors in Kibana or by using APIs.
