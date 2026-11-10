<!-- Converted from user/alerting/alerting-setup.asciidoc (AsciiDoc). Includes are inlined. -->

## Alerting set up

Kibana {alert-features} are automatically enabled, but might require some additional 
configuration.

### Prerequisites

If you are using an *on-premises* Elastic Stack deployment:

* In the `kibana.yml` configuration file, add the 
`xpack.encryptedSavedObjects.encryptionKey` 
setting.
* For emails to have a footer with a link back to Kibana, set the 
`server.publicBaseUrl` configuration setting.

If you are using an *on-premises* Elastic Stack deployment with 
*security*:

* If you are unable to access Kibana {alert-features}, ensure that you have not 
[explicitly disabled API keys](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-settings.html#api-key-service-settings).

The alerting framework uses queries that require the 
`search.allow_expensive_queries` setting to be `true`. See the scripts 
[documentation](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/query-dsl-script-query.html#_allow_expensive_queries_4). 

### Production considerations and scaling guidance

When relying on alerting and actions as mission critical services, make sure you 
follow the 
alerting production considerations.

For more information on the scalability of {alert-features}, go to
alerting-scaling-guidance.

### Security

To use {alert-features} in a Kibana app, you must have the appropriate feature privileges:

|=== 

| Action | Kibana privileges
| Give full access to manage alerts, connectors, and rules in *{stack-manage-app}*
a|
* `All` for the *Management > {stack-rules-feature}* feature.
* `All` for the *Management > Rules Settings* feature.
* `All` for the *Management > {connectors-feature}* feature.

**Note:**
The *{connectors-feature}* feature privilege is required to manage connectors.
To add rule actions and test connectors, you require only `Read` privileges.
By default, `All` privileges include authority to run {endpoint-sec} connectors (such as SentinelOne and CrowdStrike) unless you customize the sub-feature privileges.

Likewise, you can customize the *Rules Settings* sub-feature privileges related to flapping detection settings.

To create a rule that uses the Cases connector, you must also have `All` privileges for the *Cases* feature.

The rule type also affects the privileges that are required.
For example, to create or edit machine learning rules, you must have `all` privileges for the *Analytics > {ml-app}* feature.
For {stack-monitor-app} rules, you must have the `monitoring_user` role.
For Observability rules, you must have `all` privileges for the appropriate Observability features.
For Security rules, refer to {security-guide}/detections-permissions-section.html[Detections prerequisites and requirements].

| Give view-only access to alerts, connectors, and rules in  *{stack-manage-app}*
a|
* `Read` for the *Management > {stack-rules-feature}* feature.
* `Read` for the *Management > Rules Settings* feature.
* `Read` for the *Management > {connectors-feature}* feature.

**Note:**
The rule type also affects the privileges that are required.
For example, to view machine learning rules, you must have `read` privileges for the *Analytics > {ml-app}* feature.
For {stack-monitor-app} rules, you must have the `monitoring_user` role.
For Observability rules, you must have `read` privileges for the appropriate Observability features.
For Security rules, refer to {security-guide}/detections-permissions-section.html[Detections prerequisites and requirements].

| Give view-only access to alerts in *Discover* or *Dashboards*
a|
* `Read` index privileges for the `.alerts-*` system indices.

| Revoke all access to alerts, connectors, and rules in *{stack-manage-app}*, *Discover*, or *Dashboards*
a|
* `None` for the *Management > {stack-rules-feature}* feature.
* `None` for the *Management > Rules Settings* feature.
* `None` for the *Management > {connectors-feature}* feature.
* No index privileges for the `.alerts-*` system indices.
|===

For more information on configuring roles that provide access to features, go to kibana-feature-privileges.

#### API keys

Rules are authorized using an API key.
Its credentials are used to run all background tasks associated with the rule, including condition checks like Elasticsearch queries and triggered actions.

When you create a rule in Kibana, an API key is created that captures a snapshot of your privileges.
Likewise when you update a rule, the API key is updated with a snapshot of your privileges at the time of the edit. 

When you disable a rule, it retains the associated API key which is reused when the rule is enabled.
If the API key is missing when you enable the rule, a new key is generated that has your current security privileges.
When you import a rule, you must enable it before you can use it and a new API key is generated at that time.

You can generate a new API key at any time in **{stack-manage-app} > {rules-ui}** or in the rule details page by selecting **Update API key** in the actions menu.

If you manage your rules by using Kibana APIs, they support support both key- and token-based authentication as described in api-authentication.
To use key-based authentication, create API keys and use them in the header of your API calls as described in api-keys.
To use token-based authentication, provide a username and password; an API key that matches the current privileges of the user is created automatically.
In both cases, the API key is subsequently associated with the rule and used when it runs.

==============================================
If a rule requires certain privileges, such as index privileges, to run and a user without those privileges updates the rule, the rule will no longer function.
Conversely, if a user with greater or administrator privileges modifies the rule, it will begin running with increased privileges.
The same behavior occurs when you change the API key in the header of your API calls.
==============================================

#### Restrict actions

For security reasons you may wish to limit the extent to which Kibana can connect to external services.
You can use action-settings to disable certain action-types and allowlist the hostnames that Kibana can connect with.

### Space isolation

Rules and connectors are isolated to the Kibana space in which they were created. 
A rule or connector created in one space will not be visible in another. 

### Cross-cluster search

If you want to use alerting rules with cross-cluster search, you must configure privileges for
CCS and Kibana. Refer to [Remote clusters](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/remote-clusters.html).
