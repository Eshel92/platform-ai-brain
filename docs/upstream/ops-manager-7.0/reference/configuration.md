<!-- Converted from reference/configuration.txt (reStructuredText). Includes are inlined. -->

# Ops Manager Configuration Settings

Ops Manager stores configuration settings both globally in the
Ops Manager Application Database and locally on each server. Global settings
apply to all your Ops Manager servers. Local settings apply to the server
on which they are configured. Any local settings on a server override
the global settings.

You configure local settings through a server's `conf-mms.properties`
file. Each server's `conf-mms.properties` must contain the connection
string and authentication settings for accessing the Ops Manager
Application Database. The `conf-mms.properties` file also contains
any overrides of global settings specific to that server.

The location of the `conf-mms.properties` file depends on how you
installed Ops Manager, as described in the table below.

| Install method | Location of `conf-mms.properties` |
|---|---|
| `rpm` or `deb` package | `/opt/mongodb/mms/conf/` |
| `tar.gz` archive | `<install-directory>/conf/` |

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `configuration.parts/`)

- `001-bypass-initial-configuration-via-the-user-interfac.md`: Bypass Initial Configuration via the User Interface … Automation Default Paths
- `002-backup-http-proxy.md`: Backup … HTTP Proxy
- `003-mongodb-version-management-third-party-integration.md`: MongoDB Version Management … Third-Party Integrations
- `004-user-authentication.md`: User Authentication
- `005-web-server-webhook.md`: Web Server … Webhook
