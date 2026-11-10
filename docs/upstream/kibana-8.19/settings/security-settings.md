<!-- Converted from settings/security-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Security settings in Kibana

You do not need to configure any additional settings to use the
security features in Kibana. They are enabled by default.

**Important:** In high-availability deployments, make sure you use the same
security settings for all instances of Kibana. Also consider storing
sensitive security settings, such as encryption and decryption keys,
securely in the Kibana Keystore, instead of keeping them in clear text in
the kibana.yml file.

#### Authentication security settings

You configure authentication settings in the `xpack.security.authc` namespace in `kibana.yml`.

For example:

```yaml
xpack.security.authc:
    providers:
      basic.basic1: <1>
          order: 0 <2>
          ...

      saml.saml1: <3>
          order: 1
          ...

      saml.saml2: <4>
          order: 2
          ...

      pki.realm3:
          order: 3
          ...
    ...
```
<1> Specifies the type of authentication provider (for example, `basic`, `token`, `saml`, `oidc`, `kerberos`, `pki`) and the provider name. This setting is mandatory.
<2> Specifies the order of the provider in the authentication chain and on the Login Selector UI. This setting is mandatory.
<3> Specifies the settings for the SAML authentication provider with a `saml1` name.
<4> Specifies the settings for the SAML authentication provider with a `saml2` name.

#### Valid settings for all authentication providers

The valid settings in the `xpack.security.authc.providers` namespace vary depending on the authentication provider type. For more information, refer to kibana-authentication.

xpack.security.authc.providers.<provider-type>.<provider-name>.enabled ::
Determines if the authentication provider should be enabled. By default, Kibana enables the provider as soon as you configure any of its properties.

xpack.security.authc.providers.<provider-type>.<provider-name>.order ::
Order of the provider in the authentication chain and on the Login Selector UI.

xpack.security.authc.providers.<provider-type>.<provider-name>.description ::
Custom description of the provider entry displayed on the Login Selector UI.

xpack.security.authc.providers.<provider-type>.<provider-name>.hint ::
Custom hint for the provider entry displayed on the Login Selector UI.

xpack.security.authc.providers.<provider-type>.<provider-name>.icon ::
Custom icon for the provider entry displayed on the Login Selector UI.

xpack.security.authc.providers.<provider-type>.<provider-name>.showInSelector ::
Flag that indicates if the provider should have an entry on the Login Selector UI. Setting this to `false` doesn't remove the provider from the authentication chain.
**Note:** You are unable to set this setting to `false` for `basic` and `token` authentication providers.

xpack.security.authc.providers.<provider-type>.<provider-name>.accessAgreement.message ::
Access agreement text in Markdown format. For more information, refer to xpack-security-access-agreement.

[[xpack-security-provider-session-idleTimeout]] xpack.security.authc.providers.<provider-type>.<provider-name>.session.idleTimeout ::
Ensures that user sessions will expire after a period of inactivity. Setting this to `0` will prevent sessions from expiring because of inactivity. By default, this setting is equal to `xpack.security.session.idleTimeout`.
**Note:** Use a string of `<count>[ms\|s\|m\|h\|d\|w\|M\|Y]` (e.g. '20m', '24h', '7d', '1w').

[[xpack-security-provider-session-lifespan]] xpack.security.authc.providers.<provider-type>.<provider-name>.session.lifespan ::
Ensures that user sessions will expire after the defined time period. This behavior is also known as an "absolute timeout". If
this is set to `0`, user sessions could stay active indefinitely. By default, this setting is equal to `xpack.security.session.lifespan`.
**Note:** Use a string of `<count>[ms\|s\|m\|h\|d\|w\|M\|Y]` (e.g. '20m', '24h', '7d', '1w').

#### SAML authentication provider settings

In addition to the settings that are valid for all providers, you can specify the following settings:

xpack.security.authc.providers.saml.<provider-name>.realm ::
SAML realm in Elasticsearch that provider should use.

