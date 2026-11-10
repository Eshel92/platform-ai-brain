<!-- Converted from settings/alert-action-settings.asciidoc (AsciiDoc). Includes are inlined. -->

## Alerting and action settings in Kibana

Alerting and actions are enabled by default in Kibana, but require you to configure the following:

. Set up Kibana to work with Elastic Stack security features.
. Set up TLS encryption between Kibana and Elasticsearch.
. If you are using an *on-premises* Elastic Stack deployment, specify a value for `xpack.encryptedSavedObjects.encryptionKey`.

You can configure the following settings in the `kibana.yml` file.

### General settings

`xpack.encryptedSavedObjects.encryptionKey`::
A string of 32 or more characters used to encrypt sensitive properties on alerting rules and actions before they're stored in Elasticsearch. Third party credentials &mdash; such as the username and password used to connect to an SMTP service &mdash; are an example of encrypted properties.
Kibana offers a CLI tool to help generate this encryption key.
If not set, Kibana will generate a random key on startup, but all alerting and action functions will be blocked. Generated keys are not allowed for alerting and actions because when a new key is generated on restart, existing encrypted data becomes inaccessible. For the same reason, alerting and actions in high-availability deployments of Kibana will behave unexpectedly if the key isn't the same on all instances of Kibana.
Although the key can be specified in clear text in `kibana.yml`, it's recommended to store this key securely in the Kibana Keystore.
Be sure to back up the encryption key value somewhere safe, as your alerting rules and actions will cease to function due to decryption failures should you lose it.  If you want to rotate the encryption key, be sure to follow the instructions on encryption key rotation.

### Action settings

`xpack.actions.allowedHosts` ::
A list of hostnames that Kibana is allowed to connect to when built-in actions are triggered. It defaults to `["*"]`, allowing any host, but keep in mind the potential for SSRF attacks when hosts are not explicitly added to the allowed hosts. An empty list `[]` can be used to block built-in actions from making any external connections.
Note that hosts associated with built-in actions, such as Slack and PagerDuty, are not automatically added to allowed hosts. If you are not using the default `["*"]` setting, you must ensure that the corresponding endpoints are added to the allowed hosts as well.

`xpack.actions.customHostSettings` ::
A list of custom host settings to override existing global settings.
Default: an empty list.
Each entry in the list must have a `url` property, to associate a connection
type (mail or https), hostname and port with the remaining options in the
entry.
In the following example, two custom host settings
are defined.  The first provides a custom host setting for mail server
`mail.example.com` using port 465 that supplies server certificate authentication
data from both a file and inline, and requires TLS for the
connection.  The second provides a custom host setting for https server
`webhook.example.com` which turns off server certificate authentication,
that will allow Kibana to connect to the server if it's using a self-signed
certificate.  The individual properties that can be used in the settings are
documented below.
xpack.actions.customHostSettings:
  - url: smtp://mail.example.com:465
    ssl:
      verificationMode: 'full'
      certificateAuthoritiesFiles: [ 'one.crt' ]
      certificateAuthoritiesData: |
          -----BEGIN CERTIFICATE-----
          MIIDTD...
          CwUAMD...
          ... multiple lines of certificate data ...
          -----END CERTIFICATE-----
    smtp:
      requireTLS: true
  - url: <WEBHOOK_URL>
    ssl:
      verificationMode: 'none'
The settings in `xpack.actions.customHostSettings` can be used to override the
global option `xpack.actions.ssl.verificationMode` and provide customized TLS
settings on a per-server basis. Set `xpack.actions.ssl.verificationMode` to the
value to be used by default for all servers, then add an entry in
`xpack.actions.customHostSettings` for every server that requires customized
settings.

`xpack.actions.customHostSettings[n].url` ::
A URL associated with this custom host setting.  Should be in the form of
`protocol://hostname:port`, where `protocol` is `https` or `smtp`.  If the
port is not provided, 443 is used for `https` and 25 is used for
`smtp`.  The `smtp` URLs are used for the Email actions that use this
server, and the `https` URLs are used for actions which use `https` to
connect to services.
Entries with `https` URLs can use the `ssl` options, and entries with `smtp`
URLs can use both the `ssl` and `smtp` options.
No other URL values should be part of this URL, including paths,
query strings, and authentication information.  When an http or smtp request
is made as part of running an action, only the protocol, hostname, and
port of the URL for that request are used to look up these configuration
values.

