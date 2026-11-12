<!-- Part 16 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.14.3

The 8.14.3 release includes the following bug fixes and known issues.

### Known issues

**Creating or editing APM, Observability and {stack-monitor-app} rules fails**
*Details* +
When you attempt to create or edit some rule types in **{stack-manage-app}** > **{rules-ui}**, the request will fail with errors similar to `Cannot read properties of undefined (reading 'eui')` or `e.theme.eui is undefined`.
Refer to [#186969](https://github.com/elastic/kibana/issues/186969)

*Impact* +
This known issue impacts only Observability, {stack-monitor-app}, and APM and {user-experience} rules.

*Workaround* +
To work around this issue for Observability and APM and {user-experience} rules, create them from the Observability *Alerts* page.
Refer to apm-alerts and {observability-guide}/create-alerts-rules.html[Create and manage Observability rules].

*Resolved* +
This issue is resolved in 8.15.0.
.{webhook-cm} connector fails to send HTTP headers
*Details* +
If you configured the {webhook-cm} connector to send key-value pairs as headers, that information is not sent unles you have also enabled the basic authentication option for the connector.
Refer to [#189394](https://github.com/elastic/kibana/issues/189394).

*Impact* +
The impact of this issue will vary depending on the purpose of your headers.
For example, if you added an `ApiKey` authorization header, you might receive a `401` authorization error since it's no longer sent by the connector.

*Workaround* +
To work around this issue, enable the *Require authentication for this webhook* option, which is the `hasAuth` property in the API.
You must then provide a username and password for authentication.

*Resolved* +
This issue is resolved in 8.15.0.
**When using the Observability AI Assistant with the OpenAI connector, function calling will result in an error**
*Details* +
In 8.14.3, if you are using the Observability AI Assistant with the OpenAI connector, function calling will result in an error.
The error message will look similar to this:

```
Error: an error occurred while running the action - Status code: 400. Message: API Error: model_error - Missing required parameter: 'messages[4].function_call.arguments'.
```

A fix will be available in 8.15. Users on 8.14.3 can get around this error by turning on synthetic function calling in _AI Assistant Settings_:

. In Kibana, go to *Stack Management* → *AI Assistant* → *Observability*
. Toggle the _Simulate function calling_ option to *On*.

For more information, refer to {kibana-pull}185691[#185691].

### Bug Fixes

Dashboard::
* Fixes controls getting overwritten on navigation ({kibana-pull}187509[#187509]).
Elastic Security::
For the Elastic Security 8.14.3 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].


## Kibana 8.14.2

The 8.14.2 release includes the following bug fixes and known issues.

### Known issues

**Creating or editing APM, Observability and {stack-monitor-app} rules fails**
*Details* +
When you attempt to create or edit some rule types in **{stack-manage-app}** > **{rules-ui}**, the request will fail with errors similar to `Cannot read properties of undefined (reading 'eui')` or `e.theme.eui is undefined`.
Refer to [#186969](https://github.com/elastic/kibana/issues/186969)

*Impact* +
This known issue impacts only Observability, {stack-monitor-app}, and APM and {user-experience} rules.

*Workaround* +
To work around this issue for Observability and APM and {user-experience} rules, create them from the Observability *Alerts* page.
Refer to apm-alerts and {observability-guide}/create-alerts-rules.html[Create and manage Observability rules].

*Resolved* +
This issue is resolved in 8.15.0.
.{webhook-cm} connector fails to send HTTP headers
*Details* +
If you configured the {webhook-cm} connector to send key-value pairs as headers, that information is not sent unles you have also enabled the basic authentication option for the connector.
Refer to [#189394](https://github.com/elastic/kibana/issues/189394).

*Impact* +
The impact of this issue will vary depending on the purpose of your headers.
For example, if you added an `ApiKey` authorization header, you might receive a `401` authorization error since it's no longer sent by the connector.

*Workaround* +
To work around this issue, enable the *Require authentication for this webhook* option, which is the `hasAuth` property in the API.
You must then provide a username and password for authentication.

*Resolved* +
This issue is resolved in 8.15.0.

### Bug Fixes

Alerting::
* Rule runs recovered actions without ever running active actions ({kibana-pull}183646[#183646]).
Fleet::
* Updates health_check endpoint to accept hosts ids ({kibana-pull}185014[#185014]).
Machine Learning::
* AIOps Log Rate Analysis: Fixes text field selection ({kibana-pull}186176[#186176]).
Presentation::
* Fixes PresentationPanelError component throwing when error.message is empty string ({kibana-pull}186098[#186098]).


## Kibana 8.14.1

The 8.14.1 release includes the following bug fixes and known issues.

### Known issues

**Creating or editing APM, Observability and {stack-monitor-app} rules fails**
*Details* +
When you attempt to create or edit some rule types in **{stack-manage-app}** > **{rules-ui}**, the request will fail with errors similar to `Cannot read properties of undefined (reading 'eui')` or `e.theme.eui is undefined`.
Refer to [#186969](https://github.com/elastic/kibana/issues/186969)

*Impact* +
This known issue impacts only Observability, {stack-monitor-app}, and APM and {user-experience} rules.

*Workaround* +
To work around this issue for Observability and APM and {user-experience} rules, create them from the Observability *Alerts* page.
Refer to apm-alerts and {observability-guide}/create-alerts-rules.html[Create and manage Observability rules].

*Resolved* +
This issue is resolved in 8.15.0.
.{webhook-cm} connector fails to send HTTP headers
*Details* +
If you configured the {webhook-cm} connector to send key-value pairs as headers, that information is not sent unles you have also enabled the basic authentication option for the connector.
Refer to [#189394](https://github.com/elastic/kibana/issues/189394).

*Impact* +
The impact of this issue will vary depending on the purpose of your headers.
For example, if you added an `ApiKey` authorization header, you might receive a `401` authorization error since it's no longer sent by the connector.

*Workaround* +
To work around this issue, enable the *Require authentication for this webhook* option, which is the `hasAuth` property in the API.
You must then provide a username and password for authentication.

*Resolved* +
This issue is resolved in 8.15.0.

### Bug Fixes

Data Discovery::
* Notify the user about issues with access to the default data view ({kibana-pull}184740[#184740]).
Discover::
* Fixes resetting of breakdown field in a saved search ({kibana-pull}184668[#184668]).
Elastic Security::
For the Elastic Security 8.14.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Fixes restart upgrade disabled condition ({kibana-pull}184586[#184586]).
Observability::
* Fixes editing enabled state for project monitor ({kibana-pull}184775[#184775]).
