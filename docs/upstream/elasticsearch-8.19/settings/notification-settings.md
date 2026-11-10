<!-- Converted from settings/notification-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Watcher settings in Elasticsearch

You configure Watcher settings to set up Watcher and send notifications via
email,
Slack, and
PagerDuty.

All of these settings can be added to the `elasticsearch.yml` configuration file,
with the exception of the secure settings, which you add to the Elasticsearch keystore.
For more information about creating and updating the Elasticsearch keystore, see
secure-settings. Dynamic settings can also be updated across a cluster with the
cluster update settings API.

#### General Watcher Settings

`xpack.watcher.enabled`::
(Static)
Set to `false` to disable Watcher on the node.

`xpack.watcher.encrypt_sensitive_data` ::
(Static)
Set to `true` to encrypt sensitive data. If this setting is enabled, you
must also specify the `xpack.watcher.encryption_key` setting. For more
information, see encrypting-data.

`xpack.watcher.encryption_key`::
(Secure)
Specifies the path to a file that contains a key for encrypting sensitive data.
If `xpack.watcher.encrypt_sensitive_data` is set to `true`, this setting is
required. For more information, see encrypting-data.

`xpack.watcher.max.history.record.size`::
(Static)
The maximum size watcher history record that can be written into the watcher history index. Any larger history record will have some of
its larger fields removed. Defaults to 10mb.

`xpack.http.proxy.host`::
(Static)
Specifies the address of the proxy server to use to connect to HTTP services.

`xpack.http.proxy.port`::
(Static)
Specifies the port number to use to connect to the proxy server.

`xpack.http.proxy.scheme`::
(Static)
Protocol used to communicate with the proxy server. Valid values are `http` and
`https`. Defaults to the protocol used in the request.

`xpack.http.default_connection_timeout`::
(Static)
The maximum period to wait until abortion of the request, when a
connection is being initiated.

`xpack.http.default_read_timeout`::
(Static)
The maximum period of inactivity between two data packets, before the
request is aborted.

`xpack.http.tcp.keep_alive`::
(Static)
Whether to enable TCP keepalives on HTTP connections. Defaults to `true`.

`xpack.http.connection_pool_ttl`::
(Static)
The time-to-live of connections in the connection pool. If a connection is not
re-used within this timeout, it is closed. By default, the time-to-live is
infinite meaning that connections never expire.

`xpack.http.max_response_size`::
(Static)
Specifies the maximum size an HTTP response is allowed to have, defaults to
`10mb`, the maximum configurable value is `50mb`.

`xpack.http.whitelist`::
(Dynamic)
A list of URLs, that the internal HTTP client is allowed to connect to. This
client is used in the HTTP input, the webhook, the slack, pagerduty,
and jira actions. This setting can be updated dynamically. It defaults to `*`
allowing everything. Note: If you configure this setting and you are using one
of the slack/pagerduty actions, you have to ensure that the
corresponding endpoints are explicitly allowed as well.

:server!:

(See `settings/ssl-settings.md`)

#### Email Notification Settings

You can configure the following email notification settings in
`elasticsearch.yml`. For more information about sending notifications
via email, see configuring-email-actions.

`xpack.notification.email.default_account`::
(Dynamic)
Default email account to use.
If you configure multiple email accounts, you must either configure this setting
or specify the email account to use in the `email` action. See
configuring-email.

`xpack.notification.email.recipient_allowlist`::
(Dynamic)
Specifies addresses to which emails are allowed to be sent.
Emails with recipients (`To:`, `Cc:`, or `Bcc:`) outside of these patterns will be rejected and an
error thrown. This setting defaults to `["*"]` which means all recipients are allowed.
Simple globbing is supported, such as `list-*@company.com` in the list of allowed recipients.

**Note:** This setting can't be used at the same time as `xpack.notification.email.account.domain_allowlist`
and an error will be thrown if both are set at the same time. This setting can be used to specify domains
to allow by using a wildcard pattern such as `*@company.com`.

`xpack.notification.email.account`::
Specifies account information for sending notifications via email. You
can specify the following email account attributes:

`xpack.notification.email.account.domain_allowlist`::
(Dynamic)
Specifies domains to which emails are allowed to be sent. Emails with recipients (`To:`, `Cc:`, or
`Bcc:`) outside of these domains will be rejected and an error thrown. This setting defaults to
`["*"]` which means all domains are allowed. Simple globbing is supported, such as `*.company.com`
in the list of allowed domains.