`xpack.actions.customHostSettings[n].smtp.ignoreTLS` ::
A boolean value indicating that TLS must not be used for this connection.
The options `smtp.ignoreTLS` and `smtp.requireTLS` can not both be set to true.
Default: `false`.

`xpack.actions.customHostSettings[n].smtp.requireTLS` ::
A boolean value indicating that TLS must be used for this connection.
The options `smtp.ignoreTLS` and `smtp.requireTLS` can not both be set to true.
Default: `false`.

`xpack.actions.customHostSettings[n].ssl.rejectUnauthorized`::
deprecated:[8.0.0] Use `xpack.actions.customHostSettings.ssl.verificationMode` instead. A boolean value indicating whether to bypass server certificate validation.
Overrides the general `xpack.actions.rejectUnauthorized` configuration
for requests made for this hostname/port.

[[action-config-custom-host-verification-mode]] `xpack.actions.customHostSettings[n].ssl.verificationMode` ::
Controls the verification of the server certificate that Kibana receives when making an outbound SSL/TLS connection to the host server. Valid values are `full`, `certificate`, and `none`.
Use `full` to perform hostname verification, `certificate` to skip hostname verification, and `none` to skip verification. Default: `full`. Equivalent Kibana setting. Overrides the general `xpack.actions.ssl.verificationMode` configuration
for requests made for this hostname/port.

`xpack.actions.customHostSettings[n].ssl.certificateAuthoritiesFiles`::
A file name or list of file names of PEM-encoded certificate files to use
to validate the server.

`xpack.actions.customHostSettings[n].ssl.certificateAuthoritiesData` ::
The contents of one or more PEM-encoded certificate files in multiline format.
This configuration can be used for environments where the files cannot be made available.

[[action-config-email-maximum-body-length]] `xpack.actions.email.maximum_body_length`  ::
The maximum length of an email body in bytes. Values longer than this length will be truncated. The default is 25MB, the maximum is 25MB.

[[action-config-email-domain-allowlist]] `xpack.actions.email.domain_allowlist`  ::
A list of allowed email domains which can be used with the email connector. When this setting is not used, all email domains are allowed. When this setting is used, if any email is attempted to be sent that (a) includes an addressee with an email domain that is not in the allowlist, or (b) includes a from address domain that is not in the allowlist, it will fail with a message indicating the email is not allowed.
**Warning:** This feature is available in Kibana 7.17.4 and 8.3.0 onwards but is not supported in Kibana 8.0, 8.1 or 8.2. As such, this setting should be removed before upgrading from 7.17 to 8.0, 8.1 or 8.2. It is possible to configure the settings in 7.17.4 and then upgrade to 8.3.0 directly.

[[actions-config-email-services-ses-host]] `xpack.actions.email.services.ses.host`  ::
The SMTP endpoint for an Amazon Simple Email Service (SES) service provider that can be used by email connectors.
**Warning:** This setting alone is insufficient for overriding system defaults for the SES SMTP endpoint. You must also configure the `xpack.actions.email.services.ses.port` setting.

[[actions-config-email-services-ses-port]] `xpack.actions.email.services.ses.port`  ::
The port number for an Amazon Simple Email Service (SES) service provider that can be used by email connectors.

[[xpack.actions.email.services.enabled]] `xpack.actions.email.services.enabled`  ::
An array of strings indicating all email services that are enabled. Available options are `elastic-cloud`, `google-mail`, `microsoft-outlook`, `amazon-ses`, `microsoft-exchange`, and `other`. If the array is empty, no email services are enabled. The default value is `["*"]`, which enables all email services.

`xpack.actions.enableFooterInEmail` ::
A boolean value indicating that a footer with a relevant link should be added to emails sent as alerting actions. Default: true.

`xpack.actions.enabledActionTypes` ::
A list of action types that are enabled. It defaults to `["*"]`, enabling all types. The names for built-in Kibana action types are prefixed with a `.` and include: `.email`, `.index`, `.jira`, `.opsgenie`, `.pagerduty`, `.resilient`, `.server-log`, `.servicenow`, .`servicenow-itom`, `.servicenow-sir`, `.slack`, `.swimlane`, `.teams`, `.thehive`, `.tines`, `.torq`, `.xmatters`,  `.gen-ai`,  `.bedrock`, `.gemini`,  `.d3security`, and `.webhook`. An empty list `[]` will disable all action types.
Disabled action types will not appear as an option when creating new connectors, but existing connectors and actions of that type will remain in Kibana and will not function.

**Important:** Preconfigured connectors are not affected by this setting.

