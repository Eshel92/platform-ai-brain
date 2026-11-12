<!-- Part 1 of 7 of reference/configuration-options.md (split because the page is big). -->

## Configuration File

You can configure `mongod` and `mongos` instances at
startup using a configuration file. The configuration file contains
settings that are equivalent to the `mongod` and
`mongos` command-line options. See conf-file-command-line-mapping.

Using a configuration file makes managing `mongod` and
`mongos` options easier, especially for large-scale
deployments. You can also add comments to the configuration file to
explain the server's settings.

- If you installed MongoDB with a package manager
  such as `yum` or `apt` on Linux or `brew` on macOS, or with the
  MSI installer on Windows, a default configuration file has been provided as part of your
  installation:

  | Platform | Method | Configuration File |
  |---|---|---|
  | Linux | `apt`, `yum`, or `zypper` Package Manager | `/etc/mongod.conf` |
  | macOS | `brew` Package Manager | `/usr/local/etc/mongod.conf` (on Intel processors), or `/opt/homebrew/etc/mongod.conf` (on [Apple Silicon processors](https://support.apple.com/en-us/HT211814)) |
  | Windows | MSI Installer | `<install directory>\bin\mongod.cfg` |

- If you installed MongoDB
  through a downloaded `TGZ` or `ZIP` file, you must create
  your own configuration file. The basic example
  configuration is a good place to start.

### File Format

MongoDB configuration files use the [YAML](http://www.yaml.org) format
[#yaml-json]_.

The following sample configuration file contains several `mongod`
settings that you may adapt to your local configuration:

**Note:**

YAML does not support tab characters for indentation: use spaces instead.

```yaml
systemLog:
   destination: file
   path: "/var/log/mongodb/mongod.log"
   logAppend: true
storage:
   journal:
      enabled: true
processManagement:
   fork: true
net:
   bindIp: 127.0.0.1
   port: 27017
setParameter:
   enableLocalhostAuthBypass: false
...
```

The Linux package init scripts included in the official MongoDB packages depend
on specific values for `systemLog.path`, `storage.dbPath`, and
`processManagement.fork`. If you modify these settings in the default
configuration file, `mongod` may not start.

#### Externally Sourced Values

**Note:**

MongoDB supports using 
expansion directives in configuration 
files to load externally sourced values. Expansion directives can
load values for specific 
configuration file options *or* load the 
entire configuration file.

The following expansion directives are available:

| Expansion Directive | Description |
|---|---|
| `__rest` | Allows users to specify a `REST` endpoint as the external source for configuration file options *or* the full configuration file. If the configuration file includes the `__rest` expansion, on Linux/macOS, the read access to the configuration file must be limited to the user running the `mongod` / `mongos` process only. |
| `__exec` | Allows users to specify a shell or terminal command as the external source for configuration file options *or* the full configuration file. If the configuration file includes the `__exec` expansion, on Linux/macOS, the write access to the configuration file must be limited to the user running the `mongod` / `mongos` process only. |

For complete documentation, see externally-sourced-values.

### Use the Configuration File

To configure `mongod` or `mongos` using a config file,
specify the config file with the `--config` option or the
`-f` option, as in the following examples:

For example, the following uses `mongod --config
<configuration file>` `mongos --config
<configuration file>`:

```bash
mongod --config /etc/mongod.conf

mongos --config /etc/mongos.conf
```

You can also use the `-f` alias to specify the configuration
file, as in the following:

```bash
mongod -f /etc/mongod.conf

mongos -f /etc/mongos.conf
```

If you installed from a package and have started MongoDB using your
system's init script, you are already using a configuration
file.

#### Expansion Directives and `--configExpand`

If you are using expansion directives
in the configuration file, you must include the
`--configExpand` option when starting
the `mongod` or `mongos`. For example:

```bash
mongod --config /etc/mongod.conf  --configExpand "rest,exec"
mongos --config /etc/mongos.conf  --configExpand "rest,exec"
```

If the configuration file includes an expansion directive and you start
the `mongod` / `mongos` without specifying
that directive in the `--configExpand`
option, the `mongod` / `mongos` fails to start.

For complete documentation, see externally-sourced-values.


## Core Options
