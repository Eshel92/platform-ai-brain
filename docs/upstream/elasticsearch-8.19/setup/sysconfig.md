<!-- Converted from setup/sysconfig.asciidoc (AsciiDoc). Includes are inlined. -->

## Important system configuration

Ideally, Elasticsearch should run alone on a server and use all of the
resources available to it. In order to do so, you need to configure your
operating system to allow the user running Elasticsearch to access more
resources than allowed by default.

The following settings *must* be considered before going to production:

* Configure system settings
* Disable swapping
* Increase file descriptors
* Ensure sufficient virtual memory
* Ensure sufficient threads
* JVM DNS cache settings
* Temporary directory not mounted with `noexec`
* TCP retransmission timeout

### Development mode vs production mode

By default, Elasticsearch assumes that you are working in development mode.
If any of the above settings are not configured correctly, a warning will be
written to the log file, but you will be able to start and run your
Elasticsearch node.

As soon as you configure a network setting like `network.host`, Elasticsearch
assumes that you are moving to production and will upgrade the above warnings
to exceptions. These exceptions will prevent your Elasticsearch node from
starting. This is an important safety measure to ensure that you will not
lose data because of a malconfigured server.

(See `setup/sysconfig/configuring.md`)
(See `setup/sysconfig/swap.md`)
(See `setup/sysconfig/file-descriptors.md`)
(See `setup/sysconfig/virtual-memory.md`)
(See `setup/sysconfig/threads.md`)
(See `setup/sysconfig/dns-cache.md`)
(See `setup/sysconfig/executable-jna-tmpdir.md`)
(See `setup/sysconfig/tcpretries.md`)