**Note:** This setting can't be used at the same time as `xpack.notification.email.recipient_allowlist`
and an error will be thrown if both are set at the same time.

`profile`::
(Dynamic)
The email profile to use to build the MIME
messages that are sent from the account. Valid values: `standard`, `gmail` and
`outlook`. Defaults to `standard`.

`email_defaults.*`::
(Dynamic)
An optional set of email attributes to use as defaults
for the emails sent from the account. See
email-action-attributes for the supported
attributes.

`smtp.auth`::
(Dynamic)
Set to `true` to attempt to authenticate the user using the
AUTH command. Defaults to `false`.

`smtp.host`::
(Dynamic)
The SMTP server to connect to. Required.

`smtp.port`::
(Dynamic)
The SMTP server port to connect to. Defaults to 25.

`smtp.user`::
(Dynamic)
The user name for SMTP. Required.

`smtp.secure_password`::
(Secure, reloadable)
The password for the specified SMTP user.

`smtp.starttls.enable`::
(Dynamic)
Set to `true` to enable the use of the `STARTTLS`
command (if supported by the server) to switch the connection to a
TLS-protected connection before issuing any login commands. Note that
an appropriate trust store must be configured so that the client will
trust the server's certificate. Defaults to `false`.

`smtp.starttls.required`::
(Dynamic)
If `true`, then `STARTTLS` will be required. If that command fails, the
connection will fail. Defaults to `false`.

`smtp.ssl.trust`::
(Dynamic)
A list of SMTP server hosts that are assumed trusted and for which
certificate verification is disabled. If set to "*", all hosts are
trusted. If set to a whitespace separated list of hosts, those hosts
are trusted. Otherwise, trust depends on the certificate the server
presents.

`smtp.timeout`::
(Dynamic)
The socket read timeout. Default is two minutes.

`smtp.connection_timeout`::
(Dynamic)
The socket connection timeout. Default is two minutes.

`smtp.write_timeout`::
(Dynamic)
The socket write timeout. Default is two minutes.

`smtp.local_address`::
(Dynamic)
A configurable local address when sending emails. Not configured by default.

`smtp.local_port`::
(Dynamic)
A configurable local port when sending emails. Not configured by default.

`smtp.send_partial`::
(Dynamic)
Send an email, despite one of the receiver addresses being invalid.

`smtp.wait_on_quit`::
(Dynamic)
If set to false the QUIT command is sent and the connection closed. If set to
true, the QUIT command is sent and a reply is waited for. True by default.

`xpack.notification.email.html.sanitization.allow`::
Specifies the HTML elements that are allowed in email notifications. For
more information, see
email-html-sanitization. You can
specify individual HTML elements and the following HTML feature groups:

`_tables`::
(Static)
All table related elements: `<table>`, `<th>`, `<tr>`, `<td>`, `<caption>`,
`<col>`, `<colgroup>`, `<thead>`, `<tbody>`, and `<tfoot>`.

`_blocks`::
(Static)
The following block elements: `<p>`, `<div>`, `<h1>`,
`<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`, `<ul>`, `<ol>`,
`<li>`, and `<blockquote>`.

`_formatting`::
(Static)
The following inline formatting elements: `<b>`, `<i>`,
`<s>`, `<u>`, `<o>`, `<sup>`, `<sub>`, `<ins>`, `<del>`,
`<strong>`, `<strike>`, `<tt>`, `<code>`, `<big>`,
`<small>`, `<hr>`, `<br>`, `<span>`, and `<em>`.

`_links`::
(Static)
The `<a>` element with an `href` attribute that points
to a URL using the following protocols: `http`, `https`
and `mailto`.

`_styles`::
(Static)
The `style` attribute on all elements. Note that CSS
attributes are also sanitized to prevent XSS attacks.

`img`::
`img:all`::
(Static)
All images (external and embedded).

`img:embedded`::
(Static)
Only embedded images. Embedded images can only use the
`cid:` URL protocol in their `src` attribute.

`xpack.notification.email.html.sanitization.disallow`::
(Static)
Specifies the HTML elements that are NOT allowed in email notifications.
You can specify individual HTML elements and <<html-feature-groups,
HTML feature groups>>.

`xpack.notification.email.html.sanitization.enabled` ::
(Static)
Set to `false` to completely disable HTML sanitation. Not recommended.
Defaults to `true`.