`xpack.actions.microsoftExchangeUrl`::
The URL for the Microsoft Azure Active Directory endpoint to use for MS Exchange email authentication. Default: `https://login.microsoftonline.com`.

`xpack.actions.microsoftGraphApiUrl`::
The URL for the Microsoft Graph API endpoint to use for MS Exchange email authentication. Default: `https://graph.microsoft.com/v1.0`.

`xpack.actions.microsoftGraphApiScope`::
The URL for the Microsoft Graph API scope endpoint to use for MS Exchange email authentication. Default: `https://graph.microsoft.com/.default`.

`xpack.actions.proxyUrl` ::
Specifies the proxy URL to use, if using a proxy for actions. By default, no proxy is used.
Proxies may be used to proxy http or https requests through a proxy using the http or https protocol.  Kibana only uses proxies in "CONNECT" mode (sometimes referred to as "tunneling" TCP mode, compared to HTTP mode).  That is, Kibana will always make requests through a proxy using the HTTP `CONNECT` method.
If your proxy is using the https protocol (vs the http protocol), the setting `xpack.actions.ssl.proxyVerificationMode: none` will likely be needed, unless your proxy's certificates are signed using a publicly available certificate authority.
There is currently no support for using basic authentication with a proxy (authentication for the proxy itself, not the URL being requested through the proxy).
To help diagnose problems using a proxy, you can use the `curl` command with options to use your proxy, and log debug information, with the following command, replacing the proxy and target URLs as appropriate.  This will force the request to be made to the
proxy in tunneling mode, and display some of the interaction between the client and the proxy.
curl --verbose --proxytunnel --proxy http://localhost:8080 <EXAMPLE_URL>

`xpack.actions.proxyBypassHosts` ::
Specifies hostnames which should not use the proxy, if using a proxy for actions. The value is an array of hostnames as strings. Example:
```yaml
# If applicable, include the subdomain in the hostname
xpack.actions.proxyBypassHosts: [ "events.pagerduty.com" ]
```
By default, all hosts will use the proxy, but if an action's hostname is in this list, the proxy will not be used.  The settings `xpack.actions.proxyBypassHosts` and `xpack.actions.proxyOnlyHosts` cannot be used at the same time.

`xpack.actions.proxyOnlyHosts` ::
Specifies hostnames which should only use the proxy, if using a proxy for actions. The value is an array of hostnames as strings. Example:
```yaml
# If applicable, include the subdomain in the hostname
xpack.actions.proxyOnlyHosts: [ "events.pagerduty.com" ]
```
By default, no hosts will use the proxy, but if an action's hostname is in this list, the proxy will be used.  The settings `xpack.actions.proxyBypassHosts` and `xpack.actions.proxyOnlyHosts` cannot be used at the same time.

`xpack.actions.proxyHeaders` ::
Specifies HTTP headers for the proxy, if using a proxy for actions. Default: {}.

`xpack.actions.proxyRejectUnauthorizedCertificates` ::
deprecated:[8.0.0] Use `xpack.actions.ssl.proxyVerificationMode` instead. Set to `false` to bypass certificate validation for the proxy, if using a proxy for actions. Default: `true`.

[[action-config-proxy-verification-mode]]`xpack.actions.ssl.proxyVerificationMode` ::
Controls the verification for the proxy server certificate that Kibana receives when making an outbound SSL/TLS connection to the proxy server. Valid values are `full`, `certificate`, and `none`.
Use `full` to perform hostname verification, `certificate` to skip hostname verification, and `none` to skip verification. Default: `full`. Equivalent Kibana setting.

`xpack.actions.rejectUnauthorized` ::
deprecated:[8.0.0] Use `xpack.actions.ssl.verificationMode` instead. Set to `false` to bypass certificate validation for actions. Default: `true`.
As an alternative to setting `xpack.actions.rejectUnauthorized`, you can use the setting
`xpack.actions.customHostSettings` to set SSL options for specific servers.

[[action-config-verification-mode]] `xpack.actions.ssl.verificationMode` ::
Controls the verification for the server certificate that {hosted-ems} receives when making an outbound SSL/TLS connection for actions. Valid values are `full`, `certificate`, and `none`.
Use `full` to perform hostname verification, `certificate` to skip hostname verification, and `none` to skip verification. Default: `full`. Equivalent Kibana setting.
This setting can be overridden for specific URLs by using the setting
`xpack.actions.customHostSettings[n].ssl.verificationMode` (described above) to a different value.

