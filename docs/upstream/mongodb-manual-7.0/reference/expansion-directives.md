<!-- Converted from reference/expansion-directives.txt (reStructuredText). Includes are inlined. -->

# External Configuration Values for Self-Managed MongoDB

MongoDB supports using expansion directives in configuration files
to load externally sourced values. Expansion directives can
load values for specific 
configuration file options *or* load the 
entire configuration file. Expansion directives help obscure
confidential information like security certificates and passwords.

```yaml
storage: 
  dbPath: "/var/lib/mongo"
systemLog:
  destination: file
  path: "/var/log/mongodb/mongod.log"
net:
  bindIp:
    __exec: "python /home/user/getIPAddresses.py"
    type: "string"
    trim: "whitespace"
    digest: 85fed8997aac3f558e779625f2e51b4d142dff11184308dc6aca06cff26ee9ad
    digest_key: 68656c6c30303030307365637265746d796f6c64667269656e64
  tls:
    mode: requireTLS
    certificateKeyFile: "/etc/tls/mongod.pem"
    certificateKeyFilePassword:
      __rest: "https://myrestserver.example.net/api/config/myCertKeyFilePassword"
      type: "string"
      digest: b08519162ba332985ac18204851949611ef73835ec99067b85723e10113f5c26
      digest_key: 6d795365637265744b65795374756666
```

- .. include:: /includes/extracts/4.2-changes-expansion-configuration-file-permission-rest.rst

- .. include:: /includes/extracts/4.2-changes-expansion-configuration-file-permission-exec.rst

To use expansion directives, you must specify the
`--configExpand` command-line option
with the complete list of expansion directives used:

```bash
mongod --config "/path/to/config/mongod.conf" --configExpand "rest,exec"
```

If you omit the 
`--configExpand` option *or* if
you do not specify the complete list of expansion directives used in
the configuration file, the `mongod`/`mongos` returns
an error and terminates. You can only specify the
`--configExpand` option on the
command line.

## Use the `__rest` Expansion Directive

The `__rest` expansion directive loads configuration
file values from a `REST` endpoint. `__rest` supports loading
specific values  in the configuration file *or* loading the entire
configuration file.

tabs:

  - id: single-val-rest
    name: Specific Value
    content: |

      The following configuration file uses the
      `__rest` expansion directive to load the
      setting `net.tls.certificateKeyFilePassword` value from an
      external `REST` endpoint:

      ```yaml
      storage:
        dbPath: "/var/lib/mongo"
      systemLog:
        destination: file
        path: "/var/log/mongodb/mongod.log"
      net:
        bindIp: 192.51.100.24,127.0.0.1
        tls:
          mode: requireTLS
          certificateKeyFile: "/etc/tls/mongod.pem"
          certificateKeyFilePassword:
            __rest: "https://myrestserver.example.net/api/config/myCertKeyFilePassword"
            type: "string"
      ```

      File Permission

        If the configuration file includes the `__rest`
        expansion, on Linux/macOS, the read access to the configuration file must be limited
        to the user running the `mongod` / `mongos`
        process only.

      Expansion Parsing
         To parse the `__rest` blocks, start the `mongod`/`mongos` with
         the `--configExpand "rest"`
         option.

         The `mongod`/`mongos` issues a `GET` request against specified
         URL. If successful, the `mongod`/`mongos` replaces the value of
         `certificateKeyFilePassword` with the returned value. If
         the URL fails to resolve or if the `REST` endpoint
         returns an invalid value, the `mongod`/`mongos` throws an error and
         terminates.

  - id: full-file-rest
    name: Full Configuration File
    content: |

      The following configuration file uses the
      `__rest` expansion directive to load the
      configuration file from an external `REST` endpoint. The
      expansion directive and its options **must** be the only values
      specified in the configuration file.

      ```yaml
      __rest: "https://myrestserver.example.net/api/config/fullConfig"
      type: "yaml"
      ```

      File Permission

        If the configuration file includes the `__rest`
        expansion, on Linux/macOS, the read access to the configuration file must be limited
        to the user running the `mongod` / `mongos`
        process only.

      Expansion Parsing
         To parse the `__rest` blocks, start the `mongod`/`mongos` with
         the `--configExpand "rest"`
         option.

         The `mongod`/`mongos` issues a `GET` request against the
         specified URL. If successful, the `mongod`/`mongos` parses the
         returned configuration `yaml` file and uses it during
         startup. If the URL fails to resolve or return a properly
         formatted `yaml` file, the `mongod`/`mongos` throws an error and
         terminates.

