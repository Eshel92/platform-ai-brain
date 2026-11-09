<!-- Converted from core/csfle/reference/mongocryptd.txt (reStructuredText). Includes are inlined. -->

# Install and Configure mongocryptd for CSFLE

**`mongocryptd`**

## Overview

**Note:** Enterprise Feature

The automatic feature of field level encryption is only available
in MongoDB Enterprise 4.2 or later, and MongoDB Atlas 4.2 or later
clusters. 

`mongocryptd` is installed with [MongoDB Enterprise Server (version 4.2 and later)](https://www.mongodb.com/try/download/enterprise).

When you create a CSFLE-enabled MongoDB client, the `mongocryptd`
process is automatically started by default and handles the following
responsibilities:

- Uses the specified automatic encryption rules to mark fields in 
  read and write operations for encryption.

- Prevents unsupported operations from being executed on encrypted 
  fields.

- Parses the encryption schema
  specified to the database connection. Automatic encryption rules use a
  strict subset of JSON schema syntax. If the automatic encryption rules 
  contain invalid automatic encryption syntax *or* any `document validation` syntax, `mongocryptd` returns an error. 

`mongocryptd` is only responsible for the above functions, and does
not perform any of the following:

- `mongocryptd` *does not* perform encryption or decryption itself
- `mongocryptd` *does not* access any encryption key material
- `mongocryptd` *does not* listen over the network

Drivers compatible with MongoDB 4.2 and later use the
Apache-licensed [libmongocrypt](https://github.com/mongodb/libmongocrypt) library for performing
client-side field level encryption and automatic decryption.

The official MongoDB drivers, `mongosh`, and the legacy 
`mongo` shell require access to the `mongocryptd` process on the 
client host machine. These clients search for the `mongocryptd` process in the 
system PATH by default.

## Installation

For supported Linux Operating Systems, install the Server package by following the
install on Linux tutorial
, follow the documented installation instructions and install the 
`mongodb-enterprise` server package. Alternatively, specify 
`mongodb-enterprise-cryptd` instead to install only the 
`mongocryptd` binary. The package manager installs
the binaries to a location in the system PATH (e.g. `/usr/bin/`)

For OSX, install the Server package by following the
install on MacOS tutorial.
The package manager installs binaries to a location in the system
PATH.

For Windows, install the Server package by following the
install on Windows tutorial.
You must add the `mongocryptd` package to your system PATH after
installation. Defer to documented best practices for your Windows
installation for instructions on adding the `mongocryptd` binary to
the system PATH.

For installations via an official tarball or ZIP archive,
follow the documented best practices for your operating system to add
the `mongocryptd` binary to your system PATH.

## Configuration

If the 4.2+ compatible driver has access to the `mongocryptd` process,
by default the driver manages the spawning of the `mongocryptd`
process.

**Note:** mongocryptd Port In Use

If a `mongocryptd` process is already running on the port specified
by the driver, the driver may log a warning and continue to operate
without spawning a new process. Any settings specified by the driver
only apply once the existing process exits and a new encrypted client
attempts to connect.

You can configure how your driver starts `mongocryptd` through the 
following parameters:

| Name | Description |
|---|---|
| port | \| The port from which `mongocryptd` listens for messages. \| **Default**: `27020` |
| idleShutdownTimeoutSecs | \| Number of idle seconds in which the `mongocryptd` process should wait before exiting. \| **Default**: `60` |
| mongocryptdURI | \| The URI from which to run a `mongocryptd` process. \| **Default**: `"mongodb://localhost:27020"` |
| mongocryptdBypassSpawn | \| Set to `true` to prevent the driver from automatically spawning `mongocryptd`. \| **Default**: `false` |
| monogocryptdSpawnPath | \| The full path to `mongocryptd`. \| **Default**: Defaults to empty string and spawns from the system path. |

**Important:** Start on Boot

If possible, we recommend that `mongocryptd` be started on boot,
rather than launched on demand.

### Examples

To view examples of how to configure your `mongocryptd` 
process, click the tab corresponding to the driver you are using in 
your application:

**java-sync:**

The following code-snippet sets the listening port configuration
of `mongocryptd`:

```java
List<String> spawnArgs = new ArrayList<String>();
spawnArgs.add("--port=30000");

Map<String, Object> extraOpts = new HashMap<String, Object>();
extraOpts.put("mongocryptdSpawnArgs", spawnArgs);

AutoEncryptionSettings autoEncryptionSettings = AutoEncryptionSettings.builder()
    ...
    .extraOptions(extraOpts);
```

The following code-snippet sets the default timeout configuration
of `mongocryptd`:

```java
List<String> spawnArgs = new ArrayList<String>();
spawnArgs.add("--idleShutdownTimeoutSecs")
    .add("60");

Map<String, Object> extraOpts = new HashMap<String, Object>();
extraOpts.put("mongocryptdSpawnArgs", spawnArgs);

AutoEncryptionSettings autoEncryptionSettings = AutoEncryptionSettings.builder()
    ...
    .extraOptions(extraOpts);
```

**nodejs:**

The following code-snippet sets the listening port configuration
of `mongocryptd`:

```javascript
autoEncryption: {
  ...
  extraOptions: {
    mongocryptdSpawnArgs: ["--port", "30000"],
    mongocryptdURI: 'mongodb://localhost:30000',
  }
```

**Note:**

In the current version (3.3.4) of the NodeJS driver, you
must specify the `mongocryptdURI` to match the listening
port.

The following code-snippet sets the default timeout configuration
of `mongocryptd`:

```javascript
autoEncryption: {
  ...
  extraOptions: {
    mongocryptdSpawnArgs: ["--idleShutdownTimeoutSecs", "75"]
  }
```

**python:**

The following code-snippet sets the listening port configuration
of `mongocryptd`:

```python
auto_encryption_opts = AutoEncryptionOpts(mongocryptd_spawn_args=['--port=30000'])
```

The following code-snippet sets the default timeout configuration
of `mongocryptd`:

```python
auto_encryption_opts = AutoEncryptionOpts(mongocryptd_spawn_args=['--idleShutdownTimeoutSecs=75'])
```

**csharp:**

The following code-snippet sets the listening port configuration
of `mongocryptd`:

```csharp
var extraOptions = new Dictionary<string, object>()
{
    { "mongocryptdSpawnArgs", new [] { "--port=30000" } },
};
autoEncryptionOptions.With(extraOptions: extraOptions);
```

The following code-snippet sets the default timeout configuration
of `mongocryptd`:

```csharp
var extraOptions = new Dictionary<string, object>()
{
    { "idleShutdownTimeoutSecs", 60 },
};
autoEncryptionOptions.With(extraOptions: extraOptions);
```

**go:**

The following code-snippet sets the listening port configuration
of `mongocryptd`:

```go
extraOptions := map[string]interface{}{
    "mongocryptdSpawnArgs": []string{
        "--port=30000",
    },
}
```

The following code-snippet sets the default timeout configuration
of `mongocryptd`:

```go
extraOptions := map[string]interface{}{
    "mongocryptdSpawnArgs": []string{
        "--idleShutdownTimeoutSecs=75",
    },
}
```