xpack.security.authc.providers.saml.<provider-name>.useRelayStateDeepLink ::
Determines if the provider should treat the `RelayState` parameter as a deep link in Kibana during Identity Provider initiated log in. By default, this setting is set to `false`. The link specified in `RelayState` should be a relative, URL-encoded Kibana URL. For example, the `/app/dashboards#/list` link in `RelayState` parameter would look like this: `RelayState=%2Fapp%2Fdashboards%23%2Flist`.

#### OpenID Connect authentication provider settings

In addition to the settings that are valid for all providers, you can specify the following settings:

xpack.security.authc.providers.oidc.<provider-name>.realm ::
OpenID Connect realm in Elasticsearch that the provider should use.

#### Anonymous authentication provider settings

In addition to the settings that are valid for all providers, you can specify the following settings:

**Note:** You can configure only one anonymous provider per Kibana instance.

xpack.security.authc.providers.anonymous.<provider-name>.credentials ::
Credentials that Kibana should use internally to authenticate anonymous requests to Elasticsearch.
For example:
```yaml
xpack.security.authc.providers.anonymous.anonymous1:
  credentials:
    username: "anonymous_service_account"
    password: "anonymous_service_account_password"
```

For more information, refer to anonymous-authentication.

#### HTTP authentication settings

There is a very limited set of cases when you'd want to change these settings. For more information, refer to http-authentication.

xpack.security.authc.http.enabled::
Determines if HTTP authentication should be enabled. By default, this setting is set to `true`.

xpack.security.authc.http.autoSchemesEnabled::
Determines if HTTP authentication schemes used by the enabled authentication providers should be automatically supported during HTTP authentication. By default, this setting is set to `true`.

xpack.security.authc.http.schemes[]::
List of HTTP authentication schemes that Kibana HTTP authentication should support. By default, this setting is set to `['apikey', 'bearer']` to support HTTP authentication with the `ApiKey` and `Bearer` schemes.

#### Login user interface settings

You can configure the following settings in the `kibana.yml` file.

xpack.security.loginAssistanceMessage ::
Adds a message to the login UI. Useful for displaying information about maintenance windows, links to corporate sign up pages, and so on.

xpack.security.loginHelp ::
Adds a message accessible at the login UI with additional help information for the login process.

xpack.security.authc.selector.enabled ::
Determines if the login selector UI should be enabled. By default, this setting is set to `true` if more than one authentication provider is configured.

#### Configure a default access agreement

You can configure the following settings in the `kibana.yml` file.

xpack.security.accessAgreement.message ::
This setting specifies the access agreement text in Markdown format that will be used as the default access agreement for all providers that do not
specify a value for `xpack.security.authc.providers.<provider-type>.<provider-name>.accessAgreement.message`.
For more information, refer to xpack-security-access-agreement.

#### Session and cookie security settings

You can configure the following settings in the `kibana.yml` file.

xpack.security.cookieName::
Sets the name of the cookie used for the session. The default value is `"sid"`.

[[xpack-security-encryptionKey]] xpack.security.encryptionKey::
An arbitrary string of 32 characters or more that is used to encrypt session information. Do **not** expose this key to users of Kibana. By default, a value is automatically generated in memory. If you use that default behavior, all sessions are invalidated when Kibana restarts. In addition, high-availability deployments of Kibana will behave unexpectedly if this setting isn't the same for all instances of Kibana.

[[xpack-security-secureCookies]] xpack.security.secureCookies::
Sets the `secure` flag of the session cookie. The default value is `false`. It
is automatically set to `true` if `server.ssl.enabled` is set to `true`. Set this to `true` if SSL is configured outside of Kibana (for example, you are routing requests through a load balancer or proxy).

[[xpack-security-sameSiteCookies]] xpack.security.sameSiteCookies ::
Sets the `SameSite` attribute of the session cookie. This allows you to declare whether your cookie should be restricted to a first-party or same-site context.
Valid values are `Strict`, `Lax`, `None`.
This is *not set* by default, which modern browsers will treat as `Lax`. If you use Kibana embedded in an iframe in modern browsers, you might need to set it to `None`. Setting this value to `None` requires cookies to be sent over a secure connection by setting `xpack.security.secureCookies`: `true`.