**Important:**

The value returned by the specified `REST` endpoint
**cannot** include any additional expansion directives. The
`mongod`/`mongos` does **not** perform additional
processing on the returned data and will terminate with an
error code if the returned data includes additional
expansion directives.

## Use the `__exec` Expansion Directive

The `__exec` expansion directive loads configuration
file values from a shell or terminal command. `__exec` supports
loading specific values in the configuration file *or* loading the
entire configuration file.

tabs:

  - id: single-val-yaml
    name: Specific Value
    content: |

      The following example configuration file uses the
      `__exec` expansion directive to to load the
      setting `net.tls.certificateKeyFilePassword` value from the output
      of a shell or terminal command:

      ```yaml
      storage:
        dbPath: "/var/lib/mongo"
      systemLog:
        destination: file
        path: "/var/log/mongodb/mongod.log"
      net:
        bindIp: 192.51.100.24,127.0.0.1
        tls:
          mode: requireTLS
          certificateKeyFile: "/etc/tls/mongod.pem"
          certificateKeyFilePassword:
            __exec: "python /home/myUserName/getPEMPassword.py"
            type: "string"
      ```

      File Permission
        If the configuration file includes the `__exec`
        expansion, on Linux/macOS, the write access to the configuration file must be
        limited to the user running the
        `mongod` / `mongos` process only.

      Expansion Parsing
         To parse the `__exec` blocks, start the `mongod`/`mongos` with
         the `--configExpand "exec"`
         option.

         The `mongod`/`mongos` attempts to execute the specified operation.
         If the command executes successfully, the `mongod`/`mongos`
         replaces the value of `certificateKeyFilePassword` with
         the returned value. If the command fails or returns an
         invalid value for the configuration file setting, the
         `mongod`/`mongos` throws an error and terminates.

  - id: full-file-yaml
    name: Full Configuration File
    content: |

      The following example configuration file uses the
      `__exec` expansion directive to load the
      configuration file from the output of a shell or terminal
      command. The `__exec` expansion directive 
      and its options **must** be the only values specified in the 
      configuration file.  

      ```yaml
      __exec: "python /home/myUserName/getFullConfig.py"
      type: "yaml"
      ```

      File Permission
        If the configuration file includes the `__exec`
        expansion, on Linux/macOS, the write access to the configuration file must be
        limited to the user running the
        `mongod` / `mongos` process only.

      Expansion Parsing
         To parse the `__exec` blocks, start the `mongod`/`mongos` with
         the `--configExpand "rest"`
         option.

         If the command executes successfully, the `mongod`/`mongos` parses
         the returned configuration `yaml` file and uses it during
         startup. If the command fails or returns an invalid
         `yaml` file, the `mongod`/`mongos` throws an error and terminates.

**Important:**

The data returned by executing the specified  `__exec`
string **cannot** include any additional expansion
directives. The `mongod`/`mongos` does **not**
perform additional processing on the returned data and
will terminate with an error code if the returned data
includes additional expansion directives.

## Expansion Directives Reference

**`__rest`**

The `__rest` expansion directive loads configuration
file values from a `REST` endpoint. `__rest`
supports loading specific values in the configuration file *or*
loading the entire configuration file. The `mongod`/`mongos` then starts
using the externally sourced values as part of its configuration.

The `__rest` expansion directive has the following
syntax:

- To specify a `REST` endpoint for a specific configuration file
  setting or settings:

  ```yaml
  <some configuration file setting>:
    __rest: "<string>"
    type: "string"
    trim: "none|whitespace"
    digest: "<string>"
    digest_key: "<string>"
  ```

- To specify a `REST` endpoint for the entire configuration file: 

  ```yaml
  __rest: "<string>"
  type: "yaml"
  trim: "none|whitespace"
  ```

  If specifying the entire configuration file via `REST` endpoint,
  the expansion directive and its options **must** be the only values
  specified in the configuration file.

`__rest` takes the following fields:

* - Field
  - Type
  - Description

