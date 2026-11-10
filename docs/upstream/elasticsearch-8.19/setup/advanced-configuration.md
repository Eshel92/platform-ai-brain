<!-- Converted from setup/advanced-configuration.asciidoc (AsciiDoc). Includes are inlined. -->

### Set JVM options

If needed, you can override the default JVM options by adding custom options
files (preferred) or setting the `ES_JAVA_OPTS` environment variable.

JVM options files must have the suffix '.options' and contain a line-delimited
list of JVM arguments. JVM processes options files in lexicographic order.

Where you put the JVM options files depends on the type of installation:

* tar.gz or .zip: Add custom JVM options files to `config/jvm.options.d/`.
* Debian or RPM: Add custom JVM options files to `/etc/elasticsearch/jvm.options.d/`.
* Docker: Bind mount custom JVM options files into
`/usr/share/elasticsearch/config/jvm.options.d/`.

**Caution:** Setting your own JVM options is generally not recommended and could negatively
impact performance and stability. Using the Elasticsearch-provided defaults
is recommended in most circumstances.

**Note:** Do not modify the root `jvm.options` file. Use files in `jvm.options.d/` instead.

#### JVM options syntax

A JVM options file contains a line-delimited list of JVM arguments.
Arguments are preceded by a dash (`-`).
To apply the setting to specific versions, prepend the version
or a range of versions followed by a colon.

* Apply a setting to all versions:
```text
-Xmx2g
```

* Apply a setting to a specific version:
```text
17:-Xmx2g
```

* Apply a setting to a range of versions:
```text
17-18:-Xmx2g
```
To apply a setting to a specific version and any later versions,
omit the upper bound of the range.
For example, this setting applies to Java 17 and later:
```text
17-:-Xmx2g
```

Blank lines are ignored. Lines beginning with `#` are treated as comments
and ignored. Lines that aren't commented out and aren't recognized
as valid JVM arguments are rejected and Elasticsearch will fail to start.

#### Use environment variables to set JVM options

In production, use JVM options files to override the
default settings. In testing and development environments,
you can also set JVM options through the `ES_JAVA_OPTS` environment variable.

```sh
export ES_JAVA_OPTS="$ES_JAVA_OPTS -Djava.io.tmpdir=/path/to/temp/dir"
./bin/elasticsearch
```

If you're using the RPM or Debian packages, you can specify
`ES_JAVA_OPTS` in the system configuration file.

**Note:** Elasticsearch ignores the `JAVA_TOOL_OPTIONS` and `JAVA_OPTS` environment variables.

#### Set the JVM heap size

By default, Elasticsearch automatically sets the JVM heap size based on a node's
roles and total memory.
Using the default sizing is recommended for most production environments.

To override the default heap size, set the minimum and maximum heap size
settings, `Xms` and `Xmx`. The minimum and maximum values must be the same.

The heap size should be based on the available RAM:

* Set `Xms` and `Xmx` to no more than 50% of your total memory. Elasticsearch requires
memory for purposes other than the JVM heap. For example, Elasticsearch uses
off-heap buffers for efficient network communication and relies
on the operating system's filesystem cache for
efficient access to files. The JVM itself also requires some memory. It's
normal for Elasticsearch to use more memory than the limit
configured with the `Xmx` setting.
**Note:** When running in a container, such as Docker, total memory is
defined as the amount of memory visible to the container, not the total system
memory on the host.

* Set `Xms` and `Xmx` to no more than the threshold for compressed ordinary
object pointers (oops). The exact threshold varies but 26GB is safe on most
systems and can be as large as 30GB on some systems. To verify you are under the
threshold, check the Elasticsearch log for an entry like this:
```txt
heap size [1.9gb], compressed ordinary object pointers [true]
```
Or check the `jvm.using_compressed_ordinary_object_pointers` value for the nodes using the nodes info API:
```console
GET _nodes/_all/jvm
```

The more heap available to Elasticsearch, the more memory it can use for its internal
caches. This leaves less memory for the operating system to use
for the filesystem cache. Larger heaps can also cause longer garbage
collection pauses.

To configure the heap size, add the `Xms` and `Xmx` JVM arguments to a
custom JVM options file with the extension `.options` and
store it in the `jvm.options.d/` directory.
For example, to set the maximum heap size to 2GB, set both `Xms` and `Xmx` to `2g`:

```txt
-Xms2g
-Xmx2g
```

For testing, you can also set the heap sizes using the `ES_JAVA_OPTS`
environment variable:

```sh
ES_JAVA_OPTS="-Xms2g -Xmx2g" ./bin/elasticsearch
```

The `ES_JAVA_OPTS` variable overrides all other JVM
options. We do not recommend using `ES_JAVA_OPTS` in production.

**Note:** If you are running Elasticsearch as a Windows service, you can change the heap size
using the service manager. See windows-service.

(See `setup/important-settings/heap-dump-path.md`)
(See `setup/important-settings/gc-logging.md`)
(See `setup/important-settings/error-file.md`)