`xpack.actions.maxResponseContentLength` ::
Specifies the max number of bytes of the http response for requests to external resources. Default: 1000000 (1MB).

`xpack.actions.responseTimeout` ::
Specifies the time allowed for requests to external resources. Requests that take longer are canceled.
The time is formatted as a number and a time unit (`ms`, `s`, `m`, `h`, `d`, `w`, `M`, or `Y`).
For example, `20m`, `24h`, `7d`, `1w`. Default: `60s`.

`xpack.actions.run.maxAttempts` ::
Specifies the maximum number of times an action can be attempted to run. Can be minimum 1 and maximum 10.

`xpack.actions.run.connectorTypeOverrides` ::
Overrides the configs under `xpack.actions.run` for the connector type with the given ID. List the connector type identifier and its settings in an array of objects. For example:
xpack.actions.run:
    maxAttempts: 1
    connectorTypeOverrides:
        - id: '.server-log'
          maxAttempts: 5

`xpack.actions.queued.max` ::
Specifies the maximum number of actions that can be queued. Default: 1000000

### Preconfigured connector settings

These settings vary depending on which type of preconfigured connector you're adding.
For example:

```yaml
xpack.actions.preconfigured:
  my-server-log:
    name: preconfigured-server-log-connector-type
    actionTypeId: .server-log
```

For more examples, go to pre-configured-connectors.

`xpack.actions.preconfiguredAlertHistoryEsIndex` ::
Enables a preconfigured alert history Elasticsearch Index connector. Default: `false`.

`xpack.actions.preconfigured`::
Specifies configuration details that are specific to the type of preconfigured connector.

`xpack.actions.preconfigured.<connector-id>.actionTypeId`::
The type of preconfigured connector.
For example: `.email`, `.index`, `.opsgenie`, `.server-log`, `.resilient`, `.slack`, and `.webhook`.

`xpack.actions.preconfigured.<connector-id>.config`::
The configuration details, which are specific to the type of preconfigured connector.

`xpack.actions.preconfigured.<connector-id>.config.apiProvider`::
For a OpenAI connector, specifies the OpenAI API provider, either `OpenAI` or `Azure OpenAI`.

`xpack.actions.preconfigured.<connector-id>.config.apiUrl`::
A configuration URL that varies by connector:
* For an {bedrock} connector, specifies the {bedrock} request URL.
* For an {gemini} connector, specifies the {gemini} request URL.
* For a OpenAI connector, specifies the OpenAI request URL.
* For a {ibm-r} connector, specifies the {ibm-r} instance URL.
* For a Jira connector, specifies the Jira instance URL.
* For an {opsgenie} connector, specifies the {opsgenie} URL.
* For a PagerDuty connector, specifies the PagerDuty event URL. Defaults to `https://events.pagerduty.com/v2/enqueue`.
* For a {sn-itsm}, {sn-sir}, or {sn-itom} connector specifies the ServiceNow instance URL.
* For a {swimlane} connector, specifies the {swimlane} instance URL.
**Note:** If you are using the `xpack.actions.allowedHosts` setting, make sure the hostname in the URL is added to the allowed hosts.

`xpack.actions.preconfigured.<connector-id>.config.appId`::
An application ID that varies by connector:
* For a {swimlane} connector, specifies a {swimlane} application identifier.

`xpack.actions.preconfigured.<connector-id>.config.clientId`::
A client identifier that varies by connector:
* For an email connector, specifies a GUID format value that corresponds to the client ID, which is a part of OAuth 2.0 client credentials authentication.
* For a {sn-itom}, {sn-itsm}, or {sn-sir} connector specifies the client identifier assigned to the OAuth application.

`xpack.actions.preconfigured.<connector-id>.config.configUrl`::
For an xMatters connector with basic authentication, specifies the request URL for the Elastic Alerts trigger in xMatters.

`xpack.actions.preconfigured.<connector-id>.config.createCommentJson`::
For a {webhook-cm} connector, specifies a stringified JSON payload with Mustache variables that is sent to the create comment URL to create a case comment. The required variable is `case.description`.
**Note:** The JSON is validated after the Mustache variables have been placed when the REST method runs. You should manually ensure that the JSON is valid, disregarding the Mustache variables, so the later validation will pass.

`xpack.actions.preconfigured.<connector-id>.config.createCommentMethod`::
For a {webhook-cm} connector, specifies the REST API HTTP request method to create a case comment in the third-party system.
For example: `post`, `put`(default), or `patch`.

