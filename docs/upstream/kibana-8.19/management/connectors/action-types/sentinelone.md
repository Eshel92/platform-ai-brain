<!-- Converted from management/connectors/action-types/sentinelone.asciidoc (AsciiDoc). Includes are inlined. -->

## SentinelOne connector

The SentinelOne connector communicates with SentinelOne Management Console via REST API.

To use this connector, you must have authority to run {endpoint-sec} connectors, which is an *{connectors-feature}* sub-feature privilege. Refer to kibana-privileges.

### Create connectors in Kibana

You can create connectors in *{stack-manage-app} > {connectors-ui}*. For example:

(Figure: management/connectors/images/sentinelone-connector.png)

#### Connector configuration

SentinelOne connectors have the following configuration properties:

API token::  A SentinelOne API token created by the user.
URL:: The SentinelOne tenant URL. If you are using the `xpack.actions.allowedHosts` setting, make sure the hostname is added to the allowed hosts.

### Test connectors

You can test connectors as you're creating or editing the connector in Kibana.
For example:

(Figure: management/connectors/images/sentinelone-connector-test.png)
