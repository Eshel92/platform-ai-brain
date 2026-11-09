<!-- Converted from reference/configure-shell-settings-api.txt (reStructuredText). Includes are inlined. -->

# Configure Settings Using the API

The `config` API provides methods to examine and update the
`mongosh` configuration. Updates made using the `config`
API persist between sessions.

**Note:**

The `config` API can be used within the `mongosh`
command line interface. It has no effect in the
`embedded Compass shell`.

## Syntax

Print the current `mongosh` configuration:

```javascript
config 
```

Return the current value for `<property>`:

```javascript
config.get( "<property>" )
```

Change the current setting of `<property>` to `<value>`:

```javascript
config.set( "<property>", <value> )
```

Reset a `<property>` to the default value:

```javascript
config.reset( "<property>" )
```

### Supported property parameters

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

## Behavior

### Remove or Redact Sensitive Information From History

`mongosh` makes "best-effort" attempts to match patterns
that normally correspond to certain kinds of sensitive information.

There are patterns that match:

- Certificates and keys
- Email addresses
- Generic user directories
- HTTP(s) URLs
- IP addresses
- MongoDB connection strings

Certain operations, such as `connect()`, are considered
inherently sensitive. If `redactHistory` is set to `remove` or
`remove-redact`, lines with these operations will be removed from the
command line history.

Other operations, like `find()`, sometimes have
sensitive information like email addresses. The
shell history will retain these
lines as entered unless `redactHistory` is set to `remove-redact`.

### Behavior with Configuration File

Settings specified with the `config` API:

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

## Examples

### Update Number of Items Returned by a Cursor

Consider viewing a collection with a number of large documents. You can
update the `batchSize` to limit the number of items returned by a
cursor.

```javascript
config.set("displayBatchSize", 3) 
```

Future `db.collection.find()` operations will only return 3 documents
per cursor iteration.

### Turn On Stack Traces

Enable stack traces to see more detailed error reporting. 

```javascript
config.set("showStackTraces", true)
```

The output differs like this: 

```javascript
// showStackTraces set to 'false'
Enterprise> db.orders.find( {}, { $thisWontWork: 1 } )
MongoError: FieldPath field names may not start with '$'.

// showStackTraces set to 'true'
Enterprise> db.orders.find( {}, { $thisWontWork: 1 } )
Uncaught:
MongoError: FieldPath field names may not start with '$'.
    at MessageStream.messageHandler (/usr/bin/mongosh:58878:20)
    at MessageStream.emit (events.js:315:20)
    at MessageStream.EventEmitter.emit (domain.js:548:15)
    at processIncomingData (/usr/bin/mongosh:57954:12)
    at MessageStream._write (/usr/bin/mongosh:57850:5)
    at writeOrBuffer (_stream_writable.js:352:12)
    at MessageStream.Writable.write (_stream_writable.js:303:10)
    at Socket.ondata (_stream_readable.js:719:22)
    at Socket.emit (events.js:315:20)
    at Socket.EventEmitter.emit (domain.js:548:15)
```

### Call config API from outside mongosh

You can call the `config` API from the command line using
`--eval` with `mongosh`. In this case the
`--nodb` option means `mongosh` will update
without connecting to a MongoDB database.

**Important:**

You must use different quotation marks for the `--eval`
expression and the `config` property. That is, single quotes for
one and double quotes for the other. 

```
mongosh --nodb --eval 'config.set("enableTelemetry", true)'
```

`mongosh` returns additional information along with the
result of the API call.

```
Current Mongosh Log ID:	609583b730e14918fa0d363f
Using MongoDB:		undefined
Using Mongosh Beta:	0.12.1

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/

Setting "enableTelemetry" has been changed
```

### Redact Sensitive Information

Compare the recalled history when `redactHistory` is set to
`remove-redact` or `remove`. 

Set `redactHistory` to `remove-redact` mode and enter a query
containing an email address. 

```javascript
config.set( "redactHistory", "remove-redact" )
db.contacts.find( {"email": "customer@clients.com" } )
```

When you press the `up arrow` to replay the last command the email
address is redacted. 

```javascript
db.contacts.find( {"email": "<email>" } )  // Redacted
```

Set `redactHistory` to `remove` mode and enter a query containing
an email address. 

```javascript
config.set( "redactHistory", "remove" )
db.contacts.find( {"email": "customer@clients.com" } )
```

When you press the `up arrow` to replay the last command the email
address is present. 

```javascript
db.contacts.find( {"email": "customer@clients.com" } )
```

The shell history reflects the
changes. (Note that this stores the most recent input first.)

```javascript
db.contacts.find( {"email": "customer@clients.com" } )
config.set( "redactHistory", "remove" )
db.contacts.find( {"email": "<email>" } )
config.set( "redactHistory", "remove-redact" )
```

### Reset a Configuration Setting to the Default Value

If you modified a configuration setting and want to reset it to the
default value, use `config.reset( "<property>" )`.

#. Change the value of the `historyLength` setting to `2000`:

   ```javascript
   config.set("historyLength", 2000)
   ```

#. Verify the updated value for `historyLength`:

   ```javascript
   config.get("historyLength")
   ```

#. Reset the `historyLength` setting to the default value of `1000`:

   ```javascript
   config.reset("historyLength")
   ```

#. Verify the updated value for `historyLength`:

   ```javascript
   config.get("historyLength")
   ```
