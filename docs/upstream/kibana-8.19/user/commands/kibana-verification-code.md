<!-- Converted from user/commands/kibana-verification-code.asciidoc (AsciiDoc). Includes are inlined. -->

### kibana-verification-code

The `kibana-verification-code` tool retrieves a verification code for enrolling
a Kibana instance with a secured Elasticsearch cluster. 

#### Synopsis

```shell
bin/kibana-verification-code
[-V, --version] [-h, --help]
```

#### Description

Use this command to retrieve a verification code for Kibana. You enter this code
in Kibana when manually configuring a secure connection with an Elasticsearch cluster.
This tool is useful if you don’t have access to the Kibana terminal output, such
as on a hosted environment. You can connect to a machine where Kibana is
running (such as using SSH) and retrieve a verification code that you enter in
Kibana.

**Important:** You must run this tool on the same machine where Kibana is running.

#### Parameters

`-h, --help`:: Returns all of the command parameters.

`-V, --version`:: Displays the Kibana version number.

#### Examples

The following command retrieves a verification code for Kibana.

```shell
bin/kibana-verification-code
```
