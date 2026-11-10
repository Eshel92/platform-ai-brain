<!-- Converted from setup/sysconfig/threads.asciidoc (AsciiDoc). Includes are inlined. -->

### Number of threads

Elasticsearch uses a number of thread pools for different types of operations.
It is important that it is able to create new threads whenever needed. Make
sure that the number of threads that the Elasticsearch user can create is at
least 4096.

This can be done by setting `ulimit -u 4096` as root before
starting Elasticsearch, or by setting `nproc` to `4096` in
`/etc/security/limits.conf`.

The package distributions when run as services under `systemd` will configure
the number of threads for the Elasticsearch process automatically. No
additional configuration is required.