`xpack.actions.preconfigured.<connector-id>.config.createCommentUrl`::
For a {webhook-cm} connector, specifies a REST API URL string to create a case comment by ID in the third-party system.
**Note:** If you are using the `xpack.actions.allowedHosts` setting, make sure the hostname in the URL is added to the allowed hosts.

`xpack.actions.preconfigured.<connector-id>.config.createIncidentJson`::
For a {webhook-cm} connector, specifies a stringified JSON payload with Mustache variables that is sent to the create case URL to create a case. Required variables are `case.title` and `case.description`.
**Note:** The JSON is validated after the Mustache variables have been placed when the REST method runs. You should manually ensure that the JSON is valid, disregarding the Mustache variables, so the later validation will pass.

`xpack.actions.preconfigured.<connector-id>.config.createIncidentMethod`::
For a {webhook-cm} connector, specifies the REST API HTTP request method to create a case in the third-party system, either `post`(default), `put`, or `patch`.

`xpack.actions.preconfigured.<connector-id>.config.createIncidentUrl`::
For a {webhook-cm} connector, specifies a REST API URL string to create a case in the third-party system.
**Note:** If you are using the `xpack.actions.allowedHosts` setting, make sure the hostname in the URL is added to the allowed hosts.

`xpack.actions.preconfigured.<connector-id>.config.createIncidentResponseKey`::
For a {webhook-cm} connector, specifies a string from the response body of the create case method that corresponds to the external service identifier.

`xpack.actions.preconfigured.<connector-id>.config.defaultModel`::
The default model to use for requests, which varies by connector:
* For an {bedrock} connector, current support is for the Anthropic Claude models. Defaults to `anthropic.claude-3-5-sonnet-20240620-v1:0`.
* For a {gemini} connector, current support is for the Gemini models. Defaults to `gemini-2.5-pro`.
* For a OpenAI connector, it is optional and applicable only when `xpack.actions.preconfigured.<connector-id>.config.apiProvider` is `OpenAI`.

`xpack.actions.preconfigured.<connector-id>.config.executionTimeField`::
For an index connector, a field that indicates when the document was indexed.

`xpack.actions.preconfigured.<connector-id>.config.from`::
For an email connector, specifies the from address for all emails sent by the connector.
It must be specified in `user@host-name` format.

`xpack.actions.preconfigured.<connector-id>.config.getIncidentResponseExternalTitleKey`::
For a {webhook-cm} connector, specifies a string from the response body of the get case method that corresponds to the external service title.

`xpack.actions.preconfigured.<connector-id>.config.getIncidentUrl`::
For a {webhook-cm} connector, specifies a REST API URL string with an external service ID Mustache variable to get the case from the third-party system.
**Note:** If you are using the `xpack.actions.allowedHosts` setting, make sure the hostname in the URL is added to the allowed hosts. 

`xpack.actions.preconfigured.<connector-id>.config.hasAuth`::
For an email, webhook, or {webhook-cm} connector, specifies whether a user and password are required inside the secrets configuration. Defaults to `true`.

`xpack.actions.preconfigured.<connector-id>.config.headers`::
For a webhook or {webhook-cm} connector, specifies a set of key-value pairs sent as headers with the request.

`xpack.actions.preconfigured.<connector-id>.config.host`::
For an email connector, specifies the host name of the service provider.

`xpack.actions.preconfigured.<connector-id>.config.index`::
For an index connector, specifies the Elasticsearch index.

`xpack.actions.preconfigured.<connector-id>.config.isOAuth`::
For a {sn-itsm}, {sn-sir}, or {sn-itom} connector, specifies whether to use basic or OAuth authentication.

`xpack.actions.preconfigured.<connector-id>.config.jwtKeyId`::
For a {sn-itsm}, {sn-sir}, or {sn-itom} connector, specifies the key ID assigned to the JWT verifier map of your OAuth application. It is required when `xpack.actions.preconfigured.<connector-id>.config.isOAuth` is `true`.

`xpack.actions.preconfigured.<connector-id>.config.mappings`::
For a Swimlane connector, specifies field mappings.

`xpack.actions.preconfigured.<connector-id>.config.mappings.alertIdConfig`::
For a Swimlane connector, field mapping for the alert identifier.
You must provide `fieldtype`, `id`, `key`, and `name` values.

`xpack.actions.preconfigured.<connector-id>.config.mappings.caseIdConfig`::
For a Swimlane connector, field mapping for the case identifier.
You must provide `fieldtype`, `id`, `key`, and `name` values.