[[xpack-session-idleTimeout]] xpack.security.session.idleTimeout ::
Ensures that user sessions will expire after a period of inactivity. This and `xpack.security.session.lifespan` are both highly recommended. You can also specify this setting for every provider separately. If this is set to `0`, then sessions will never expire due to inactivity. By default, this value is 3 days.
**Note:** Use a string of `<count>[ms\|s\|m\|h\|d\|w\|M\|Y]` (e.g. '20m', '24h', '7d', '1w').

[[xpack-session-lifespan]] xpack.security.session.lifespan ::
Ensures that user sessions will expire after the defined time period. This behavior is also known as an "absolute timeout". If this is set to `0`, user sessions could stay active indefinitely. This and `xpack.security.session.idleTimeout` are both highly
recommended. You can also specify this setting for every provider separately. By default, this value is 30 days for on-prem installations, and 24 hours for Elastic Cloud installations.
**Tip:** Use a string of `<count>[ms\|s\|m\|h\|d\|w\|M\|Y]` (e.g. '20m', '24h', '7d', '1w').

xpack.security.session.cleanupInterval ::
Sets the interval at which Kibana tries to remove expired and invalid sessions from the session index. By default, this value is 1 hour. The minimum value is 10 seconds.
**Tip:** Use a string of `<count>[ms\|s\|m\|h\|d\|w\|M\|Y]` (e.g. '20m', '24h', '7d', '1w').

xpack.security.session.concurrentSessions.maxSessions ::
Set the maximum number of sessions each user is allowed to have active at any given time.
By default, no limit is applied.
If set, the value of this option should be an integer between `1` and `1000`.
When the limit is exceeded, the oldest session is automatically invalidated.

#### Encrypted saved objects settings

These settings control the encryption of saved objects with sensitive data. For more details, refer to xpack-security-secure-saved-objects.

[[xpack-encryptedSavedObjects-encryptionKey]] xpack.encryptedSavedObjects.encryptionKey::
An arbitrary string of at least 32 characters that is used to encrypt sensitive properties of saved objects before they're stored in Elasticsearch. If not set, Kibana will generate a random key on startup, but certain features won't be available until you set the encryption key explicitly.

[[xpack-encryptedSavedObjects-keyRotation-decryptionOnlyKeys]] xpack.encryptedSavedObjects.keyRotation.decryptionOnlyKeys::
An optional list of previously used encryption keys. Like `xpack.encryptedSavedObjects.encryptionKey`, these must be at least 32 characters in length. Kibana doesn't use these keys for encryption, but may still require them to decrypt some existing saved objects. Use this setting if you wish to change your encryption key, but don't want to lose access to saved objects that were previously encrypted with a different key.

#### Audit logging settings

You can enable audit logging to support compliance, accountability, and security. When enabled, Kibana will capture:

* Who performed an action
* What action was performed
* When the action occurred

For more details and a reference of audit events, refer to xpack-security-audit-logging.

xpack.security.audit.enabled ::
Set to `true` to enable audit logging`. *Default:* `false`
For example:
```yaml
xpack.security.audit.enabled: true
xpack.security.audit.appender: <1>
  type: rolling-file
  fileName: ./logs/audit.log
  policy:
    type: time-interval
    interval: 24h <2>
  strategy:
    type: numeric
    max: 10 <3>
  layout:
    type: json
