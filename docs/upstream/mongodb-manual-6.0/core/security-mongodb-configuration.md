<!-- Converted from core/security-mongodb-configuration.txt (reStructuredText). Includes are inlined. -->

# IP Binding in Self-Managed Deployments

## Overview

MongoDB binaries, `mongod` and `mongos`, bind to
localhost by default. If the `net.ipv6` configuration file
setting or the `--ipv6` command line option is set for the binary,
the binary additionally binds to the localhost IPv6 address.

## Considerations

**Warning:**

Make sure that your `mongod` and `mongos`
instances are only accessible on trusted networks. If your system
has more than one network interface, bind MongoDB programs to the
private or internal network interface.

If the `net.ipv6` configuration file setting or the `--ipv6`
command line option is set for the binary, the binary additionally
binds to the localhost IPv6 address.

To bind to all IPv4 addresses, you can specify the bind ip address of
`0.0.0.0`. To bind to all IPv4 and IPv6 addresses, you can specify
the bind ip address of `::,0.0.0.0` or alternatively, use the new
`net.bindIpAll` setting or the new command-line option
`--bind_ip_all`.

**See also:**

- security-firewalls
- configuration-security
