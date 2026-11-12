<!-- Part 44 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.0.0-alpha1

Review the Kibana 8.0.0-alpha1 changes, then use the Upgrade Assistant to complete the upgrade.

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance. Review the breaking changes, then mitigate the impact to your application.

#### Enterprise Search changes

**Required security plugin in 8.0**
*Details* +
Enterprise Search now requires that you enable X-Pack Security. For more information, refer to {kibana-pull}106307[#106307]

*Impact* +
Enable X-Pack Security.

#### Index pattern changes

**Removed support for time-based interval index patterns**
*Details* +
Time-based interval index patterns were deprecated in 5.x. In 6.x, you could no longer create time-based interval index patterns, but they continued to function as expected. Support for these index patterns has been removed in 8.0. For more information, refer to {kibana-pull}35173[#35173]

*Impact* +
You must migrate your time_based index patterns to a wildcard pattern. For example, logstash-*.

#### Operations changes

**Removed platform from archive root directory**
*Details* +
After you extract an archive, the output directory no longer includes the target platform. For example, `kibana-8.0.0-linux-aarch64.tar.gz` produces a `kibana-8.0.0` folder. For more information, refer to {kibana-pull}93835[#93835].

*Impact* +
To use the new folder, update the configuration management tools and automation.

**Removed default support for TLS v1.0 and v1.1**
*Details* +
The default support for TLS v1.0 and v1.1 has been removed. For more information, refer to {kibana-pull}90511[#90511].

*Impact* +
To enable support, set `--tls-min-1.0` in the `node.options` configuration file. To locate the configuration file, go to the kibana/config folder or any other configuration with the `KBN_PATH_CONF` environment variable. For example, if you are using a Debian-based system, the configuration file is located in /etc/kibana.

**Removed support for sysv init**
*Details* +
All supported operating systems use systemd service files. Any system that doesn’t have `service` aliased to use kibana.service should use `systemctl start kibana.service` instead of `service start kibana`. For more information, refer to {kibana-pull}74424[#74424].

*Impact* +
If your installation uses .deb or .rpm packages with SysV, migrate to systemd.

**Disabled response logging as a default**
*Details* +
In previous versions, all events are logged in `json` when `logging.json:true`. With the new logging configuration, you can choose the `json` and pattern output formats with layouts. For more information, refer to {kibana-pull}42353[#42353].

*Impact* +
To restore the previous behavior, configure the logging format for each custom appender with the `appender.layout property` in kibana.yml. There is no default for custom appenders, and each appender must be configured expilictly.

```yaml
logging:
  appenders:
    custom_console:
      type: console
      layout:
        type: pattern
    custom_json:
      type: console
      layout:
        type: json
  loggers:
    - name: plugins.myPlugin
      appenders: [custom_console]
  root:
    appenders: [default, custom_json]
    level: warn
```

#### Reporting changes

**Legacy job parameters are no longer supported**
*Details* +
*Reporting* is no longer compatible with POST URL snippets generated with Kibana 6.2.0 and earlier. For more information, refer to {kibana-pull}52539[#52539]

*Impact* +
If you use POST URL snippets to automatically generate PDF reports, regenerate the POST URL strings.

#### Security changes

**Removed `/api/security/v1/saml` route**
*Details* +
The `/api/security/v1/saml` route has been removed and is reflected in the kibana.yml `server.xsrf.whitelist` setting, Elasticsearch, and the Identity Provider SAML settings. For more information, refer to {kibana-pull}47929[#47929]

*Impact* +
Use the `/api/security/saml/callback` route, or wait to upgrade to 8.0.0-alpha2 when the `/api/security/saml/callback` route breaking change is reverted.

**Reject legacy browsers by default**
*Details* +
To provide the maximum level of protection for most installations, the csp.strict config is now enabled by default. Legacy browsers not supported by Kibana, such as Internet Explorer 11, are unable to access Kibana unless explicitly enabled. All browsers officially supported by Kibana do not have this issue. For more information, refer to {kibana-pull}41700[#41700]

*Impact* +
To enable support for legacy browsers, set `csp.strict: false` in kibana.yml. To effectively enforce the security protocol, we strongly discourage disabling `csp.strict` unless it is critical that you support Internet Explorer 11.

#### Settings changes

**Use new session timeout defaults**
*Details* +
The default values for the session timeout `xpack.security.session.{lifespan|idleTimeout}` settings have changed. For more information, refer to {kibana-pull}106061[#106061]

*Impact* +
Use the following default values:

* `xpack.security.session.idleTimeout: 3d`
* `xpack.security.session.lifespan: 30d`

**Removed support for setting `server.host` to '0'**
*Details* +
Support for configuring Kibana with `0` as the `server.host` has been removed. Please use `0.0.0.0` instead. For more information, refer to {kibana-pull}87114[#87114]

*Impact* +
You are now unable to use `0` as the `server.host`.

**Removed `xpack.security.public` and `xpack.security.authProviders`**
*Details* +
The `xpack.security.public` and `xpack.security.authProviders` settings have been removed. For more information, refer to {kibana-pull}38657[#38657]

*Impact* +
Use the `xpack.security.authc.saml.realm` and `xpack.security.authc.providers` settings.

**Removed useUTC deprecation**
*Details* +
The `logging.useUTC` setting has been removed. For more information, refer to {kibana-pull}22696[#22696]

*Impact* +
The default timezone is UTC. To change the timezone, set `logging.timezone: false` in kibana.yml. Change the timezone when the system, such as a docker container, is configured for a nonlocal timezone.

**Removed environment variables `CONFIG_PATH` and `DATA_PATH`**
*Details* +
The environment variables `CONFIG_PATH` and `DATA_PATH` have been removed.  For more information, refer to {kibana-pull}32049[#32049]

*Impact* +
Use the environment variable `KBN_PATH_CONF` instead of `CONFIG_PATH`.  Use the setting `path.data` instead of `DATA_PATH`.

### Deprecations

The following functionality is deprecated in 8.0.0, and will be removed in 9.0.0. Deprecated functionality does not have an immediate impact on your application, but we strongly recommend you make the necessary updates after you complete the upgrade.

**Removed support for SysV init**
*Details* +
Systems that don't have `service` aliased to use kibana.service are unable to use `service start kibana`. For more information, refer to {kibana-pull}74424[#74424]

*Impact* +
If your system doesn't have `service` aliased to use kibana.service, use `systemctl start kibana.service`.

**Removed `xpack:defaultAdminEmail` setting**
*Details* +
The `xpack:default_admin_email` setting for monitoring use has been removed. For more information, refer to {kibana-pull}33603[#33603]

*Impact* +
Use the `xpack.monitoring.clusterAlertsEmail` in kibana.yml.

### Bug fix

The 8.0.0-alpha1 release includes the following bug fix.

Operations::
* Moves systemd service to /usr/lib/systemd/system {kibana-pull}83571[#83571]
