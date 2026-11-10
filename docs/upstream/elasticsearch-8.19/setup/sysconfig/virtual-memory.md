<!-- Converted from setup/sysconfig/virtual-memory.asciidoc (AsciiDoc). Includes are inlined. -->

### Virtual memory

Elasticsearch uses a `mmapfs` directory by
default to store its indices. The default operating system limits on mmap
counts is likely to be too low, which might result in out of memory exceptions.

**Note:** If the operating system's default `vm.max_map_count` value is `1048576` or higher, no configuration change is necessary. If the default value is lower than `1048576`, configure the `vm.max_map_count` parameter to `1048576`.

On Linux, you can increase the limits by running the following command as
`root`:

```sh
sysctl -w vm.max_map_count=1048576
```

To set this value permanently, update the `vm.max_map_count` setting in
`/etc/sysctl.conf`. To verify after rebooting, run `sysctl vm.max_map_count`.

The RPM and Debian packages will configure this setting automatically. No
further configuration is required.

You can find out the current mmap count of a running Elasticsearch process
using the following command, where `$PID` is the process ID of the running
Elasticsearch process:
```sh
wc -l /proc/$PID/maps
```
