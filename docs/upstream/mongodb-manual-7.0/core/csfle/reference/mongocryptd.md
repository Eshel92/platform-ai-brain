<!-- Converted from core/csfle/reference/mongocryptd.txt (reStructuredText). Includes are inlined. -->

# Install and Configure mongocryptd for CSFLE

**`mongocryptd`**

## Overview

**Note:** Enterprise Feature

The automatic feature of field level encryption is only supported
in MongoDB Enterprise 6.0 or later, and MongoDB Atlas 6.0 or later
clusters. 

`mongocryptd` is installed with [MongoDB Enterprise Server](https://www.mongodb.com/try/download/enterprise).

When you create a CSFLE-enabled MongoDB client, the `mongocryptd`
process starts automatically by default.

The `mongocryptd` process:

- Uses the specified automatic encryption rules to mark fields in 
  read and write operations for encryption.

- Prevents unsupported operations from executing on encrypted 
  fields.

- Parses the encryption schema specified for the database connection.
  Automatic encryption rules use a strict subset of JSON schema syntax.
  If the rules contain invalid automatic encryption syntax or any
  `schema validation` syntax, `mongocryptd`
  returns an error. 

`mongocryptd` only performs the previous functions, and doesn't perform any of the following:

- `mongocryptd` doesn't perform encryption or decryption
- `mongocryptd` doesn't access any encryption key material
- `mongocryptd` doesn't listen over the network

To perform client-side field level encryption and automatic decryption, Drivers use the Apache-licensed [libmongocrypt](https://github.com/mongodb/libmongocrypt) library

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

If the driver has access to the `mongocryptd` process, it spawns the
process by default. Your application must have write permissions on the 
working directory to create the `mongocryptd.pid` file.

**Note:** mongocryptd Port In Use

If a `mongocryptd` process is already running on the port specified
by the driver, the driver may log a warning and continue without
spawning a new process. Any settings specified by the driver only
apply once the existing process exits and a new encrypted client
attempts to connect.

Configure how the driver starts `mongocryptd` through the 
following parameters:

| Name | Description |
|---|---|
| port | \| The port from which `mongocryptd` listens for messages. \| **Default**: `27020` |
| idleShutdownTimeoutSecs | \| Number of idle seconds the `mongocryptd` process waits before exiting. \| **Default**: `60` |
| mongocryptdURI | \| The URI on which to run the `mongocryptd` process. \| **Default**: `"mongodb://localhost:27020"` |
| mongocryptdBypassSpawn | \| When `true`, prevents the driver from automatically spawning `mongocryptd`. \| **Default**: `false` |
| mongocryptdSpawnPath | \| The full path to `mongocryptd`. \| **Default**: Defaults to empty string and spawns from the system path. |

**Important:** Start on Boot

If possible, start `mongocryptd` on boot, rather than launching it
on demand.

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

In the NodeJS driver, the `mongocryptdURI` must match the listening port.

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
