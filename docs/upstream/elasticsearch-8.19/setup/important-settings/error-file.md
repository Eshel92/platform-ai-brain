<!-- Converted from setup/important-settings/error-file.asciidoc (AsciiDoc). Includes are inlined. -->

#### JVM fatal error log setting

By default, Elasticsearch configures the JVM to write fatal error logs
to the default logging directory. On RPM and Debian packages,
this directory is `/var/log/elasticsearch`. On Linux and MacOS and Windows distributions, the `logs`
directory is located under the root of the Elasticsearch installation.

These are logs produced by the JVM when it encounters a fatal error, such as a
segmentation fault. If this path is not suitable for receiving logs,
modify the `-XX:ErrorFile=...` entry in `jvm.options`.
