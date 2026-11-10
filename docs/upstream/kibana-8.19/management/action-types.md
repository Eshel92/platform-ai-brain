<!-- Converted from management/action-types.asciidoc (AsciiDoc). Includes are inlined. -->

## Connectors

Connectors provide a central place to store connection information for services and integrations with Elastic or third party systems.
Actions are instantiations of a connector that are linked to rules and run as background tasks on the Kibana server when rule conditions are met. Kibana provides the following types of connectors:

|===

a| {bedrock}

| Send a request to {bedrock}.

a| Cases

| Add alerts to cases.

a| CrowdStrike

| Send a request to CrowdStrike.

a| D3 Security

| Send a request to D3 Security.

a| Elastic Managed LLM

| Send a request to the Elastic Managed LLM.

a| {gemini}

| Send a request to {gemini}.

a| Email

| Send email from your server.

a| {ibm-r}

| Create an incident in {ibm-r}.

a| Index

| Index data into Elasticsearch.

a| Jira

| Create an incident in Jira.

a| Microsoft Defender for Endpoint

| Send requests to Microsoft Defender-enrolled hosts.

a| Microsoft Teams

| Send a message to a Microsoft Teams channel.

a| Observability AI Assistant

| Add AI-driven insights and custom actions to your workflow.

a| OpenAI

| Send a request to OpenAI.

a| {opsgenie}

| Create or close an alert in {opsgenie}.

a| PagerDuty

| Send an event in PagerDuty.

a| SentinelOne

| Send a request to SentinelOne.

a| ServerLog

| Add a message to a Kibana log.

a| {sn-itsm}

| Create an incident in {sn}.

a| {sn-sir}

| Create a security incident in {sn}.

a| {sn-itom}

| Create an event in {sn}.

a| Slack

| Send a message to a Slack channel or user.

a| {swimlane}

| Create an incident in {swimlane}.

a| {hive}

| Create cases and alerts in {hive}.

a| Tines

| Send events to a Tines Story.

a| Torq

| Trigger a Torq workflow.

a| {webhook}

| Send a request to a web service.

a| {webhook-cm}

| Send a request to a Case Management web service.

a| xMatters

| Send actionable alerts to on-call xMatters resources.

|===

==============================================
Some connector types are paid commercial features, while others are free.
For a comparison of the Elastic subscription levels, go to
{subscriptions}[the subscription page].
==============================================

### Managing connectors

Rules use connectors to route actions to different destinations like log files, ticketing systems, and messaging tools. While each Kibana app can offer their own types of rules, they typically share connectors. *{stack-manage-app} > {connectors-ui}* offers a central place to view and manage all the connectors in the current space.

(Figure: images/connector-listing.png)

### Required permissions

Access to connectors is granted based on your privileges to alerting-enabled
features. For more information, go to alerting-security.

### Connector networking configuration

Use the action configuration settings to customize connector networking configurations, such as proxies, certificates, or TLS settings. You can set configurations that apply to all your connectors or use `xpack.actions.customHostSettings` to set per-host configurations.

### Connector list

In *{stack-manage-app} > {connectors-ui}*, you can find a list of the connectors
in the current space. You can use the search bar to find specific connectors by
name and type. The *Type* dropdown also enables you to filter to a subset of
connector types.

(Figure: images/connector-filter-by-type.png)

You can delete individual connectors using the trash icon. Alternatively, select
multiple connectors and delete them in bulk using the *Delete* button.

(Figure: images/connector-delete.png)

============================================================================
You can delete a connector even if there are still actions referencing it.
When this happens the action will fail to run and errors appear in the Kibana logs.
============================================================================

### Creating a new connector

New connectors can be created with the *Create connector* button, which guides
you to select the type of connector and configure its properties.

(Figure: images/connector-select-type.png)

After you create a connector, it is available for use any time you set up an
action in the current space.

For out-of-the-box and standardized connectors, refer to
preconfigured connectors.

**Tip:** You can also manage connectors as resources with the [Elasticstack provider](https://registry.terraform.io/providers/elastic/elasticstack/latest) for Terraform.
For more details, refer to the [elasticstack_kibana_action_connector](https://registry.terraform.io/providers/elastic/elasticstack/latest/docs/resources/kibana_action_connector) resource.

### Importing and exporting connectors

To import and export connectors, use the
Saved Objects Management UI.

(Figure: images/connectors-import-banner.png)

If a connector is missing sensitive information after the import, a **Fix**
button appears in *{connectors-ui}*.

(Figure: images/connectors-with-missing-secrets.png)

### Monitoring connectors

The Task Manager health API helps you understand the performance of all tasks in your environment.
However, if connectors fail to run, they will report as successful to Task Manager. The failure stats will not
accurately depict the performance of connectors.

For more information on connector successes and failures, refer to the Event log index.

(See `management/connectors/action-types/bedrock.md`)
(See `management/connectors/action-types/cases-action-type.md`)
(See `management/connectors/action-types/crowdstrike.md`)
(See `management/connectors/action-types/d3security.md`)
(See `management/connectors/action-types/elastic-managed-llm.md`)
(See `management/connectors/action-types/email.md`)
(See `management/connectors/action-types/gemini.md`)
(See `management/connectors/action-types/resilient.md`)
(See `management/connectors/action-types/index.md`)
(See `management/connectors/action-types/jira.md`)
(See `management/connectors/action-types/defender.md`)
(See `management/connectors/action-types/teams.md`)
(See `management/connectors/action-types/obs-ai-assistant.md`)
(See `management/connectors/action-types/openai.md`)
(See `management/connectors/action-types/opsgenie.md`)
(See `management/connectors/action-types/pagerduty.md`)
(See `management/connectors/action-types/sentinelone.md`)
(See `management/connectors/action-types/server-log.md`)
(See `management/connectors/action-types/servicenow.md`)
(See `management/connectors/action-types/servicenow-sir.md`)
(See `management/connectors/action-types/servicenow-itom.md`)
(See `management/connectors/action-types/swimlane.md`)
(See `management/connectors/action-types/slack.md`)
(See `management/connectors/action-types/thehive.md`)
(See `management/connectors/action-types/tines.md`)
(See `management/connectors/action-types/torq.md`)
(See `management/connectors/action-types/webhook.md`)
(See `management/connectors/action-types/cases-webhook.md`)
(See `management/connectors/action-types/xmatters.md`)
(See `management/connectors/pre-configured-connectors.md`)
