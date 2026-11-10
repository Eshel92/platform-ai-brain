<!-- Converted from management/connectors/action-types/defender.asciidoc (AsciiDoc). Includes are inlined. -->

## Microsoft Defender for Endpoint connector and action

The Microsoft Defender for Endpoint connector enables you to perform actions on Microsoft Defender-enrolled hosts.

### Create connectors in Kibana

You can create connectors in *{stack-manage-app} > {connectors-ui}* or as needed when you're creating a rule.
For example:

(Figure: management/connectors/images/defender-connector.png)

#### Connector configuration

Microsoft Defender for Endpoint connectors have the following configuration properties:

API URL::
The URL of the Microsoft Defender for Endpoint API. If you are using the `xpack.actions.allowedHosts` setting, make sure the hostname is added to the allowed hosts.

Application client ID::
The application (client) identifier for your app in the Azure portal.

Client secret value::
The client secret for your app in the Azure portal.

Name::
The name of the connector.

OAuth scope::
The OAuth scopes or permission sets for the Microsoft Defender for Endpoint API.

OAuth server URL::
The OAuth server URL where authentication is sent and received for the Microsoft Defender for Endpoint API.

Tenant ID::
The tenant identifier for your app in the Azure portal.

### Test connectors

You can test connectors as you're creating or editing the connector in Kibana. For example:

(Figure: management/connectors/images/defender-connector-test.png)

### Configure Microsoft Defender for Endpoint

Before you create the connector, you must create a new application on your Azure domain.
The procedure to create an application is found in the [Microsoft Defender documentation](https://learn.microsoft.com/en-us/defender-endpoint/api/exposed-apis-create-app-webapp).

Make note of the client ID, client secret, and tenant ID, since you must provide this information when you create your connector.