`xpack.notification.reporting.warning.kbn-csv-contains-formulas.text`::
(Dynamic)
Specifies a custom message, which is sent if the formula verification criteria
for CSV files from Kibana's [`xpack.reporting.csv.checkForFormulas`](https://www.elastic.co/guide/en/kibana/8.19/reporting-settings-kb.html#reporting-csv-settings) is `true`.
Use `%s` in the message as a placeholder for the filename.
Defaults to `Warning: The attachment [%s] contains characters which spreadsheet applications may interpret as formulas. Please ensure that the attachment is safe prior to opening.`

:server!:

(See `settings/ssl-settings.md`)

#### Slack Notification Settings

You can configure the following Slack notification settings in
`elasticsearch.yml`. For more information about sending notifications
via Slack, see configuring-slack-actions.

`xpack.notification.slack.default_account`::
(Dynamic)
Default Slack account to use.
If you configure multiple Slack accounts, you must either configure this setting
or specify the Slack account to use in the `slack` action. See
configuring-slack.

`xpack.notification.slack.account`::
Specifies account information for sending notifications
via Slack. You can specify the following Slack account attributes:
`secure_url`::
(Secure, reloadable)
The Incoming Webhook URL to use to post messages to Slack. Required.

`message_defaults`::
Default values for
Slack message attributes.

`from`:::
(Dynamic)
The sender name to display in the
Slack message. Defaults to the watch ID.

`to`:::
(Dynamic)
The default Slack channels or groups you
want to send messages to.

`icon`:::
(Dynamic)
The icon to display in the Slack messages.
Overrides the incoming webhook's configured
icon. Accepts a public URL to an image.

`text`:::
(Dynamic)
The default message content.

`attachment`:::
(Dynamic)
Default message attachments. Slack message attachments
enable you to create more richly-formatted messages.
Specified as an array as defined in the
https://api.slack.com/docs/attachments[
Slack attachments documentation].

#### Jira Notification Settings

You can configure the following Jira notification settings in
`elasticsearch.yml`. For more information about using notifications
to create issues in Jira, see configuring-jira-actions.

`xpack.notification.jira.default_account`::
(Dynamic)
Default Jira account to use.
If you configure multiple Jira accounts, you must either configure this setting
or specify the Jira account to use in the `jira` action. See
configuring-jira.

`xpack.notification.jira.account`::
Specifies account information for using notifications to create
issues in Jira. You can specify the following Jira account attributes:
`allow_http`::
(Dynamic)
If `false`, Watcher rejects URL settings that use a HTTP protocol. Defaults to
`false`.

`secure_url`::
(Secure, reloadable)
The URL of the Jira Software server. Required.

`secure_user`::
(Secure, reloadable)
The name of the user to connect to the Jira Software server. Required.

`secure_password`::
(Secure, reloadable)
The password of the user to connect to the Jira Software server. Required.

`issue_defaults`::
(Dynamic)
Default fields values for the issue created in Jira. See
jira-action-attributes for more information.
Optional.

#### PagerDuty Notification Settings

You can configure the following PagerDuty notification settings in
`elasticsearch.yml`. For more information about sending notifications
via PagerDuty, see configuring-pagerduty-actions.

`xpack.notification.pagerduty.default_account`::
(Dynamic)
Default PagerDuty account to use.
If you configure multiple PagerDuty accounts, you must either configure this
setting or specify the PagerDuty account to use in the
`pagerduty` action. See configuring-pagerduty.

`xpack.notification.pagerduty.account`::
Specifies account information for sending notifications via PagerDuty. You can
specify the following PagerDuty account attributes:
`name`::
(Static)
A name for the PagerDuty account associated with the API key you
are using to access PagerDuty. Required.

`secure_service_api_key`::
(Secure, reloadable)
The https://developer.pagerduty.com/documentation/rest/authentication[
PagerDuty API key] to use to access PagerDuty. Required.
`event_defaults`::
Default values for
PagerDuty event attributes.
Optional.
`description`::
(Dynamic)
A string that contains the default description for PagerDuty events.
If no default is configured, each PagerDuty action must specify a
`description`.

`incident_key`::
(Dynamic)
A string that contains the default incident key to use when sending
PagerDuty events.

`client`::
(Dynamic)
A string that specifies the default monitoring client.

`client_url`::
(Dynamic)
The URL of the default monitoring client.

`event_type`::
(Dynamic)
The default event type. Valid values: `trigger`,`resolve`, `acknowledge`.

`attach_payload`::
(Dynamic)
Whether or not to provide the watch payload as context for
the event by default. Valid values: `true`, `false`.
