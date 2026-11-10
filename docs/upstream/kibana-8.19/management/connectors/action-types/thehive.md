<!-- Converted from management/connectors/action-types/thehive.asciidoc (AsciiDoc). Includes are inlined. -->

## {hive} connector and action

{hive} connector uses the [{hive} (v1) REST API](https://docs.strangebee.com/thehive/api-docs/) to create cases and alerts. added:[8.16.0]

**Note:**
If you use this connector with cases, the status values differ in Kibana and {hive}.
The status values are not synchronized when you update a case.

### Create connectors in Kibana

You can create connectors in *{stack-manage-app} > {connectors-ui}*
or as needed when you're creating a rule. For example:

(Figure: management/connectors/images/thehive-connector.png)

#### Connector configuration

{hive} connectors have the following configuration properties:

Name::         The name of the connector.
Organisation:: The organisation in {hive} that will contain the cases or alerts.
URL::          The instance URL in {hive}.
API key::      The API key for authentication in {hive}.

### Test connectors

You can test connectors for creating a case or an alert with the run connector API or
as you're creating or editing the connector in Kibana. For example:

(Figure: management/connectors/images/thehive-params-case-test.png)

(Figure: management/connectors/images/thehive-params-alert-test.png)

{hive} actions have the following configuration properties.

Event action:: The action that will be performed in {hive}: create a case or an alert.
Title:: The title of the incident.
Description:: The details about the incident.
Severity:: The severity of the incident: `LOW`, `MEDIUM`, `HIGH` or `CRITICAL`.
TLP:: The traffic light protocol designation for the incident: `CLEAR`, `GREEN`, `AMBER`, `AMBER+STRICT` or `RED`.
Tags:: The keywords or tags for the incident.
Additional comments:: Additional information about the incident.
Type:: The type of alert.
Source:: The source of the alert.
Source reference:: A source reference for the alert.

### Connector networking configuration

Use the Action configuration settings to customize connector networking configurations, such as proxies, certificates, or TLS settings. You can set configurations that apply to all your connectors or use `xpack.actions.customHostSettings` to set per-host configurations.

### Configure {hive}

To generate an API key in {hive}:

1. Log in to your {hive} instance.
2. Open profile tab and select the settings.
3. Go to *API Key*.
4. Click *Create* if no API key has been created previously; otherwise, you can view the API key by clicking on *Reveal*.
5. Copy the *API key* value to configure the connector in Kibana.
