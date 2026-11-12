<!-- Converted from user/commands/encryption-keys/index.asciidoc (AsciiDoc). Includes are inlined. -->

### kibana-encryption-keys

The `kibana-encryption-keys` command helps you generate encryption keys that Kibana uses
to protect sensitive information.

Kibana uses encryption keys in several areas, ranging from encrypting data
in Kibana associated indices to storing session information. By defining these
encryption keys in your configuration, you'll ensure consistent operations
across restarts.

### Usage

```shell
bin/kibana-encryption-keys [command] [options]
```

### Commands

`generate`:: Generate encryption keys.
Unless interactive mode (`-i`) is used, the generated encryption keys will be output to your console only.
From here, you should manually copy the keys into either `kibana.yml` or where else you're configurating Kibana.
`-i, --interactive`::: Prompts you for which encryption keys to set and optionally where to save a sample configuration file.
`-q, --quiet`::: Outputs the config options/encryption keys only (without helper information).
`-f, --force`::: Generates new keys for all settings. By default, only un-configured encryption keys will be generated.
`-h, --help`::: Shows help information.

### Examples

```shell
bin/kibana-encryption-keys generate
```