`xpack.actions.preconfigured.<connector-id>.config.mappings.caseNameConfig`::
For a Swimlane connector, field mapping for the case name.
You must provide `fieldtype`, `id`, `key`, and `name` values.

`xpack.actions.preconfigured.<connector-id>.config.mappings.commentsConfig`::
For a Swimlane connector, field mapping for the case comments.
You must provide `fieldtype`, `id`, `key`, and `name` values.

`xpack.actions.preconfigured.<connector-id>.config.mappings.descriptionConfig`::
For a Swimlane connector, field mapping for the case description.
You must provide `fieldtype`, `id`, `key`, and `name` values.

`xpack.actions.preconfigured.<connector-id>.config.mappings.ruleNameConfig`::
For a Swimlane connector, field mapping for the rule name.
You must provide `fieldtype`, `id`, `key`, and `name` values.

`xpack.actions.preconfigured.<connector-id>.config.mappings.severityConfig`::
For a Swimlane connector, specifies a field mapping for the severity.
You must provide `fieldtype`, `id`, `key`, and `name` values.

`xpack.actions.preconfigured.<connector-id>.config.method`::
For a webhook connector, specifies the HTTP request method, either `post` or `put`. Defaults to `post`.

`xpack.actions.preconfigured.<connector-id>.config.orgId`::
For an {ibm-r} connector, specifies the {ibm-r} organization identifier.

`xpack.actions.preconfigured.<connector-id>.config.port`::
For an email connector, specifies the port to connect to on the service provider.

`xpack.actions.preconfigured.<connector-id>.config.projectKey`::
For a Jira connector, specifies the Jira project key.

`xpack.actions.preconfigured.<connector-id>.config.secure`::
For an email connector, specifies whether the connection will use TLS when connecting to the service provider. If not true, the connection will initially connect over TCP then attempt to switch to TLS via the SMTP STARTTLS command.

`xpack.actions.preconfigured.<connector-id>.config.service`::
For an email connector, specifies the name of the email service. For example, `elastic_cloud`, `exchange_server`, `gmail`, `other`, `outlook365`, or `ses`.

`xpack.actions.preconfigured.<connector-id>.config.tenantId`::
For an email connector, specifies a GUID format value that corresponds to a tenant ID, which is a part of OAuth 2.0 client credentials authentication.

`xpack.actions.preconfigured.<connector-id>.config.updateIncidentJson`::
For a {webhook-cm} connector, specifies a stringified JSON payload with Mustache variables that is sent to the update case URL to update a case. Required variables are `case.title` and `case.description`.
**Note:** The JSON is validated after the Mustache variables have been placed when the REST method runs. You should manually ensure that the JSON is valid, disregarding the Mustache variables, so the later validation will pass.

`xpack.actions.preconfigured.<connector-id>.config.updateIncidentMethod`::
For a {webhook-cm} connector, specifies the REST API HTTP request method to update the case in the third-party system.
For example: `post`, `put`(default), or `patch`.

`xpack.actions.preconfigured.<connector-id>.config.updateIncidentUrl`::
For a {webhook-cm} connector, specifies the REST API URL to update the case by ID in the third-party system.
**Note:** If you are using the `xpack.actions.allowedHosts` setting, make sure the hostname in the URL is added to the allowed hosts.

`xpack.actions.preconfigured.<connector-id>.config.url`::
A configuration URL that varies by connector:
* For a D3 Security connector, specifies the D3 Security API request URL.
* For a Tines connector, specifies the Tines tenant URL.
* For a webhook connector, specifies the web service request URL.

**Note:** If you are using the `xpack.actions.allowedHosts` setting, make sure this hostname is added to the allowed hosts.

`xpack.actions.preconfigured.<connector-id>.config.userIdentifierValue`::
For a {sn-itsm}, {sn-sir}, or {sn-itom} connector, specifies the user identifier. It is required when required when `xpack.actions.preconfigured.<connector-id>.config.isOAuth` is `true`.

`xpack.actions.preconfigured.<connector-id>.config.usesBasic`::
For an xMatters connector, specifies whether it uses HTTP basic authentication. Defaults to `true`.

`xpack.actions.preconfigured.<connector-id>.config.usesTableApi`::
For a {sn-itsm} or {sn-sir} connector, specifies whether the connector uses the Table API or the Import Set API.
If set to `false`, the Elastic application should be installed in ServiceNow.

`xpack.actions.preconfigured.<connector-id>.config.viewIncidentUrl`::
For a {webhook-cm} connector, specifies a URL string with either the external service ID or external service title Mustache variable to view a case in the external system.

