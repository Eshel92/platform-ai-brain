<!-- Converted from commands/syskeygen.asciidoc (AsciiDoc). Includes are inlined. -->

## elasticsearch-syskeygen

The `elasticsearch-syskeygen` command creates a system key file in the
elasticsearch config directory.

### Synopsis

```shell
bin/elasticsearch-syskeygen
[-E <KeyValuePair>] [-h, --help]
([-s, --silent] | [-v, --verbose])
```

### Description

The command generates a `system_key` file, which you can use to symmetrically
encrypt sensitive data. For example, you can use this key to prevent Watcher
from returning and storing information that contains clear text credentials. See
encrypting-data. 

**Important:** The system key is a symmetric key, so the same key must be used on
every node in the cluster.

### Parameters

`-E <KeyValuePair>`:: Configures a setting. For example, if you have a custom
installation of Elasticsearch, you can use this parameter to specify the `ES_PATH_CONF`
environment variable.

`-h, --help`:: Returns all of the command parameters.

`-s, --silent`:: Shows minimal output.

`-v, --verbose`:: Shows verbose output.

### Examples

The following command generates a `system_key` file in the
default `$ES_HOME/config` directory:

```sh
bin/elasticsearch-syskeygen
```
