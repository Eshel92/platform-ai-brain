<!-- Converted from setup/important-settings/heap-dump-path.asciidoc (AsciiDoc). Includes are inlined. -->

#### JVM heap dump path setting

By default, Elasticsearch configures the JVM to dump the heap on out of
memory exceptions to the default data directory. On RPM and
Debian packages, the data directory is `/var/lib/elasticsearch`. On
Linux and MacOS and Windows distributions,
the `data` directory is located under the root of the Elasticsearch installation.

If this path is not suitable for receiving heap dumps, modify the
`-XX:HeapDumpPath=...` entry in `jvm.options`:

* If you specify a directory, the JVM will generate a filename for the heap
dump based on the PID of the running instance.
* If you specify a fixed filename instead of a directory, the file must
not exist when the JVM needs to perform a heap dump on an out of memory
exception. Otherwise, the heap dump will fail.
