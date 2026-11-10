<!-- Converted from management/connectors/action-types/resilient.asciidoc (AsciiDoc). Includes are inlined. -->

## {ibm-r} connector and action

The {ibm-r} connector uses the [RESILIENT REST v2](https://developer.ibm.com/security/resilient/rest/) to create {ibm-r} incidents.

### Create connectors in Kibana

You can create connectors in *{stack-manage-app} > {connectors-ui}*
or as needed when you're creating a rule. For example:

(Figure: management/connectors/images/resilient-connector.png)

#### Connector configuration

{ibm-r} connectors have the following configuration properties:

API key ID::
The authentication key ID for HTTP Basic authentication.
API key secret::
The authentication key secret for HTTP Basic authentication.
Organization ID::
The {ibm-r} organization ID.
URL::
The {ibm-r} instance URL.

### Test connectors

You can test connectors as you're creating or editing the connector in Kibana.
For example:

(Figure: management/connectors/images/resilient-params-test.png)

{ibm-r} actions have the following configuration properties.

Additional comments::
Extra information for the client, such as how to troubleshoot the issue.
Description::
The details about the incident.
Incident type::
The type of the incident.
Name::
A name for the issue, used for searching the contents of the knowledge base.
Severity::
The severity of the incident.

### Connector networking configuration

Use the action configuration settings to customize connector networking configurations, such as proxies, certificates, or TLS settings.
You can set configurations that apply to all your connectors or use `xpack.actions.customHostSettings` to set per-host configurations.