`xpack.actions.preconfigured.<connector-id>.config.webhookIntegrationUrl`::
For a Torq connector, specifies the endpoint URL of the Elastic Security integration in Torq.

`xpack.actions.preconfigured.<connector-id>.name`::
The name of the preconfigured connector.

`xpack.actions.preconfigured.<connector-id>.secrets`::
Sensitive configuration details, such as username, password, and keys, which are specific to the connector type.
**Tip:** Sensitive properties, such as passwords, should be stored in the Kibana keystore.

`xpack.actions.preconfigured.<connector-id>.secrets.accessKey`::
For an {bedrock} connector, specifies the AWS access key for authentication.

`xpack.actions.preconfigured.<connector-id>.secrets.apikey`::
An API key secret that varies by connector:

`xpack.actions.preconfigured.<connector-id>.secrets.credentialsJson`::
For an {gemini} connector, specifies the GCP service account credentials JSON file for authentication.
* For a OpenAI connector, specifies the OpenAI or Azure OpenAI API key for authentication.
* For an {opsgenie} connector, specifies the {opsgenie} API authentication key for HTTP basic authentication.

`xpack.actions.preconfigured.<connector-id>.secrets.apiKeyId`::
For an {ibm-r} connector, specifies the authentication key ID for HTTP basic authentication.

`xpack.actions.preconfigured.<connector-id>.secrets.apiKeySecret`::
For an {ibm-r} connector, specifies the authentication key secret for HTTP basic authentication.

`xpack.actions.preconfigured.<connector-id>.secrets.apiToken`::
For a Jira or {swimlane} connector, specifies the API authentication token for HTTP basic authentication.

`xpack.actions.preconfigured.<connector-id>.secrets.clientSecret`::
A client secret that varies by connector:
* For an email connector, specifies the client secret that you generated for your app in the app registration portal. It is required when the email service is `exchange_server`, which uses OAuth 2.0 client credentials authentication.
* For a {sn-itsm}, {sn-sir}, or {sn-itom} connector, specifies the client secret assigned to the OAuth application. It is required when `xpack.actions.preconfigured.<connector-id>.config.isOAuth` is `true`.

**Note:** The client secret must be URL-encoded.

`xpack.actions.preconfigured.<connector-id>.secrets.email`::
An email address that varies by connector:
* For a Jira connector, specifies the account email for HTTP basic authentication.
* For a Tines connector, specifies the email used to sign in to Tines.

`xpack.actions.preconfigured.<connector-id>.secrets.password`::
A password secret that varies by connector:

* For an email, webhook, or {webhook-cm} connector, specifies a password that is required when `xpack.actions.preconfigured.<connector-id>.config.hasAuth` is `true`.
* For a {sn-itsm}, {sn-sir}, or {sn-itom} connector, specifies a password that is required when `xpack.actions.preconfigured.<connector-id>.config.isOAuth` is `false`.
* For an xMatters connector, specifies a password that is required when `xpack.actions.preconfigured.<connector-id>.config.usesBasic` is `true`.

`xpack.actions.preconfigured.<connector-id>.secrets.privateKey`::
For a {sn-itsm}, {sn-sir}, or {sn-itom} connector, specifies the RSA private key. It is required when `xpack.actions.preconfigured.<connector-id>.config.isOAuth` is `true`.

`xpack.actions.preconfigured.<connector-id>.secrets.privateKeyPassword`::
For a {sn-itsm}, {sn-sir}, or {sn-itom} connector, specifies the password for the RSA private key.

`xpack.actions.preconfigured.<connector-id>.secrets.routingKey`::
For a PagerDuty connector, specifies the 32 character PagerDuty Integration Key for an integration on a service, also referred to as the routing key.

`xpack.actions.preconfigured.<connector-id>.secrets.secret`::
For an {bedrock} connector, specifies the AWS secret for authentication.

`xpack.actions.preconfigured.<connector-id>.secrets.secretsUrl`::
For an xMatters connector with URL authentication, specifies the request URL for the Elastic Alerts trigger in xMatters with the API key included in the URL.
It is used only when `xpack.actions.preconfigured.<connector-id>.config.usesBasic` is `false`.
**Note:** If you are using the `xpack.actions.allowedHosts` setting, make sure this hostname is added to the allowed hosts.