```
<1> This appender is the default and will be used if no `appender.*` config options are specified.
<2> Rotates log files every 24 hours.
<3> Keeps maximum of 10 log files before deleting older ones.

xpack.security.audit.appender::
Optional. Specifies where audit logs should be written to and how they should be formatted. If no appender is specified, a default appender will be used (see above).

xpack.security.audit.appender.type::
Required. Specifies where audit logs should be written to. Allowed values are `console`, `file`, or `rolling-file`.
Refer to audit-logging-file-appender and audit-logging-rolling-file-appender for appender specific settings.

xpack.security.audit.appender.layout.type::
Required. Specifies how audit logs should be formatted. Allowed values are `json` or `pattern`.
Refer to audit-logging-pattern-layout for layout specific settings.
**Tip:** We recommend using `json` format to allow ingesting Kibana audit logs into Elasticsearch using Filebeat.

#### File appender

The `file` appender writes to a file and can be configured using the following settings:

xpack.security.audit.appender.fileName::
Required. Full file path the log file should be written to.

#### Rolling file appender

The `rolling-file` appender writes to a file and rotates it using a rolling strategy, when a particular policy is triggered:

xpack.security.audit.appender.fileName::
Required. Full file path the log file should be written to.

xpack.security.audit.appender.policy.type::
Specifies when a rollover should occur. Allowed values are `size-limit` and `time-interval`. *Default:* `time-interval`.
Refer to audit-logging-size-limit-policy and audit-logging-time-interval-policy for policy specific settings.

xpack.security.audit.appender.strategy.type::
Specifies how the rollover should occur. Only allowed value is currently `numeric`. *Default:* `numeric`
Refer to audit-logging-numeric-strategy for strategy specific settings.

#### Size limit triggering policy

The `size-limit` triggering policy will rotate the file when it reaches a certain size:

xpack.security.audit.appender.policy.size::
Maximum size the log file should reach before a rollover should be performed. *Default:* `100mb`

#### Time interval triggering policy

The `time-interval` triggering policy will rotate the file every given interval of time:

xpack.security.audit.appender.policy.interval::
How often a rollover should occur. *Default:* `24h`

xpack.security.audit.appender.policy.modulate::
Whether the interval should be adjusted to cause the next rollover to occur on the interval boundary. *Default:* `true`

#### Numeric rolling strategy

The `numeric` rolling strategy will suffix the log file with a given pattern when rolling over, and will retain a fixed number of rolled files:

xpack.security.audit.appender.strategy.pattern::
Suffix to append to the file name when rolling over. Must include `%i`. *Default:* `-%i`

xpack.security.audit.appender.strategy.max::
Maximum number of files to keep. Once this number is reached, oldest files will be deleted. *Default:* `7`

#### Pattern layout

The `pattern` layout outputs a string, formatted using a pattern with special placeholders, which will be replaced with data from the actual log message:

xpack.security.audit.appender.layout.pattern::
Optional. Specifies how the log line should be formatted. *Default:* `[%date][%level][%logger]%meta %message`

xpack.security.audit.appender.layout.highlight::
Optional. Set to `true` to enable highlighting log messages with colors.

#### Ignore filters

xpack.security.audit.ignore_filters[] ::
List of filters that determine which events should be excluded from the audit log. An event will get filtered out if at least one of the provided filters matches.
For example:
```yaml
xpack.security.audit.ignore_filters:
- actions: [http_request] <1>
- categories: [database]
  types: [creation, change, deletion] <2>
- spaces: [default] <3>
- users: [elastic, kibana_system] <4>
```
<1> Filters out HTTP request events
<2> Filters out any data write events
<3> Filters out events from the `default` space
<4> Filters out events from the `elastic` and `kibana_system` users

xpack.security.audit.ignore_filters[].actions[] ::
List of values matched against the `event.action` field of an audit event. Refer to xpack-security-audit-logging for a list of available events.

xpack.security.audit.ignore_filters[].categories[] ::
List of values matched against the `event.category` field of an audit event. Refer to [ECS categorization field](https://www.elastic.co/guide/en/ecs/1.5/ecs-allowed-values-event-category.html) for allowed values.

xpack.security.audit.ignore_filters[].outcomes[] ::
List of values matched against the `event.outcome` field of an audit event. Refer to [ECS outcome field](https://www.elastic.co/guide/en/ecs/1.5/ecs-allowed-values-event-outcome.html) for allowed values.

xpack.security.audit.ignore_filters[].spaces[] ::
List of values matched against the `kibana.space_id` field of an audit event. This represents the space id in which the event took place.

xpack.security.audit.ignore_filters[].types[] ::
List of values matched against the `event.type` field of an audit event. Refer to [ECS type field](https://www.elastic.co/guide/en/ecs/1.5/ecs-allowed-values-event-type.html) for allowed values.

xpack.security.audit.ignore_filters[].users[] ::
List of values matched against the `user.name` field of an audit event. This represents the `username` associated with the audit event.