* - __rest
  - string
  - .. _expansion-rest:

    *Required* The URL against which the `mongod`/`mongos`
    issues a `GET` request
    to retrieve the externally sourced value.

    For non-localhost `REST` endpoints (e.g. a `REST` endpoint
    hosted on a remote server), `__rest`
    requires encrypted (`https://`) URLs where both the host
    machine and the remote server support TLS 1.1 or later.

    If the `REST` endpoint specified in the URL requires
    authentication, encode credentials into the URL with the
    standard  
    [RFC 3986 User Information](https://tools.ietf.org/html/rfc3986#section-3.2.1)
    format.

    For localhost `REST` endpoints (e.g. a `REST` endpoint
    listening on the host machine), `__rest` 
    allows unencrypted (`http://`) URLs.

    IMPORTANT: The value returned by the specified `REST` endpoint
    **cannot** include any additional expansion directives. The
    `mongod`/`mongos` does **not** perform additional
    processing on the returned data and will terminate with an
    error code if the returned data includes additional
    expansion directives.

* - `type`
  - string
  - *Optional* Controls how `__rest` 
    parses the returned value from the specified URL.

    Possible values are:

    - `string` (*Default*) 

      Directs `__rest` to parse the returned data
      as a literal string. If specifying `string`, the entire
      `__rest` block and supporting options must
      be nested under the field for which you are loading
      externally sourced values.

    - `yaml`

      Directs `__rest` to parse the returned data
      as a `yaml` formatted file. If specifying `yaml`, the
      `__rest` block must be the only content in
      the configuration file. The `mongod`/`mongos` replaces the
      configuration file contents with the `yaml` retrieved from
      the REST resource.

* - `trim`
  - string
  - *Optional* Specify `whitespace` to direct 
    `__rest` 
    to trim any leading or trailing whitespace, specifically 
    occurrences of
    `" "`, `"\r"`, `"\n"`, `"\t"`, `"\v"`, and
    `"\f"`. Defaults to `none`, or no trimming. 

* - digest
  - string

  - .. _expansion-rest-digest:

    *Optional*. The HMAC-SHA256 output of the expansion result,
    calculated as `HMAC-SHA256(digest_key, message)`, where
    `message` is the value of the configuration setting to be
    retrieved.

    If specified, you must also specify the digest_key.

* - digest_key
  - string

  - .. _expansion-rest-digest-key:

    *Optional*. The 64-character hexadecimal string
    representation of the 32-byte key used to calculate the
    HMAC-SHA256 digest of the
    expansion result.

    If specified, you must also specify the digest.

    For example, assume the `certificateKeyFilePassword` is
    "superSecret123". To retrieve this password by using a REST request
    or exec service call, you must generate a digest key and use it to
    calculate the digest of your password.

    Run the following code in your terminal to generate a 32-byte digest
    key:

    ```bash
    openssl rand -hex 32
    ```

    Output:

    ```none
    f38d0d5adfcf1a0575f9fa9051c70a2f88b1bb7562513c9efd7686e9c21ad304
    ```

    After you generate a digest key, you can use it to calculate the
    digest of your password:

    ```bash
    echo -ne "superSecret123" | openssl dgst -sha256 -mac hmac -macopt hexkey:f38d0d5adfcf1a0575f9fa9051c70a2f88b1bb7562513c9efd7686e9c21ad304
    ```

    Output:

    ```none
    8ca2f57caef0bb23b76e45b3fd1e899b7e306b8ba93f406a56d8969846ca9122
    ```

**Note:**

- .. include:: /includes/extracts/4.2-changes-expansion-configuration-file-permission-rest.rst

- To enable parsing of the `__rest` expansion directive, start
  the `mongod`/`mongos` with the `--configExpand "rest"` option.

For examples, see expansion-directive-rest.

**`__exec`**

The `__exec` expansion directive loads configuration
file values from the output of a shell or terminal command.
`__exec` supports loading specific values in the
configuration file *or* loading the entire configuration file. The
`mongod`/`mongos` then starts using the externally sourced values as part of
its configuration.

The `__exec` expansion directive has the following
syntax:

- To specify a shell or terminal command for a specific configuration
  file
  setting or settings:

  ```yaml
  <some configuration file setting>:
    __exec: "<string>"
    type: "string"
    trim: "none|whitespace"
  ```

- To specify a  a shell or terminal command for the entire 
  configuration file: 

  ```yaml
  __exec: "<string>"
  type: "yaml"
  trim: "none|whitespace"
  ```

  If specifying the entire configuration file via a terminal or shell
  command, the expansion directive and its options **must** be the
  only values specified in the configuration file.

`__exec` takes the following fields:

* - Field
  - Type
  - Description

* - `__exec`
  - string
  - *Required* The string which the `mongod`/`mongos` executes on the 
    terminal or shell to retrieve the externally sourced value. 

    On Linux and OSX hosts, execution is handled via
    POSIX `popen()`. On Windows hosts, execution is handled via
    the process control API. `__exec` opens a read-only
    pipe as the same user that started the `mongod` or
    `mongos`. 

    IMPORTANT: The data returned by executing the specified 
    command **cannot** include any additional expansion
    directives. The `mongod`/`mongos` does **not**
    perform additional processing on the returned data and
    will terminate with an error code if the returned data
    includes additional expansion directives.

* - `type`
  - string
  - *Optional* Controls how `__exec` 
    parses the value returned by the executed command.

    Possible values are:

    - `string` (*Default* )

      Directs `__exec` to parse the returned data
      as a literal string. If specifying `string`, the entire
      `__exec` block and supporting options must
      be nested under the field for which you are loading
      externally sourced values.

    - `yaml`

      Directs `__exec` to parse the returned data
      as a `yaml` formatted file. If specifying `yaml`, the
      `__exec` block must be the only content in
      the configuration file. The `mongod`/`mongos` replaces the
      configuration file contents with the `yaml` retrieved from
      the executed command.

* - `trim`
  - string
  - *Optional* Specify `whitespace` to direct 
    `__exec` 
    to trim any leading or trailing whitespace, specifically 
    occurrences of
    `" "`, `"\r"`, `"\n"`, `"\t"`, `"\v"`, and
    `"\f"`. Defaults to `none`, or no trimming. 

* - digest
  - string

  - .. _expansion-exec-digest:

    *Optional*. The HMAC-SHA256 output of the expansion result,
    calculated as `HMAC-SHA256(digest_key, message)`, where
    `message` is the value of the configuration setting to be
    retrieved.

    If specified, you must also specify the digest_key

* - digest_key
  - string

  - .. _expansion-exec-digest-key:

    *Optional*. The 64-character hexadecimal string
    representation of the 32-byte key used to calculate the
    HMAC-SHA256 digest of the
    expansion result.

    If specified, you must also specify the digest

    For example, assume the `certificateKeyFilePassword` is
    "superSecret123". To retrieve this password by using a REST request
    or exec service call, you must generate a digest key and use it to
    calculate the digest of your password.

    Run the following code in your terminal to generate a 32-byte digest
    key:

    ```bash
    openssl rand -hex 32
    ```

    Output:

    ```none
    f38d0d5adfcf1a0575f9fa9051c70a2f88b1bb7562513c9efd7686e9c21ad304
    ```

    After you generate a digest key, you can use it to calculate the
    digest of your password:

    ```bash
    echo -ne "superSecret123" | openssl dgst -sha256 -mac hmac -macopt hexkey:f38d0d5adfcf1a0575f9fa9051c70a2f88b1bb7562513c9efd7686e9c21ad304
    ```

    Output:

    ```none
    8ca2f57caef0bb23b76e45b3fd1e899b7e306b8ba93f406a56d8969846ca9122
    ```

**Note:**

- .. include:: /includes/extracts/4.2-changes-expansion-configuration-file-permission-exec.rst

- To enable parsing of the `__exec` expansion directives, start
  the `mongod`/`mongos` with the `--configExpand "exec"` option.

For examples, see expansion-directive-exec.

## Output the Configuration File with Resolved Expansion Directive Values

You can test the final output of a configuration file that specifies one
or more expansion directives by starting the `mongod`/`mongos` with the
`--outputConfig` option. A `mongod`/`mongos`
started with `--outputConfig` outputs
the resolved YAML configuration document to `stdout` and halts. If any
expansion directive specified in the configuration file returns
additional expansion directives, the `mongod`/`mongos` throws an error and
terminates.

**Warning:**

The `--outputConfig` option returns
the resolved values for any field using an expansion directive. This
includes any private or sensitive information previously obscured by
using an external source for the configuration option.

For example, the following configuration file 
`mongod.conf` contains a `__rest` expansion 
directive:

```yaml
storage:
  dbPath: "/var/lib/mongo"
systemLog:
  destination: file
  path: "/var/log/mongodb/mongod.log"
net:
  port:
    __rest: "https://mongoconf.example.net:8080/record/1"
    type: string
```

The string recorded at the specified URL is `20128`

If the configuration file includes the `__rest`
expansion, on Linux/macOS, the read access to the configuration file must be limited
to the user running the `mongod` / `mongos`
process only.

Start the `mongod` with the
`--configExpand "rest"` and
`--outputConfig` options:

```yaml
mongod -f mongod.conf --configExpand rest --outputConfig
```

The `mongod` outputs the following to `stdout` 
before terminating:

```yaml
config: mongod.conf
storage:
  dbPath: "/var/lib/mongo"
systemLog:
  destination: file
  path: "/var/log/mongodb/mongod.log"
net:
  port: 20128
outputConfig: true
```