`xpack.actions.preconfigured.<connector-id>.secrets.token`::
A token secret that varies by connector:
* For a D3 Security conector, specifies the D3 Security token.
* For a Slack connector, specifies the Slack bot user OAuth token.
* For a Tines connector, specifies the Tines API token.
* For a Torq connector, specifies the secret of the webhook authentication header.

`xpack.actions.preconfigured.<connector-id>.secrets.user`::
A user name secret that varies by connector:
* For an email, webhook, or {webhook-cm} connector, specifies a user name that is required when `xpack.actions.preconfigured.<connector-id>.config.hasAuth` is `true`.
* For an xMatters connector, specifies a user name that is required when `xpack.actions.preconfigured.<connector-id>.config.usesBasic` is `true`.

`xpack.actions.preconfigured.<connector-id>.secrets.webhookUrl`::
A URL that varies by connector:
* For a Microsoft Teams, specifies the URL of the incoming webhook.
For a Slack connector, specifies the Slack webhook URL.

**Note:** If you are using the `xpack.actions.allowedHosts` setting, make sure the hostname is added to the allowed hosts.

`xpack.actions.preconfigured.<connector-id>.secrets.username`::
For a {sn-itsm}, {sn-sir}, or {sn-itom} connector, specifies a user name that is required when `xpack.actions.preconfigured.<connector-id>.config.isOAuth` is `false`.

### Alerting settings

`xpack.alerting.maxEphemeralActionsPerAlert` ::
deprecated:[8.8.0]
Sets the number of actions that will run ephemerally. To use this, enable
ephemeral tasks in task manager first with
`xpack.task_manager.ephemeral_tasks.enabled`

`xpack.actions.webhook.ssl.pfx.enabled` ::
Disable PFX file support for SSL client authentication. When set to `false`, the application will not accept PFX certificate files and will require separate certificate and private key files instead. Only applies to the [Webhook connector](/reference/connectors-kibana/webhook-action-type.md).

`xpack.alerting.cancelAlertsOnRuleTimeout` ::
Specifies whether to skip writing alerts and scheduling actions if rule
processing was cancelled due to a timeout. Default: `true`. This setting can be
overridden by individual rule types.

`xpack.alerting.rules.maxScheduledPerMinute`::
Specifies the maximum number of rules to run per minute. Default: 32000

`xpack.alerting.rules.minimumScheduleInterval.value` ::
Specifies the minimum schedule interval for rules. This minimum is applied to all rules created or updated after you set this value.
The time is formatted as a number and a time unit (`s`, `m`, `h`, or `d`). 
For example, `20m`, `24h`, `7d`. This duration cannot exceed `1d`. Default: `1m`.

`xpack.alerting.rules.minimumScheduleInterval.enforce` ::
Specifies the behavior when a new or changed rule has a schedule interval less than the value defined in `xpack.alerting.rules.minimumScheduleInterval.value`. If `false`, rules with schedules less than the interval will be created but warnings will be logged. If `true`, rules with schedules less than the interval cannot be created. Default: `false`.

`xpack.alerting.rules.run.actions.max` ::
Specifies the maximum number of actions that a rule can generate each time detection checks run.

`xpack.alerting.rules.run.alerts.max` ::
Specifies the maximum number of alerts that a rule can generate each time detection checks run. Default: 1000.
**Warning:** The exact number of alerts your cluster can safely handle depends on your cluster configuration and workload, however setting a value higher than the default (`1000`) is not recommended or supported. Doing so could strain system resources and lead to performance issues, delays in alert processing, and potential disruptions during high alert activity periods.

`xpack.alerting.rules.run.timeout` ::
Specifies the default timeout for tasks associated with all types of rules.
The time is formatted as a number and a time unit (`ms`, `s`, `m`, `h`, `d`, `w`, `M`, or `Y`).
For example, `20m`, `24h`, `7d`, `1w`. Default: `5m`.

`xpack.alerting.rules.run.ruleTypeOverrides` ::
Overrides the configs under `xpack.alerting.rules.run` for the rule type with the given ID. List the rule identifier and its settings in an array of objects. For example:
xpack.alerting.rules.run:
    timeout: '5m'
    ruleTypeOverrides:
        - id: '.index-threshold'
          timeout: '15m'

`xpack.alerting.rules.run.actions.connectorTypeOverrides` ::
Overrides the configs under `xpack.alerting.rules.run.actions` for the connector type with the given ID. List the connector type identifier and its settings in an array of objects. For example:
xpack.alerting.rules.run:
    actions:
        max: 10
        connectorTypeOverrides:
            - id: '.server-log'
              max: 5
