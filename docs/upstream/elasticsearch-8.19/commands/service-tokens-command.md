<!-- Converted from commands/service-tokens-command.asciidoc (AsciiDoc). Includes are inlined. -->

## elasticsearch-service-tokens

Use the `elasticsearch-service-tokens` command to create, list, and delete file-based service account tokens.

### Synopsis

```shell
bin/elasticsearch-service-tokens
([create <service_account_principal> <token_name>]) |
([list] [<service_account_principal>]) |
([delete <service_account_principal> <token_name>])
```

### Description

**Note:** The recommended way to manage service tokens
is via the security-api-create-service-token API.
File based tokens are intended for use with orchestrators such as
{ece-ref}[Elastic Cloud Enterprise] and {eck-ref}[Elastic Cloud on Kubernetes]

This command creates a `service_tokens` file in the `$ES_HOME/config` directory
when you create the first service account token. This file does not exist by
default. Elasticsearch monitors this file for changes and dynamically reloads it.

This command only makes changes to the `service_tokens` file on the local node.
If the service token will be used to authenticate requests against multiple nodes
in the cluster then you must copy the `service_tokens` file to each node.

See service accounts for further information about the
behaviour of service accounts and the management of service tokens.

**Important:** To ensure that Elasticsearch can read the service account token information at
startup, run `elasticsearch-service-tokens` as the same user you use to run
Elasticsearch. Running this command as `root` or some other user updates the permissions
for the `service_tokens` file and prevents Elasticsearch from accessing it.

### Parameters

`create`::
Creates a service account token for the specified service account.
**Properties of `create`**
`<service_account_principal>`:::
(Required, string) Service account principal that takes the format of
`<namespace>/<service>`, where the `namespace` is a top-level grouping of
service accounts, and `service` is the name of the service. For example, `elastic/fleet-server`.
The service account principal must match a known service account.

`<token_name>`:::
(Required, string) An identifier for the token name.
Token names must be at least 1 and no more than 256 characters. They can contain
alphanumeric characters (`a-z`, `A-Z`, `0-9`), dashes (`-`), and underscores
(`_`), but cannot begin with an underscore.

**Note:** Token names must be unique in the context of the associated service
account.

`list`::
Lists all service account tokens defined in the `service_tokens` file. If you
specify a service account principal, the command lists only the tokens that
belong to the specified service account.
**Properties of `list`**
`<service_account_principal>`:::
(Optional, string) Service account principal that takes the format of
`<namespace>/<service>`, where the `namespace` is a top-level grouping of
service accounts, and `service` is the name of the service. For example, `elastic/fleet-server`.
The service account principal must match a known service account.

`delete`::
Deletes a service account token for the specified service account.
**Properties of `delete`**
`<service_account_principal>`:::
(Required, string) Service account principal that takes the format of
`<namespace>/<service>`, where the `namespace` is a top-level grouping of
service accounts, and `service` is the name of the service. For example, `elastic/fleet-server`.
The service account principal must match a known service account.

`<token_name>`:::
(Required, string) Name of an existing token.

### Examples

The following command creates a service account token named `my-token` for
the `elastic/fleet-server` service account.

```shell
bin/elasticsearch-service-tokens create elastic/fleet-server my-token
```

The output is a bearer token, which is a Base64 encoded string.

```shell
SERVICE_TOKEN elastic/fleet-server/my-token = AAEAAWVsYXN0aWM...vZmxlZXQtc2VydmVyL3Rva2VuMTo3TFdaSDZ
```

Use this bearer token to authenticate with your Elasticsearch cluster.

```shell
curl -H "Authorization: Bearer AAEAAWVsYXN0aWM...vZmxlZXQtc2VydmVyL3Rva2VuMTo3TFdaSDZ" http://localhost:9200/_cluster/health
```

**Note:** If your node has `xpack.security.http.ssl.enabled` set to `true`, then
you must specify `https` in the request URL.

The following command lists all service account tokens that are defined in the
`service_tokens` file.

```shell
bin/elasticsearch-service-tokens list
```

A list of all service account tokens displays in your terminal:

```txt
elastic/fleet-server/my-token
elastic/fleet-server/another-token
```

The following command deletes the `my-token` service account token for the
`elastic/fleet-server` service account:

```shell
bin/elasticsearch-service-tokens delete elastic/fleet-server my-token
```
