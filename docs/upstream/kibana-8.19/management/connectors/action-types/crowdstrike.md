<!-- Converted from management/connectors/action-types/crowdstrike.asciidoc (AsciiDoc). Includes are inlined. -->

## CrowdStrike connector

The CrowdStrike connector communicates with CrowdStrike Management Console via REST API.

To use this connector, you must have authority to run {endpoint-sec} connectors, which is an *{connectors-feature}* sub-feature privilege. Refer to kibana-privileges.

### Create connectors in Kibana

You can create connectors in *{stack-manage-app} > {connectors-ui}*. For example:

(Figure: management/connectors/images/crowdstrike-connector.png)

#### Connector configuration

CrowdStrike connectors have the following configuration properties:

CrowdStrike API URL:: The CrowdStrike tenant URL. If you are using the `xpack.actions.allowedHosts` setting, make sure the hostname is added to the allowed hosts.
CrowdStrike client ID::  The CrowdStrike API client identifier.
Client secret::  The CrowdStrike API client secret to authenticate the client ID.

### Test connectors

You can test connectors as you're creating or editing the connector in Kibana. For example:

(Figure: management/connectors/images/crowdstrike-connector-test.png)

The CrowdStrike action has the following configuration properties:

Agent IDs:: Get details about one or more CrowdStrike agent IDs.
