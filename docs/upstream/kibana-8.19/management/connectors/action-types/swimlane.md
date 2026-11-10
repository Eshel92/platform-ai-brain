<!-- Converted from management/connectors/action-types/swimlane.asciidoc (AsciiDoc). Includes are inlined. -->

## Swimlane connector and action

The Swimlane connector uses the [Swimlane REST API](https://swimlane.com/knowledge-center/docs/developer-guide/rest-api/) to create Swimlane records.

### Create connectors in Kibana

You can create connectors in *{stack-manage-app} > {connectors-ui}*
or as needed when you're creating a rule. For example:

(Figure: management/connectors/images/swimlane-connector.png)

#### Connector configuration

Swimlane connectors have the following configuration properties:

Name:: The name of the connector.
URL:: Swimlane instance URL.
Application ID:: Swimlane application ID.
API token::  Swimlane API authentication token for HTTP basic authentication.

### Test connectors

You can test connectors as you're creating or editing the connector in Kibana. For example:

(Figure: management/connectors/images/swimlane-params-test.png)

Swimlane actions have the following configuration properties.

Comments:: Additional information for the client, such as how to troubleshoot the issue.
Severity:: The severity of the incident.

**Note:** Alert ID and Rule Name are filled automatically. Specifically, Alert ID is set to `{{alert.id}}` and Rule Name to `{{rule.name}}`.
