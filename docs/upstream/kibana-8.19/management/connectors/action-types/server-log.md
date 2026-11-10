<!-- Converted from management/connectors/action-types/server-log.asciidoc (AsciiDoc). Includes are inlined. -->

## Server log connector and action

A server log connector writes an entry to the Kibana server log.

### Create connectors in Kibana

You can create connectors in *{stack-manage-app} > {connectors-ui}*
or as needed when you're creating a rule. For example:

(Figure: management/connectors/images/serverlog-connector.png)

#### Connector configuration

Server log connectors do not have any configuration properties other than a name.

### Test connectors

You can test connectors as you're creating or editing the connector in Kibana.
For example:

(Figure: management/connectors/images/serverlog-params-test.png)

Server log connector actions contain a message and a log level, which defaults to `info`. Valid log level values are `trace`, `debug`, `info`, `warn`, `error`,
and `fatal`.
