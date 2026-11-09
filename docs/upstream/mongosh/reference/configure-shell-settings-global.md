<!-- Converted from reference/configure-shell-settings-global.txt (reStructuredText). Includes are inlined. -->

# Configure Settings Using a Configuration File

You can specify `mongosh` settings in a global configuration file.
When you specify settings in a configuration file, those settings are
applied at startup. After you create a configuration file, the settings
in the file take effect the next time you start `mongosh`.

## Configuration File Format

The `mongosh` configuration file uses the YAML format. All options are
under the `mongosh` namespace.

### Example Configuration File

The following configuration file sets:

- `displayBatchSize` to 50
- `inspectDepth` to 20
- `redactHistory` to `remove-redact`

```yaml
mongosh:
  displayBatchSize: 50
  inspectDepth: 20
  redactHistory: "remove-redact"
```

## Configuration File Location

The file location where `mongosh` looks for the configuration file
depends on your operating system:

| Operating System | File Location |
|---|---|
| Windows | `mongosh.cfg`, in the same directory as the `mongosh.exe` binary. |
| macOS | `mongosh` looks for a configuration file in the following directories in the order they are listed: 1. `/usr/local/etc/mongosh.conf` #. `/opt/homebrew/etc/mongosh.conf` #. `/etc/mongosh.conf` Once `mongosh` reads a configuration file in one of these directories, any remaining directories in the list are not checked and configuration files in those directories are ignored. |
| Linux | `/etc/mongosh.conf` |

## Configurable Settings

You can specify the following `mongosh` settings in your configuration
file:

* - Key
  - Type
  - Default
  - Description

* - `browser`
  - string or boolean
  - System default browser
  - .. include:: /includes/browser-description.rst

    Set `browser` to `false` to disable opening browsers entirely.

* - `disableLogging`
  - boolean
  - `false`
  - Specifies whether MongoDB Shell writes log entries.

* - `disableSchemaSampling`
  - boolean
  - `false`
  - By default, MongoDB Shell samples your database schema to enable
    autocomplete suggestions.

    If you set this setting to `true`, MongoDB Shell does not sample
    your database schema and autocomplete behaves as if the
    collection is empty.

* - `displayBatchSize`
  - integer
  - 20
  - The number of items displayed per cursor iteration

* - `enableTelemetry`
  - boolean
  - `true`
  - Enables sending pseudo-anonymous tracking and diagnostic data to
    MongoDB during interactive and agentic sessions only.

* - `editor`
  - string
  - `null`
  - Designates an editor to use within the `mongosh`
    console. Overrides the `EDITOR` environment variable if set.

* - `forceDisableTelemetry`
  - boolean
  - `false`
  - Only available in the global configuration file. When true,
    users cannot enable telemetry manually.

* - `historyLength`
  - integer
  - 1000
  - The number of items to store in `mongosh` REPL's
    history file.

* - `inspectCompact`
  - integer or boolean
  - 3
  - The level of inner elements that `mongosh` outputs
    on a single line. Short array elements are also grouped together
    on a single line.

    If set to `false`, `mongosh` outputs each field
    on its own line.

* - `inspectDepth`
  - integer or Infinity
  - 6
  - The depth to which objects are printed. Setting `inspectDepth`
    to `Infinity` (the javascript object) prints all nested
    objects to their full depth. 

* - `logCompressionEnabled`
  - boolean
  - false
  - Specifies whether MongoDB Shell compresses log files. When this
    value is `true`, MongoDB Shell uses gzip to compress logs. See
    mongosh-log-compression.

* - `logLocation`
  - string
  - Depends on your operating system. See mdb-shell-view-logs.
  - Directory where MongoDB Shell writes log files. Specify an
    absolute filepath. See mongosh-log-location.

* - `logMaxFileCount`
  - integer or Infinity
  - 100
  - Maximum number of log files that the MongoDB Shell retains. After
    the MongoDB Shell reaches the maximum log file count, it starts
    deleting the oldest log files until the count is below the
    threshold. See mongosh-log-file-count.

* - `logRetentionDays`
  - integer or Infinity
  - 30
  - Number of days that MongoDB Shell log files are retained. If this
    value is set to `Infinity`, log files are not deleted based on
    age. To prevent log storage from growing too large, always
    specify at least one log retention criterion. See
    mongosh-logs-retention.

* - `logRetentionGB`
  - float or Infinity
  - Unset
  - Maximum amount of space in gigabytes used for MongoDB Shell logs.
    If the combined size of MongoDB Shell logs exceeds this value, log
    files are deleted starting with the oldest logs.

    If this value is set to `Infinity`, log files are not deleted
    based on storage size. To prevent log storage from growing too
    large, always specify at least one log retention criterion. See
    mongosh-logs-retention.

* - `oidcRedirectUri`
  - string
  - `http://localhost:27097/redirect`
  - .. include:: /includes/oidc-redirect-uri-description.rst

* - `oidcTrustedEndpoints`
  - array of strings
  - `[]` (empty array)
  - Specifies an array of trusted endpoint hostnames, including possible 
    wildcards, that are not Atlas or `localhost`. Access tokens are sent 
    to these endpoints. Only configure endpoints that you trust.

* - `redactHistory`
  - string
  - `remove`
  - Controls what information is recorded in the `mongosh` command history.
    You can access the `mongosh` command history via the up and down keys 
    or Ctrl+R while inside the shell.

    Must be one of the following values:

    - `keep`: Retain all history.
    - `remove`: Remove lines that contain sensitive commands from the history. 
      For example, `remove` removes calls to db.auth() or connect().
    - `remove-redact`: Remove lines that contain sensitive commands and redact 
      specific strings in other history lines, such as file paths, email addresses, and URLs. 

* - `showStackTraces`
  - boolean
  - `false`
  - Controls display of a stack trace along with error messages.

* - `snippetAutoload`
  - boolean
  - `true`
  - If `true`, automatically load installed
    snippets at startup.

* - `snippetIndexSourceURLs`
  - string
  - [MongoDB Repository](https://compass.mongodb.com/mongosh/snippets-index.bson.br)
  - A semicolon-separated list of URLs that link to a
    snippet registry.

* - `snippetRegistryURL`
  - string
  - [npm Registry](https://registry.npmjs.org)
  - The npm registry used by the `mongosh` npm client
    that installs snippet.

* - `updateURL`
  - string
  - `https://downloads.mongodb.com/compass/mongosh.json`
  - The URL that MongoDB Shell checks for available updates at startup.

    To disable update notifications and the associated outbound network
    request, set `updateURL` to an empty string.

## Behavior with config API

Settings specified with the config API:

- Override settings specified in the configuration file.

- Persist across restarts.

**Example:**

Consider the following configuration file that sets the
`inspectDepth` setting to `20`:

```yaml
mongosh:
  inspectDepth: 20
```

During your `mongosh` session you run the following command to set
`inspectDepth` to `10`:

```javascript
config.set( "inspectDepth", 10 )
```

The value of `inspectDepth` becomes `10`, and will remain `10`
even when `mongosh` is restarted.
