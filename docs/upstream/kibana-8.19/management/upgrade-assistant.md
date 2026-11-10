<!-- Converted from management/upgrade-assistant.asciidoc (AsciiDoc). Includes are inlined. -->

## Upgrade Assistant

The Upgrade Assistant helps you prepare for your upgrade 
to the next version of the Elastic Stack.
To access the assistant, go to *{stack-manage-app} > Upgrade Assistant*.

The assistant identifies deprecated settings in your configuration
and guides you through the process of resolving issues if any deprecated features are enabled.

### Required permissions

The `manage` cluster privilege is required to access the *Upgrade assistant*.
Additional privileges may be needed to perform certain actions.

### Feature set

Some features of the Upgrade assistant are only needed when upgrading to a new major version. The feature set enabled by default are those for the very next version from the one Kibana currently runs on.

### Deprecations

The Upgrade assistant pulls information about deprecations from the following sources:

* Elasticsearch Deprecation Info API
* Elasticsearch deprecation logs
* Kibana deprecations API

For more information about Upgrade Assistant APIs, refer to Upgrade Assistant APIs.
